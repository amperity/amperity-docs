.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Look up a profile in a profile store by keychain keys.

.. meta::
    :content class=swiftype name=body data-type=text:
        Look up a profile in a profile store by keychain keys.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /lookup/{collection-id}/keychain

==================================================
GET /lookup/{collection-id}/keychain
==================================================

.. endpoint-get-profile-store-lookup-start

Use the **GET /lookup/{collection-id}/keychain** endpoint to find a single profile in a profile store by one or more keychain keys, such as an email address or loyalty ID. Keychain keys are passed as query string parameters.

.. endpoint-get-profile-store-lookup-end

.. note:: In the Amperity user interface a profile store is shown on the **Profiles** page and may also be referred to as a profile collection. The value for **{collection-id}** identifies that profile store.


.. _endpoint-get-profile-store-lookup-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-store-lookup-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.
#. A profile store must be configured for your tenant. To set up a profile store, contact your Amperity representative.

.. endpoint-get-profile-store-lookup-prerequisites-end

.. note:: The access token must be granted the **profile-collections:read** and **pii:read** permissions.


.. _endpoint-get-profile-store-lookup-request-url:

Request URL
==================================================

.. endpoint-get-profile-store-lookup-request-url-start

Direct all requests to the **GET /lookup/{collection-id}/keychain** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/lookup/{collection-id}/keychain

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/lookup/{collection-id}/keychain

.. endpoint-get-profile-store-lookup-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profile-store-lookup-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-store-lookup-request:

Requests
==================================================

.. endpoint-get-profile-store-lookup-request-start

A request to the **GET /lookup/{collection-id}/keychain** endpoint passes one or more keychain keys as query string parameters. At least one key is required.

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/lookup/{collection-id}/keychain?email=customer@example.com' \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-store-lookup-request-end


.. _endpoint-get-profile-store-lookup-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-store-lookup-request-parameters-start

The following table describes the parameters that may be used with the **GET /lookup/{collection-id}/keychain** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **collection-id**
     - String. Required.

       The ID of the profile store to search.

   * - **keychain keys**
     - String. Required.

       One or more keychain keys, passed as query string parameters in the form ``{key}={value}``. For example: ``email=customer@example.com``. At least one key is required.

   * - **_enrich**
     - Boolean. Optional.

       Set to **true** to include enriched attributes in the returned profile. Default value: **false**.

.. endpoint-get-profile-store-lookup-request-parameters-end


.. _endpoint-get-profile-store-lookup-responses:

Responses
==================================================

.. endpoint-get-profile-store-lookup-responses-start

A response from the **GET /lookup/{collection-id}/keychain** endpoint will match an :doc:`HTTP status code <responses>`. A **200** response returns the matching profile. The **Location** header of a **200** response contains the URL for the matched profile.

.. endpoint-get-profile-store-lookup-responses-end


.. _endpoint-get-profile-store-lookup-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-store-lookup-response-200ok-start

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

.. endpoint-get-profile-store-lookup-response-200ok-end


.. _endpoint-get-profile-store-lookup-response-other:

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
