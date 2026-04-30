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

The Amperity MCP server exposes tools across the Amperity surface. Tools are grouped here by domain. Tool names follow a ``domain.action`` convention -- for example, ``tenant.list`` or ``database.create_table``. For the canonical list available to your account, send a ``tools/list`` request from your MCP client; the result reflects the exact tool surface your account is authorized to call.

.. mcp-tool-reference-end


How to discover tools
==================================================

Most MCP clients call ``tools/list`` automatically when they connect. To inspect the surface from a chat:

   *"List the Amperity tools available to you."*

The client returns each tool's name, description, and input schema. The names below match the tool names returned by ``tools/list``.


Tenants and sessions
==================================================

Manage which Amperity tenant the current session targets, and read session-level safety configuration.

* ``tenant.list``, ``tenant.info``, ``tenant.use``, ``tenant.resync`` -- list, inspect, switch, and refresh tenants.
* ``sandbox.list``, ``sandbox.create``, ``sandbox.get_create_status``, ``sandbox.delete`` -- manage sandbox tenants.
* ``sandbox.get_status``, ``sandbox.compare``, ``sandbox.get_merge_warnings``, ``sandbox.pull``, ``sandbox.push`` -- inspect and merge sandbox state.
* ``safety.get_mode``, ``safety.set_mode`` -- read and set the session :doc:`safety mode <mcp_safety_modes>`.


Databases and tables
==================================================

Operate Amperity Customer 360 databases, datasets, and the underlying tables.

* ``database.list``, ``database.get_schema``, ``database.get_table``, ``database.list_tables`` -- inspect databases.
* ``database.create``, ``database.create_table``, ``database.update``, ``database.update_table`` -- create and update databases and tables.
* ``database.activate``, ``database.run``, ``database.discard`` -- manage database lifecycle.
* ``database.delete``, ``database.delete_table`` -- delete databases and tables.
* ``database.get_validation_report``, ``database.list_validation_reports`` -- inspect validation reports.
* ``dataset.get_catalog``, ``dataset.list_tables``, ``dataset.get_table`` -- read dataset catalogs and tables.
* ``core_table.list``, ``core_table.get``, ``core_table.get_tenant_schema``, ``core_table.analyze``, ``core_table.upsert``, ``core_table.delete`` -- manage core tables.
* ``domain_transform.list``, ``domain_transform.get``, ``domain_transform.upsert``, ``domain_transform.analyze``, ``domain_transform.delete`` -- manage domain transforms.
* ``domain_table_history.get_history`` -- inspect domain table history.
* ``table_run_history.list_runs``, ``table_run_history.get_run``, ``table_run_history.get_table_history`` -- inspect run history for tables.


Queries
==================================================

Author, run, and organize queries against Amperity data.

* ``queries.list``, ``queries.get``, ``queries.create``, ``queries.update``, ``queries.delete`` -- manage queries.
* ``queries.run``, ``queries.activate``, ``queries.discard``, ``queries.move`` -- run and manage query lifecycle.
* ``query.run``, ``query.get_column_stats`` -- run ad hoc queries and inspect column statistics.
* ``query_folder.list``, ``query_folder.get``, ``query_folder.create``, ``query_folder.update``, ``query_folder.delete`` -- organize queries into folders.


Identity resolution (Stitch)
==================================================

Run, inspect, and tune Amperity's identity resolution.

* ``stitch.run`` -- run Stitch.
* ``stitch.get_report``, ``stitch.list_recent_reports``, ``stitch.lookup_record``, ``stitch.explain_pair`` -- inspect Stitch results and explain match pairs.
* ``stitch.get_settings``, ``stitch.update_settings``, ``stitch.set_table_availability`` -- read and update Stitch configuration.
* ``stitch.list_benchmarks``, ``stitch.get_benchmark_examples``, ``stitch.get_benchmark_history`` -- review benchmark coverage.


Bridges
==================================================

Manage data bridges between Amperity and external systems.

* ``bridge.list``, ``bridge.get``, ``bridge.create``, ``bridge.update``, ``bridge.delete`` -- manage bridge configuration.
* ``bridge.connect``, ``bridge.disconnect`` -- control bridge connection state.
* ``bridge.run_sync``, ``bridge.get_sync``, ``bridge.update_sync`` -- run and inspect bridge syncs.
* ``bridge.create_share``, ``bridge.get_share``, ``bridge.delete_share``, ``bridge.list_share_tables`` -- manage share configuration.
* ``bridge.upload_credential``, ``bridge.download_credential`` -- manage bridge credentials.
* ``bridge.load_amperity_data`` -- load Amperity data through a bridge.


Couriers, feeds, and destinations
==================================================

Configure data movement into and out of Amperity.

* ``courier.list``, ``courier.get``, ``courier.create``, ``courier.update``, ``courier.delete``, ``courier.run`` -- manage couriers.
* ``courier_group.list``, ``courier_group.get``, ``courier_group.create``, ``courier_group.update``, ``courier_group.delete``, ``courier_group.run`` -- manage courier groups.
* ``feed.list``, ``feed.get``, ``feed.upsert``, ``feed.delete`` -- manage feeds.
* ``destination.list``, ``destination.get``, ``destination.create``, ``destination.update``, ``destination.delete`` -- manage destinations.
* ``destination.list_target_templates``, ``destination.get_target_template``, ``destination.create_target_template``, ``destination.delete_target_template`` -- manage destination target templates.


Orchestrations
==================================================

Schedule and run orchestrations and orchestration groups.

