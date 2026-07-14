.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Look up a profile in a profile store by keychain keys sent in the request body.

.. meta::
    :content class=swiftype name=body data-type=text:
        Look up a profile in a profile store by keychain keys sent in the request body.

.. meta::
    :content class=swiftype name=title data-type=string:
        POST /lookup/{collection-id}/keychain

==================================================
POST /lookup/{collection-id}/keychain
==================================================

.. endpoint-post-profile-store-lookup-start

Use the **POST /lookup/{collection-id}/keychain** endpoint to find a single profile in a profile store by one or more keychain keys, such as an email address or loyalty ID. This endpoint behaves like :doc:`GET /lookup/{collection-id}/keychain <endpoint_get_profile_store_lookup>`, but the keychain keys are sent in the request body. Use this endpoint when a key value should not appear in a query string.

.. endpoint-post-profile-store-lookup-end

.. note:: This endpoint is part of the Real-time Profile API, an unstable API that may change without advance notice of breaking changes.

.. note:: In the Amperity user interface a profile store is shown on the **Profiles** page and may also be referred to as a profile collection. The value for **{collection-id}** identifies that profile store.


.. _endpoint-post-profile-store-lookup-prerequisites:

Prerequisites
==================================================

.. endpoint-post-profile-store-lookup-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.
#. A profile store must be configured for your tenant. To set up a profile store, contact your Amperity representative.

.. endpoint-post-profile-store-lookup-prerequisites-end

.. note:: The access token must be granted the **profile-collections:read** and **pii:read** permissions.


.. _endpoint-post-profile-store-lookup-request-url:

Request URL
==================================================

.. endpoint-post-profile-store-lookup-request-url-start

Direct all requests to the **POST /lookup/{collection-id}/keychain** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/lookup/{collection-id}/keychain

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/lookup/{collection-id}/keychain

.. endpoint-post-profile-store-lookup-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-post-profile-store-lookup-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-post-profile-store-lookup-request:

Requests
==================================================

.. endpoint-post-profile-store-lookup-request-start

A request to the **POST /lookup/{collection-id}/keychain** endpoint sends the keychain keys in a JSON request body. At least one key is required.

.. code-block:: rest

   curl --request POST \
          'https://app.amperity.com/prof/lookup/{collection-id}/keychain' \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}' \
        --header 'Content-Type: application/json' \
        --data '{ "keys": { "email": "customer@example.com" }, "enrich": false }'

This example is formatted for readability in a narrow page layout.

.. endpoint-post-profile-store-lookup-request-end


.. _endpoint-post-profile-store-lookup-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-post-profile-store-lookup-request-parameters-start

The following table describes the parameters that may be used with the **POST /lookup/{collection-id}/keychain** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **collection-id**
     - String. Required.

       The ID of the profile store to search.

   * - **keys**
     - JSON object. Required.

       A map of keychain keys to values, such as ``{ "email": "customer@example.com" }``. At least one key is required.

   * - **enrich**
     - Boolean. Optional.

       Set to **true** to include enriched attributes in the returned profile. Default value: **false**.

.. endpoint-post-profile-store-lookup-request-parameters-end


.. _endpoint-post-profile-store-lookup-responses:

Responses
==================================================

.. endpoint-post-profile-store-lookup-responses-start

A response from the **POST /lookup/{collection-id}/keychain** endpoint will match an :doc:`HTTP status code <responses>`. A **200** response returns the matching profile. The **Location** header of a **200** response contains the URL for the matched profile.

.. endpoint-post-profile-store-lookup-responses-end


.. _endpoint-post-profile-store-lookup-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-post-profile-store-lookup-response-200ok-start

The **200** response returns the matching profile.

.. code-block:: json
   :linenos:

   {
     "collection_id": "{collection-id}",
     "profile_id": "{profile-id}",
     "attributes": {
       "email": "customer@example.com"
     },
     "created_at": "{timestamp}",
     "updated_at": "{timestamp}",
     "ticked_at": "{timestamp}",
     "links": {
       "email": ["customer@example.com"],
       "phone": ["+15555550100"]
     }
   }

.. endpoint-post-profile-store-lookup-response-200ok-end


.. _endpoint-post-profile-store-lookup-response-other:

Other responses
--------------------------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Status
     - Description

   * - **400**
     - No keychain keys were provided. At least one key is required.

   * - **404**
     - No matching profile was found in the profile store.
