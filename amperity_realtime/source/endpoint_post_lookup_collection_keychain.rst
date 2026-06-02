.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
         Look up a real-time customer profile by identity key using a request body.

.. meta::
    :content class=swiftype name=body data-type=text:
         Look up a real-time customer profile by identity key using a request body.

.. meta::
    :content class=swiftype name=title data-type=string:
        POST /lookup/{collection-id}/keychain

==================================================
POST /lookup/{collection-id}/keychain
==================================================

.. endpoint-post-lookup-collection-keychain-start

Use the **POST /lookup/{collection-id}/keychain** endpoint to look up a customer profile from a real-time profile collection using an identity key provided in the request body. Because the key is not part of the URL it does not appear in server access logs, CDN logs, or proxy logs. Use this endpoint when the identity key is PII, such as an email address, phone number, or loyalty ID, where exposing the value in logs is not acceptable.

When the identity key is a non-PII opaque identifier, such as an internal UUID, :doc:`GET /lookup/{collection-id}/keychain <endpoint_get_lookup_collection_keychain>` is a simpler alternative that supports edge caching.

.. endpoint-post-lookup-collection-keychain-end

.. endpoint-post-lookup-collection-keychain-note-start

.. note:: Exactly one identity linking key must be provided in the ``keys`` object. The key name must match a linking key configured for the collection.

.. endpoint-post-lookup-collection-keychain-note-end


.. _endpoint-post-lookup-collection-keychain-prerequisites:

Prerequisites
==================================================

.. endpoint-post-lookup-collection-keychain-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>` with the **Real-time API data access** policy.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-post-lookup-collection-keychain-prerequisites-end


.. _endpoint-post-lookup-collection-keychain-request-url:

Request URL
==================================================

.. endpoint-post-lookup-collection-keychain-request-url-start

Direct all requests to the **POST /lookup/{collection-id}/keychain** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/lookup/{collection-id}/keychain

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/lookup/{collection-id}/keychain

.. endpoint-post-lookup-collection-keychain-request-url-end

.. include:: base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-post-lookup-collection-keychain-rate-limit:

Rate limit
==================================================

.. include:: rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

.. include:: rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _endpoint-post-lookup-collection-keychain-request:

Requests
==================================================

.. endpoint-post-lookup-collection-keychain-request-start

A request to the **POST /lookup/{collection-id}/keychain** endpoint is similar to:

.. code-block:: rest

   curl --request POST \
          'https://app.amperity.com/prof/lookup/{collection-id}/keychain' \
        --header 'Amperity-Tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}' \
        --header 'Content-Type: application/json' \
        --data '{"keys": {"email": "user@example.com"}}'

This example is formatted for readability in a narrow page layout.

.. endpoint-post-lookup-collection-keychain-request-end


.. _endpoint-post-lookup-collection-keychain-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-post-lookup-collection-keychain-request-parameters-start

The following table describes the parameters that may be used with the **POST /lookup/{collection-id}/keychain** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **keys**
     - Object. Required.

       An object containing exactly one identity key-value pair. The key name must match a linking key configured for the collection.

       For example: ``{"email": "user@example.com"}`` or ``{"loyalty_id": "123456789"}``.

   * - **enrich**
     - Boolean. Optional.

       Set to **true** to return enriched profile data. Default value: **false**.

.. endpoint-post-lookup-collection-keychain-request-parameters-end


.. _endpoint-post-lookup-collection-keychain-request-examples:

Request examples
--------------------------------------------------

.. endpoint-post-lookup-collection-keychain-request-examples-start

The following examples show how to send requests to the **POST /lookup/{collection-id}/keychain** endpoint.

.. endpoint-post-lookup-collection-keychain-request-examples-end

.. endpoint-post-lookup-collection-keychain-request-examples-tabs-start

.. tabs::

   .. tab:: cURL

      The following example looks up a hotel guest by loyalty ID when they arrive at the booking site, so their preferences and status can be loaded before they search for rooms.

      .. code-block:: rest

         curl --request POST \
                'https://app.amperity.com/prof/lookup/{collection-id}/keychain' \
              --header 'Amperity-Tenant: {tenant-id}' \
              --header 'Authorization: Bearer {token}' \
              --header 'Content-Type: application/json' \
              --data '{"keys": {"loyalty_id": "LYL-556677"}}'

   .. tab:: Python

      The following example looks up a retail customer by email address when they sign in, so their purchase history and loyalty tier can be used to personalize recommendations.

      .. code-block:: python
         :linenos:

         import requests

         url = "https://app.amperity.com/prof/lookup/{collection-id}/keychain"

         headers = {
           "Authorization": "Bearer {token}",
           "Amperity-Tenant": "{tenant-id}",
           "Content-Type": "application/json"
         }

         body = {
           "keys": {"email": "j.henderson@example.com"}
         }

         response = requests.post(url, headers=headers, json=body)
         if response.status_code == 200:
           profile = response.json()
           print("Profile ID:", profile.get("profile_id"))
           print("Attributes:", profile.get("attributes"))
         elif response.status_code == 404:
           print("No profile found--treat as anonymous user")

   .. tab:: Node.js

      The following example looks up a restaurant customer by phone number when they open the app, so their saved preferences and order history can be surfaced immediately.

      .. code-block:: javascript
         :linenos:

         const https = require('https');

         const collectionId = '{collection-id}';
         const body = JSON.stringify({
           keys: { phone: '+13125550142' }  // captured at app login
         });

         const options = {
           hostname: 'app.amperity.com',
           path: `/prof/lookup/${collectionId}/keychain`,
           method: 'POST',
           headers: {
             'Authorization': 'Bearer {token}',
             'Amperity-Tenant': '{tenant-id}',
             'Content-Type': 'application/json',
             'Content-Length': Buffer.byteLength(body)
           }
         };

         const req = https.request(options, (res) => {
           let data = '';
           res.on('data', chunk => data += chunk);
           res.on('end', () => {
             if (res.statusCode === 200) {
               const profile = JSON.parse(data);
               console.log('Profile ID:', profile.profile_id);
               console.log('Attributes:', profile.attributes);
             } else if (res.statusCode === 404) {
               console.log('New customer--show registration prompt');
             }
           });
         });
         req.write(body);
         req.end();

   .. tab:: JavaScript

      The following example looks up a car rental customer by email after they authenticate on the booking site, so their driver details and membership tier can be pre-filled in the reservation form.

      .. code-block:: javascript
         :linenos:

         async function lookupRentalCustomer(email) {
           const collectionId = '{collection-id}';
           const url = `https://app.amperity.com/prof/lookup/${collectionId}/keychain`;

           const response = await fetch(url, {
             method: 'POST',
             headers: {
               'Authorization': 'Bearer {token}',
               'Amperity-Tenant': '{tenant-id}',
               'Content-Type': 'application/json'
             },
             body: JSON.stringify({ keys: { email } })
           });

           if (response.ok) {
             const profile = await response.json();
             // Pre-fill reservation form with known driver details
             prefillForm(profile.attributes);
             return profile;
           } else if (response.status === 404) {
             // Unknown customer--show new member enrollment offer
             showEnrollmentBanner();
             return null;
           }
         }

