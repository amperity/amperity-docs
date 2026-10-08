# Parked articles

Articles in this directory are **written to publish standard and committed on the branch**, but
they are **outside the build**. Sphinx is pointed at `amperity_per/source`, never at this
directory, so nothing here is built, enters a toctree, reaches a search index, or is reachable
by URL. Both CircleCI and the GoCD deploy pipeline build `<collection>/source`, so this holds
for the published site by construction, not by configuration.

`:orphan:` is **not** parking — an orphan page still builds and still gets a URL.

Every file here begins with:

    .. PENDING D3: <what has to change for this to ship>

## Publishing a parked article

1. `git mv amperity_per/parked/<article>.rst amperity_per/source/<article>.rst`
2. Add its entry to the right toctree in `source/index.rst`
3. Delete the `.. PENDING D3:` line
4. `grep -rn "PARKED-LINK: <article>.rst" amperity_per/source/` and add every link it names
5. Rebuild with `-W`

No configuration changes when an article moves in or out. That is why parking lives outside
`source/` rather than inside it behind an `exclude_patterns` entry — one stray edit to that
setting would publish every parked article at once.
