.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Return a list of indexes.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return a list of indexes.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /indexes

==================================================
GET /indexes
==================================================

.. endpoint-get-profile-index-start

Use the **GET /indexes** endpoint to return a list of indexes.

.. endpoint-get-profile-index-end


.. _endpoint-get-profile-index-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-index-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-profile-index-prerequisites-end


.. _endpoint-get-profile-index-base-url:

Base URL
==================================================

.. endpoint-get-profile-index-base-url-start

Direct all requests to the **GET /indexes** endpoint to the following base URL:

::

   https://{tenant-id}.amperity.com/api/indexes/

.. endpoint-get-profile-index-base-url-end


.. _endpoint-get-profile-index-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-index-request:

Requests
==================================================

.. endpoint-get-profile-index-request-start

A request to the **GET /indexes** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/indexes \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2025-07-31' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-index-request-end


.. _endpoint-get-profile-index-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-index-request-parameters-start

The following table describes the parameters that may be used with the **GET /indexes** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **limit**
     - Integer. Optional.

       The maximum number of records to include in a single page of results. Default value: ``25``.


   * - **next_token**
     - String. Optional.

       An opaque token that is used to paginate results. Omit the **next_token** property to return the first page. Use the cursor value for **next_token** that was returned in a response to view the next page of results.

       For example: **ABCd1fghIJk2l3M**

       .. note:: The possible values for **next_token** are returned within the **200** response.

       .. important:: The value for **next_token** cannot be **NULL**.


   * - **with_total**
     - Boolean. Optional.

       Set this value to **true** to include a total count of all results. Default value: **false**.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. endpoint-get-profile-index-request-parameters-end


.. _endpoint-get-profile-index-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-profile-index-request-examples-start

The following examples show how to send requests to the **GET /indexes** endpoint.

.. endpoint-get-profile-index-request-examples-end


.. endpoint-get-profile-index-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /indexes** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://tenant.amperity.com/api/indexes \
                --header 'amperity-tenant: {tenant}' \
                --header 'api-version: 2025-07-31' \
                --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-index-request-examples-tabs-end


.. _endpoint-get-profile-index-responses:

Responses
==================================================

.. endpoint-get-profile-index-responses-start

A response from the **GET /indexes** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-profile-index-responses-end


.. _endpoint-get-profile-index-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-index-response-200ok-start

The **200** response returns a list of indexes.

.. code-block:: json
   :linenos:

   {
     "data": [
       {
         "id": "{id}",
         "name": "{name of index}",
         "description": "{description of index}",
         "created_at": "{timestamp}",
         "updated_at": "{timestamp}"
       }
     ],
     "next_token": "string",
     "total": 0
   }

For example:

.. code-block:: json
   :linenos:

   {
     "data": [
       {
         "id": "idx-xyz789",
         "name": "loyalty_members",
         "description": "Profiles from the loyalty program",
         "created_at": "2025-07-30T22:16:04.409Z",
         "updated_at": "2025-07-30T22:16:04.409Z"
       }
     ],
     "next_token": "string",
     "total": 0
   }

.. endpoint-get-profile-index-response-200ok-end


.. _endpoint-get-profile-index-response-parameters:

Response parameters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-profile-index-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of data for an index.

       For example:

       .. code-block:: json
          :linenos:

          {
            "data": [
              {
                "id": "idx-xyz789",
                "name": "loyalty_members",
                "description": "Profiles from the loyalty program",
                "created_at": "2025-07-30T22:16:04.409Z",
                "updated_at": "2025-07-30T22:16:04.409Z"
              }
            ],
            "next_token": "string",
            "total": 0
          }

       **created_at**
          The timestamp at which the index was created.

       **description**
          The description of the index.

       **id**
          The unique ID for the index.

       **name**
          The name of the index.

       **updated_at**
          The timestamp at which the index was last updated.

   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.

   * - **total**
     - The total number of returned indexes.

.. endpoint-get-profile-index-response-parameters-end


.. _endpoint-get-profile-index-response-404:

400
--------------------------------------------------

.. endpoint-get-profile-index-response-404-start

.. code-block:: json
   :linenos:

   {
     "status": 400,
     "message": "A human-readable summary of the error.",
     "request_id": "3fa85f64-1234-5678-901a-2c9asdfa6",
     "trace_id": "string"
   }

.. endpoint-get-profile-index-response-404-end
