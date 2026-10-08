.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        The Tenant API changelog lists breaking and non-breaking changes that were made for each version of the Tenant API.

.. meta::
    :content class=swiftype name=body data-type=text:
        The Tenant API changelog lists breaking and non-breaking changes that were made for each version of the Tenant API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Tenant API changelog

==================================================
Changelog
==================================================

.. changelog-start

The Tenant API changelog lists breaking and non-breaking changes that were made for `each version of the Tenant API <explorer-tenant-api_>`__.

.. changelog-end

.. _changelog-current:

Tenant API: 2024-04-01
==================================================

.. changelog-current-start

**Breaking changes**

* None

**Non-breaking changes**

* Add ``GET /audit-events`` endpoint.
* Add ``GET /campaign-drafts`` endpoint.
* Add ``GET /campaigns`` endpoint.
* Add ``GET /ingest/jobs`` endpoint.
* Add ``GET /ingest/jobs/{id}`` endpoint.
* Add ``GET /segments`` endpoint.
* Add ``GET /workflow/runs`` endpoint.
* Add ``GET /workflow/runs/{id}`` endpoint.
* Add ``POST /workflow/runs`` endpoint.
* Add ``POST /workflow/runs/{id}/stop`` endpoint.

.. changelog-current-end


.. _changelog-profile-api-current:

Database Profile API: 2025-07-31
==================================================

.. changelog-profile-api-current-start

**Breaking changes**

* None

**Non-breaking changes**

* Add ``GET /indexes`` endpoint.
* Add ``GET /indexes/{id}`` endpoint.
* Add ``GET /indexes/{id}/profiles`` endpoint.
* Add ``GET /indexes/{id}/profiles/{id}`` endpoint.

.. changelog-profile-api-current-end


.. _changelog-realtime-api-current:

Real-time API: unstable
==================================================

.. changelog-realtime-api-current-start

**Breaking changes**

* None

**Non-breaking changes**

* Add ``POST /events/{stream-id}`` endpoint.
* Add ``GET /lookup/{collection-id}/keychain`` endpoint.
* Add ``POST /lookup/{collection-id}/keychain`` endpoint.
* Add ``GET /profiles/{collection-id}/{profile-id}`` endpoint.
* Add ``GET /segments/{segment-id}/profiles`` endpoint.
* Add ``GET /profiles/{collection-id}/{profile-id}/segments`` endpoint.
* Add ``GET /collections/{collection-id}/stats`` endpoint.
* Add ``GET /collections/{collection-id}/history`` endpoint.

.. changelog-realtime-api-current-end
