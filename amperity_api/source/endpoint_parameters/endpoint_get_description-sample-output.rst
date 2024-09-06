..
.. https://docs.amperity.com/api/
..

.. meta::
    :description lang=en:
         Return description from your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return description from your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /workflow/runs/


==================================================
GET /workflow/runs/
==================================================

.. endpoint-get-workflow-runs-start

Use the **/workflow/runs/** endpoint to description.

.. endpoint-get-workflow-runs-end


.. _endpoint-get-workflow-runs-http-methods:

Available HTTP methods
==================================================

.. image:: ../../images/api-request-get-image.png
   :width: 440 px
   :alt: GET /workflow/runs/
   :align: left
   :class: no-scaled-link


.. _endpoint-get-workflow-runs-prerequisites:

Prerequisites
==================================================

.. endpoint-get-workflow-runs-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-workflow-runs-prerequisites-end


.. _endpoint-get-workflow-runs-base-url:

Base URL
==================================================

.. endpoint-get-workflow-runs-base-url-start

All requests made to the **/workflow/runs/** endpoint should be directed to the following base URL:

::

   https://{tenant-id}.amperity.com/api/workflow/runs/

.. endpoint-get-workflow-runs-base-url-end


.. _endpoint-get-workflow-runs-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-workflow-runs-request:

Requests
==================================================

.. endpoint-get-workflow-runs-request-start

A request to the **/workflow/runs/** endpoint is similar to:

.. code-block:: rest

   curl --request GET 
          'https://tenant.amperity.com/api//workflow/runs/ 
          ?limit=12
          &with_total=true
        --header 'amperity-tenant: tenant'
        --header 'api-version: 2024-04-01'
        --header 'Authorization: Bearer token'

(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-workflow-runs-request-end

.. _endpoint-get-workflows-list-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-workflow-runs-request-parameters-start

The following table describes the parameters that may be used with the **/workflow/runs/** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description
.. endpoint-get-workflow-runs-request-parameters-end


.. _endpoint-get-workflow-runs-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-workflow-runs-request-examples-start

The following examples show how to send requests to the **/workflows/runs** endpoint.

.. endpoint-get-workflow-runs-request-examples-end


.. _endpoint-get-workflow-runs-request-example-curl:

cURL
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-workflow-runs-request-example-curl-start

The following example shows how to use cURL to send a request to the **/workflows/runs** endpoint.

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/workflows/runs \
          ?limit=12 \
          &with_total=true \
        --header 'amperity-tenant: tenant' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer token'

(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-workflow-runs-request-example-curl-end


.. _endpoint-get-workflow-runs-responses:

Responses
==================================================

.. endpoint-get-workflow-runs-responses-start

A response from the **/workflows/runs** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response will contain the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-workflow-runs-responses-end


.. _endpoint-get-workflow-runs-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-workflow-runs-response-200ok-start

The **200** response returns a list of workflows.

.. code-block:: json

description - Add the 200 response json code from the openapi docs

.. endpoint-get-workflow-runs-response-200ok-end


.. _endpoint-get-workflow-runs-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-workflow-runs-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description


.. endpoint-get-workflow-runs-response-parameters-end
