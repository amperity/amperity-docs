.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Return records for all user activity that occured in your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return records for all user activity that occured in your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /audit-events


==================================================
GET /audit-events
==================================================

.. users-about-activity-start

Amperity maintains :ref:`records of all user activity that occured in your tenant <endpoint-get-audit-events-list-common-event-types>`. For example:

* A user makes a configuration change to the Amperity platform
* A user creates a sandbox
* A user views personally identifiable information (PII)
* A workflow was stopped by a user
* A user configured a destination
* A user created an API key
* A user was assigned to a resource group

.. users-about-activity-end

.. endpoint-get-audit-events-list-start

Use the **/audit-events** endpoint to return a log of user activity that occurred with your tenant. Each response may contain up to 1000 audit events.

.. note:: When requesting events for a production tenant, audit events for sandboxes are included in the response. When requesting events from a sandbox, only events from that sandbox are included in the response.

.. endpoint-get-audit-events-list-end


.. _endpoint-get-audit-events-list-http-methods:

Available HTTP methods
==================================================

.. image:: ../../images/api-request-get-audit-events.png
   :width: 440 px
   :alt: GET /audit-events
   :align: left
   :class: no-scaled-link


.. _endpoint-get-audit-events-list-prerequisites:

Prerequisites
==================================================

.. endpoint-get-audit-events-list-prerequisites-start

Each request to an endpoint in the Amperity API must be authenticated.

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-audit-events-list-prerequisites-end


.. _endpoint-get-audit-events-list-base-url:

Base URL
==================================================

.. endpoint-get-audit-events-list-base-url-start

All requests made to the **/audit-events** endpoint should be directed to the following base URL:

::

   https://{tenant-id}.amperity.com/api/audit-events/

.. endpoint-get-audit-events-list-base-url-end


.. _endpoint-get-audit-events-list-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-audit-events-list-request-body:

Requests
==================================================

.. endpoint-get-audit-events-list-request-body-start

A request to the **/audit-events** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/audit-events \
          ?limit=10 \
          ?with_total=true \
          ?happened_from=2024-04-01 \
          ?happened_tod=2024-04-10' \
        --header 'amperity-tenant: tenant' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer token'

(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-audit-events-list-request-body-end


.. _endpoint-get-audit-events-list-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-audit-events-list-request-parameters-start

The following table describes the parameters that may be used with the **/audit-events** endpoint.

.. endpoint-get-audit-events-list-request-parameters-end

.. include:: /endpoint_parameters/audit_events_request.txt


.. _endpoint-get-audit-events-list-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-audit-events-list-request-examples-start

The following examples show how to send requests to the **/audit-events** endpoint.

.. endpoint-get-audit-events-list-request-examples-end


.. _endpoint-get-audit-events-list-request-curl:

cURL
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-audit-events-list-request-curl-start

The following example shows how to use cURL to send a request to the **/audit-events** endpoint.

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/audit-events \
          ?limit=10 \
          &with_total=true \
          &happened_from=2024-04-01 \
          &happened_to=2024-04-10' \
        --header 'amperity-tenant: tenant' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer token'

(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-audit-events-list-request-curl-end


.. _endpoint-get-audit-events-list-request-python:

Python
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-audit-events-list-request-python-start

The following example shows how to use Python to send a request to the **/audit-events** endpoint. This example converts the JSON response into a CSV file named "audit_events.csv".

.. code-block:: python

   import requests
   import json
   import csv

   # URL for Audit Events endpoint
   url = "https://tenant-name.amperity.com/api/audit-events"

   # Required headers
   headers = {
     'accept': 'application/json',
     'authorization': 'Bearer token', # add token here
     'amperity-tenant': 'tenant-name'
   }

   # Query parameters for time ranges
   payload = {
     # 'happened_from': '',
     # 'happened_to': ''
   }

   # Get the response from the endpoint
   response = requests.request("GET", url, headers=headers, params=payload)
   response_json = response.json()

   # Extract headers from the first data entry
   headers = list(response_json["data"][0].keys())

   # Specify the output CSV file path
   csv_file_path = "audit_events.csv"

   # Write data to a CSV file
   with open(csv_file_path, mode='w', newline='') as file:
     writer = csv.DictWriter(file, fieldnames=headers)
     writer.writeheader()
     for entry in response_json["data"]:
       writer.writerow(entry)

   print("CSV file generated successfully.")

.. endpoint-get-audit-events-list-request-python-end


.. _endpoint-get-audit-events-list-responses:

Responses
==================================================

.. endpoint-get-audit-events-list-responses-start

A response from the **/audit-events** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response will contain the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-audit-events-list-responses-end


.. _endpoint-get-audit-events-list-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-audit-events-list-response-200ok-start

A successful request made to the **/audit-events** endpoint will return a response with up to 1000 audit events, similar to:

.. code-block:: json

   {
     "data": [
       {
         "tenant": "socktown",
         "principal_name": "Socktown User",
         "object_id": "aud-20240409-55140-aBCDEFg1hiK",
         "happened_from": "2024-04-09T15:19:00.636Z",
         "tenant_family": "family",
         "principal_email": "user@socktown.com",
         "principal_id": "google-apps|user@socktown.com",
         "origin_ip": "111.11.111.1",
         "event_id": "ae-Ab1cDeFgHijkLMN2Op3QrS",
         "event_type": "amperity.alert.audience/created"
       }
     ],
     "total": 102,
     "next_token": "PAGE_TOKEN"
   }

.. endpoint-get-audit-events-list-response-200ok-end


.. _endpoint-get-audit-events-list-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-audit-events-list-response-parameters-start

A **200 OK** response contains the following parameters.

.. endpoint-get-audit-events-list-response-parameters-end

.. include:: /endpoint_parameters/audit_events_response.txt


.. _endpoint-get-audit-events-list-common-event-types:

Common event types
==================================================

.. include:: ../../amperity_reference/source/settings.rst
   :start-after: .. settings-user-activity-logs-event-types-start
   :end-before: .. settings-user-activity-logs-event-types-end
