.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Release notes for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Release notes for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Release notes

==================================================
Release notes
==================================================

.. updates-intro-start

What is new and what has changed?

.. updates-intro-end

.. tip:: Sign up to `receive Amperity product news via email <https://amperity.com/customers/customer-newsletter>`__ |ext_link|.

   To submit product feedback or requests use the question mark icon within your Amperity tenant, select **Product feedback**, and then follow the prompt.

.. TODO: Headers only for the product release, i.e. "April 2025". Do not use headers within the page for individual updates.

.. TODO: Use a short paragraph, not more than 3 wrapped lines, that contains a link to a doc with the update. only persistent links allowed. only tier 1 or tier 2 changes. no beta announcements. in alphabetical order.

.. TODO: Three choices for badges: 

.. TODO: :bdg-info:`NOTE`

.. TODO: :bdg-success:`NEW`

.. TODO: :bdg-light:`UPDATED`

.. _updates-2026-spring:

Spring 2026
==================================================

.. updates-2026-spring-start

**Amp Insights**

   :bdg-success:`NEW` Use natural language to ask `Amp Insights <assistant.html>`__ questions to understand Amps usage and consumption.

**Audience monetization**

   :bdg-success:`NEW` The :doc:`Audience monetization <monetize>` page is available for monetizing UID 2.0-based audiences in The Trade Desk Data Marketplace.

**Customer Data Assistant**

   :bdg-success:`NEW` The :doc:`Customer Data Assistant <customer_data_assistant>` helps you move from intent to action through natural language conversation to create segments, build journeys, and explore customer data.

**Home page**

   :bdg-success:`NEW` The `Home page <home.html>`__ provides an at-a-glance view of tenant health, Amps consumption, recent work, segment insights, and feature adoption.

**Identity resolution summary**

   :bdg-light:`UPDATED` The :doc:`Identity resolution summary <stitch_summary>` page shows the outcome of identity resolution, including identity changes over time, matching strategies, and identity complexity.

**Labels available in filters**

   :bdg-light:`UPDATED` You can now add and filter by labels for `segments <segments_howtos.html#filter-segments>`__, `queries <queries.html#filter-queries>`__, `campaigns <campaigns.html#filter-campaigns>`__, and `journeys <journeys.html#filter-journeys>`__ to help organize your work by grouping related items together.

**MCP server**

   :bdg-success:`NEW` The `Amperity MCP server <../api/mcp_overview.html>`__ lets AI assistants operate Amperity programmatically. Connect any MCP-compatible client, such as Copilot, Claude, or ChatGPT, to your Amperity tenant, and then use natural language to manage your tenant.

**Predictive modeling UI**

   :bdg-success:`NEW` The Predictive modeling UI has a new setup process for the `predicted customer lifetime value <../operator/model_predicted_clv.html>`__ model and `product affinity <../operator/model_product_affinity.html>`__ model so users can now self-serve and iterate on their predictive models.

.. updates-2026-spring-end


.. _updates-2026-winter:

Winter 2026
==================================================

.. updates-2026-winter-start

**Destination topics**

   :bdg-success:`NEW` New destinations for `Google Analytics 4 <../operator/events_google_analytics.html>`__, `Pinterest offline events <../operator/events_pinterest.html>`__, `SAP Emarsys <../operator/destination_sap_emarsys.html>`__, `The Trade Desk Data Marketplace <../operator/monetize_the_trade_desk_marketplace.html>`__, and `Tulip <../operator/destination_tulip.html>`__.
   
**Incremental matching**

   :bdg-success:`NEW` An `incremental Stitch run <../operator/stitch.html#incremental-match>`__ does not reevaluate existing profiles and only attaches new records to existing profiles *or* creates new profiles. Profiles are not split or merged. PII is not reassigned.

**Journeys AI Assistant**

   :bdg-success:`NEW` The :doc:`AI Assistant <assistant>` is available in the **Journeys Canvas** to help build and refine journeys.

**Journeys measurement**

   :bdg-success:`NEW` `Journeys measurement <../reference/journeys.html#journeys-measurement>`__ provides insight into performance by tracking milestones, measuring goal achievement, and calculating incremental lift on test versus control splits.

**Source topics**

   :bdg-success:`NEW` New source for `Toast <../operator/source_toast.html>`__.

.. updates-2026-winter-end


.. _updates-2025-fall:

Fall 2025
==================================================

.. updates-2025-fall-start

**Amperity Bridge for Google BigQuery (outbound)**

   :bdg-success:`NEW` Configure Amperity to connect with `Google BigQuery <../operator/bridge_google_bigquery.html#to-google-bigquery>`__.

**Bring your own storage**

   :bdg-success:`NEW` For new tenants, `use your own Microsoft Azure storage bucket <../operator/storage.html#provision-storage-on-microsoft-azure>`__ without significant architecture changes.

**Campaign activation states**

   :bdg-success:`NEW` Keep track of customers who are `activated by a campaign <../user/activations.html#campaign-activation-states>`__, including by sub-audience or treatment, by destination, and frequency.

**Custom prompts for AmpAI**

   :bdg-success:`NEW` Use :ref:`custom prompts <ampai-custom-prompt>` with AmpAI to align responses to specific business logic for the AI Assistant for segments and queries.

**Custom segment metrics**

   :bdg-success:`NEW` Define :ref:`custom segment metrics <segments-howitworks-custom-segment-metrics>` that track key indicators that are meaningful to your business.

**Destination topics**

   :bdg-success:`NEW` New destinations for `Listrak SMS <../operator/destination_listrak_sms.html>`__.

**Journey activation states**

   :bdg-success:`NEW` Keep track of customers who have `entered a journey <../user/activations.html#journey-activation-states>`__, moved through specific nodes, and first and last entry.

**Merge paths in journeys**

   :bdg-success:`NEW` A merge node :ref:`joins paths defined by conditional splits or percent splits <journeys-node-merge>` back into a shared pathway within a journey.

**Multi-factor authentication**

   :bdg-light:`UPDATED` Amperity requires :ref:`multi-factor authentication <settings-users-multifactor-authentication>` for all users who log in with a username and password.

.. updates-2025-fall-end


.. _updates-2025-summer:

Summer 2025
==================================================

.. updates-2025-summer-start

**Activation activity**

   :bdg-success:`NEW` Use the Segment Editor to apply customer `activation activity <http://docs.amperity.com/user/activations.html#activation-activity>`__ to segments used with campaigns and journeys.

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

**Events**

   :bdg-success:`NEW` Configure Amperity to send events to `Google Enhanced Conversions <../operator/events_google_enhanced_conversions.html>`__.

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

**Bring your own storage**

   :bdg-success:`NEW` For new tenants, `use your own Amazon AWS storage bucket <../operator/storage.html>`__ with no significant architecture changes required. 

**Complex types in source data**

   :bdg-success:`NEW` Amperity can ingest, process, and utilize complex data structures like arrays and structs directly from source systems without flattening.

**Configure destinations**

   :bdg-light:`UPDATED` The workflow for configuring Amperity to send query results to built-in destinations has been refreshed with a more direct series of steps. Descriptions for each setting are provided within the configuration dialog box alongside the settings. All `destinations that use orchestrations to send query results <../operator/grid_destinations.html>`__ use the updated workflow.

**European Unified ID (EUID)**

   :bdg-success:`NEW` `EUID <euid.html>`__ is available for use with European audiences alongside Unified ID 2.0 (UID2) for North American audiences.

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

   :bdg-success:`NEW` Start workflows programatically using the `POST /workflow/runs <../api/endpoint_post_workflows_start.html>`__ endpoint.

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