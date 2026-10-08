# Working in amperity-docs

Source for https://docs.amperity.com, built with Sphinx from reStructuredText.
Style, terminology, and reST formatting rules are in `CONTRIBUTING.md` and the
`contributing/source/` pages; follow them for any content you write.


## Start the dev server before editing

Start the dev server at the beginning of a session that changes docs content, and
leave it running. It rebuilds what you change and reloads the browser, so the
person you are working with sees each edit within seconds:

```bash
make dev                              # http://localhost:8765
python3 tools/dev-server.py --port 9000 # another port
python3 tools/dev-server.py --build-all # rewrite every page first
```

On start it brings every section up to date, then watches. Run it in the
background, from the repository root, with the Python environment
that has the packages in `requirements.txt` (see `contributing/source/setup.rst`).
If it is already running, do not start a second copy; check with
`curl -s localhost:8765/__livereload`.

Tell the person the URL of the page you are editing, for example
`http://localhost:8765/operator/api_profile.html`. Each section is served under
the folder its Makefile target builds to (`amperity_operator` -> `/operator/`,
`amperity_api` -> `/api/`, `amperity_base` -> `/`).

What a save rebuilds:

| You change | The dev server |
|---|---|
| A page in a section | Rebuilds that section, and any section that includes the page |
| A page with a `toctree` (it defines navigation) | Rewrites every page in its section |
| A file in `shared/` or `images/` | Rebuilds the sections that reference it |
| A file in `tokens/` | Rewrites every page in every section |
| A `conf.py`, template, or `_static` file | Rebuilds that section from scratch |
| A file in `downloads/` | Copies it into the build |

The dev server prints warnings but does not stop on them. Read its output after
each save: a `WARNING` or `FAILED` line is something to fix, because the real
build treats warnings as errors.


## Before you open a pull request

Run the build the way CI does, with warnings as errors:

```bash
make all
```

Fix every warning it reports. Do not commit `build/`.


## How the repository is organized

| Folder | Published at | What it holds |
|---|---|---|
| `amperity_base` | `/` | Site home page |
| `amperity_user` | `/user` | Guides for marketers and analysts |
| `amperity_operator` | `/operator` | Guides for configuring a tenant |
| `amperity_guides` | `/guides` | Guided setup |
| `amperity_reference` | `/reference` | Concepts, explained once and included elsewhere |
| `amperity_api` | `/api` | API overview and authentication |
| `amperity_help` | `/tooltips` | In-app tooltips, not browsed on the site |
| `amperity_modals` | `/modals` | In-app destination setup panels; file names must match plugin IDs |
| `legions` | `/legions` | Small pages for LLMs, built from includes |
| `legacy` | `/legacy` | Pages kept for older setups |
| `shared/` | not published | Reusable text, included by other pages |
| `tokens/` | not published | Substitutions every section loads, such as product names and links |

Content is written once and included where it is needed:

```rst
.. include:: ../../shared/terms.rst
   :start-after: .. term-event-stream-start
   :end-before: .. term-event-stream-end
```

An include starts after the first line that matches `:start-after:`, so never
repeat a chunk's marker text anywhere else in the file, including in comments.
Before you rename or delete a page, a label, or a chunk marker, search the whole
repository for it: other sections may include or link to it.
