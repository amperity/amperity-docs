.. 
.. https://docs.amperity.com/api/
..

.. meta::
    :description lang=en:
         Use this API to stop a running workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
         Use this API to stop a running workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        POST /workflows/stop


==================================================
POST /workflows stop details
==================================================

.. endpoint-post-workflows-stop-start

Use the **workflow/runs/{id}:stop** to stop a running workflow. 

.. endpoint-post-workflows-stop-end


.. _endpoint-post-workflows-stop-http-methods:

Available HTTP methods
==================================================

.. image:: ../../images/api-request-post-workflows-stop.png
   :width: 440 px
   :alt: GET /campaigns
   :align: left
   :class: no-scaled-link


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

All requests made to the **workflow/runs/{id}:stop** endpoint should be directed to the following base URL:

.. code-block:: rest

   https://{tenant-id}.amperity.com/api/workflow/runs/{id}:stop

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

A request to the **workflow/runs/{id}:stop** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/api/ingest/jobs/{id}" \
          --header "accept: application/json"


(This example is formatted for readability in a narrow page layout.)

.. endpoint-post-workflows-stop-request-end


.. _endpoint-post-workflows-stop-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-post-workflows-stop-request-parameters-start

The following table describes the parameters that may be used with the **workflow/runs/{id}:stop** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **job_id**
     - String. Required.

       The Amperity internal identifier for the workflow. For example **wf-20240619-14418-6UhqSe**.

       .. note:: On the workflows page, under **Actions**, copy the workflow id from the dropdown.

.. endpoint-post-workflows-stop-request-parameters-end


.. _endpoint-post-workflows-stop-request-examples:

Request examples
--------------------------------------------------

.. endpoint-post-workflows-stop-request-examples-start

The following examples show how to send requests to the **workflow/runs/{id}:stop** endpoint.

.. endpoint-post-workflows-stop-request-examples-end


.. _endpoint-post-workflows-stop-request-example-curl:

cURL
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-post-workflows-stop-request-example-curl-start

The following example shows how to use cURL to send a request to the **workflow/runs/{id}:stop** endpoint.

::

   curl --request GET \
          'https://tenant.amperity.com/api/workflow/runs/{id}:stop" \
          --header "accept: application/json"

(This example is formatted for readability in a narrow page layout.)

.. endpoint-post-workflows-stop-request-example-curl-end


.. _endpoint-post-workflows-stop-responses:

Responses
==================================================

.. endpoint-post-workflows-stop-responses-start

A response from the **workflow/runs/{id}:stop** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response will contain the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-post-workflows-stop-responses-end


.. _endpoint-post-workflows-stop-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-post-workflows-stop-response-200ok-start

The **200** response returns a set of jobs.

.. code-block:: json

   {
     "created_at": "2024-06-19T04:00:18.764Z",
     "ended_at": "2024-06-19T04:03:10.119Z",
     "error": {
       "attribution": "customer",
       "data": {
           "error_code": "InvalidAccessKeyId",
           "id": "s3",
           "request_id": "Z47DXHNGJ7ZPMRVS",
           "retryable?": false
       },
       "message": "The credential does not provide access to the given resource. Please update the credential's access or try another credential.",
       "type": "amperity.plugin.error/invalid-credentials"
     },
     "id": "wf-20240619-14418-6UhqSe",
     "name": "Customer Attribute Daily",
     "state": "failed",
     "tenant": "acme2-max",
     "type": "campaign.send"
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

   * - **id**
     - The workflow identifier.

.. endpoint-post-workflows-stop-response-parameters-end
