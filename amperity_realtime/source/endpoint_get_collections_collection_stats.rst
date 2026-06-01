.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
         Return statistics for a real-time profile collection.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return statistics for a real-time profile collection.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /collections/{collection-id}/stats

==================================================
GET /collections/{collection-id}/stats
==================================================

.. endpoint-get-collections-collection-stats-start

Use the **GET /collections/{collection-id}/stats** endpoint to return aggregate statistics for a real-time profile collection, including profile counts and last-updated timestamps.

.. endpoint-get-collections-collection-stats-end


.. _endpoint-get-collections-collection-stats-prerequisites:

Prerequisites
==================================================

.. endpoint-get-collections-collection-stats-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>` with the **Real-time API data access** policy.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-collections-collection-stats-prerequisites-end


.. _endpoint-get-collections-collection-stats-request-url:

Request URL
==================================================

.. endpoint-get-collections-collection-stats-request-url-start

Direct all requests to the **GET /collections/{collection-id}/stats** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/collections/{collection-id}/stats

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/collections/{collection-id}/stats

.. endpoint-get-collections-collection-stats-request-url-end

.. include:: base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-collections-collection-stats-rate-limit:

Rate limit
==================================================

.. include:: rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

.. include:: rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _endpoint-get-collections-collection-stats-request:

Requests
==================================================

.. endpoint-get-collections-collection-stats-request-start

A request to the **GET /collections/{collection-id}/stats** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/collections/{collection-id}/stats' \
        --header 'Amperity-Tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-collections-collection-stats-request-end


.. _endpoint-get-collections-collection-stats-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-collections-collection-stats-request-parameters-start

The **GET /collections/{collection-id}/stats** endpoint does not have any request parameters.

.. endpoint-get-collections-collection-stats-request-parameters-end


.. _endpoint-get-collections-collection-stats-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-collections-collection-stats-request-examples-start

The following examples show how to send requests to the **GET /collections/{collection-id}/stats** endpoint.

.. endpoint-get-collections-collection-stats-request-examples-end

.. endpoint-get-collections-collection-stats-request-examples-tabs-start

.. tabs::

   .. tab:: cURL

      The following example shows how to use cURL to send a request to the **GET /collections/{collection-id}/stats** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://app.amperity.com/prof/collections/{collection-id}/stats' \
              --header 'Amperity-Tenant: {tenant-id}' \
              --header 'Authorization: Bearer {token}'

   .. tab:: Python

      The following example shows how to use Python to send a request to the **GET /collections/{collection-id}/stats** endpoint.

      .. code-block:: python
         :linenos:

         import requests

         url = "https://app.amperity.com/prof/collections/{collection-id}/stats"

         headers = {
           "Authorization": "Bearer {token}",
           "Amperity-Tenant": "{tenant-id}"
         }

         response = requests.get(url, headers=headers)
         print("Status Code:", response.status_code)
         print("Response:", response.json())

.. endpoint-get-collections-collection-stats-request-examples-tabs-end


.. _endpoint-get-collections-collection-stats-responses:

Responses
==================================================

.. endpoint-get-collections-collection-stats-responses-start

A response from the **GET /collections/{collection-id}/stats** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-collections-collection-stats-responses-end


.. _endpoint-get-collections-collection-stats-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-collections-collection-stats-response-200ok-start

The **200** response returns statistics for the specified profile collection, similar to:

.. code-block:: json
   :linenos:

   {
     "collection_id": "col-abc123",
     "profile_count": 1482903,
     "updated_at": "2026-05-14T06:00:00.000Z"
   }

.. endpoint-get-collections-collection-stats-response-200ok-end


.. _endpoint-get-collections-collection-stats-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-collections-collection-stats-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **collection_id**
     - The unique identifier for the profile collection.

   * - **profile_count**
     - The total number of profiles in the collection.

   * - **updated_at**
     - The date and time at which the collection statistics were last updated, in |ext_iso_8601| format and in UTC.

.. endpoint-get-collections-collection-stats-response-parameters-end
