#!/usr/bin/env python3
"""Serve the docs locally, rebuild what changed on save, and reload the browser.

Usage (from the repository root, inside the Python environment that has Sphinx):

    python3 tools/dev-server.py            # serve on http://localhost:8765
    python3 tools/dev-server.py --port 9000
    python3 tools/dev-server.py --build-all    # rewrite every page first
    python3 tools/dev-server.py --host 0.0.0.0 # reachable from other machines

On start, every section gets an incremental build, which is quick when little has
changed and catches edits made while the server was stopped or a branch switch.
After that, each saved file triggers the smallest rebuild that covers it:

* A page in a section rebuilds that section, plus every other section that
  includes the page.
* A file in shared/ or images/ rebuilds the sections that reference it.
* A file in tokens/ rebuilds every section, because every section's conf.py
  includes the tokens.
* A page that holds a toctree rewrites every page in its section, because the
  toctree is the left-hand navigation that every page renders.
* A conf.py, template, or _static file rebuilds that section from scratch, since
  Sphinx does not always pick those up incrementally.
* A file in downloads/ is copied into the build; nothing is rebuilt.

Pages open with a small script that reloads the browser after each rebuild, and
nothing is cached, so a save shows up without a manual refresh.

The sections and their output folders come from the Makefile's build targets,
so a new section is picked up without changing this script. Uses only the Python
standard library.
"""

import argparse
import functools
import http.server
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
POLL_SECONDS = 0.5
SETTLE_SECONDS = 0.4
WATCHED_SUFFIXES = {".rst", ".py", ".html", ".txt", ".css", ".js", ".json", ".png", ".jpg",
                    ".jpeg", ".gif", ".svg", ".csv", ".md", ".xml", ".sql", ".pdf"}
# Includes bin/ and lib/ because the docs Python environment is often created at the
# repository root (see .gitignore); scanning it would be slow and is never needed.
SKIP_DIRS = {".git", "build", "_build", "__pycache__", "node_modules", ".venv", "venv", "bin", "lib", "include"}

# Bumped after every rebuild; the browser polls it to know when to reload.
build_generation = 0
generation_lock = threading.Lock()

LIVERELOAD_SNIPPET = b"""
<script>
(function () {
  var seen = null;
  function poll() {
    fetch("/__livereload", {cache: "no-store"})
      .then(function (r) { return r.text(); })
      .then(function (g) {
        if (seen !== null && g !== seen) { location.reload(); return; }
        seen = g;
        setTimeout(poll, 700);
      })
      .catch(function () { setTimeout(poll, 2000); });
  }
  poll();
})();
</script>
"""


def log(message):
    print(f"[{time.strftime('%H:%M:%S')}] {message}", flush=True)


def read_sections():
    """Map each section's source folder to its output folder, from the Makefile."""
    sections = {}
    for line in (ROOT / "Makefile").read_text().splitlines():
        m = re.search(r"\$\(BUILD_COMMAND\)\s+(\S+)/source\s+\$\(BUILDDIR\)/?(\S*)", line)
        if m:
            sections[m.group(1)] = m.group(2)
    return sections


def snapshot():
    """Modification times of every watched file under the repository."""
    mtimes = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if Path(name).suffix.lower() in WATCHED_SUFFIXES:
                path = os.path.join(dirpath, name)
                try:
                    mtimes[path] = os.stat(path).st_mtime_ns
                except FileNotFoundError:
                    pass
    return mtimes


def changed_paths(before, after):
    return sorted({p for p in after if before.get(p) != after[p]} | {p for p in before if p not in after})


def sections_referencing(fragment, sections):
    """Sections whose sources mention `fragment`, such as an included file's path or an image name."""
    found = set()
    for section in sections:
        for dirpath, dirnames, filenames in os.walk(ROOT / section / "source"):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for name in filenames:
                if not name.endswith((".rst", ".html", ".py", ".txt")):
                    continue
                try:
                    if fragment in Path(dirpath, name).read_text(errors="ignore"):
                        found.add(section)
                        break
                except OSError:
                    pass
            if section in found:
                break
    return found


