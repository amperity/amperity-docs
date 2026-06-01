.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        The Amperity Real-time APIs are released under an unstable version identifier.

.. meta::
    :content class=swiftype name=body data-type=text:
        The Amperity Real-time APIs are released under an unstable version identifier.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity Real-time API versions

==================================================
Versioning
==================================================

.. versioning-start

The Amperity Real-time APIs—the Events API and the Profile API v3—are released under the **unstable** version identifier.

.. versioning-end


.. _versioning-unstable-versions:

Unstable versions
==================================================

.. versioning-unstable-versions-start

Unstable versions contain features that are still in progress and may not be backward compatible.

Unstable versions do not guarantee customer support, notification of changes or breaking changes, or availability.

.. versioning-unstable-versions-end


.. _versioning-no-version-header:

No version header required
==================================================

.. versioning-no-version-header-start

Requests to Real-time API endpoints do not require a version header. The **Authorization** and **Amperity-Tenant** headers are the only required headers.

.. versioning-no-version-header-end


.. _versioning-breaking-changes:

Breaking changes
==================================================

.. versioning-breaking-changes-start

A breaking change occurs when functionality within an API is modified in a way that causes integrations or applications to function abnormally or to stop working.

.. versioning-breaking-changes-end

.. versioning-breaking-changes-examples-start

Examples of breaking changes include, but are not limited to:

* Removing an endpoint
* Renaming a URL, request or response field, or query parameter
* Adding a required request field or query parameter
* Requiring a request field or query parameter that was previously optional
* Removing a request or response field or query parameter
* Modifying a data type or enumeration value
* Adding pagination to a resource collection response

.. versioning-breaking-changes-examples-end


.. _versioning-non-breaking-changes:

Non-breaking changes
--------------------------------------------------

.. versioning-non-breaking-changes-start

A non-breaking change does not cause integrations or applications to function abnormally or to stop working.

.. versioning-non-breaking-changes-end

.. versioning-non-breaking-changes-examples-start

Examples of non-breaking changes include, but are not limited to:

* Adding an endpoint
* Adding a request or response field or query parameter
* Adding an enumeration value

.. versioning-non-breaking-changes-examples-end
