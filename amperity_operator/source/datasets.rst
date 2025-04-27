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


.. _datasets-sources:

Data sources
==================================================

.. TODO: Link to sources cardwall, bridge overview, and individual source datasets.

.. datasets-sources-start

Each `data source <https://docs.amperity.com/sources.html>`__ or :doc:`data asset <data_assets>` that is made available to your Amperity tenant acts as a dataset that can be used as a building block for customer profiles. The combination of source datasets is unique to your brand and depends on what types of data your brand wants to make available to Amperity.

.. datasets-sources-end


.. _datasets-customer-profile:

Customer profiles
==================================================

.. datasets-customer-360-start

A customer profile dataset contains a collection of unified customer profiles that your brand can use to build audiences that enable any marketing workflow.

A customer profile dataset is most often represented by the **Customer 360** database in your Amperity tenant. This may be configured to :doc:`filter databases by brand <filtered_360_databases>`.

.. datasets-customer-360-end

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-profiles-start
   :end-before: .. databases-profiles-end

.. image:: ../../images/mockup-customer360-tab-customer-profile.png
   :width: 600 px
   :alt: Customer 360 page, customer profile
   :align: left
   :class: no-scaled-link

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-profiles-context-start
   :end-before: .. databases-profiles-context-end


.. _datasets-flexible-merge-rules:

Flexible merge rules
--------------------------------------------------

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-flexible-merge-rules-start
   :end-before: .. databases-flexible-merge-rules-end


.. _datasets-realtime:

Real-time tables
==================================================

.. include:: ../../amperity_operator/source/realtime.rst
   :start-after: .. real-time-about-start
   :end-before: .. real-time-about-end


.. _datasets-stitched:

Stitched tables
==================================================

.. datasets-stitched-start

Stitch uses a patented identity resolution workflow to find the hidden connections in your brand's online and offline customer data. Stitch assigns each customer profile a unique identifier that remains stable over time, even when new and conflicting data is collected.

A stitched dataset contains a collection of unified customer profiles that are maintained by Stitch. A stitched dataset provides the foundation for all of the datasets that your brand can build within Amperity. Tables within the stitched dataset are also referred to as "standard core tables".

.. datasets-stitched-end


.. _datasets-stitched-standard-core:

Standard core tables
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-core-tables-standard-start
   :end-before: .. term-core-tables-standard-end

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-core-table-type-standard-start
   :end-before: .. databases-core-table-type-standard-end
