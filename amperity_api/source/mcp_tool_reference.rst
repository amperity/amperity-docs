.. https://docs.amperity.com/api/


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

The Amperity MCP server exposes tools across the Amperity surface. Tool names follow a **domain_action** convention, such as **tenant_list** or **database_create_table**.

For the canonical list available to your account, send a **tools/list** request from your MCP client. Many clients do this automatically on connect. The list of tools returned by **tools/list** is the exact tool surface your account is authorized to call.

.. mcp-tool-reference-end


.. _mcp-tool-tenants:

Tenants and sessions
==================================================

Discover the tenants available to your account, and read session-level safety configuration. Every tenant-scoped tool takes a **tenant_id** argument -- an id from **tenant_list**, optionally stack-qualified as **stack:tenant_id** -- so each call names the tenant it runs against. There is no session-selected tenant to switch.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - List, inspect, and refresh tenants
     - **tenant_list**

       **tenant_info**

       **tenant_resync**

   * - Manage sandbox tenants
     - **sandbox_create**

       **sandbox_get_create_status**

       **sandbox_delete**

   * - Inspect and merge sandbox state
     - **sandbox_get_status**

       **sandbox_compare**

       **sandbox_get_merge_warnings**

       **sandbox_pull**

       **sandbox_push**

   * - Read and set the session :doc:`safety mode <mcp_safety_modes>`
     - **safety_get_mode**

       **safety_set_mode**

   * - Submit feedback to the Amperity team
     - **feedback_submit**


.. _mcp-tool-databases:

Databases and tables
==================================================

Operate Amperity Customer 360 databases, datasets, and the underlying tables.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Inspect databases
     - **database_list**

       **database_get_schema**

       **database_get_table**

       **database_list_tables**

   * - Create and update databases and tables
     - **database_create**

       **database_create_table**

       **database_update**

       **database_update_table**

   * - Manage database lifecycle
     - **database_activate**

       **database_run**

       **database_discard**

   * - Delete databases and tables
     - **database_delete**

       **database_delete_table**

   * - Inspect validation reports
     - **database_get_validation_report**

       **database_list_validation_reports**

   * - Read dataset catalogs and tables
     - **dataset_get_catalog**

       **dataset_list_tables**

       **dataset_get_table**

   * - Manage core tables
     - **core_table_list**

       **core_table_get**

       **core_table_get_tenant_schema**

       **core_table_analyze**

       **core_table_upsert**

       **core_table_delete**

   * - Manage domain transforms
     - **domain_transform_list**

       **domain_transform_get**

       **domain_transform_upsert**

       **domain_transform_analyze**

       **domain_transform_delete**

   * - Inspect domain table history
     - **domain_table_history_get_history**

   * - Inspect run history for tables
     - **table_run_history_list_runs**

       **table_run_history_get_run**

       **table_run_history_get_table_history**


.. _mcp-tool-queries:

Queries
==================================================

Author, run, and organize queries against Amperity data.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Manage queries
     - **queries_list**

       **queries_get**

       **queries_create**

       **queries_update**

       **queries_delete**

   * - Run and manage query lifecycle
     - **queries_run**

       **queries_activate**

       **queries_discard**

       **queries_move**

   * - Run ad hoc queries and inspect column statistics
     - **query_run**

       **query_get_column_stats**

   * - Organize queries into folders
     - **query_folder_list**

       **query_folder_get**

       **query_folder_create**

       **query_folder_update**

       **query_folder_delete**


.. _mcp-tool-identity-resolution:

Identity resolution
==================================================

Run, inspect, and tune identity resolution.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Run Stitch
     - **stitch_run**

   * - Inspect Stitch results and explain match pairs
     - **stitch_get_report**

       **stitch_list_recent_reports**

       **stitch_lookup_record**

       **stitch_explain_pair**

   * - Read and update Stitch configuration
     - **stitch_get_settings**

       **stitch_update_settings**

       **stitch_set_table_availability**

   * - Review benchmark coverage
     - **stitch_list_benchmarks**

       **stitch_get_benchmark_examples**

       **stitch_get_benchmark_history**


.. _mcp-tool-bridge:

Amperity Bridge
==================================================

Manage data bridges between Amperity and external systems.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Manage bridge configuration
     - **bridge_list**

       **bridge_get**

       **bridge_create**

       **bridge_update**

       **bridge_delete**

   * - Control bridge connection state
     - **bridge_connect**

       **bridge_disconnect**

   * - Run and inspect bridge syncs
     - **bridge_run_sync**

       **bridge_get_sync**

       **bridge_update_sync**

   * - Manage share configuration
     - **bridge_create_share**

       **bridge_get_share**

       **bridge_delete_share**

       **bridge_list_share_tables**

   * - Manage bridge credentials
     - **bridge_upload_credential**

       **bridge_download_credential**

   * - Load Amperity data through a bridge
     - **bridge_load_amperity_data**


.. _mcp-tool-couriers-feeds-destinations:

Couriers, feeds, and destinations
==================================================

