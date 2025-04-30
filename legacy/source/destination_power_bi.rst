.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Microsoft Power BI
.. |plugin-name| replace:: Microsoft Power BI
.. |what-send| replace:: data
.. |filter-the-list| replace:: "micro"
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


==================================================
Send data to Microsoft Power BI
==================================================

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_power_bi.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-powerbi-start
   :end-before: .. term-microsoft-powerbi-end

.. destination-powerbi-important-start

.. important:: Data is not sent from Amperity directly to Microsoft Power BI. Microsoft Power BI must connect to a location that supports queries to that data and cannot connect directly to a static file. Amperity must send data to Microsoft Power BI indirectly by configuring a destination to:

   #. Send a CSV file to an Azure container, after which it is :ref:`picked up by Azure Synapse Analytics <destination-powerbi-connect-to-azure>`.
   #. Send a CSV file to Google Cloud Storage, after which it is :ref:`transferred to Google BigQuery <destination-powerbi-connect-to-google-bigquery>`
   #. Send data directly :ref:`to a Snowflake data warehouse <destination-powerbi-connect-to-snowflake>`.

   Microsoft Power BI may be configured to connect directly to Snowflake, Google BigQuery, or Azure Synapse Analytics. The destination workflow in Amperity may be configured to send data on a regular basis to ensure that the data available to the Microsoft Power BI user is up to date.

.. destination-powerbi-important-end


.. _destination-powerbi-connect-to-azure:

Connect to Azure Synapse Analytics
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-synapse-analytics-start
   :end-before: .. term-azure-synapse-analytics-end

.. destination-powerbi-connect-to-azure-start

Amperity can be configured to send data to an Azure container, after which Azure Synapse Analytics can be configured to load that data. Microsoft Power BI can be configured to connect to Azure Synapse Analytics and use the Amperity output as a data source.

You may use the Azure Blob Storage container that comes with your Amperity tenant for the intermediate step (if your Amperity tenant is running on Azure). Or you may configure Amperity to send data to an Azure container that your organization manages directly.

.. destination-powerbi-connect-to-azure-end

**To connect Microsoft Power BI to Azure Synapse Analytics**

.. destination-powerbi-connect-to-azure-synapse-analytics-steps-start

The steps required to configure Amperity to send data that is accessible to Microsoft Power BI from Azure Synapse Analytics requires completion of a series of short workflows, some of which must be done outside of Amperity.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Send CSV data to an :doc:`Azure Blob Storage <destination_azure_blob_storage>` container from Amperity.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - `Load CSV data from Azure Blob Storage <https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/develop-tables-external-tables?tabs=sql-pool>`__ |ext_link| to Azure Synapse Analytics.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - `Connect Microsoft Power BI <https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/tutorial-connect-power-bi-desktop>`__ |ext_link| to an Azure Synapse Analytics workspac, and then access the data sent from Amperity.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Validate the workflow within Amperity and the data within Microsoft Power BI.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - Configure Amperity to automate this workflow for a regular (daily) refresh of data.

.. destination-powerbi-connect-to-azure-synapse-analytics-steps-end


.. _destination-powerbi-connect-to-google-bigquery:

Connect to Google BigQuery
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-bigquery-start
   :end-before: .. term-google-bigquery-end

.. destination-powerbi-connect-to-google-bigquery-start

Amperity can be configured to send data to Google Cloud Storage, after which Google BigQuery can be configured to load that data. Power BI can be configured to connect to Google BigQuery and use the Amperity output as a data source.

You must configure Amperity to send data to a Cloud Storage bucket that your organization manages directly.

.. destination-powerbi-connect-to-google-bigquery-end

**To connect Power BI to Google BigQuery**

.. destination-powerbi-connect-to-google-bigquery-steps-start

The steps required to configure Amperity to send data that is accessible to Power BI from Google BigQuery requires completion of a series of short workflows, some of which must be done outside of Amperity.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Send CSV data to :doc:`Google Cloud Storage <destination_google_cloud_storage>` from Amperity.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - `Transfer data from Cloud Storage <https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer>`__ |ext_link| to Google BigQuery.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - `Connect Microsoft Power BI to Google BigQuery <https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-connect-bigquery>`__ |ext_link|, and then access the data sent from Amperity.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Validate the workflow within Amperity and the data within Microsoft Power BI.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - Configure Amperity to automate this workflow for a regular (daily) refresh of data.

.. destination-powerbi-connect-to-google-bigquery-steps-end


.. _destination-powerbi-connect-to-snowflake:

Connect to Snowflake
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-snowflake-start
   :end-before: .. term-snowflake-end

.. destination-powerbi-connect-to-snowflake-start

Amperity can be configured to share data (tables and/or entire databases) directly with Snowflake. Microsoft Power BI can be configured to connect to a Snowflake data warehouse and use that data as a data source.

Amperity offers additional services that allow Amperity to run as the Amperity Data Warehouse, which is synchronized to your Amperity tenant. (This is, currently, run as a Snowflake data warehouse that is accessible to only your Amperity tenant.) Microsoft Power BI is configured to connect directly to the Amperity Data Warehouse. Or you may send data directly to Snowflake by configuring the Snowflake destination to send data to your Snowflake tenant.

.. destination-powerbi-connect-to-snowflake-end

**To connect Microsoft Power BI to Snowflake**

.. destination-powerbi-connect-to-snowflake-steps-start

The steps required to configure Amperity to send data that is accessible to Microsoft Power BI from a Snowflake data warehouse requires completion of a series of short workflows, some of which must be done outside of Amperity.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Configure Snowflake objects for the correct database, tables, roles, and users. (Refer to the :ref:`Amazon S3 <destination-snowflake-aws-configure-objects>` or :ref:`Azure <destination-snowflake-azure-configure-objects>` tutorial, as appropriate for your tenant.)

       .. note:: Snowflake can be configured to run in Amazon AWS or Azure. When using the Amazon Data Warehouse you will use the same cloud platform as your Amperity tenant. When using your own instance of Snowflake, you should use the same Amazon S3 bucket or Azure Blob Storage container that is included with your tenant when configuring Snowflake for data sharing, but then connect Microsoft Power BI directly to your own instance of Snowflake.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Send data to Snowflake from Amperity. (Refer to the :doc:`Amazon S3 <destination_snowflake_aws>` or :doc:`Azure <destination_snowflake_azure>` tutorial, as appropriate for your tenant.)


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Connect Microsoft Power BI to Snowflake, and then access the data sent from Amperity. This connection may be from the `Power BI Desktop <https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-connect-snowflake>`__ |ext_link| or from the `Power BI Service <https://docs.microsoft.com/en-us/power-bi/connect-data/service-connect-snowflake>`__ |ext_link|.

       .. note:: The URL for the Snowflake data warehouse, the Snowflake username, the password, and the name of the Snowflake data warehouse are sent to the Microsoft Power BI user within a SnapPass link. Request this information from your Amperity representative prior to attempting to connect Microsoft Power BI to Snowflake.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Validate the workflow within Amperity and the data within Microsoft Power BI.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - Configure Amperity to automate this workflow for a regular (daily) refresh of data.

.. destination-powerbi-connect-to-snowflake-steps-end
