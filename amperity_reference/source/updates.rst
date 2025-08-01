.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Product updates for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Product updates for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Product updates

==================================================
Product updates
==================================================

.. updates-intro-start

What's new and what's changed?

.. updates-intro-end

.. TODO: Headers only for the product release, i.e. "April 2025". Do not use headers within the page for individual updates.

.. TODO: Use a short paragraph, not more than 3 wrapped lines, that contains a link to a doc with the update. only persistent links allowed. only tier 1 or tier 2 changes. no beta announcements. in alphabetical order.

.. TODO: Three choices for badges: 

.. TODO: :bdg-info:`NOTE`

.. TODO: :bdg-success:`NEW`

.. TODO: :bdg-light:`UPDATED`


.. _updates-2025-summer:

Summer 2025
==================================================

.. updates-2025-summer-start

**AI Assistant**
   :bdg-success:`NEW` The :doc:`AI Assistant <assistant>` is available in the **Segments** page.

**Amperity Bridge for Google BigQuery (inbound)**
   :bdg-success:`NEW` Configure Amperity to sync data with `Google BigQuery <../operator/bridge_google_bigquery.html>`__.

**Configure destinations**
   :bdg-light:`UPDATED` The configuration steps for `destinations <../operator/grid_destinations.html>`__ have been updated with dedicated configuration paths for `campaigns <../operator/grid_campaigns.html>`__.

**Destination topics**
   :bdg-success:`NEW` New destinations for `Dotdigital <../operator/destination_dotdigital.html>`__, `MoEngage <../operator/destination_moengage.html>`__, `Movable Ink <../operator/destination_moveableink.html>`__, and `LinkedIn DMP  <../operator/destination_linkedin_dmp.html>`__.

**Journeys**
   :bdg-light:`UPDATED` Use the activation canvas to build a series of audiences for :doc:`multi-touch journeys <journeys>` to support your brand's marketing ecosystem.

**Multi-factor authentication**
   :bdg-success:`NEW` Added support to :ref:`enforce multi-factor authentication (MFA) <settings-users-multifactor-authentication>` for all username-password users on non-SSO tenants.

**Offline events**
   :bdg-success:`NEW` Configure Amperity to send offline events to `Google Enhanced Conversions <../operator/events_google_enhanced_conversions.html>`__.

**Profile API**
   :bdg-light:`UPDATED` The Profile API is updated to support flexible, multi-criteria search that allows systems to look up profiles using any combination of available fields from a single endpoint.

   :bdg-success:`NEW` The following endpoints are new:

   * `GET /indexes <../api/endpoint_get_profile_index.html>`__ 
   * `GET /indexes/{id} <../api/endpoint_get_profile_index_id.html>`__ 
   * `GET /indexes/{id}/profiles <../api/endpoint_get_profiles_list.html>`__ 
   * `GET /indexes/{id}/profiles/{id} <../api/endpoint_get_profile.html>`__.

.. updates-2025-summer-end


.. _updates-2025-spring:

Spring 2025
==================================================

.. updates-2025-spring-start

**Activation IDs**
   :bdg-success:`NEW` Define and manage multiple `activation identifiers <../operator/activation_ids.html>`__ to support multiple channels and a variety of downstream audience requirements.

**Benchmarks**
   :bdg-success:`NEW` `Stitch benchmarks <../operator/benchmarks.html>`__ are heuristic scores that define the expectations for the quality of customer profiles. Use benchmarks to explore data quality and configuration changes that can help improve the quality of customer profiles in your tenant.

**Bring your own storage** (Amazon S3)
   :bdg-success:`NEW` For new tenants, `use your own AWS storage bucket <../operator/storage.html>`__ with no significant architecture changes required. 

**Complex types in source data**
   :bdg-success:`NEW` Amperity can ingest, process, and utilize complex data structures like arrays and structs directly from source systems without flattening.

**Configure destinations**
   :bdg-light:`UPDATED` The workflow for configuring Amperity to send query results to built-in destinations has been refreshed with a more direct series of steps. Descriptions for each setting are provided within the configuration dialog box alongside the settings. All `destinations that use orchestrations to send query results <../operator/grid_destinations.html>`__ use the updated workflow.

**European Unified ID (EUID)**
   :bdg-success:`NEW` `EUID <euid.html>`__ is now available for use with European audiences alongside Unified ID 2.0 (UID2) for North American audiences.

**Journeys**
   :bdg-success:`NEW` `Journeys <journeys.html>`__ provide a canvas on which you can create, visualize, and manage automated customer workflows for personalized experiences.

**Merge policy settings**
   :bdg-success:`NEW` Use a `drag-and-drop editor to define merge policy settings <../operator/merge_policy.html>`__ for all customer profile attributes and for all source tables that contain customer PII. This replaces the need to use SQL to define priority and determines how records are added to the **Merged Customers** table.

**Amperity Bridge for Snowflake (outbound)**
   :bdg-success:`NEW` Use Secure Data Sharing to make unified customer data available in `Snowflake <../operator/bridge_snowflake.html>`__.

**Real-time tables**
   :bdg-light:`UPDATED` `Process and activate customer events in real-time <../operator/realtime.html>`__ instead of scheduled batches.

**Rules editor for Stitch**
   :bdg-light:`UPDATED` Define a `prioritized collection of rules <../operator/configure_stitch.html#rules>`__ to use for deterministic identity resolution. Rules are evaluated in order, starting from the first, until a rule returns true.

**Start workflows programmatically**
   :bdg-success:`NEW` Start workflows programatically using the `POST /workflow/runs (start) <../api/endpoint_post_workflows_start.html>`__ endpoint.

.. updates-2025-spring-end


.. _updates-2024-fall:

Fall 2024
==================================================

.. updates-2024-fall-start

**Amazon S3 storage**
   :bdg-success:`NEW` Configure a new tenant to use your brand's `Amazon S3 storage <../operator/storage.html>`__.

**Amperity Bridge for Snowflake (inbound)**
   :bdg-success:`NEW` Use Secure Data Sharing to make `Snowflake <../operator/bridge_snowflake.html>`__ data available to unified customer profiles.

**Real-time tables**
   :bdg-success:`NEW` `Process and activate customer events in real-time <../operator/realtime.html>`__ instead of scheduled batches.

.. updates-2024-fall-end