.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Microsoft Power BI
.. |plugin-name| replace:: Microsoft Power BI
.. |what-send| replace:: data
.. |filter-the-list| replace:: "micro"
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


.. meta::
    :description lang=en:
        Configure Amperity to send data to Microsoft Power BI.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Microsoft Power BI.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Microsoft Power BI

==================================================
Configure destinations for Microsoft Power BI
==================================================

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
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Send CSV data to an :doc:`Azure Blob Storage <destination_azure_blob_storage>` container from Amperity.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - `Load CSV data from Azure Blob Storage <https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/develop-tables-external-tables?tabs=sql-pool>`__ |ext_link| to Azure Synapse Analytics.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - `Connect Microsoft Power BI <https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/tutorial-connect-power-bi-desktop>`__ |ext_link| to an Azure Synapse Analytics workspac, and then access the data sent from Amperity.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Validate the workflow within Amperity and the data within Microsoft Power BI.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Configure Amperity to :doc:`automate this workflow <workflows>` for a regular (daily) refresh of data.

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
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Send CSV data to :doc:`Google Cloud Storage <destination_google_cloud_storage>` from Amperity.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - `Transfer data from Cloud Storage <https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer>`__ |ext_link| to Google BigQuery.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - `Connect Microsoft Power BI to Google BigQuery <https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-connect-bigquery>`__ |ext_link|, and then access the data sent from Amperity.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Validate the workflow within Amperity and the data within Microsoft Power BI.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Configure Amperity to :doc:`automate this workflow <workflows>` for a regular (daily) refresh of data.

.. destination-powerbi-connect-to-google-bigquery-steps-end


.. _destination-powerbi-connect-to-snowflake:

Connect to Snowflake
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-snowflake-start
   :end-before: .. term-snowflake-end

.. destination-powerbi-connect-to-snowflake-start

Amperity can be configured to :doc:`share datasets directly with Snowflake <bridge_snowflake>`. Microsoft Power BI can be configured to connect to a Snowflake data warehouse and use that data as a data source.

.. destination-powerbi-connect-to-snowflake-end

**To connect Microsoft Power BI to Snowflake**

.. destination-powerbi-connect-to-snowflake-steps-start

The steps required to configure Amperity to send data that is accessible to Microsoft Power BI from a Snowflake data warehouse requires completion of a series of short workflows, some of which must be done outside of Amperity.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Configure Snowflake to sync data using :doc:`Amperity Bridge <bridge_snowflake>`.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Connect Microsoft Power BI to Snowflake, and then access the data sent from Amperity. This connection may be from the `Power BI Desktop <https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-connect-snowflake>`__ |ext_link| or from the `Power BI Service <https://docs.microsoft.com/en-us/power-bi/connect-data/service-connect-snowflake>`__ |ext_link|.

       .. note:: The URL of the Snowflake data warehouse, the Snowflake username, the password, and the name of the Snowflake data warehouse are sent to the Microsoft Power BI user within a SnapPass link. Request this information from your Amperity representative prior to attempting to connect Microsoft Power BI to Snowflake.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Validate the workflow within Amperity and the data within Microsoft Power BI.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Configure Amperity to :doc:`automate this workflow <workflows>` for a regular (daily) refresh of data.

.. destination-powerbi-connect-to-snowflake-steps-end
