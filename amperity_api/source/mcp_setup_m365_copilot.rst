.. https://docs.amperity.com/api/mcp_setup_m365_copilot.html


.. meta::
    :description lang=en:
        Configure Copilot Studio to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Copilot Studio to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Copilot Studio


==================================================
Set up Copilot Studio
==================================================

.. mcp-setup-m365-copilot-start

Copilot Studio is the primary supported MCP client for Amperity. Once configured in Copilot Studio, the Amperity MCP server is available to any agent you build there, including agents you publish to the Microsoft 365 surface.

.. mcp-setup-m365-copilot-end


Before you begin
==================================================

You need:

* An active Amperity account with access to at least one tenant.
* Copilot Studio with permission to add custom connectors.
* The Amperity MCP endpoint: ``https://mcp.amperity.com``


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
        - ``https://mcp.amperity.com``

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


Tool surface limits
==================================================

Copilot Studio's orchestrator handles a maximum of 128 tools per agent, and Microsoft recommends limiting agents to 25-30 tools for best performance. The full Amperity MCP surface exposes more than 200 tools, so most agents will need to scope down. Two options:

* Use a persona-scoped MCP server. Amperity publishes split MCP servers that expose a smaller, role-scoped tool surface for clients with tool-count limits. Contact your Amperity representative for access.
* Restrict your agent to a subset of tools. On your agent's **Tools** tab, select the Amperity MCP server to open its settings page. Under the **Tools** section, turn off the **Allow all** toggle, then use the individual toggles to enable only the tools your agent needs. Note that any new tools added to the server are turned off by default once **Allow all** is off.


Verify the connection
==================================================

Open a chat in any M365 app where the agent is available. Ask the agent about your Amperity tenant:

   *"Tell me about my Amperity tenant."*

The agent should call the ``tenant_info`` tool and return details about your current Amperity tenant. If the agent reports an authorization error, sign out of the connector and reauthorize.


Troubleshooting
==================================================

For common errors -- 401 responses, missing tools, or session issues -- see :doc:`mcp_troubleshooting`.
