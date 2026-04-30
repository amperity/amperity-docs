.. https://docs.amperity.com/api/mcp_tool_reference.html


.. meta::
    :description lang=en:
        A domain-grouped reference of the tools exposed by the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        A domain-grouped reference of the tools exposed by the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        MCP tool reference


==================================================
MCP tool reference
==================================================

.. mcp-tool-reference-start

The Amperity MCP server exposes more than 200 tools across the Amperity surface. Tools are grouped here by domain. For the canonical, machine-readable list, send a ``tools/list`` request from your MCP client -- the result reflects the exact tool surface available to your account.

.. mcp-tool-reference-end


How to discover tools
==================================================

Most MCP clients call ``tools/list`` automatically when they connect. To inspect the surface from a chat:

   *"List the Amperity tools available to you."*

The client returns each tool's name, description, and input schema. The names below match the tool names returned by ``tools/list``.


Tenants and sessions
==================================================

Manage which Amperity tenant the current session targets, and configure session-level safety.

* ``tenant_list``, ``tenant_use``, ``tenant_info``, ``tenant_resync`` -- list, switch, and refresh tenants.
* ``sandbox_create``, ``sandbox_push``, ``sandbox_pull``, ``sandbox_compare`` -- manage sandbox tenants and merges.
* ``safety_get_mode``, ``safety_set_mode`` -- read and set the session :doc:`safety mode <mcp_safety_modes>`.


Databases and tables
==================================================

Operate Amperity Customer 360 databases, datasets, and the underlying tables.

* ``database_*`` -- create, run, validate, and manage Customer 360 databases and their tables.
* ``dataset_*`` -- read dataset catalogs and inspect tables.
* ``core_table_*`` -- inspect, upsert, and delete core tables.
* ``domain_table_history_*`` -- review domain table history.
* ``domain_transform_*`` -- manage domain transforms.
* ``table_run_history_*`` -- inspect run history for individual tables.


Queries
==================================================

Author, run, and organize queries against Amperity data.

* ``queries_*`` -- create, update, run, activate, and delete queries.
* ``query_run``, ``query_get_column_stats`` -- run ad hoc queries and inspect column statistics.
* ``query_folder_*`` -- organize queries into folders.


Identity resolution (Stitch)
==================================================

Run, inspect, and tune Amperity's identity resolution.

* ``stitch_run`` -- run Stitch.
* ``stitch_get_report``, ``stitch_lookup_record``, ``stitch_explain_pair`` -- inspect Stitch results and explain match pairs.
* ``stitch_get_settings``, ``stitch_update_settings``, ``stitch_set_table_availability`` -- read and update Stitch configuration.
* ``stitch_list_benchmarks``, ``stitch_get_benchmark_examples``, ``stitch_get_benchmark_history`` -- review benchmark coverage.


Bridges
==================================================

Manage data bridges between Amperity and external systems.

* ``bridge_list``, ``bridge_get``, ``bridge_create``, ``bridge_update``, ``bridge_delete`` -- manage bridge configuration.
* ``bridge_connect``, ``bridge_disconnect`` -- control bridge connection state.
* ``bridge_run_sync``, ``bridge_get_sync``, ``bridge_update_sync`` -- run and inspect bridge syncs.
* ``bridge_create_share``, ``bridge_get_share``, ``bridge_delete_share``, ``bridge_list_share_tables`` -- manage share configuration.
* ``bridge_upload_credential``, ``bridge_download_credential`` -- manage bridge credentials.
* ``bridge_load_amperity_data`` -- load Amperity data through a bridge.


Couriers, feeds, and destinations
==================================================

Configure data movement into and out of Amperity.

* ``courier_*``, ``courier_group_*`` -- create, run, and manage couriers and courier groups.
* ``feed_*`` -- manage feeds.
* ``destination_*`` -- manage destinations and target templates.


Orchestrations
==================================================

Schedule and run orchestrations and orchestration groups.

* ``orchestration_*`` -- create, update, run, and delete orchestrations.
* ``orchestration_group_*`` -- manage orchestration groups.


Campaigns and journeys
==================================================

Manage campaign drafts, campaign folders, journeys, and audience slices.

* ``campaign_*``, ``campaign_folder_*`` -- create, update, schedule, and organize campaigns.
* ``journey_*`` -- manage journeys.
* ``slice_*`` -- manage audience slices.
* ``label_*`` -- manage labels applied to campaigns and other resources.


Predictions
==================================================

Configure and run prediction models.

* ``prediction_create_model``, ``prediction_update_model``, ``prediction_delete_model``, ``prediction_get_model``, ``prediction_list_models`` -- model lifecycle.
* ``prediction_*_model_config`` -- model configuration management.
* ``prediction_run_workflow``, ``prediction_get_run_history``, ``prediction_get_full_job_history`` -- run and inspect prediction workflows.
* ``prediction_get_validation_results``, ``prediction_get_model_config_validation_results`` -- inspect validation output.


Profile collections and real-time segments
==================================================

* ``profile_collection_*`` -- create, update, run, and manage profile collections, including their attributes.
* ``real_time_segment_*`` -- create and manage real-time segments.


AI insights (Gnosis)
==================================================

Generate, read, and submit insights, themes, alerts, recommendations, and segments via Amperity's Gnosis service.

* ``gnosis_create_run``, ``gnosis_get_run``, ``gnosis_update_run``, ``gnosis_delete_run``, ``gnosis_list_runs``, ``gnosis_publish_run`` -- run lifecycle.
* ``gnosis_get_*``, ``gnosis_submit_*`` -- read or submit insights, themes, alerts, recommendations, segments, and executive summaries.


Events
==================================================

Manage event streams and event types.

* ``event_stream_*`` -- create, update, list, and inspect event streams; read recent events.
* ``event_type_*`` -- manage event type definitions.


Custom domain (Iq) and assets
==================================================

* ``iq_*``, ``iq_folder_*`` -- manage Iq objects and folders.
* ``assets_get_company_context_document``, ``assets_list_company_context_documents`` -- read company context assets.


Configuration history and recovery
==================================================

Inspect configuration changes and revert to prior versions.

* ``config_history_search``, ``config_history_get_version_nodes``, ``config_history_diff_node`` -- search and inspect history.
* ``config_revert_compare_revert``, ``config_revert_revert`` -- compare and revert configuration.
* ``comp_graph_get``, ``comp_graph_get_dependencies``, ``comp_graph_get_dependents`` -- inspect the configuration computation graph.


Workflows and compute
==================================================

Inspect Amperity workflows and Spark execution.

* ``workflow_list``, ``workflow_get_status``, ``workflow_resolve_task``, ``workflow_cancel`` -- inspect and manage running workflows.
* ``spark_*`` -- inspect Spark applications, jobs, stages, executors, SQL, and storage.
* ``compute_get_settings``, ``compute_update_settings`` -- read and update compute settings.


Alerts and training
==================================================

* ``alert_list_subscriptions``, ``alert_get_subscription``, ``alert_subscribe``, ``alert_unsubscribe`` -- manage alert subscriptions.
* ``training_setup_semantic_tags`` -- run training tasks for semantic tagging.
