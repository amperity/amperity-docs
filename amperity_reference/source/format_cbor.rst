.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        About using CBOR files as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About using CBOR files as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: CBOR

==================================================
File format: CBOR
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-cbor-start
   :end-before: .. term-cbor-end

.. format-cbor-streaming-ingest-start

.. note:: XML data can be sent to the |api_streaming_ingest|, after which it is converted to CBOR format and may be loaded to Amperity using an ingest query that flattens it into a tabular format.

.. format-cbor-streaming-ingest-end


.. _format-cbor-pull:

Pull CBOR files
==================================================

.. format-cbor-pull-start

To pull CBOR files to Amperity:

#. Select a :ref:`filedrop data source <format-cbor-pull-data-sources>` or identify the location at which the Streaming Ingest API has put the CBOR file.
#. Use an :ref:`ingest query <format-cbor-pull-ingest-queries>` to select fields from the CBOR file to pull to Amperity.
#. Configure a courier for :ref:`the location and name of the CBOR file <format-cbor-pull-couriers-load-settings>`, and then for :ref:`the name of an ingest query <format-cbor-pull-couriers-load-operations>`.
#. Define a :ref:`feed to associate the fields that were selected from the CBOR file with semantic tags <format-cbor-pull-feed>` for customer profiles and interactions, as necessary.

.. format-cbor-pull-end


.. _format-cbor-pull-data-sources:

Data sources
--------------------------------------------------

.. format-cbor-pull-data-sources-start

Pull CBOR files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-cbor-pull-data-sources-end


.. _format-cbor-pull-ingest-queries:

Ingest queries
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-cbor-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the CBOR file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. format-cbor-pull-ingest-queries-end


.. _format-cbor-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-cbor-pull-couriers-start

A courier must specify the location of the CBOR file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-cbor-pull-couriers-load-settings>`
#. :ref:`Load operations <format-cbor-pull-couriers-load-operations>`

.. format-cbor-pull-couriers-end


.. _format-cbor-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-cbor-pull-couriers-load-operations-start

Use courier load settings to specify the path to the CBOR file, a file tag (which can be the same as the name of the CBOR file), and the ``"application/ingest-pack+cbor"`` content type.

.. format-cbor-pull-couriers-load-operations-end


.. _format-cbor-pull-couriers-load-settings-aws-block:

for Amazon AWS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-cbor-pull-couriers-load-settings-aws-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'ingest/stream/TENANT/STREAM_ID/'yyyy-MM-dd'/'*'.cbor'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/content-type": "application/ingest-pack+cbor"
     }
   },

.. format-cbor-pull-couriers-load-settings-aws-block-end


.. _format-cbor-pull-couriers-load-settings-azure-block:

for Microsoft Azure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-cbor-pull-couriers-load-settings-azure-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'STREAM_ID/'yyyy-MM-dd'/'*'.cbor'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/content-type": "application/ingest-pack+cbor"
     }
   },

.. format-cbor-pull-couriers-load-settings-azure-block-end


.. _format-cbor-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-cbor-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings, the element within the CBOR schema to be treated as a row in a table, and the name of the ingest query.

.. format-cbor-pull-couriers-load-operations-end

.. format-cbor-pull-couriers-load-operations-block-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "spark-sql",
         "spark-sql-files": [
           {
             "file": "FILE_NAME",
             "options": {
               "rowTag": "row"
             },
             "schema": {
               "fields": [
                 {
                   "metadata": {},
                   "name": "field-1",
                   "type": "string",
                   "nullable": true
                 },
                 ...
                 {
                   "metadata": {},
                   "name": "nested-group-1",
                   "type": {
                     "fields": [
                       {
                         "metadata": {},
                         "name": "field-a",
                         "type": "string",
                         "nullable": true
                       },
                       {
                         "metadata": {},
                         "name": "nested-group-a",
                         "type": {
                           "fields": [
                             ...
                           ],
                           "type": "struct"
                         },
                         "nullable": true
                       },
                       {
                         "metadata": {},
                         "name": "field-xyz",
                         "type": "string",
                         "nullable": true
                       },
                     ],
                     "type": "struct"
                   }
                   "type": "struct"
                 }
                 ...
               }
               ...
             ]
           }
         ],
         "spark-sql-query": "INGEST_QUERY_NAME"
       }
     ]
   }

.. format-cbor-pull-couriers-load-operations-block-end

.. format-cbor-pull-couriers-load-operations-important-start

.. important:: The ``"schema"`` must match the structure of the incoming file, including all nested groupings and data types. Set ``"nullable"`` to ``True`` to allow fields to contain ``NULL`` values. A CBOR file can have hundreds of fields. The ellipses (``...``) in this example represents locations within this example structure where additional fields may be present.

.. format-cbor-pull-couriers-load-operations-important-end

.. format-cbor-pull-couriers-load-operations-rowtag-start

.. tip:: Set ``rowTag`` to the element in the CBOR file that should be treated as a row in a table. The default value is ``row``.

.. format-cbor-pull-couriers-load-operations-rowtag-start


.. _format-cbor-pull-feed:

Feeds
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-cbor-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-cbor-pull-feeds-end


.. _format-cbor-destination:

Send CBOR files
==================================================

.. format-cbor-destination-start

.. important:: Amperity does not send CBOR files to downstream workflows.

.. format-cbor-destination-end
