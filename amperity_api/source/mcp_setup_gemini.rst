.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Configure Gemini CLI to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Gemini CLI to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Gemini CLI


==================================================
Set up Gemini CLI
==================================================

.. mcp-setup-gemini-start

Connect Gemini CLI to the Amperity MCP server by adding it as a remote MCP server and signing in with your Amperity credentials.

.. important:: Gemini CLI only works for organizations on a Gemini Code Assist Standard or Enterprise license.

.. mcp-setup-gemini-end


.. _mcp-setup-gemini-requirements:

Requirements
==================================================

.. mcp-setup-gemini-requirements-start

Connecting Gemini CLI to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* Gemini CLI installed and signed in.
* The :ref:`URL for your tenant's MCP server endpoint <mcp-overview-mcp-urls>`.

.. mcp-setup-gemini-requirements-end


.. _mcp-setup-gemini-add:

Add the Amperity MCP server
==================================================

.. mcp-setup-gemini-add-start

Register the Amperity MCP server in your Gemini CLI configuration.

#. Add the server:

   .. code-block:: bash

      gemini mcp add --transport http --scope user amperity https://mcp.amperity.com

#. Add Amperity's OAuth client ID to the server entry. Open ``~/.gemini/settings.json`` and add an ``oauth`` block to the ``amperity`` server so it matches the following:

   .. code-block:: json

      {
        "mcpServers": {
          "amperity": {
            "url": "https://mcp.amperity.com",
            "type": "http",
            "oauth": {
              "clientId": "nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs",
              "authorizationUrl": "https://mcp.amperity.com/authorize",
              "tokenUrl": "https://mcp.amperity.com/oauth/token"
            }
          }
        }
      }

   .. important:: The ``oauth.clientId`` field is required. Without it, Gemini CLI cannot authenticate to the Amperity MCP server.

.. mcp-setup-gemini-add-end


.. _mcp-setup-gemini-authenticate:

Authenticate
==================================================

.. mcp-setup-gemini-authenticate-start

Complete the OAuth flow to connect to the MCP server.

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

.. mcp-setup-gemini-authenticate-end


.. _mcp-setup-gemini-interacting:

Start interacting with Gemini CLI
==================================================

.. mcp-setup-gemini-interacting-start

In a Gemini CLI session, ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

Gemini CLI calls the **tenant_info** tool and returns details about your current Amperity tenant.

.. tip:: If you see a ``dynamic client registration is disabled`` error during ``/mcp auth``, confirm the ``oauth.clientId`` field is present in your ``amperity`` server entry in ``settings.json``, and then restart Gemini CLI to reload the configuration.

.. mcp-setup-gemini-interacting-end
