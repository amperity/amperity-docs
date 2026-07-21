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

The MCP server is hosted by Amperity. Customers connect to a single public endpoint and authenticate to the MCP server by using their existing Amperity credentials. The MCP server is not installed or run locally.

.. mcp-overview-end


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

* Control the AI client or its underlying model.

  .. important:: Tool results may include personally identifiable information (PII). You are responsible for ensuring that the client and model you connect are approved to handle this data under your organization's policies and any agreements with the model provider.

* Replace the Amperity REST API.

  .. important:: Use the :doc:`Amperity API <overview>` for programmatic integrations that do not involve an AI agent.

.. mcp-what-mcp-not-enabled-end


.. _mcp-token-usage:

Does the MCP server use tokens?
==================================================

.. mcp-token-usage-start

Enabling the Amperity MCP server does not use tokens. The MCP server is a connector to your Amperity data; connecting a client does not consume tokens on the Amperity side.

Tokens are consumed by your AI client when its agent calls a tool and processes the response. That usage is metered and billed within your own AI platform, such as Claude or ChatGPT, and never by Amperity. The more data an agent pulls, the more tokens it uses.

.. mcp-token-usage-end


.. _mcp-connect-client:

Connect a client
==================================================

.. mcp-connect-client-start

Connect a client to the MCP server:

* :doc:`ChatGPT custom connectors <mcp_setup_chatgpt>`
* :doc:`Claude.ai, Claude Desktop, and Claude Code <mcp_setup_claude>`
* :doc:`Copilot Studio <mcp_setup_m365_copilot>`
* :doc:`Gemini -- Antigravity and Gemini CLI <mcp_setup_gemini>`

.. mcp-connect-client-end
