.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About TSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About TSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: TSV

==================================================
File format: TSV
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-tsv-start
   :end-before: .. term-tsv-end

.. format-tsv-tip-start

.. tip:: Consider using :doc:`Apache Avro <format_avro>` and :doc:`Apache Parquet <format_parquet>` file formats instead of TSV. 

   * Avro uses a JSON-like schema that stores data in rows. Avro files have a very small file size that transfers quickly.
   * Parquet is highly compact, can be transferred easily, and avoids escape character and data formatting issues that can be present in other formats.

.. format-tsv-tip-end


.. _format-tsv-file-sizes:

File sizes
==================================================

.. format-tsv-file-sizes-start

The size of a TSV file cannot exceed 10 GB. A TSV file that is larger than 10 GB must be split into smaller files before it is made available to Amperity. The total number of TSV files in a single ingest job cannot exceed 500k.

.. format-tsv-file-sizes-end


.. _format-tsv-pull:

Pull TSV files
==================================================

.. format-tsv-pull-start

To pull TSV files to Amperity:

#. Select a :ref:`filedrop data source <format-tsv-pull-data-sources>`.
#. Define a :ref:`feed to associate fields in the TSV file with semantic tags <format-tsv-pull-feeds>`; in some situations you may need to use an :ref:`ingest query to transform data in the TSV file <format-tsv-pull-ingest-queries>` prior to loading it to Amperity.
#. Configure a courier for :ref:`the location and name of the TSV file <format-tsv-pull-couriers-load-settings>`, and then for :ref:`the load operation <format-tsv-pull-couriers-load-operations>` (either directly from a feed or from a ingest query).

.. format-tsv-pull-end


.. _format-tsv-pull-data-sources:

Data sources
--------------------------------------------------

.. format-tsv-pull-data-sources-start

Pull TSV files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-tsv-pull-data-sources-end


.. _format-tsv-pull-data-sources-recommendations:

Recommendations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-tsv-pull-data-sources-recommendations

When using TSV files, it is recommend to:

* Use column headers (with no special characters except underscores)
* Ensure duplicate header names are not present
* Ensure one (or more) fields are present that can act as a unique identifier
* Use a comma as the delimiter for fields; use a newline character as the delimiter for rows
* Escape commas or quotes that appear in the data
* Quote string values
* Encode files in UTF-8 or UTF-16. Amperity automatically detects the 2-byte header present with the UTF-16 encoding format. If the 2-byte header is missing, the file is treated as UTF-8.
* Compress files prior to encryption using ZIP, GZIP, and/or TAR. Amperity automatically decompresses GZIP files; ZIP and TAR decompression must be specified in courier file load settings.
* Encrypt files using PGP; compression will not reduce the size of an encrypted file

.. format-tsv-pull-data-sources-recommendations


.. _format-tsv-pull-load-data:

Load data
--------------------------------------------------

.. format-tsv-pull-load-data-start

For most TSV files, use a feed to associate fields in the TSV file with semantic tags. In some situations, an ingest query may be necessary to transform data prior to loading it to Amperity.

* :ref:`Feeds <format-tsv-pull-feeds>`
* :ref:`Ingest queries <format-tsv-pull-ingest-queries>`

.. format-tsv-pull-load-data-end


.. _format-tsv-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-tsv-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-tsv-pull-feeds-end


.. _format-tsv-pull-feeds-headers:

Files with header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-feeds-headers-start

Most TSV files contain a row of data that defines headers for the data set. Configure the load settings for the courier to accept the headers.

.. format-tsv-pull-feeds-headers-end


.. _format-tsv-pull-feeds-non-standard-quotes-and-separators:

Files with non-standard quotes and separators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-feeds-non-standard-quotes-and-separators-start

Some TSV files may use non-standard characters for quotes and separators, such as ``*`` for quotes and ``;`` for separators. If a TSV file contains non-standard characters, you must specify the character in the courier load settings. For example:

::

      "file/quote": "*",
      "file/separator": ";"

.. format-tsv-pull-feeds-non-standard-quotes-and-separators-end


.. _format-tsv-pull-feeds-headerless:

Files without header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-feeds-headerless-start

A headerless TSV file does not contain a row of data that defines headers for the data set. When working with a headerless TSV file you can configure the load settings for the courier to accept headerless files or you may use an ingest query when the data must be changed in some way prior to loading it to Amperity.

.. format-tsv-pull-feeds-headerless-end

.. format-tsv-pull-feeds-headerless-tip-start

.. tip:: Before using an ingest query to change data *prior* to loading it to Amperity, consider using domain SQL *after* it has been loaded to Amperity. Using domain SQL allows for easier changes to data schemas and (more importantly) does not require data to be truncated, and then reloaded on a regular basis.

.. format-tsv-pull-feeds-headerless-tip-end


.. _format-tsv-pull-feeds-domain-sql:

Domain SQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../shared/terms.rst
   :start-after: .. term-domain-sql-start
   :end-before: .. term-domain-sql-end

.. format-tsv-pull-feeds-domain-sql-start

Domain SQL allows the data in TSV files to be transformed *after* it has been loaded to Amperity. Some common use cases for using domain SQL to transform data include:

