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

The Amperity MCP server gates write operations behind a per-session safety mode. The safety mode controls whether tools that create, update, or delete data can run on production tenants. Safety modes are scoped to the calling user's session -- one user's setting does not affect any other user.

.. mcp-safety-modes-end

.. note::

   The safety mode model is being evaluated and may change during beta as Amperity moves toward more granular access controls. The agent itself can call ``safety_set_mode`` to change the current session's mode -- treat the safety mode as a guardrail, not a permission boundary, and pair it with the access controls on the underlying Amperity tenant.


.. _mcp-safety-modes-table:

Available modes
==================================================

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Mode
     - Production tenant
     - Sandbox tenant
   * - ``strict`` (default)
     - Write operations are blocked. Reads are allowed.
     - Reads and writes are allowed.
   * - ``confirm``
     - Write operations require an explicit ``confirm: true`` argument from the agent.
     - Reads and writes are allowed.
   * - ``unrestricted``
     - All operations are allowed without explicit confirmation.
     - Reads and writes are allowed.

The default mode for new sessions is ``strict``, which restricts writes to sandbox tenants. Switch modes when you are ready to write to production.


Set the safety mode
==================================================

The MCP server exposes tools to read and update the safety mode for the current session. Ask your agent to set the mode:

   "Set the Amperity safety mode to confirm."

The agent calls the ``safety_set_mode`` tool. The new setting takes effect immediately and persists for the remainder of the session. You can read the current mode with ``safety_get_mode``.


Recommended usage
==================================================

* Use ``strict`` (default) while you explore the tool surface or test prompts. The MCP server still allows full read access and full sandbox writes -- you can do meaningful work without unlocking production writes.
* Use ``confirm`` for routine work against production tenants. Each write requires the agent to pass ``confirm: true``, which surfaces the change for human review.
* Use ``unrestricted`` only for scripted, audited automations or in contexts where you accept full responsibility for write actions.


Confirm-required operations
==================================================

Some tools always require ``confirm: true`` regardless of the session safety mode. Examples include external send operations such as ``campaign_schedule`` and ``orchestration_group_run``. The tool descriptions returned by ``tools/list`` indicate when explicit confirmation is required.