.. endpoint-post-lookup-collection-keychain-request-examples-tabs-end


.. _endpoint-post-lookup-collection-keychain-responses:

Responses
==================================================

.. endpoint-post-lookup-collection-keychain-responses-start

A response from the **POST /lookup/{collection-id}/keychain** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the matching profile. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-post-lookup-collection-keychain-responses-end


.. _endpoint-post-lookup-collection-keychain-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-post-lookup-collection-keychain-response-200ok-start

The **200** response returns the matching customer profile, similar to:

.. code-block:: json
   :linenos:

   {
     "collection_id": "col-abc123",
     "profile_id": "prf-xyz789",
     "attributes": {
       "first_name": "Daniel",
       "last_name": "Kuhlman",
       "email": "danielkuhlman@email.com",
       "loyalty_id": "123456789-0"
     },
     "created_at": "2026-01-15T10:30:00.000Z",
     "updated_at": "2026-05-14T08:00:00.000Z"
   }

.. endpoint-post-lookup-collection-keychain-response-200ok-end


.. _endpoint-post-lookup-collection-keychain-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-post-lookup-collection-keychain-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **attributes**
     - A JSON object containing the attribute fields for the profile. The fields present depend on the attributes configured for the collection.

   * - **collection_id**
     - The unique identifier for the profile collection.

   * - **created_at**
     - The date and time at which the profile was created, in |ext_iso_8601| format and in UTC.

   * - **links**
     - Optional. An array of identity links associated with this profile.

   * - **profile_id**
     - The unique identifier for the customer profile.

   * - **ticked_at**
     - Optional. The date and time at which the profile was last processed by the identity resolution pipeline, in |ext_iso_8601| format and in UTC.

   * - **updated_at**
     - The date and time at which the profile was last updated, in |ext_iso_8601| format and in UTC.

.. endpoint-post-lookup-collection-keychain-response-parameters-end
