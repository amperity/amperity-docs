.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Return a list of workflows from your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of workflows from your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /workflow/runs

==================================================
GET /workflow/runs
==================================================

.. endpoint-get-workflows-list-start

Use the **GET /workflow/runs** endpoint to return a list of workflows that exist within the date range defined in the request.

.. endpoint-get-workflows-list-end


.. _endpoint-get-workflows-list-prerequisites:

Prerequisites
==================================================

.. endpoint-get-workflows-list-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-workflows-list-prerequisites-end


.. _endpoint-get-workflows-list-base-url:

Base URL
==================================================

.. endpoint-get-workflows-list-base-url-start

Direct all requests to the **GET /workflow/runs** endpoint to the following base URL:

::

   https://{tenant-id}.amperity.com/api/workflow/runs

.. endpoint-get-workflows-list-base-url-end


.. _endpoint-get-workflows-list-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-workflows-list-request:

Requests
==================================================

.. endpoint-get-workflows-list-request-start

A request to the **GET /workflow/runs** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/workflow/runs \
          ?limit=12 \
          &with_total=true' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer {token}'

(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-workflows-list-request-end


.. _endpoint-get-workflows-list-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-workflows-list-request-parameters-start

The following table describes the parameters that may be used with the **GET /workflow/runs** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description


   * - **api_version**
     - String. Optional.

       A :ref:`supported version of the Amperity API <versioning-supported-versions>`. For example: **2024-04-01**.

       .. note:: You may use the **api-version** request header instead of the **api_version** request parameter.


   * - **created_from**
     - Datetime. Optional.

       A timestamp that defines the start (inclusive) of the time window in which one (or more) workflows started to run. See the **created_to** request parameter.

       This timestamp may be a partial timestamp, such as YYYY-MM-DD. The timestamp must be in |ext_iso_8601| format and is in Coordinated Universal Time (UTC).

       .. important:: Only workflows that have a **created_at** value that falls within this time window will be returned. (See the **created_at** response property for the :doc:`endpoint_get_workflows_fetch` endpoint.)


   * - **created_to**
     - Datetime. Optional.

       A timestamp that defines the end (exclusive) of the time window in which one (or more) workflows started to run. See the **created_from** request parameter.

       This timestamp may be a partial timestamp, such as YYYY-MM-DD. The timestamp must be in |ext_iso_8601| format and is in Coordinated Universal Time (UTC).

       .. important:: Only workflows that have a **created_at** value that falls within this time window will be returned. (See the **created_at** response property for the :doc:`endpoint_get_workflows_fetch` endpoint.)


   * - **ended_from**
     - Datetime. Optional.

       A timestamp that defines the start (inclusive) of the time window in which one (or more) workflows stopped running. See the **ended_to** request parameter.

       This timestamp may be a partial timestamp, such as YYYY-MM-DD. The timestamp must be in |ext_iso_8601| format and is in Coordinated Universal Time (UTC).

       .. important:: Only workflows that have a **ended_at** value that falls within this time window will be returned. (See the **ended_at** response property for the :doc:`endpoint_get_workflows_fetch` endpoint.)


   * - **ended_to**
     - Datetime. Optional.

       A timestamp that defines the end (exclusive) of the time window in which one (or more) workflows stopped running. See the **ended_from** request parameter.

       This timestamp may be a partial timestamp, such as YYYY-MM-DD. The timestamp must be in |ext_iso_8601| format and is in Coordinated Universal Time (UTC).

       .. important:: Only workflows that have a **ended_at** value that falls within this time window will be returned. (See the **ended_at** response property for the :doc:`endpoint_get_workflows_fetch` endpoint.)


   * - **limit**
     - Integer. Optional.

       The maximum number of records to include in a single page of results.


   * - **next_token**
     - String. Optional.

       An opaque token that is used to paginate results. Omit the **next_token** property to return the first page. Use the cursor value for **next_token** that was returned in a response to view the next page of results.

       For example: **ABCd1fghIJk2l3M**

       .. note:: The possible values for **next_token** are returned within the **200** response.

       .. important:: The value for **next_token** cannot be **NULL**.


   * - **state**
     - String. Optional.

       Return a list of workflows that only match the specified workflow state. May be one of the following:

          * Started
          * In progress
          * Stopping
          * Stopped
          * Succeeded

          .. note:: This is the same value that is visible from the **Status** column on each individual workflow page.


   * - **type**
     - String. Optional.

       Return a list of workflows that only match the specified workflow type.

       .. tip:: Use this endpoint to return a list of workflows (and workflow types), and then use a value from the **type** response parameter to make a new request that filters by that workflow type value.


   * - **with_total**
     - Boolean. Optional.

       Set this value to **true** to include a total count of all results. Default value: **false**.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. endpoint-get-workflows-list-request-parameters-end


.. _endpoint-get-workflows-list-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-workflows-list-request-examples-start

The following examples show how to send requests to the **GET /workflow/runs** endpoint.

.. endpoint-get-workflows-list-request-examples-end

.. endpoint-get-workflows-list-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /workflow/runs** endpoint.

      .. code-block:: bash

         curl --request GET \
                'https://tenant.amperity.com/api/workflow/runs \
                ?limit=12 \
                ?with_total=true' \
              --header 'amperity-tenant: {tenant}' \
              --header 'api-version: 2024-04-01' \
              --header 'Authorization: Bearer {token}'

      (This example is formatted for readability in a narrow page layout.)

.. endpoint-get-workflows-list-request-examples-tabs-end


.. _endpoint-get-workflows-list-responses:

Responses
==================================================

.. endpoint-get-workflows-list-responses-start

A response from the **GET /workflow/runs** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response will contain the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-workflows-list-responses-end


.. _endpoint-get-workflows-list-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-workflows-list-response-200ok-start

The **200** response returns a list of workflows.

.. code-block:: json
   :linenos:

   {
     "error": {
       "attribution": "customer",
       "type": "amperity.workflow.error/type",
       "message": "Found table in an invalid state:\n
                   loyalty_members. This error can be\n
                   resolved by removing this table\n
                   or by loading data to the table.",
       },
     "id": "wf-20240603-12345-MNabc",
     "ended_at": "2024-02-10T17:29:32.687Z",
     "name": "Loyalty Membership",
     "principal_name": "Justin Scott",
     "principal_id": "google-apps|justin.scott@socktown.com",
     "type": "amperity.orchestration.orchestration/run",
     "principal_email": "justin.scott@socktown.com",
     "state": "canceled",
     "created_at": "2024-02-10T17:29:22.454Z",
     "tenant": "socktown",
   }

.. endpoint-get-workflows-list-response-200ok-end


.. _endpoint-get-workflows-list-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-workflows-list-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **created_at**
     - The date and time at which a workflow task started.

       .. note:: This is the same value as the **Started** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

          **Duration**, as shown in the **Task Details** dialog, is the amount of time that occurred between **created_at** and **ended_at**.


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

          * **customer** indicates the source of the error is one (or more) configuration issues within Amperity. These issues can often be resolved by updating the configuration, and then restarting or rerunning the workflow.
          * **platform** indicates there is an issue with components and/or services that Amperity relies on to process the workflow. These issues are often transient and rerunning the workflow will resolve the error. In some cases, this type of error may require help from Amperity Support.

       **data**
          Additional data that is associated with the error. This parameter may be omitted from the response when the error message does not contain additional data or may return a NULL value.

       **message**
          The error message.

       **type**
          A period-delimited string that indicates where an error occurred.

   * - **ended_at**
     - The date and time at which a workflow task ended.

       .. note:: This is the same value as the **Completed** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.

          **Duration**, as shown in the **Task Details** dialog, is the amount of time that occurred between **created_at** and **ended_at**.

   * - **id**
     - The unique identifier for the workflow.

       .. note:: This is the same value as the **Definition ID** field in the **Task Details** dialog, which can be opened from the actions menu (|fa-kebab|) for each task in the workflow.


   * - **name**
     - The name of the workflow.

       .. note:: This is the same value that is visible from the title of each individual workflow page and from the **Name** column on the **Workflows** page.


   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.


   * - **principal_email**
     - The email address for the user who started the workflow.


   * - **principal_id**
     - A unique identifier for the Amperity user who started the workflow. For example: "google-apps|socktown@socktown.com".


   * - **principal_name**
     - The name of the Amperity user who started the workflow. For example: "Justin Scott" or "Automated workflow".


   * - **state**
     - The current state of the task: May be one of the following:

       * Started
       * In progress
       * Stopping
       * Stopped
       * Succeeded

       .. note:: This is the same value that is visible from the **Status** column on each individual workflow page.


   * - **total**
     - The total count of all results. This property is only returned when **with_total** is set to **true** in a request.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.


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

.. endpoint-get-workflows-list-response-parameters-end
