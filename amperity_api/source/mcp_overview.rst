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

The MCP server is hosted by Amperity. Customers connect to a single public endpoint and authenticate by using their existing Amperity credentials. There is nothing to install or run locally.

.. mcp-overview-end


.. admonition:: Beta

   The Amperity MCP server is available as a private beta. Tool surface, configuration, and behavior may change as the beta progresses. Contact your Amperity representative for access.


What it enables
==================================================

* Conversational access to Amperity from Copilot Studio, Claude, ChatGPT, and other MCP-compatible clients.
* More than 200 tools across tenants, databases, queries, identity resolution, campaigns, predictions, and more. Some clients enforce a per-agent tool ceiling -- for example, Copilot Studio supports up to 70 tools per agent -- and surface only a subset of the full tool surface. See :doc:`mcp_setup_m365_copilot` for options when you connect a tool-count-limited client. Tool count is approximate during beta and subject to change.
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
* :doc:`mcp_setup_claude` -- Claude Desktop and Claude Code
* :doc:`mcp_setup_chatgpt` -- ChatGPT custom connectors

For details about connection metadata, OAuth flow, and the public endpoint, see :doc:`mcp_connect`.
