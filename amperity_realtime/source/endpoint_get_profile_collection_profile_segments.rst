.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
         Return the real-time segments a customer profile belongs to.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return the real-time segments a customer profile belongs to.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /profiles/{collection-id}/{profile-id}/segments

===================================================
GET /profiles/{collection-id}/{profile-id}/segments
===================================================

.. endpoint-get-profile-collection-profile-segments-start

Use the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint to return a paginated list of real-time segments that the specified customer profile is a member of.

.. endpoint-get-profile-collection-profile-segments-end


.. _endpoint-get-profile-collection-profile-segments-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-collection-profile-segments-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>` with the **Real-time API data access** policy.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-profile-collection-profile-segments-prerequisites-end


.. _endpoint-get-profile-collection-profile-segments-request-url:

Request URL
==================================================

.. endpoint-get-profile-collection-profile-segments-request-url-start

Direct all requests to the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/profiles/{collection-id}/{profile-id}/segments

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/profiles/{collection-id}/{profile-id}/segments

.. endpoint-get-profile-collection-profile-segments-request-url-end

.. include:: base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profile-collection-profile-segments-rate-limit:

Rate limit
==================================================

.. include:: rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

.. include:: rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _endpoint-get-profile-collection-profile-segments-request:

Requests
==================================================

.. endpoint-get-profile-collection-profile-segments-request-start

A request to the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/profiles/{collection-id}/{profile-id}/segments \
          ?limit=25' \
        --header 'Amperity-Tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-collection-profile-segments-request-end


.. _endpoint-get-profile-collection-profile-segments-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-collection-profile-segments-request-parameters-start

The following table describes the parameters that may be used with the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **limit**
     - Integer. Optional.

       The maximum number of records to include in a single page of results.

   * - **next_token**
     - String. Optional.

       An opaque token that is used to paginate results. Omit the **next_token** property to return the first page. Use the cursor value for **next_token** that was returned in a response to view the next page of results.

       For example: **ABCd1fghIJk2l3M**

       .. note:: The possible values for **next_token** are returned within the **200** response.

       .. important:: The value for **next_token** cannot be **NULL**.

.. endpoint-get-profile-collection-profile-segments-request-parameters-end


.. _endpoint-get-profile-collection-profile-segments-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-profile-collection-profile-segments-request-examples-start

The following examples show how to send requests to the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint.

.. endpoint-get-profile-collection-profile-segments-request-examples-end

.. endpoint-get-profile-collection-profile-segments-request-examples-tabs-start

.. tabs::

   .. tab:: cURL

      The following example returns the real-time segments a hotel guest belongs to after check-in so personalized in-stay offers can be triggered based on their loyalty tier and travel patterns.

      .. code-block:: rest

         curl --request GET \
                'https://app.amperity.com/prof/profiles/{collection-id}/prf-xyz789/segments \
                ?limit=25' \
              --header 'Amperity-Tenant: {tenant-id}' \
              --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

   .. tab:: Python

      The following example returns all segments a retail customer belongs to when they sign in, then filters for high-value segments to decide which promotional banner to display.

      .. code-block:: python
         :linenos:

         import requests

         collection_id = "{collection-id}"
         profile_id    = "prf-xyz789"

         url = f"https://app.amperity.com/prof/profiles/{collection_id}/{profile_id}/segments"

         headers = {
           "Authorization": "Bearer {token}",
           "Amperity-Tenant": "{tenant-id}"
         }

         segments = []
         params   = {"limit": 100}

         while True:
           response = requests.get(url, headers=headers, params=params)
           data = response.json()
           segments.extend(data.get("data", []))
           next_token = data.get("next_token")
           if not next_token:
             break
           params["next_token"] = next_token

         segment_names = [s["segment_name"] for s in segments]
         if "High LTV--90 Day" in segment_names:
           show_vip_banner()

   .. tab:: Node.js

      The following example returns the segments a restaurant customer belongs to when they open the app so the home screen can highlight relevant loyalty rewards and personalized menu suggestions.

      .. code-block:: javascript
         :linenos:

         const https = require('https');

         const collectionId = '{collection-id}';
         const profileId    = 'prf-xyz789';

         const options = {
           hostname: 'app.amperity.com',
           path: `/prof/profiles/${collectionId}/${profileId}/segments?limit=50`,
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
               const { data } = JSON.parse(body);
               const names = data.map(s => s.segment_name);
               console.log('Member of segments:', names);
             }
           });
         }).end();

   .. tab:: JavaScript

      The following example returns the segments a car rental customer belongs to after authentication so the booking page can apply the correct member discount and surface upgrade offers.

      .. code-block:: javascript
         :linenos:

         async function getCustomerSegments(profileId) {
           const collectionId = '{collection-id}';
           const url = new URL(
             `https://app.amperity.com/prof/profiles/${collectionId}/${profileId}/segments`
           );
           url.searchParams.set('limit', '50');

           const response = await fetch(url.toString(), {
             method: 'GET',
             headers: {
               'Authorization': 'Bearer {token}',
               'Amperity-Tenant': '{tenant-id}'
             }
           });

           if (response.ok) {
             const { data } = await response.json();
             const segmentIds = data.map(s => s.segment_id);

             // Apply member discount if customer is in the elite tier segment
             if (segmentIds.includes('rts-elite-members')) {
               applyMemberDiscount(0.15);
             }
             return data;
           }
           return [];
         }

   .. tab:: PHP

      The following example returns the segments a banking customer belongs to when they log in so the dashboard can display targeted product offers based on their financial profile.

      .. code-block:: php
         :linenos:

         <?php

         $collectionId = '{collection-id}';
         $profileId    = 'prf-xyz789';
         $segments     = [];
         $nextToken    = null;

         do {
           $url = sprintf(
             'https://app.amperity.com/prof/profiles/%s/%s/segments?limit=100%s',
             $collectionId,
             $profileId,
             $nextToken ? '&next_token=' . urlencode($nextToken) : ''
           );

           $ch = curl_init($url);
           curl_setopt_array($ch, [
             CURLOPT_RETURNTRANSFER => true,
             CURLOPT_HTTPHEADER     => [
               'Authorization: Bearer {token}',
               'Amperity-Tenant: {tenant-id}'
             ]
           ]);

           $data      = json_decode(curl_exec($ch), true);
           $nextToken = $data['next_token'] ?? null;
           curl_close($ch);

           $segments = array_merge($segments, $data['data'] ?? []);
         } while ($nextToken);

         // Show mortgage offer only to relevant segment
         $names = array_column($segments, 'segment_name');
         if (in_array('Mortgage Ready', $names)) {
           renderMortgageOffer();
         }

   .. tab:: Java

      The following example returns the segments a retail customer belongs to when they scan their loyalty card at checkout so the point-of-sale system can display applicable rewards and tier benefits.

      .. code-block:: java
         :linenos:

         import java.net.URI;
         import java.net.http.HttpClient;
         import java.net.http.HttpRequest;
         import java.net.http.HttpResponse;

         public class ProfileSegmentsExample {
           public static void main(String[] args) throws Exception {

             String collectionId = "{collection-id}";
             String profileId    = "prf-xyz789";

             String url = String.format(
               "https://app.amperity.com/prof/profiles/%s/%s/segments?limit=50",
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
               System.out.println("Segments: " + response.body());
             } else {
               System.out.println("Error: " + response.statusCode());
             }
           }
         }

   .. tab:: Swift

      The following example returns the segments a hotel guest belongs to after loyalty check-in so the mobile app can display personalized in-stay offers and upgrade prompts.

      .. code-block:: swift
         :linenos:

         import Foundation

         func fetchGuestSegments(profileId: String) {
           let collectionId = "{collection-id}"
           var components = URLComponents(
             string: "https://app.amperity.com/prof/profiles/\(collectionId)/\(profileId)/segments"
           )!
           components.queryItems = [URLQueryItem(name: "limit", value: "50")]

           var request = URLRequest(url: components.url!)
           request.httpMethod = "GET"
           request.setValue("Bearer {token}", forHTTPHeaderField: "Authorization")
           request.setValue("{tenant-id}", forHTTPHeaderField: "Amperity-Tenant")

           URLSession.shared.dataTask(with: request) { data, response, _ in
             guard let http = response as? HTTPURLResponse,
                   http.statusCode == 200,
                   let data = data,
                   let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
                   let segments = json["data"] as? [[String: Any]] else { return }

             let names = segments.compactMap { $0["segment_name"] as? String }
             DispatchQueue.main.async {
               self.renderPersonalizedOffers(segments: names)
             }
           }.resume()
         }

