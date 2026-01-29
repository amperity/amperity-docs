.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Requests to Amperity API endpoints use bearer authentication to make requests to a specific tenant ID.

.. meta::
    :content class=swiftype name=body data-type=text:
        Requests to Amperity API endpoints use bearer authentication to make requests to a specific tenant ID.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity API requests

==================================================
Requests
==================================================

.. api-amperity-request-format-start

Requests made to Amperity API endpoints require the following headers:

* **Authorization** Required. The bearer authentication header. This should be the access token for your tenant's API key.
* **Amperity-Tenant** Required. The ID for the tenant to which the request is sent.

  .. include:: ../../amperity_api/source/base_url.rst
     :start-after: .. base-url-tenant-id-start
     :end-before: .. base-url-tenant-id-end

  .. important:: A sandbox must use the tenant ID for the sandbox. The request URL must be the same as the base URL for your production tenant.

* **api-version** Required. A supported version of the Amperity API. For example: **2024-04-01**.

In addition to all required headers, you must specify the HTTP method and append endpoint path to the base URL. Most endpoints provide a set of endpoint-specific properties that may be included within the request header.

**For Amazon AWS**

Requests to a production tenant:

::

   curl -request GET \
        -url "https://app.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {tenant-id}" \
        -H "api-version: {version}"

Requests to a sandbox:

::

   curl -request GET \
        -url "https://app.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {sandbox-tenant-id}" \
        -H "api-version: {version}"

**For Microsoft Azure**

Requests to a production tenant:

::

   curl -request GET \
        -url "https://{tenant-id}.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {tenant-id}" \
        -H "api-version: {version}"

Requests to a sandbox:

::

   curl -request GET \
        -url "https://{tenant-id}.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {sandbox-tenant-id}" \
        -H "api-version: {version}"

.. api-amperity-request-format-end
