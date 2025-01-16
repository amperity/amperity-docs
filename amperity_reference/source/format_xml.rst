.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About XML files, when used as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About XML files, when used as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: XML

==================================================
File format: XML
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-xml-start
   :end-before: .. term-xml-end

.. format-xml-streaming-ingest-start

.. note:: This topic is about standalone XML files. XML data that is sent to the |api_streaming_ingest| is converted to :doc:`CBOR format <format_cbor>`.

.. format-xml-streaming-ingest-end


.. _format-xml-pull:

Pull XML files
==================================================

.. format-xml-pull-start

To pull XML files to Amperity:

#. Select a :ref:`filedrop data source <format-xml-pull-data-sources>`.
#. Use a :ref:`ingest query <format-xml-pull-ingest-queries>` to select fields from the XML file to pull to Amperity.
#. Configure a courier for :ref:`the location and name of the XML file <format-xml-pull-couriers-load-settings>`, and then for :ref:`the name of an ingest query <format-xml-pull-couriers-load-operations>`.
#. Define a :ref:`feed to associate the fields that were selected from the XML file with semantic tags <format-xml-pull-feed>` for customer profiles and interactions, as necessary.

.. format-xml-pull-end


.. _format-xml-pull-data-sources:

Data sources
--------------------------------------------------

.. format-xml-pull-data-sources-start

Pull XML files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-xml-pull-data-sources-end


.. _format-xml-pull-ingest-queries:

Ingest queries
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-xml-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the XML file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. format-xml-pull-ingest-queries-end


.. _format-xml-pull-ingest-queries-explode-interactions:

Explode interactions data
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-explode-example-load-xml-as-ingest-query-start
   :end-before: .. sql-spark-function-explode-example-load-xml-as-ingest-query-end


.. _format-xml-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-xml-pull-couriers-start

A courier must specify the location of the XML file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-xml-pull-couriers-load-settings>`
#. :ref:`Load operations <format-xml-pull-couriers-load-operations>`

.. format-xml-pull-couriers-end


.. _format-xml-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-xml-pull-couriers-load-settings-start

Use courier load settings to specify the path to the XML file, a file tag (which can be the same as the name of the XML file), and the ``"application/xml"`` content type.

.. format-xml-pull-couriers-load-settings-end

.. format-xml-pull-couriers-load-settings-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.xml'",
     "object/land-as": {
       "file/tag": "FILE_NAME",
       "file/content-type": "application/xml"
     }
   }

.. format-xml-pull-couriers-load-settings-block-end


.. _format-xml-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-xml-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings, the element within the XML schema to be treated as a row in a table, and the name of the ingest query.

.. format-xml-pull-couriers-load-operations-end

.. format-xml-pull-couriers-load-operations-block-start

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
             }
           }
         ],
         "spark-sql-query": "INGEST_QUERY_NAME"
       }
     ]
   }

.. format-xml-pull-couriers-load-operations-block-end

.. format-xml-pull-couriers-load-operations-rowtag-start

.. tip:: Set ``ROW`` to the element in the XML schema that should be treated as a row in a table. For example, if the XML schema contained:

   .. code-block:: none

      <salesTransactions>
        <salesTransaction> ... </salesTransaction>
      </salesTransactions>

   then use ``salesTransaction`` as the value for ``rowTag``. The default value is ``row``.

   .. code-block:: none

      {
        "df-5Jagkabc": [
          {
            "type": "spark-sql",
            "spark-sql-files": [
              {
                "file": "PosXml",
                "options": {
                  "rowTag": "salesTransaction"
                }
              }
            ],
            "spark-sql-query": "API_Test_Headers"
          }
        ]
      }

.. format-xml-pull-couriers-load-operations-rowtag-start


.. _format-xml-pull-feed:

Feeds
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-xml-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-xml-pull-feeds-end


.. _format-xml-destination:

Send XML files
==================================================

.. format-xml-destination-start

.. important:: Amperity does not send XML files to downstream workflows.

.. format-xml-destination-end
