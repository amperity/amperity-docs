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

Each Amperity production stack has its own MCP server endpoint. Use the URL that matches the region of your Amperity tenant:

.. list-table::
   :header-rows: 1
   :widths: 25 45 30

   * - Stack
     - Public URL
     - Cloud / region
   * - **aws-prod** (default)
     - **https://mcp.amperity.com**
     - AWS us-west-2
   * - **aws-prod-cc1**
     - **https://mcp-aws-cc1.amperity.com**
     - AWS ca-central-1
   * - **aws-prod-apse2**
     - **https://mcp-aws-apse2.amperity.com**
     - AWS ap-southeast-2
   * - **az-prod**
     - **https://mcp-az-prod.amperity.com**
     - Azure eastus2
   * - **az-prod-en1**
     - **https://mcp-az-prod-en1.amperity.com**
     - Azure northeurope

The setup pages below show **https://mcp.amperity.com** (aws-prod) in their examples. If your tenant is on a different stack, substitute the corresponding URL in every place that the docs reference an MCP host. If you are unsure which stack hosts your tenant, contact your Amperity representative.

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
