.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        The Amperity MCP server lets AI assistants and agents operate Amperity programmatically by using the Model Context Protocol over an authenticated HTTP endpoint.

.. meta::
    :content class=swiftype name=body data-type=text:
        The Amperity MCP server lets AI assistants and agents operate Amperity programmatically by using the Model Context Protocol over an authenticated HTTP endpoint.

.. meta::
    :content class=swiftype name=title data-type=string:
        About the Amperity MCP server


==================================================
About the Amperity MCP server
==================================================

.. mcp-overview-start

The Amperity MCP server enables AI assistants and agents to operate Amperity programmatically by using the `Model Context Protocol <https://modelcontextprotocol.io/>`__ (MCP). Connect any MCP-compatible client, such as Copilot Studio, Claude, or ChatGPT, to your Amperity tenant, and then use natural language to inspect data, run identity resolution, build queries and segments, create activations, run campaigns and journeys, and build predictive models.

The MCP server is hosted by Amperity. Customers connect to a single public endpoint and authenticate to the MCP server by using their existing Amperity credentials. There is nothing to install or run locally.

.. mcp-overview-end


.. admonition:: Private beta

   The MCP server is available as a private beta. Tool surface, configuration, and behavior may change as the beta progresses. Tool count is approximate during beta and subject to change. Contact your Amperity representative for access.


.. _mcp-overview-mcp-urls:

MCP server URLs
==================================================

.. mcp-overview-mcp-urls-start

The Amperity MCP server is available at a single front-door URL, **https://mcp.amperity.com**, which automatically routes each request to the Amperity stack that hosts the calling user's tenant. Per-stack URLs are also available for clients that need to connect to a specific stack directly:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - URL
     - Routes to
     - Cloud / region
   * - **https://mcp.amperity.com**
     - Any stack (automatic per-tenant routing)
     - --
   * - **https://mcp-aws-prod.amperity.com**
     - aws-prod
     - AWS us-west-2
   * - **https://mcp-aws-cc1.amperity.com**
     - aws-prod-cc1
     - AWS ca-central-1
   * - **https://mcp-aws-apse2.amperity.com**
     - aws-prod-apse2
     - AWS ap-southeast-2
   * - **https://mcp-az-prod.amperity.com**
     - az-prod
     - Azure eastus2
   * - **https://mcp-az-prod-en1.amperity.com**
     - az-prod-en1
     - Azure northeurope

For most clients, use **https://mcp.amperity.com**. If you need to connect directly to a specific stack--for example, to reduce the latency added by the cross-stack routing layer--use the matching per-stack URL in every place that the setup pages reference an MCP host. If you are unsure which stack hosts your tenant, contact your Amperity representative.

.. mcp-overview-mcp-urls-end


.. _mcp-what-mcp-enables:

What is enabled?
==================================================

.. mcp-what-mcp-enables-start

The MCP server enables:

* Conversational access to Amperity from Copilot Studio, Claude, ChatGPT, and other MCP-compatible clients.

* More than 200 tools across tenants, such as databases, queries, identity resolution, campaigns, and predictive modeling.

  .. note:: Some clients, such as Copilot Studio, limit the number of individual tools an agent can register and may require surfacing only a subset of the full toolset available in the MCP server.

* Per-user isolation. Each request is authenticated and scoped to the calling user's identity, tenant, and permissions.

* Configurable :doc:`safety modes <mcp_safety_modes>` for write operations.

.. mcp-what-mcp-enables-end


.. _mcp-what-mcp-not-enabled:

What is not enabled?
==================================================

.. mcp-what-mcp-not-enabled-start

The Amperity MCP server does not:

* Bypass authorization to Amperity services.

  .. important:: A user of the Amperity MCP server sees only the tenants and operations allowed by their credentials.

* Store conversation history. Per-token session state--selected tenant and safety mode--persists across requests within the same session.

* Replace the Amperity REST API.

  .. important:: Use the :doc:`Amperity API <overview>` for programmatic integrations that do not involve an AI agent.

.. mcp-what-mcp-not-enabled-end


.. _mcp-connect-client:

Connect a client
==================================================

.. mcp-connect-client-start

Connect a client to the MCP server:

* :doc:`ChatGPT custom connectors <mcp_setup_chatgpt>`
* :doc:`Claude.ai, Claude Desktop, and Claude Code <mcp_setup_claude>`
* :doc:`Copilot Studio <mcp_setup_m365_copilot>`

.. mcp-connect-client-end
