.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |destination-name| replace:: Azure Synapse Analytics
.. |what-send| replace:: Apache Parquet files and delimited files (CSV, TSV, or PSV)
.. |filter-the-list| replace:: "az"
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


.. meta::
    :description lang=en:
        Configure Amperity to send data to Azure Synapse Analytics.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Azure Synapse Analytics.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Azure Synapse Analytics

==================================================
Send data to Azure Synapse Analytics
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-synapse-analytics-start
   :end-before: .. term-azure-synapse-analytics-end

.. destination-azure-synapse-steps-to-send-start

This topic describes how to configure Amperity to send files to a cloud storage destination, load data from that destination to Azure Synapse Analytics, and then enable downstream applications and workflows.

.. destination-azure-synapse-steps-to-send-end


.. _destination-azure-synapse-add-cloud-storage-destination:

Add cloud storage destination
==================================================

.. destination-azure-synapse-add-cloud-storage-destination-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

* Send the data to :doc:`Amazon S3 <destination_amazon_s3>`.
* Send the data to :doc:`Azure Blob Storage <destination_azure_blob_storage>`.
* Send the data to :doc:`Google Cloud Storage <destination_google_cloud_storage>`.

.. destination-azure-synapse-add-cloud-storage-destination-end


.. _destination-azure-synapse-analytics-load:

Load data to Azure Synapse Analytics
==================================================

.. destination-azure-synapse-configure-start

Load data from your preferred cloud storage location to Azure Synapse Analytics.

* |ext_azure_synapse_analytics_load_from_amazon_s3| to Azure Synapse Analytics.
* Use Azure Data Factory to |ext_azure_synapse_analytics_load_from_azure_blob_storage| to Azure Synapse Analytics.
* |ext_azure_synapse_analytics_load_from_cloud_storage| to Azure Synapse Analytics.

.. destination-azure-synapse-configure-end


.. _destination-azure-synapse-downstream:

Enable downstream workflows
==================================================

.. destination-azure-synapse-downstream-start

Loading data to Azure Synapse Analytics enables downstream workflows, including the use of applications like:

* :ref:`Microsoft Power BI <destination-powerbi-connect-to-azure>`
* :doc:`Tableau <destination_tableau_azure_synapse_analytics>`

.. destination-azure-synapse-downstream-end
