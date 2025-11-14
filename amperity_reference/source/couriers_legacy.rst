.. https://docs.amperity.com/legacy/

:orphan:

.. meta::
    :description lang=en:
        A courier brings data from an external system to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        A courier brings data from an external system to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        About couriers (legacy)

==================================================
About couriers (legacy)
==================================================

.. vale off

.. warning:: Use this topic for couriers with legacy configuration patterns and options. Use :doc:`About couriers <couriers>` for the new configuration patterns and options.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. couriers-legacy-what-they-do-start

What a courier does:

#. Checks if data is available at the source location.
#. Collects data from the source location, and then pulls that data to Amperity.

What a courier needs:

#. Access to the source location. Most data sources--Amazon S3, Azure Blob Storage, Google Cloud Storage, or any SFTP site--allow the use of many file formats, while others may use Snowflake or REST APIs.
#. A location from which to copy data.
#. An associated feed.
#. A file format, such as CSV, TSV, or Apache Parquet, along with additional details for compression, archive, and encryption.
#. A combination of :ref:`load settings <couriers-legacy-files-load-settings>` and :ref:`load operations <couriers-legacy-load-operation-types>`. The exact combination of settings and operations depends on the data source and the types of files to be pulled to Amperity.

.. couriers-legacy-what-they-do-end


.. _couriers-legacy-files:

File couriers
==================================================

.. couriers-legacy-files-start

A file data source can provide files to Amperity in just about any file format, such as CSV, JSON, Apache Parquet, Apache AVRO, PSV, and TSV. Locations from which file data sources can be pulled include Amazon S3, Azure Blob Storage, Google Cloud Storage, and any SFTP site.

.. couriers-legacy-files-end


.. _couriers-legacy-files-load-settings:

Load settings
--------------------------------------------------

.. couriers-legacy-files-load-settings-start

File data sources define load settings in two parts:

#. A list of files that should be pulled to Amperity.
#. A list of load operations that associate each file with a feed.

The exact combination of files and load operations depends on the data source from which data is made available to Amperity.

.. couriers-legacy-files-load-settings-end

.. couriers-legacy-files-load-settings-syntax-start

Load settings define the location of a data source, it is type, and how it should be processed by Amperity. The syntax for file load settings is similar to:

.. code-block:: none

   [
     {
       "object/file-pattern": "'CUSTOMER/ENV/FILENAME_'MM-dd-yyyy'.csv'",
       "object/type": "file",
       "object/land-as": {
         "file/tag": "FILE_TAG",
         "file/content-type": "text/csv",
         "file/header-rows": 1
       }
     },
     {
       "object/file-pattern": "ARCHIVED/FILENAME_'MM-dd-yyyy'.zip",
       "object/type": "archive",
       "archive/contents": {
         "FILENAME": {
           "subobject/land-as": {
             "file/tag": "FILENAME_TAG",
             "file/content-type": "text/csv"
           }
         },
        "archive/skip-missing-contents": true
       }
     },
     {
       "object/file-pattern": "ARCHIVED/FILENAME_'MM-dd-yyyy'.zip",
       "object/type": "archive",
       "object/land-as": {
         "file/tag": "FILENAME_TAG",
         "file/content-type": "text/csv",
         "file/header-rows": 1
       }
     }
    ]

.. couriers-legacy-files-load-settings-syntax-end

.. couriers-legacy-files-load-settings-context-start

Each filedrop load setting must specify the file pattern, which is the path to the file, its filename, a date stamp, and a file extension. The rest of the load settings block must match. For example, the content type for a "some-file.csv" must be "text/csv".

An archive must specify the archive *and* the file contained within it. If the file is archived as "some-file.zip" then the ``"object/type"`` would be "archive" and the content type of the file within it would be "text/csv".

If an archive contains only a single file *or* if all the files within the archive have the same file tag, content type, and other settings, then ``"archive/contents"`` can be omitted and ``"object/land-as"`` can be specified instead. The files within the archive will all use the specified ``"object/land-as"`` settings.

If an archive is missing contents and you would like to ignore or skip those missing contents, then ``"archive/skip-missing-contents"`` can be added to your settings.

.. couriers-legacy-files-load-settings-context-end


.. _couriers-legacy-files-patterns:

File patterns
--------------------------------------------------

.. couriers-legacy-files-patterns-start

A courier looks for objects in a filedrop location using a combination of the path to a directory, the name of a file, and a date. These are defined by the ``"object/file-pattern"`` setting for each object. A courier runs based on a date or a date range, and then looks for files in the filedrop location for that date or date range.

.. couriers-legacy-files-patterns-end

.. couriers-legacy-files-patterns-links-start

A file pattern may use a combination of :ref:`literal strings <couriers-legacy-files-patterns-literal-strings>`, :ref:`wildcard characters <couriers-legacy-files-patterns-wildcards>` (``*``) within literal strings, :ref:`wildcard characters for filenames in archives <couriers-legacy-files-patterns-wildcards-within-archives>`, and :ref:`date components <couriers-legacy-files-patterns-date-components>`, separated by single quotes and forward slashes.

.. couriers-legacy-files-patterns-links-end


.. _couriers-legacy-files-patterns-wildcards:

Wildcards
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-files-patterns-wildcards-start

A wildcard can match zero or more characters up until a forward-slash character.

.. note:: When a file pattern with a wildcard matches more than one file for a given date or date range, the matched files are loaded in such a way that guarantees per-day ordering. If your courier uses an ingest query, ascending lexicographical ordering by file is not guaranteed or preserved within a single day's files.

