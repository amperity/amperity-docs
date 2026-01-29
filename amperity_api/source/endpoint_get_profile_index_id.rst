.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Return the details for a specific index ID.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return the details for a specific index ID.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /indexes/{id}

==================================================
GET /indexes/{id}
==================================================

.. endpoint-get-profile-index-id-start

Use the **GET /indexes/{id}** endpoint to return the details for a specific index ID.

.. endpoint-get-profile-index-id-end

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-maximum-filters-start
   :end-before: .. endpoint-get-profiles-list-maximum-filters-end


.. _endpoint-get-profile-index-id-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-index-id-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-profile-index-id-prerequisites-end


.. _endpoint-get-profile-index-id-request-url:

Request URL
==================================================

.. endpoint-get-profile-index-id-request-url-start

Direct all requests to the **GET /indexes/{id}** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/api/indexes/{id}

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/api/indexes/{id}

.. endpoint-get-profile-index-id-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profile-index-id-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-index-id-request:

Requests
==================================================

.. endpoint-get-profile-index-id-request-start

A request to the **GET /indexes/{id}** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/api/indexes \
          ?index-id={id} \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'api-version: 2025-07-31' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-index-id-request-end


.. _endpoint-get-profile-index-id-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-index-id-request-parameters-start

The following table describes the parameters that may be used with the **GET /indexes/{id}** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **index-id**
     - String. Required.

       The unique identifier for the index.

.. endpoint-get-profile-index-id-request-parameters-end


.. _endpoint-get-profile-index-id-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-profile-index-id-request-examples-start

The following examples show how to send requests to the **GET /indexes/{id}** endpoint.

.. endpoint-get-profile-index-id-request-examples-end


.. endpoint-get-profile-index-id-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /indexes/{id}** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://app.amperity.com/api/indexes/ \
                ?index-id={id} \
                --header 'amperity-tenant: {tenant-id}' \
                --header 'api-version: 2025-07-31' \
                --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-index-id-request-examples-tabs-end


.. _endpoint-get-profile-index-id-responses:

Responses
==================================================

.. endpoint-get-profile-index-id-responses-start

A response from the **GET /indexes/{id}** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-profile-index-id-responses-end


.. _endpoint-get-profile-index-id-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-index-id-response-200ok-start

The **200** response returns a specific index ID.

.. code-block:: json
   :linenos:

   {
     "id": "{id}",
     "name": "{name of index}",
     "description": "{description of index}",
     "created_at": "{timestamp}",
     "updated_at": "{timestamp}"
   }

For example:

.. code-block:: json
   :linenos:

   {
       "id": "idx-xyz789",
       "name": "loyalty_members",
       "description": "Profiles from the loyalty program",
       "created_at": "2025-07-30T22:24:01.798Z",
       "updated_at": "2025-07-30T22:24:01.798Z"
   }

.. endpoint-get-profile-index-id-response-200ok-end


.. _endpoint-get-profile-index-id-response-parameters:

Response parameters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-profile-index-id-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **created_at**
     - The timestamp at which the index was created.

   * - **description**
     - The description of the index.

   * - **id**
     - The unique ID for the index.

   * - **name**
     - The name of the index.

   * - **updated_at**
     - The timestamp at which the index was last updated.

.. endpoint-get-profile-index-id-response-parameters-end


.. _endpoint-get-profile-index-id-response-404:

404 Not Found
--------------------------------------------------

.. endpoint-get-profile-index-id-response-404-start

.. code-block:: json
   :linenos:

   {
     "status": 404,
     "message": "The requested entity does not exist.",
     "request_id": "7d2f4a3e-1234-5678-90ab-cd3f",
     "trace_id": "1c9d3asdfasdf9b0c1d2e3f4"
   }

.. endpoint-get-profile-index-id-response-404-end
