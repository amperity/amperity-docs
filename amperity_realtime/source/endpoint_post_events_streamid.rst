.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
         Send a behavioral event to a real-time profile collection.

.. meta::
    :content class=swiftype name=body data-type=text:
         Send a behavioral event to a real-time profile collection.

.. meta::
    :content class=swiftype name=title data-type=string:
        POST /events/{stream-id}

==================================================
POST /events/{stream-id}
==================================================

.. endpoint-post-events-streamid-start

Use the **POST /events/{stream-id}** endpoint to send a behavioral event to a real-time profile collection.

.. endpoint-post-events-streamid-end

.. endpoint-post-events-streamid-note-start

.. note:: The request body must be a single JSON object. Arrays are not supported. The body may not exceed **64 KB**. The **Content-Length** header is required.

.. endpoint-post-events-streamid-note-end


.. _endpoint-post-events-streamid-prerequisites:

Prerequisites
==================================================

.. endpoint-post-events-streamid-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>` with the **Real-time API data access** policy.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-post-events-streamid-prerequisites-end


.. _endpoint-post-events-streamid-request-url:

Request URL
==================================================

.. endpoint-post-events-streamid-request-url-start

Direct all requests to the **POST /events/{stream-id}** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/events/{stream-id}

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/events/{stream-id}

.. endpoint-post-events-streamid-request-url-end

.. include:: base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-post-events-streamid-rate-limit:

Rate limit
==================================================

.. include:: rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

.. include:: rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _endpoint-post-events-streamid-request:

Requests
==================================================

.. endpoint-post-events-streamid-request-start

A request to the **POST /events/{stream-id}** endpoint is similar to:

.. code-block:: rest

   curl --request POST \
          'https://app.amperity.com/events/{stream-id}' \
        --header 'Amperity-Tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}' \
        --header 'Content-Type: application/json' \
        --data-binary '{"event_name": "page_view", "user_pseudo_id": "abc123"}'

This example is formatted for readability in a narrow page layout.

.. endpoint-post-events-streamid-request-end


.. _endpoint-post-events-streamid-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-post-events-streamid-request-parameters-start

The **POST /events/{stream-id}** endpoint does not define specific request body fields. The body may contain any fields relevant to the event. The following table describes path and header parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **stream-id**
     - String. Required.

       The unique identifier for the event stream. For example: **esm-2cnVk9ngm**.

   * - **Content-Length**
     - Integer. Required.

       The byte length of the request body. Requests that do not include this header will return a **411** response.

   * - **Content-Type**
     - String. Required.

       Must be ``application/json``.

.. endpoint-post-events-streamid-request-parameters-end


.. _endpoint-post-events-streamid-request-examples:

Request examples
--------------------------------------------------

.. endpoint-post-events-streamid-request-examples-start

The following examples show how to send requests to the **POST /events/{stream-id}** endpoint.

.. endpoint-post-events-streamid-request-examples-end

.. endpoint-post-events-streamid-request-examples-tabs-start

.. tabs::

   .. tab:: cURL

      The following example shows how to send a hotel room search event from a hospitality website using cURL.

      .. code-block:: rest

         curl --request POST \
                'https://app.amperity.com/events/{stream-id}' \
              --header 'Amperity-Tenant: {tenant-id}' \
              --header 'Authorization: Bearer {token}' \
              --header 'Content-Type: application/json' \
              --data-binary '{
                "event_name": "room_search",
                "event_timestamp": "2026-05-15T14:23:00.000Z",
                "property_id": "SW001",
                "property_brand": "Starwood",
                "check_in_date": "2026-08-10",
                "check_out_date": "2026-08-14",
                "nights": 4,
                "guests": 2,
                "room_type": "Suite",
                "geo_city": "London",
                "geo_country": "United Kingdom",
                "device_category": "desktop",
                "page_location": "https://acmehotels.com/search",
                "user_pseudo_id": "4a3271a9f4a22dbd.1778796153"
              }'

      This example is formatted for readability in a narrow page layout.

   .. tab:: Python

      The following example shows how to send a retail cart abandonment event using Python.

      .. code-block:: python
         :linenos:

         import requests
         from datetime import datetime, timezone

         url = "https://app.amperity.com/events/{stream-id}"

         headers = {
           "Authorization": "Bearer {token}",
           "Amperity-Tenant": "{tenant-id}",
           "Content-Type": "application/json"
         }

         payload = {
           "event_name": "cart_abandon",
           "event_timestamp": datetime.now(timezone.utc).isoformat(),
           "cart_id": "cart-20260515-abc123",
           "item_id": "SKU-98765",
           "item_name": "Trail Running Shoes Pro X",
           "item_brand": "TrailGear",
           "item_category": "Footwear",
           "item_price": 149.99,
           "item_quantity": 1,
           "cart_total": 149.99,
           "currency": "USD",
           "page_location": "https://retailstore.com/cart",
           "device_category": "mobile",
           "email": "j.henderson@example.com",
           "loyalty_id": "LYL-334455"
         }

         response = requests.post(url, headers=headers, json=payload)
         print("Status Code:", response.status_code)

   .. tab:: Node.js

      The following example shows how to send a restaurant order event from a Node.js backend service.

      .. code-block:: javascript
         :linenos:

         const https = require('https');

         const payload = JSON.stringify({
           event_name: 'order_started',
           event_timestamp: new Date().toISOString(),
           restaurant_id: 'RST-0042',
           restaurant_name: 'The Rustic Fork',
           order_type: 'delivery',
           item_name: 'Grilled Salmon',
           item_price: 24.00,
           item_quantity: 2,
           cart_total: 48.50,
           currency: 'USD',
           platform: 'app',
           geo_city: 'Chicago',
           geo_country: 'United States',
           user_id: 'USR-77889'
         });

         const options = {
           hostname: 'app.amperity.com',
           path: '/events/{stream-id}',
           method: 'POST',
           headers: {
             'Authorization': 'Bearer {token}',
             'Amperity-Tenant': '{tenant-id}',
             'Content-Type': 'application/json',
             'Content-Length': Buffer.byteLength(payload)
           }
         };

         const req = https.request(options, (res) => {
           console.log('Status:', res.statusCode);
         });

         req.on('error', (e) => console.error(e));
         req.write(payload);
         req.end();

   .. tab:: JavaScript

      The following example shows how to send a car rental search event from a browser using the Fetch API.

      .. code-block:: javascript
         :linenos:

         const payload = {
           event_name: 'vehicle_search',
           event_timestamp: new Date().toISOString(),
           pickup_location: 'LAX',
           pickup_date: '2026-07-01',
           return_date: '2026-07-07',
           vehicle_class: 'SUV',
           driver_age: 35,
           currency: 'USD',
           page_location: window.location.href,
           page_title: document.title,
           device_category: 'mobile',
           traffic_source_medium: document.referrer || '(direct)',
           geo_country: 'United States',
           user_pseudo_id: getUserCookie('amp_uid')  // browser cookie ID
         };

         fetch('https://app.amperity.com/events/{stream-id}', {
           method: 'POST',
           headers: {
             'Authorization': 'Bearer {token}',
             'Amperity-Tenant': '{tenant-id}',
             'Content-Type': 'application/json'
           },
           body: JSON.stringify(payload)
         })
         .then(res => console.log('Status:', res.status))
         .catch(err => console.error(err));

   .. tab:: PHP

      The following example shows how to send a banking session event from a PHP backend.

      .. code-block:: php
         :linenos:

         <?php

         $payload = json_encode([
           'event_name'           => 'account_dashboard_viewed',
           'event_timestamp'      => gmdate('Y-m-d\TH:i:s.000\Z'),
           'account_type'         => 'checking',
           'session_type'         => 'online_banking',
           'last_login_days_ago'  => 7,
           'product_viewed'       => 'savings_rates',
           'platform'             => 'WEB',
           'device_category'      => 'desktop',
           'geo_country'          => 'United States',
           'traffic_source'       => 'email_campaign',
           'customer_id'          => 'CUS-112233'
         ]);

         $ch = curl_init('https://app.amperity.com/events/{stream-id}');
         curl_setopt_array($ch, [
           CURLOPT_RETURNTRANSFER => true,
           CURLOPT_POST           => true,
           CURLOPT_POSTFIELDS     => $payload,
           CURLOPT_HTTPHEADER     => [
             'Authorization: Bearer {token}',
             'Amperity-Tenant: {tenant-id}',
             'Content-Type: application/json',
             'Content-Length: ' . strlen($payload)
           ]
         ]);

         $response = curl_exec($ch);
         $status   = curl_getinfo($ch, CURLINFO_HTTP_CODE);
         curl_close($ch);

         echo "Status: $status\n";

   .. tab:: Java

      The following example shows how to send a retail product view event from a Java backend service.

      .. code-block:: java
         :linenos:

         import java.net.URI;
         import java.net.http.HttpClient;
         import java.net.http.HttpRequest;
         import java.net.http.HttpResponse;
         import java.time.Instant;

         public class AmperityEventExample {
           public static void main(String[] args) throws Exception {

             String payload = String.format("""
               {
                 "event_name": "view_item",
                 "event_timestamp": "%s",
                 "item_id": "SKU-44321",
                 "item_name": "4K Smart TV 65-inch",
                 "item_brand": "VisionPlus",
                 "item_category": "Electronics",
                 "item_price": 899.99,
                 "currency": "USD",
                 "page_location": "https://retailstore.com/products/tv-65-4k",
                 "device_category": "desktop",
                 "geo_country": "United States",
                 "loyalty_id": "LYL-998877"
               }
             """, Instant.now().toString());

             HttpRequest request = HttpRequest.newBuilder()
               .uri(URI.create("https://app.amperity.com/events/{stream-id}"))
               .header("Authorization", "Bearer {token}")
               .header("Amperity-Tenant", "{tenant-id}")
               .header("Content-Type", "application/json")
               .POST(HttpRequest.BodyPublishers.ofString(payload))
               .build();

             HttpResponse<String> response = HttpClient.newHttpClient()
               .send(request, HttpResponse.BodyHandlers.ofString());

             System.out.println("Status: " + response.statusCode());
           }
         }

   .. tab:: Swift

      The following example shows how to send a hotel loyalty check-in event from an iOS app.

      .. code-block:: swift
         :linenos:

         import Foundation

         let payload: [String: Any] = [
           "event_name": "loyalty_checkin",
           "event_timestamp": ISO8601DateFormatter().string(from: Date()),
           "property_id": "SW001",
           "property_name": "Starwood Grand London",
           "reservation_id": "RES-20260515-001",
           "loyalty_tier": "Gold",
           "room_type": "Junior Suite",
           "nights": 3,
           "platform": "iOS",
           "app_version": Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "",
           "geo_country": "United Kingdom",
           "loyalty_id": "LYL-556677"
         ]

         var request = URLRequest(
           url: URL(string: "https://app.amperity.com/events/{stream-id}")!
         )
         request.httpMethod = "POST"
         request.setValue("Bearer {token}", forHTTPHeaderField: "Authorization")
         request.setValue("{tenant-id}", forHTTPHeaderField: "Amperity-Tenant")
         request.setValue("application/json", forHTTPHeaderField: "Content-Type")
         request.httpBody = try? JSONSerialization.data(withJSONObject: payload)

         URLSession.shared.dataTask(with: request) { _, response, _ in
           if let http = response as? HTTPURLResponse {
             print("Status: \(http.statusCode)")
           }
         }.resume()

.. endpoint-post-events-streamid-request-examples-tabs-end


.. _endpoint-post-events-streamid-responses:

Responses
==================================================

.. endpoint-post-events-streamid-responses-start

A response from the **POST /events/{stream-id}** endpoint will match an :doc:`HTTP status code <responses>`. A 202 response indicates the event was accepted. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-post-events-streamid-responses-end


.. _endpoint-post-events-streamid-response-202accepted:

202 Accepted
--------------------------------------------------

.. endpoint-post-events-streamid-response-202accepted-start

The **202** response indicates the event was received and queued for processing. No response body is returned.

.. endpoint-post-events-streamid-response-202accepted-end


.. _endpoint-post-events-streamid-response-204nocontent:

204 No Content
--------------------------------------------------

.. endpoint-post-events-streamid-response-204nocontent-start

The **204** response indicates the stream is configured to drop events. The event was not processed and no response body is returned.

.. endpoint-post-events-streamid-response-204nocontent-end


.. _endpoint-post-events-streamid-response-409conflict:

409 Conflict
--------------------------------------------------

.. endpoint-post-events-streamid-response-409conflict-start

The **409** response indicates the stream is not currently accepting events.

.. code-block:: json
   :linenos:

   {
     "error": "stream-rejected",
     "message": "Stream esm-abc123 is not accepting events",
     "stream": "esm-abc123"
   }

.. endpoint-post-events-streamid-response-409conflict-end
