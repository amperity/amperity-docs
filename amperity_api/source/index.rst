.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Programmatic access to your Amperity tenant by using a collection of RESTful endpoints that support API-first use cases for integrations, applications, and custom workflows.

.. meta::
    :content class=swiftype name=body data-type=text:
        Programmatic access to your Amperity tenant by using a collection of RESTful endpoints that support API-first use cases for integrations, applications, and custom workflows.

.. meta::
    :content class=swiftype name=title data-type=string:
        About the Amperity API

==================================================
About the Amperity API
==================================================

.. start-here-start

The Amperity API enables programmatic access to your Amperity tenant by using a collection of RESTful endpoints that support API-first use cases for integrations, applications, and custom workflows. Use Amperity API endpoints to streamline workflows, enhance marketing strategies, and unlock the value of your brand's customer data.

.. start-here-end


.. _index-openapi-specification:

OpenAPI specification
==================================================

.. start-here-openapi-specification-start

Amperity has an `OpenAPI specification <https://docs.amperity.com/api/openapi.html>`__ for the Amperity API along with one for `unstable endpoints <https://docs.amperity.com/api/openapi-unstable.html>`__. Download the OpenAPI specification, and then import it into an API tool, such as `Postman <https://www.postman.com/>`__, to start interacting with Amperity API endpoints.

.. start-here-openapi-specification-end


.. toctree::
   :caption: OVERVIEW
   :maxdepth: 2
   :hidden:

   About the Amperity API <overview>
   Versioning <versioning>
   Authentication <authentication>
   Base URL <base_url>
   Requests <requests>
   Responses <responses>
   Pagination <pagination>
   Rate limits <rate_limits>
   Changelog <changelog>


.. toctree::
   :caption: AMPERITY API ENDPOINTS
   :maxdepth: 2
   :hidden:

   About endpoints <endpoints>
   GET /audit-events <endpoint_get_audit_events_list>
   GET /campaign-drafts <endpoint_get_campaign_drafts_list>
   GET /campaigns <endpoint_get_campaigns_list>
   GET /ingest/jobs <endpoint_get_ingest_jobs>
   GET /ingest/jobs/{id} <endpoint_get_ingest_jobs_id>
   GET /segments <endpoint_get_segments_list>
   GET /workflow/runs <endpoint_get_workflows_list>
   POST /workflow/runs/ <endpoint_post_workflows_start>
   GET /workflow/runs/{id} <endpoint_get_workflows_fetch>
   POST /workflow/runs/{id}/stop <endpoint_post_workflows_stop>
   OpenAPI specification <https://docs.amperity.com/api/openapi.html>
   Unstable endpoints <https://docs.amperity.com/api/openapi-unstable.html>


.. toctree::
   :caption: PROFILE API ENDPOINTS
   :maxdepth: 2
   :hidden:

   GET /indexes <endpoint_get_profile_index>
   GET /indexes/{id} <endpoint_get_profile_index_id>
   GET /indexes/{id}/profiles <endpoint_get_profiles_list>
   GET /indexes/{id}/profiles/{id} <endpoint_get_profile>

.. toctree::
   :caption: MORE RESOURCES
   :hidden:

   Help Center <https://help.amperity.com>
   Learning Lab <https://learn.amperity.com>
   System Status <https://status.amperity.com>
   Amperity.com <https://www.amperity.com>

