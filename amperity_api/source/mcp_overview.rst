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

MCP server URL
==================================================

.. mcp-overview-mcp-urls-start

The Amperity MCP server is available at **https://mcp.amperity.com**. This URL automatically routes each request to the Amperity stack that hosts the calling user's tenant. Use this URL in every place that the setup pages below reference an MCP host.

.. mcp-overview-mcp-urls-end


.. _mcp-what-mcp-enables:

What is enabled?
==================================================

.. mcp-what-mcp-enables-start

The MCP server enables:

* Conversational access to Amperity from Copilot Studio, Claude, ChatGPT, and other MCP-compatible clients.

* More than 200 tools across tenants, such as databases, queries, identity resolution, campaigns, and predictive modeling. This full toolset is the default for connected clients.

  .. note:: Copilot Studio limits the number of individual tools an agent can register. For Copilot Studio connections, the Amperity MCP server automatically serves a curated subset of tools that fits within this limit. See :ref:`Tool surface limits <mcp-setup-copilot-surface-limits>`.

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
