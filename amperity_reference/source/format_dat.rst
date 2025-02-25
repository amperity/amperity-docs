.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About DAT files, when used as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About DAT files, when used as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: DAT

==================================================
File format: DAT
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dat-start
   :end-before: .. term-dat-end

.. format-dat-important-start

.. important:: This topic exists to show that, in addition to handling Apache Avro, Apache Parquet, CSV, JSON, NDJSON, PSV, TSV, and XML files, Amperity is also capable of collecting data from non-standard data sources.

.. format-dat-important-end

.. format-dat-note-start

.. note:: You can use an ingest query to parse individual fields out of a DAT file, and then configure a courier to load that query. Rename the fields in the ingest query, in a feed, or by using domain SQL.

.. format-dat-note-end


.. _format-dat-pull:

Pull DAT files
==================================================

.. format-dat-pull-start

To pull DAT files to Amperity:

#. Select a :ref:`filedrop data source <format-dat-pull-data-sources>`.
#. Use an :ref:`ingest query <format-dat-pull-ingest-queries>` to parse the fields in the DAT file.
#. Configure a courier for :ref:`the location and name of the DAT file <format-dat-pull-couriers-load-settings>`, and then for :ref:`the name of an ingest query <format-dat-pull-couriers-load-operations>`.
#. Define a :ref:`feed to associate the fields that were selected from the DAT file with semantic tags <format-dat-pull-feed>` for customer profiles and interactions or use domain SQL to transform this data into a shape that is usable within Amperity.

.. format-dat-pull-end


.. _format-dat-pull-data-sources:

Data sources
--------------------------------------------------

.. format-dat-pull-data-sources-start

Pull DAT files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-dat-pull-data-sources-end


.. _format-dat-pull-ingest-queries:

Ingest queries
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-dat-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the DAT file that parses the individual fields. This can be done using the **SUBSTR()** function to identify the positions for each field within the DAT file. Use other functions, such as **TRIM()** and **NULLIF()** as necessary to ensure the data that is parsed from the DAT file is as clean as possible. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. format-dat-pull-ingest-queries-end

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-substr-example-parse-fields-from-dat-file-start
   :end-before: .. sql-spark-function-substr-example-parse-fields-from-dat-file-end

.. format-dat-pull-ingest-queries-important-start

.. important:: Verify the fields that are parsed from the DAT file to ensure they contain correct values and have column names that represent the values they contain. In addition, be sure to verify that the feed is able to apply semantic tags to customer records and/or interactions records, and that the data is represented correctly downstream within Amperity by Stitch, within the customer 360 database, and as the data may be used within queries and segments.

.. format-dat-pull-ingest-queries-important-end


.. _format-dat-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-dat-pull-couriers-start

A courier must specify the location of the DAT file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-dat-pull-couriers-load-settings>`
#. :ref:`Load operations <format-dat-pull-couriers-load-operations>`

.. format-dat-pull-couriers-end


.. _format-dat-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-dat-pull-couriers-load-settings-start

Use courier load settings to specify the path to the DAT file, a file tag (which can be the same as the name of the DAT file). Use the ``"text/csv"`` content type. Set ``"file/header-rows"`` to ``0``.

.. format-dat-pull-couriers-load-settings-end

.. format-dat-pull-couriers-load-settings-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.dat'",
     "object/land-as": {
        "file/header-rows": 0,
        "file/tag": "FILE_NAME",
        "file/content-type": "text/csv"
     }
   },

.. format-dat-pull-couriers-load-settings-block-end


.. _format-dat-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-dat-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings, the column defined in the ingest query to represent the DAT schema, and the name of the ingest query.

.. format-dat-pull-couriers-load-operations-end

.. format-dat-pull-couriers-load-operations-block-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "spark-sql",
         "spark-sql-files": [
           {
             "file": "FILE_NAME",
             "schema": {
               "fields": [
                 {
                   "metadata": {},
                   "name": "_c0",
                   "type": "string",
                   "nullable": true
                 },
                 "type": "struct"
               }
             ]
           }
         ],
         "spark-sql-query": "INGEST_QUERY_NAME"
       }
     ]
   }

.. format-dat-pull-couriers-load-operations-block-end

.. format-dat-pull-couriers-load-operations-schema-start

.. important:: Use a single ordinal column to define the ``"schema"`` of a DAT file.

.. format-dat-pull-couriers-load-operations-schema-start


.. _format-dat-pull-feed:

Feeds
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-dat-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-dat-pull-feeds-end


.. _format-dat-destination:

Send DAT files
==================================================

.. format-dat-destination-start

.. important:: Amperity does not send DAT files to downstream workflows.

.. format-dat-destination-end
