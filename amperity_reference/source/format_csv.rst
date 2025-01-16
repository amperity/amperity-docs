.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About CSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About CSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: CSV

==================================================
File format: CSV
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-csv-start
   :end-before: .. term-csv-end

.. format-csv-tip-start

.. tip:: Consider using :doc:`Apache Avro <format_avro>` and :doc:`Apache Parquet <format_parquet>` file formats instead of CSV. 

   * Avro uses a JSON-like schema that stores data in rows. Avro files have a very small file size that transfers quickly.
   * Parquet is highly compact, can be transferred easily, and avoids escape character and data formatting issues that can be present in other formats.

.. format-csv-tip-end


.. _format-csv-double-quotes:

Double quotes
==================================================

.. format-csv-double-quotes-start

|ext_rfc4180| has the following guidelines for the use of double quotes in CSV files:

* A field may or may not be enclosed by double quotes. When a field is not enclosed by double quotes, double quotes may not appear inside a field.
* A field that contains line breaks (CRLF), double quotes, and/or commas should be enclosed in double quotes.
* When a field is enclosed by double quotes, a double quote that appears inside a field must be escaped using a double quote.

When an escape character is not specified, Amperity will assume that the escape character is double quotes. This follows the RFC as closely as possible: "If double quotes are used to enclose fields, then a double quote appearing inside a field must be escaped by preceding it with another double quote."

CSV files, generally, do not have a formal specification, which allows for a wide variety of implementations that can create very specific problems.

If you notice data quality issues from a data source that uses a CSV file, consider updating that CSV file to adhere to the RFC as closely as possible, including applying a consistent approach for the use of double quotes, and then ensuring the escape character is compatible with the data provided by that data source.

