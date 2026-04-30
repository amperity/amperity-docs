.. https://docs.amperity.com/api/mcp_setup_claude.html


.. meta::
    :description lang=en:
        Configure Claude Desktop and Claude Code to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Claude Desktop and Claude Code to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Claude


==================================================
Set up Claude
==================================================

.. mcp-setup-claude-start

Connect Claude Desktop or Claude Code to the Amperity MCP server. Both clients support remote MCP servers with OAuth authentication.

.. mcp-setup-claude-end


Before you begin
==================================================

You need:

* An active Amperity account with access to at least one tenant.
* Claude Desktop or Claude Code installed.
* The Amperity MCP endpoint: ``https://mcp.amperity.com/mcp``


.. _mcp-setup-claude-desktop:

Claude Desktop
==================================================

Edit your Claude Desktop configuration file:

* macOS: ``~/Library/Application Support/Claude/claude_desktop_config.json``
* Windows: ``%APPDATA%\Claude\claude_desktop_config.json``

Add an entry under ``mcpServers``:

::

   {
     "mcpServers": {
       "amperity": {
         "url": "https://mcp.amperity.com/mcp"
       }
     }
   }

Restart Claude Desktop. On first use, Claude opens a browser to complete the OAuth login. Sign in with your Amperity credentials.


.. _mcp-setup-claude-code:

Claude Code
==================================================

Add the Amperity MCP server with the Claude CLI:

::

   claude mcp add --transport http --scope user amperity https://mcp.amperity.com/mcp

When you next start Claude Code, it prompts you to authorize. Sign in with your Amperity credentials in the browser window that opens.


Verify the connection
==================================================

In a Claude conversation, ask:

   *"List my Amperity tenants."*

Claude should call the ``tenant_list`` tool and return your tenants. If you see an authorization error, remove the server and add it again to retrigger the OAuth flow:

::

   claude mcp remove amperity
   claude mcp add --transport http --scope user amperity https://mcp.amperity.com/mcp


Troubleshooting
==================================================

For common errors, see :doc:`mcp_troubleshooting`.
