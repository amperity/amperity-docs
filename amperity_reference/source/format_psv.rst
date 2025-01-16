.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About PSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About PSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: PSV

==================================================
File format: PSV
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-psv-start
   :end-before: .. term-psv-end

.. format-psv-tip-start

.. tip:: Consider using :doc:`Apache Avro <format_avro>` and :doc:`Apache Parquet <format_parquet>` file formats instead of PSV. 

   * Avro uses a JSON-like schema that stores data in rows. Avro files have a very small file size that transfers quickly.
   * Parquet is highly compact, can be transferred easily, and avoids escape character and data formatting issues that can be present in other formats.

.. format-psv-tip-end


.. _format-psv-pull:

Pull PSV files
==================================================

.. format-psv-pull-start

To pull PSV files to Amperity:

#. Select a :ref:`filedrop data source <format-psv-pull-data-sources>`.
#. Define a :ref:`feed to associate fields in the PSV file with semantic tags <format-psv-pull-feeds>`; in some situations you may need to use an :ref:`ingest query to transform data in the PSV file <format-psv-pull-ingest-queries>` prior to loading it to Amperity.
#. Configure a courier for :ref:`the location and name of the PSV file <format-psv-pull-couriers-load-settings>`, and then for :ref:`the load operation <format-psv-pull-couriers-load-operations>` (either directly from a feed or from an ingest query).

.. format-psv-pull-end


.. _format-psv-pull-data-sources:

Data sources
--------------------------------------------------

.. format-psv-pull-data-sources-start

Pull PSV files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-psv-pull-data-sources-end


.. _format-psv-pull-load-data:

Load data
--------------------------------------------------

.. format-psv-pull-load-data-start

For most PSV files, use a feed to associate fields in the PSV file with semantic tags. In some situations, an ingest query may be necessary to transform data prior to loading it to Amperity.

* :ref:`Feeds <format-psv-pull-feeds>`
* :ref:`Ingest queries <format-psv-pull-ingest-queries>`

.. format-psv-pull-load-data-end


.. _format-psv-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-psv-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-psv-pull-feeds-end


.. _format-psv-pull-feeds-headers:

Files with header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-feeds-headers-start

Most PSV files contain a row of data that defines headers for the data set. Configure the load settings for the courier to accept the headers.

.. format-psv-pull-feeds-headers-end


.. _format-psv-pull-feeds-non-standard-quotes-and-separators:

Files with non-standard quotes and separators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-feeds-non-standard-quotes-and-separators-start

Some PSV files may use non-standard characters for quotes and separators, such as ``*`` for quotes and ``;`` for separators. If a PSV file contains non-standard characters, you must specify the character in the courier load settings. For example:

::

      "file/quote": "*",
      "file/separator": ";"

.. format-psv-pull-feeds-non-standard-quotes-and-separators-end


.. _format-psv-pull-feeds-headerless:

Files without header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-feeds-headerless-start

A headerless PSV file does not contain a row of data that defines headers for the data set. When working with a headerless PSV file you can configure the load settings for the courier to accept headerless files or you may use an ingest query when the data must be changed in some way prior to loading it to Amperity.

.. format-psv-pull-feeds-headerless-end

.. format-psv-pull-feeds-headerless-tip-start

.. tip:: Before using an ingest query to change data *prior* to loading it to Amperity, consider using domain SQL *after* it has been loaded to Amperity. Using domain SQL allows for easier changes to data schemas and (more importantly) does not require data to be truncated, and then reloaded on a regular basis.

.. format-psv-pull-feeds-headerless-tip-end


.. _format-psv-pull-feeds-domain-sql:

Domain SQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../shared/terms.rst
   :start-after: .. term-domain-sql-start
   :end-before: .. term-domain-sql-end

.. format-psv-pull-feeds-domain-sql-start

Domain SQL allows the data in PSV files to be transformed *after* it has been loaded to Amperity. Some common use cases for using domain SQL to transform data include:

