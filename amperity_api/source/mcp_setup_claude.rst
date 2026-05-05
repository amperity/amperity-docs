.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Configure Claude.ai, Claude Desktop, and Claude Code to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Claude.ai, Claude Desktop, and Claude Code to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Claude


==================================================
Set up Claude
==================================================

.. mcp-setup-claude-start

Connect Claude to the Amperity MCP server through Claude.ai, which also makes the MCP server available in Claude Desktop and Claude mobile apps, or through Claude Code.

.. mcp-setup-claude-end


.. _mcp-setup-claude-requirements:

Requirements
==================================================

.. mcp-setup-claude-requirements-start

Connecting Claude to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* Access to a Claude account--**Pro**, **Max**, **Team**, or **Enterprise**--or access to Claude Code.
* The :ref:`URL for your tenant's MCP server endpoint <mcp-overview-mcp-urls>`.

.. mcp-setup-claude-requirements-end


.. _mcp-setup-claude-ai:

Claude.ai
==================================================

.. mcp-setup-claude-ai-start

Claude.ai is the canonical location to add remote MCP connectors. Once added, the connector is also available in Claude Desktop and Claude mobile apps signed into the same account.

#. Open Claude.ai and log in.
#. Open the **Connectors** page for your plan:

   For **Pro** or **Max** plans in Claude.ai, open **Customize**, select **Connectors**, and then click **+** or **Add custom connector**.

   For **Team** or **Enterprise** plans, as the organization Owner only, open **Organization settings**, select **Connectors**, click **Add**, hover over **Custom**, then select **Web**.

#. For **Remote MCP server URL** enter:

   .. code-block:: none

      https://mcp.amperity.com

   .. important:: Use the :ref:`correct MCP server URL <mcp-overview-mcp-urls>` for this setting.

   Use **nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs** as the OAuth client ID.

#. Click **Add**. A browser tab opens. Sign in with your Amperity OAuth credentials.

   For **Team** or **Enterprise** plans open **Customize**, select **Connectors**, and then click **Connect** for the Amperity connector.

.. mcp-setup-claude-ai-end


.. _mcp-setup-claude-code:

Claude Code
==================================================

.. mcp-setup-claude-code-start

Configure the Amperity MCP server for Claude Code.

#. Open Claude Code.

#. Add the Amperity MCP server:

   .. code-block:: bash

      claude mcp add --transport http --scope user amperity https://mcp.amperity.com

   .. important:: Use the :ref:`correct MCP server URL <mcp-overview-mcp-urls>` in the command.

   The server is registered in your user-scoped Claude configuration and is available in every Claude Code session.

#. To verify the server is registered with Claude Code:

   .. code-block:: bash

      claude mcp list

   The Amperity entry appears with a status of **Needs authentication** or **Connected**.

   .. note:: The first time Claude Code calls an Amperity tool a browser tab opens for OAuth. Sign in with your Amperity credentials, after which the registration status is set to **Connected**.

.. mcp-setup-claude-code-end


.. _mcp-setup-claude-interacting:

Start interacting with Claude
==================================================

.. mcp-setup-claude-interacting-start

Open a Claude conversation and ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

Claude calls the **tenant_info** tool and return details about your current Amperity tenant.

.. tip:: If you see an authorization error, remove the server and add it again to force the OAuth flow.

   .. code-block:: none

      claude mcp remove amperity

      claude mcp add --transport http --scope user amperity https://mcp.amperity.com

      .. important:: Use the :ref:`correct MCP server URL <mcp-overview-mcp-urls>` in the command.

.. mcp-setup-claude-interacting-end