def plan(paths, sections):
    """Work out which sections to rebuild, which to rebuild from scratch, and which downloads to copy."""
    rebuild, clean, rewrite, downloads = set(), set(), set(), set()
    for path in paths:
        rel = Path(path).relative_to(ROOT)
        top = rel.parts[0]
        rel_posix = rel.as_posix()
        if top == "downloads":
            downloads.add(rel)
        elif top == "tokens":
            rebuild.update(sections)
            rewrite.update(sections)
        elif top in ("shared", "images"):
            fragment = rel_posix if top == "shared" else rel.name
            rebuild.update(sections_referencing(fragment, sections))
        elif top in sections:
            rebuild.add(top)
            if rel.name == "conf.py" or {"_static", "_templates"} & set(rel.parts):
                clean.add(top)
            elif rel.suffix == ".rst":
                # A toctree change alters the navigation on every page of the section,
                # but Sphinx only rewrites the pages whose own source changed.
                try:
                    if ".. toctree::" in Path(path).read_text(errors="ignore"):
                        rewrite.add(top)
                except OSError:
                    pass
                # Other sections may include this page.
                rebuild.update(sections_referencing(rel_posix, sections))
    return rebuild, clean, rewrite, downloads


def copy_downloads(rels, quiet=False):
    for rel in rels:
        src, dest = ROOT / rel, BUILD / rel
        if src.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            if not quiet:
                log(f"copied {rel}")
        elif dest.exists():
            dest.unlink()
            log(f"removed {rel}")


def build(section, out, clean=False, rewrite=False):
    """Build one section with Sphinx. Warnings are shown but do not stop the build."""
    target = BUILD / out if out else BUILD
    if clean:
        # The base section builds into build/ itself, so only clear its Sphinx cache.
        shutil.rmtree(target / ".doctrees" if not out else target, ignore_errors=True)
    started = time.time()
    mode = " (clean)" if clean else " (all pages)" if rewrite else ""
    log(f"building {section} -> build/{out}{mode}")
    result = subprocess.run(
        [sys.executable, "-m", "sphinx", "-b", "html", "--jobs", "auto", "-q"]
        + (["-a"] if rewrite else [])
        + [f"{section}/source", str(target)],
        cwd=ROOT, capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    if output:
        print(output, flush=True)
    status = "built" if result.returncode == 0 else f"FAILED (exit {result.returncode})"
    log(f"{status} {section} in {time.time() - started:.1f}s")
    return result.returncode == 0


def bump_generation():
    global build_generation
    with generation_lock:
        build_generation += 1


class Handler(http.server.SimpleHTTPRequestHandler):
    """Static file server that disables caching and adds the reload script to pages."""

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def do_GET(self):
        if self.path.startswith("/__livereload"):
            body = str(build_generation).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        path = Path(self.translate_path(self.path))
        if path.is_dir():
            path = path / "index.html"
        if path.suffix == ".html" and path.is_file():
            html = path.read_bytes()
            html = html.replace(b"</body>", LIVERELOAD_SNIPPET + b"</body>", 1) if b"</body>" in html else html + LIVERELOAD_SNIPPET
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
            return
        super().do_GET()

    def log_message(self, *args):
        pass


def serve(host, port):
    BUILD.mkdir(exist_ok=True)
    server = http.server.ThreadingHTTPServer((host, port), functools.partial(Handler, directory=str(BUILD)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    log(f"serving http://{'localhost' if host in ('127.0.0.1', '') else host}:{port}/")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--host", default="127.0.0.1",
                        help="address to listen on; 127.0.0.1 keeps the server on this machine")
    parser.add_argument("--build-all", action="store_true", help="rebuild every section before watching")
    args = parser.parse_args()

    try:
        import sphinx  # noqa: F401
    except ImportError:
        sys.exit("Sphinx is not installed for this Python. Activate the docs environment first "
                 "(see contributing/source/setup.rst).")

    sections = read_sections()
    copy_downloads([p.relative_to(ROOT) for p in (ROOT / "downloads").rglob("*") if p.is_file()], quiet=True)
    for section, out in sections.items():
        build(section, out, rewrite=args.build_all)
    serve(args.host, args.port)
    log("watching for changes (Ctrl+C to stop)")

    before = snapshot()
    try:
        while True:
            time.sleep(POLL_SECONDS)
            after = snapshot()
            paths = changed_paths(before, after)
            if not paths:
                continue
            # Let a burst of saves (an editor's save-all, a git checkout) settle first.
            time.sleep(SETTLE_SECONDS)
            after = snapshot()
            paths = changed_paths(before, after)
            before = after
            for p in paths[:5]:
                log(f"changed {Path(p).relative_to(ROOT)}")
            if len(paths) > 5:
                log(f"... and {len(paths) - 5} more")
            rebuild, clean, rewrite, downloads = plan(paths, sections)
            copy_downloads(downloads)
            for section in sorted(rebuild):
                build(section, sections[section], clean=section in clean, rewrite=section in rewrite)
            if rebuild or downloads:
                bump_generation()
            # Builds write only to build/, which is not watched, so anything saved
            # while a build ran still differs from `before` and is picked up next.
    except KeyboardInterrupt:
        log("stopped")


if __name__ == "__main__":
    main()
