.. https://docs.amperity.com/api/

:canonical: https://docs.amperity.com/api/endpoints.html


.. meta::
    :description lang=en:
        A landing page for the collection of content about the Amperity API.

.. meta::
    :content class=swiftype name=body data-type=text:
        A landing page for the collection of content about the Amperity API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity API endpoints

==================================================
Endpoints
==================================================

.. endpoints-about-start

The Amperity API enables programmatic access to your Amperity tenant with the following groups of endpoints:

* :ref:`endpoints-audit-events`
* :ref:`endpoints-campaigns`
* :ref:`endpoints-ingest-jobs`
* :ref:`endpoints-segments`
* :ref:`endpoints-workflows`

.. endpoints-about-end


.. _endpoints-audit-events:

Audit events
==================================================

.. endpoints-audit-events-start

Use the audit event endpoints to return a log of up to 1000 audit events for user activity.

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /audit-events
      :link: endpoint_get_audit_events_list.html

      .. include:: ../../amperity_reference/source/activity_logs.rst
         :start-after: .. settings-user-activity-logs-about-start
         :end-before: .. settings-user-activity-logs-about-end

.. endpoints-audit-events-end


.. _endpoints-campaigns:

Campaigns
==================================================

.. endpoints-campaigns-start

Use campaign endpoints to return a list of campaigns or draft campaigns.

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /campaign-drafts
      :link: endpoint_get_campaign_drafts_list.html

      .. include:: ../../amperity_api/source/endpoint_get_campaign_drafts_list.rst
         :start-after: .. endpoint-get-campaign-drafts-list-start
         :end-before: .. endpoint-get-campaign-drafts-list-end

   .. grid-item-card:: GET /campaigns
      :link: endpoint_get_campaigns_list.html

      .. include:: ../../amperity_api/source/endpoint_get_campaigns_list.rst
         :start-after: .. endpoint-get-campaigns-list-start
         :end-before: .. endpoint-get-campaigns-list-end

.. endpoints-campaigns-end


.. _endpoints-ingest-jobs:

Ingest jobs
==================================================

.. endpoints-ingest-jobs-start

Use ingest job endpoints to return a list of jobs or return details about a specific job.

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /ingest/jobs
      :link: endpoint_get_ingest_jobs.html

      .. include:: ../../amperity_api/source/endpoint_get_ingest_jobs.rst
         :start-after: .. endpoint-get-ingest-jobs-start
         :end-before: .. endpoint-get-ingest-jobs-end

   .. grid-item-card:: GET /ingest/jobs/(id)
      :link: endpoint_get_ingest_jobs_id.html

      .. include:: ../../amperity_api/source/endpoint_get_ingest_jobs_id.rst
         :start-after: .. endpoint-get-ingest-jobs-id-start
         :end-before: .. endpoint-get-ingest-jobs-id-end

.. endpoints-ingest-jobs-end


.. _endpoints-segments:

Segments
==================================================

.. endpoints-segments-start

Use the segments endpoint to return a list of segments.

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /segments
      :link: endpoint_get_segments_list.html

      .. include:: ../../amperity_api/source/endpoint_get_segments_list.rst
         :start-after: .. endpoint-get-segments-list-start
         :end-before: .. endpoint-get-segments-list-end

.. endpoints-segments-end


.. _endpoints-workflows:

Workflows
==================================================

.. endpoints-workflows-start

Use workflows endpoints to get a list of workflows, details for a specific workflow, start and stop a workflow.

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface


   .. grid-item-card:: GET /workflow/runs
      :link: endpoint_get_workflows_list.html

      .. include:: ../../amperity_api/source/endpoint_get_workflows_list.rst
         :start-after: .. endpoint-get-workflows-list-start
         :end-before: .. endpoint-get-workflows-list-end

   .. grid-item-card:: GET /workflow/runs/{id}
      :link: endpoint_get_workflows_fetch.html

      .. include:: ../../amperity_api/source/endpoint_get_workflows_fetch.rst
         :start-after: .. endpoint-get-workflows-fetch-start
         :end-before: .. endpoint-get-workflows-fetch-end

   .. grid-item-card:: POST /workflow/runs
      :link: endpoint_post_workflows_start.html

      .. include:: ../../amperity_api/source/endpoint_post_workflows_start.rst
         :start-after: .. endpoint-post-workflows-start-start
         :end-before: .. endpoint-post-workflows-start-end

   .. grid-item-card:: POST /workflow/runs/{id}/stop
      :link: endpoint_post_workflows_stop.html

      .. include:: ../../amperity_api/source/endpoint_post_workflows_stop.rst
         :start-after: .. endpoint-post-workflows-stop-start
         :end-before: .. endpoint-post-workflows-stop-end

.. endpoints-workflows-end