For example, many Polynesian languages use an apostrophe (') or a single quote (ʻ) at the start of (and within) first, last, and location names: Hawai'i, O'ahu, Kau'i, U'ilani. In Hawai'ian, a grave accent (`\``) is often used instead of an apostrophe: Hawai\`ian. (Apostrophes within names is, of course, not unique to Polynesian languages.)

A courier configuration similar to:

.. code-block:: none

   {
     "object/type": "file",
     "object/file-pattern": "'path/to/file'-YYYY-MM-dd'.csv'",
     "object/land-as": {
       "file/escape": "?",
       "file/quote": """
     }
   },

will allow string values like:

::

   "Kau'i","Hawai'i","O'ahu","A description of 'places'"

and:

::

   Kau'i,Hawai'i,O'ahu,A description of 'places'

If the escape character is a single quote (``"file/escape": "'"``), similar string values must be escaped:

::

   Kau''i,Hawai''i,O''ahu,A description of ''places''

.. format-csv-double-quotes-end


.. _format-csv-pull:

Pull CSV files
==================================================

.. format-csv-pull-start

To pull CSV files to Amperity:

#. Select a :ref:`filedrop data source <format-csv-pull-data-sources>`.
#. Define a :ref:`feed to associate fields in the CSV file with semantic tags <format-csv-pull-feeds>`; in some situations you may need to use an :ref:`ingest query to transform data in the CSV file <format-csv-pull-ingest-queries>` prior to loading it to Amperity.
#. Configure a courier for :ref:`the location and name of the CSV file <format-csv-pull-couriers-load-settings>`, and then for :ref:`the load operation <format-csv-pull-couriers-load-operations>` (either directly from a feed or from an ingest query).

.. format-csv-pull-end


.. _format-csv-pull-data-sources:

Data sources
--------------------------------------------------

.. format-csv-pull-data-sources-start

Pull CSV files to Amperity using any filedrop data source:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-csv-pull-data-sources-end


.. _format-csv-pull-data-sources-recommendations:

Recommendations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-csv-pull-data-sources-recommendations

When using CSV files, it is recommend to:

* Use column headers (with no special characters except underscores)

  .. note:: When loading data from a CSV file that does not have headers, all fields in the feed are enabled and are required.

* Ensure duplicate header names are not present
* Ensure one (or more) fields are present that can act as a unique identifier
* Use a comma as the delimiter for fields; use a newline character as the delimiter for rows
* Escape commas or quotes that appear in the data
* Quote string values
* Encode files in UTF-8 or UTF-16. Amperity automatically detects the 2-byte header present with the UTF-16 encoding format. If the 2-byte header is missing, the file is treated as UTF-8.
* Compress files prior to encryption using ZIP, GZIP, and/or TAR. Amperity automatically decompresses GZIP files; ZIP and TAR decompression must be specified in courier file load settings.
* Encrypt files using PGP; compression will not reduce the size of an encrypted file

.. format-csv-pull-data-sources-recommendations


.. _format-csv-pull-load-data:

Load data
--------------------------------------------------

.. format-csv-pull-load-data-start

For most CSV files, use a feed to associate fields in the CSV file with semantic tags. In some situations, an ingest query may be necessary to transform data prior to loading it to Amperity.

* :ref:`Feeds <format-csv-pull-feeds>`
* :ref:`Ingest queries <format-csv-pull-ingest-queries>`

.. format-csv-pull-load-data-end


.. _format-csv-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-csv-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand how field relationships should be understood when those values are present across your data sources.

.. format-csv-pull-feeds-end


.. _format-csv-pull-feeds-domain-sql:

Domain SQL
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-domain-sql-start
   :end-before: .. term-domain-sql-end

.. format-csv-pull-feeds-domain-sql-start

Domain SQL allows the data in CSV files to be transformed *after* it has been loaded to Amperity. Some common use cases for using domain SQL to transform data include:

* :ref:`Combining days, months, and years into a single birthdate field <domain-tables-custom-sql-use-case-combine-birthdate>`
* :ref:`Combining postal codes <domain-tables-custom-sql-use-case-combine-postal>`
* :ref:`Extracting first and last names <domain-tables-custom-sql-use-case-extract-names>`
* :ref:`Hashing profile (PII) data <domain-tables-custom-sql-use-case-rehash-data>`
* :ref:`Parsing fields with multiple separators <domain-tables-custom-sql-use-case-parse-fields-with-multiple-separators>`
* :ref:`Setting non-US-ASCII email addresses to NULL <domain-tables-custom-sql-use-case-set-email-to-null>`
* :ref:`Standardizing values for USA states <domain-tables-custom-sql-use-case-standardize-values-for-usa-states>`

.. format-csv-pull-feeds-domain-sql-end


.. _format-csv-pull-ingest-queries:

Ingest queries
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. format-csv-pull-ingest-queries-start

Use :doc:`Spark SQL <sql_spark>` to :doc:`define an ingest query <ingest_queries>` for the CSV file. Use a **SELECT** statement to specify which fields should be loaded to Amperity. Apply transforms to those fields as necessary.

.. format-csv-pull-ingest-queries-end


.. _format-csv-pull-ingest-queries-flatten-rows:

Flatten rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-ingest-queries-flatten-rows-start

Some CSV output contains rows where a field within that row contains multiple lines of data. For example, conversions data pulled from Attentive Mobile has a field named ``message_text`` that contains the lines of an SMS message using ``\n`` to separate each line of the message.

This should be flattened using an ingest query to remove the ``\n`` prior to pulling this data to Amperity. For example:

.. code-block:: none

   SELECT 
     client_id
     ,phone
     ,message_id
     ,message_name
     ,REGEXP_REPLACE(message_text,"\n","") AS message_text
     ...
   FROM AttentiveTable

.. format-csv-pull-ingest-queries-flatten-rows-end


.. _format-csv-pull-ingest-queries-nested-records:

Nested records
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-ingest-queries-nested-records-start

Occasionally, a CSV file will contain nested records. For example, a field within the CSV file contains JSON data similar to:

.. code-block:: none

   [{"street": "123 Main Street", "apt": "101", "city": "Seattle", "state": "WA", "zip": "98101"}]

which is JSON data in a nested format:

.. code-block:: none

   [
     {
       "street": "123 Main Street",
       "apt": "101",
       "city": "Seattle",
       "state": "WA",
       "zip": "98101"
     }
   ]

There are two general approaches to take when a CSV file contains nested records:

#. Recommended. The customer should update the process for how the data is provided to Amperity to ensure the file does not contain nested records.
#. If the file cannot be provided without nested records, use an ingest query to flatten the data in these fields prior to loading it to Amperity.

   .. note:: This will increase the preprocessing effort required by Amperity. Large datasets will take more time and this approach should be avoided with very large datasets and should be used carefully with datasets that will be processed on a daily basis.

For example:

.. code-block:: sql

   WITH explodedData AS (
     SELECT
       table_id
       ,EXPLODE(combined_address) AS address FROM Source
   )

   SELECT
     table_id
     ,address.street AS address
     ,address.apt AS address2
     ,address.city AS city
     ,address.state AS state
     ,address.zip AS postal
   FROM Source

.. format-csv-pull-ingest-queries-nested-records-end


.. _format-csv-pull-ingest-queries-ordinals:

Ordinal column names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-ingest-queries-ordinals-start

Some situations require using an ingest query to load a headerless CSV file. Use a **SELECT** statement to apply ordinal column names, and then aliasing each column name to a field name if desired.

A headerless file should use column names that are based on ordinal positions using the following pattern:

.. code-block:: none

   _c0
   _c1
   _c2
   _c3
   ...
   _cN

Add these column names within the **SELECT** statement. You may use aliasing to apply better column names within the ingest query.

For example, using ordinal columns to define a schema for profile data:

.. code-block:: sql

   SELECT
     _c0 AS user_id
     ,_c1 AS given_name
     ,_c2 AS surname
     ,_c3 AS email
     ,_c4 AS phone
   FROM table

.. format-csv-pull-ingest-queries-ordinals-end


.. _format-csv-pull-couriers:

Couriers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-csv-pull-couriers-start

A courier must specify the location of the CSV file, and then define how that file is to be pulled to Amperity. This is done using a combination of configuration blocks:

#. :ref:`Load settings <format-csv-pull-couriers-load-settings>`
#. :ref:`Load operations <format-csv-pull-couriers-load-operations>`

.. format-csv-pull-couriers-end


.. _format-csv-pull-couriers-load-settings:

Load settings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-csv-pull-couriers-load-settings-start

Use courier load settings to specify the path to the CSV file, a file tag (which can be the same as the name of the CSV file), if the file does not contain header rows, and the ``"text/csv"`` content type.

With some CSV files it may be necessary to specify the character used for quotes and the character used as a separator.

.. format-csv-pull-couriers-load-settings-start


.. _format-csv-pull-couriers-load-settings-headers:

with header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-couriers-load-settings-headers-start

Most CSV files contain a row of data that defines header rows for the data set. Configure the load settings for the courier to accept the header rows.

.. format-csv-pull-couriers-load-settings-headers-end

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


.. _format-csv-pull-couriers-load-settings-quotes-separators:

with non-standard quotes and separators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-couriers-load-settings-quotes-separators-start

Some CSV files may use non-standard characters for quotes and separators, such as ``'`` for quotes and ``\`` for separators. If a CSV file contains non-standard characters, you must specify these characters in the courier load settings.

.. format-csv-pull-couriers-load-settings-quotes-separators-end

.. format-csv-pull-couriers-load-settings-quotes-separators-important-start

.. important:: The syntax used within courier configuration blocks is JSON, which uses a backslash as the escape character. You must escape a backslash in JSON using a backslash: ``"file/escape": "\\"`` (and not ``"file/escape": "\"``).

.. format-csv-pull-couriers-load-settings-quotes-separators-important-end

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


.. _format-csv-pull-couriers-load-settings-headerless:

without header rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-couriers-load-settings-headerless-start

A headerless CSV file does not contain a row of data that defines headers for the data set. When working with a headerless CSV file you can configure the load settings for the courier to accept headerless files or you may use an ingest query when the data must be changed in some way prior to loading it to Amperity.

.. format-csv-pull-couriers-load-settings-headerless-end

.. format-csv-pull-couriers-load-settings-headerless-tip-start

.. tip:: Before using an ingest query to change data *prior* to loading it to Amperity, consider using domain SQL *after* it has been loaded to Amperity. Using domain SQL allows for easier changes to data schemas and (more importantly) does not require data to be truncated, and then reloaded on a regular basis.

.. format-csv-pull-couriers-load-settings-headerless-tip-end

.. format-csv-pull-couriers-load-settings-headerless-start

If a CSV file is headerless, change the load setting for ``"file/header-rows"`` from ``1`` to ``0``.

.. format-csv-pull-couriers-load-settings-headerless-end

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


.. _format-csv-pull-couriers-load-settings-wildcards-in-archives:

wildcards in archives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../amperity_reference/source/couriers.rst
   :start-after: .. couriers-files-patterns-wildcards-within-archives-start
   :end-before: .. couriers-files-patterns-wildcards-within-archives-end


.. _format-csv-pull-couriers-as400:

AS/400
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-couriers-as400-start

AS/400 is a computer platform that can provide raw data to Amperity as zipped CSV files configured as a one-time export or as a recurring export. For recurring exports, the customer must set up a workflow that collects this data, and then puts it into a location from which Amperity can pull data (Amazon S3, Azure Blob Storage, Google Cloud Storage, or SFTP).

#. Data must be configured to be exported as a collection of zipped CSV tables. For example, tables for customer profiles, orders, order items, shipments, emails, and so on.
#. Records within these tables should have a common identifier, such as a customer number. Use this identifier for foreign key tagging within feeds.
#. A data dictionary must be defined for these tables, and then provided to Amperity.
#. Verify date formats. These may require additional processing within Amperity that transforms them into the preferred format.
#. Review the data within the tables, and then use domain SQL for additional data shaping, as necessary.

.. format-csv-pull-couriers-as400-end


.. _format-csv-pull-couriers-load-operations:

Load operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-csv-pull-couriers-load-operations-start

Use courier load operations to associate a feed ID to the courier, apply the same file tag as the one used for load settings. Load operations for an ingest query may specify a series of options.

.. format-csv-pull-couriers-load-operations-end


.. _format-csv-pull-couriers-load-operations-feed:

Load from feed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


.. _format-csv-pull-couriers-load-operations-ingest-query:

Load from ingest query
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. caution:: Spark does not correctly implement |ext_rfc4180| for escape characters in CSV files. The most common implementations of CSV files expect a double quote ``"`` as an escape character while Spark uses a backslash ``\``. For more information about this issue view the `SPARK-22236 <https://issues.apache.org/jira/browse/SPARK-22236>`__ |ext_link| issue within the Spark project.

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


.. _format-csv-destination:

Send CSV files
==================================================

.. format-csv-destination-links-start

Amperity can send CSV files to downstream workflows using any filedrop destination:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-csv-destination-links-end
