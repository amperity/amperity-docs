.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        A dataset is a collection of data that is grouped together to support all of the use cases required by a high-level goal.

.. meta::
    :content class=swiftype name=body data-type=text:
        A dataset is a collection of data that is grouped together to support all of the use cases required by a high-level goal.

.. meta::
    :content class=swiftype name=title data-type=string:
        About datasets

==================================================
About datasets
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dataset-start
   :end-before: .. term-dataset-end

.. datasets-about-start

For example, data that is streamed to Amperity to provide the underlying data that enables real-time workflows may also be configured to run as part of the batch process, which makes that data available to the real-time dataset *and* the customer 360 dataset.

.. datasets-about-end


.. _datasets-customer-profile:

Customer profile
==================================================

.. TODO: Add link to databases.rst for "most often represented by the Customer 360 database" and filtered_360_databases.rst for "filtering databases by brand".

.. datasets-customer-360-start

A customer profile dataset contains a collection of unified customer profiles that your brand can use to build audiences that enable any marketing workflow.

A customer profile dataset is most often represented by the **Customer 360** database in your Amperity tenant. This may be configured to filter databases by brand.

.. datasets-customer-360-end


.. _datasets-realtime:

Real-time
==================================================

.. TODO: Add link to realtime.rst for "real-time dataset contains data that is streamed to Amperity".

.. datasets-realtime-start

A real-time dataset contains data that is streamed to Amperity, processed quickly within Amperity, and then made avaialable to use cases that require access to time-sensitive data that is updated more frequently than batched workflows.

.. datasets-realtime-end


.. _datasets-stitched:

Stitched
==================================================

.. datasets-stitched-start

Stitch uses a patented identity resolution workflow to find the hidden connections in your brand's online and offline customer data. Stitch assigns each customer profile a unique identifier that remains stable over time, even when new and conflicting data is collected.

A stitched dataset contains a collection of unified customer profiles that are maintained by Stitch. A stitched dataset provides the foundation for all of the datasets that your brand can build within Amperity. Tables within the stitched dataset are also referred to as "standard core tables".

.. datasets-stitched-end


.. _datasets-stitched-standard-core:

Standard core tables
--------------------------------------------------

.. TODO: Hook the following section in as an include.

.. TODO: Need to move some content about core tables into the operators guide.

.. databases-core-table-type-standard-start

Standard core tables belong to one of the following broad categories:

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Stitched domain tables**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-domain-table-stitched-start
          :end-before: .. term-domain-table-stitched-end

       .. image:: ../../images/howitworks-standard-core-table.png
          :width: 440 px
          :alt: Standard core tables.
          :align: left
          :class: no-scaled-link

       Stitched versions of domain tables have an added column for the Amperity ID and replace the source domain table within Amperity for all downstream use cases, but are otherwise identical to the source domain table.

   * - **Unified tables**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-unified-tables-start
          :end-before: .. term-unified-tables-end

       The collection of unified tables that is generated within your tenant depends on the types of semantic tags that were applied to feeds and/or custom domain tables in the **Sources** tab.

   * - **Stitch QA tables**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-stitch-qa-tables-start
          :end-before: .. term-stitch-qa-tables-end

       Some Stitch QA tables are required by databases that are configured as customer 360 databases; most are only available from databases that are configured as a Stitch QA database.

.. databases-core-table-type-standard-end


.. _datasets-sources:

Source
==================================================

.. TODO: Link to sources cardwall, bridge overview, and individual source datasets.

.. datasets-sources-start

Each data source or data asset that is made available to your Amperity tenant acts as a dataset that can be used as a building block for a stitched dataset, a real-time dataset, or a customer 360 dataset.

The list of possible source datasets is unique to your brand and depends on what types of data your brand wants to make available to Amperity.

Amperity provides a collection of standard source datasets, such as fiscal calendars, common nicknames, standardizations, that your brand can use to simplify how your brand's data is understood by Amperity.

.. datasets-sources-end