* :ref:`Combining days, months, and years into a single birthdate field <domain-tables-custom-sql-use-case-combine-birthdate>`
* :ref:`Combining postal codes <domain-tables-custom-sql-use-case-combine-postal>`
* :ref:`Extracting first and last names <domain-tables-custom-sql-use-case-extract-names>`
* :ref:`Hashing profile (PII) data <domain-tables-custom-sql-use-case-rehash-data>`
* :ref:`Parsing fields with multiple separators <domain-tables-custom-sql-use-case-parse-fields-with-multiple-separators>`
* :ref:`Setting non-US-ASCII email addresses to NULL <domain-tables-custom-sql-use-case-set-email-to-null>`
* :ref:`Standardizing values for USA states <domain-tables-custom-sql-use-case-standardize-values-for-usa-states>`

.. format-tsv-pull-feeds-domain-sql-end


.. _format-tsv-pull-ingest-queries:

Ingest queries
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-tsv-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the TSV file. Use a **SELECT** statement to specify which fields should be loaded to Amperity. Apply transforms to those fields as necessary.

.. format-tsv-pull-ingest-queries-end


.. _format-tsv-pull-ingest-queries-ordinals:

Ordinal column names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-ingest-queries-ordinals-start

Some situations require using an ingest query to load a headerless TSV file. Use a **SELECT** statement to apply ordinal column names, and then aliasing each column name to a field name if desired.

A headerless file should use column names that are based on ordinal positions using the following pattern:

.. code-block:: none

   _c0
   _c1
   _c2
   _c3
   ...
   _cN

Add these column names within the **SELECT** statement. You may use aliasing to apply better column names within the ingest query.

For example, using ordinal columns to filter a long list of clickstream data points down to a usable schema for use within Amperity:

.. code-block:: sql

   SELECT
     _c0 AS click_time_gmt
     ,_c1 AS datetime
     ,_c2 AS ip_address
     ,_c3 AS page_event
     ,_c4 AS duplicate_purchase
     ,_c5 AS campaign_name
     ,_c6 AS click_source
     ,_c7 AS channel_name
     ,_c8 AS product_list
     ...
   FROM table

.. format-tsv-pull-ingest-queries-ordinals-end


.. _format-tsv-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-tsv-pull-couriers-start

A courier must specify the location of the TSV file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-tsv-pull-couriers-load-settings>`
#. :ref:`Load operations <format-tsv-pull-couriers-load-operations>`

.. format-tsv-pull-couriers-end


.. _format-tsv-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-tsv-pull-couriers-load-settings-start

Use courier load settings to specify the path to the TSV file, a file tag (which can be the same as the name of the TSV file), if the file does not contain header rows, and the ``"text/tab-separated-values"`` content type.

With some TSV files it may be necessary to specify the character used for quotes and the character used as a separator.

.. format-tsv-pull-couriers-load-settings-start


.. _format-tsv-pull-couriers-load-settings-headers:

with header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-couriers-load-settings-headerless-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.tsv'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/content-type": "text/tab-separated-values"
     }
   },

.. format-tsv-pull-couriers-load-settings-headerless-end


.. _format-tsv-pull-couriers-load-settings-quotes-separators:

with non-standard quotes and separators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-couriers-load-settings-quotes-separators-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.tsv'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/quote": "*",
        "file/separator": ";",
        "file/content-type": "text/tab-separated-values"
     }
   },

.. format-tsv-pull-couriers-load-settings-quotes-separators-end


.. _format-tsv-pull-couriers-load-settings-headerless:

without header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-couriers-load-settings-headerless-start

If a TSV file is headerless, change the load setting for ``"file/header-rows"`` from ``1`` to ``0``.

.. format-tsv-pull-couriers-load-settings-headerless-end

.. format-tsv-pull-couriers-load-settings-headerless-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.tsv'",
     "object/land-as": {
        "file/header-rows": 0,
        "file/tag": "FILE_NAME",
        "file/content-type": "text/tab-separated-values"
     }
   },

.. format-tsv-pull-couriers-load-settings-headerless-block-end


.. _format-tsv-pull-couriers-load-settings-wildcards-in-archives:

wildcards in archives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../amperity_reference/source/couriers.rst
   :start-after: .. couriers-files-patterns-wildcards-within-archives-start
   :end-before: .. couriers-files-patterns-wildcards-within-archives-end


.. _format-tsv-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-tsv-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings. Load operations for an ingest query may specify a series of options.

.. format-tsv-pull-couriers-load-operations-end


.. _format-tsv-pull-couriers-load-operations-feed:

Load from feed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-couriers-load-operations-feed-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "OPERATION",
         "file": "FILE_NAME"
       }
     ]
   }

.. format-tsv-pull-couriers-load-operations-feed-end


.. _format-tsv-pull-couriers-load-operations-ingest-query:

Load from ingest query
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-couriers-load-operations-ingest-query-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "spark-sql",
         "spark-sql-files": [
           {
             "file": "FILE_NAME",
             "options": {
               "delimiter": "\t",
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

.. format-tsv-pull-couriers-load-operations-ingest-query-end


.. _format-tsv-destination:

Send TSV files
==================================================

.. format-tsv-destination-links-start

Amperity can send TSV files to downstream workflows using any filedrop destination:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-tsv-destination-links-end
