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

The Amperity MCP server exposes tools across the Amperity surface, grouped here by domain. Tool names follow a ``domain_action`` convention -- for example, ``tenant_list`` or ``database_create_table``. For the canonical list available to your account, send a ``tools/list`` request from your MCP client (most clients do this automatically on connect, or you can ask your agent to list the available Amperity tools). The result reflects the exact tool surface your account is authorized to call.

.. mcp-tool-reference-end


Tenants and sessions
==================================================

Manage which Amperity tenant the current session targets, and read session-level safety configuration.

* ``tenant_list``, ``tenant_info``, ``tenant_use``, ``tenant_resync`` -- list, inspect, switch, and refresh tenants.
* ``sandbox_list``, ``sandbox_create``, ``sandbox_get_create_status``, ``sandbox_delete`` -- manage sandbox tenants.
* ``sandbox_get_status``, ``sandbox_compare``, ``sandbox_get_merge_warnings``, ``sandbox_pull``, ``sandbox_push`` -- inspect and merge sandbox state.
* ``safety_get_mode``, ``safety_set_mode`` -- read and set the session :doc:`safety mode <mcp_safety_modes>`.


Databases and tables
==================================================

Operate Amperity Customer 360 databases, datasets, and the underlying tables.

* ``database_list``, ``database_get_schema``, ``database_get_table``, ``database_list_tables`` -- inspect databases.
* ``database_create``, ``database_create_table``, ``database_update``, ``database_update_table`` -- create and update databases and tables.
* ``database_activate``, ``database_run``, ``database_discard`` -- manage database lifecycle.
* ``database_delete``, ``database_delete_table`` -- delete databases and tables.
* ``database_get_validation_report``, ``database_list_validation_reports`` -- inspect validation reports.
* ``dataset_get_catalog``, ``dataset_list_tables``, ``dataset_get_table`` -- read dataset catalogs and tables.
* ``core_table_list``, ``core_table_get``, ``core_table_get_tenant_schema``, ``core_table_analyze``, ``core_table_upsert``, ``core_table_delete`` -- manage core tables.
* ``domain_transform_list``, ``domain_transform_get``, ``domain_transform_upsert``, ``domain_transform_analyze``, ``domain_transform_delete`` -- manage domain transforms.
* ``domain_table_history_get_history`` -- inspect domain table history.
* ``table_run_history_list_runs``, ``table_run_history_get_run``, ``table_run_history_get_table_history`` -- inspect run history for tables.


Queries
==================================================

Author, run, and organize queries against Amperity data.

* ``queries_list``, ``queries_get``, ``queries_create``, ``queries_update``, ``queries_delete`` -- manage queries.
* ``queries_run``, ``queries_activate``, ``queries_discard``, ``queries_move`` -- run and manage query lifecycle.
* ``query_run``, ``query_get_column_stats`` -- run ad hoc queries and inspect column statistics.
* ``query_folder_list``, ``query_folder_get``, ``query_folder_create``, ``query_folder_update``, ``query_folder_delete`` -- organize queries into folders.


Identity resolution (Stitch)
==================================================

Run, inspect, and tune Amperity's identity resolution.

* ``stitch_run`` -- run Stitch.
* ``stitch_get_report``, ``stitch_list_recent_reports``, ``stitch_lookup_record``, ``stitch_explain_pair`` -- inspect Stitch results and explain match pairs.
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

* ``courier_list``, ``courier_get``, ``courier_create``, ``courier_update``, ``courier_delete``, ``courier_run`` -- manage couriers.
* ``courier_group_list``, ``courier_group_get``, ``courier_group_create``, ``courier_group_update``, ``courier_group_delete``, ``courier_group_run`` -- manage courier groups.
* ``feed_list``, ``feed_get``, ``feed_upsert``, ``feed_delete`` -- manage feeds.
* ``destination_list``, ``destination_get``, ``destination_create``, ``destination_update``, ``destination_delete`` -- manage destinations.
* ``destination_list_target_templates``, ``destination_get_target_template``, ``destination_create_target_template``, ``destination_delete_target_template`` -- manage destination target templates.


Orchestrations
==================================================

Schedule and run orchestrations and orchestration groups.

* ``orchestration_list``, ``orchestration_get``, ``orchestration_create``, ``orchestration_update``, ``orchestration_delete`` -- manage orchestrations.
* ``orchestration_group_list``, ``orchestration_group_get``, ``orchestration_group_create``, ``orchestration_group_update``, ``orchestration_group_delete``, ``orchestration_group_run`` -- manage orchestration groups.


Campaigns and journeys
==================================================

Manage campaigns, campaign folders, journeys, and labels.

