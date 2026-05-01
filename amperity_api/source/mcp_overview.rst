.. https://docs.amperity.com/api/mcp_overview.html


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

The Amperity MCP server enables AI assistants and agents to operate Amperity programmatically by using the `Model Context Protocol <https://modelcontextprotocol.io/>`__ (MCP). Connect any MCP-compatible client -- such as Copilot Studio, Claude, or ChatGPT -- to your Amperity tenant and use natural language to inspect data, run queries, manage campaigns, run identity resolution, and more.

The MCP server is hosted by Amperity. Customers connect to the public endpoint for their stack and authenticate by using their existing Amperity credentials. There is nothing to install or run locally.

.. mcp-overview-end


.. admonition:: Beta

   The Amperity MCP server is available as a private beta. Tool surface, configuration, and behavior may change as the beta progresses. Contact your Amperity representative for access.


.. _mcp-overview-stack-urls:

Find your MCP URL
==================================================

Each Amperity production stack has its own MCP endpoint. Use the URL that matches the region of your Amperity tenant:

.. list-table::
   :header-rows: 1
   :widths: 25 45 30

   * - Stack
     - Public MCP URL
     - Cloud / region
   * - ``aws-prod`` (default)
     - ``https://mcp.amperity.com``
     - AWS us-west-2
   * - ``aws-prod-cc1``
     - ``https://mcp-aws-cc1.amperity.com``
     - AWS ca-central-1
   * - ``aws-prod-apse2``
     - ``https://mcp-aws-apse2.amperity.com``
     - AWS ap-southeast-2
   * - ``az-prod``
     - ``https://mcp-az-prod.amperity.com``
     - Azure eastus2
   * - ``az-prod-en1``
     - ``https://mcp-az-prod-en1.amperity.com``
     - Azure northeurope

The setup pages below show ``https://mcp.amperity.com`` (aws-prod) in their examples. If your tenant is on a different stack, substitute the corresponding URL in every place that the docs reference an MCP host. If you are unsure which stack hosts your tenant, contact your Amperity representative.


What it enables
==================================================

* Conversational access to Amperity from Copilot Studio, Claude, ChatGPT, and other MCP-compatible clients.
* More than 200 tools across tenants, databases, queries, identity resolution, campaigns, predictions, and more. Some clients limit the number of tools an agent can register -- Copilot Studio is one -- so connected clients may surface only a subset of the full tool surface. See :doc:`mcp_setup_m365_copilot` for options when you connect a tool-count-limited client. Tool count is approximate during beta and subject to change.
* Per-user isolation. Each request is authenticated and scoped to the calling user's identity, tenant, and permissions.
* Configurable safety modes for write operations. See :doc:`mcp_safety_modes`.


What it does not do
==================================================

* The MCP server does not bypass Amperity authorization. Users see only the tenants and operations their credentials allow.
* The MCP server does not store conversation history. Per-token session state -- selected tenant and safety mode -- persists across requests within the same session.
* The MCP server is not a replacement for the Amperity REST API. Use the :doc:`overview` for programmatic integrations that do not involve an AI agent.


Connect a client
==================================================

Choose a setup guide for your client:

* :doc:`mcp_setup_m365_copilot` -- the primary supported integration
* :doc:`mcp_setup_claude` -- Claude.ai, Claude Desktop, and Claude Code
* :doc:`mcp_setup_chatgpt` -- ChatGPT custom connectors
