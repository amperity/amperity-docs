.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Configure GitHub Copilot in VS Code or Copilot Studio to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure GitHub Copilot in VS Code or Copilot Studio to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Microsoft Copilot


==================================================
Set up Microsoft Copilot
==================================================

.. mcp-setup-copilot-page-start

Connect Microsoft's Copilot products to the Amperity MCP server and sign in with your Amperity credentials. This page covers two clients:

* :ref:`VS Code <mcp-setup-vscode>` -- GitHub Copilot in agent mode.
* :ref:`Copilot Studio <mcp-setup-copilot-studio-section>` -- the agent builder for Microsoft 365.

.. important:: These are separate Microsoft products and they receive different tool surfaces. VS Code receives the full tool surface; Copilot Studio receives a curated subset of tools because it limits how many tools an agent can register. See :ref:`Tool surface <mcp-setup-vscode-surface>` and :ref:`Tool surface limits <mcp-setup-copilot-surface-limits>`.

.. mcp-setup-copilot-page-end


.. _mcp-setup-vscode:

VS Code
==================================================

.. mcp-setup-vscode-start

Configure the Amperity MCP server in VS Code, after which the Amperity tools are available to GitHub Copilot in agent mode.

.. mcp-setup-vscode-end


.. _mcp-setup-vscode-requirements:

Requirements
--------------------------------------------------

.. mcp-setup-vscode-requirements-start

Connecting VS Code to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* GitHub Copilot, signed in with an account that has an active Copilot subscription. Agent mode is required; Copilot code completion alone cannot call MCP tools.

.. mcp-setup-vscode-requirements-end


.. _mcp-setup-vscode-add:

Add the Amperity MCP server
--------------------------------------------------

.. mcp-setup-vscode-add-start

Add the Amperity server to your MCP configuration file. Use the user-level file to make Amperity available in every workspace, or the workspace-level file to limit it to one project.

.. mcp-setup-vscode-add-end

.. mcp-setup-vscode-add-steps-start

#. Open the MCP configuration file.

   * For all workspaces, open the **Command Palette**, and then run **MCP: Open User Configuration**.
   * For a single workspace, create ``.vscode/mcp.json`` in the project folder.

#. Add the ``amperity`` server:

   .. code-block:: json

      {
        "servers": {
          "amperity": {
            "type": "http",
            "url": "https://mcp.amperity.com"
          }
        }
      }

#. Save the file. VS Code detects the new server automatically.

#. Open the **Command Palette**, run **MCP: List Servers**, select **amperity**, and then select **Start**.

#. A browser window opens. Sign in with your Amperity credentials, and then select the tenant you want to work with.

.. note:: VS Code discovers Amperity's OAuth settings automatically, so no client ID or secret is required.

.. mcp-setup-vscode-add-steps-end


.. _mcp-setup-vscode-surface:

Tool surface
--------------------------------------------------

.. mcp-setup-vscode-surface-start

VS Code receives the full Amperity tool surface, which exposes more than 200 tools. Unlike Copilot Studio, VS Code does not cap the number of tools a server can register, so no curated subset is served. Instead, you choose which tools to send to the model.

To narrow the surface, open a Copilot Chat session in agent mode, select the tools icon, and then clear the tools you do not need. Expand the **amperity** group to toggle Amperity tools individually. Selections apply to every chat session that uses the default agent.

.. tip:: A smaller, well-chosen tool set usually produces better results than the full surface, because the model has fewer similar options to choose between.

.. mcp-setup-vscode-surface-end


.. _mcp-setup-vscode-interacting:

Start interacting with Copilot in VS Code
--------------------------------------------------

.. mcp-setup-vscode-interacting-start

Open Copilot Chat, set the mode to **Agent**, and then ask about your Amperity tenant:

.. code-block:: none

   "Tell me about my Amperity tenant."

Copilot calls the **tenant_info** tool and returns details about your current Amperity tenant. To work with a different tenant, ask Copilot to switch:

.. code-block:: none

   "Switch to the acme2 tenant."

.. tip:: If Copilot returns an authorization error, run **MCP: List Servers**, select **amperity**, and then select **Start** to reauthorize.

.. mcp-setup-vscode-interacting-end


.. _mcp-setup-copilot-studio-section:

Copilot Studio
==================================================

.. mcp-setup-copilot-start

Configure the Amperity MCP server in Copilot Studio, after which the Amperity MCP server is available to any agent built in Copilot Studio, including agents published to the Microsoft 365 surface.

.. mcp-setup-copilot-end


.. _mcp-setup-copilot-requirements:

Requirements
--------------------------------------------------

.. mcp-setup-copilot-requirements-start

Connecting Copilot Studio to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* Access to Copilot Studio with permission to add custom connectors.

.. mcp-setup-copilot-requirements-end


.. _mcp-setup-copilot-studio:

Add the Amperity MCP server
--------------------------------------------------

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
        - A short description of what the connector is for. The agent orchestrator uses this text to decide when to call Amperity at runtime.
      * - **Server URL**
        - **https://mcp.amperity.com**

#. Under **Authentication**, select **OAuth 2.0**, and then choose the **Dynamic discovery** type.

#. Select **Create**, and then **Next** to continue. On the **Add tool** dialog, choose **Create a new connection** and sign in with your Amperity credentials.
#. Select **Add to agent**.

.. mcp-setup-copilot-studio-steps-end


.. _mcp-setup-copilot-surface-limits:

Tool surface limits
--------------------------------------------------

.. mcp-setup-copilot-surface-limits-start

Copilot Studio limits the number of tools an agent can register. The full Amperity MCP surface exposes more than 200 tools, which exceeds this limit.

To stay within the limit, the Amperity MCP server automatically detects Copilot Studio connections and serves a curated subset of tools sized to fit within Copilot Studio's connector tool limit. No manual configuration is required--connect Copilot Studio by following the steps above, and your agent receives the curated tool set automatically.

.. note:: This curated subset is specific to Copilot Studio. It is the server's response to Copilot Studio's connector tool limit, and it does not apply to other clients. In particular, :ref:`VS Code <mcp-setup-vscode>` receives the full tool surface, so a tool available to Copilot in VS Code may not be available to a Copilot Studio agent.

To narrow the surface further, restrict your agent to a smaller subset of tools. On your agent's **Tools** tab, select the Amperity MCP server to open its settings page. Under the **Tools** section, turn off the **Allow all** toggle, and then use the individual toggles to enable only the tools your agent needs.

.. important:: Tools added to the Amperity MCP server are turned off by default when **Allow all** is disabled.

.. mcp-setup-copilot-surface-limits-end


.. _mcp-setup-copilot-interacting:

Start interacting with Copilot
--------------------------------------------------

.. mcp-setup-copilot-interacting-start

Open a chat in any Microsoft 365 application in which an agent with access to the Amperity MCP server is configured. Ask the agent about your Amperity tenant:

.. code-block:: none

   "Tell me about my Amperity tenant."

The agent calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. tip:: If the agent returns an authorization error, sign out, and then reauthorize the connector.

.. mcp-setup-copilot-interacting-end
