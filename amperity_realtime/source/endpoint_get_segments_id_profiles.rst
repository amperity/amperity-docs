.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
         Return a list of profiles that are members of a real-time segment.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return a list of profiles that are members of a real-time segment.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /segments/{segment-id}/profiles

==================================================
GET /segments/{segment-id}/profiles
==================================================

.. endpoint-get-segments-id-profiles-start

Use the **GET /segments/{segment-id}/profiles** endpoint to return a paginated list of customer profiles that are members of the specified real-time segment.

.. endpoint-get-segments-id-profiles-end


.. _endpoint-get-segments-id-profiles-prerequisites:

Prerequisites
==================================================

.. endpoint-get-segments-id-profiles-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>` with the **Real-time API data access** policy.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-segments-id-profiles-prerequisites-end


.. _endpoint-get-segments-id-profiles-request-url:

Request URL
==================================================

.. endpoint-get-segments-id-profiles-request-url-start

Direct all requests to the **GET /segments/{segment-id}/profiles** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/segments/{segment-id}/profiles

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/segments/{segment-id}/profiles

.. endpoint-get-segments-id-profiles-request-url-end

.. include:: base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-segments-id-profiles-rate-limit:

Rate limit
==================================================

.. include:: rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

.. include:: rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _endpoint-get-segments-id-profiles-request:

Requests
==================================================

.. endpoint-get-segments-id-profiles-request-start

A request to the **GET /segments/{segment-id}/profiles** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/segments/{segment-id}/profiles \
          ?limit=25' \
        --header 'Amperity-Tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-segments-id-profiles-request-end


.. _endpoint-get-segments-id-profiles-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-segments-id-profiles-request-parameters-start

The following table describes the parameters that may be used with the **GET /segments/{segment-id}/profiles** endpoint.

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

.. endpoint-get-segments-id-profiles-request-parameters-end


.. _endpoint-get-segments-id-profiles-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-segments-id-profiles-request-examples-start

The following examples show how to send requests to the **GET /segments/{segment-id}/profiles** endpoint.

.. endpoint-get-segments-id-profiles-request-examples-end

.. endpoint-get-segments-id-profiles-request-examples-tabs-start

.. tabs::

   .. tab:: cURL

      The following example returns the first page of profiles that belong to a real-time segment.

      .. code-block:: rest

         curl --request GET \
                'https://app.amperity.com/prof/segments/{segment-id}/profiles \
                ?limit=25' \
              --header 'Amperity-Tenant: {tenant-id}' \
              --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

   .. tab:: Python

      The following example iterates through all pages of profiles in a segment and collects every profile ID, which a retail marketing team can then use to build a targeted campaign audience.

      .. code-block:: python
         :linenos:

         import requests

         base_url = "https://app.amperity.com/prof/segments/{segment-id}/profiles"

         headers = {
           "Authorization": "Bearer {token}",
           "Amperity-Tenant": "{tenant-id}"
         }

         params = {"limit": 100}
         profiles = []

         while True:
           response = requests.get(base_url, headers=headers, params=params)
           data = response.json()
           profiles.extend(data.get("data", []))
           next_token = data.get("next_token")
           if not next_token:
             break
           params["next_token"] = next_token

         print(f"Total profiles: {len(profiles)}")

   .. tab:: Node.js

      The following example pages through all profiles in a segment from a Node.js backend service and writes each profile ID to an array, which a restaurant loyalty platform can use to trigger a targeted re-engagement campaign.

      .. code-block:: javascript
         :linenos:

         const https = require('https');

         function fetchPage(segmentId, nextToken) {
           return new Promise((resolve, reject) => {
             const path = `/prof/segments/${segmentId}/profiles?limit=100` +
               (nextToken ? `&next_token=${encodeURIComponent(nextToken)}` : '');

             const options = {
               hostname: 'app.amperity.com',
               path,
               method: 'GET',
               headers: {
                 'Authorization': 'Bearer {token}',
                 'Amperity-Tenant': '{tenant-id}'
               }
             };

             https.request(options, (res) => {
               let body = '';
               res.on('data', chunk => body += chunk);
               res.on('end', () => resolve(JSON.parse(body)));
             }).on('error', reject).end();
           });
         }

         async function getAllProfiles(segmentId) {
           const profiles = [];
           let nextToken = null;

           do {
             const data = await fetchPage(segmentId, nextToken);
             profiles.push(...data.data);
             nextToken = data.next_token || null;
           } while (nextToken);

           console.log(`Total profiles: ${profiles.length}`);
           return profiles;
         }

         getAllProfiles('{segment-id}');

   .. tab:: PHP

      The following example pages through all profiles in a segment from a PHP backend and collects profile IDs that a banking marketing team can use to send a personalized offer to a targeted customer group.

      .. code-block:: php
         :linenos:

         <?php

         $segmentId = '{segment-id}';
         $profiles  = [];
         $nextToken = null;

         do {
           $url = sprintf(
             'https://app.amperity.com/prof/segments/%s/profiles?limit=100%s',
             $segmentId,
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

           $profiles = array_merge($profiles, $data['data'] ?? []);
         } while ($nextToken);

         echo "Total profiles: " . count($profiles) . "\n";

   .. tab:: Java

      The following example pages through all profiles in a segment from a Java backend service and collects profile IDs that a retail loyalty platform can use to issue targeted reward notifications.

      .. code-block:: java
         :linenos:

         import java.net.URI;
         import java.net.URLEncoder;
         import java.net.http.HttpClient;
         import java.net.http.HttpRequest;
         import java.net.http.HttpResponse;
         import java.nio.charset.StandardCharsets;
         import java.util.ArrayList;
         import java.util.List;
         import com.fasterxml.jackson.databind.JsonNode;
         import com.fasterxml.jackson.databind.ObjectMapper;

         public class SegmentProfilesExample {
           private static final HttpClient CLIENT = HttpClient.newHttpClient();
           private static final ObjectMapper MAPPER = new ObjectMapper();

           public static void main(String[] args) throws Exception {
             String segmentId = "{segment-id}";
             List<String> profileIds = new ArrayList<>();
             String nextToken = null;

             do {
               String path = String.format(
                 "https://app.amperity.com/prof/segments/%s/profiles?limit=100%s",
                 segmentId,
                 nextToken != null
                   ? "&next_token=" + URLEncoder.encode(nextToken, StandardCharsets.UTF_8)
                   : ""
               );

               HttpRequest request = HttpRequest.newBuilder()
                 .uri(URI.create(path))
                 .header("Authorization", "Bearer {token}")
                 .header("Amperity-Tenant", "{tenant-id}")
                 .GET()
                 .build();

               HttpResponse<String> response = CLIENT.send(
                 request, HttpResponse.BodyHandlers.ofString()
               );

               JsonNode body = MAPPER.readTree(response.body());
               body.path("data").forEach(p ->
                 profileIds.add(p.path("profile_id").asText())
               );
               nextToken = body.path("next_token").asText(null);
             } while (nextToken != null && !nextToken.isEmpty());

             System.out.println("Total profiles: " + profileIds.size());
           }
         }

.. endpoint-get-segments-id-profiles-request-examples-tabs-end


.. _endpoint-get-segments-id-profiles-responses:

Responses
==================================================

.. endpoint-get-segments-id-profiles-responses-start

A response from the **GET /segments/{segment-id}/profiles** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-segments-id-profiles-responses-end


.. _endpoint-get-segments-id-profiles-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-segments-id-profiles-response-200ok-start

The **200** response returns a paginated list of profiles that are members of the segment, similar to:

.. code-block:: json
   :linenos:

   {
     "data": [
       {
         "profile_id": "prf-xyz789"
       },
       {
         "profile_id": "prf-def456"
       }
     ],
     "next_token": "ABCa1bcdDEe2f3G",
     "total": 4821
   }

.. endpoint-get-segments-id-profiles-response-200ok-end


.. _endpoint-get-segments-id-profiles-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-segments-id-profiles-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of profile objects for the current page of results. Each object includes the following property:

       **profile_id**
          The unique identifier for the customer profile.

   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.

   * - **total**
     - The total number of profiles that are members of the segment.

.. endpoint-get-segments-id-profiles-response-parameters-end
