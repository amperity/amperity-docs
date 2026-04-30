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
* A ChatGPT plan that includes custom MCP connectors.
* The Amperity MCP endpoint: ``https://mcp.amperity.com/mcp``


Add the Amperity MCP server
==================================================

1. In ChatGPT, open **Settings**, then **Connectors**, then **Add connector**.
2. Select **Custom MCP server**.
3. Set the server URL:

   ::

      https://mcp.amperity.com/mcp

4. Set the authentication type to **OAuth**.
5. Save the connector. ChatGPT opens a browser tab to complete authorization. Sign in with your Amperity credentials.
6. Enable the Amperity connector for any GPT or chat where you want it available.


Verify the connection
==================================================

In a chat with the connector enabled, ask:

   *"List my Amperity tenants."*

ChatGPT should call the ``tenant.list`` tool and return your tenants.


Troubleshooting
==================================================

For common errors, see :doc:`mcp_troubleshooting`.
