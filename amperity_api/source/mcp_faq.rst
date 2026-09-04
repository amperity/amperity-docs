.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Answers to common questions about the Amperity MCP server, including authentication, permissions, PII handling, and auditability.

.. meta::
    :content class=swiftype name=body data-type=text:
        Answers to common questions about the Amperity MCP server, including authentication, permissions, PII handling, and auditability.

.. meta::
    :content class=swiftype name=title data-type=string:
        MCP FAQ


==================================================
MCP FAQ
==================================================

.. mcp-faq-start

This page answers common questions about the Amperity MCP server.

.. mcp-faq-end


.. _mcp-faq-permissions:

Permissions and data access
==================================================

.. mcp-faq-permissions-start

.. mcp-faq-permissions-end


.. _mcp-faq-permission-model:

Does the MCP server have its own permission model?
--------------------------------------------------

.. mcp-faq-permission-model-start

No. **The MCP server is a new interface to Amperity, not a new path into your data.**

The MCP server does not evaluate permissions. It forwards the calling user's credentials to the same Amperity APIs that serve the Amperity user interface, and as such inherits the same permissions and restrictions. Authorization is enforced once, in the platform, for every caller.

The practical consequence: **a user's MCP permissions are a mirror of their permissions in the Amperity user interface.** Every permission, policy option, and resource group restriction that applies to a user in Amperity applies to that same user through MCP. If a user cannot see a database, a table, or a field when signed in to Amperity, they cannot see it through an AI client either. When a user attempts something their policies do not allow, the tool call fails and the agent is told that the user lacks the required permission.

MCP is not a privilege escalation path. To change what a user can do through MCP, change their policies--the same way you would for any other Amperity user.

.. mcp-faq-permission-model-end


.. _mcp-faq-pii:

How is PII handled?
--------------------------------------------------

.. mcp-faq-pii-start

PII protection in Amperity has two parts, and both apply to MCP.

#. **Mark the fields.** Individual fields in a database table are marked as PII with the **PII** checkbox in the table editor. Amperity selects this checkbox automatically for columns tagged with profile (PII) semantics. See `Mark columns as PII <https://docs.amperity.com/reference/databases.html#databases-database-howto-mark-columns-as-pii>`__.

#. **Restrict the users.** The `Restrict PII access <https://docs.amperity.com/reference/policies.html#policies-option-restrict-pii>`__ policy option prevents a user from viewing data that is marked as PII.

The MCP server performs no redaction of its own and has no ability to bypass these controls. Tools that return profile data require PII read authorization from the platform, and a user without it receives a permission error instead of the data. This is the same enforcement that hides PII from a restricted user on the **Queries** and **Segments** pages.

.. important:: Tool results returned to an authorized user may include PII. You are responsible for confirming that the AI client and model you connect are approved to handle this data under your organization's policies and any agreements with the model provider. See :ref:`What is not enabled? <mcp-what-mcp-not-enabled>`.

.. mcp-faq-pii-end


.. _mcp-faq-resource-groups:

Do resource groups apply to MCP?
--------------------------------------------------

.. mcp-faq-resource-groups-start

Yes. Resource groups scope which databases a user can interact with, and that scoping is applied by the same authorization layer that serves the Amperity user interface. A user assigned to a custom resource group sees only the databases in that resource group, whether they are working in Amperity or through an AI client.

See `Resource groups <https://docs.amperity.com/reference/resource_groups.html>`__ and `Database permissions <https://docs.amperity.com/reference/resource_groups.html#settings-security-resource-groups-database-permissions>`__.

.. mcp-faq-resource-groups-end


.. _mcp-faq-policy-options:

Which policy options apply to MCP?
--------------------------------------------------

.. mcp-faq-policy-options-start

Policy options attach to a user's standard policy and restrict specific actions. They apply through MCP exactly as they apply in the Amperity user interface.

For the full list, see `Policy options <https://docs.amperity.com/reference/policies.html#policy-options>`__.

.. mcp-faq-policy-options-end


.. _mcp-faq-authentication:

Authentication and identity
==================================================

.. mcp-faq-authentication-start

.. mcp-faq-authentication-end


.. _mcp-faq-how-authenticate:

How do users authenticate to the MCP server?
--------------------------------------------------

