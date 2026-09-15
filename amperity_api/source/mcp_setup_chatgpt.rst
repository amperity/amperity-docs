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
#. Enable the Amperity plugin for any chat session.

.. mcp-setup-chatgpt-add-end


.. _mcp-setup-chatgpt-custom-connector:

Add as a custom connector
==================================================

.. mcp-setup-chatgpt-custom-connector-start

Workspaces that restrict the plugin directory can reach the same MCP server through a custom connector:

#. Open **Settings**, select **Apps**, and then choose **Create**.
#. Set the server URL:

   .. code-block:: none

      https://mcp.amperity.com

#. Set the authentication type to **OAuth**, and then use the following OAuth client ID:

   .. code-block:: none

      nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs

#. Save the connector. A browser tab opens. Sign in with your Amperity credentials.

.. note:: A custom connector snapshots the tool list when it is published. If you are unable to access tools documented in the :doc:`tool reference </mcp_tool_reference>`, ask your workplace administrator to publish an updated version of the connector. The plugin directory listing is updated by Amperity and does not have this limitation.

.. mcp-setup-chatgpt-custom-connector-end


.. _mcp-setup-chatgpt-interacting:

Start interacting with ChatGPT
==================================================

.. mcp-setup-chatgpt-interacting-start

In a ChatGPT session with the Amperity plugin enabled, ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

ChatGPT calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. note:: Write operations in ChatGPT require a manual-confirm prompt in the chat the first time they are called.

.. mcp-setup-chatgpt-interacting-end
