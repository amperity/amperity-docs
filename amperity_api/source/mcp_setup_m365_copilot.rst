.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Configure GitHub Copilot in VS Code, GitHub Copilot CLI, Copilot Studio, or Microsoft Foundry to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure GitHub Copilot in VS Code, GitHub Copilot CLI, Copilot Studio, or Microsoft Foundry to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Microsoft Copilot and Foundry


==================================================
Set up Microsoft Copilot and Foundry
==================================================

.. mcp-setup-copilot-page-start

Connect Microsoft's agent products to the Amperity MCP server and sign in with your Amperity credentials. This page covers four clients:

* :ref:`VS Code <mcp-setup-vscode>` -- GitHub Copilot in agent mode.
* :ref:`GitHub Copilot CLI <mcp-setup-copilot-cli>` -- the terminal agent.
* :ref:`Copilot Studio <mcp-setup-copilot-studio-section>` -- the agent builder for Microsoft 365.
* :ref:`Microsoft Foundry <mcp-setup-foundry>` -- Foundry Agent Service.

.. important:: These are separate Microsoft products and they receive different tool surfaces. VS Code and GitHub Copilot CLI receive the full tool surface. Copilot Studio and Microsoft Foundry receive a curated subset of tools--see :ref:`Tool surface limits <mcp-setup-copilot-surface-limits>`.

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
* GitHub Copilot, signed in with an account that has an active Copilot subscription. Agent mode is required.

.. mcp-setup-vscode-requirements-end


.. _mcp-setup-vscode-add:

Add the Amperity MCP server
--------------------------------------------------

.. mcp-setup-vscode-add-start

Add the Amperity server to your user-level MCP configuration file, which makes Amperity available in every VS Code workspace.

.. mcp-setup-vscode-add-end

.. mcp-setup-vscode-add-steps-start

#. Open the **Command Palette** (**Ctrl+Shift+P** on Windows and Linux, **Cmd+Shift+P** on macOS), and then run **MCP: Open User Configuration**.

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

#. A browser window opens. Sign in with your Amperity credentials.

.. mcp-setup-vscode-add-steps-end


.. _mcp-setup-vscode-interacting:

Start interacting with Copilot in VS Code
--------------------------------------------------

.. mcp-setup-vscode-interacting-start

Open Copilot Chat, set the mode to **Agent**, and then ask about your Amperity tenant:

.. code-block:: none

   "Tell me about my Amperity tenant."

Copilot calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. mcp-setup-vscode-interacting-end


.. _mcp-setup-copilot-cli:

GitHub Copilot CLI
==================================================

.. mcp-setup-copilot-cli-start

Configure the Amperity MCP server in GitHub Copilot CLI, after which the Amperity tools are available to the agent in your terminal.

.. mcp-setup-copilot-cli-end


.. _mcp-setup-copilot-cli-requirements:

Requirements
--------------------------------------------------

.. mcp-setup-copilot-cli-requirements-start

Connecting GitHub Copilot CLI to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* GitHub Copilot CLI installed, and a GitHub account with an active Copilot subscription.

Install the CLI with npm:

.. code-block:: none

   npm install -g @github/copilot

.. mcp-setup-copilot-cli-requirements-end


.. _mcp-setup-copilot-cli-add:

Add the Amperity MCP server
--------------------------------------------------

.. mcp-setup-copilot-cli-add-start

Register Amperity as a remote MCP server, and then authorize it from an interactive session.

.. mcp-setup-copilot-cli-add-end

.. mcp-setup-copilot-cli-add-steps-start

#. Add the server:

   .. code-block:: none

      copilot mcp add --transport http amperity https://mcp.amperity.com

   This writes the server to your user configuration at ``~/.copilot/mcp-config.json``. Confirm it with ``copilot mcp list``.

#. Start an interactive session:

   .. code-block:: none

      copilot

#. Authorize the server:

   .. code-block:: none

      /mcp auth amperity

#. A browser window opens. Sign in with your Amperity credentials. The browser confirms **Authorization Successful**; close it and return to the terminal.

.. mcp-setup-copilot-cli-add-steps-end


.. _mcp-setup-copilot-cli-interacting:

Start interacting with Copilot CLI
--------------------------------------------------

.. mcp-setup-copilot-cli-interacting-start

In an interactive session, ask about your Amperity tenant:

.. code-block:: none

   "Tell me about my Amperity tenant."

Copilot calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. mcp-setup-copilot-cli-interacting-end


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


.. _mcp-setup-foundry:

Microsoft Foundry
==================================================

.. mcp-setup-foundry-start

Connect a Microsoft Foundry agent to the Amperity MCP server. Amperity is listed in the `Foundry Tool Catalog <https://ai.azure.com/catalog/tools/amperity-mcp-server/version/1/apiCenter/registry-prod-bl/eastus>`_.

.. mcp-setup-foundry-end


.. _mcp-setup-foundry-requirements:

Requirements
--------------------------------------------------

.. mcp-setup-foundry-requirements-start

Connecting Foundry to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* A Foundry project with a model deployment.
* The **Foundry User** role on the project to build the agent.

.. mcp-setup-foundry-requirements-end


.. _mcp-setup-foundry-connect:

Connect the Amperity tool
--------------------------------------------------

.. mcp-setup-foundry-connect-start

Create a project connection that holds the Amperity endpoint and its OAuth settings.

.. mcp-setup-foundry-connect-end

.. mcp-setup-foundry-connect-steps-start

#. In the Foundry portal, open your agent and go to **Tools**.
#. Select **Add**, open the **Catalog** tab, and then search for **Amperity**.
#. Select the **Amperity** entry. The **Connect the Amperity tool** dialog opens with the server endpoint already filled in as **https://mcp.amperity.com/mcp**.
#. Leave **Authentication** set to **OAuth Identity Passthrough**.
#. Under **OAuth Provider**, select **Custom**, and then fill in the following fields:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Field
        - Value
      * - **Client ID**
        - ``nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs``
      * - **Client secret**
        - Enter ``placeholder``. Foundry requires this field, but Amperity is a public OAuth client and issues no secret, so the value is ignored.
      * - **Auth URL**
        - **https://mcp.amperity.com/authorize**
      * - **Token URL**
        - **https://mcp.amperity.com/oauth/token**
      * - **Refresh URL**
        - **https://mcp.amperity.com/oauth/token**
      * - **Scopes**
        - ``openid offline_access``

#. Select **Connect**, and then save the agent.

.. mcp-setup-foundry-connect-steps-end


.. _mcp-setup-foundry-tool-surface:

Tool surface limits
--------------------------------------------------

.. mcp-setup-foundry-tool-surface-start

Foundry agents receive the same curated subset of tools as Copilot Studio. See :ref:`Tool surface limits <mcp-setup-copilot-surface-limits>`.

.. mcp-setup-foundry-tool-surface-end


.. _mcp-setup-foundry-interacting:

Start interacting with your agent
--------------------------------------------------

.. mcp-setup-foundry-interacting-start

Open the agent in the playground and ask about your Amperity tenant:

.. code-block:: none

   "Tell me about my Amperity tenant."

The agent calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. mcp-setup-foundry-interacting-end
