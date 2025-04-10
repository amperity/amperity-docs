.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google BigQuery
.. |what-send| replace:: files
.. |filter-the-list| replace:: "google"
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


.. meta::
    :description lang=en:
        Configure Amperity to send data to Google BigQuery.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Google BigQuery.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Google BigQuery

==================================================
Send data to Google BigQuery
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-bigquery-start
   :end-before: .. term-google-bigquery-end

.. destination-google-bigquery-steps-to-send-start

This topic describes how to configure Amperity to send files to a cloud storage destination, load data from that destination to Google BigQuery, and then enable downstream applications and workflows.

.. destination-google-bigquery-steps-to-send-end


.. _destination-google-bigquery-add-cloud-storage:

Add Cloud Storage destination
==================================================

.. destination-google-bigquery-add-cloud-storage-start

Send Apache Parquet and CSV files from Amperity to your preferred cloud storage location.

* Send the data to :doc:`Amazon S3 <destination_amazon_s3>`.
* Send the data to :doc:`Google Cloud Storage <destination_google_cloud_storage>`.

.. destination-google-bigquery-add-cloud-storage-end


.. _destination-google-bigquery-configure:

Configure Google BigQuery
==================================================

.. destination-google-bigquery-configure-start

Load your preferred data format from your preferred cloud storage location to Google BigQuery.

* Load |ext_google_bigquery_load_parquet| from Cloud Storage to Google BigQuery.
* Load |ext_google_bigquery_load_csv| from Cloud Storage to Google BigQuery.
* Transfer Parquet and CSV |ext_google_bigquery_load_from_amazon_s3| to Google BigQuery.

.. destination-google-bigquery-configure-end


.. _destination-google-bigquery-downstream:

Enable downstream workflows
==================================================

.. destination-google-bigquery-downstream-start

Loading data to Google BigQuery enables downstream workflows, including the use of applications like:

* |ext_google_analytics_hub|
* |ext_google_pubsub_overview| to support or enable real-time downstream workflows
* :ref:`Microsoft Power BI <destination-powerbi-connect-to-google-bigquery>`
* :doc:`Tableau <destination_tableau_google_big_query>`

.. destination-google-bigquery-downstream-end
