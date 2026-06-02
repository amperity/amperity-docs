.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
         Look up a real-time customer profile by identity key using a query parameter.

.. meta::
    :content class=swiftype name=body data-type=text:
         Look up a real-time customer profile by identity key using a query parameter.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /lookup/{collection-id}/keychain

==================================================
GET /lookup/{collection-id}/keychain
==================================================

.. endpoint-get-lookup-collection-keychain-start

Use the **GET /lookup/{collection-id}/keychain** endpoint to look up a customer profile from a real-time profile collection using an identity key provided as a query parameter. Because the key is part of the URL it will appear in server access logs, CDN logs, and proxy logs. Use this endpoint when the identity key is a non-PII opaque identifier, such as an internal UUID, where URL logging is acceptable.

When the identity key is PII, such as an email address, phone number, or loyalty ID, use :doc:`POST /lookup/{collection-id}/keychain <endpoint_post_lookup_collection_keychain>` instead, which sends the key in the request body and keeps it out of logs.

.. endpoint-get-lookup-collection-keychain-end

.. endpoint-get-lookup-collection-keychain-note-start

.. note:: Exactly one identity linking key must be provided as a query parameter. The key name must match a linking key configured for the collection.

.. endpoint-get-lookup-collection-keychain-note-end


.. _endpoint-get-lookup-collection-keychain-prerequisites:

Prerequisites
==================================================