**Examples**

The following example shows using a wildcard at the end of a file pattern:

.. code-block:: none

   'files/'yyyy'/'MM'/'dd'/customers-*.csv'

will match any of these files:

* /customers-.csv
* /customers-1.csv
* /customers-hello-world.csv

and will not match any of these:

* /customers-.csv.0
* /customers-0.json
* /customers-0/1/file.csv
* /customers.csv

The following example shows using multiple wildcards:

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'responsys/outbound_files/*_STATE_'yyyyMMdd'_*.txt.gpg'",
     "object/land-as": {
       "file/header-rows": 1,
       "file/tag": "launch",
       "file/content-type": "text/csv"
     }
   },

.. couriers-legacy-files-patterns-wildcards-end


.. _couriers-legacy-files-patterns-wildcards-within-archives:

Wildcards within archives
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-files-patterns-wildcards-within-archives-start

A wildcard can be used to match one or more files in an archive.

The following example shows how to use a wildcard to match a set of CSV files contained within the same archive:

.. code-block:: none

   [
     {
       "archive/contents": {
         "ArchiveName/files_*.csv:" {
           "subobject/land-as": {
             "file/header-rows": 1,
             "file/separator": ",",
             "file/tag": "launch",
             "file/content-type": "text/csv"
           }
         }
       },
       "object/type": "archive",
       "object/file-pattern": "/path/to/archive/ArchiveName.zip"
     }
   ]

.. couriers-legacy-files-patterns-wildcards-within-archives-end


.. _couriers-legacy-files-patterns-literal-strings:

Literal strings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-load-settings-file-pattern-literal-strings-start

A literal string must be an exact match to characters in the file path, with the exception of the presence of wildcard characters within literal strings. Wrap literal strings that match Joda-Time format in single quotes. For example:

* 'files/'
* '/'
* '/'
* 'MM-dd-YYYY'

.. couriers-legacy-files-patterns-literal-strings-end


.. _couriers-legacy-files-patterns-date-components:

Date components
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-files-patterns-date-components-start

Date components act as placeholders for months, days, and years. Real values are applied when the courier runs on a given date or date range. Date components must match `Joda-Time pattern-based formatting <https://www.joda.org/joda-time/key_format.html>`__ |ext_link|, but should be limited to the following patterns:

.. list-table::
   :widths: 200 200 200
   :header-rows: 1

   * - Pattern
     - Meaning
     - Examples
   * - **yyyy**
     - 4-digit year
     - 2020, 2021, 2022
   * - **MM**
     - 2-digit month
     - 01, 02, 03
   * - **dd**
     - 2-digit date
     - 01, 02, 03, 04

A courier that runs using this pattern:

.. code-block:: none

   'files/'yyyy'/'MM'/'dd'/customers-*.csv'

when run on April 10, 2020 will look for files at ``'files/2020/04/10/customers-*.csv'`` and will return any files that match.

.. couriers-legacy-files-patterns-date-components-end


.. _couriers-legacy-files-patterns-compression:

File compression / archive
--------------------------------------------------

.. couriers-legacy-files-patterns-compression-start

Amperity supports the following compression and archive types:

* :ref:`couriers-legacy-files-patterns-compression-gzip`
* :ref:`couriers-legacy-files-patterns-compression-tar`
* :ref:`couriers-legacy-files-patterns-compression-zip`

.. couriers-legacy-files-patterns-compression-end


.. _couriers-legacy-files-patterns-compression-gzip:

GZIP
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-files-patterns-compression-gzip-start

.. code-block:: none

   {
     "object/type": "file",
     "object/optional": false,
     "object/file-pattern": "'ARCHIVED/FILENAME_'MM-dd-yyyy'.csv.gz'",
     "object/land-as": {
       "file/header-rows": 1,
       "file/tag": "FILENAME_TAG",
       "file/content-type": "text/csv"
     }
   }

.. couriers-legacy-files-patterns-compression-gzip-end


.. _couriers-legacy-files-patterns-compression-tar:

TAR
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-files-patterns-compression-tar-start

.. code-block:: none

   {
     "object/file-pattern": "'ARCHIVED/FILENAME_'MM-dd-yyyy'.tar'",
     "object/type": "archive",
     "archive/contents": {
       "FILENAME": {
         "subobject/land-as": {
           "file/tag": "FILENAME_TAG",
           "file/content-type": "text/csv"
         }
       }
     }
   }

.. couriers-legacy-files-patterns-compression-tar-end


.. _couriers-legacy-files-patterns-compression-zip:

ZIP
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-files-patterns-compression-zip-start

.. code-block:: none

   {
     "object/file-pattern": "ARCHIVED/FILENAME_'MM-dd-yyyy'.zip",
     "object/type": "archive",
     "archive/contents": {
       "FILENAME": {
         "subobject/land-as": {
           "file/tag": "FILENAME_TAG",
           "file/content-type": "text/csv"
         }
       }
     }
   }

.. couriers-legacy-files-patterns-compression-zip-end


.. _couriers-legacy-load-settings-input-examples:

Input examples
--------------------------------------------------

.. include:: ../../amperity_reference/source/format_common.rst
   :start-after: .. format-common-send-input-examples-start
   :end-before: .. format-common-send-input-examples-end


.. _couriers-legacy-load-settings-input-example-single:

for single files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/format_common.rst
   :start-after: .. format-common-send-input-examples-single-start
   :end-before: .. format-common-send-input-examples-single-end