.. endpoint-get-profile-collection-profile-segments-request-examples-tabs-end


.. _endpoint-get-profile-collection-profile-segments-responses:

Responses
==================================================

.. endpoint-get-profile-collection-profile-segments-responses-start

A response from the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-profile-collection-profile-segments-responses-end


.. _endpoint-get-profile-collection-profile-segments-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-collection-profile-segments-response-200ok-start

The **200** response returns a paginated list of real-time segments the profile belongs to, similar to:

.. code-block:: json
   :linenos:

   {
     "data": [
       {
         "segment_id": "rts-abc001",
         "segment_name": "Gold Loyalty Members"
       },
       {
         "segment_id": "rts-abc002",
         "segment_name": "High LTV--90 Day"
       }
     ],
     "next_token": "ABCa1bcdDEe2f3G",
     "total": 2
   }

.. endpoint-get-profile-collection-profile-segments-response-200ok-end


.. _endpoint-get-profile-collection-profile-segments-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-profile-collection-profile-segments-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of segment membership objects for the current page of results. Each object includes the following properties:

       **segment_id**
          The unique identifier for the real-time segment.

       **segment_name**
          The display name of the real-time segment.

   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.

   * - **total**
     - The total number of segments the profile belongs to.

.. endpoint-get-profile-collection-profile-segments-response-parameters-end
