.. /downloads/markdown/


Tenant API Overview
==================================================

.. include:: ../../amperity_api/source/overview.rst
   :start-after: .. api-amperity-start
   :end-before: .. api-amperity-end

Versions
==================================================

Amperity APIs evolve and change over time. Amperity versions API endpoints to help your brand track changes to the Tenant API and to offer support to developers as these endpoints evolve.

Your team of developers can track improvements to the Tenant API from the `changelog <https://docs.amperity.com/api/changelog.html>`__. Monitor the changelog to know when new versions are available or when existing versions are updated or planned for deprecation.

Breaking changes
--------------------------------------------------

A breaking change occurs when functionality within an API is modified in a way that causes integrations or applications to function abnormally or to stop working.

A breaking change often requires a third-party developer to make changes to their existing integrations or applications to maintain functionality with an API.

Examples of breaking changes include, but are not limited to:

* Removing an endpoint
* Renaming a URL, request or response field, HTTP header, or query parameter
* Adding a required request field, HTTP header, or query parameter
* Requiring a request field, HTTP header, or query parameter that was previously optional
* Removing a request or response field, HTTP header, or query parameter
* Modifying a data type or enumeration value
* Adding pagination to a resource collection response

Non-breaking changes
--------------------------------------------------

A non-breaking change does not cause integrations or applications to function abnormally or to stop working.

A non-breaking change should not require a third-party developer to do any migration work to maintain existing functionality.

Examples of non-breaking changes include, but are not limited to:

* Adding an endpoint
* Adding a request or response field, HTTP header, or query parameter
* Adding an enumeration value

Version identifiers
--------------------------------------------------

A version identifier is a date string that must be included with each request made to an API endpoint. All endpoints are versioned together. This provides consistency across all endpoints and ensures interoperability. A version identifier is updated only when breaking changes occur.

For example:

::

   curl -request GET \
        -url "https://{tenant-id}.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {tenant-id}" \
        -H "Content-Type: application/json" \
        -H "api-version: {version}"


Supported versions
--------------------------------------------------

.. TODO: Do list tables work when converting from RST > Markdown using Pandoc? Keep an eye here.

New versions of the Tenant API are released periodically. Each version of an endpoint will be supported for at least 1 year.

Current versions:

* **2024-04-01** The current version of the Tenant API.
* **2025-07-31** The current version of the Database Profile API.


Unstable versions
--------------------------------------------------

During development, Amperity may release APIs for testing using the **unstable** version identifier. Unstable versions contain features that are still in progress and may not be backward compatible.

Unstable versions do not guarantee customer support, notification of changes or breaking changes, or availability.

Deprecated versions
--------------------------------------------------

At least 6 months notice will be given before any supported version is marked as unsupported. API calls that are made to an endpoint using a version identifier that is no longer supported will return a 400 response.

Amperity APIs evolve and change over time. To warn developers of upcoming deprecations Amperity uses the following headers:

* `Deprecation Header <https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-deprecation-header>`__. When **true** a deprecation will occur at the date indicated in the header.
* `Sunset Header <https://datatracker.ietf.org/doc/html/rfc8594>`__. When **true** a deprecated feature stops working and return a 4xx response at the date indicated in the header.

Deprecation and Sunset headers will be added at least 6 months before a deprecation. A deprecation date will be at least 3 months before a sunset date. For example:

::

   Deprecation: Tue, 1 Sep 2024 23:59:59 GMT
   Sunset: Wed, 1 Dec 2024 23:59:59 GMT

Deprecation and Sunset headers are informational. Amperity recommends building alerts to monitor for these headers to ensure that your applications and workflows can be migrated.

Authentication
==================================================

.. TODO: This is NOT single-sourced, just paraphrased. Is pulled from the A-Z reference in docs and have images and more complex formatting.

All requests that are made to Amperity APIs must be authenticated by access tokens that are signed by Amperity-managed API keys.


API keys
--------------------------------------------------

.. TODO: This is NOT single-sourced, just paraphrased. Is pulled from the A-Z reference in docs and have images and more complex formatting.

Amperity API keys are synthetic identities that are bound to your tenant and enable programmatic access to Amperity. Your API key is configured within Amperity from the **Settings** page, **Security** tab.

Access tokens
--------------------------------------------------

.. TODO: This is NOT single-sourced, just paraphrased. Is pulled from the A-Z reference in docs and have images and more complex formatting.

Access to Amperity APIs requires using JWT access tokens that are signed by Amperity-managed API keys. Access tokens are generated against Amperity API keys within Amperity from the **Settings** page, **Security** tab.

Base URL
==================================================

All requests made to Tenant API endpoints should be directed to the base URL.

Requests
==================================================

.. TODO: Do list tables work when converting from RST > Markdown using Pandoc? Keep an eye here.

Requests made to Tenant API endpoints require the following headers:

* **Authorization** Required. The bearer authentication header. This should be the access token for your tenant's API key.
* **Amperity-Tenant** Required. The ID for the tenant to which the request is sent.

  You can find the tenant ID from the Amperity user interface. From the **Settings** page and select the **Security** tab. Under **API keys**, in the row for an API key, open the |fa-kebab| menu and select **Copy tenant ID**.

  .. important:: A sandbox must use the tenant ID for the sandbox. The request URL must be the same as the base URL of your production tenant.

* **api-version** Required. A supported version of the Tenant API. For example: **2024-04-01**.

In addition to all required headers, you must specify the HTTP method and append endpoint path to the base URL. Most endpoints have a set of endpoint-specific properties that may be included within the request header.

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

Responses
==================================================

Tenant API endpoints use conventional HTTP response status codes--3-digit numbers where the first digit of the code defines the class of response--to indicate success or failure for any API request. Response status codes fall into three categories:

#. 2xx Success
#. 4xx Error

   A 4xx error occurs when information in a request is invalid, such as requesting access to an endpoint that does not exist or by including the wrong value for a query parameter.

#. 5xx Error

   A 5xx error is caused when the API or endpoint is unavailable.

Pagination
==================================================

.. TODO: This is NOT single-sourced. The docs page has more content about pagination than the OpenAPI specification.

Amperity uses cursor-based pagination to return pages of data for large lists. A paginated endpoint returns responses with a list of results *and* a **next_token** parameter when another page is available in the returned dataset. You have reached the last page in the results set when the **next_token** parameter is not returned.

Pagination in requests
--------------------------------------------------

.. TODO: This is NOT single-sourced. The docs page has more content about request pagination and this is a paraphrased version of the key details.

Omit the **next_token** property to return the first page. Use the cursor value for **next_token** that was returned in a response to view the next page of results. The possible values for **next_token** are returned within the **200** response. **next_token** cannot be set to **NULL**.

Pagination in responses
--------------------------------------------------

.. TODO: This is NOT single-sourced. The docs page has more content about request pagination and this is a paraphrased version of the key details.

A response will include the value of the next page as the value of the **next_token** parameter. You may use this value in the next request to return the next page of results. When the value for **next_token** is empty, the last page in the results set has been returned.


Rate limits
==================================================

A rate limit is the number of requests that may be made to the Tenant API in a given time period.