.. endpoint-get-lookup-collection-keychain-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>` with the **Real-time API data access** policy.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-lookup-collection-keychain-prerequisites-end


.. _endpoint-get-lookup-collection-keychain-request-url:

Request URL
==================================================

.. endpoint-get-lookup-collection-keychain-request-url-start

Direct all requests to the **GET /lookup/{collection-id}/keychain** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/lookup/{collection-id}/keychain

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/lookup/{collection-id}/keychain

.. endpoint-get-lookup-collection-keychain-request-url-end

.. include:: base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-lookup-collection-keychain-rate-limit:

Rate limit
==================================================

.. include:: rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

.. include:: rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _endpoint-get-lookup-collection-keychain-request:

Requests
==================================================

.. endpoint-get-lookup-collection-keychain-request-start

A request to the **GET /lookup/{collection-id}/keychain** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/lookup/{collection-id}/keychain \
          ?email=user@example.com' \
        --header 'Amperity-Tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-lookup-collection-keychain-request-end


.. _endpoint-get-lookup-collection-keychain-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-lookup-collection-keychain-request-parameters-start

The following table describes the parameters that may be used with the **GET /lookup/{collection-id}/keychain** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **<linking-key>**
     - String. Required.

       The identity linking key and value to use for the lookup. Exactly one linking key must be provided. Replace ``<linking-key>`` with the name of a configured identity key for this collection.

       For example: ``?email=user@example.com`` or ``?loyalty_id=123456789``.

   * - **enrich**
     - Boolean. Optional.

       Set to **true** to return enriched profile data. Default value: **false**.

.. endpoint-get-lookup-collection-keychain-request-parameters-end


.. _endpoint-get-lookup-collection-keychain-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-lookup-collection-keychain-request-examples-start

The following examples show how to send requests to the **GET /lookup/{collection-id}/keychain** endpoint.

.. endpoint-get-lookup-collection-keychain-request-examples-end

.. endpoint-get-lookup-collection-keychain-request-examples-tabs-start

.. tabs::

   .. tab:: cURL

      The following example looks up a hotel guest by loyalty ID when they arrive at the booking site, so their preferences and status can be loaded before they search for rooms.

      .. code-block:: rest

         curl --request GET \
                'https://app.amperity.com/prof/lookup/{collection-id}/keychain \
                ?loyalty_id=LYL-556677' \
              --header 'Amperity-Tenant: {tenant-id}' \
              --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

   .. tab:: Python

      The following example looks up a retail customer by email address when they sign in, so their purchase history and loyalty tier can be used to personalize recommendations.

      .. code-block:: python
         :linenos:

         import requests

         url = "https://app.amperity.com/prof/lookup/{collection-id}/keychain"

         headers = {
           "Authorization": "Bearer {token}",
           "Amperity-Tenant": "{tenant-id}"
         }

         # Look up by email address captured at sign-in
         params = {
           "email": "j.henderson@example.com"
         }

         response = requests.get(url, headers=headers, params=params)
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
         const phone = '+13125550142';  // captured at app login

         const options = {
           hostname: 'app.amperity.com',
           path: `/prof/lookup/${collectionId}/keychain?phone=${encodeURIComponent(phone)}`,
           method: 'GET',
           headers: {
             'Authorization': 'Bearer {token}',
             'Amperity-Tenant': '{tenant-id}'
           }
         };

         https.request(options, (res) => {
           let body = '';
           res.on('data', chunk => body += chunk);
           res.on('end', () => {
             if (res.statusCode === 200) {
               const profile = JSON.parse(body);
               console.log('Profile ID:', profile.profile_id);
               console.log('Attributes:', profile.attributes);
             } else if (res.statusCode === 404) {
               console.log('New customer--show registration prompt');
             }
           });
         }).end();

   .. tab:: JavaScript

      The following example looks up a car rental customer by email after they authenticate on the booking site, so their driver details and membership tier can be pre-filled in the reservation form.

      .. code-block:: javascript
         :linenos:

         async function lookupRentalCustomer(email) {
           const collectionId = '{collection-id}';
           const url = new URL(
             `https://app.amperity.com/prof/lookup/${collectionId}/keychain`
           );
           url.searchParams.set('email', email);

           const response = await fetch(url.toString(), {
             method: 'GET',
             headers: {
               'Authorization': 'Bearer {token}',
               'Amperity-Tenant': '{tenant-id}'
             }
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

   .. tab:: PHP

      The following example looks up a banking customer by their customer ID when they log in, so their account summary and product recommendations can be personalized.

      .. code-block:: php
         :linenos:

         <?php

         $collectionId = '{collection-id}';
         $customerId   = 'CUS-112233';  // from authenticated session

         $url = sprintf(
           'https://app.amperity.com/prof/lookup/%s/keychain?customer_id=%s',
           $collectionId,
           urlencode($customerId)
         );

         $ch = curl_init($url);
         curl_setopt_array($ch, [
           CURLOPT_RETURNTRANSFER => true,
           CURLOPT_HTTPHEADER     => [
             'Authorization: Bearer {token}',
             'Amperity-Tenant: {tenant-id}'
           ]
         ]);

         $body   = curl_exec($ch);
         $status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
         curl_close($ch);

         if ($status === 200) {
           $profile = json_decode($body, true);
           // Load personalized dashboard content
           renderDashboard($profile['attributes']);
         } elseif ($status === 404) {
           // First-time online banking user
           renderOnboardingFlow();
         }

   .. tab:: Java

      The following example looks up a retail customer by their loyalty ID when they scan their card at checkout, so the point-of-sale system can display their tier status and available rewards.

      .. code-block:: java
         :linenos:

         import java.net.URI;
         import java.net.URLEncoder;
         import java.net.http.HttpClient;
         import java.net.http.HttpRequest;
         import java.net.http.HttpResponse;
         import java.nio.charset.StandardCharsets;

         public class ProfileLookupExample {
           public static void main(String[] args) throws Exception {

             String collectionId = "{collection-id}";
             String loyaltyId    = "LYL-998877";  // scanned from loyalty card

             String url = String.format(
               "https://app.amperity.com/prof/lookup/%s/keychain?loyalty_id=%s",
               collectionId,
               URLEncoder.encode(loyaltyId, StandardCharsets.UTF_8)
             );

             HttpRequest request = HttpRequest.newBuilder()
               .uri(URI.create(url))
               .header("Authorization", "Bearer {token}")
               .header("Amperity-Tenant", "{tenant-id}")
               .GET()
               .build();

             HttpResponse<String> response = HttpClient.newHttpClient()
               .send(request, HttpResponse.BodyHandlers.ofString());

             if (response.statusCode() == 200) {
               System.out.println("Profile: " + response.body());
             } else if (response.statusCode() == 404) {
               System.out.println("Unknown loyalty ID--prompt for enrollment");
             }
           }
         }

   .. tab:: Swift

      The following example looks up a hotel guest by their loyalty ID when they open the mobile app, so the home screen can display their upcoming reservation and member benefits.

      .. code-block:: swift
         :linenos:

         import Foundation

         func lookupGuestProfile(loyaltyId: String) {
           let collectionId = "{collection-id}"
           var components = URLComponents(
             string: "https://app.amperity.com/prof/lookup/\(collectionId)/keychain"
           )!
           components.queryItems = [
             URLQueryItem(name: "loyalty_id", value: loyaltyId)
           ]

           var request = URLRequest(url: components.url!)
           request.httpMethod = "GET"
           request.setValue("Bearer {token}", forHTTPHeaderField: "Authorization")
           request.setValue("{tenant-id}", forHTTPHeaderField: "Amperity-Tenant")

           URLSession.shared.dataTask(with: request) { data, response, _ in
             guard let http = response as? HTTPURLResponse else { return }
             if http.statusCode == 200, let data = data,
                let profile = try? JSONSerialization.jsonObject(with: data) as? [String: Any] {
               // Update home screen with member status and upcoming stays
               DispatchQueue.main.async {
                 self.updateHomeScreen(profile: profile)
               }
             } else if http.statusCode == 404 {
               // Guest not in system--show enrollment prompt
               DispatchQueue.main.async {
                 self.showEnrollmentPrompt()
               }
             }
           }.resume()
         }

.. endpoint-get-lookup-collection-keychain-request-examples-tabs-end


.. _endpoint-get-lookup-collection-keychain-responses:

Responses
==================================================

.. endpoint-get-lookup-collection-keychain-responses-start

A response from the **GET /lookup/{collection-id}/keychain** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the matching profile. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-lookup-collection-keychain-responses-end


.. _endpoint-get-lookup-collection-keychain-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-lookup-collection-keychain-response-200ok-start

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

.. endpoint-get-lookup-collection-keychain-response-200ok-end


.. _endpoint-get-lookup-collection-keychain-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-lookup-collection-keychain-response-parameters-start

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

.. endpoint-get-lookup-collection-keychain-response-parameters-end
