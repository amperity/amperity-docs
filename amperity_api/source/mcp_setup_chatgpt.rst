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

Amperity is published in the `ChatGPT plugin directory <https://chatgpt.com/plugins/plugin_asdk_app_6a908cd7176081919717ffa210436393>`_. Install the plugin, or connect the Amperity MCP server to Codex, sign in with your Amperity credentials, and work with your customer data.

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
#. Enable the plugin in a chat with an **@** mention, or by selecting **+** and then **More**.

.. mcp-setup-chatgpt-add-end


.. _mcp-setup-codex:

Set up Codex
==================================================

.. mcp-setup-codex-start

Connect the Amperity MCP server to Codex from a terminal.

#. Add the Amperity MCP server to your Codex configuration:

   .. code-block:: bash

      codex mcp add amperity --url https://mcp.amperity.com

   Codex registers the server for your user account. The command detects Amperity's OAuth support and opens a browser window. Sign in with your Amperity credentials to authorize Codex.

#. Verify that Codex registered the server:

   .. code-block:: bash

      codex mcp list

   The **amperity** entry appears as enabled and uses OAuth authentication.


.. mcp-setup-codex-end


.. _mcp-setup-chatgpt-interacting:

Start interacting with ChatGPT
==================================================

.. mcp-setup-chatgpt-interacting-start

In a chat with the Amperity plugin enabled, or in a new Codex session, ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

ChatGPT or Codex calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. note:: Write operations in ChatGPT require a manual-confirm prompt in the chat the first time they are called.

.. mcp-setup-chatgpt-interacting-end
