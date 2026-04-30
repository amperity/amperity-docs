.. https://docs.amperity.com/api/mcp_authentication.html


.. meta::
    :description lang=en:
        How the Amperity MCP server authenticates clients using OAuth 2.1 with PKCE.

.. meta::
    :content class=swiftype name=body data-type=text:
        How the Amperity MCP server authenticates clients using OAuth 2.1 with PKCE.

.. meta::
    :content class=swiftype name=title data-type=string:
        MCP authentication


==================================================
MCP authentication
==================================================

.. mcp-authentication-start

The Amperity MCP server uses OAuth 2.1 with PKCE for client authentication. Each request to the server must include a valid bearer token in the ``Authorization`` header. Tokens are issued by Amperity's identity provider after a user signs in.

.. mcp-authentication-end


.. _mcp-authentication-flow:

Authorization flow
==================================================

The MCP server uses the OAuth 2.0 authorization code flow with the PKCE extension (`RFC 7636 <https://datatracker.ietf.org/doc/html/rfc7636>`__). This is the recommended flow for public clients that cannot store a client secret.

The high-level flow:

1. The client reads OAuth metadata from the discovery document at ``/.well-known/oauth-authorization-server``.
2. The client generates a PKCE code verifier and challenge.
3. The client opens a browser to the authorization endpoint, including the code challenge.
4. The user signs in with Amperity credentials and consents to the requested scopes.
5. The authorization server returns an authorization code to the client.
6. The client exchanges the code for an access token at the token endpoint, including the PKCE code verifier.
7. The client uses the access token in the ``Authorization`` header on requests to ``/mcp``.


.. _mcp-authentication-client-id:

Client identification
==================================================

There are two supported ways for a client to identify itself.

**Dynamic Client Registration (recommended).** The MCP server supports `RFC 7591 <https://datatracker.ietf.org/doc/html/rfc7591>`__ Dynamic Client Registration. Clients that support DCR call ``POST https://mcp.amperity.com/oauth/register`` to obtain a per-installation client identifier. Most modern MCP clients use DCR automatically.

**Pre-configured client identifier.** Clients that do not support DCR can use the static identifier published in the OAuth discovery document at ``/.well-known/oauth-authorization-server``. The static client identifier is a public value -- there is no client secret -- and is safe to embed in client configuration.


.. _mcp-authentication-tokens:

Tokens
==================================================

The MCP server requires a bearer access token on every request:

::

   Authorization: Bearer <access-token>

The MCP server validates incoming tokens against Auth0 and proxies the token through to downstream Amperity API calls.

Tokens expire. When a token expires, the client receives a 401 response. Most MCP clients handle the refresh transparently. If yours does not, sign in again to obtain a fresh token.


.. _mcp-authentication-tenants:

Tenants and scoping
==================================================

After authentication, the MCP server scopes every tool call to the calling user's identity. If your account belongs to multiple tenants, the MCP session begins without a tenant selected. Use the ``tenant.list`` and ``tenant.use`` tools to select a tenant for the session.

The current tenant selection is stored per-token on the server and persists across subsequent requests on the same token.


.. _mcp-authentication-permissions:

Permissions
==================================================

Tool calls are subject to your user's permissions on the selected tenant. The MCP server does not bypass authorization. If a tool call fails with a permissions error, your account does not have the required role on the current tenant.


References
==================================================

* `Model Context Protocol authorization <https://modelcontextprotocol.io/specification/basic/authorization>`__
* `OAuth 2.1 <https://oauth.net/2.1/>`__
* `RFC 7636 -- PKCE <https://datatracker.ietf.org/doc/html/rfc7636>`__
* `RFC 7591 -- Dynamic Client Registration <https://datatracker.ietf.org/doc/html/rfc7591>`__
