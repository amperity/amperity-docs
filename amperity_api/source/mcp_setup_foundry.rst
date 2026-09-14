.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Configure Microsoft Foundry Agent Service to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Microsoft Foundry Agent Service to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Microsoft Foundry


==================================================
Set up Microsoft Foundry
==================================================

.. mcp-setup-foundry-start

Connect a Microsoft Foundry agent to the Amperity MCP server. Amperity is listed in the Foundry Tool Catalog, so you can find it by name rather than entering the server endpoint by hand.

Foundry uses **OAuth identity passthrough**: each person who uses the agent signs in to Amperity themselves, and the agent acts with that person's own Amperity permissions.

.. mcp-setup-foundry-end


.. _mcp-setup-foundry-requirements:

Requirements
==================================================

.. mcp-setup-foundry-requirements-start

Connecting Foundry to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* A Foundry project with a model deployment.
* The **Foundry User** role on the project to build the agent. People who only use the agent need the **Foundry Agent Consumer** role.

.. mcp-setup-foundry-requirements-end


.. _mcp-setup-foundry-connect:

Connect the Amperity tool
==================================================

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
        - Leave empty. Amperity is a public OAuth client and issues no secret. If the field is required, enter any placeholder value.
      * - **Auth URL**
        - **https://mcp.amperity.com/authorize**
      * - **Token URL**
        - **https://mcp.amperity.com/oauth/token**
      * - **Refresh URL**
        - **https://mcp.amperity.com/oauth/token**
      * - **Scopes**
        - ``openid offline_access``, separated by a space

#. Select **Connect**, and then save the agent.

.. important:: Select **Custom**, not **Managed**. **Managed** sends a Microsoft Entra token, which the Amperity MCP server does not accept. An agent configured that way fails with ``Missing required query parameter: audience``.

.. mcp-setup-foundry-connect-steps-end


.. _mcp-setup-foundry-tool-surface:

Tool surface
==================================================

.. mcp-setup-foundry-tool-surface-start

Foundry receives a curated subset of the Amperity tool surface rather than all of it.

The subset still includes tools that change data, such as creating segments and campaigns. It is sized to fit a tool count limit; it is not a read-only boundary. Foundry requires approval for every tool call by default. Keep that default unless you have reviewed which tools the agent can reach.

.. mcp-setup-foundry-tool-surface-end


.. _mcp-setup-foundry-interacting:

Start interacting with your agent
==================================================

.. mcp-setup-foundry-interacting-start

Open the agent in the playground and ask about your Amperity tenant:

.. code-block:: none

   "Tell me about my Amperity tenant."

The first time you use the tool, the agent returns a consent link. Open it, sign in with your Amperity credentials, and then close the window and return to the agent. Ask again, and the agent calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. tip:: The consent window sometimes reports that authentication failed even though it succeeded. Before retrying, ask the agent another question. If it answers, the sign-in worked.

.. mcp-setup-foundry-interacting-end
