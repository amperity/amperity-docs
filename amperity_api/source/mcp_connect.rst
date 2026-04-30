.. https://docs.amperity.com/api/mcp_connect.html


.. meta::
    :description lang=en:
        The connection details, OAuth metadata, and authentication flow for the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        The connection details, OAuth metadata, and authentication flow for the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect to the Amperity MCP server


==================================================
Connect to the Amperity MCP server
==================================================

.. mcp-connect-start

The Amperity MCP server is hosted by Amperity at a single public endpoint. Connect any MCP-compatible client by configuring the endpoint URL and completing an OAuth login.

.. mcp-connect-end


Endpoint
==================================================

The MCP server is available at:

::

   https://mcp.amperity.com

This endpoint speaks the Model Context Protocol over HTTP using the streamable transport. All requests must include a valid bearer token in the ``Authorization`` header.


Authentication summary
==================================================

The MCP server uses OAuth 2.1 with PKCE. Most MCP clients handle the OAuth flow automatically -- on first connect, the client opens a browser, sends you to Amperity's identity provider, and receives a token after you sign in. The discovery table below lists the values clients use when manual configuration is required.


.. _mcp-connect-discovery:

OAuth discovery
==================================================

The MCP server publishes OAuth 2.0 Authorization Server metadata at a well-known URL. Clients that support automatic discovery read this document to find the authorization, token, and registration endpoints.

::

   https://mcp.amperity.com/.well-known/oauth-authorization-server

The discovery document advertises the following:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Value
   * - ``issuer``
     - ``https://amperity.auth0.com/``
   * - ``authorization_endpoint``
     - ``https://mcp.amperity.com/authorize``
   * - ``token_endpoint``
     - ``https://mcp.amperity.com/oauth/token``
   * - ``registration_endpoint``
     - ``https://mcp.amperity.com/oauth/register``
   * - ``response_types_supported``
     - ``["code"]``
   * - ``grant_types_supported``
     - ``["authorization_code"]``
   * - ``code_challenge_methods_supported``
     - ``["S256"]``
   * - ``token_endpoint_auth_methods_supported``
     - ``["none"]``

A static client identifier is also published in the same discovery document for clients that do not support Dynamic Client Registration. The static identifier is a public value -- there is no client secret -- and is safe to embed in client configuration.


First-time connect
==================================================

The first time you connect a new client:

1. The client reads OAuth metadata from ``/.well-known/oauth-authorization-server``.
2. The client opens a browser window and sends you to ``https://mcp.amperity.com/authorize``.
3. You sign in with your Amperity credentials. If you belong to multiple tenants, you may be prompted to select one.
4. The browser returns to the client with an authorization code, which the client exchanges for an access token.
5. The client connects to ``https://mcp.amperity.com`` with the access token. Subsequent requests reuse the token until it expires.

After the token expires, most clients refresh automatically or prompt you to sign in again.
