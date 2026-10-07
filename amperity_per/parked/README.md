# Parked articles

Articles in this directory are **written to publish standard and committed on the branch**, but
they are **outside the build**. Sphinx is pointed at `amperity_per/source`, never at this
directory, so nothing here is built, enters a toctree, reaches a search index, or is reachable
by URL. Both CircleCI and the GoCD deploy pipeline build `<collection>/source`, so this holds
for the published site by construction, not by configuration.

`:orphan:` is **not** parking — an orphan page still builds and still gets a URL.

Every file here begins with a marker naming the decision or open question that holds it, and
the condition that releases it:

    .. PENDING <D3 | NC-nnn>: <what has to change for this to ship>

## What is parked

Seven articles, each written to publish standard. **Each file's own `.. PENDING` line is the
authority** — this table summarises it so the directory can be read at a glance.

| Article | File | Ships when |
|---|---|---|
| Connect Databricks | `connect_databricks.rst` | **D3** — the Databricks connection is enabled for production tenants. Limited to one tenant at the pin. |
| Connect Pér as an MCP server | `connect_per_as_mcp_server.rst` | **NC-004** — the Pér MCP server is advertised to customers and a host address is published. The feature works at the pin; it is not being advertised. |
| Giving feedback | `giving_feedback.rst` | **NC-060** — sending feedback is judged essential to document. Parked on review, not on behaviour. |
| Linked accounts | `linked_accounts.rst` | **D3** — account linking is enabled for production tenants and a link changes what Pér does. At the pin a link is recorded and nothing reads it. |
| Notifications | `notifications.rst` | **NC-059** — notifications are mature enough to document. Parked on review, not on behaviour. |
| Scheduled tasks | `scheduled_tasks.rst` | **D3** — scheduled tasks are enabled for production tenants. Off for every production tenant at the pin. |
| Use-case feasibility | `use_case_feasibility.rst` | **D3** — use-case feasibility is enabled for production tenants. Limited to one family of tenants at the pin. |

Add a row when you park an article, and remove it when you publish one — step 6 below.

## Publishing a parked article

1. `git mv amperity_per/parked/<article>.rst amperity_per/source/<article>.rst`
2. Add its entry to the right toctree in `source/index.rst`
3. Delete its `.. PENDING` line
4. `grep -rn "PARKED-LINK: <article>.rst" amperity_per/source/` and add every link it names
5. Rebuild with `-W`
6. Remove its row from the table above

No configuration changes when an article moves in or out. That is why parking lives outside
`source/` rather than inside it behind an `exclude_patterns` entry — one stray edit to that
setting would publish every parked article at once.