.. _couriers-legacy-load-settings-input-example-multiple:

for multiple files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/format_common.rst
   :start-after: .. format-common-send-input-examples-multiple-start
   :end-before: .. format-common-send-input-examples-multiple-end


.. _couriers-legacy-api:

API couriers
==================================================

.. couriers-legacy-api-start

An API data source varies, depending on the file format and other configuration details. API data sources include Google Analytics, Salesforce Sales Cloud, and Zendesk.

.. couriers-legacy-api-end


.. _couriers-legacy-snowflake:

Snowflake couriers
==================================================

.. couriers-legacy-snowflake-start

A Snowflake data source provides a list of tables that are consolidated into a fileset. Snowflake data sources include Snowflake itself, and then also any Fivetran data source, such as Klaviyo, Shopify, Kustomer, and HubSpot.

.. couriers-legacy-snowflake-end


.. _couriers-legacy-snowflake-table-list:

Table lists
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-table-list-start
   :end-before: .. sources-add-courier-fivetran-table-list-end

.. couriers-legacy-snowflake-table-list-example-start

::

   [
     "AMPERITY_A1BO987C.ACME.CAMPAIGN",
     "AMPERITY_A1BO987C.ACME.LIST",
     "AMPERITY_A1BO987C.ACME.CONTACT"
   ]

.. couriers-legacy-snowflake-table-list-example-end


.. _couriers-legacy-snowflake-stage-name:

Stage names
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-stage-name-start
   :end-before: .. sources-add-courier-fivetran-stage-name-end

.. couriers-legacy-snowflake-stage-name-example-start

::

   AMPERITY_A1BO987C.ACME.ACME_STAGE

.. couriers-legacy-snowflake-stage-name-example-end


.. _couriers-legacy-snowflake-load-operation:

Load operations
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-load-operation-start
   :end-before: .. sources-add-courier-fivetran-load-operation-end

.. couriers-legacy-snowflake-load-operation-start

::

   {
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.ACME.CAMPAIGN"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.ACME.LIST"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.ACME.CONTACT"
       }
     ]
   }

.. couriers-legacy-snowflake-load-operation-end


.. _couriers-legacy-load-operation-types:

Load operation types
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-fileset-start
   :end-before: .. term-courier-fileset-end

.. couriers-legacy-load-operation-types-start

.. couriers-legacy-load-operation-types-links-start

Each file in a fileset must be associated with one of the following load operation types:

* :ref:`couriers-legacy-load-operation-type-empty`
* :ref:`couriers-legacy-load-operation-type-incorrect-feed-id`
* :ref:`couriers-legacy-load-operation-type-load-files`
* :ref:`couriers-legacy-load-operation-type-load-ingest-query`
* :ref:`couriers-legacy-load-operation-type-truncate-then-load`

.. couriers-legacy-load-operation-types-links-end


.. _couriers-legacy-load-operation-type-empty:

Empty
--------------------------------------------------

.. couriers-legacy-load-operation-type-empty-start

An empty load operation will bring files to Amperity, but not try to load those files into a feed. An empty load operation is ideal for bringing sample files to Amperity prior to configuring the feed that defines the schema within Amperity for a data source. Use the sample file while configuring the feed, and then update the load operation to match the configuration requirements for the associated file type.

.. couriers-legacy-load-operation-type-empty-end

.. couriers-legacy-load-operation-type-empty-block-start

.. code-block:: none

   {}

.. couriers-legacy-load-operation-type-empty-block-end

.. vale off

.. couriers-legacy-load-operation-type-empty-tip-start

.. tip:: You cannot use an empty load operation for files that require the use of an ingest query to transform the data prior to it being made available to the feed.

   For example, a JSON file with nested data must use an ingest query to flatten the file. A feed cannot use a JSON file with nested data as a sample file. And a courier cannot run to successful completion unless the courier is configured with a feed ID.

   In this type of situation, create a file outside of this workflow to use as the sample file for the feed. For example, use Databricks to generate a zero-row sample file, and then upload that file during feed creation.

   Another option is to define the schema without using a sample file. Select the **Don't use sample file** option when adding the feed, and then use the **Add field** button to define each field in the schema.

.. couriers-legacy-load-operation-type-empty-tip-end

.. vale on


.. _couriers-legacy-load-operation-type-incorrect-feed-id:

Incorrect feed ID
--------------------------------------------------

.. couriers-legacy-load-operation-type-incorrect-feed-id-start

Instead of using an empty load operation you can use an incorrect feed ID to pull files to Amperity. This approach uses the default load configuration, but sets the feed ID to a string that is not available to the courier after feeds have been updated. For example, replacing the digits with six "x" characters:

.. code-block:: none

   {
     "df-xxxxxx": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "campaign-members"
       }
     ]
   }

This will return an error message similar to:

.. code-block:: none

   Error running load-operations task
   Cannot find required feeds: "df-xxxxxx"

The load operation will pull the files and make them available for use with defining a feed schema.

.. couriers-legacy-load-operation-type-incorrect-feed-id-end


.. _couriers-legacy-load-operation-type-load-files:

Load files
--------------------------------------------------

.. couriers-legacy-load-operation-type-load-files-start

You can load contents of a data file to a domain table as a load operation as an ``UPSERT`` operation that is based off of the primary key in the table.

.. couriers-legacy-load-operation-type-load-files-end

.. couriers-legacy-load-operation-type-load-files-block-start

.. code-block:: none

   "OTHER_FEED_ID": [
     {
       "type": "load",
       "file": "OTHER_FILE_TAG"
     }
   ]

