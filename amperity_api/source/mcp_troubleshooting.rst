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

The most common cause is an expired access token. Most MCP clients refresh automatically; if yours does not, sign out of the connector and sign back in.

If 401 responses persist after a fresh sign-in:

* Confirm that the user account exists in the target tenant.
* Confirm that you are signing in to the correct identity provider. The MCP server uses ``https://amperity.auth0.com/`` as the issuer.
* If your client lets you inspect the access token, confirm it has three segments separated by periods (a JWS-signed JWT). If your token has five segments (a JWE), contact your Amperity representative.


Tools missing or truncated
==================================================

Some MCP clients limit the number of tools that can be registered per agent or chat. Copilot Studio, for example, allows up to 70 tools per agent. The full Amperity tool surface is more than 200 tools.

Workarounds:

* Use a persona-scoped MCP server. Amperity publishes split MCP servers that expose smaller, role-scoped tool surfaces. Contact your Amperity representative for access.
* Restrict your client to a subset of tools by using the client's tool selection controls.

If a specific tool you expect to see is missing, ask your agent to call ``tools/list`` and check whether it appears. If it does not, your account may not have permission to use it on the current tenant.


No tenant selected
==================================================

A new MCP session begins without a tenant selected. If a tool that requires a tenant fails with a "no tenant selected" error, ask your agent to list and select a tenant:

   *"List my Amperity tenants, then use ``acme``."*

The agent calls ``tenant_list`` followed by ``tenant_use``. The selected tenant persists for the remainder of the session.


Write operation refused
==================================================

If a write tool fails with a safety error, the session safety mode is blocking the call. See :doc:`mcp_safety_modes` for the list of modes and how to change them. The default ``confirm`` mode requires an explicit ``confirm: true`` argument from the agent for writes against production tenants.


Connection failures or timeouts
==================================================

The MCP server is hosted at ``https://mcp.amperity.com``. Confirm that your network allows outbound HTTPS to that hostname. If your client supports it, send a request directly to the OAuth discovery document to verify connectivity:

::

   curl https://mcp.amperity.com/.well-known/oauth-authorization-server

A successful response returns a JSON document with the authorization server metadata.


Still stuck?
==================================================

Contact your Amperity representative with:

* The MCP client and version you are using.
* The exact error text or status code.
* The approximate time the error occurred (UTC), so we can correlate with server logs.
