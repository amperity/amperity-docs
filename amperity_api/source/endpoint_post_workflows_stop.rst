.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Use this API to stop a running workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
         Use this API to stop a running workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        POST /workflow/runs/{id}/stop

==================================================
POST /workflow/runs/{id}/stop
==================================================

.. endpoint-post-workflows-stop-start

Use the **POST workflow/runs/{id}/stop** to stop a running workflow. 

.. endpoint-post-workflows-stop-end


.. _endpoint-post-workflows-stop-prerequisites:

Prerequisites
==================================================

.. endpoint-post-workflows-stop-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-post-workflows-stop-prerequisites-end


.. _endpoint-post-workflows-stop-base-url:

Base URL
==================================================

.. endpoint-post-workflows-stop-base-url-start

Direct all requests to the **POST workflow/runs/{id}/stop** endpoint should be directed to the following base URL:

.. code-block:: rest

   https://{tenant-id}.amperity.com/api/workflow/runs/{id}/stop

.. endpoint-post-workflows-stop-base-url-end


.. _endpoint-post-workflows-stop-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-post-workflows-stop-request:

Requests
==================================================

.. endpoint-post-workflows-stop-request-start

A request to the **POST workflow/runs/{id}/stop** endpoint is similar to:

.. code-block:: rest

   curl --request POST \ 
          'https://app.amperity.com/api/workflow/runs/{id}/stop' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer {token}'


This example is formatted for readability in a narrow page layout.

.. endpoint-post-workflows-stop-request-end


.. _endpoint-post-workflows-stop-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-post-workflows-stop-request-parameters-start

The following table describes the parameters that may be used with the **POST workflow/runs/{id}/stop** endpoint.

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

       The Amperity internal identifier for the workflow. For example **wf-20240619-14418-6UhqSe**.

       .. note:: On the workflows page, under **Actions**, copy the workflow id from the dropdown.

.. endpoint-post-workflows-stop-request-parameters-end


.. _endpoint-post-workflows-stop-request-examples:

Request examples
--------------------------------------------------

.. endpoint-post-workflows-stop-request-examples-start

The following examples show how to send requests to the **POST workflow/runs/{id}/stop** endpoint.

.. endpoint-post-workflows-stop-request-examples-end

.. endpoint-post-workflows-stop-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **POST workflow/runs/{id}/stop** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://tenant.amperity.com/api/workflow/runs/{id}/stop' \
              --header 'amperity-tenant: {tenant}' \
              --header 'api-version: 2024-04-01' \
              --header 'Authorization: Bearer {token}'

      (This example is formatted for readability in a narrow page layout.)

.. endpoint-post-workflows-stop-request-examples-tabs-end


.. _endpoint-post-workflows-stop-responses:

Responses
==================================================

.. endpoint-post-workflows-stop-responses-start

A response from the **POST workflow/runs/{id}/stop** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains workflow details for the workflow run that was stopped. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-post-workflows-stop-responses-end


.. _endpoint-post-workflows-stop-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-post-workflows-stop-response-200ok-start

The **200** response returns details for the workflow that was stopped.

.. code-block:: json
   :linenos:

   {
     "id":"wf-20240801-65278-x9E9U",
      "type":"campaign.send",
      "name":"testing",
      "tenant":"acme2-max",
      "created_at":"2024-08-01T18:07:58.099Z",
      "ended_at":"2024-08-01T18:10:47.712Z",
      "state":"succeeded"
   }

.. endpoint-post-workflows-stop-response-200ok-end


.. _endpoint-post-workflows-stop-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-post-workflows-stop-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

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
          A period-delimited string that indicates where an error occurred

   * - **id**
     - The Amperity internal identifier for the workflow. For example **wf-20240619-14418-6UhqSe**.

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

       **ended_at**
          The date and time at which a workflow task ended.

          .. note:: This is the same value as the **Completed** field in the **Task Details** dialog, which can be opened from the actions menu--|fa-kebab|--for each task in the workflow.

       **execution_type**
          The service that runs a workflow task. Possible return values are spark-sql, prodigal, prodigal-aurora, databricks, identity, task-identity, legacy.

       **id**
          The unique identifier for the task instance.

          .. note:: This is the same value as the **Task ID** field in the **Task Details** dialog, which can be opened from the actions menu--|fa-kebab|--for each task in the workflow.

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

          where the brackets ``[]`` are placeholders for named objects withn your tenant.

       .. note:: This is the same value that is visible from the **Task** column on each individual workflow page.

       **run_id**
          A unique identifier provided to the task instance to support situations where execution engines cannot provide a run ID. The value for this property is similar to: "abc-20240210-12345-6AbCDE".

          .. note:: This is the same value as the **Job ID** field in the **Task Details** dialog, which can be opened from the actions menu--|fa-kebab|--for each task in the workflow.

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

       **task_definition_id**
          A unique identifier for a task definition.

          These values often contain human-readable strings within a series of alphanumeric characters. For example, a task that runs a SQL query that updates the view for the **Unified Scores** table has a task definition ID similar to **ab-create-view-db-1a2BcdEFGhI-unified_scores**.

       **task_definition_type**
          The task definition type. The possible values for this property are the similar to the **type** property for the workflow. For example, "bridge.sync" or "campaign.append-results".

          .. note:: This is the same value as the **Definition ID** field in the **Task Details** dialog, which can be opened from the actions menu--|fa-kebab|--for each task in the workflow.

       **tenant**
          The unique identifier for the tenant.

       **timeout_ms**
          The length of time in milliseconds after which a running task instance will be forced to stop.

       **workflow_id**
          The unique identifier for the workflow to which this task belongs.

   * - **tenant**
     - The unique identifier for the tenant.

   * - **type**
     - The type of workflow. Most workflows have workflow types related to the following areas within Amperity:

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
     - The length of time in milliseconds after which a warning is sent that notifies users that a workflow is running longer than expected.

       .. note:: This parameter only applies to workflows that use SQL to write tables to storage.

.. endpoint-post-workflows-stop-response-parameters-end