.. couriers-legacy-load-operation-type-load-files-block-end


.. _couriers-legacy-load-operation-type-load-ingest-query:

Load ingest query
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-spark-sql-start
   :end-before: .. term-spark-sql-end

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-about-start
   :end-before: .. sql-spark-about-end

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-note-spark-vs-presto-start
   :end-before: .. sql-spark-note-spark-vs-presto-end

.. couriers-legacy-load-operation-type-load-ingest-query-start

The configuration for an ingest query load operation depends on the data source against which the ingest query runs:

* Apache Avro
* Apache Parquet
* CBOR
* CSV
* JSON
* NDJSON
* PSV
* TSV
* XML

.. couriers-legacy-load-operation-type-load-ingest-query-end


.. _couriers-legacy-load-operation-type-truncate-then-load:

Truncate, then load
--------------------------------------------------

.. couriers-legacy-load-operation-type-truncate-then-load-start

You can empty the contents of a table prior to loading a data file to a domain table as a load operation.

.. note:: A truncate operation is always run first, regardless of where it is specified within the load operation.

.. couriers-legacy-load-operation-type-truncate-then-load-end

.. couriers-legacy-load-operation-type-truncate-then-load-block-start

.. code-block:: none

   "FEED_ID": [
     {
       "type": "truncate"
     },
     {
       "type": "load",
       "file": "FILE_NAME"
     }
   ],

.. couriers-legacy-load-operation-type-truncate-then-load-block-end


.. _couriers-legacy-examples:

Examples
==================================================

The following sections provide examples for load settings and load operations by data source and by file type:

* :ref:`couriers-legacy-example-apache-avro`
* :ref:`couriers-legacy-example-apache-parquet`
* :ref:`couriers-legacy-example-cbor`
* :ref:`couriers-legacy-example-csv`
* :ref:`couriers-legacy-example-json`
* :ref:`couriers-legacy-example-ndjson`
* :ref:`couriers-legacy-example-psv`
* :ref:`couriers-legacy-example-salesforce-commerce-cloud`
* :ref:`couriers-legacy-example-salesforce-sales-cloud`
* :ref:`couriers-legacy-example-snowflake`
* :ref:`couriers-legacy-example-tsv`
* :ref:`couriers-legacy-example-xml`


.. _couriers-legacy-example-apache-avro:

Apache Avro
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-apache-avro-start
   :end-before: .. term-apache-avro-end

**Load settings**

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

**Load operations**

.. format-avro-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings. Load operations for an ingest query may specify a series of options.

.. format-avro-pull-couriers-load-operations-end


.. _couriers-legacy-example-apache-parquet:

Apache Parquet
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-apache-parquet-start
   :end-before: .. term-apache-parquet-end

.. format-parquet-pull-couriers-load-settings-partition-start

.. note:: Apache Parquet files are almost always partitioned, where a single logical Parquet file is comprised of multiple physical files in a directory structure, each of them representing a partition.

   Parquet partitioning optionally permits for data to be nested in a directory structure determined by the value of partitioning columns. Amperity only detects Parquet partition files one directory level below the configured file pattern. For example:

   .. code-block:: none

       "path/to/file-YYYY-MM-dd.parquet/part-0000.parquet"

.. format-parquet-pull-couriers-load-settings-partition-end

**Load settings**

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

**Load operations**

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


.. _couriers-legacy-example-cbor:

CBOR
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-cbor-start
   :end-before: .. term-cbor-end

**Load settings for Amazon AWS**

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

**Load settings for Microsoft Azure**

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

**Load operations**

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

.. important:: The ``"schema"`` must match the structure of the incoming file, including all nested groupings and data types. Set ``"nullable"`` to ``True`` to allow fields to contain **NULL** values. A CBOR file can have hundreds of fields. The ellipses (``...``) in this example represents locations within this example structure where additional fields may be present.

.. format-cbor-pull-couriers-load-operations-important-end

.. format-cbor-pull-couriers-load-operations-rowtag-start

.. tip:: Set ``rowTag`` to the element in the CBOR file that should be treated as a row in a table. The default value is ``row``.

.. format-cbor-pull-couriers-load-operations-rowtag-start


.. _couriers-legacy-example-csv:

CSV
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-csv-start
   :end-before: .. term-csv-end

**Load settings with header rows**

.. format-csv-pull-couriers-load-settings-headers-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.csv'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/content-type": "text/csv"
     }
   },

.. format-csv-pull-couriers-load-settings-headers-end

**Load settings with non-standard quotes and separators**

.. format-csv-pull-couriers-load-settings-quotes-separators-example-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.csv'",
     "object/land-as": {
        "file/header-rows": 1,
        "file/tag": "FILE_NAME",
        "file/quote": "'",
        "file/separator": "\\",
        "file/content-type": "text/csv"
     }
   },

.. format-csv-pull-couriers-load-settings-quotes-separators-example-end

**Load settings without header rows**

.. format-csv-pull-couriers-load-settings-headerless-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.csv'",
     "object/land-as": {
        "file/header-rows": 0,
        "file/tag": "FILE_NAME",
        "file/content-type": "text/csv"
     }
   },

.. format-csv-pull-couriers-load-settings-headerless-block-end

**Load operations for feed**

.. format-csv-pull-couriers-load-operations-feed-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "OPERATION",
         "file": "FILE_NAME"
       }
     ]
   }

.. format-csv-pull-couriers-load-operations-feed-end

