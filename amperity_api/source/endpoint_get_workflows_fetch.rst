.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Return details for a specific workflow from your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return details for a specific workflow from your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /workflow/runs/{id}

==================================================
GET /workflow/runs/{id}
==================================================

.. endpoint-get-workflows-fetch-start

Use the **GET /workflow/runs/{id}** endpoint to return details for a specific workflow.

.. endpoint-get-workflows-fetch-end


.. _endpoint-get-workflows-fetch-prerequisites:

Prerequisites
==================================================

.. endpoint-get-workflows-fetch-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-workflows-fetch-prerequisites-end


.. _endpoint-get-workflows-fetch-base-url:

Base URL
==================================================

.. endpoint-get-workflows-fetch-base-url-start

Direct all requests to the **GET /workflow/runs/{id}** endpoint to the following base URL:

::

   https://{tenant-id}.amperity.com/api/workflow/runs/{id}

.. endpoint-get-workflows-fetch-base-url-end


.. _endpoint-get-workflows-fetch-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-workflows-fetch-request:

Requests
==================================================

.. endpoint-get-workflows-fetch-request-start

A request to the **GET /workflow/runs/{id}** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/workflow/runs/{id} \
          ?view=overview' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer {token}'

(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-workflows-fetch-request-end


.. _endpoint-get-workflows-fetch-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-workflows-fetch-request-parameters-start

The following table describes the parameters that may be used with the **GET /workflow/runs/{id}** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **api_version**
     - String. Optional.

       A :ref:`supported version of the Amperity API <versioning-supported-versions>`. For example: **2024-04-01**.

       .. note:: You may use the **api-version** request header instead of the **api_version** request parameter.


   * - **{id}**
     - String. Required.

       The unique identifier for a workflow, similar to: **wf-20240603-12345-MNabc**.

       The workflow ID must be in the URL. For example: **/workflow/runs/wf-20240603-12345-MNabc**.

       Use the :doc:`endpoint_get_workflows_list` endpoint to get a list of workflow IDs or copy the ID from the **Workflows** page in Amperity.


   * - **view**
     - String. Optional.

       Set this value to **overview** to return only the following parameters: **created_at**, **ended_at**, **id**, **name**, **state**, **tenant**, and **type**.

       Set this value to **verbose** to return all :ref:`response parameters for the workflow <endpoint-get-workflows-fetch-response-parameters>`, including for any tasks that were started by the workflow.

       Default value: **overview**.

.. endpoint-get-workflows-fetch-request-parameters-end


.. _endpoint-get-workflows-fetch-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-workflows-fetch-request-examples-start

The following examples show how to send requests to the **GET /workflow/runs/{id}** endpoint.

.. endpoint-get-workflows-fetch-request-examples-end

.. endpoint-get-workflows-fetch-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /workflow/runs/{id}** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://tenant.amperity.com/api/workflow/runs/{id} \
                ?view=overview' \
              --header 'amperity-tenant: {tenant}' \
              --header 'api-version: 2024-04-01' \
              --header 'Authorization: Bearer {token}'

      (This example is formatted for readability in a narrow page layout.)

.. endpoint-get-workflows-fetch-request-examples-tabs-end


.. _endpoint-get-workflows-fetch-responses:

Responses
==================================================

.. endpoint-get-workflows-fetch-responses-start

A response from the **GET /workflow/runs/{id}** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response will contain the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-workflows-fetch-responses-end


.. _endpoint-get-workflows-fetch-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-workflows-fetch-response-200ok-start

The **200** response returns details for the named workflow.

**Overview**

.. code-block:: json
   :linenos:

   {
     "type": "campaign.fetch",
     "ended_at": "2024-01-22T18:02:50.769Z",
     "id": "wf-20240603-12345-MNabc",
     "tenant": "socktown",
     "created_at": "2024-01-22T17:57:36.371Z",
     "name": "Send audiences to Braze",
     "state": "succeeded"
   }

**Verbose**

.. important:: The list of :ref:`response parameters that are returned <endpoint-get-workflows-fetch-response-parameters>` in the response will vary, depending on the state of the workflow, the number of tasks that were initiated by the workflow, and if an error occurred.

.. code-block:: json
   :linenos:

   {
     "task_instances": [],
     "error": {
       "attribution": "customer",
       "type": "amperity.workflow.workflow.repository.core/cancel",
       "message": "Workflow manually stopped"
     },
     "id": "wf-20240603-12345-MNabc",
     "ended_at": "2024-02-10T17:29:32.687Z",
     "name": "Braze",
     "principal_name": "Justin Scott",
     "principal_id": "google-apps|justin.scott@socktown.com",
     "type": "amperity.orchestration.orchestration/run",
     "launched_version": "etv-20240210-12345-6AbCDE",
     "principal_email": "justin.scott@socktown.com",
     "state": "canceled",
     "created_at": "2024-02-10T17:29:22.454Z",
     "tenant": "socktown",
     "current_version": "etv-20240210-12345-6AbCDE"
   }

.. endpoint-get-workflows-fetch-response-200ok-end


.. _endpoint-get-workflows-fetch-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-workflows-fetch-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **created_at**
     - The date and time at which a workflow started.

       .. note:: The amount of time that elapsed between **created_at** and **ended_at** is the runtime for the workflow.

          The length of time a workflow ran is visible from the **Runtime** box visible from the **Type** box on each individual workflow page.


   * - **current_version**
     - A unique identifier that describes the configuration state of Amperity at the end of the workflow or at the time an error occurred. The value for this property is similar to: "etv-20240210-12345-6AbCDE".


   * - **ended_at**
     - The date and time at which a workflow ended.

       .. note:: The amount of time that elapsed between **created_at** and **ended_at** is the runtime for the workflow.

          The length of time a workflow ran is visible from the **Runtime** box visible from the **Type** box on each individual workflow page.


   * - **error**
     - A JSON array of values for a workflow error.

       .. note:: An error message is shown for any workflow with a state of **Failed**. You can view the error message the from the **Workflows** page.

       The JSON array for an error is similar to:

       .. code-block:: django

          "error": {
            "attribution": "customer",
            "type": "amperity.workflow.task.stitch/table",
            "message": "Found table in an invalid state:\n
                        loyalty_members. This error can be\n
                        resolved by removing this table\n
                        or by loading data to the table.",
            "data": NULL,
          },

       where:

       **attribution**
          The source of the error. May be attributed to **customer** or **platform**.

          * **customer** indicates the source of the error is one or more configuration issues within Amperity. These issues can often be resolved by updating the configuration, and then restarting or rerunning the workflow.
          * **platform** indicates there is an issue with components and/or services that Amperity relies on to process the workflow. These issues are often transient and rerunning the workflow will resolve the error. In some cases, this type of error may require help from Amperity Support.

       **data**
          Additional data that is associated with the error. This parameter may be omitted from the response when the error message does not contain additional data or may return a NULL value.

       **message**
          The error message.

       **type**
          A period-delimited string that indicates where an error occurred.


   * - **launched_version**
     - A unique identifier that describes the configuration state of Amperity at the start of the workflow. The value for this property is similar to: "etv-20240210-12345-6AbCDE".


   * - **name**
     - The name of the workflow.

       .. note:: This is the same value that is visible from the title of each individual workflow page and from the **Name** column on the **Workflows** page.


   * - **principal_email**
     - The email address for the user who started the workflow.


   * - **principal_id**
     - A unique identifier for the Amperity user who started the workflow. For example: "google-apps|socktown@socktown.com".


   * - **principal_name**
     - The name of the Amperity user who started the workflow. For example: "Justin Scott" or "Automated workflow".


   * - **state**
     - The current state of the workflow. For example:

       * Scheduled
       * Started
       * In progress
       * Stopping
       * Stopped
       * Succeeded
       * Running with failures
       * Failed
       * Canceled

       .. note:: This is the same value that is visible from the **Status** box on each individual workflow page and from the **Status** column on the **Workflows** page.


   * - **task_instances**
     - A JSON array that contains zero or more sets of the following parameters, one set for each task in the workflow. The list of parameters returned in the response may vary, depending on the type of task.

       **created_at**
          The date and time at which a workflow task started.

          .. note:: This is the same value as the **Started** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

             **Duration**, as shown in the **Task Details** dialog, is the amount of time that occurred between **created_at** and **ended_at**.

       **ended_at**
          The date and time at which a workflow task ended.

          .. note:: This is the same value as the **Completed** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

             **Duration**, as shown in the **Task Details** dialog, is the amount of time that occurred between **created_at** and **ended_at**.

       **error**
          A JSON array of values for a workflow task error.

          For example:

          .. code-block:: django

             "error": {
               "attribution": "customer",
               "type": "amperity.workflow.task-instance/table",
               "message": "Found tables in an invalid state:\n
                           loyalty_members. This error can be\n
                           resolved by removing these tables\n
                           or by loading data to the table.",
               "data": {
                 "error": {
                   "message": "Job stopped.",
                   "data": NULL
                  }
                }
             },

       **id**
          The unique identifier for the task instance.

          .. note:: This is the same value as the **Task ID** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

       **label**
          The name of the task instance. Examples of task instance labels include:

          * Appending outputs of treatment [treatment] into campaign recipients table
          * Deleting records
          * Generating database
          * Getting query results
          * Getting segment results
          * Migrating [schema] schema
          * Recording segment tracking history
          * Resolving input tasks
          * Runing query: [query]
          * Running segment
          * Syncing tables
          * Truncating tables
          * Validating database [database-name]
          * Updating domain tables
          * Updating [table-name]

          where the brackets [] are placeholders for named objects withn your tenant.

       .. note:: This is the same value that is visible from the **Task** column on each individual workflow page.

       **run_id**
          A unique identifier provided to the task instance to support situations where execution engines cannot provide a run ID. The value for this property is similar to: "abc-20240210-12345-6AbCDE".

          .. note:: This is the same value as the **Job ID** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

       **state**
          The current state of the task. For example:

          * Scheduled
          * Started
          * In progress
          * Running
          * Finalizing
          * Succeeded
          * Stopping
          * Stopped
          * Failed
          * Skipped
          * Canceled

          .. note:: This is the same value that is visible from the **Status** column on each individual workflow page. Some values are only visible while a task is active.

       **state_changed_at**
          The date and time at which the task completed and the state of the workflow was updated. This can be the same value as **ended_at**.

       **task_definition_id**
          A unique identifier for a task definition.

          These values often contain human-readable strings within a series of alphanumeric characters. For example, a task that runs a SQL query that updates the view for the **Unified Scores** table has a task definition ID similar to **ab-create-view-db-1a2BcdEFGhI-unified_scores**.

       **task_definition_type**
          The task definition type. The possible values for this property are the similar to the **type** property for the workflow. For example, "bridge.sync" or "campaign.append-results".

          .. note:: This is the same value as the **Definition ID** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

       **task_instance_id**
          The unique identifier for the task instance.

          .. note:: This is the same value as the **Task ID** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

       **tenant**
          The unique identifier for the tenant.

       **timeout_ms**
          The length of time (in milliseconds) after which a running task instance will be forced to stop.

       **workflow_id**
          The unique identifier for the workflow to which this task belongs.

   * - **tenant**
     - The unique identifier for the tenant.


   * - **type**
     - The type of workflow. Most workflows will have workflow types related to the following areas within Amperity:

       * Bridge sync
       * C360 validation
       * Campaign results
       * Campaign send
       * CCPA delete
       * Compact campaign recipients table
       * Courier
       * Courier group
       * Data refresh
       * Database
       * Domain table schema migration
       * File upload
       * Ingest
       * Input validation report update
       * Manual campaign run
       * Manual index run
       * Orchestration
       * Orchestration group
       * Predictive job
       * Record deletion
       * System migration on campaigns recipients table
       * UID2 enrichment
       * Update campaign recipients table

       .. note:: This is the same value that is visible from the **Type** box on each individual workflow page and from the **Type** column on the **Workflows** page.


   * - **warn_after_ms**
     - The length of time (in milliseconds) after which a warning is sent that notifies users that a workflow is running longer than expected.

       .. note:: This parameter only applies to workflows that use SQL to write tables to storage.


   * - **workflow_id**
     - The unique identifier for the workflow.

       .. note:: This is the same value as the **Definition ID** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

.. endpoint-get-workflows-fetch-response-parameters-end
