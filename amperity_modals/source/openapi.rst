.. 
.. /markdown
.. 



==================================================
Amperity API Overview
==================================================

.. include:: ../../amperity_api/source/overview.rst
   :start-after: .. api-amperity-start
   :end-before: .. api-amperity-end

Versions
==================================================

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-start
   :end-before: .. versioning-end

Breaking changes
--------------------------------------------------

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-breaking-changes-start
   :end-before: .. versioning-breaking-changes-end

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-breaking-changes-examples-start
   :end-before: .. versioning-breaking-changes-examples-end

Non-breaking changes
--------------------------------------------------

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-non-breaking-changes-start
   :end-before: .. versioning-non-breaking-changes-end

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-non-breaking-changes-examples-start
   :end-before: .. versioning-non-breaking-changes-examples-end

Version identifiers
--------------------------------------------------

.. TODO: Not identical to docs page because of an admonition. Could reverse the single-sourcing to be FROM this topic to get the admonition enabled (in the docs page).

A version identifier is a date string that must be included with each request made to an API endpoint. All endpoints are versioned together. This provides consistency across all endpoints and ensures interoperability. A version identifier is updated only when breaking changes occur.

**Example versioning in request header**

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-version-identifier-request-header-example-start
   :end-before: .. versioning-version-identifier-request-header-example-end


Supported versions
--------------------------------------------------

.. TODO: Do list tables work when converting from RST > Markdown using Pandoc? Keep an eye here.

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-supported-versions-start
   :end-before: .. versioning-supported-versions-end


Unstable versions
--------------------------------------------------

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-unstable-versions-start
   :end-before: .. versioning-unstable-versions-end

Deprecated versions
--------------------------------------------------

.. include:: ../../amperity_api/source/versioning.rst
   :start-after: .. versioning-deprecated-versions-start
   :end-before: .. versioning-deprecated-versions-end

Authentication
==================================================

.. TODO: This is NOT single-sourced, just paraphrased. This section in docs is pulling from the A-Z reference in docs and have images and more complex formatting.

All requests that are made to Amperity API endpoints must be authenticated by access tokens that are signed by Amperity-managed API keys.


API keys
--------------------------------------------------

.. TODO: This is NOT single-sourced, just paraphrased. This section in docs is pulling from the A-Z reference in docs and have images and more complex formatting.

Amperity API keys are synthetic identities that are bound to your tenant and enable programmatic access to Amperity. Your API key is configured within Amperity from the **Settings** page, **Security** tab.

Access tokens
--------------------------------------------------

.. TODO: This is NOT single-sourced, just paraphrased. This section in docs is pulling from the A-Z reference in docs and have images and more complex formatting.

Access to the Amperity API requires using JWT access tokens that are signed by Amperity-managed API keys. Access tokens are generated against Amperity API keys within Amperity from the **Settings** page, **Security** tab.

Base URL
==================================================

.. include:: ../../amperity_api/source/overview.rst
   :start-after: .. api-amperity-base-url-start
   :end-before: .. api-amperity-base-url-end

Requests
==================================================

.. TODO: Do list tables work when converting from RST > Markdown using Pandoc? Keep an eye here.

.. include:: ../../amperity_api/source/overview.rst
   :start-after: .. api-amperity-request-format-start
   :end-before: .. api-amperity-request-format-end

Responses
==================================================

.. include:: ../../amperity_api/source/overview.rst
   :start-after: .. api-amperity-response-format-start
   :end-before: .. api-amperity-response-format-end

Pagination
==================================================

.. TODO: This is NOT single-sourced. The docs page has more content about pagination than this section in the OpenAPI specification.

Amperity uses cursor-based pagination to return pages of data for large lists. A paginated endpoint returns responses with a list of results *and* a **next_token** parameter when another page is available in the returned dataset. You have reached the last page in the results set when the **next_token** parameter is not returned.

Pagination in requests
--------------------------------------------------

.. TODO: This is NOT single-sourced. The docs page has more content about request pagination and this is a paraphrased version of the key details.

Omit the **next_token** property to return the first page. Use the cursor value for **next_token** that was returned in a response to view the next page of results. The possible values for **next_token** are returned within the **200** response. **next_token** cannot be set to **NULL**.

Pagination in responses
--------------------------------------------------

.. TODO: This is NOT single-sourced. The docs page has more content about request pagination and this is a paraphrased version of the key details.

A response will include the value of the next page as the value of the **next_token** parameter. You may use this value in a subsequent request to return the next page of results. When the value for **next_token** is empty, the last page in the results set has been returned.


Rate limits
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-start
   :end-before: .. rate-limits-end

