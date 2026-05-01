.. https://docs.amperity.com/api/mcp_troubleshooting.html


.. meta::
    :description lang=en:
        Common issues and resolutions when connecting to and using the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Common issues and resolutions when connecting to and using the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        MCP troubleshooting


==================================================
MCP troubleshooting
==================================================

.. mcp-troubleshooting-start

Common issues you may encounter when connecting to or using the Amperity MCP server, and how to resolve them.

.. mcp-troubleshooting-end


401 Unauthorized
==================================================

The MCP server returns a 401 with a body like:

::

   {"error": "unauthorized", "detail": "Missing or malformed Authorization header"}

or:

::

   {"error": "unauthorized", "detail": "Invalid token: ..."}

The most common cause is an expired access token. Most MCP clients refresh automatically; if yours does not, sign out of the connector and sign back in.

If 401 responses persist after a fresh sign-in:

* Confirm that the user account exists in the target tenant and that the user has not been removed.
* Confirm the client is signing in to the correct identity provider. The MCP server authenticates against ``https://amperity.auth0.com/`` -- if your client is configured to point at a different issuer, fix the configuration and reconnect.


Tool returns ``isError: true``
==================================================

When an individual tool call fails, the MCP server returns a result of the form:

::

   {"isError": true, "error": "<message>"}

The agent typically surfaces the message in the chat. Common causes:

* **Missing permissions on the tenant.** Your account does not have the role required for the tool. Check the user's permissions in the Amperity tenant settings.
* **Missing or invalid arguments.** The agent supplied a value that the underlying API rejected. Re-run with the corrected argument, or ask the agent to inspect the tool's input schema with ``tools/list``.
* **Stale references.** The agent referenced an ID (campaign, query, table) that has since been deleted or renamed. Re-list the parent resource and try again.

If the same tool fails repeatedly with the same error, share the exact error text with your Amperity representative.


No tenant selected
==================================================

A new MCP session begins without a tenant selected. Tools that operate on tenant data return:

::

   No tenant selected. Use tenant_list to see available tenants, then tenant_use to select one.

Ask your agent to list tenants and pick one:

   *"List my Amperity tenants, then use ``acme``."*

The selected tenant persists for the remainder of the session.


Tenant or sandbox missing from ``tenant_list``
==================================================

Tenants are cached server-side per token. When a new sandbox or tenant is provisioned, the cache may not reflect it immediately. Ask the agent to refresh:

   *"Resync my Amperity tenants."*

The agent calls ``tenant_resync``, which clears the cache and re-fetches tenants from the API. The new tenant should appear on the next ``tenant_list``.


Write operation refused
==================================================

If a write tool fails with a safety error, the session safety mode is blocking the call. The default is ``strict``, which restricts writes to sandbox tenants. To write to a production tenant, switch the session to ``confirm`` (writes require an explicit ``confirm: true`` argument from the agent) or ``unrestricted``. See :doc:`mcp_safety_modes`.

For external send operations -- ``campaign_schedule`` and ``orchestration_group_run`` -- the safety mode must be ``unrestricted`` and the agent must pass ``confirm: true``. These two requirements are independent of the safety mode for other writes.


Tools missing or truncated
==================================================

Some MCP clients limit the number of tools that can be registered per agent or chat -- Copilot Studio is one. The full Amperity tool surface is more than 200 tools.

Workarounds:

* Use a persona-scoped MCP server. Amperity publishes split MCP servers that expose smaller, role-scoped tool surfaces. Contact your Amperity representative for access.
* Restrict your client to a subset of tools by using the client's tool selection controls.

If a specific tool you expect to see is missing entirely (rather than truncated), ask your agent to call ``tools/list`` and check whether the tool appears. If it does not, your account may not have permission to use it on the current tenant.


Connection failures
==================================================

The MCP server is hosted at ``https://mcp.amperity.com``. Confirm that your network allows outbound HTTPS to that hostname.


Still stuck?
==================================================

Contact your Amperity representative with:

* The MCP client and version you are using.
* The exact error text or status code (the JSON ``detail`` or ``error`` field is most useful).
* The approximate time the error occurred (UTC), so we can correlate with server logs.
