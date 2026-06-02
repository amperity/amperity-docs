.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
         Return a specific customer profile from a real-time profile collection.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return a specific customer profile from a real-time profile collection.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /profiles/{collection-id}/{profile-id}

==================================================
GET /profiles/{collection-id}/{profile-id}
==================================================

.. endpoint-get-profiles-collection-profile-start

Use the **GET /profiles/{collection-id}/{profile-id}** endpoint to return a specific customer profile from a real-time profile collection.

.. endpoint-get-profiles-collection-profile-end


.. _endpoint-get-profiles-collection-profile-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profiles-collection-profile-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>` with the **Real-time API data access** policy.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-profiles-collection-profile-prerequisites-end


.. _endpoint-get-profiles-collection-profile-request-url:

Request URL
==================================================

.. endpoint-get-profiles-collection-profile-request-url-start

Direct all requests to the **GET /profiles/{collection-id}/{profile-id}** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/profiles/{collection-id}/{profile-id}

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/profiles/{collection-id}/{profile-id}

.. endpoint-get-profiles-collection-profile-request-url-end

.. include:: base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profiles-collection-profile-rate-limit:

Rate limit
==================================================

.. include:: rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

.. include:: rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _endpoint-get-profiles-collection-profile-request:

Requests
==================================================

.. endpoint-get-profiles-collection-profile-request-start

A request to the **GET /profiles/{collection-id}/{profile-id}** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/profiles/{collection-id}/{profile-id}' \
        --header 'Amperity-Tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profiles-collection-profile-request-end


.. _endpoint-get-profiles-collection-profile-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profiles-collection-profile-request-parameters-start

The following table describes the parameters that may be used with the **GET /profiles/{collection-id}/{profile-id}** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **enrich**
     - Boolean. Optional.

       Set to **true** to return enriched profile data. Default value: **false**.

.. endpoint-get-profiles-collection-profile-request-parameters-end


.. _endpoint-get-profiles-collection-profile-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-profiles-collection-profile-request-examples-start

The following examples show how to send requests to the **GET /profiles/{collection-id}/{profile-id}** endpoint.

.. endpoint-get-profiles-collection-profile-request-examples-end

.. endpoint-get-profiles-collection-profile-request-examples-tabs-start

.. tabs::

   .. tab:: cURL

      The following example fetches a hotel guest's profile by profile ID at check-in so the front desk system can display their stay history and preferences.

      .. code-block:: rest

         curl --request GET \
                'https://app.amperity.com/prof/profiles/{collection-id}/prf-xyz789' \
              --header 'Amperity-Tenant: {tenant-id}' \
              --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

   .. tab:: Python

      The following example fetches a retail customer's profile after sign-in so the storefront can personalize product recommendations based on their loyalty tier and purchase history.

      .. code-block:: python
         :linenos:

         import requests

         collection_id = "{collection-id}"
         profile_id    = "prf-xyz789"  # resolved from prior lookup

         url = f"https://app.amperity.com/prof/profiles/{collection_id}/{profile_id}"

         headers = {
           "Authorization": "Bearer {token}",
           "Amperity-Tenant": "{tenant-id}"
         }

         response = requests.get(url, headers=headers)
         if response.status_code == 200:
           profile = response.json()
           tier = profile.get("attributes", {}).get("loyalty_tier", "standard")
           print("Loyalty tier:", tier)
         elif response.status_code == 404:
           print("Profile not found")

   .. tab:: Node.js

      The following example fetches a restaurant customer's profile when they open the app so their saved dietary preferences and favorite orders can be surfaced on the home screen.

      .. code-block:: javascript
         :linenos:

         const https = require('https');

         const collectionId = '{collection-id}';
         const profileId    = 'prf-xyz789';  // from session cookie or prior lookup

         const options = {
           hostname: 'app.amperity.com',
           path: `/prof/profiles/${collectionId}/${profileId}`,
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
               console.log('Dietary prefs:', profile.attributes?.dietary_preferences);
               console.log('Favorite cuisine:', profile.attributes?.favorite_cuisine);
             }
           });
         }).end();

   .. tab:: JavaScript

      The following example fetches a car rental customer's profile after authentication so the booking form can be pre-filled with their driver details and membership tier.

      .. code-block:: javascript
         :linenos:

         async function loadRentalProfile(profileId) {
           const collectionId = '{collection-id}';
           const url = `https://app.amperity.com/prof/profiles/${collectionId}/${profileId}`;

           const response = await fetch(url, {
             method: 'GET',
             headers: {
               'Authorization': 'Bearer {token}',
               'Amperity-Tenant': '{tenant-id}'
             }
           });

           if (response.ok) {
             const profile = await response.json();
             // Pre-fill reservation form with known driver details
             document.getElementById('driver-name').value =
               `${profile.attributes.first_name} ${profile.attributes.last_name}`;
             document.getElementById('membership-tier').value =
               profile.attributes.membership_tier ?? '';
             return profile;
           } else if (response.status === 404) {
             showNewMemberPrompt();
             return null;
           }
         }

   .. tab:: PHP

      The following example fetches a banking customer's profile when they log in to online banking so their account summary and product recommendations can be personalized.

      .. code-block:: php
         :linenos:

         <?php

         $collectionId = '{collection-id}';
         $profileId    = 'prf-xyz789';  // from authenticated session

         $url = sprintf(
           'https://app.amperity.com/prof/profiles/%s/%s',
           $collectionId,
           $profileId
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
           $segment = $profile['attributes']['customer_segment'] ?? 'standard';
           renderPersonalizedDashboard($segment, $profile['attributes']);
         } elseif ($status === 404) {
           renderOnboardingFlow();
         }

   .. tab:: Java

      The following example fetches a retail customer's profile when they scan their loyalty card at the point of sale so available rewards and tier status can be displayed on the register screen.

      .. code-block:: java
         :linenos:

         import java.net.URI;
         import java.net.http.HttpClient;
         import java.net.http.HttpRequest;
         import java.net.http.HttpResponse;

         public class FetchProfileExample {
           public static void main(String[] args) throws Exception {

             String collectionId = "{collection-id}";
             String profileId    = "prf-xyz789";  // resolved from loyalty card scan

             String url = String.format(
               "https://app.amperity.com/prof/profiles/%s/%s",
               collectionId, profileId
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
               System.out.println("Profile not found--prompt for enrollment");
             }
           }
         }

   .. tab:: Swift

      The following example fetches a hotel guest's profile after they complete a loyalty check-in so the mobile app home screen can display their member status and upcoming reservation.

      .. code-block:: swift
         :linenos:

         import Foundation

         func fetchGuestProfile(profileId: String) {
           let collectionId = "{collection-id}"
           let url = URL(
             string: "https://app.amperity.com/prof/profiles/\(collectionId)/\(profileId)"
           )!

           var request = URLRequest(url: url)
           request.httpMethod = "GET"
           request.setValue("Bearer {token}", forHTTPHeaderField: "Authorization")
           request.setValue("{tenant-id}", forHTTPHeaderField: "Amperity-Tenant")

           URLSession.shared.dataTask(with: request) { data, response, _ in
             guard let http = response as? HTTPURLResponse else { return }
             if http.statusCode == 200,
                let data = data,
                let profile = try? JSONSerialization.jsonObject(with: data) as? [String: Any] {
               DispatchQueue.main.async {
                 self.updateHomeScreen(profile: profile)
               }
             } else if http.statusCode == 404 {
               DispatchQueue.main.async {
                 self.showEnrollmentPrompt()
               }
             }
           }.resume()
         }

.. endpoint-get-profiles-collection-profile-request-examples-tabs-end


.. _endpoint-get-profiles-collection-profile-responses:

Responses
==================================================

.. endpoint-get-profiles-collection-profile-responses-start

A response from the **GET /profiles/{collection-id}/{profile-id}** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the matching profile. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-profiles-collection-profile-responses-end


.. _endpoint-get-profiles-collection-profile-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profiles-collection-profile-response-200ok-start

The **200** response returns the specified customer profile, similar to:

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

The fields returned in **attributes** depend on the attributes configured for the collection.

.. endpoint-get-profiles-collection-profile-response-200ok-end


.. _endpoint-get-profiles-collection-profile-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-profiles-collection-profile-response-parameters-start

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

.. endpoint-get-profiles-collection-profile-response-parameters-end
