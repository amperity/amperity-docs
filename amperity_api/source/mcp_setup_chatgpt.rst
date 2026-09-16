.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Install the Amperity plugin in ChatGPT to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Install the Amperity plugin in ChatGPT to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up ChatGPT


==================================================
Set up ChatGPT
==================================================

.. mcp-setup-chatgpt-start

Amperity is published in the `ChatGPT plugin directory <https://chatgpt.com/plugins/plugin_asdk_app_6a908cd7176081919717ffa210436393>`_. Install the plugin, sign in with your Amperity credentials, and ChatGPT can work with your customer data.

.. mcp-setup-chatgpt-end


.. _mcp-setup-chatgpt-requirements:

Requirements
==================================================

.. mcp-setup-chatgpt-requirements-start

Connecting ChatGPT to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* Access to ChatGPT with a plan that supports plugins.

.. mcp-setup-chatgpt-requirements-end


.. _mcp-setup-chatgpt-add:

Install the Amperity plugin
==================================================

.. mcp-setup-chatgpt-add-start

To install the Amperity plugin:

#. Open ChatGPT and log in.
#. Select **Plugins** from the sidebar, and then search for "Amperity".

   .. note:: A workplace administrator may need to allow plugins for **Business** or **Enterprise** plans. Contact your workplace administrator if the Amperity plugin is unavailable.

#. Select **Amperity**, and then select **Install plugin**.
#. A browser tab opens. Sign in with your Amperity credentials.
#. In a chat, bring in the plugin with an **@** mention, or by selecting **+** and then **More**.

.. mcp-setup-chatgpt-add-end


.. _mcp-setup-chatgpt-interacting:

Start interacting with ChatGPT
==================================================

.. mcp-setup-chatgpt-interacting-start

In a chat with the Amperity plugin brought in, ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

ChatGPT calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. note:: Write operations in ChatGPT require a manual-confirm prompt in the chat the first time they are called.

.. mcp-setup-chatgpt-interacting-end
