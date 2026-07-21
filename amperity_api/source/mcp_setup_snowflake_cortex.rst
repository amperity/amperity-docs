.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Configure Snowflake Cortex Agents to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Snowflake Cortex Agents to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Snowflake Cortex


==================================================
Set up Snowflake Cortex
==================================================

.. mcp-setup-cortex-start

Connect Snowflake Cortex Agents to the Amperity MCP server by registering it as an external MCP server and signing in with your Amperity credentials. Once registered, you can attach the Amperity MCP server to any Cortex Agent so the agent can call Amperity tools directly from Snowflake.

Setup involves five steps:

#. :ref:`Create an API integration <mcp-setup-cortex-integration>` that points at the Amperity MCP server and its OAuth endpoints.
#. :ref:`Register the external MCP server <mcp-setup-cortex-register>` through that integration.
#. :ref:`Grant usage <mcp-setup-cortex-grant>` on the server and integration to the roles that need it.
#. :ref:`Authorize the connection <mcp-setup-cortex-authorize>` by signing in to Amperity with OAuth.
#. :ref:`Attach the server to a Cortex Agent <mcp-setup-cortex-attach>` so the agent can call Amperity tools.

For details on Snowflake's external MCP connector feature, see the `Snowflake documentation <https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp-connectors>`__.

.. mcp-setup-cortex-end


.. _mcp-setup-cortex-requirements:

Requirements
==================================================

.. mcp-setup-cortex-requirements-start

Connecting Snowflake Cortex to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* The ``ACCOUNTADMIN`` role to create the API integration and the external MCP server.
* ``USAGE`` on both the external MCP server object and the API integration for any role that will use the connection.

.. mcp-setup-cortex-requirements-end


.. _mcp-setup-cortex-integration:

Create an API integration
==================================================

.. mcp-setup-cortex-integration-start

Create an API integration that allows Snowflake to reach the Amperity MCP server and complete the OAuth handshake. Run the following as ``ACCOUNTADMIN``:

.. code-block:: sql

   CREATE OR REPLACE API INTEGRATION amperity_mcp_integration
     API_PROVIDER = external_mcp
     API_ALLOWED_PREFIXES = ('https://mcp.amperity.com')
     API_USER_AUTHENTICATION = (
       TYPE = oauth2
       OAUTH_CLIENT_ID = 'nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs'
       OAUTH_CLIENT_SECRET = 'placeholder'
       OAUTH_TOKEN_ENDPOINT = 'https://mcp.amperity.com/oauth/token'
       OAUTH_AUTHORIZATION_ENDPOINT = 'https://mcp.amperity.com/authorize'
       OAUTH_RESOURCE_URL = 'https://mcp.amperity.com'
     )
     ENABLED = true;

``OAUTH_CLIENT_ID`` is Amperity's public MCP client ID and is the same for every customer.

.. important:: The Amperity MCP server is a public OAuth client that uses PKCE and does not issue a client secret. Snowflake still requires ``OAUTH_CLIENT_SECRET`` to be non-empty, so supply any non-empty placeholder value, such as ``placeholder``.

.. mcp-setup-cortex-integration-end


.. _mcp-setup-cortex-register:

Register the external MCP server
==================================================

.. mcp-setup-cortex-register-start

Register the Amperity MCP server through the integration you just created. The server object is created in your current database and schema, so set your context first. Replace ``<db>`` and ``<schema>`` with the database and schema where you want the server object to live:

.. code-block:: sql

   USE DATABASE <db>;
   USE SCHEMA <schema>;

   CREATE EXTERNAL MCP SERVER amperity_mcp
     WITH DISPLAY_NAME = 'Amperity MCP'
     URL = 'https://mcp.amperity.com'
     API_INTEGRATION = amperity_mcp_integration;

.. mcp-setup-cortex-register-end


.. _mcp-setup-cortex-grant:

Grant usage
==================================================

.. mcp-setup-cortex-grant-start

Grant ``USAGE`` on both the external MCP server and the API integration to the role used by anyone who will query the agent. Replace ``<analyst_role>`` with that role:

.. code-block:: sql

   GRANT USAGE ON EXTERNAL MCP SERVER amperity_mcp TO ROLE <analyst_role>;
   GRANT USAGE ON INTEGRATION amperity_mcp_integration TO ROLE <analyst_role>;

.. mcp-setup-cortex-grant-end


.. _mcp-setup-cortex-authorize:

Authorize the connection
==================================================

.. mcp-setup-cortex-authorize-start

Before the server can be used, each user signs in to Amperity with OAuth. Authorize from the Snowflake interface where you use the agent:

* In Snowflake Intelligence, select **+** in the message box, choose **Connectors**, then select **Connect** next to **Amperity MCP**.
* In Snowsight, open the **MCP connectors** page under **Settings** > **Cortex**, find the **Amperity MCP** connector, and select **Connect**.

A browser tab opens. Sign in with your Amperity credentials and select your tenant. Snowflake stores the resulting token for your user.

.. mcp-setup-cortex-authorize-end


.. _mcp-setup-cortex-attach:

Attach the server to a Cortex Agent
==================================================

.. mcp-setup-cortex-attach-start

Add the Amperity MCP server to a Cortex Agent so the agent can call Amperity tools. Update the agent's specification to reference the server object by its fully qualified name. Keep your existing agent specification and add the ``mcp_servers`` block. Replace ``<agent_name>`` and the ``<db>.<schema>`` prefix to match your environment:

.. code-block:: sql

   ALTER AGENT <agent_name> MODIFY LIVE VERSION SET SPECIFICATION $$
     <...your existing agent spec...>
     mcp_servers:
       - server_spec:
           name: "<db>.<schema>.amperity_mcp"
   $$;

.. mcp-setup-cortex-attach-end


.. _mcp-setup-cortex-verify:

Verify the connection
==================================================

.. mcp-setup-cortex-verify-start

Confirm the server is registered and that the agent can reach Amperity.

#. Confirm the server exists and inspect its configuration:

   .. code-block:: sql

      SHOW EXTERNAL MCP SERVERS IN ACCOUNT;
      DESCRIBE EXTERNAL MCP SERVER <db>.<schema>.amperity_mcp;

#. Prompt a Cortex Agent that has the Amperity MCP server attached:

   .. code-block:: none

      "List my Amperity tenants."

   The agent calls the **tenant_list** tool and returns the tenants available to your Amperity account. This confirms the connection end to end.

.. note:: Cortex Agent MCP tool calls are not written to Snowflake's monitoring tables. To confirm a tool ran, review the agent's live tool-invocation trace rather than looking for a query in your account history.

.. mcp-setup-cortex-verify-end
