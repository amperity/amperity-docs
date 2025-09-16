.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Return a specific customer profile from your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return a specific customer profile from your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /indexes/{id}/profiles/{id}

==================================================
GET /indexes/{id}/profiles/{id}
==================================================

.. endpoint-get-profile-start

Use the **GET /indexes/{id}/profiles/{id}** endpoint to return a specific customer profile.

.. endpoint-get-profile-end


.. _endpoint-get-profile-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-profile-prerequisites-end


.. _endpoint-get-profile-base-url:

Base URL
==================================================

.. endpoint-get-profile-base-url-start

Direct all requests to the **GET /indexes/{id}/profiles/{id}** endpoint to the following base URL:

::

   https://{tenant-id}.amperity.com/api/indexes/

.. endpoint-get-profile-base-url-end


.. _endpoint-get-profile-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-request:

Requests
==================================================

.. endpoint-get-profile-request-start

A request to the **GET /indexes/{id}/profiles/{id}** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/indexes/{id}/profiles/{id} \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2025-07-31' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-request-end


.. _endpoint-get-profile-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-request-parameters-start

The **GET /indexes/{id}/profiles/{id}** endpoint does not have any request parameters.

.. endpoint-get-profile-request-parameters-end


.. _endpoint-get-profile-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-profile-request-examples-start

The following examples show how to send requests to the **GET /indexes/{id}/profiles/{id}** endpoint.

.. endpoint-get-profile-request-examples-end


.. endpoint-get-profile-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /indexes/{id}/profiles/{id}** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://tenant.amperity.com/api/indexes/{id}/profiles/{id} \
                --header 'amperity-tenant: {tenant}' \
                --header 'api-version: 2025-07-31' \
                --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-request-examples-tabs-end


.. _endpoint-get-profile-responses:

Responses
==================================================

.. endpoint-get-profile-responses-start

A response from the **GET /indexes/{id}/profiles/{id}** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-profile-responses-end


.. _endpoint-get-profile-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-response-200ok-start

The **200** response returns a specific customer profile.

.. code-block:: json
   :linenos:

   {
     "id": "{profile_id}",
     "index_id": "{index_id}",
     "attributes": [
       {
         "attribute": "value",
         "attribute": "value"
       },
     ]
   }

where the contents of ``attributes`` depend on the attributes that are in the index. For example:

.. code-block:: json
   :linenos:

   {
     "id": "{profile_id}",
     "index_id": "{index_id}",
     "attributes": [
       {
         "first_name": "Daniel",
         "last_name": "Kuhlman",
         "email": "danielkuhlman@email.com",
         "loyalty_id": "123456789-0"
       },
     ]
   }

.. endpoint-get-profile-response-200ok-end


.. _endpoint-get-profile-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-profile-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **atttributes**
     - A JSON array of attributes for a profile in an index. The attributes that are returned are specific to the index.

       For example:

       .. code-block:: json
          :linenos:

          {
            "id": "{profile_id}",
            "index_id": "{index_id}",
            "attributes": [
              {
                "first_name": "Daniel",
                "last_name": "Kuhlman",
                "email": "danielkuhlman@email.com",
                "loyalty_id": "123456789-0"
              },
            ]
          }

   * - **id**
     - The unique ID for the customer profile.

   * - **index_id**
     - The unique ID for the profile index.

.. endpoint-get-profile-response-parameters-end
