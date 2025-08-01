.. https://docs.amperity.com/api/

:canonical: https://docs.amperity.com/api/endpoint_get_segments_list.html


.. meta::
    :description lang=en:
         Return a list of segments from your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of segments from your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /segments

==================================================
GET /segments
==================================================

.. endpoint-get-segments-list-start

Use the **GET /segments** endpoint to return a list of segments from your tenant.

.. endpoint-get-segments-list-end


.. _endpoint-get-segments-list-prerequisites:

Prerequisites
==================================================

.. endpoint-get-segments-list-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-segments-list-prerequisites-end


.. _endpoint-get-segments-list-base-url:

Base URL
==================================================

.. endpoint-get-segments-list-base-url-start

Direct all requests to the **GET /segments** endpoint to the following base URL:

::

   https://{tenant-id}.amperity.com/api/segments/

.. endpoint-get-segments-list-base-url-end


.. _endpoint-get-segments-list-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-segments-list-request:

Requests
==================================================

.. endpoint-get-segments-list-request-start

A request to the **GET /segments** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/segments \
          ?limit=12 \
          ?with_total=true' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer {token}'

(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-segments-list-request-end


.. _endpoint-get-segments-list-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-segments-list-request-parameters-start

The following table describes the parameters that may be used with the **GET /segments** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **api_version**
     - String. Optional.

       A :ref:`supported version of the Amperity API <versioning-supported-versions>`. For example: **2024-04-01**.

       .. note:: You may use the **api-version** request header instead of the **api_version** request parameter.


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

.. endpoint-get-segments-list-request-parameters-end


.. _endpoint-get-segments-list-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-segments-list-request-examples-start

The following examples show how to send requests to the **GET /segments** endpoint.

.. endpoint-get-segments-list-request-examples-end


.. endpoint-get-segments-list-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /segments** endpoint.

      .. code-block:: bash

         curl --request GET \
                'https://tenant.amperity.com/api/segments \
                ?limit=12 \
                &with_total=true' \
              --header 'amperity-tenant: {tenant}' \
              --header 'api-version: 2024-04-01' \
              --header 'Authorization: Bearer {token}'

      (This example is formatted for readability in a narrow page layout.)

   .. tab-item:: Python

      The following example shows how to use Python to send a request to the **GET /segments** endpoint. This example converts the JSON response into a CSV file named "segments.csv".

      .. code-block:: python
         :linenos:

         import requests
         import json
         import csv

         # URL for Segments endpoint
         url = "https://tenant-name.amperity.com/api/segments"

         # Required headers
         headers = {
           'accept': 'application/json',
           'authorization': 'Bearer {token}', # add token here
           'amperity-tenant': '{tenant}',
           'api-version': 'version'
         }

         # Get the response from the Segments endpoint
         response = requests.request("GET", url, headers=headers, params=payload)
         response_json = response.json()

         # Extract headers from the first data entry
         headers = list(response_json["data"][0].keys())

         # Specify the output CSV file path
         csv_file_path = "segments.csv"

         # Write data to a CSV file
         with open(csv_file_path, mode='w', newline='') as file:
           writer = csv.DictWriter(file, fieldnames=headers)
           writer.writeheader()
           for entry in response_json["data"]:
             writer.writerow(entry)

         print("CSV file generated successfully.")

.. endpoint-get-segments-list-request-examples-tabs-end


.. _endpoint-get-segments-list-responses:

Responses
==================================================

.. endpoint-get-segments-list-responses-start

A response from the **GET /segments** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response will contain the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-segments-list-responses-end


.. _endpoint-get-segments-list-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-segments-list-response-200ok-start

The **200** response returns a set of segments.

.. code-block:: json
   :linenos:

   {
     "total": 0,
     "next_token": "ABCa1bcdDEe2f3G",
     "data": [
       {
         "id": "ab-1CDEfGHI",
         "name": "Holiday Segment"
       },
       {
         "id": "cd-2FGHiJKL",
         "name": "Returning Customers"
       }
     ]
   }

.. endpoint-get-segments-list-response-200ok-end


.. _endpoint-get-segments-list-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-segments-list-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of values for the current page of results. The array of values includes the following properties:

       **id**
          The Amperity internal identifier for the segment.

       **name**
          The name of the segment.

   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.

   * - **total**
     - The total count of all results. This property is only returned when **with_total** is set to **true** in a request.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. endpoint-get-segments-list-response-parameters-end
