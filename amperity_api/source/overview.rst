.. 
.. https://docs.amperity.com/api/
..

.. meta::
    :description lang=en:
        An overview of the Amperity API.

.. meta::
    :content class=swiftype name=body data-type=text:
        An overview of the Amperity API.

.. meta::
    :content class=swiftype name=title data-type=string:
        About the Amperity API


==================================================
About the Amperity API
==================================================

.. api-amperity-start

The Amperity API enables programmatic access to your Amperity tenant through a collection of RESTful endpoints that support API-first use cases for integrations, applications, and custom workflows. Use Amperity API endpoints to streamline workflows, enhance marketing strategies, and unlock the value of your brand's customer data.

.. api-amperity-end

.. api-amperity-openapi-and-postman-start

.. admonition:: OpenAPI and Postman

   Amperity provides an `OpenAPI specification <https://docs.amperity.com/openapi.html>`__ for the Amperity API. Download the OpenAPI specification, and then import it into an API tool, such as Postman, to start interacting with Amperity API endpoints.

.. api-amperity-openapi-and-postman-end


.. start-here-endpoints-start

.. include:: ../../shared/api_amperity.rst
   :start-after: .. term-http-methods-start
   :end-before: .. term-http-methods-end

.. start-here-endpoints-end


.. _api-amperity-auth:

Authentication
==================================================

.. api-amperity-auth-start

All requests that are made to Amperity API endpoints :doc:`must be authenticated by access tokens that are signed by Amperity-managed API keys <authentication>`.

Amperity :ref:`API keys <authentication-api-keys>` are synthetic identities that are bound to your tenant and enable programmatic access to Amperity.

:ref:`Access tokens <authentication-access-tokens>` are signed by Amperity-managed API keys and are authorized to perform certain actions with Amperity.

.. api-amperity-auth-end


.. _api-amperity-base-url:

Base URL
==================================================

.. api-amperity-base-url-start

All requests made to Amperity API endpoints should be directed to the following base URL:

::

   https://{tenant-id}.amperity.com/api


You can find the tenant ID from the Amperity user interface. From the **Users and Activity** page, select the **Actions** menu for an API key, and then click **Copy tenant ID**.

For example, if the tenant ID is **acme** the base URL would be

::

   https://acme.amperity.com/api

.. api-amperity-base-url-end


.. _api-amperity-request-format:

Requests
==================================================

.. api-amperity-request-format-start

Requests made to Amperity API endpoints require the following headers:

* **Authorization** Required. The bearer authentication header. This should be the access token for your tenant's API key.
* **Amperity-Tenant** Required. The ID for the tenant to which the request will be sent. You can find the tenant ID in the base URL for your tenant.
* **api-version** Required. A supported version of the Amperity API. For example: **2024-04-01**.

In addition to all required headers, you must specify the HTTP method, and base URL. For example:

::

   curl -request GET \
        -url "https://{tenant-id}.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {tenant-id}" \
        -H "api-version: {version}"

Most endpoints provide a set of endpoint-specific properties that may be included within the URL header.

.. api-amperity-request-format-end


.. _api-amperity-response-format:

Responses
==================================================

.. api-amperity-response-format-start

The Amperity API responds in JSON format. Each response includes relevant HTTP status codes that indicate the success or failure of the request. The individual properties in a response will vary by endpoint; all endpoints that support the GET HTTP method will return lists using pagination.

.. api-amperity-response-format-end


.. _api-amperity-pagination:

Pagination
==================================================

.. api-amperity-pagination-start

Amperity uses cursor-based pagination to return pages of data for large lists.

.. tip:: A cursor acts like a pointer; it refers to a particular point in the data and marks the boundary between pages. A paginated endpoint returns responses with a list of results *and* a **next_token** parameter when another page is available in the returned dataset.

   You have reached the last page in the results set when the **next_token** parameter is not returned.

.. api-amperity-pagination-end


.. _api-amperity-pagination-properties-request:

Pagination requests
--------------------------------------------------

.. api-amperity-pagination-properties-request-start

All endpoints that support the **GET** HTTP method use the following properties to support pagination. Use these properties to iterate through a results set.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **limit**
     - The maximum number of records to include in a single page of results.

   * - **next_token**
     - An opaque token that is used to paginate results. Omit the **next_token** property to return the first page. Use the cursor value for **next_token** that was returned in a response to view the next page of results.

       For example: **ABCd1fghIJk2l3M**

       .. note:: The possible values for **next_token** are returned within the **200** response.

       .. important:: The value for **next_token** cannot be **NULL**.

   * - **with_total**
     - Set this value to **true** to include a total count of all results. Default value: **false**.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. api-amperity-pagination-properties-request-end


.. _api-amperity-pagination-properties-response:

Pagination responses
--------------------------------------------------

.. api-amperity-pagination-properties-response-start

All endpoints that support the **GET** HTTP method return following properties to support pagination.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of values for the current page of results.

   * - **next_token**
     - The cursor value to use in a subsequent request to return the next page of results.

       .. note:: When the value for **next_token** is empty, the last page in the results set has been returned.

   * - **total**
     - The total count of all results. This property is only returned when **with_total** is set to **true** in a request.

       .. note:: Obtaining the total count of all results can be an expensive operation when there is a high number of pages in the results set.

.. api-amperity-pagination-properties-response-end
