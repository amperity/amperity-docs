.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Return a list of campaigns from your tenant. You may restrict the list of campaigns to those associated with a specific data template.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of campaigns from your tenant. You may restrict the list of campaigns to those associated with a specific data template.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /campaigns

==================================================
GET /campaign-drafts
==================================================

.. endpoint-get-campaign-drafts-list-start

Use the **GET /campaign-drafts** endpoint to return a list of draft campaigns from your tenant. You may restrict the list of draft campaigns to those associated with a specific data template.

.. endpoint-get-campaign-drafts-list-end

.. endpoint-get-campaign-drafts-list-unstable-start

.. important:: This endpoint is only available from the **unstable** version of the Amperity API.

.. endpoint-get-campaign-drafts-list-unstable-end


.. _endpoint-get-campaign-drafts-list-prerequisites:

Prerequisites
==================================================

.. endpoint-get-campaign-drafts-list-prerequisites-start

#. `Add an API key <__https://docs.amperity.com/api/authentication.html#add-api-key>`__.
#. `Generate an access token <https://docs.amperity.com/api/authentication.html#generate-access-token>`__.

.. endpoint-get-campaign-drafts-list-prerequisites-end


.. _endpoint-get-campaign-drafts-list-base-url:

Base URL
==================================================

.. endpoint-get-campaign-drafts-list-base-url-start

Direct all requests to the **GET /campaign-drafts** endpoint to the following base URL:

::

   https://{tenant}.amperity.com/api/campaign-drafts/

.. endpoint-get-campaign-drafts-list-base-url-end


.. _endpoint-get-campaign-drafts-list-rate-limit:

Rate limit
==================================================

A rate limit is the number of requests that may be made to the Amperity API in a given time period.

The Amperity API supports requests to endpoints that do not exceed a rate of 10 requests per second. Response times will vary by endpoint and the complexity of data that is returned by the response. Some requests may take seconds to return.

Requests to the Amperity API that exceed 10 requests per second may return an error response with an HTTP 429 status code.


.. _endpoint-get-campaign-drafts-list-request:

Requests
==================================================

.. endpoint-get-campaign-drafts-list-request-start

A request to the **GET /campaign-drafts** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/campaign-drafts \
          ?limit=12 \
          ?with_total=true \
          ?destination_data_template_id=ptg-1abcAB4C2' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: unstable' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-campaign-drafts-list-request-end


.. _endpoint-get-campaign-drafts-list-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-campaign-drafts-list-request-parameters-start

The following table describes the parameters that may be used with the **GET /campaign-drafts** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **api_version**
     - String. Optional.

       A `supported version of the Amperity API <https://docs.amperity.com/api/versioning.html#supported-versions>`. For example: **unstable**.

       .. note:: You may use the **api-version** request header instead of the **api_version** request parameter.


   * - **destination_data_template_id**
     - String. Optional.

       Use this parameter to restrict the list of campaigns that are returned to only campaigns that are configured to use a specific data template.

       .. tip:: You can find the ID for the data template from the Amperity user interface.

          From the **Destinations** page, open the menu in the same row as the data template for which the ID is to be copied, and then select **Copy ID**.


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

.. endpoint-get-campaign-drafts-list-request-parameters-end


.. _endpoint-get-campaign-drafts-list-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-campaign-drafts-list-request-examples-start

The following examples show how to send requests to the **GET /campaign-drafts** endpoint.

.. endpoint-get-campaign-drafts-list-request-examples-end

.. endpoint-get-campaign-drafts-list-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /campaign-drafts** endpoint.

      .. code-block:: rest

         curl --request GET \
                'https://tenant.amperity.com/api/campaign-drafts \
                ?limit=12 \
                &with_total=true \
                &destination_data_template_id=ptg-1abcAB4C2' \
              --header 'amperity-tenant: {tenant}' \
              --header 'api-version: unstable' \
              --header 'Authorization: Bearer {token}'

      This example is formatted for readability in a narrow page layout.

   .. tab-item:: Python

      The following example shows how to use Python to send a request to the **GET /campaign-drafts** endpoint. This example converts the JSON response into a CSV file named "campaigns.csv".

      .. code-block:: python
         :linenos:

         import requests
         import json
         import csv

         # URL for Draft campaigns endpoint
         url = "https://tenant-name.amperity.com/api/campaign-drafts"

         # Required headers
         headers = {
           'accept': 'application/json',
           'authorization': 'Bearer {token}', # add token here
           'amperity-tenant': '{tenant}',
           'api-version': 'version'
         }

         # Query parameter for data template IDs
         payload = {
           # 'destination_data_template_id': ''
         }

         # Get the response from the Draft campaigns endpoint
         response = requests.request("GET", url, headers=headers, params=payload)
         response_json = response.json()

         # Extract headers from the first data entry
         headers = list(response_json["data"][0].keys())

         # Specify the output CSV file path
         csv_file_path = "campaigns.csv"

         # Write data to a CSV file
         with open(csv_file_path, mode='w', newline='') as file:
           writer = csv.DictWriter(file, fieldnames=headers)
           writer.writeheader()
           for entry in response_json["data"]:
             writer.writerow(entry)

         print("CSV file generated successfully.")

.. endpoint-get-campaign-drafts-list-request-examples-tabs-end


.. _endpoint-get-campaign-drafts-list-unstable-responses:

Responses
==================================================

.. endpoint-get-campaign-drafts-list-unstable-responses-start

A response from the **GET /campaign-drafts** endpoint will match an `HTTP status code <https://docs.amperity.com/api/responses.html>`__. A 200 response contains the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-campaign-drafts-list-unstable-responses-end


.. _endpoint-get-campaign-drafts-list-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-campaign-drafts-list-response-200ok-start

The **200** response returns a set of draft campaigns.

.. code-block:: json
   :linenos:

   {
     "total": 0,
     "next_token": "ABCa1bcdDEe2f3G",
     "data": [
       {
         "id": "ab-1CDEfGHI",
         "name": "Holiday Campaign",
         "deliver_at": "2024-04-22T20:30:00Z"
       },
       {
         "id": "cd-2FGHiJKL",
         "name": "Returning Customers",
         "deliver_at": "2024-04-23T21:00:00Z"
       }
     ]
   }

.. endpoint-get-campaign-drafts-list-response-200ok-end


.. _endpoint-get-campaign-drafts-list-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-campaign-drafts-list-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of values for the current page of results. The array of values includes the following properties:

       **deliver_at**
          The date and time at which the campaign was delivered or will be delivered. Dates and times are in |ext_iso_8601| format and in UTC.

       **id**
          The Amperity internal identifier for the campaign.

       **name**
          The name of the campaign.

   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.

   * - **total**
     - The total count of all results. This property is only returned when **with_total** is set to **true** in a request.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. endpoint-get-campaign-drafts-list-response-parameters-end
