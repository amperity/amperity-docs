.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        About using Apache Avro files as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About using Apache Avro files as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: Apache Avro

==================================================
File format: Apache Avro
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-apache-avro-start
   :end-before: .. term-apache-avro-end

.. format-avro-start

Apache Avro may be used with any upstream or downstream customer environment that supports the use of Avro. Avro offers the most compact file format available for use with Amperity.

.. format-avro-end


.. _format-avro-pull:

Pull Avro files
==================================================

.. format-avro-pull-start

To pull Avro files to Amperity:

#. Select a :ref:`filedrop data source <format-avro-pull-data-sources>`.
#. Define a :ref:`feed to associate fields in the Avro file with semantic tags <format-avro-pull-feeds>`; in some situations you may need to use an :ref:`ingest query to transform data in the Avro file <format-avro-pull-ingest-queries>` prior to loading it to Amperity.
#. Configure a courier for :ref:`the location and name of the Avro file <format-avro-pull-couriers-load-settings>`, and then for :ref:`the name of an ingest query <format-avro-pull-couriers-load-operations>`.

.. format-avro-pull-end


.. _format-avro-pull-data-sources:

Data sources
--------------------------------------------------

.. format-avro-pull-data-sources-start

Pull Apache Avro files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-avro-pull-data-sources-end


.. _format-avro-pull-load-data:

Load data
--------------------------------------------------

.. format-avro-pull-load-data-start

For most Apache Avro files, use a feed to associate fields in the file with semantic tags. In some situations, an ingest query may be necessary to transform data prior to loading it to Amperity.

* :ref:`Feeds <format-avro-pull-feeds>`
* :ref:`Ingest queries <format-avro-pull-ingest-queries>`

.. format-avro-pull-load-data-end


.. _format-avro-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-avro-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-avro-pull-feeds-end


.. _format-avro-pull-ingest-queries:

Ingest queries
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-avro-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the Avro file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. format-avro-pull-ingest-queries-end


.. _format-avro-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-avro-pull-couriers-start

A courier must specify the location of the Avro file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-avro-pull-couriers-load-settings>`
#. :ref:`Load operations <format-avro-pull-couriers-load-operations>`

.. format-avro-pull-couriers-end


.. _format-avro-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-avro-pull-couriers-load-settings-start

Use courier load settings to specify the path to the Avro file, a file tag (which can be the same as the name of the Avro file), and the ``"application/avro"`` content type.

.. format-avro-pull-couriers-load-settings-end

.. format-avro-pull-couriers-load-settings-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.avro'",
     "object/land-as": {
       "file/tag": "FILE_NAME",
       "file/content-type": "application/avro"
     }
   }

.. format-avro-pull-couriers-load-settings-block-end


.. _format-avro-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-avro-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings. Load operations for an ingest query may specify a series of options.

.. format-avro-pull-couriers-load-operations-end


.. _format-avro-pull-couriers-load-operations-feed:

Load from feed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-avro-pull-couriers-load-operations-feed-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "OPERATION",
         "file": "FILE_NAME"
       }
     ]
   }

.. format-avro-pull-couriers-load-operations-feed-end


.. _format-avro-pull-couriers-load-operations-ingest-query:

Load from ingest query
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-avro-pull-couriers-load-operations-ingest-query-start

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

.. format-avro-pull-couriers-load-operations-ingest-query-end


.. _format-avro-destination:

Send Avro files
==================================================

.. format-avro-destination-start

.. important:: Amperity does not send Avro files to downstream workflows.

.. format-avro-destination-end
