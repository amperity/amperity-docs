.. https://docs.amperity.com/api/mcp_setup_m365_copilot.html


.. meta::
    :description lang=en:
        Configure Microsoft 365 Copilot Studio to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Microsoft 365 Copilot Studio to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Microsoft 365 Copilot


==================================================
Set up Microsoft 365 Copilot
==================================================

.. mcp-setup-m365-copilot-start

Microsoft 365 Copilot is the primary supported MCP client for Amperity. Once configured in Copilot Studio, the Amperity MCP server is available across the M365 surface, including Word, Excel, Teams, and Outlook.

.. mcp-setup-m365-copilot-end


Before you begin
==================================================

You need:

* An active Amperity account with access to at least one tenant.
* Microsoft 365 Copilot Studio with permission to add custom connectors.
* The Amperity MCP endpoint: ``https://mcp.amperity.com/mcp``


Add the Amperity MCP server in Copilot Studio
==================================================

1. In Copilot Studio, open the agent you want to extend.
2. Add a new connector and choose **Model Context Protocol** as the connector type.
3. Set the server URL:

   ::

      https://mcp.amperity.com/mcp

4. Set the authentication type to **OAuth 2.0** with **PKCE**.

5. When Copilot Studio prompts you to authorize, sign in with your Amperity credentials.

6. Save the connector and add it to your agent's available tools.


Tool surface limits
==================================================

Microsoft 365 Copilot supports up to 70 tools per agent. The full Amperity MCP surface exposes more than 200 tools. If your agent fails to register all tools, you have two options:

* Use a persona-scoped MCP server. Amperity publishes split MCP servers that expose a smaller, role-scoped tool surface for clients with tool-count limits. Contact your Amperity representative for access.
* Restrict your agent to a subset of tools by using Copilot Studio's tool selection controls.


Verify the connection
==================================================

Open a chat in any M365 app where the agent is available. Ask the agent to list its available Amperity tenants:

   *"List my Amperity tenants."*

The agent should call the ``tenant_list`` tool and return your tenants. If the agent reports an authorization error, sign out of the connector and reauthorize.


Troubleshooting
==================================================

For common errors -- 401 responses, missing tools, or session issues -- see :doc:`mcp_troubleshooting`.
