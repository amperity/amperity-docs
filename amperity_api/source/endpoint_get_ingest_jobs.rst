.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Return a list of ingest jobs from your tenant that occurred within the previous 7 days.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of ingest jobs from your tenant that occurred within the previous 7 days.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /ingest/jobs

==================================================
GET /ingest/jobs
==================================================

.. endpoint-get-ingest-jobs-start

Use the **GET /ingest/jobs** endpoint to return a list of jobs from your tenant that occurred within the previous 7 days.

.. endpoint-get-ingest-jobs-end


.. _endpoint-get-ingest-jobs-prerequisites:

Prerequisites
==================================================

.. endpoint-get-ingest-jobs-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-ingest-jobs-prerequisites-end


.. _endpoint-get-ingest-jobs-base-url:

Base URL
==================================================

.. endpoint-get-ingest-jobs-base-url-start

Direct all requests to the **GET /ingest/jobs** endpoint to the following base URL:

.. code-block:: rest

   https://{tenant-id}.amperity.com/api/ingest/jobs

.. endpoint-get-ingest-jobs-base-url-end


.. _endpoint-get-ingest-jobs-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-ingest-jobs-request:

Requests
==================================================

.. endpoint-get-ingest-jobs-request-start

A request to the **GET /ingest/jobs** endpoint is similar to:

::

   curl --request GET \
          'https://tenant.amperity.com/api/ingest/jobs \
          ?created_from=2024-10-01 \
          ?created_to=2024-10-07' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-ingest-jobs-request-end


.. _endpoint-get-ingest-jobs-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-ingest-jobs-request-parameters-start

The following table describes the parameters that may be used with the **GET /ingest/jobs** endpoint.

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
     - Datetime. Required.

       A timestamp that defines the start (inclusive) of a 7-day time window in which one or more ingest jobs started. See the **created_to** request parameter.

       This timestamp may be a partial timestamp, such as YYYY-MM-DD. The timestamp must be in |ext_iso_8601| format and is in Coordinated Universal Time (UTC).

       .. important:: Only ingest jobs that have a **started_at** value that falls within this time window is returned. See the **created_at** response property for the :doc:`endpoint_get_ingest_jobs_id` endpoint.


   * - **created_to**
     - Datetime. Required.

       A timestamp that defines the end (exclusive) of a 7-day time window in which one or more ingest jobs started. See the **created_from** request parameter.

       This timestamp may be a partial timestamp, such as YYYY-MM-DD. The timestamp must be in |ext_iso_8601| format and is in Coordinated Universal Time (UTC).

       .. important:: Only ingest jobs that have a **started_at** value that falls within this time window is returned. See the **created_at** response property for the :doc:`endpoint_get_ingest_jobs_id` endpoint.

   * - **with_total**
     - Boolean. Optional.

       Set this value to **true** to include a total count of all results. Default value: **false**.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. endpoint-get-ingest-jobs-request-parameters-end


.. _endpoint-get-ingest-jobs-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-ingest-jobs-request-examples-start

The following examples show how to send requests to the **GET /ingest/jobs** endpoint.

.. endpoint-get-ingest-jobs-request-examples-end

.. endpoint-get-ingest-jobs-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /ingest/jobs** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://tenant.amperity.com/api/ingest/jobs \
                ?created_from=2024-10-01 \
                ?created_to=2024-10-07' \
               --header 'amperity-tenant: {tenant}' \
               --header 'api-version: 2024-04-01' \
               --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

.. endpoint-get-ingest-jobs-request-examples-tabs-end


.. _endpoint-get-ingest-jobs-responses:

Responses
==================================================

.. endpoint-get-ingest-jobs-responses-start

A response from the **GET /ingest/jobs** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-ingest-jobs-responses-end


.. _endpoint-get-ingest-jobs-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-ingest-jobs-response-200ok-start

The **200** response returns a set of records, files, and feeds that were ingested during the specified range, similar to the following response example, but with a response section for each record, file, and feed.

.. code-block:: json
   :linenos:

   {
     "total": 0,
     "data": [
       {
         "id": "isj-1f73r9u2",
         "tables": [
           {
             "errors": 200,
             "feed_id": "df-5L6d1veh",
             "read": 1000,
             "rejected": 200,
             "updated": 200,
             "started_at": "2024-06-01T04:02:54.433Z",
             "state": "succeeded",
             "ended_at": "2024-06-01T04:02:57.433Z",
             "files": [
               {
                 "file_id": "cb-20240618-71992-SF3Uz/part0.avro",
                 "name": "part0.avro",
                 "read": 1000,
                 "errors": 200
               }
             ],
             "inserted": 400,
             "table_name": "My table",
             "job_id": "isj-1f73r9u2"
           }
         ],
         "workflow_id": "wf-20240618-3423-b45"
       }
     ],
   }

.. endpoint-get-ingest-jobs-response-200ok-end


.. _endpoint-get-ingest-jobs-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-ingest-jobs-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **id**
     - The ingest job identifier.

   * - **tables**
     - A summary of table details from this ingest job.

       The JSON array for this summary is similar to:

       .. code-block:: json

          "tables" : [ {
            "errors" : 200,
            "feed_id" : "df-5L6d1veh",
            "read" : 1000,
            "rejected" : 200,
            "updated" : 200,
            "started_at" : "2024-06-01T04:02:54.433Z",
            "state" : "succeeded",
            "ended_at" : "2024-06-01T04:02:57.433Z",
            "files" : [ {
              "file_id" : "cb-20240618-71992-SF3Uz/part0.avro",
              "name" : "part0.avro",
              "read" : 1000,
              "errors" : 200
            } ],
            "inserted" : 400,
            "table_name" : "My table",
            "job_id" : "isj-1f73r9u2"
          } ],

       where

       **errors**
          The number of rows with an ingest error. For example, when Amperity cannot match a field value to the expected data type.

       **feed_id**
          The unique ID of this feed.

       **read**
          The number of rows ingested into this feed.

       **rejected**
          The number of duplicate rows that were not ingested.  

       **updated**
          The total count of rows updated for this feed during the job.

       **started_at**
          The date and time at which a job started.

       **state**
          The current state of the job. For example:

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

       **ended_at**
          The date and time at which a job ended.

       **files**
          A collection of file details, including a unique ID, the name of the file, the number of records ingested, and the number of errors.

          .. code-block:: json

             "files" : [ {
               "file_id" : "cb-20241234-123452-AB1Ca/part0.avro",
               "name" : "part0.avro",
               "read" : 1000,
               "errors" : 200
             } ],

       **inserted**	
          The number of records that were inserted into the table.

       **table_name**	
          The name of the table.

       **job_id**	
          The unique identifier for the ingest job.

   * - **workflow_id**
     - The Amperity internal identifier for the workflow that ran this job.

   * - **next_token**
     - The **next_token** parameter is included in the response, but is not available for use with the **GET /ingest/jobs** endpoint. The **GET /ingest/jobs** endpoint only returns a list of ingest jobs that occurred within the previous 7 days.

.. endpoint-get-ingest-jobs-response-parameters-end
