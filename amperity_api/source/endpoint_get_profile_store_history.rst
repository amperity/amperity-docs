.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Return a bucketed time series of profile counts for a profile store.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a bucketed time series of profile counts for a profile store.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /collections/{collection-id}/history

==================================================
GET /collections/{collection-id}/history
==================================================

.. endpoint-get-profile-store-history-start

Use the **GET /collections/{collection-id}/history** endpoint to return a bucketed time series of profile counts for a profile store.

.. endpoint-get-profile-store-history-end

.. note:: In the Amperity user interface a profile store is shown on the **Profiles** page and may also be referred to as a profile collection. The value for **{collection-id}** identifies that profile store.


.. _endpoint-get-profile-store-history-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-store-history-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.
#. A profile store must be configured for your tenant. To set up a profile store, contact your Amperity representative.

.. endpoint-get-profile-store-history-prerequisites-end

.. note:: The access token must be granted the **profile-collections:read** permission.


.. _endpoint-get-profile-store-history-request-url:

Request URL
==================================================

.. endpoint-get-profile-store-history-request-url-start

Direct all requests to the **GET /collections/{collection-id}/history** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/collections/{collection-id}/history

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/collections/{collection-id}/history

.. endpoint-get-profile-store-history-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profile-store-history-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-store-history-request:

Requests
==================================================

.. endpoint-get-profile-store-history-request-start

A request to the **GET /collections/{collection-id}/history** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/collections/{collection-id}/history?scale=day' \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-store-history-request-end


.. _endpoint-get-profile-store-history-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-store-history-request-parameters-start

The following table describes the parameters that may be used with the **GET /collections/{collection-id}/history** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **collection-id**
     - String. Required.

       The ID of the profile store.

   * - **scale**
     - String. Optional.

       The size of each time bucket. One of **minute**, **hour**, or **day**. Default value: **day**.

   * - **after**
     - Timestamp. Optional.

       Return buckets at or after this time. When omitted, a default look-back window is used based on the value for **scale**.

   * - **before**
     - Timestamp. Optional.

       Return buckets at or before this time. When omitted, defaults to the current time.

.. endpoint-get-profile-store-history-request-parameters-end


.. _endpoint-get-profile-store-history-responses:

Responses
==================================================

.. endpoint-get-profile-store-history-responses-start

A response from the **GET /collections/{collection-id}/history** endpoint will match an :doc:`HTTP status code <responses>`. A **200** response returns the profile-count time series.

.. endpoint-get-profile-store-history-responses-end


.. _endpoint-get-profile-store-history-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-store-history-response-200ok-start

The **200** response returns the profile-count time series.

.. code-block:: json
   :linenos:

   {
     "scale": "day",
     "data": [
       {
         "bucket": "{timestamp}",
         "count": 0
       }
     ]
   }

.. endpoint-get-profile-store-history-response-200ok-end


.. _endpoint-get-profile-store-history-response-parameters:

Response parameters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-profile-store-history-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **scale**
     - The size of each time bucket. One of **minute**, **hour**, or **day**.

   * - **data**
     - A JSON array of time buckets. Each item contains a **bucket** timestamp and the **count** of profiles for that bucket.

.. endpoint-get-profile-store-history-response-parameters-end


.. _endpoint-get-profile-store-history-response-400:

400
--------------------------------------------------

.. endpoint-get-profile-store-history-response-400-start

The value for **after** is not before the value for **before**.

.. endpoint-get-profile-store-history-response-400-end
