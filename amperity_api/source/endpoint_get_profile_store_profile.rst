.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Return a single profile from a profile store by its profile ID.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a single profile from a profile store by its profile ID.

.. meta::
    :content class=swiftype name=title data-type=string:
        GET /profiles/{collection-id}/{profile-id}

==================================================
GET /profiles/{collection-id}/{profile-id}
==================================================

.. endpoint-get-profile-store-profile-start

Use the **GET /profiles/{collection-id}/{profile-id}** endpoint to return a single profile from a profile store by its profile ID.

.. endpoint-get-profile-store-profile-end

.. note:: In the Amperity user interface a profile store is shown on the **Profiles** page and may also be referred to as a profile collection. The value for **{collection-id}** identifies that profile store.


.. _endpoint-get-profile-store-profile-prerequisites:

Prerequisites
==================================================

.. endpoint-get-profile-store-profile-prerequisites-start

#. :ref:`Add an API key <authentication-api-keys-add>`.
#. :ref:`Generate an access token <authentication-access-token-generate>`.
#. A profile store must be configured for your tenant. To set up a profile store, contact your Amperity representative.

.. endpoint-get-profile-store-profile-prerequisites-end

.. note:: The access token must be granted the **profile-collections:read** and **pii:read** permissions.


.. _endpoint-get-profile-store-profile-request-url:

Request URL
==================================================

.. endpoint-get-profile-store-profile-request-url-start

Direct all requests to the **GET /profiles/{collection-id}/{profile-id}** endpoint to the request URL. The request URL uses the base URL with the endpoint path appended.

**Amazon AWS**

.. code-block:: rest

   https://app.amperity.com/prof/profiles/{collection-id}/{profile-id}

**Microsoft Azure**

.. code-block:: rest

   https://{tenant-id}.amperity.com/prof/profiles/{collection-id}/{profile-id}

.. endpoint-get-profile-store-profile-request-url-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _endpoint-get-profile-store-profile-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end


.. _endpoint-get-profile-store-profile-request:

Requests
==================================================

.. endpoint-get-profile-store-profile-request-start

A request to the **GET /profiles/{collection-id}/{profile-id}** endpoint is similar to:

.. code-block:: rest

   curl --request GET \
          'https://app.amperity.com/prof/profiles/{collection-id}/{profile-id}' \
        --header 'amperity-tenant: {tenant-id}' \
        --header 'Authorization: Bearer {token}'

This example is formatted for readability in a narrow page layout.

.. endpoint-get-profile-store-profile-request-end


.. _endpoint-get-profile-store-profile-request-parameters:

Request parameters
--------------------------------------------------

.. endpoint-get-profile-store-profile-request-parameters-start

The following table describes the parameters that may be used with the **GET /profiles/{collection-id}/{profile-id}** endpoint.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **collection-id**
     - String. Required.

       The ID of the profile store that contains the profile.

   * - **profile-id**
     - String. Required.

       The ID of the profile to return.

   * - **enrich**
     - Boolean. Optional.

       Set to **true** to include enriched attributes in the returned profile. Default value: **false**.

.. endpoint-get-profile-store-profile-request-parameters-end


.. _endpoint-get-profile-store-profile-responses:

Responses
==================================================

.. endpoint-get-profile-store-profile-responses-start

A response from the **GET /profiles/{collection-id}/{profile-id}** endpoint will match an :doc:`HTTP status code <responses>`. A **200** response returns the profile.

.. endpoint-get-profile-store-profile-responses-end


.. _endpoint-get-profile-store-profile-response-200ok:

200 OK
--------------------------------------------------

.. endpoint-get-profile-store-profile-response-200ok-start

The **200** response returns the profile.

.. code-block:: json
   :linenos:

   {
     "collection_id": "{collection-id}",
     "profile_id": "{profile-id}",
     "attributes": {
       "email": "customer@example.com"
     },
     "created_at": "{timestamp}",
     "updated_at": "{timestamp}",
     "ticked_at": "{timestamp}",
     "links": []
   }

.. endpoint-get-profile-store-profile-response-200ok-end


.. _endpoint-get-profile-store-profile-response-parameters:

Response parameters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. endpoint-get-profile-store-profile-response-parameters-start

A **200 OK** response contains the following parameters.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Parameter
     - Description

   * - **collection_id**
     - The ID of the profile store that contains the profile.

   * - **profile_id**
     - The unique ID for the profile.

   * - **attributes**
     - A map of key-value profile attributes. The specific keys and values depend on how the profile store is configured.

   * - **created_at**
     - The timestamp at which the profile was created.

   * - **updated_at**
     - The timestamp at which the profile was last updated.

   * - **ticked_at**
     - The timestamp at which the profile was last processed.

   * - **links**
     - The keychain links associated with the profile.

.. endpoint-get-profile-store-profile-response-parameters-end


.. _endpoint-get-profile-store-profile-response-404:

404
--------------------------------------------------

.. endpoint-get-profile-store-profile-response-404-start

No profile with the given **{profile-id}** exists in the profile store.

.. endpoint-get-profile-store-profile-response-404-end