**Load operations for ingest query**

.. format-csv-pull-couriers-load-operations-ingest-query-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "spark-sql",
         "spark-sql-files": [
           {
             "file": "FILE_NAME",
             "options": {
               "delimiter": ",",
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

.. format-csv-pull-couriers-load-operations-ingest-query-end

.. format-csv-pull-couriers-load-operations-ingest-query-caution-start

.. caution:: Spark does not correctly implement `RFC 4180 <https://tools.ietf.org/html/rfc4180>`__ |ext_link| for escape characters in CSV files. The most common implementations of CSV files expect a double quote ``"`` as an escape character while Spark uses a backslash ``\``. For more information about this issue view the `SPARK-22236 <https://issues.apache.org/jira/browse/SPARK-22236>`__ |ext_link| issue within the Spark project.

   You can override this behavior when working with RFC-compliant CSV files by specifying an escape character in the courier load operations using ``'`` or ``"`` as the escape character.

   For example: 

   .. code-block:: none

      {
        "FEED_ID": [
          {
            "type": "spark-sql",
            "spark-sql-files": [
            {
              "file": "FILE_NAME",
              "options": {
                "escape": "'"
              }
            }
          ],
          "spark-sql-query": "INGEST_QUERY_NAME"
          }
        ]
      }

   If a CSV file uses ``\`` as the delimiter, configure the load operation to specify an empty delimiter value, after which Spark will automatically apply the ``\`` character as the delimiter.

   For example:

   .. code-block:: none

      {
        "FEED_ID": [
          {
            "type": "spark-sql",
            "spark-sql-files": [
            {
              "file": "FILE_NAME",
              "options": {
                "delimiter": ""
              }
            }
          ],
          "spark-sql-query": "INGEST_QUERY_NAME"
          }
        ]
      }

.. format-csv-pull-couriers-load-operations-ingest-query-caution-end


.. _couriers-legacy-example-json:

JSON
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-json-start
   :end-before: .. term-json-end

**Load settings**

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

**Load operations**

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


.. _couriers-legacy-example-ndjson:

NDJSON
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ndjson-start
   :end-before: .. term-ndjson-end

**Load settings**

.. format-ndjson-pull-couriers-load-settings-block-start

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.ndjson'",
     "object/land-as": {
        "file/tag": "FILE_NAME",
        "file/content-type": "application/x-ndjson"
     }
   },

.. format-ndjson-pull-couriers-load-settings-block-end

**Load operations**

.. format-ndjson-pull-couriers-load-operations-block-start

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

.. format-ndjson-pull-couriers-load-operations-block-end


.. _couriers-legacy-example-psv:

PSV
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-psv-start
   :end-before: .. term-psv-end

**Load settings with header rows**

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

**Load settings with non-standard quotes and separators**

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

**Load settings without header rows**

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

**Load operations for feed**

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

**Load operations for ingest query**

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


.. _couriers-legacy-example-salesforce-commerce-cloud:

Salesforce Commerce Cloud
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-commerce-cloud-start
   :end-before: .. term-salesforce-commerce-cloud-end

**Load settings**

.. couriers-legacy-example-salesforce-commerce-cloud-settings-start

The Salesforce Commerce Cloud REST API has a defined set of files that can be made available to Amperity. The load settings are built into Amperity by default. (Salesforce Commerce Cloud was previously known as Demandware.)

.. couriers-legacy-example-salesforce-commerce-cloud-settings-end

.. couriers-legacy-example-salesforce-commerce-cloud-settings-block-start

.. code-block:: none

   [
     {
       "entity-type": "returns",
        "file-tag": "returns-file"
     },
     {
       "entity-type": "customers",
       "file-tag": "customers-file"
     },
     {
       "entity-type": "sites",
       "file-tag": "sites-file"
     },
     {
       "entity-type": "shipping_orders",
       "file-tag": "shipping_orders-file"
     },
     {
       "entity-type": "purchase_orders",
       "file-tag": "purchase_orders-file"
     },
     {
       "entity-type": "vendors",
       "file-tag": "vendors-file"
     },
     {
       "entity-type": "return_orders",
       "file-tag": "return_orders-file"
     },
     {
       "entity-type": "items",
       "file-tag": "items-file"
     },
     {
       "entity-type": "shipments",
       "file-tag": "shipments-file"
     },
     {
       "entity-type": "payments",
       "file-tag": "payments-file"
     },
     {
       "entity-type": "invoices",
       "file-tag": "invoices-file"
     },
     {
       "entity-type": "orders",
       "file-tag": "orders-file",
       "expand": [
         "invoices",
         "order_items"
       ],
       "json-path": "..."
     }
   ]

.. couriers-legacy-example-salesforce-commerce-cloud-settings-block-end

**Load operations**

.. couriers-legacy-example-salesforce-commerce-cloud-operations-block-start

.. code-block:: none

   {
     "SHIPMENTS_FEED_ID": [
       {
         "type": "load",
         "file": "shipments-file"
       }
     ],
     "PURCHASE_ORDERS_FEED_ID": [
       {
         "type": "load",
         "file": "purchase_orders-file"
       }
     ],
     "INVOICES_FEED_ID": [
       {
         "type": "load",
         "file": "invoices-file"
       }
     ],
     "SITES_FEED_ID": [
       {
         "type": "load",
         "file": "sites-file"
       }
     ],
     "RETURN_ORDERS_FEED_ID": [
       {
         "type": "load",
         "file": "return_orders-file"
       }
     ],
     "ORDERS_FEED_ID": [
       {
         "type": "load",
         "file": "orders-file"
       }
     ],
     "PAYMENTS_FEED_ID": [
       {
         "type": "load",
         "file": "payments-file"
       }
     ],
     "ITEMS_FEED_ID": [
       {
         "type": "load",
         "file": "items-file"
       }
     ],
     "VENDORS_FEED_ID": [
       {
         "type": "load",
         "file": "vendors-file"
       }
     ],
     "RETURNS_FEED_ID": [
       {
         "type": "load",
         "file": "returns-file"
       }
     ],
     "SHIPPING_ORDERS_FEED_ID": [
       {
         "type": "load",
         "file": "shipping_orders-file"
       }
     ],
     "CUSTOMERS_FEED_ID": [
       {
         "type": "load",
         "file": "customers-file"
       }
     ]
   }

.. couriers-legacy-example-salesforce-commerce-cloud-operations-block-end


.. _couriers-legacy-example-salesforce-sales-cloud:

Salesforce Sales Cloud
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-sales-cloud-start
   :end-before: .. term-salesforce-sales-cloud-end

**Load settings**

.. couriers-legacy-example-salesforce-sales-cloud-settings-start

The Sales Cloud integration uses SQL patterns to specify which fields in an Object should be brought back to Amperity. Use the ``fields`` grouping to define which fields to bring back. Use ``*`` for all fields, otherwise specify a list of fields. Use ``where`` to specify values in the fields. The following table shows examples of Objects and the equivalent SQL query used to define load settings.

.. couriers-legacy-example-salesforce-sales-cloud-settings-end

.. couriers-legacy-example-salesforce-sales-cloud-settings-block-start

.. code-block:: none

   [
     {
       "from": "ObjectName",
       "file/tag": "objectname-file",
       "fields": [
         "*"
       ]
     },
     {
       "from": "CustomObject",
       "file/tag": "custom-object-file",
       "fields": [
         "*"
       ]
     },
     {
       "from": "AnotherObject",
       "file/tag": "another-object-file",
       "fields": [
         "field-a.name",
         "field-b.name"
       ]
     },
     {
       "from": "Object2",
       "file/tag": "object2-file",
       "fields": [
         "field-one.name",
         "field-two.name"
       ]
       "where": "field-two = 'true'" 
     }
   ]

.. couriers-legacy-example-salesforce-sales-cloud-settings-block-end

.. couriers-legacy-example-salesforce-sales-cloud-settings-start

**Select all fields in an Object**

The following SQL query:

.. code-block:: sql

   SELECT * FROM Account

Is equivalent to the following load operation:

.. code-block:: none

   {
     "from": "Account",
     "file/tag": "account-file",
     "fields": [
       "*"
     ]
   },

**Select fields in an Object with specified values**

The following SQL query:

.. code-block:: sql

   SELECT Id, Name FROM Opportunity
   WHERE Name = 'John'

Is equivalent to the following load operation:

.. code-block:: none

   {
     "from": "Opportunity",
     "file/tag": "opportunity-file",
     "fields": [
       "Id",
       "Name"
     ]
     "where": "Name = 'John'"
   },


**Select only direct reports**

The following SQL query:

.. code-block:: sql

   SELECT *, ReportsTo.Name FROM Contact

Is equivalent to the following load operation:

.. code-block:: none

   {
     "from": "Contact",
     "file/tag": "contact-file",
     "fields": [
       "*",
       "ReportsTo.Name"
     ]
   },


**Select only rows with a certain value in a custom column**

The following SQL query:

.. code-block:: sql

   SELECT * FROM CustomTable__c
   WHERE CustomField__c = 34

Is equivalent to the following load operation:

.. code-block:: none

   {
     "from": "CustomObject",
     "file/tag": "custom-object-file",
     "fields": [
       "*"
     ],
     "where": "CustomField__c = 34"
   },

.. couriers-legacy-example-salesforce-sales-cloud-settings-examples-end

**Load operations**

.. couriers-legacy-example-salesforce-sales-cloud-operations-block-start

.. code-block:: none

   {
     "ACCOUNTS_FEED": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "accounts-file"
       }
     ],
     "CUSTOM_OBJECTS_FEED": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "custom-objects-file"
       }
    ]
   }

