.. https://docs.amperity.com/user/


.. |destination-name| replace:: Microsoft Power BI
.. |plugin-name| replace:: Microsoft Power BI
.. |what-send| replace:: data


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Microsoft Power BI.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Microsoft Power BI.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Microsoft Power BI

==================================================
Send query results to Microsoft Power BI
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-powerbi-start
   :end-before: .. term-microsoft-powerbi-end

.. sendto-powerbi-important-start

.. important:: Data is not sent from Amperity directly to Microsoft Power BI. Microsoft Power BI must connect to a location that supports queries to that data and cannot connect directly to a static file. Amperity must send data to Microsoft Power BI indirectly by configuring a destination to:

   #. Send a CSV file to an Azure container, after which it is :ref:`picked up by Azure Synapse Analytics <sendto-powerbi-connect-to-azure>`.
   #. Send a CSV file to Google Cloud Storage, after which it is :ref:`transferred to Google BigQuery <sendto-powerbi-connect-to-google-bigquery>`

   Microsoft Power BI may be configured to connect directly to Snowflake, Google BigQuery, or Azure Synapse Analytics. The destination workflow in Amperity may be configured to send data on a regular basis to ensure that the data available to the Microsoft Power BI user is up to date.

.. sendto-powerbi-important-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending query results to |destination-name|.


.. _sendto-powerbi-connect-to-azure:

Connect to Azure Synapse Analytics
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-synapse-analytics-start
   :end-before: .. term-azure-synapse-analytics-end

.. sendto-powerbi-connect-to-azure-start

Amperity can be configured to send data to an Azure container, after which Azure Synapse Analytics can be configured to load that data. Microsoft Power BI can be configured to connect to Azure Synapse Analytics and use the Amperity output as a data source.

You may use the Azure Blob Storage container that comes with your Amperity tenant for the intermediate step (if your Amperity tenant is running on Azure). Or you may configure Amperity to send data to an Azure container that your organization manages directly.

.. sendto-powerbi-connect-to-azure-end

**To connect Microsoft Power BI to Azure Synapse Analytics**

.. sendto-powerbi-connect-to-azure-synapse-analytics-steps-start

The steps required to configure Amperity to send data that is accessible to Microsoft Power BI from Azure Synapse Analytics requires completion of a series of short workflows, some of which must be done outside of Amperity.

#. Send CSV data to an :doc:`Azure Blob Storage <destination_azure_blob_storage>` container from Amperity.
#. `Load CSV data from Azure Blob Storage <https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/develop-tables-external-tables?tabs=sql-pool>`__ |ext_link| to Azure Synapse Analytics.
#. `Connect Microsoft Power BI <https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/tutorial-connect-power-bi-desktop>`__ |ext_link| to an Azure Synapse Analytics workspace, and then access the data sent from Amperity.
#. Validate the workflow within Amperity and the data within Microsoft Power BI.
#. Configure Amperity to automate this workflow for a regular (daily) refresh of data.

.. sendto-powerbi-connect-to-azure-synapse-analytics-steps-end


.. _sendto-powerbi-connect-to-google-bigquery:

Connect to Google BigQuery
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-bigquery-start
   :end-before: .. term-google-bigquery-end

.. sendto-powerbi-connect-to-google-bigquery-start

Amperity can be configured to send data to Google Cloud Storage, after which Google BigQuery can be configured to load that data. Power BI can be configured to connect to Google BigQuery and use the Amperity output as a data source.

You must configure Amperity to send data to a Cloud Storage bucket that your organization manages directly.

.. sendto-powerbi-connect-to-google-bigquery-end

**To connect Power BI to Google BigQuery**

.. sendto-powerbi-connect-to-google-bigquery-steps-start

The steps required to configure Amperity to send data that is accessible to Power BI from Google BigQuery requires completion of a series of short workflows, some of which must be done outside of Amperity.

#. Send CSV data to :doc:`Google Cloud Storage <destination_google_cloud_storage>` from Amperity.
#. `Transfer data from Cloud Storage <https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer>`__ |ext_link| to Google BigQuery.
#. `Connect Microsoft Power BI to Google BigQuery <https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-connect-bigquery>`__ |ext_link|, and then access the data sent from Amperity.
#. Validate the workflow within Amperity and the data within Microsoft Power BI.
#. Configure Amperity to automate this workflow for a regular (daily) refresh of data.

.. sendto-powerbi-connect-to-google-bigquery-steps-end
