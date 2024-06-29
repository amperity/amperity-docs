.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        About JSON files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About JSON files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: JSON

==================================================
File format: JSON
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-json-start
   :end-before: .. term-json-end

.. format-json-streaming-ingest-start

.. note:: This topic is about standalone JSON files. JSON data that is sent to the |api_streaming_ingest| is converted to :doc:`NDJSON format <format_ndjson>`.

.. format-json-streaming-ingest-end


.. _format-json-pull:

Pull JSON files
==================================================

.. format-json-pull-start

To pull JSON files to Amperity:

#. Select a :ref:`filedrop data source <format-ndjson-pull-data-sources>`.
#. Use an :ref:`ingest query <format-ndjson-pull-ingest-queries>` to select fields from the JSON file to pull to Amperity.
#. Configure a courier for :ref:`the location and name of the JSON file <format-ndjson-pull-couriers-load-settings>`, and then for :ref:`the name of an ingest query <format-ndjson-pull-couriers-load-operations>`.
#. Define a :ref:`feed to associate the fields that were selected from the JSON file with semantic tags <format-ndjson-pull-feed>` for customer profiles and interactions, as necessary.

.. format-json-pull-end


.. _format-json-pull-data-sources:

Data sources
--------------------------------------------------

.. format-json-pull-data-sources-start

Pull JSON files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-json-pull-data-sources-end


.. _format-json-pull-data-sources-recommendations:

Recommendations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-json-pull-data-sources-recommendations-start

.. TODO: See .. sources-filedrop-file-format-json-start

When using JSON files, it is recommend to:

* Do use simple nested data structures; do not use nested array data structures

  **DO**

  .. code-block:: json

     {
       "employee":{ "name":"John", "age":30, "city":"New York" }
     }

  **DO NOT**

  .. code-block:: json

     {
       "employees":[ "John", "Anna", "Peter" ]
     }

* Quote string data
* Quote date values and use the supported date format
* Ensure numeric data is not quoted
* Encode files in UTF-8 or UTF-16. Amperity automatically detects the 2-byte header present with the UTF-16 encoding format. If the 2-byte header is missing, the file is treated as UTF-8.

  .. caution::

     .. include:: ../../shared/file-formats.rst
        :start-after: .. formats-json-rfc-8259-start
        :end-before: .. formats-json-rfc-8259-end

* Compress files prior to encryption using ZIP, GZIP, and/or TAR
* Encrypt files using PGP; compression will not reduce the size of an encrypted file

.. format-json-pull-data-sources-recommendations-end


.. _format-json-pull-ingest-queries:

Ingest queries
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-json-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the JSON file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. format-json-pull-ingest-queries-end


.. _format-json-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-json-pull-couriers-start

A courier must specify the location of the JSON file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-json-pull-couriers-load-settings>`
#. :ref:`Load operations <format-json-pull-couriers-load-operations>`

.. format-json-pull-couriers-end


.. _format-json-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-json-pull-couriers-load-settings-start

Use courier load settings to specify the path to the JSON file, a file tag (which can be the same as the name of the JSON file), and the ``"application/json"`` content type.

.. format-json-pull-couriers-load-settings-end

.. format-json-pull-couriers-load-settings-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.json'",
     "object/land-as": {
        "file/tag": "FILE_NAME",
        "file/content-type": "application/json"
     }
   },

.. format-json-pull-couriers-load-settings-block-end


.. _format-json-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-json-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings, and the name of the ingest query.

.. format-json-pull-couriers-load-operations-end

.. format-json-pull-couriers-load-operations-block-start

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

.. format-json-pull-couriers-load-operations-block-end


.. _format-json-pull-feed:

Feeds
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-json-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-json-pull-feeds-end

.. format-json-pull-feeds-important-start

.. important:: A feed will use the first record in a JSON file to determine its schema in the **Feed Editor**. If records contain optional fields and those records are *not the first record* you must add those fields to the feed definition manually.

.. format-json-pull-feeds-important-end


.. _format-json-destination:

Send JSON files
==================================================

.. format-json-destination-links-start

Amperity can send JSON files to downstream workflows using any filedrop destination:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-json-destination-links-end
