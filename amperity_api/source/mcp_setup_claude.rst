.. https://docs.amperity.com/api/mcp_setup_claude.html


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

Connect Amperity to Claude in two places: through Claude.ai (which also makes the connector available in Claude Desktop and the Claude mobile apps), and through Claude Code for terminal use.

.. mcp-setup-claude-end


Before you begin
==================================================

You need:

* An active Amperity account with access to at least one tenant.
* A Claude account (Pro, Max, Team, or Enterprise) and / or Claude Code installed.
* The Amperity MCP endpoint: ``https://mcp.amperity.com``


.. _mcp-setup-claude-web:

Claude.ai (and Claude Desktop)
==================================================

Claude.ai is the canonical place to add remote MCP connectors. Once added, the connector is also available in Claude Desktop and Claude mobile apps signed into the same account. Claude Desktop's ``claude_desktop_config.json`` file is for local stdio servers only and does not need to be edited for the hosted Amperity MCP.

Pro or Max plan
--------------------------------------------------

1. In Claude.ai, go to **Customize** > **Connectors**.
2. Click **+** (or **Add custom connector**).
3. In **Remote MCP server URL**, enter:

   ::

      https://mcp.amperity.com

4. Click **Add**. Claude opens a browser tab to complete OAuth. Sign in with your Amperity credentials.

Team or Enterprise plan
--------------------------------------------------

Only an organization Owner can add a custom connector for a Team or Enterprise plan.

1. In Claude.ai, go to **Organization settings** > **Connectors**.
2. Click **Add**. Hover over **Custom**, then select **Web**.
3. In **Remote MCP server URL**, enter:

   ::

      https://mcp.amperity.com

4. Click **Add**.

Members of the organization can then connect by going to **Customize** > **Connectors** and clicking **Connect** on the Amperity entry. The first connect opens a browser tab to complete OAuth.


.. _mcp-setup-claude-code:

Claude Code
==================================================

Add the Amperity MCP server with the Claude CLI:

::

   claude mcp add --transport http --scope user amperity https://mcp.amperity.com

The server is registered in your user-scope Claude configuration and is available in every Claude Code session. The first time Claude Code calls an Amperity tool it opens a browser tab to complete OAuth -- sign in with your Amperity credentials.

To verify the server is registered:

::

   claude mcp list

The Amperity entry should appear with status **Needs authentication** until your first authorized call, then **Connected**.


Verify the connection
==================================================

In a Claude conversation, ask:

   *"Tell me about my Amperity tenant."*

Claude should call the ``tenant_info`` tool and return details about your current Amperity tenant. If you see an authorization error, remove the server and add it again to retrigger the OAuth flow:

::

   claude mcp remove amperity
   claude mcp add --transport http --scope user amperity https://mcp.amperity.com


Troubleshooting
==================================================

For common errors, see :doc:`mcp_troubleshooting`.
