.. https://docs.amperity.com/api/


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

.. mcp-setup-copilot-start

Configure the Amperity MCP server in Copilot Studio, after which the Amperity MCP server is available to any agent built in Copilot Studio, including agents published to the Microsoft 365 surface.

.. mcp-setup-copilot-end


.. _mcp-setup-copilot-requirements:

Requirements
==================================================

.. mcp-setup-copilot-requirements-start

Connecting Copilot Studio to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* Access to Copilot Studio with permission to add custom connectors.
* The :ref:`URL for your tenant's MCP server endpoint <mcp-overview-mcp-urls>`.

.. mcp-setup-copilot-requirements-end


.. _mcp-setup-copilot-studio:

Copilot Studio
==================================================

.. mcp-setup-copilot-studio-start

Use the **Copilot Studio** MCP onboarding wizard to configure server details and to configure OAuth.

.. mcp-setup-copilot-studio-end

.. mcp-setup-copilot-studio-steps-start

#. Open **Copilot Studio**.
#. In **Copilot Studio**, open an agent.
#. Go to the **Tools** page, select **Add a tool**, and then **New tool**.
#. Select **Model Context Protocol**. The MCP onboarding wizard appears.
#. Fill in the following fields:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Field
        - Value
      * - **Server name**
        - "Amperity" or any name your team prefers
      * - **Server description**
        - A short description of what the is connector for. The agent orchestrator uses this text to decide when to call Amperity at runtime.
      * - **Server URL**
        - **https://mcp.amperity.com**

          .. important:: Use the :ref:`correct MCP server URL <mcp-overview-mcp-urls>` in the command.

#. Under **Authentication**, select **OAuth 2.0**.

   Choose the **Manual** type and fill in the following fields.

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Field
        - Value
      * - **Client ID**
        - **nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs**
      * - **Client secret**
        - Any non-empty placeholder, for example "unused". The Amperity MCP server is a PKCE-based public OAuth client and ignores this value, but **Copilot Studio** requires the field to be non-empty.
      * - **Authorization URL**
        - **https://mcp.amperity.com/authorize**
      * - **Token URL template**
        - **https://mcp.amperity.com/oauth/token**
      * - **Refresh URL**
        - **https://mcp.amperity.com/oauth/token**

   .. important:: Use the :ref:`correct MCP server URL <mcp-overview-mcp-urls>` in the command, and then append **/authorize** and **/oauth/token** to that URL for the **Authorization URL**, **Token URL template**, and **Refresh URL** values.

#. Select **Create**. **Copilot Studio** displays a callback URL. The Amperity OAuth proxy registers the callback URL dynamically.

#. Select **Next** to continue. On the **Add tool** dialog, choose **Create a new connection** and sign in with your Amperity credentials.
#. Select **Add to agent**.

.. mcp-setup-copilot-studio-steps-end


.. _mcp-setup-copilot-surface-limits:

Tool surface limits
==================================================

.. mcp-setup-copilot-surface-limits-start

Copilot Studio limits the number of tools an agent can register. The full Amperity MCP surface exposes more than 200 tools, so most agents will need to scope down the number of tools. There are two options:

#. Use a persona-scoped MCP server. Amperity publishes split MCP servers that expose a smaller, role-scoped tool surface for clients with tool-count limits. Contact your Amperity representative for access.

#. Restrict your agent to a subset of tools. On your agent's **Tools** tab, select the Amperity MCP server to open its settings page. Under the **Tools** section, turn off the **Allow all** toggle, and then use the individual toggles to enable only the tools your agent needs.

   .. important:: Tools added to the Amperity MCP server are turned off by default when **Allow all** is disabled.

.. mcp-setup-copilot-surface-limits-end


.. _mcp-setup-copilot-interacting:

Start interacting with Copilot
==================================================

.. mcp-setup-copilot-interacting-start

Open a chat in any Microsoft 365 application in which an agent with access to the Amperity MCP server is configured. Ask the agent about your Amperity tenant:

.. code-block:: none

   "Tell me about my Amperity tenant."

The agent calls the **tenant_info** tool and return details about your current Amperity tenant.

.. tip:: If the agent returns an authorization error, sign out, and then reauthorize the connector.

.. mcp-setup-copilot-interacting-end
