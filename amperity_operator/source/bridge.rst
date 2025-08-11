.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Amperity Bridge allows users to share data between Amperity and a data lakehouse using industry-standard data formats.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity Bridge allows users to share data between Amperity and a data lakehouse using industry-standard data formats.

.. meta::
    :content class=swiftype name=title data-type=string:
        About Amperity Bridge


==================================================
Configure Amperity Bridge
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amperity-bridge-start
   :end-before: .. term-amperity-bridge-end

.. bridge-context-start

Advantages of Amperity Bridge include:

**Fast setup**
   Connect Amperity to a lakehouse in minutes using sharing keys instead of integrations.

**Zero copy**
   Control access to shared tables without replicating data across platforms. Build pipelines faster and consolidate your brand's storage costs into a single location.

**Scalable processing**
   Enrich massive volumes of data quickly. Data is not moved or transformed from where it resides. Model customer data directly in the lakehouse or model it in Amperity.

**Live data**
   View customer data at rest in a lakehouse or in Amperity through a shared catalog. Explore and query data without waiting for refreshes or updates.

.. bridge-context-end

.. bridge-learning-lab-start

.. admonition:: Amperity Learning Lab

   Amperity Bridge enables data sharing between Amperity and data lakehouses. Each bridge can be quickly configured for inbound and outbound shares to give you access to shared tables without replication.

   Start with an overview of data warehouses, compare Databricks and Snowflake, and then learn how Amperity Bridge shares data between Amperity and Databricks.

   Open **Learning Lab** to learn more about how `Amperity Bridge <https://learn.amperity.com/amperity-bridge-and-data-warehouses>`__ |ext_link| works. Registration is required.

.. bridge-learning-lab-end


.. _bridge-sync-data-with:

Sync data with ...
==================================================

.. bridge-sync-data-with-start

Amperity Bridge supports syncing tables with the following applications:

* :ref:`bridge-sync-data-with-databricks`
* :ref:`bridge-sync-data-with-google-bigquery`
* :ref:`bridge-sync-data-with-snowflake`

.. bridge-sync-data-with-end


.. _bridge-sync-data-with-databricks:

Amperity Bridge for Databricks
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-delta-sharing-start
   :end-before: .. term-delta-sharing-end

.. bridge-sync-data-with-databricks-start

Configure inbound and outbound shares in Amperity to :ref:`sync Databricks with Amperity <bridge-databricks-sync-with-amperity>` and :ref:`sync Amperity with Databricks <bridge-databricks-sync-with-databricks>`.

.. bridge-sync-data-with-databricks-end


.. _bridge-sync-data-with-google-bigquery:

Amperity Bridge for Google BigQuery
--------------------------------------------------

.. bridge-sync-data-with-google-bigquery-start

Configure inbound and outbound shares in Amperity to enable :ref:`inbound syncing of data tables between Amperity and Google BigQuery <bridge-google-bigquery-sync-with-amperity>`.

.. bridge-sync-data-with-google-bigquery-end


.. _bridge-sync-data-with-snowflake:

Amperity Bridge for Snowflake
--------------------------------------------------

.. bridge-sync-data-with-snowflake-start

Amperity Bridge for Snowflake is a first-class integration that leverages secure data sharing to enable :doc:`bi-directional data access between Amperity and Snowflake <bridge_snowflake>` without copying data or scheduling ETL workloads.

.. bridge-sync-data-with-snowflake-end
