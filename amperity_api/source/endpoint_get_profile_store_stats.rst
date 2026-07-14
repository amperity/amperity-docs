.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Return statistics for a profile store.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return statistics for a profile store.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /collections/{collection-id}/stats

==================================================
GET /collections/{collection-id}/stats
==================================================

.. endpoint-get-profile-store-stats-start

Use the **GET /collections/{collection-id}/stats** endpoint to return statistics for a profile store, including the total number of profiles it contains.

.. endpoint-get-profile-store-stats-end

.. note:: This endpoint is part of the Real-time API, an unstable API that may change without advance notice of breaking changes.

.. note:: In the Amperity user interface a profile store is shown on the **Profiles** page and may also be referred to as a profile collection. The value for **{collection-id}** identifies that profile store.


.. _endpoint-get-profile-store-stats-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-store-stats-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.
#. A profile store must be configured for your tenant. To set up a profile store, contact your Amperity representative.

.. endpoint-get-profile-store-stats-prerequisites-end

.. note:: The access token must be granted the **profile-collections:read** permission.


.. _endpoint-get-profile-store-stats-request-url:

Request URL
==================================================

.. endpoint-get-profile-store-stats-request-url-start

Direct all requests to the **GET /collections/{collection-id}/stats** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/collections/{collection-id}/stats

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/collections/{collection-id}/stats

.. endpoint-get-profile-store-stats-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profile-store-stats-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-store-stats-request:

Requests
==================================================

.. endpoint-get-profile-store-stats-request-start

A request to the **GET /collections/{collection-id}/stats** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/collections/{collection-id}/stats' \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-store-stats-request-end


.. _endpoint-get-profile-store-stats-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-store-stats-request-parameters-start

The following table describes the parameters that may be used with the **GET /collections/{collection-id}/stats** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **collection-id**
     - String. Required.

       The ID of the profile store.

.. endpoint-get-profile-store-stats-request-parameters-end


.. _endpoint-get-profile-store-stats-responses:

Responses
==================================================

.. endpoint-get-profile-store-stats-responses-start

A response from the **GET /collections/{collection-id}/stats** endpoint will match an :doc:`HTTP status code <responses>`. A **200** response returns statistics for the profile store.

.. endpoint-get-profile-store-stats-responses-end


.. _endpoint-get-profile-store-stats-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-store-stats-response-200ok-start

The **200** response returns statistics for the profile store.

.. code-block:: json
   :linenos:

   {
     "total-profiles": 0,
     "link-cardinality": {
       "email": 0,
       "phone": 0
     }
   }

.. endpoint-get-profile-store-stats-response-200ok-end


.. _endpoint-get-profile-store-stats-response-parameters:

Response parameters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-profile-store-stats-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **total-profiles**
     - The total number of profiles in the profile store.

   * - **link-cardinality**
     - A map of keychain link type to the number of indexed link values for that type.

.. endpoint-get-profile-store-stats-response-parameters-end
