.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Return a paginated list of the real-time segments a profile belongs to.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a paginated list of the real-time segments a profile belongs to.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /profiles/{collection-id}/{profile-id}/segments

=====================================================
GET /profiles/{collection-id}/{profile-id}/segments
=====================================================

.. endpoint-get-profile-segments-start

Use the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint to return a paginated list of the real-time segments that a profile is a member of.

.. endpoint-get-profile-segments-end

.. note:: This endpoint is part of the Real-time API, an unstable API that may change without advance notice of breaking changes.


.. _endpoint-get-profile-segments-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-segments-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.
#. A profile collection and a real-time segment must be configured for your tenant. Before creating a profile collection or a real-time segment, you must contact your Amperity representative to enable real-time product features.

.. endpoint-get-profile-segments-prerequisites-end

.. note:: The access token must be granted the **real-time-segments:read** and **pii:read** permissions.


.. _endpoint-get-profile-segments-request-url:

Request URL
==================================================

.. endpoint-get-profile-segments-request-url-start

Direct all requests to the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/profiles/{collection-id}/{profile-id}/segments

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/profiles/{collection-id}/{profile-id}/segments

.. endpoint-get-profile-segments-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profile-segments-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-segments-request:

Requests
==================================================

.. endpoint-get-profile-segments-request-start

A request to the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/profiles/{collection-id}/{profile-id}/segments?limit=100' \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-segments-request-end


.. _endpoint-get-profile-segments-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-segments-request-parameters-start

The following table describes the parameters that may be used with the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **collection-id**
     - String. Required.

       The ID of the profile collection that contains the profile.

   * - **profile-id**
     - String. Required.

       The ID of the profile whose segment membership is returned.

   * - **limit**
     - Integer. Optional.

       The maximum number of records to include in a single page of results.

   * - **next_token**
     - String. Optional.

       An opaque token that is used to paginate results. Omit the **next_token** property to return the first page. Use the cursor value for **next_token** that was returned in a response to view the next page of results.

.. endpoint-get-profile-segments-request-parameters-end


.. _endpoint-get-profile-segments-responses:

Responses
==================================================

.. endpoint-get-profile-segments-responses-start

A response from the **GET /profiles/{collection-id}/{profile-id}/segments** endpoint will match an :doc:`HTTP status code <responses>`. A **200** response returns a page of the real-time segments the profile is a member of.

.. endpoint-get-profile-segments-responses-end


.. _endpoint-get-profile-segments-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-segments-response-200ok-start

The **200** response returns a page of segment memberships.

.. code-block:: json
   :linenos:

   {
     "data": [
       {
         "segment_id": "{segment-id}",
         "segment_name": "{segment-name}"
       }
     ],
     "next_token": "{next-token}",
     "total": 0
   }

.. endpoint-get-profile-segments-response-200ok-end


.. _endpoint-get-profile-segments-response-parameters:

Response parameters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-profile-segments-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of segment memberships. Each item contains the **segment_id** and **segment_name** of a real-time segment that the profile is a member of.

   * - **next_token**
     - A pagination cursor returned with the results. Pass this value as the **next_token** request parameter to view the next page of results.

   * - **total**
     - The total number of real-time segments that the profile is a member of.

.. endpoint-get-profile-segments-response-parameters-end