* ``orchestration.list``, ``orchestration.get``, ``orchestration.create``, ``orchestration.update``, ``orchestration.delete`` -- manage orchestrations.
* ``orchestration_group.list``, ``orchestration_group.get``, ``orchestration_group.create``, ``orchestration_group.update``, ``orchestration_group.delete``, ``orchestration_group.run`` -- manage orchestration groups.


Campaigns and journeys
==================================================

Manage campaigns, campaign folders, journeys, and audience slices.

* ``campaign.list``, ``campaign.get``, ``campaign.create``, ``campaign.update``, ``campaign.delete``, ``campaign.duplicate``, ``campaign.move`` -- manage campaigns.
* ``campaign.schedule`` -- schedule (or unschedule) a campaign send.
* ``campaign_folder.list``, ``campaign_folder.get``, ``campaign_folder.create``, ``campaign_folder.update``, ``campaign_folder.delete`` -- manage campaign folders.
* ``journey.list``, ``journey.get``, ``journey.create``, ``journey.update``, ``journey.delete`` -- manage journeys.
* ``slice.list``, ``slice.get``, ``slice.create``, ``slice.update``, ``slice.delete`` -- manage audience slices.
* ``label.list``, ``label.get``, ``label.create``, ``label.update``, ``label.delete`` -- manage labels.


Predictions
==================================================

Configure and run prediction models.

* ``prediction.list_models``, ``prediction.get_model``, ``prediction.create_model``, ``prediction.update_model``, ``prediction.delete_model`` -- model lifecycle.
* ``prediction.list_model_configs``, ``prediction.get_model_config``, ``prediction.create_model_config``, ``prediction.delete_model_config``, ``prediction.activate_model_config``, ``prediction.save_model_settings`` -- model configuration.
* ``prediction.run_workflow``, ``prediction.get_run_history``, ``prediction.get_full_job_history`` -- run and inspect prediction workflows.
* ``prediction.get_validation_results``, ``prediction.get_model_config_validation_results`` -- inspect validation output.


Profile collections and real-time segments
==================================================

* ``profile_collection.list``, ``profile_collection.get``, ``profile_collection.create``, ``profile_collection.update``, ``profile_collection.delete`` -- manage profile collections.
* ``profile_collection.set_attribute``, ``profile_collection.delete_attribute``, ``profile_collection.refresh``, ``profile_collection.run`` -- manage attributes and runs.
* ``real_time_segment.list``, ``real_time_segment.get``, ``real_time_segment.create``, ``real_time_segment.update``, ``real_time_segment.delete`` -- manage real-time segments.


AI insights (Gnosis)
==================================================

Generate, read, and submit insights, themes, alerts, recommendations, and segments via Amperity's Gnosis service.

* ``gnosis.list_runs``, ``gnosis.get_run``, ``gnosis.create_run``, ``gnosis.update_run``, ``gnosis.delete_run``, ``gnosis.publish_run`` -- run lifecycle.
* ``gnosis.submit_insights``, ``gnosis.submit_recommendations``, ``gnosis.submit_alerts``, ``gnosis.submit_themes``, ``gnosis.submit_segments``, ``gnosis.submit_executive_summary`` -- submit content.
* ``gnosis.get_insights``, ``gnosis.get_recommendations``, ``gnosis.get_alerts``, ``gnosis.get_themes``, ``gnosis.get_segments``, ``gnosis.get_executive_summary`` -- read content.


Events
==================================================

Manage event streams and event types.

* ``event_stream.list``, ``event_stream.get``, ``event_stream.create``, ``event_stream.update``, ``event_stream.delete``, ``event_stream.get_recent_events`` -- manage event streams.
* ``event_type.list``, ``event_type.get``, ``event_type.create``, ``event_type.update``, ``event_type.delete`` -- manage event type definitions.


Custom domains (Iq) and assets
==================================================

* ``iq.list``, ``iq.get``, ``iq.create``, ``iq.update``, ``iq.delete``, ``iq.activate`` -- manage Iq objects.
* ``iq_folder.list``, ``iq_folder.get``, ``iq_folder.create``, ``iq_folder.update``, ``iq_folder.delete`` -- manage Iq folders.
* ``assets.list_company_context_documents``, ``assets.get_company_context_document`` -- read company context assets.


Configuration history and recovery
==================================================

Inspect configuration changes and revert to prior versions.

* ``config_history.search``, ``config_history.get_version_nodes``, ``config_history.diff_node`` -- search and inspect configuration history.
* ``config_revert.compare_revert``, ``config_revert.revert`` -- compare and revert configuration.
* ``comp_graph.get``, ``comp_graph.get_dependents``, ``comp_graph.get_dependencies`` -- inspect the configuration computation graph.


Workflows and compute
==================================================

Inspect Amperity workflows and Spark execution.

* ``workflow.list``, ``workflow.get_status``, ``workflow.cancel``, ``workflow.resolve_task`` -- inspect and manage workflows.
* ``spark.get_application``, ``spark.list_jobs``, ``spark.list_stages``, ``spark.get_stage``, ``spark.list_sql``, ``spark.get_sql``, ``spark.list_executors``, ``spark.get_environment``, ``spark.list_storage`` -- inspect Spark applications, jobs, stages, executors, SQL, and storage.
* ``compute.get_settings``, ``compute.update_settings`` -- read and update compute settings.


Alerts and training
==================================================

* ``alert.list_subscriptions``, ``alert.get_subscription``, ``alert.subscribe``, ``alert.unsubscribe`` -- manage alert subscriptions.
* ``training.setup_semantic_tags`` -- run training tasks for semantic tagging.