.. couriers-legacy-example-salesforce-sales-cloud-operations-block-end


.. _couriers-legacy-example-snowflake:

Snowflake
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-snowflake-start
   :end-before: .. term-snowflake-end

**Load settings**

.. couriers-legacy-example-snowflake-settings-start

For tables in a data warehouse, such as Snowflake, a list of table names must be specified.

.. couriers-legacy-example-snowflake-settings-end

.. couriers-legacy-example-snowflake-settings-block-start

.. code-block:: none

   [
      "table.name",
      "table.name"
   ]

.. couriers-legacy-example-snowflake-settings-block-end

**Load operations**

.. couriers-legacy-example-snowflake-operations-block-start

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "load",
         "file": "marketing.public.customer"
       }
     ]
   }

.. couriers-legacy-example-snowflake-operations-block-end


.. _couriers-legacy-example-streaming-json:

Streaming JSON
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-streaming-json-start
   :end-before: .. term-streaming-json-end

**Load settings**

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

**Load operations**

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


.. _couriers-legacy-example-tsv:

TSV
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-tsv-start
   :end-before: .. term-tsv-end

**Load settings with header rows**

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

**Load settings with non-standard quotes and separators**

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

**Load settings without header rows**

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

**Load operations for feed**

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

**Load operations for ingest query**

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


