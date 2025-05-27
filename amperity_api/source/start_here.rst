.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        A landing page for the collection of content about the Amperity API.

.. meta::
    :content class=swiftype name=body data-type=text:
        A landing page for the collection of content about the Amperity API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Start here


==================================================
About the Amperity API
==================================================

.. start-here-start

The Amperity API enables programmatic access to your Amperity tenant by using a collection of RESTful endpoints that support API-first use cases for integrations, applications, and custom workflows. Use Amperity API endpoints to streamline workflows, enhance marketing strategies, and unlock the value of your brand's customer data.

.. start-here-end


.. _start-here-endpoints:

Available Endpoints
==================================================

.. include:: ../../shared/api_amperity.rst
   :start-after: .. term-http-methods-start
   :end-before: .. term-http-methods-end


.. _start-here-openapi-specification:

OpenAPI specification
==================================================

.. start-here-openapi-specification-start

Amperity provides an `OpenAPI specification <https://docs.amperity.com/api/openapi.html>`__ for the Amperity API. Download the OpenAPI specification, and then import it into an API tool, such as `Postman <https://www.postman.com/>`__, to start interacting with Amperity API endpoints.

.. start-here-openapi-specification-end


.. _start-here-versioning:

Versioning
==================================================

.. start-here-versioning-start

Amperity APIs evolve and change over time. :doc:`Amperity versions API endpoints <versioning>` to help your brand track changes to the Amperity API and to offer support to developers as these endpoints evolve.

Your team of developers can track improvements to the Amperity API from the :ref:`changelog <changelog-current>`. Monitor the changelog to know when new versions are available and/or when existing versions are updated or planned for deprecation.

.. start-here-versioning-end


.. _start-here-authentication:

Authentication
==================================================

.. start-here-authentication-start

All requests that are made to Amperity API endpoints :doc:`must be authenticated by access tokens that are signed by Amperity-managed API keys <authentication>`.

Amperity :ref:`API keys <authentication-api-keys>` are synthetic identities that are bound to your tenant and enable programmatic access to Amperity.

:ref:`Access tokens <authentication-access-tokens>` are signed by Amperity-managed API keys and are authorized to perform certain actions with Amperity.

.. start-here-authentication-end


.. _start-here-base-url:

Base URL
==================================================

.. start-here-base-url-start

All requests made to Amperity API endpoints should be directed to the following base URL:

::

   https://{tenant-id}.amperity.com/api

.. start-here-base-url-end


.. _start-here-requests:

Requests
==================================================

.. start-here-requests-start

All requests made to an Amperity API endpoint require a :ref:`base URL <api-amperity-base-url>`, a tenant ID, and an :ref:`access token <authentication-access-tokens>` for a valid :ref:`API key <authentication-api-keys-add>`.

In addition to all required headers, you must specify the HTTP method, base URL, and content type. For example:

::

   curl -request GET \
        -url "https://{tenant-id}.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {tenant-id}" \
        -H "Content-Type: application/json" \
        -H "api-version: {version}"

Most endpoints have additional endpoint-specific parameters that may be included in the request.

.. start-here-requests-end


.. _start-here-responses:

Responses
==================================================

.. start-here-responses-start

The Amperity API responds in JSON format. Each response includes relevant :doc:`HTTP status codes <responses>` that indicate the success or the failure of a request. The individual properties in a response will vary by endpoint; all endpoints that support the GET HTTP method will return lists using :ref:`pagination <api-amperity-pagination>`.

.. start-here-responses-end


.. _start-here-pagination:

Pagination
==================================================

.. start-here-pagination-start

Amperity uses :ref:`cursor-based pagination <api-amperity-pagination>` to return pages of data for large lists.

.. start-here-pagination-end


.. _start-here-rate-limits:

Rate Limits
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end
