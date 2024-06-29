.. 
.. https://docs.amperity.com/api/
..

.. meta::
    :description lang=en:
        Amperity versions API endpoints to help your brand track changes to the Amperity API and to offer support to developers as these endpoints evolve.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity versions API endpoints to help your brand track changes to the Amperity API and to offer support to developers as these endpoints evolve.

.. meta::
    :content class=swiftype name=title data-type=string:
        Versions


==================================================
Amperity API Versions
==================================================

.. versioning-start

Amperity APIs evolve and change over time. Amperity versions API endpoints to help your brand track changes to the Amperity API and to offer support to developers as these endpoints evolve.

Your team of developers can track improvements to the Amperity API from the :ref:`changelog <changelog-current>`. Monitor the changelog to know when new versions are available and/or when existing versions are updated or planned for deprecation.

.. versioning-end

.. versioning-identifiers-start

.. important:: A :ref:`version identifier <versioning-version-identifier>` is a date string that must be included with each request made to an API endpoint.

   All endpoints are versioned together. This provides consistency across all endpoints and ensures interoperability.

   A version identifier is updated only when :ref:`breaking changes <versioning-breaking-changes>` occur.

.. versioning-identifiers-end


.. _versioning-breaking-changes:

Breaking changes
==================================================

.. versioning-breaking-changes-start

A breaking change occurs when functionality within an API is modified in a way that causes integrations or applications to function abnormally or to stop working.

A breaking change often requires a third-party developer to make changes to their existing integrations or applications to maintain functionality with an API.

.. versioning-breaking-changes-end

.. versioning-breaking-changes-examples-start

Examples of breaking changes include, but are not limited to:

* Removing an endpoint
* Renaming a URL, request or response field, HTTP header, or query parameter
* Adding a required request field, HTTP header, or query parameter
* Requiring a request field, HTTP header, or query parameter that was previously optional
* Removing a request or response field, HTTP header, or query parameter
* Modifying a data type or enumeration value
* Adding pagination to a resource collection response

.. versioning-breaking-changes-examples-end


.. _versioning-non-breaking-changes:

Non-breaking changes
--------------------------------------------------

.. versioning-non-breaking-changes-start

A non-breaking change does not cause integrations or applications to function abnormally or to stop working.

A non-breaking change should not require a third-party developer to do any migration work to maintain existing functionality.

.. versioning-non-breaking-changes-end

.. versioning-non-breaking-changes-examples-start

Examples of non-breaking changes include, but are not limited to:

* Adding an endpoint
* Adding a request or response field, HTTP header, or query parameter
* Adding an enumeration value

.. versioning-non-breaking-changes-examples-end


.. _versioning-version-identifier:

Version identifiers
==================================================

.. versioning-version-identifier-start

A version identifier is a string that identifies a :ref:`supported version <versioning-supported-versions>`. A version identifier must be included in each request that is made to an API endpoint and may be passed as a request header or as a query parameter.

.. versioning-version-identifier-end

**Request header**

.. versioning-version-identifier-request-header-example-start

::

   curl -request GET \
        -url "https://{tenant-id}.amperity.com/api/{endpoint}/" \
        -H "Authorization: Bearer ${access-token}" \
        -H "Amperity-Tenant: {tenant-id}" \
        -H "Content-Type: application/json" \
        -H "api-version: {version}"

where "{version}" identifies the version of the Amperity ID, such as "2024-04-01".

.. versioning-version-identifier-request-header-example-end


.. _versioning-supported-versions:

Supported versions
==================================================

.. versioning-supported-versions-start

New versions of the Amperity API are released periodically. Each version of an endpoint will be supported for at least 1 year.

Current versions:

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Version
     - Deprecated?
     - Description

   * - **2024-04-01**
     - No
     - The current version of the Amperity API.

.. versioning-supported-versions-end


.. _versioning-deprecated-versions:

Deprecated versions
==================================================

.. versioning-deprecated-versions-start

At least 6 months notice will be given before any supported version is marked as unsupported.

.. important:: API calls that are made to an endpoint using a version identifier that is no longer supported will return a 400 response.

.. note:: The Amperity API does not have any deprecated versions.

.. versioning-deprecated-versions-end
