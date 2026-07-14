.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Return a paginated list of profiles that are members of a real-time segment.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a paginated list of profiles that are members of a real-time segment.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /segments/{segment-id}/profiles

==================================================
GET /segments/{segment-id}/profiles
==================================================

.. endpoint-get-profile-store-segment-profiles-start

Use the **GET /segments/{segment-id}/profiles** endpoint to return a paginated list of the profiles that are members of a real-time segment.

.. endpoint-get-profile-store-segment-profiles-end

.. note:: This endpoint is part of the Real-time Profile API, an unstable API that may change without advance notice of breaking changes.

.. note:: In the Amperity user interface a real-time segment is configured from a profile store. The list of member profiles is shown as **Customers**.


.. _endpoint-get-profile-store-segment-profiles-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-store-segment-profiles-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.
#. A profile store and a real-time segment must be configured for your tenant. To set up a profile store, contact your Amperity representative.

.. endpoint-get-profile-store-segment-profiles-prerequisites-end

.. note:: The access token must be granted the **real-time-segments:read** and **pii:read** permissions.


.. _endpoint-get-profile-store-segment-profiles-request-url:

Request URL
==================================================

.. endpoint-get-profile-store-segment-profiles-request-url-start

Direct all requests to the **GET /segments/{segment-id}/profiles** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/segments/{segment-id}/profiles

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/segments/{segment-id}/profiles

.. endpoint-get-profile-store-segment-profiles-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profile-store-segment-profiles-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-store-segment-profiles-request:

Requests
==================================================

.. endpoint-get-profile-store-segment-profiles-request-start

A request to the **GET /segments/{segment-id}/profiles** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/segments/{segment-id}/profiles' \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-store-segment-profiles-request-end


.. _endpoint-get-profile-store-segment-profiles-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-store-segment-profiles-request-parameters-start

The following table describes the parameters that may be used with the **GET /segments/{segment-id}/profiles** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **segment-id**
     - String. Required.

       The ID of the real-time segment.

.. note:: This endpoint does not currently accept pagination request parameters. A single page of results is returned.

.. endpoint-get-profile-store-segment-profiles-request-parameters-end


.. _endpoint-get-profile-store-segment-profiles-responses:

Responses
==================================================

.. endpoint-get-profile-store-segment-profiles-responses-start

A response from the **GET /segments/{segment-id}/profiles** endpoint will match an :doc:`HTTP status code <responses>`. A **200** response returns a page of profiles that are members of the segment.

.. endpoint-get-profile-store-segment-profiles-responses-end


.. _endpoint-get-profile-store-segment-profiles-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-store-segment-profiles-response-200ok-start

The **200** response returns a page of profiles.

.. code-block:: json
   :linenos:

   {
     "data": [
       {
         "profile_id": "{profile-id}"
       }
     ],
     "next_token": "{next-token}",
     "total": 0
   }

.. endpoint-get-profile-store-segment-profiles-response-200ok-end


.. _endpoint-get-profile-store-segment-profiles-response-parameters:

Response parameters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-profile-store-segment-profiles-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **data**
     - A JSON array of member profiles. Each item contains the **profile_id** of a profile that is a member of the segment.

   * - **next_token**
     - A pagination cursor returned with the results. This endpoint does not currently accept a **next_token** request parameter.

   * - **total**
     - The total number of profiles that are members of the segment.

.. endpoint-get-profile-store-segment-profiles-response-parameters-end
