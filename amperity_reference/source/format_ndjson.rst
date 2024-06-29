.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        About NDJSON files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About NDJSON files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: NDJSON

==================================================
File format: NDJSON
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-ndjson-start
   :end-before: .. term-ndjson-end


.. _format-ndjson-pull:

Pull NDJSON files
==================================================

.. format-ndjson-pull-start

To pull NDJSON files to Amperity:

#. Select a :ref:`filedrop data source <format-ndjson-pull-data-sources>`.
#. Use an :ref:`ingest query <format-ndjson-pull-ingest-queries>` to select fields from the NDJSON file to pull to Amperity.
#. Configure a courier for :ref:`the location and name of the NDJSON file <format-ndjson-pull-couriers-load-settings>`, and then for :ref:`the name of an ingest query <format-ndjson-pull-couriers-load-operations>`.
#. Define a :ref:`feed to associate the fields that were selected from the NDJSON file with semantic tags <format-ndjson-pull-feed>` for customer profiles and interactions, as necessary.

.. format-ndjson-pull-end


.. _format-ndjson-pull-data-sources:

Data sources
--------------------------------------------------

.. format-ndjson-pull-data-sources-start

Pull NDJSON files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-ndjson-pull-data-sources-end


.. _format-ndjson-pull-ingest-queries:

Ingest queries
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-ndjson-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for NDJSON files that contain nested data using a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. note:: An ingest query is not required for simple NDJSON files that do not have nested values. Simple NDJSON files may be loaded to a feed directly.

.. format-ndjson-pull-ingest-queries-end


.. _format-ndjson-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-ndjson-pull-couriers-start

A courier must specify the location of the NDJSON file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-ndjson-pull-couriers-load-settings>`
#. :ref:`Load operations <format-ndjson-pull-couriers-load-operations>`

.. format-ndjson-pull-couriers-end


.. _format-ndjson-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-ndjson-pull-couriers-load-settings-start

Use courier load settings to specify the path to the NDJSON file, a file tag (which can be the same as the name of the NDJSON file), and the ``"application/x-ndjson"`` content type.

.. format-ndjson-pull-couriers-load-settings-end

.. format-ndjson-pull-couriers-load-settings-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.ndjson'",
     "object/land-as": {
        "file/tag": "FILE_NAME",
        "file/content-type": "application/x-ndjson"
     }
   },

.. format-ndjson-pull-couriers-load-settings-block-end


.. _format-ndjson-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-ndjson-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings, and the name of the ingest query.

.. format-ndjson-pull-couriers-load-operations-end

.. format-ndjson-pull-couriers-load-operations-block-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "spark-sql",
         "spark-sql-files": [
           {
             "file": "FILE_NAME"
           }
         ],
         "spark-sql-query": "INGEST_QUERY_NAME"
       }
     ]
   }

.. format-ndjson-pull-couriers-load-operations-block-end


.. _format-ndjson-pull-feed:

Feeds
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-ndjson-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-ndjson-pull-feeds-end


.. _format-ndjson-destination:

Send NDJSON files
==================================================

.. format-ndjson-destination-links-start

Amperity can send NDJSON files to downstream workflows using any filedrop destination:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-ndjson-destination-links-end