.. mcp-faq-how-authenticate-start

Users authenticate with OAuth 2.1 using the authorization code flow with Proof Key for Code Exchange (PKCE). The MCP server is registered as a public client and does not use a client secret.

PKCE is required, not merely supported. The authorization endpoint rejects any request that does not include a code challenge with **code_challenge_method=S256**.

Every request to the MCP server carries a bearer token that is verified before any tool runs. Tokens are signed with RS256 and are bound to the Amperity API audience. A token that cannot be validated is rejected and the request fails with a **401** response.

.. mcp-faq-how-authenticate-end


.. _mcp-faq-service-accounts:

Is there a service account or static API key?
--------------------------------------------------

.. mcp-faq-service-accounts-start

No. There is no service account, no shared secret, and no static API key.

The calling identity is always a named human user. Each user signs in with their own Amperity credentials, and the MCP server forwards that user's token to the Amperity API, which performs authorization. Two users connected to the same tenant have exactly the access their own accounts grant them.

Sessions are also isolated per conversation. Two conversations opened under the same login are tracked separately.

.. mcp-faq-service-accounts-end


.. _mcp-faq-sso:

Does MCP work with our identity provider?
--------------------------------------------------

.. mcp-faq-sso-start

Yes. The MCP server uses the same single sign-on configuration as the rest of Amperity. If your tenant signs in to Amperity through your SAML identity provider, users sign in to the MCP server the same way. No separate identity configuration is required.

Because the identity provider is shared, deprovisioning a user in your identity provider removes their access to the MCP server along with their access to Amperity.

.. mcp-faq-sso-end


.. _mcp-faq-logging:

Logging and auditability
==================================================

.. mcp-faq-logging-start

.. mcp-faq-logging-end


.. _mcp-faq-audit:

Are actions taken through MCP audited?
--------------------------------------------------

.. mcp-faq-audit-start

Yes. Because MCP calls the same Amperity APIs as the user interface, actions taken through MCP are recorded in activity logs and configuration version history the same way they would be if the user had performed them in Amperity directly.

Audit events and configuration versions additionally record how the action was initiated, so an action taken through MCP is distinguishable from the same action taken in the user interface. In Amperity, these entries are labeled **via Amperity MCP**.

.. mcp-faq-audit-end


.. _mcp-faq-log-export:

Can audit logs be exported to a SIEM?
--------------------------------------------------

.. mcp-faq-log-export-start

Yes, by pull. Use the :doc:`GET /audit-events <endpoint_get_audit_events_list>` endpoint to retrieve user activity for your tenant. Activity is also available in the Amperity user interface under **Settings**, and may be filtered and downloaded from there. See `About activity logs <https://docs.amperity.com/reference/activity_logs.html>`__.

.. mcp-faq-log-export-end


.. _mcp-faq-data-handling:

Data handling
==================================================

.. mcp-faq-data-handling-start

.. mcp-faq-data-handling-end


.. _mcp-faq-llm:

Does Amperity send my data to a model provider?
--------------------------------------------------

.. mcp-faq-llm-start

No. The MCP server does not call any large language model. It returns tool results to the AI client that requested them, and nothing else.

The model that processes those results is the one in the client you connect, under your own agreement with that provider. Choosing that client and confirming it is approved to handle your data is your organization's decision.

.. note:: This is a different architecture from `AmpAI <https://docs.amperity.com/reference/ampai.html>`__, which is a first-party Amperity feature. For how AmpAI handles data, see the `AmpAI Privacy FAQ <https://docs.amperity.com/reference/ampai_privacy.html>`__.

.. mcp-faq-llm-end


.. _mcp-faq-conversation-history:

Does the MCP server store conversation history?
--------------------------------------------------

.. mcp-faq-conversation-history-start

No. The MCP server stores no conversation history and retains no tenant data.

The only state the MCP server keeps between requests is the session context: the selected tenant, the current safety mode, and the identity of the connected client. Tenant data is never written to that store.

Your AI client may retain conversation history according to its own settings and your organization's configuration of it. Check that client's data retention policy.

.. mcp-faq-conversation-history-end


.. _mcp-faq-tool-surface:

Tool surface and write operations
==================================================

.. mcp-faq-tool-surface-start

