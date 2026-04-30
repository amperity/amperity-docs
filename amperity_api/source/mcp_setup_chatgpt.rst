.. https://docs.amperity.com/api/mcp_setup_chatgpt.html


.. meta::
    :description lang=en:
        Configure ChatGPT custom connectors to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure ChatGPT custom connectors to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up ChatGPT


==================================================
Set up ChatGPT
==================================================

.. mcp-setup-chatgpt-start

Connect ChatGPT to the Amperity MCP server by adding it as a custom connector. ChatGPT custom connectors require a ChatGPT plan that supports remote MCP servers.

.. mcp-setup-chatgpt-end


Before you begin
==================================================

You need:

* An active Amperity account with access to at least one tenant.
* ChatGPT on the web on a Pro, Plus, Business, Enterprise, or Education plan. Developer mode (see below) is required to use Amperity's write tools.
* The Amperity MCP endpoint: ``https://mcp.amperity.com``


Enable developer mode
==================================================

ChatGPT's standard custom connectors are restricted; full Model Context Protocol support -- including write tools -- is gated behind **developer mode**. Because the Amperity MCP server exposes write tools (campaigns, databases, queries, and more), you need developer mode on to use the full surface.

To turn it on for an individual user, go to **Settings** > **Apps** > **Advanced settings** in ChatGPT, then enable **Developer mode**.

On a Business or Enterprise plan, the workspace admin must enable developer mode for the workspace before individual users can turn it on. Per OpenAI: *"Developer mode is powerful but dangerous"* -- review OpenAI's documentation on prompt-injection and write-action risks before enabling at the organization level.


Add the Amperity MCP server
==================================================

With developer mode enabled, add Amperity as a custom MCP connector from **Settings** > **Apps**:

1. Add a new custom MCP server.
2. Set the server URL:

   ::

      https://mcp.amperity.com

3. Set the authentication type to **OAuth**.
4. Save the connector. ChatGPT opens a browser tab to complete authorization. Sign in with your Amperity credentials.
5. Enable the Amperity connector for any GPT or chat where you want it available.


Verify the connection
==================================================

In a chat with the connector enabled, ask:

   *"Tell me about my Amperity tenant."*

ChatGPT should call the ``tenant_info`` tool and return details about your current Amperity tenant.


Troubleshooting
==================================================

For common errors, see :doc:`mcp_troubleshooting`.