.. _couriers-legacy-example-xml:

XML
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-xml-start
   :end-before: .. term-xml-end

**Load settings**

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

**Load operations**

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


.. _couriers-legacy-howtos:

How-tos
==================================================

.. couriers-legacy-howtos-list-start

Tasks related to managing couriers in Amperity:

* :ref:`couriers-legacy-add`
* :ref:`couriers-legacy-add-as-copy`
* :ref:`couriers-legacy-add-to-courier-group`
* :ref:`couriers-legacy-delete`
* :ref:`couriers-legacy-edit`
* :ref:`couriers-legacy-load-data-only`
* :ref:`Run and only load files <couriers-legacy-run-only-load-files>`
* :ref:`Run for a specific day <couriers-legacy-run-for-specific-day>`
* :ref:`Run for a time period <couriers-legacy-run-for-time-period>`
* :ref:`Run, but skip missing files <couriers-legacy-run-skip-missing-files>`
* :ref:`couriers-legacy-run-restart-job`
* :ref:`couriers-legacy-view`

.. couriers-legacy-howtos-list-end


.. _couriers-legacy-add:

Add courier
--------------------------------------------------

.. couriers-legacy-add-start

Use the **Add Courier** button to add a courier to Amperity. A courier should be created for each feed that exists in Amperity.

.. couriers-legacy-add-end

.. couriers-legacy-add-context-start

For smaller data sources, a courier may be associated with more than one feed. For larger data sources, a courier should be associated with a single feed. This is, in part, because couriers are run in parallel, but multiple feeds associated with a single courier are run sequentially.

For example: if Snowflake is configured to send six tables to Amperity via six feeds, but all running as part of the same courier, table one must finish before table two, which must finish before table three. Whereas if each table is configured with its own courier, all six tables could start processing at the same time.

A courier configured from the Amperity UI must be configured to use one of the existing plugins in Amperity, such as for Amazon S3, Azure Blob Storage, Azure Data Lake Storage, SFTP, or Snowflake.

Some of these plugins have more than one option for credentials.

Use SnapPass to securely share configuration data with your Amperity representative.

.. couriers-legacy-add-context-end

**To add a courier**

.. couriers-legacy-add-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Courier** page opens.
#. Enter the name of the courier.
#. From the **Plugin** dropdown, select a plugin.

   .. note:: The settings for a courier varies, depending on the courier selected from the **Plugin** dropdown.

#. Enter the credentials for the courier type.
#. Enter any courier-specific settings.
#. Under **<COURIER NAME> Settings** configure the file load settings. This is done in two parts: a list of files that should be available to Amperity (including how they are made available), and then a series of load operations that associates each file in the list to a feed.
#. Click **Save**.

.. couriers-legacy-add-steps-end


.. _couriers-legacy-add-as-copy:

Add courier as copy
--------------------------------------------------

.. couriers-legacy-add-as-copy-start

You may add a courier by copying an existing courier. This is useful when couriers share plugin, credential, and other common settings. A copied courier retains all of the configured settings as the original, but will be assigned a unique name based on the name of the copied courier.

.. couriers-legacy-add-as-copy-end

**To add a courier as a copy**

.. couriers-legacy-add-as-copy-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Make a copy**. The **Add Courier** page opens.
#. Update the name of the courier.
#. Verify all other configuration settings. Edit them as necessary.
#. Under **<COURIER NAME> Settings** configure the file load settings. This is done in two parts: a list of files that should be available to Amperity (including how they are made available), and then a series of load operations that associates each file in the list to a feed.
#. Click **Save**.

.. couriers-legacy-add-as-copy-steps-end


.. _couriers-legacy-add-to-courier-group:

Add to courier group
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add a courier to a courier group**

.. couriers-legacy-add-to-courier-group-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Edit**.
#. On the **Couriers** tab, click the **Add courier** link.
#. Select the name of a courier from the dropdown list, set the wait time and range for which data is loaded. Enable alerts for when files are missing.
#. Click **Save**.

.. couriers-legacy-add-to-courier-group-steps-end


.. _couriers-legacy-delete:

Delete courier
--------------------------------------------------

.. couriers-legacy-delete-start

Use the **Delete** option to remove a courier from Amperity. Verify that both upstream and downstream processes no longer depend on this courier before you delete it. This action will *not* delete the feeds associated with the courier.

.. couriers-legacy-delete-end

**To delete a courier**

.. couriers-legacy-delete-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Delete**. The **Delete Courier** dialog box opens.
#. Click **Delete**.

.. couriers-legacy-delete-steps-end


.. _couriers-legacy-edit:

Edit courier
--------------------------------------------------

.. couriers-legacy-edit-start

Use the **Edit** option in the row for a specific courier to make configuration changes. For example, a new file is added to an Amazon S3 filedrop location already configured to send data to Amperity. After the feed is created, it can be added to the existing courier objects and load operations.

In other cases, a courier may need editing because the credentials to the data source have changed. 

.. couriers-legacy-edit-end

**To edit a courier**

.. couriers-legacy-edit-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Edit**. The **Edit Courier** page opens.
#. Make your changes.
#. Click **Save**.

.. couriers-legacy-edit-steps-end


.. _couriers-legacy-load-data-only:

Load data only
--------------------------------------------------

.. couriers-legacy-load-data-only-start

A courier can be run to load data to a domain table and prevent downstream processes, such as Stitch, customer 360 database runs, queries, and orchestrations.

