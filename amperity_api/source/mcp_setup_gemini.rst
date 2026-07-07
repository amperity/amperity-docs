.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Configure Antigravity or Gemini CLI to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Antigravity or Gemini CLI to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Gemini


==================================================
Set up Gemini
==================================================

.. mcp-setup-gemini-start

Connect Google's Gemini agents to the Amperity MCP server and sign in with your Amperity credentials. This page covers two clients:

* :ref:`Antigravity <mcp-setup-antigravity>` -- Google's agentic IDE.
* :ref:`Gemini CLI <mcp-setup-gemini-cli>` -- the command-line agent.

.. mcp-setup-gemini-end


.. _mcp-setup-antigravity:

Antigravity
==================================================

.. mcp-setup-antigravity-start

Connect Antigravity to the Amperity MCP server by adding it as a custom remote MCP server and signing in with your Amperity credentials.

.. mcp-setup-antigravity-end


.. _mcp-setup-antigravity-requirements:

Requirements
--------------------------------------------------

.. mcp-setup-antigravity-requirements-start

Connecting Antigravity to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* Antigravity installed and signed in.

.. mcp-setup-antigravity-requirements-end


.. _mcp-setup-antigravity-add:

Add the Amperity MCP server
--------------------------------------------------

.. mcp-setup-antigravity-add-start

Register the Amperity MCP server as a custom server in your Antigravity configuration.

#. Open your global Antigravity MCP configuration file at ``~/.gemini/config/mcp_config.json``.

#. Add the ``amperity`` server with Amperity's OAuth client ID:

   .. code-block:: json

      {
        "mcpServers": {
          "amperity": {
            "serverUrl": "https://mcp.amperity.com",
            "oauth": {
              "clientId": "nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs"
            }
          }
        }
      }

   .. important:: Antigravity requires the ``serverUrl`` field for remote servers; the ``url`` and ``httpUrl`` fields are not supported. The ``oauth.clientId`` field is required so Antigravity surfaces the **Authenticate** button.

.. mcp-setup-antigravity-add-end


.. _mcp-setup-antigravity-authenticate:

Authenticate
--------------------------------------------------

.. mcp-setup-antigravity-authenticate-start

#. Click **Settings** at the bottom left, then select the **Customizations** tab.

#. Under **Installed MCP Servers**, click **Authenticate** next to the **amperity** server. A browser tab opens. Sign in with your Amperity OAuth credentials and select your tenant.

#. Copy the authorization code from the browser, paste it back into the settings panel, and click **Submit**. The server reconnects automatically and its tools become available.

.. mcp-setup-antigravity-authenticate-end


.. _mcp-setup-antigravity-interacting:

Start interacting with Antigravity
--------------------------------------------------

.. mcp-setup-antigravity-interacting-start

In an Antigravity agent session, ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

Antigravity calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. mcp-setup-antigravity-interacting-end


.. _mcp-setup-gemini-cli:

Gemini CLI
==================================================

.. mcp-setup-gemini-cli-start

Connect Gemini CLI to the Amperity MCP server by adding it as a remote MCP server and signing in with your Amperity credentials.

.. important:: Gemini CLI only works for organizations on a Gemini Code Assist Standard or Enterprise license.

.. mcp-setup-gemini-cli-end


.. _mcp-setup-gemini-cli-requirements:

Requirements
--------------------------------------------------

.. mcp-setup-gemini-cli-requirements-start

Connecting Gemini CLI to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* Gemini CLI installed and signed in.

.. mcp-setup-gemini-cli-requirements-end


.. _mcp-setup-gemini-cli-add:

Add the Amperity MCP server
--------------------------------------------------

.. mcp-setup-gemini-cli-add-start

Register the Amperity MCP server in your Gemini CLI configuration.

#. Add the server:

   .. code-block:: bash

      gemini mcp add --transport http --scope user amperity https://mcp.amperity.com

#. Add Amperity's OAuth client ID to the server entry. Open ``~/.gemini/settings.json`` and add an ``oauth`` block to the ``amperity`` server so it matches the following:

   .. code-block:: json

      {
        "mcpServers": {
          "amperity": {
            "httpUrl": "https://mcp.amperity.com",
            "oauth": {
              "clientId": "nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs",
              "authorizationUrl": "https://mcp.amperity.com/authorize",
              "tokenUrl": "https://mcp.amperity.com/oauth/token"
            }
          }
        }
      }

   .. important:: The ``oauth.clientId`` field is required. Without it, Gemini CLI cannot authenticate to the Amperity MCP server.

.. mcp-setup-gemini-cli-add-end


.. _mcp-setup-gemini-cli-authenticate:

Authenticate
--------------------------------------------------

.. mcp-setup-gemini-cli-authenticate-start

#. Start Gemini CLI, or restart it if it was already running, so it reloads ``settings.json``:

   .. code-block:: bash

      gemini

#. Trigger the OAuth flow:

   .. code-block:: none

      /mcp auth amperity

   A browser tab opens. Sign in with your Amperity OAuth credentials. Gemini CLI reports a successful authentication and reloads the Amperity tools.

#. Verify the server is connected:

   .. code-block:: none

      /mcp

   The **amperity** server appears with its available tools.

.. mcp-setup-gemini-cli-authenticate-end


.. _mcp-setup-gemini-cli-interacting:

Start interacting with Gemini CLI
--------------------------------------------------

.. mcp-setup-gemini-cli-interacting-start

In a Gemini CLI session, ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

Gemini CLI calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. mcp-setup-gemini-cli-interacting-end
