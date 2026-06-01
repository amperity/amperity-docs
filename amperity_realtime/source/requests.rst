.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        Requests to Amperity Real-time API endpoints use bearer authentication to make requests to a specific tenant ID.

.. meta::
    :content class=swiftype name=body data-type=text:
        Requests to Amperity Real-time API endpoints use bearer authentication to make requests to a specific tenant ID.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity Real-time API requests

==================================================
Requests
==================================================

.. api-amperity-request-format-start

Requests made to Amperity Real-time API endpoints require the following headers:

* **Authorization** Required. The bearer authentication header. Use the access token for your tenant's API key.
* **Amperity-Tenant** Required. The ID for the tenant to which the request is sent.

  .. important:: A sandbox must use the tenant ID for the sandbox. The request URL must be the same as the base URL for your production tenant.

.. api-amperity-request-format-end


.. _requests-events:

Events API
==================================================

.. api-amperity-request-format-events-start

Events API endpoints do not use the ``/prof/`` path prefix.

**For Amazon AWS**

.. code-block:: rest

   curl --request POST \
        --url "https://app.amperity.com/events/{stream-id}" \
        --header 'Authorization: Bearer {token}' \
        --header 'Amperity-Tenant: {tenant-id}'

**For Microsoft Azure**

.. code-block:: rest

   curl --request POST \
        --url "https://{tenant-id}.amperity.com/events/{stream-id}" \
        --header 'Authorization: Bearer {token}' \
        --header 'Amperity-Tenant: {tenant-id}'

.. api-amperity-request-format-events-end


.. _requests-profile:

Profile API v3
==================================================

.. api-amperity-request-format-profile-start

Profile API v3 endpoints use the ``/prof/`` path prefix.

**For Amazon AWS**

.. code-block:: rest

   curl --request GET \
        --url "https://app.amperity.com/prof/{endpoint}" \
        --header 'Authorization: Bearer {token}' \
        --header 'Amperity-Tenant: {tenant-id}'

**For Microsoft Azure**

.. code-block:: rest

   curl --request GET \
        --url "https://{tenant-id}.amperity.com/prof/{endpoint}" \
        --header 'Authorization: Bearer {token}' \
        --header 'Amperity-Tenant: {tenant-id}'

.. api-amperity-request-format-profile-end
