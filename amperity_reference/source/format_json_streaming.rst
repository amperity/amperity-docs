.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        About using streaming JSON files as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About using streaming JSON files as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: Streaming JSON

==================================================
File format: Streaming JSON
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-streaming-json-start
   :end-before: .. term-streaming-json-end


.. _format-json-streaming-pull:

Pull streaming JSON files
==================================================

.. format-json-streaming-pull-start

To pull streaming JSON files to Amperity:

#. Select a :ref:`filedrop data source <format-json-streaming-pull-data-sources>`.
#. Use an :ref:`ingest query <format-json-streaming-pull-ingest-queries>` to select fields from the streaming JSON file to pull to Amperity.
#. Configure a courier for :ref:`the location and name of the streaming JSON file <format-json-streaming-pull-couriers-load-settings>`, and then for :ref:`the name of an ingest query <format-json-streaming-pull-couriers-load-operations>`.
#. Define a :ref:`feed to associate the fields that were selected from the streaming JSON file with semantic tags <format-json-streaming-pull-feed>` for customer profiles and interactions, as necessary.

.. format-json-streaming-pull-end


.. _format-json-streaming-pull-data-sources:

Data sources
--------------------------------------------------

.. format-json-streaming-pull-data-sources-start

Pull streaming JSON files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-json-streaming-pull-data-sources-end


.. _format-json-streaming-pull-ingest-queries:

Ingest queries
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-json-streaming-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the streaming JSON file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. format-json-streaming-pull-ingest-queries-end


.. _format-json-streaming-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-json-streaming-pull-couriers-start

A courier must specify the location of the streaming JSON file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-json-streaming-pull-couriers-load-settings>`
#. :ref:`Load operations <format-json-streaming-pull-couriers-load-operations>`

.. format-json-streaming-pull-couriers-end


.. _format-json-streaming-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-json-streaming-pull-couriers-load-settings-start

Use courier load settings to specify the path to the streaming JSON file, a file tag (which can be the same as the name of the streaming JSON file), and the ``"application/x-json-stream"`` content type.

.. format-json-streaming-pull-couriers-load-settings-end

.. format-json-streaming-pull-couriers-load-settings-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.ndjson'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/content-type": "application/x-json-stream"
     }
   },

.. format-json-streaming-pull-couriers-load-settings-block-end


.. _format-json-streaming-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-json-streaming-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings, and the name of the ingest query.

.. format-json-streaming-pull-couriers-load-operations-end

.. format-json-streaming-pull-couriers-load-operations-block-start

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

.. format-json-streaming-pull-couriers-load-operations-block-end


.. _format-json-streaming-pull-feed:

Feeds
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-json-streaming-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-json-streaming-pull-feeds-end


.. _format-json-streaming-destination:

Send streaming JSON files
==================================================

.. format-json-streaming-destination-start

.. important:: Amperity does not send streaming JSON files to downstream workflows.

.. format-json-streaming-destination-end
