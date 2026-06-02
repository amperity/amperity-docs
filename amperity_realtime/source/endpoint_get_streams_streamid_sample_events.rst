.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
         Return a sample of recent events from an event stream.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return a sample of recent events from an event stream.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /streams/{stream-id}/sample-events

==================================================
GET /streams/{stream-id}/sample-events
==================================================

.. endpoint-get-streams-streamid-sample-events-start

Use the **GET /streams/{stream-id}/sample-events** endpoint to return a sample of recent events received by the stream. Returns up to **50** of the most recently received events.

.. endpoint-get-streams-streamid-sample-events-end


.. _endpoint-get-streams-streamid-sample-events-prerequisites:

Prerequisites
==================================================

.. endpoint-get-streams-streamid-sample-events-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>` with the **Real-time API data access** policy.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-streams-streamid-sample-events-prerequisites-end


.. _endpoint-get-streams-streamid-sample-events-request-url:

Request URL
==================================================

.. endpoint-get-streams-streamid-sample-events-request-url-start

Direct all requests to the **GET /streams/{stream-id}/sample-events** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/streams/{stream-id}/sample-events

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/streams/{stream-id}/sample-events

.. endpoint-get-streams-streamid-sample-events-request-url-end

.. include:: base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-streams-streamid-sample-events-rate-limit:

Rate limit
==================================================

.. include:: rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

.. include:: rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _endpoint-get-streams-streamid-sample-events-request:

Requests
==================================================

.. endpoint-get-streams-streamid-sample-events-request-start

A request to the **GET /streams/{stream-id}/sample-events** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/streams/{stream-id}/sample-events \
          ?type=page_view' \
        --header 'Amperity-Tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-streams-streamid-sample-events-request-end


.. _endpoint-get-streams-streamid-sample-events-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-streams-streamid-sample-events-request-parameters-start

The following table describes the parameters that may be used with the **GET /streams/{stream-id}/sample-events** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **state**
     - String. Optional.

       Filter results to events in a specific processing state. For example: **processed**.

   * - **type**
     - String. Optional.

       Filter results to events with the specified event type. For example: **page_view** or **purchase**.

.. endpoint-get-streams-streamid-sample-events-request-parameters-end


.. _endpoint-get-streams-streamid-sample-events-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-streams-streamid-sample-events-request-examples-start

The following examples show how to send requests to the **GET /streams/{stream-id}/sample-events** endpoint.

.. endpoint-get-streams-streamid-sample-events-request-examples-end

.. endpoint-get-streams-streamid-sample-events-request-examples-tabs-start

.. tabs::

   .. tab:: cURL

      The following example shows how to use cURL to send a request to the **GET /streams/{stream-id}/sample-events** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://app.amperity.com/streams/{stream-id}/sample-events \
                ?type=page_view' \
              --header 'Amperity-Tenant: {tenant-id}' \
              --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

   .. tab:: Python

      The following example shows how to use Python to send a request to the **GET /streams/{stream-id}/sample-events** endpoint.

      .. code-block:: python
         :linenos:

         import requests

         url = "https://app.amperity.com/streams/{stream-id}/sample-events"

         headers = {
           "Authorization": "Bearer {token}",
           "Amperity-Tenant": "{tenant-id}"
         }

         params = {
           "type": "page_view"
         }

         response = requests.get(url, headers=headers, params=params)
         print("Status Code:", response.status_code)
         print("Response:", response.json())

.. endpoint-get-streams-streamid-sample-events-request-examples-tabs-end


.. _endpoint-get-streams-streamid-sample-events-responses:

Responses
==================================================

.. endpoint-get-streams-streamid-sample-events-responses-start

A response from the **GET /streams/{stream-id}/sample-events** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-streams-streamid-sample-events-responses-end


.. _endpoint-get-streams-streamid-sample-events-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-streams-streamid-sample-events-response-200ok-start

The **200** response returns a list of recent events from the stream, similar to:

.. code-block:: json
   :linenos:

   [
     {
       "event_name": "page_view",
       "event_timestamp": "2026-05-14T23:42:38.510Z",
       "page_title": "Acme Hotels - Luxury Hotels & Resorts",
       "page_location": "https://acmehotels.com/promotions/",
       "user_pseudo_id": "4a3271a9f4a22dbd.1778796153",
       "geo_country": "United States",
       "device_category": "desktop"
     }
   ]

The fields returned in each event object reflect the fields that were included when the event was submitted.

.. endpoint-get-streams-streamid-sample-events-response-200ok-end
