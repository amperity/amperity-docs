.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        About Apache Parquet files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About Apache Parquet files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: Apache Parquet

==================================================
File format: Apache Parquet
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-apache-parquet-start
   :end-before: .. term-apache-parquet-end

.. format-parquet-start

Apache Parquet may be used with any upstream or downstream customer environment that supports the use of Parquet. Parquet is highly compact and can be transferred easily. Parquet embeds data-typing and avoids escape character and data formatting issues that can be present in other formats like CSV and TSV. 

.. format-parquet-end


.. _format-parquet-pull:

Pull Parquet files
==================================================

.. format-parquet-pull-start

To pull Parquet files to Amperity:

#. Select a :ref:`filedrop data source <format-parquet-pull-data-sources>`.
#. Define a :ref:`feed to associate fields in the Parquet file with semantic tags <format-parquet-pull-feeds>`; in some situations you may need to use an :ref:`ingest query to transform data in the Parquet file <format-parquet-pull-ingest-queries>` prior to loading it to Amperity.
#. Configure a courier for :ref:`the location and name of the Parquet file <format-parquet-pull-couriers-load-settings>`, and then for :ref:`the name of an ingest query <format-parquet-pull-couriers-load-operations>`.

.. format-parquet-pull-end

.. format-parquet-zstd-start

.. note:: The Zstandard (zstd) commpression scheme is not supported when ingesting Apache Parquet files.

.. format-parquet-zstd-start


.. _format-parquet-pull-data-sources:

Data sources
--------------------------------------------------

.. format-parquet-pull-data-sources-start

Pull Apache Parquet files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-parquet-pull-data-sources-end


.. _format-parquet-pull-load-data:

Load data
--------------------------------------------------

.. format-parquet-pull-load-data-start

For most Parquet files, use a feed to associate fields in the Parquet file with semantic tags. In some situations, an ingest query may be necessary to transform data prior to loading it to Amperity.

* :ref:`Feeds <format-parquet-pull-feeds>`
* :ref:`Ingest queries <format-parquet-pull-ingest-queries>`

.. format-parquet-pull-load-data-end


.. _format-parquet-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-parquet-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-parquet-pull-feeds-end


.. _format-parquet-pull-ingest-queries:

Ingest queries
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-parquet-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the Parquet file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. format-parquet-pull-ingest-queries-end


.. _format-parquet-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-parquet-pull-couriers-start

A courier must specify the location of the Parquet file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-parquet-pull-couriers-load-settings>`
#. :ref:`Load operations <format-parquet-pull-couriers-load-operations>`

.. format-parquet-pull-couriers-end


.. _format-parquet-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-parquet-pull-couriers-load-settings-start

Use courier load settings to specify the path to the Parquet file, a file tag (which can be the same as the name of the Parquet file), and the ``"application/x-parquet"`` content type.

.. format-parquet-pull-couriers-load-settings-end

.. format-parquet-pull-couriers-load-settings-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.parquet/'",
     "object/land-as": {
       "file/tag": "FILE_NAME",
       "file/content-type": "application/x-parquet"
     }
   }

.. format-parquet-pull-couriers-load-settings-block-end

.. format-parquet-pull-couriers-load-settings-partition-start

.. note:: Apache Parquet files are almost always partitioned, where a single logical Parquet file is comprised of multiple physical files in a directory structure, each of them representing a partition.

   Parquet partitioning optionally permits for data to be nested in a directory structure determined by the value of partitioning columns. Amperity only detects Parquet partition files one directory level below the configured file pattern. For example:

   .. code-block:: none

       "path/to/file-YYYY-MM-dd.parquet/part-0000.parquet"

.. format-parquet-pull-couriers-load-settings-partition-end


.. _format-parquet-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-parquet-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings. Load operations for an ingest query may specify a series of options.

.. format-parquet-pull-couriers-load-operations-end


.. _format-parquet-pull-couriers-load-operations-feed:

Load from feed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-parquet-pull-couriers-load-operations-feed-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "OPERATION",
         "file": "FILE_NAME"
       }
     ]
   }

.. format-parquet-pull-couriers-load-operations-feed-end


.. _format-parquet-pull-couriers-load-operations-ingest-query:

Load from ingest query
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-parquet-pull-couriers-load-operations-ingest-query-start

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

.. format-parquet-pull-couriers-load-operations-ingest-query-end


.. _format-parquet-destination:

Send Parquet files
==================================================

.. format-parquet-destination-start

Apache Parquet is the recommended format for any customer environment that supports the use of Parquet. This is because Parquet data embeds data-typing and avoids escape character and data formatting issues that can be present in other formats like CSV and TSV formats. Parquet is highly compact--file sizes can be up to 20 times smaller--and a format that systems can load and use quickly.

.. format-parquet-destination-end

.. format-parquet-destination-context-start

Amperity overwrites Apache Parquet files when they are sent to the same location.

.. format-parquet-destination-context-end

.. format-parquet-destination-note-start

.. tip:: By default, Amperity uses Snappy to compress Apache Parquet files prior to sending them to a destination. If you do not need PGP encryption or output as a single file, you should not use compression.

.. format-parquet-destination-note-end

.. format-parquet-destination-warning-start

.. note:: A folder is created with one (or more) files unless Parquet files are configured to be compressed/archived during orchestration.

.. format-parquet-destination-warning-end

.. format-parquet-destination-links-start

Amperity can send Apache Parquet files to downstream workflows using any filedrop destination:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-parquet-destination-links-end


.. _format-parquet-destination-directories:

Configure Parquet directories
--------------------------------------------------

.. format-parquet-destination-directories-start

The filename template defines the name of the directory into which Apache Parquet files are placed. By default, Amperity appends ".parquet" to the name of the directory. You can configure Amperity to omit ".parquet" from the name using the **Exclude Parquet extension from the directory name** setting when configuring a destination that supports sending Apache Parquet files from Amperity, including many SFTP sites, Amazon S3, Azure Blob Storage, and Google Cloud Storage.

.. format-parquet-destination-directories-end