Configure data movement into and out of Amperity.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Manage couriers
     - **courier_list**

       **courier_get**

       **courier_create**

       **courier_update**

       **courier_delete**

       **courier_run**

   * - Manage courier groups
     - **courier_group_list**

       **courier_group_get**

       **courier_group_create**

       **courier_group_update**

       **courier_group_delete**

       **courier_group_run**

   * - Manage feeds
     - **feed_list**

       **feed_get**

       **feed_upsert**

       **feed_delete**

   * - Manage destinations
     - **destination_list**

       **destination_get**

       **destination_create**

       **destination_update**

       **destination_delete**

   * - Manage destination target templates
     - **destination_list_target_templates**

       **destination_get_target_template**

       **destination_create_target_template**

       **destination_delete_target_template**


.. _mcp-tool-orchestrations:

Orchestrations
==================================================

Schedule and run orchestrations and orchestration groups.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Manage orchestrations
     - **orchestration_list**

       **orchestration_get**

       **orchestration_create**

       **orchestration_update**

       **orchestration_delete**

   * - Manage orchestration groups
     - **orchestration_group_list**

       **orchestration_group_get**

       **orchestration_group_create**

       **orchestration_group_update**

       **orchestration_group_delete**

       **orchestration_group_run**


.. _mcp-tool-campaigns-journeys:

Campaigns and journeys
==================================================

Manage campaigns, campaign folders, journeys, and audiences.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Manage campaigns
     - **campaign_list**

       **campaign_get**

       **campaign_create**

       **campaign_update**

       **campaign_delete**

       **campaign_duplicate**

       **campaign_move**

   * - Schedule or unschedule a campaign send
     - **campaign_schedule**

   * - Manage campaign folders
     - **campaign_folder_list**

       **campaign_folder_get**

       **campaign_folder_create**

       **campaign_folder_update**

       **campaign_folder_delete**

   * - Manage journeys
     - **journey_list**

       **journey_get**

       **journey_create**

       **journey_update**

       **journey_delete**

   * - Manage journey versions
     - **journey_list_versions**

       **journey_get_version**

       **journey_create_version**

       **journey_update_version**

   * - Run, schedule, and unschedule journeys
     - **journey_run**

       **journey_schedule**

       **journey_unschedule**

   * - Read a journey's node schema
     - **journey_get_node_schema**


.. _mcp-tool-data-exports:

Data exports
==================================================

Manage data exports.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Manage database export slices (**slc-xxx**)
     - **slice_list**

       **slice_get**

       **slice_create**

       **slice_update**

       **slice_delete**


.. _mcp-tool-predictions:

Predictions
==================================================

Configure and run prediction models.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Model lifecycle
     - **prediction_list_models**

       **prediction_get_model**

       **prediction_create_model**

       **prediction_update_model**

       **prediction_delete_model**

   * - Model configuration
     - **prediction_list_model_configs**

       **prediction_get_model_config**

       **prediction_create_model_config**

       **prediction_delete_model_config**

       **prediction_activate_model_config**

       **prediction_save_model_settings**

   * - Run and inspect prediction workflows
     - **prediction_run_workflow**

       **prediction_get_run_history**

       **prediction_get_full_job_history** 

   * - Inspect validation output
     - **prediction_get_validation_results**

       **prediction_get_model_config_validation_results**


.. _mcp-tool-segments:

Segments
==================================================

Manage segments and folders.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Manage segments
     - **iq_list**

       **iq_get**

       **iq_create**

       **iq_update**

       **iq_delete**

       **iq_activate**

   * - Manage segments folders
     - **iq_folder_list**

       **iq_folder_get**

       **iq_folder_create**

       **iq_folder_update**

       **iq_folder_delete**

   * - Read company context assets
     - **assets_list_company_context_documents**

       **assets_get_company_context_document**


.. _mcp-tool-configuration-history:

Configuration history and recovery
==================================================

Inspect configuration changes and revert to prior versions.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Search and inspect configuration history
     - **config_history_search**

       **config_history_get_version_nodes**

       **config_history_diff_node**

   * - Compare and revert configuration
     - **config_revert_compare_revert**

       **config_revert_revert**

   * - Inspect the configuration computation graph
     - **comp_graph_get**

       **comp_graph_get_dependents**

       **comp_graph_get_dependencies**


.. _mcp-tool-workflows-compute:

Workflows and compute
==================================================

Inspect Amperity workflows and Spark execution.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Inspect and manage workflows
     - **workflow_list**

       **workflow_get_status**

       **workflow_cancel**

       **workflow_resolve_task**

   * - Inspect Spark applications, jobs, stages, executors, SQL, and storage
     - **spark_get_application**

       **spark_list_jobs**

       **spark_list_stages**

       **spark_get_stage**

       **spark_list_sql**

       **spark_get_sql**

       **spark_list_executors**

       **spark_get_environment**

       **spark_list_storage**

   * - Read and update compute settings
     - **compute_get_settings**

       **compute_update_settings**


.. _mcp-tool-alerts-training:

Alerts and training
==================================================

Manage alert subscriptions and run training tasks for semantic tagging.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Manage alert subscriptions
     - **alert_list_subscriptions**

       **alert_get_subscription**

       **alert_subscribe**

       **alert_unsubscribe**

   * - Run training tasks for semantic tagging
     - **training_setup_semantic_tags**


.. _mcp-tool-deep-links:

Deep links
==================================================

Build deep-link URLs to Amperity UI pages. Constructed locally, with no API call.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Description
     - Tools

   * - Build a deep-link URL to an Amperity UI page
     - **build_object_url**
