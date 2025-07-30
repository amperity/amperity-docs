.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
         Return a list of customer profiles from your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
         Return a list of customer profiles from your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /indexes/{id}/profiles

==================================================
GET /indexes/{id}/profiles
==================================================

.. endpoint-get-profiles-list-start

Use the **GET /indexes/{id}/profiles** endpoint to return a paginated list of customer profiles.

.. endpoint-get-profiles-list-end


.. _endpoint-get-profiles-list-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profiles-list-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.

.. endpoint-get-profiles-list-prerequisites-end


.. _endpoint-get-profiles-list-base-url:

Base URL
==================================================

.. endpoint-get-profiles-list-base-url-start

Direct all requests to the **GET /indexes/{id}/profiles** endpoint to the following base URL:

::

   https://{tenant-id}.amperity.com/api/indexes/

.. endpoint-get-profiles-list-base-url-end


.. _endpoint-get-profiles-list-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profiles-list-request:

Requests
==================================================

.. endpoint-get-profiles-list-request-start

A request to the **GET /indexes/{id}/profiles** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://tenant.amperity.com/api/indexes/{id}/profiles \
          ?limit=100 \
          &with_total=true' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2025-07-31' \
        --header 'Authorization: Bearer {token}'

(This example is formatted for readability in a narrow page layout.)

.. endpoint-get-profiles-list-request-end


.. _endpoint-get-profiles-list-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profiles-list-request-parameters-start

The following table describes the parameters that may be used with the **GET /indexes/{id}/profiles** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **api_version**
     - String. Optional.

       A :ref:`supported version of the Amperity API <versioning-supported-versions>`. For example: **2025-07-31**.

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

.. endpoint-get-profiles-list-request-parameters-end


.. _endpoint-get-profiles-list-request-examples:

Request examples
--------------------------------------------------

.. endpoint-get-profiles-list-request-examples-start

The following examples show how to send requests to the **GET /indexes/{id}/profiles** endpoint.

.. endpoint-get-profiles-list-request-examples-end


.. endpoint-get-profiles-list-request-examples-tabs-start

.. tab-set::

   .. tab-item:: cURL

      The following example shows how to use cURL to send a request to the **GET /indexes/{id}/profiles** endpoint.

      .. code-block:: bash

         curl --request GET \
                'https://tenant.amperity.com/api/indexes/{id}/profiles \
                ?limit=100 \
                &with_total=true' \
                --header 'amperity-tenant: {tenant}' \
                --header 'api-version: 2025-07-31' \
                --header 'Authorization: Bearer {token}'

      (This example is formatted for readability in a narrow page layout.)

   .. tab-item:: Python

      The following example shows how to use Python to send a request to the **GET /indexes/{id}/profiles** endpoint. This example converts the JSON response into a CSV file named "profiles.csv".

      .. code-block:: python
         :linenos:

         import requests
         import json
         import csv

         # URL for Campaigns endpoint
         url = "https://tenant-name.amperity.com/api/indexes/{id}/profiles"

         # Required headers
         headers = {
           'accept': 'application/json',
           'authorization': 'Bearer {token}', # add token here
           'amperity-tenant': '{tenant}',
           'api-version': '{version}'
         }

         # Get the response from the Profiles endpoint
         response = requests.request("GET", url, headers=headers, params=payload)
         response_json = response.json()

         # Extract headers from the first data entry
         headers = list(response_json["data"][0].keys())

         # Specify the output CSV file path
         csv_file_path = "profiles.csv"

         # Write data to a CSV file
         with open(csv_file_path, mode='w', newline='') as file:
           writer = csv.DictWriter(file, fieldnames=headers)
           writer.writeheader()
           for entry in response_json["data"]:
             writer.writerow(entry)

         print("CSV file generated successfully.")

.. endpoint-get-profiles-list-request-examples-tabs-end


.. _endpoint-get-profiles-list-responses:

Responses
==================================================

.. endpoint-get-profiles-list-responses-start

A response from the **GET /indexes/{id}/profiles** endpoint will match an :doc:`HTTP status code <responses>`. A 200 response will contain the results set. A 4xx response indicates an issue with the configuration of your request. A 5xx response indicates that the endpoint is unavailable.

.. endpoint-get-profiles-list-responses-end


.. _endpoint-get-profiles-list-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profiles-list-response-200ok-start

The **200** response returns a set of customer profile indexes.

.. code-block:: json
   :linenos:

   {
     "total": 0,
     "next_token": "ABCa1bcdDEe2f3G",
     "data": [
       {
         "id": "cl-abc123",
         "name": "Loyalty Members",
         "created_at": "2025-04-25T20:30:00Z"
         "updated_at": "2025-07-26T20:30:00Z"
       },
       {
         "id": "cl-def456",
         "name": "Online Shoppers",
         "created_at": "2025-04-25T20:30:00Z"
         "updated_at": "2025-07-26T20:30:00Z"
       },
     ]
   }

.. endpoint-get-profiles-list-response-200ok-end


.. _endpoint-get-profiles-list-response-parameters:

Response parameters
--------------------------------------------------

.. endpoint-get-profiles-list-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of values for the current page of results. The array of values includes the following properties:

       **created_at**
          The date and time on which the profile index was created. The date and time must be in `RFC3339 format <https://www.rfc-editor.org/rfc/rfc3339>`__ |ext_link|.

       **id**
          The Amperity internal identifier for the campaign.

         "id": "cl-def456",
         "name": "Online Shoppers",
         "created_at": "2025-04-25T20:30:00Z"
         "updated_at": "2025-07-26T20:30:00Z"

       **name**
          The name of the campaign.

   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.

   * - **updated_at**
     -    The date and time on which the profile index was updated. The date and time must be in `RFC3339 format <https://www.rfc-editor.org/rfc/rfc3339>`__ |ext_link|.

.. endpoint-get-profiles-list-response-parameters-end
