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

.. include:: ../../amperity_reference/source/activity_logs.rst
   :start-after: .. settings-user-activity-logs-about-start
   :end-before: .. settings-user-activity-logs-about-end

.. endpoint-get-audit-events-list-start

Use the **GET /audit-events** endpoint to return a log of user activity that occurred with your tenant. Each response may contain up to 1000 audit events.

.. note:: When requesting events for a production tenant, audit events for sandboxes are included in the response. When requesting events from a sandbox, only events from that sandbox are included in the response.

.. endpoint-get-audit-events-list-end


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

Direct all requests to the **GET /audit-events** endpoint to the following base URL:

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

A request to the **GET /audit-events** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/audit-events \
          ?limit=10 \
          ?with_total=true \
          ?happened_from=2024-04-01 \
          ?happened_tod=2024-04-10' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-audit-events-list-request-body-end


.. _endpoint-get-audit-events-list-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-audit-events-list-request-parameters-start

The following table describes the parameters that may be used with the **GET /audit-events** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **api_version**
     - String. Optional.

       A :ref:`supported version of the Amperity API <versioning-supported-versions>`. For example: **2024-04-01**.

       .. note:: You may use the **api-version** request header instead of the **api-version** request parameter.


   * - **happened_end**
     - String. Optional.

       The end date (exclusive) that defines the end of the time range for which audit events are returned. For example: "2024-03-01T11:11:11Z".

       The values for the end date must be a string, should be in |ext_iso_8601| format, and should be in UTC.


   * - **happened_start**
     - String. Optional.

       The start date (inclusive) that defines the beginning of the time range for which audit events are returned. For example: "2024-04-01T11:11:11Z".

       The start date must be a string, should be in |ext_iso_8601| format, and should be in UTC.


   * - **limit**
     - Integer. Optional.

       The maximum number of records to include in a single page of results.


   * - **next_token**
     - String. Optional.

       An opaque token that is used to paginate results. Omit the **next_token** property to return the first page. Use the cursor value for **next_token** that was returned in a response to view the next page of results.

       For example: **ABCd1fghIJk2l3M**

       .. note:: The possible values for **next_token** are returned within the **200** response.

       .. important:: The value for **next_token** cannot be **NULL**.


   * - **with_total**
     - Boolean. Optional.

       Set this value to **true** to include a total count of all results. Default value: **false**.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. endpoint-get-audit-events-list-request-parameters-end


.. _endpoint-get-audit-events-list-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-audit-events-list-request-examples-start

The following examples show how to send requests to the **GET /audit-events** endpoint.

.. endpoint-get-audit-events-list-request-examples-end

.. endpoint-get-audit-events-list-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /audit-events** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://tenant.amperity.com/api/audit-events \
                ?limit=10 \
                &with_total=true \
                &happened_from=2024-04-01 \
                &happened_to=2024-04-10' \
              --header 'amperity-tenant: {tenant}' \
              --header 'api-version: 2024-04-01' \
              --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

   .. tab-item:: Python

      The following example shows how to use Python to send a request to the **GET /audit-events** endpoint. This example converts the JSON response into a CSV file named "audit_events.csv".

      .. code-block:: python
         :linenos:

         import requests
         import json
         import csv

         # URL for Audit Events endpoint
         url = "https://tenant-name.amperity.com/api/audit-events"

         # Required headers
         headers = {
           'accept': 'application/json',
           'authorization': 'Bearer {token}', # add token here
           'amperity-tenant': '{tenant}'
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

.. endpoint-get-audit-events-list-request-examples-tabs-end


.. _endpoint-get-audit-events-list-responses:

Responses
==================================================

.. endpoint-get-audit-events-list-responses-start

A response from the **GET /audit-events** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-audit-events-list-responses-end


.. _endpoint-get-audit-events-list-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-audit-events-list-response-200ok-start

A successful request made to the **GET /audit-events** endpoint will return a response with up to 1000 audit events, similar to:

.. code-block:: json
   :linenos:

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

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of values for the current page of results. The array of values includes the following properties:

       **event_id**
          The Amperity internal identifier for the event.

       **event_type**
          The :ref:`type of event <endpoint-get-audit-events-list-common-event-types>`.

       **happened_at**
          The date and time at which the action occurred. Dates and times are in |ext_iso_8601| format and in UTC.

       **principal_email**
          The email address for the user who initiated the action.

       **principal_id**
          The authentication identifier for the user who initiated the action. This user may be an API key or a non-human user.

       **principal_name**
          The friendly name of the user associated with the activity, if available, otherwise the email address or API key.

       **object_id**
          The identifier for the object against which the action occurred.

       **object_name**
          Optional. A composed string that describes the objects for which the action occurred.

       **origin_ip**
          The IP address that is associated with the user who initiated the action.

       **tenant_family**
          The name of the tenant family that is associated with the action. When **tenant** is a sandbox, **tenant_family** is the tenant ID of the production tenant.

       **tenant**
          The tenant ID of the tenant associated with the action. This ID may be for a sandbox.

   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.

   * - **total**
     - The total count of all results. This property is only returned when **with_total** is set to **true** in a request.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. endpoint-get-audit-events-list-response-parameters-end


.. _endpoint-get-audit-events-list-common-event-types:

Common event types
==================================================

.. include:: ../../amperity_reference/source/activity_logs.rst
   :start-after: .. settings-user-activity-logs-event-types-start
   :end-before: .. settings-user-activity-logs-event-types-end
