.. https://docs.amperity.com/api/

:canonical: https://docs.amperity.com/api/endpoint_get_ingest_jobs_id.html


.. meta::
    :description lang=en:
         Return a list of ingest jobs from your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of ingest jobs from your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /ingest/jobs/{id}

==================================================
GET /ingest/jobs/{id}
==================================================

.. endpoint-get-ingest-jobs-id-start

Use the **GET /ingest/jobs/{id}** endpoint to return a list of jobs from your tenant.

.. endpoint-get-ingest-jobs-id-end


.. _endpoint-get-ingest-jobs-id-prerequisites:

Prerequisites
==================================================

.. endpoint-get-ingest-jobs-id-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-ingest-jobs-id-prerequisites-end


.. _endpoint-get-ingest-jobs-id-base-url:

Base URL
==================================================

.. endpoint-get-ingest-jobs-id-base-url-start

Direct all requests to the **GET /ingest/jobs/{id}** endpoint to the following base URL:

.. code-block:: rest

   https://{tenant-id}.amperity.com/api/ingest/jobs/{id}

.. endpoint-get-ingest-jobs-id-base-url-end


.. _endpoint-get-ingest-jobs-id-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-ingest-jobs-id-request:

Requests
==================================================

.. endpoint-get-ingest-jobs-id-request-start

A request to the **GET /ingest/jobs/{id}** endpoint is similar to:

::

   curl --request GET \
          'https://app.amperity.com/api/ingest/jobs/{id}' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer {token}'


(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-ingest-jobs-id-request-end


.. _endpoint-get-ingest-jobs-id-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-ingest-jobs-id-request-parameters-start

The following table describes the parameters that may be used with the **GET /ingest/jobs/{id}** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **api_version**
     - String. Optional.

       A :ref:`supported version of the Amperity API <versioning-supported-versions>`. For example: **2024-04-01**.

       .. note:: You may use the **api-version** request header instead of the **api_version** request parameter.

   * - **id**
     - String. Required.

       The Amperity internal identifier for the injest job. For example **isj-20240701-48815-6dcXdk**.

       .. note:: From the workflows page, on the right side, click **Recent Activity**, select **Ingest details** under the job, and copy the job id from the open dialog box.

.. endpoint-get-ingest-jobs-id-request-parameters-end


.. _endpoint-get-ingest-jobs-id-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-ingest-jobs-id-request-examples-start

The following examples show how to send requests to the **GET /ingest/jobs/{id}** endpoint.

.. endpoint-get-ingest-jobs-id-request-examples-end

.. endpoint-get-ingest-jobs-id-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /ingest/jobs/{id}** endpoint.

      .. code-block:: bash

         curl --request GET \
                'https://tenant.amperity.com/api/ingest/jobs/{id}' \
              --header 'amperity-tenant: {tenant}' \
              --header 'api-version: 2024-04-01' \
              --header 'Authorization: Bearer {token}'

      (This example is formatted for readability in a narrow page layout.)

.. endpoint-get-ingest-jobs-id-request-examples-tabs-end


.. _endpoint-get-ingest-jobs-id-responses:

Responses
==================================================

.. endpoint-get-ingest-jobs-id-responses-start

A response from the **GET /ingest/jobs/{id}** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response will contain the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-ingest-jobs-id-responses-end


.. _endpoint-get-ingest-jobs-id-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-ingest-jobs-id-response-200ok-start

The **200** response returns a set of jobs.

.. code-block:: json
   :linenos:

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

.. endpoint-get-ingest-jobs-id-response-200ok-end


.. _endpoint-get-ingest-jobs-id-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-ingest-jobs-id-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **id**
     - The ingest job identifier.

   * - **workflow_id**
     - The Amperity internal identifier for the workflow that ran this job.

   * - **tables**
     - A summary of table details from this ingest job.

       The JSON array for this summary is similar to: 

       .. code-block:: json

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

.. endpoint-get-ingest-jobs-id-response-parameters-end
