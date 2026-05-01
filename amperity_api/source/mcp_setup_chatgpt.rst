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
* ChatGPT on the web on a plan that supports custom MCP connectors.
* The Amperity MCP endpoint: ``https://mcp.amperity.com``


Add the Amperity MCP server
==================================================

1. In ChatGPT, go to **Settings** > **Connectors**, then choose **Create**.
2. Set the server URL:

   ::

      https://mcp.amperity.com

3. Set the authentication type to **OAuth**.
4. Save the connector. ChatGPT opens a browser tab to complete authorization. Sign in with your Amperity credentials.
5. Enable the Amperity connector for any chat where you want it available.

.. note::

   On Business or Enterprise plans, your workspace admin may need to allow custom MCP connectors before you can add one. If you do not see the **Create** option, contact your workspace admin. Write tools fire a manual-confirm prompt in the chat the first time they are called.


Verify the connection
==================================================

In a chat with the connector enabled, ask:

   *"Tell me about my Amperity tenant."*

ChatGPT should call the ``tenant_info`` tool and return details about your current Amperity tenant.