.. mcp-faq-tool-surface-end


.. _mcp-faq-tool-list:

What tools does the MCP server expose?
--------------------------------------------------

.. mcp-faq-tool-list-start

The complete list is published in the :doc:`MCP tool reference <mcp_tool_reference>`, organized by domain. More than 200 tools are available, and the connected client can enumerate them at any time.

Which tools a given user can successfully call depends on that user's permissions. The tool being listed does not mean the user is authorized to run it.

Many AI clients also provide their own controls for enabling and disabling individual tools, which you can use to narrow the tool surface further for a given user or agent. See :ref:`Is the MCP server read-only? <mcp-faq-read-only>`.

.. mcp-faq-tool-list-end


.. _mcp-faq-read-only:

Is the MCP server read-only?
--------------------------------------------------

.. mcp-faq-read-only-start

No. Write operations are part of the tool surface--creating segments, running identity resolution, scheduling campaigns--and they are gated by two independent controls:

#. **The user's permissions.** A user without permission to perform an action cannot perform it through MCP. This is the permission boundary.

#. **The session's** :doc:`safety mode <mcp_safety_modes>`. The default mode, **strict**, blocks all write operations against production tenants while allowing reads. Write operations against sandbox tenants remain available, so users can do meaningful work without risk to production.

.. important:: Safety mode is a guardrail, not a permission boundary. It limits what an agent may attempt within a session; it does not grant or remove access. Authorization is always enforced by the user's policies.

Every tool the MCP server advertises is also tagged with the standard MCP behavioral annotations that describe what calling it would do: **readOnlyHint**, **destructiveHint**, **idempotentHint**, and **openWorldHint**. See `Tools <https://modelcontextprotocol.io/specification/latest/server/tools>`__ |ext_link| in the Model Context Protocol specification.

Many AI clients expose tool-level permission controls that read these annotations, which lets you approve or block individual tools--or restrict a connection to read-only tools--in the client itself. Using those controls is the recommended way to narrow the tool surface for a given user or agent, alongside the Amperity policies that determine what that user is authorized to do.

.. mcp-faq-read-only-end


.. _mcp-faq-connecting:

Connecting a client
==================================================

.. mcp-faq-connecting-start

.. mcp-faq-connecting-end


.. _mcp-faq-unlisted-client:

Can I connect a tool that has no setup page?
--------------------------------------------------

.. mcp-faq-unlisted-client-start

Yes. Any client that implements the Model Context Protocol should be able to connect.

The Amperity MCP server implements the protocol and its standard OAuth authorization flow rather than special-casing individual clients. A client that supports remote MCP servers over HTTP and signs in with OAuth 2.1 and PKCE can connect to **https://mcp.amperity.com**.

Most clients need no manual configuration. The MCP server publishes standard OAuth metadata and supports dynamic client registration, so a client discovers the endpoints and registers itself as a public PKCE client without a client secret. Point the client at the server URL and sign in.

Clients that cannot discover or register automatically need these values entered by hand:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Value

   * - Server or resource URL
     - ``https://mcp.amperity.com``

   * - Authorization endpoint
     - ``https://mcp.amperity.com/authorize``

   * - Token endpoint
     - ``https://mcp.amperity.com/oauth/token``

   * - Registration endpoint
     - ``https://mcp.amperity.com/oauth/register``

   * - Client ID
     - ``nwbd0MGCyh1VysmYQM05UoDXIuVPdGEs``

       This is Amperity's public MCP client ID. It is the same for every customer and is not a secret.

   * - Client secret
     - None. The MCP server is a public OAuth client that uses PKCE and does not issue a client secret. If a client requires the field to be non-empty, supply any placeholder value.

   * - Grant types
     - ``authorization_code``, ``refresh_token``

   * - Scopes
     - ``openid``, ``offline_access``

   * - PKCE
     - Required. The authorization endpoint rejects any request that does not use ``code_challenge_method=S256``.

.. important:: Hosted clients complete the sign-in flow by redirecting to their own callback address, and that address must be on Amperity's redirect URI allowlist.

   If a hosted tool's callback address has not been approved, the sign-in request is rejected. Contact Amperity to have the address reviewed and added.

.. mcp-faq-unlisted-client-end
