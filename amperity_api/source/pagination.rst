.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        The Amperity API uses cursor-based pagination to return pages of data for large lists.

.. meta::
    :content class=swiftype name=body data-type=text:
        The Amperity API uses cursor-based pagination to return pages of data for large lists.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity API pagination

==================================================
Pagination
==================================================

.. api-amperity-pagination-start

Amperity uses cursor-based pagination to return pages of data for large lists.

.. tip:: A cursor acts like a pointer; it refers to a particular point in the data and marks the boundary between pages. A paginated endpoint returns responses with a list of results *and* a **next_token** parameter when another page is available in the returned dataset.

   You have reached the last page in the results set when the **next_token** parameter is not returned.

.. api-amperity-pagination-end


.. _api-amperity-pagination-properties-request:

Pagination requests
==================================================

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
==================================================

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