* ``campaign_list``, ``campaign_get``, ``campaign_create``, ``campaign_update``, ``campaign_delete``, ``campaign_duplicate``, ``campaign_move`` -- manage campaigns.
* ``campaign_schedule`` -- schedule (or unschedule) a campaign send.
* ``campaign_folder_list``, ``campaign_folder_get``, ``campaign_folder_create``, ``campaign_folder_update``, ``campaign_folder_delete`` -- manage campaign folders.
* ``journey_list``, ``journey_get``, ``journey_create``, ``journey_update``, ``journey_delete`` -- manage journeys.
* ``label_list``, ``label_get``, ``label_create``, ``label_update``, ``label_delete`` -- manage labels.


Data export slices
==================================================

Slices define which tables from a database get exported to a destination via an orchestration.

* ``slice_list``, ``slice_get``, ``slice_create``, ``slice_update``, ``slice_delete`` -- manage database export slices (``slc-xxx``).


Predictions
==================================================

Configure and run prediction models.

* ``prediction_list_models``, ``prediction_get_model``, ``prediction_create_model``, ``prediction_update_model``, ``prediction_delete_model`` -- model lifecycle.
* ``prediction_list_model_configs``, ``prediction_get_model_config``, ``prediction_create_model_config``, ``prediction_delete_model_config``, ``prediction_activate_model_config``, ``prediction_save_model_settings`` -- model configuration.
* ``prediction_run_workflow``, ``prediction_get_run_history``, ``prediction_get_full_job_history`` -- run and inspect prediction workflows.
* ``prediction_get_validation_results``, ``prediction_get_model_config_validation_results`` -- inspect validation output.


Profile collections and real-time segments
==================================================

* ``profile_collection_list``, ``profile_collection_get``, ``profile_collection_create``, ``profile_collection_update``, ``profile_collection_delete`` -- manage profile collections.
* ``profile_collection_set_attribute``, ``profile_collection_delete_attribute``, ``profile_collection_refresh``, ``profile_collection_run`` -- manage attributes and runs.
* ``real_time_segment_list``, ``real_time_segment_get``, ``real_time_segment_create``, ``real_time_segment_update``, ``real_time_segment_delete`` -- manage real-time segments.


AI insights (Gnosis)
==================================================

Generate, read, and submit insights, themes, alerts, recommendations, and segments via Amperity's Gnosis service.

* ``gnosis_list_runs``, ``gnosis_get_run``, ``gnosis_create_run``, ``gnosis_update_run``, ``gnosis_delete_run``, ``gnosis_publish_run`` -- run lifecycle.
* ``gnosis_submit_insights``, ``gnosis_submit_recommendations``, ``gnosis_submit_alerts``, ``gnosis_submit_themes``, ``gnosis_submit_segments``, ``gnosis_submit_executive_summary`` -- submit content.
* ``gnosis_get_insights``, ``gnosis_get_recommendations``, ``gnosis_get_alerts``, ``gnosis_get_themes``, ``gnosis_get_segments``, ``gnosis_get_executive_summary`` -- read content.


Events
==================================================

Manage event streams and event types.

* ``event_stream_list``, ``event_stream_get``, ``event_stream_create``, ``event_stream_update``, ``event_stream_delete``, ``event_stream_get_recent_events`` -- manage event streams.
* ``event_type_list``, ``event_type_get``, ``event_type_create``, ``event_type_update``, ``event_type_delete`` -- manage event type definitions.


Custom domains (Iq) and assets
==================================================

* ``iq_list``, ``iq_get``, ``iq_create``, ``iq_update``, ``iq_delete``, ``iq_activate`` -- manage Iq objects.
* ``iq_folder_list``, ``iq_folder_get``, ``iq_folder_create``, ``iq_folder_update``, ``iq_folder_delete`` -- manage Iq folders.
* ``assets_list_company_context_documents``, ``assets_get_company_context_document`` -- read company context assets.


Configuration history and recovery
==================================================

Inspect configuration changes and revert to prior versions.

* ``config_history_search``, ``config_history_get_version_nodes``, ``config_history_diff_node`` -- search and inspect configuration history.
* ``config_revert_compare_revert``, ``config_revert_revert`` -- compare and revert configuration.
* ``comp_graph_get``, ``comp_graph_get_dependents``, ``comp_graph_get_dependencies`` -- inspect the configuration computation graph.


Workflows and compute
==================================================

Inspect Amperity workflows and Spark execution.

* ``workflow_list``, ``workflow_get_status``, ``workflow_cancel``, ``workflow_resolve_task`` -- inspect and manage workflows.
* ``spark_get_application``, ``spark_list_jobs``, ``spark_list_stages``, ``spark_get_stage``, ``spark_list_sql``, ``spark_get_sql``, ``spark_list_executors``, ``spark_get_environment``, ``spark_list_storage`` -- inspect Spark applications, jobs, stages, executors, SQL, and storage.
* ``compute_get_settings``, ``compute_update_settings`` -- read and update compute settings.


Alerts and training
==================================================

* ``alert_list_subscriptions``, ``alert_get_subscription``, ``alert_subscribe``, ``alert_unsubscribe`` -- manage alert subscriptions.
* ``training_setup_semantic_tags`` -- run training tasks for semantic tagging.
