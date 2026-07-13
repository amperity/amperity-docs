.. https://docs.amperity.com/api/


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

The Amperity MCP server gates write operations behind a per-session safety mode. The safety mode controls if tools that create, update, or delete data can run on production tenants. Safety modes are scoped to the calling user's session. A user's safety mode setting does not affect another user's safety mode setting.

.. mcp-safety-modes-end



.. note::

   The agent can call the **safety_set_mode** tool to change the current session's mode. Treat the safety mode as a guardrail and not as a permission boundary. The true permission boundary is the tool permissions configured in your MCP client (for example, Claude's per-tool "Always allow," "Needs approval," and "Blocked" settings).



.. _mcp-safety-modes-table:

Available modes
==================================================

.. mcp-safety-modes-table-start

The default safety mode for new sessions is **strict**, which restricts write operations to sandbox tenants. Safety mode :ref:`must be switched <mcp-safety-modes-setup>` to allow write operations to a production tenant.

Safety mode has the following options:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Mode
     - Production tenant
     - Sandbox tenant
   * - **strict** (default)
     - Write operations are blocked. Read operations are allowed.
     - Read and write operations are allowed.

       Use **strict** for exploring the tool surface or testing prompts. The MCP server allows read and write operations to sandboxes, which allows meaningful work to occur within a sandbox and prevents write operations to the production tenant.

   * - **confirm**
     - Write operations require an explicit **confirm: true** argument from the agent.

       Use **confirm** for routine work against production tenants. Each write operation requires the agent to pass **confirm: true**, which surfaces the change for human review.

     - Read and write operations are allowed.
   * - **unrestricted**
     - All operations are allowed without explicit confirmation.

       .. caution:: Use **unrestricted** only for scripted, audited automations or in contexts where you accept full responsibility for the outcome of write operations.

     - Read and write operations are allowed.

.. mcp-safety-modes-table-end


.. _mcp-safety-modes-setup:

Set the safety mode
==================================================

.. mcp-safety-modes-setup-start

The MCP server exposes tools to read and update the safety mode for the current session. Ask your agent to set the safety mode with the following statement:

.. code-block:: none

   Set the Amperity safety mode to <mode>.

For example:

.. code-block:: none

   Set the Amperity safety mode to confirm.

The agent calls the **safety_set_mode** tool, after which the setting updates immediately and persists for the remainder of the session unless changed. You can read the current mode with **safety_get_mode**.

.. mcp-safety-modes-setup-end


.. _mcp-safety-modes-confirm:

"confirm: true" may be required
==================================================

.. mcp-safety-modes-confirm-start

Some tools in the MCP server, such as scheduling a campaign, running a courier group, or running an orchestration group, always require confirmation regardless of the session safety mode. This is because these actions send data to downstream systems that exist outside of Amperity. 

.. note:: The **campaign_schedule**, **courier_group_run**, and **orchestration_group_run** tools always require safety mode to be set to **unrestricted** *and* always require **confirm: true**. If either are missing the tool is not allowed to run.

Tool descriptions returned by **tools/list** indicate when explicit confirmation is required.

.. mcp-safety-modes-confirm-end
