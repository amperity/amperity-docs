.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About Apache Parquet files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About Apache Parquet files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        Apache Parquet files

==================================================
Apache Parquet files
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
#. Configure a courier for :ref:`the location and name of the Parquet file <format-parquet-pull-couriers>`.
#. Define a :ref:`feed to associate fields in the Parquet file with semantic tags <format-parquet-pull-feeds>`.

.. format-parquet-pull-end

.. format-parquet-zstd-start

.. note:: The Zstandard (zstd) commpression scheme is not supported when ingesting Apache Parquet files.

.. format-parquet-zstd-start


.. _format-parquet-pull-data-sources:

Data sources
--------------------------------------------------

.. format-parquet-pull-data-sources-start

Pull Apache Parquet files to Amperity using one of the following data sources:

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

Use a feed to associate fields in the Apache Parquet file with semantic tags and a courier to pull the Apache Parquet file from its upstream data source.

* :ref:`Couriers <format-parquet-pull-couriers>`
* :ref:`Feeds <format-parquet-pull-feeds>`

.. format-parquet-pull-load-data-end


.. _format-parquet-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-parquet-pull-couriers-start

A courier must specify the location of the Apache Parquet file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-parquet-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-parquet-pull-couriers-feed-selection>`

.. format-parquet-pull-couriers-end


.. _format-parquet-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-parquet-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the Apache Parquet file and to define formatting within the file.

.. format-parquet-pull-couriers-file-settings-start

.. format-parquet-pull-couriers-load-settings-partition-start

.. note:: Apache Parquet files are partitioned, where a single logical Parquet file is comprised of multiple physical files in a directory structure, each of them representing a partition.

   Parquet partitioning optionally permits for data to be nested in a directory structure determined by the value of partitioning columns. Amperity only detects Parquet partition files one directory level below the configured file pattern. For example:

   .. code-block:: none

       "path/to/file-YYYY-MM-dd.parquet/part-0000.parquet"

.. format-parquet-pull-couriers-load-settings-partition-end


.. _format-parquet-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-parquet-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Spark** Use this option to load data when the Apache Parquet file contains complex types, such as **structs**, **arrays**, or **maps**.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-parquet-pull-couriers-feed-selection-end


.. _format-parquet-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-parquet-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-parquet-pull-feeds-end


.. _format-parquet-destination:

Send Parquet files
==================================================

.. format-parquet-destination-start

Apache Parquet is the recommended format for any customer environment that supports the use of Parquet. This is because Parquet data embeds data-typing and avoids escape character and data formatting issues that can be present in other formats like CSV and TSV formats. Parquet is highly compact--file sizes can be up to 20 times smaller--and is a fast loading format.

.. format-parquet-destination-end

.. format-parquet-destination-context-start

Amperity overwrites Apache Parquet files when they are sent to the same location.

.. format-parquet-destination-context-end

.. format-parquet-destination-note-start

.. tip:: By default, Amperity uses Snappy to compress Apache Parquet files prior to sending them to a destination. If you do not need PGP encryption or output as a single file, you should not use compression.

.. format-parquet-destination-note-end

.. format-parquet-destination-warning-start

.. note:: A folder is created with one or more files unless Parquet files are configured to be compressed/archived during orchestration.

.. format-parquet-destination-warning-end

.. format-parquet-destination-links-start

Amperity can send Apache Parquet files to downstream workflows any of the following destinations:

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