.. couriers-legacy-load-data-only-end

**To load data (without downstream processing)**

.. couriers-legacy-load-data-only-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific day** or **Load data from a specific time period**.
#. To prevent downstream processing, select **Ingest only**.
#. Click **Run**.

.. couriers-legacy-load-data-only-steps-end


.. _couriers-legacy-run:

Run couriers
--------------------------------------------------

.. couriers-legacy-run-start

Use the **Run** option to run the courier manually.

.. couriers-legacy-run-end

A courier can be run in the following ways:

* :ref:`Only load files <couriers-legacy-run-only-load-files>`
* :ref:`Run for a specific day <couriers-legacy-run-for-specific-day>`
* :ref:`Run for a time period <couriers-legacy-run-for-time-period>`
* :ref:`Skip missing files <couriers-legacy-run-skip-missing-files>`
* :ref:`With empty load operation <couriers-legacy-run-with-empty-load-operation>`


.. _couriers-legacy-run-only-load-files:

Only load files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-run-only-load-files-start

A courier can be configured to load data, but not start any downstream processing, including Stitch, database generation, or queries.

.. warning:: Stitch must be run for data to be available in databases. Jobs that are run as load only do not automatically run Stitch.

.. couriers-legacy-run-only-load-files-end

**To run a courier without downstream processing**

.. couriers-legacy-run-without-downstream-processing-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific day** or **Load data from a specific time period**.
#. Under **Load options**, select **Ingest only**.
#. Click **Run**.

.. couriers-legacy-run-without-downstream-processing-steps-end


.. _couriers-legacy-run-for-specific-day:

Run for a specific day
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-run-for-specific-day-start

A courier can be configured to load data from a specific day.

.. couriers-legacy-run-for-specific-day-end

**To run a courier and load data from a specific day**

.. couriers-legacy-run-for-specific-day-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific day**.
#. Select a calendar date.
#. To prevent downstream processing, select **Ingest only**.

   .. warning:: When a data source is changed, and then loaded using the **Ingest only** option, downstream processes are not started automatically. Data that contains PII must be stitched. Databases that contain interaction records must be regenerated so that attributes and predictions are recalculated.
#. Click **Run**.

.. couriers-legacy-run-for-specific-day-steps-end


.. _couriers-legacy-run-for-time-period:

Run for a time period
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-run-for-time-period-start

A courier can be configured to load all data from a specified time period.

.. couriers-legacy-run-for-time-period-end

**To run a courier to load all data from a specific time period**

.. couriers-legacy-run-for-time-period-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific time period**.
#. Select a start date and an end date.

   .. important:: The start of the selected date range is inclusive, whereas the end of the selected date range is exclusive.
#. To prevent downstream processing, select **Ingest only**.

   .. warning:: When a data source is changed, and then loaded using the **Ingest only** option, downstream processes are not started automatically. Data that contains PII must be stitched. Databases that contain interaction records must be regenerated so that attributes and predictions are recalculated.
#. Click **Run**.

.. couriers-legacy-run-for-time-period-steps-end


.. _couriers-legacy-run-skip-missing-files:

Skip missing files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-run-skip-missing-files-start

A courier can be configured to skip sources files that are missing and continue running.

.. couriers-legacy-run-skip-missing-files-end

**To skip missing files**

.. couriers-legacy-run-skip-missing-files-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific day** or **Load data from a specific time period**.
#. Under **Load options**, select **Skip missing files**.
#. Click **Run**.

.. couriers-legacy-run-skip-missing-files-steps-end


.. _couriers-legacy-run-with-empty-load-operation:

With empty load operation
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-run-without-load-operations-start

You can run a courier with an empty load operation using ``{}`` as the value for the load operation. Use this approach to get files to upload during feed creation, as a feed requires knowing the schema of a file before you can apply semantic tagging and other feed configuration settings.

.. couriers-legacy-run-without-load-operations-end


.. _couriers-legacy-view-errors:

View error log
--------------------------------------------------

.. couriers-legacy-view-errors-start

If a courier runs and returns an error, you may view the errors from that feed.

.. couriers-legacy-view-errors-end

**To view errors**

.. couriers-legacy-view-errors-steps-start

#. From the **Notifications** pane, for the stage error, open the **View Load Details** link.
#. From the **View Load Details** pane, select **View Error Log** for the feed with errors.
#. Investigate the errors reported.

.. couriers-legacy-view-errors-steps-end


.. _couriers-legacy-run-restart-job:

Restart job
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-legacy-run-restart-job-start

If a courier runs and returns an error, you may view the error, resolve that error by updating the feed configuration or Spark SQL query, and then restart it without having to reload the data associated with the job.

.. couriers-legacy-run-restart-job-end

**To restart a job**

.. couriers-legacy-run-restart-job-steps-start

#. From the **Notifications** pane, for the stage error, open the **View Load Details** link and investigate why the job failed.
#. Edit the feed configuration or Spark SQL query to address the reasons for the error.
#. From the **Notifications** pane, click **Restart Ingest Job**.

.. couriers-legacy-run-restart-job-steps-end


.. _couriers-legacy-view:

View courier
--------------------------------------------------

.. couriers-legacy-view-start

The **Sources** page shows the status of every courier, including when it last ran or updated, and its current status.

.. couriers-legacy-view-end

**To view a courier**

.. couriers-legacy-view-steps-start

From the **Sources** page, open the menu for a courier, and then select **View**. The **View Courier** page opens.

.. couriers-legacy-view-steps-end