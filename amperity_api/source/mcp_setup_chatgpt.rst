.. https://docs.amperity.com/api/


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


.. _mcp-setup-chatgpt-requirements:

Requirements
==================================================

.. mcp-setup-chatgpt-requirements-start

Connecting ChatGPT to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* Access to ChatGPT with a plan that supports custom MCP connectors.
* The :ref:`URL for your tenant's MCP server endpoint <mcp-overview-mcp-urls>`.

.. mcp-setup-chatgpt-requirements-end


.. _mcp-setup-chatgpt-add:

Add the Amperity MCP server
==================================================

.. mcp-setup-chatgpt-add-start

To add the Amperity MCP server to ChatGPT:

#. Open ChatGPT and log in.
#. Open **Settings**, select **Connectors**, and then choose **Create**.

   .. note:: A workplace administrator may need to allow using custom MCP connectors for **Business** or **Enterprise** plans. Contact your workplace administrator if the **Create** option is unavailable.

#. Set the server URL:

   .. code-block:: none

      https://mcp.amperity.com

#. Set the authentication type to **OAuth**, and then use the following OAuth client ID:

   .. code-block:: none

      nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs
#. Save the connector. A browser tab opens. Sign in with your Amperity OAuth credentials.
#. Enable the Amperity connector for any chat session.

.. mcp-setup-chatgpt-add-end


.. _mcp-setup-chatgpt-interacting:

Start interacting with ChatGPT
==================================================

.. mcp-setup-chatgpt-interacting-start

In a ChatGPT session with the Amperity connector enabled, ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

ChatGPT calls the **tenant_info** tool and return details about your current Amperity tenant.

.. note:: Write operations in ChatGPT require a manual-confirm prompt in the chat the first time they are called.

.. mcp-setup-chatgpt-interacting-end
