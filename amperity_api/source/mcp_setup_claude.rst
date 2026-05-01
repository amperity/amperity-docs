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

Claude.ai is the canonical place to add remote MCP connectors. Once added, the connector is also available in Claude Desktop and Claude mobile apps signed into the same account.

Open the right Connectors page for your plan:

* **Pro or Max** -- in Claude.ai, go to **Customize** > **Connectors**, then click **+** (or **Add custom connector**).
* **Team or Enterprise** (organization Owner only) -- go to **Organization settings** > **Connectors**, click **Add**, hover over **Custom**, then select **Web**.

Then, in either flow:

1. In **Remote MCP server URL**, enter:

   ::

      https://mcp.amperity.com

2. Click **Add**. A browser tab opens to complete OAuth on first connect -- sign in with your Amperity credentials.

On Team or Enterprise plans, members can then connect by going to **Customize** > **Connectors** and clicking **Connect** on the Amperity entry.


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
