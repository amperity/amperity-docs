.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Send an event to a profile store event stream.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send an event to a profile store event stream.

.. meta::
    :content class=swiftype name=title data-type=string:
        POST /events/{stream-id}

==================================================
POST /events/{stream-id}
==================================================

.. endpoint-post-profile-store-events-start

Use the **POST /events/{stream-id}** endpoint to send a real-time event to an event stream. Events are the primary way to update profiles in a profile store in real time.

.. endpoint-post-profile-store-events-end

.. note:: This endpoint is part of the Real-time Events API, an unstable API that may change without advance notice of breaking changes.

.. note:: In the Amperity user interface an event stream is shown on the **Events** > **Event streams** page. The value for **{stream-id}** is shown as the **Endpoint ID** for that event stream.


.. _endpoint-post-profile-store-events-prerequisites:

Prerequisites
==================================================

.. endpoint-post-profile-store-events-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.
#. An event stream must be configured for your tenant. To set up a profile store and its event streams, contact your Amperity representative.

.. endpoint-post-profile-store-events-prerequisites-end

.. note:: The access token must be granted the **profile-events:write** (or **streaming-ingest-api:write**) permission.


.. _endpoint-post-profile-store-events-request-url:

Request URL
==================================================

.. endpoint-post-profile-store-events-request-url-start

Direct all requests to the **POST /events/{stream-id}** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/events/{stream-id}

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/events/{stream-id}

.. endpoint-post-profile-store-events-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-post-profile-store-events-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-post-profile-store-events-request:

Requests
==================================================

.. endpoint-post-profile-store-events-request-start

A request to the **POST /events/{stream-id}** endpoint sends a single JSON event object to the stream. The request body must be a JSON object and must not exceed 64 KB. A **Content-Length** header is required.

.. code-block:: rest

   curl --request POST \
          'https://app.amperity.com/prof/events/{stream-id}' \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}' \
        --header 'Content-Type: application/json' \
        --data '{ "email": "customer@example.com", "event_type": "purchase", "order_total": 42.00 }'

This example is formatted for readability in a narrow page layout.

.. endpoint-post-profile-store-events-request-end


.. _endpoint-post-profile-store-events-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-post-profile-store-events-request-parameters-start

The following table describes the parameters that may be used with the **POST /events/{stream-id}** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **stream-id**
     - String. Required.

       The ID of the event stream to which the event is sent. This value is shown as the **Endpoint ID** for an event stream in the Amperity user interface.

   * - **request body**
     - JSON object. Required.

       The event payload, sent as a single JSON object. The shape of the payload depends on how the event stream is configured. The payload must not exceed 64 KB.

.. endpoint-post-profile-store-events-request-parameters-end


.. _endpoint-post-profile-store-events-responses:

Responses
==================================================

.. endpoint-post-profile-store-events-responses-start

A response from the **POST /events/{stream-id}** endpoint will match an :doc:`HTTP status code <responses>`.

.. endpoint-post-profile-store-events-responses-end

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Status
     - Description

   * - **202**
     - The event was accepted and published to the stream.

   * - **204**
     - The event was accepted, but the stream is configured to drop events. No event was published.

   * - **400**
     - The request body is missing, malformed, or is not a JSON object.

   * - **404**
     - No event stream with the given **{stream-id}** exists for the tenant.

   * - **409**
     - The event stream is not currently accepting events.

   * - **411**
     - The **Content-Length** header is missing.

   * - **413**
     - The request body exceeds the 64 KB limit.

   * - **415**
     - The request **Content-Type** is not **application/json**.

   * - **503**
     - The event could not be published because of a temporary downstream error. Retry the request.
