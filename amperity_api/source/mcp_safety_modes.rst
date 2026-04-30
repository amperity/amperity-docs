.. https://docs.amperity.com/api/mcp_safety_modes.html


.. meta::
    :description lang=en:
        How the Amperity MCP server gates write operations using session safety modes.

.. meta::
    :content class=swiftype name=body data-type=text:
        How the Amperity MCP server gates write operations using session safety modes.

.. meta::
    :content class=swiftype name=title data-type=string:
        MCP safety modes


==================================================
MCP safety modes
==================================================

.. mcp-safety-modes-start

The Amperity MCP server gates write operations behind a per-session safety mode. The safety mode controls whether tools that create, update, or delete data can run without explicit confirmation. Safety modes are scoped to the calling user's session -- one user's setting does not affect any other user.

.. mcp-safety-modes-end


.. _mcp-safety-modes-table:

Available modes
==================================================

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Mode
     - Production tenant
     - Sandbox tenant
   * - ``strict``
     - All write operations are blocked.
     - All writes are allowed.
   * - ``confirm`` (default)
     - Write operations require an explicit ``confirm: true`` argument from the agent.
     - All writes are allowed.
   * - ``unrestricted``
     - All write operations are allowed without explicit confirmation.
     - All writes are allowed.

The default for new sessions is ``confirm``. This requires an AI agent to pass an explicit confirmation argument to any write operation against a production tenant, while leaving sandbox tenants unrestricted for fast iteration.


Set the safety mode
==================================================

The MCP server exposes tools to read and update the safety mode for the current session. Ask your agent to set the mode:

   *"Set the Amperity safety mode to strict."*

The agent calls the ``safety_set_mode`` tool. The new setting takes effect immediately and persists for the remainder of the session.


Recommendation
==================================================

* Use ``strict`` while you explore the tool surface or test prompts against production tenants.
* Use ``confirm`` (default) for routine work against production tenants.
* Use ``unrestricted`` only in sandbox tenants or when running scripted, audited automations.


Audit
==================================================

Every tool call is logged with the calling user, the tenant, and the tool name. Customer-facing audit logging for MCP-originated changes is on the roadmap. In the interim, contact your Amperity representative if you need an audit trail of MCP activity.
