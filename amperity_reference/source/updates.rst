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

.. 
.. this is the format
.. 
.. Note: headers only for the product release, i.e. "April 2025". Do not use headers within the page for individual updates.
.. 
.. **title**
.. 
.. short paragraph, not more than 3 wrapped lines, that contains a link to a doc with the update. only persistent links allowed. only tier 1 or tier 2 changes. no beta announcements. in alphabetical order.
.. 
.. Three choices for badges: 
.. 
.. :bdg-info:`NOTE`
.. 
.. :bdg-success:`NEW`
.. 
.. :bdg-light:`UPDATED`
.. 


Product updates for Spring 2025
==================================================

**Activation IDs**
   :bdg-success:`NEW` Define and manage multiple `activation identifiers <https://docs.amperity.com/operator/activation_ids.html>`__ to support multiple channels and a variety of downstream audience requirements.

**Benchmarks**
   :bdg-success:`NEW` `Stitch benchmarks <https://docs.amperity.com/operator/benchmarks.html>`__ are heuristic scores that define the expectations for the quality of customer profiles. Use benchmarks to explore data quality and configuration changes that can help improve the quality of customer profiles in your tenant.

**Bring your own storage** (Amazon S3)
   :bdg-success:`NEW` For new tenants, `use your own AWS storage bucket <https://docs.amperity.com/operator/storage.html>`__ with no significant architecture changes required. 

**Complex types in source data**
   :bdg-success:`NEW` Amperity can ingest, process, and utilize complex data structures like arrays and structs directly from source systems without flattening.

**Configure destinations**
   :bdg-light:`UPDATED` The workflow for configuring Amperity to send query results to built-in destinations has been refreshed with a more direct series of steps. Descriptions for each setting are provided within the configuration dialog box alongside the settings. All `destinations that use orchestrations to send query results <https://docs.amperity.com/destinations.html>`__ use the updated workflow.

**European Unified ID (EUID)**
   :bdg-success:`NEW` `EUID <https://docs.amperity.com/reference/euid.html>`__ is now available for use with European audiences alongside Unified ID 2.0 (UID2) for North American audiences.

**Journeys**
   :bdg-success:`NEW` `Journeys <https://docs.amperity.com/reference/journeys.html>`__ provide a canvas on which you can create, visualize, and manage automated customer workflows for personalized experiences.

**Merge policy settings**
   :bdg-success:`NEW` Use a `drag-and-drop editor to define merge policy settings <https://docs.amperity.com/operator/merge_policy.html>`__ for all customer profile attributes and for all source tables that contain customer PII. This replaces the need to use SQL to define priority and determines how records are added to the **Merged Customers** table.

**Outbound Snowflake bridge**
   :bdg-success:`NEW` Use Secure Data Sharing to make unified customer data available in `Snowflake <https://docs.amperity.com/operator/bridge_snowflake.html>`__.

**Real-time tables**
   :bdg-light:`UPDATED` `Process and activate customer events in real-time <https://docs.amperity.com/operator/realtime.html>`__ instead of scheduled batches.

**Rules editor for Stitch**
   :bdg-light:`UPDATED` Define a `prioritized collection of rules <https://docs.amperity.com/operator/configure_stitch.html#rules>`__ to use for deterministic identity resolution. Rules are evaluated in order, starting from the first, until a rule returns true.

**Start workflows programmatically**
   :bdg-success:`NEW` Start workflows programatically using the `POST /workflow/runs (start) <https://docs.amperity.com/api/endpoint_post_workflows_start.html>`__ endpoint.
