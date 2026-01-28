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
* **Amperity-Tenant** Required. The ID for the tenant to which the request is sent. You can find the tenant ID in the base URL of your tenant.
* **api-version** Required. A supported version of the Amperity API. For example: **2024-04-01**.

In addition to all required headers, you must specify the HTTP method, and base URL. For example:

::

   curl -request GET \
        -url "https://{tenant}.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {tenant}" \
        -H "api-version: {version}"

Most endpoints provide a set of endpoint-specific properties that may be included within the URL header.

.. api-amperity-request-format-end