* :ref:`Combining days, months, and years into a single birthdate field <domain-tables-custom-sql-use-case-combine-birthdate>`
* :ref:`Combining postal codes <domain-tables-custom-sql-use-case-combine-postal>`
* :ref:`Extracting first and last names <domain-tables-custom-sql-use-case-extract-names>`
* :ref:`Hashing profile (PII) data <domain-tables-custom-sql-use-case-rehash-data>`
* :ref:`Parsing fields with multiple separators <domain-tables-custom-sql-use-case-parse-fields-with-multiple-separators>`
* :ref:`Setting non-US-ASCII email addresses to NULL <domain-tables-custom-sql-use-case-set-email-to-null>`
* :ref:`Standardizing values for USA states <domain-tables-custom-sql-use-case-standardize-values-for-usa-states>`

.. format-psv-pull-feeds-domain-sql-end


.. _format-psv-pull-ingest-queries:

Ingest queries
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-psv-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the PSV file. Use a **SELECT** statement to specify which fields should be loaded to Amperity. Apply transforms to those fields as necessary.

.. format-psv-pull-ingest-queries-end


.. _format-psv-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-psv-pull-couriers-start

A courier must specify the location of the PSV file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-psv-pull-couriers-load-settings>`
#. :ref:`Load operations <format-psv-pull-couriers-load-operations>`

.. format-psv-pull-couriers-end


.. _format-psv-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-psv-pull-couriers-load-settings-start

Use courier load settings to specify the path to the PSV file, a file tag (which can be the same as the name of the PSV file), if the file does not contain header rows, and the ``"text/pipe-separated-values"`` content type.

With some PSV files it may be necessary to specify the character used for quotes and the character used as a separator.

.. format-psv-pull-couriers-load-settings-start


.. _format-psv-pull-couriers-load-settings-headers:

with header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-couriers-load-settings-headerless-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.psv'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/content-type": "text/pipe-separated-values"
     }
   },

.. format-psv-pull-couriers-load-settings-headerless-end


.. _format-psv-pull-couriers-load-settings-quotes-separators:

with non-standard quotes and separators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-couriers-load-settings-quotes-separators-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.psv'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/quote": "*",
        "file/separator": ";",
        "file/content-type": "text/pipe-separated-values"
     }
   },

.. format-psv-pull-couriers-load-settings-quotes-separators-end


.. _format-psv-pull-couriers-load-settings-headerless:

without header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-couriers-load-settings-headerless-start

If a PSV file is headerless, change the load setting for ``"file/header-rows"`` from ``1`` to ``0``.

.. format-psv-pull-couriers-load-settings-headerless-end

.. format-psv-pull-couriers-load-settings-headerless-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.psv'",
     "object/land-as": {
        "file/header-rows": p,
        "file/tag": "FILE_NAME",
        "file/content-type": "text/pipe-separated-values"
     }
   },

.. format-psv-pull-couriers-load-settings-headerless-block-end


.. _format-psv-pull-couriers-load-settings-wildcards-in-archives:

wildcards in archives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../amperity_reference/source/couriers.rst
   :start-after: .. couriers-files-patterns-wildcards-within-archives-start
   :end-before: .. couriers-files-patterns-wildcards-within-archives-end


.. _format-psv-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-psv-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings. Load operations for an ingest query may specify a series of options.

.. format-psv-pull-couriers-load-operations-end


.. _format-psv-pull-couriers-load-operations-feed:

Load from feed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-couriers-load-operations-feed-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "OPERATION",
         "file": "FILE_NAME"
       }
     ]
   }

.. format-psv-pull-couriers-load-operations-feed-end


.. _format-psv-pull-couriers-load-operations-ingest-query:

Load from ingest query
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-couriers-load-operations-ingest-query-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "spark-sql",
         "spark-sql-files": [
           {
             "file": "FILE_NAME"
             "options": {
               "delimiter": "\|",
               "escape": "\\",
               "multiline": "true",
               "quote": "\""
             }
           }
         ],
         "spark-sql-query": "INGEST_QUERY_NAME"
       }
     ]
   }

.. format-psv-pull-couriers-load-operations-ingest-query-end


.. _format-psv-destination:

Send PSV files
==================================================

.. format-psv-destination-links-start

Amperity can send PSV files to downstream workflows using any filedrop destination:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-psv-destination-links-end
