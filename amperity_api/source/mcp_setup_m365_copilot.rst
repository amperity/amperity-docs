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

The Copilot Studio MCP onboarding wizard collects the connection details and the OAuth configuration in two steps.

Configure server details
--------------------------------------------------

1. In Copilot Studio, open the agent you want to extend.
2. Go to the **Tools** page, then select **Add a tool** > **New tool**.
3. Select **Model Context Protocol**. The MCP onboarding wizard appears.
4. Fill in the basic server fields:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Field
        - Value
      * - Server name
        - ``Amperity`` (or any name your team prefers)
      * - Server description
        - A short description of what your team uses the connector for. The agent orchestrator uses this text to decide when to call Amperity at runtime.
      * - Server URL
        - ``https://mcp.amperity.com/mcp``

5. Under **Authentication**, select **OAuth 2.0**.

Configure OAuth 2.0 (Manual)
--------------------------------------------------

After you select **OAuth 2.0**, choose the **Manual** type and fill in the following fields. Field order matches the Copilot Studio UI.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Value
   * - Client ID
     - ``nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs``
   * - Client secret
     - *(see note below)*
   * - Authorization URL
     - ``https://mcp.amperity.com/authorize``
   * - Token URL template
     - ``https://mcp.amperity.com/oauth/token``
   * - Refresh URL
     - ``https://mcp.amperity.com/oauth/token``
   * - Scopes
     - *(leave empty)*

.. note::

   The Amperity MCP server is a PKCE-based public OAuth client and does not issue a client secret. If the Copilot Studio UI requires a non-empty value for **Client secret**, contact your Amperity representative for guidance.

After you select **Create**, Copilot Studio displays a callback URL. Copy this URL -- you (or your Amperity representative) need to register it as a valid redirect URI on the Amperity OAuth client before the connection can complete.

Select **Next** to continue. On the **Add tool** dialog, choose **Create a new connection** and sign in with your Amperity credentials. Then select **Add to agent**.

Alternative: Dynamic discovery
--------------------------------------------------

The Amperity MCP server also publishes OAuth discovery metadata and supports Dynamic Client Registration. If your environment allows it, choose **OAuth 2.0** > **Dynamic discovery** instead of **Manual**. In that mode, Copilot Studio reads the configuration from ``https://mcp.amperity.com/.well-known/oauth-authorization-server`` automatically and you do not need to enter any of the fields above. Use **Manual** when you need an explicit, repeatable configuration -- for example, when distributing setup steps to many users.


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
