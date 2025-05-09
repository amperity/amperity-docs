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
        Configure destination for Google BigQuery

==================================================
Configure destination for Google BigQuery
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

* Load `Parquet files <https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet>`__ |ext_link| from Cloud Storage to Google BigQuery.
* Load `CSV files <https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv>`__ |ext_link| from Cloud Storage to Google BigQuery.
* Transfer Parquet and CSV `files from Amazon S3 <https://cloud.google.com/bigquery-transfer/docs/s3-transfer>`__ |ext_link| to Google BigQuery.

.. destination-google-bigquery-configure-end


.. _destination-google-bigquery-downstream:

Enable downstream workflows
==================================================

.. destination-google-bigquery-downstream-start

Loading data to Google BigQuery enables downstream workflows, including the use of applications like:

* `Google Analytics Hub <https://cloud.google.com/bigquery/docs/analytics-hub-introduction>`__ |ext_link|
* `Google Pub/Sub <https://cloud.google.com/pubsub/docs/overview>`__ |ext_link| to support or enable real-time downstream workflows
* :ref:`Microsoft Power BI <destination-powerbi-connect-to-google-bigquery>`
* :doc:`Tableau <destination_tableau_google_big_query>`

.. destination-google-bigquery-downstream-end
