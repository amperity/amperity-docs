.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About CSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About CSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        CSV files

==================================================
CSV files
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-csv-start
   :end-before: .. term-csv-end

.. format-csv-tip-start

.. tip:: Consider using :doc:`Apache Avro <format_avro>` and :doc:`Apache Parquet <format_parquet>` file formats instead of CSV. 

   * Avro uses a JSON-like schema that stores data in rows. Avro files have a very small file size that transfers quickly.
   * Parquet is highly compact, can be transferred easily, and avoids escape character and data formatting issues that can be present in other formats.

.. format-csv-tip-end


.. _format-csv-file-sizes:

File sizes
==================================================

.. format-csv-file-sizes-start

The size of a CSV file cannot exceed 10 GB. A CSV file that is larger than 10 GB must be split into smaller files before it is made available to Amperity. The total number of CSV files in a single ingest job cannot exceed 500,000.

.. format-csv-file-sizes-end


.. _format-csv-double-quotes:

Double quotes
==================================================

.. format-csv-double-quotes-start

`RFC 4180 <https://tools.ietf.org/html/rfc4180>`__ |ext_link| has the following guidelines for the use of double quotes in CSV files:

* A field may or may not be enclosed by double quotes. When a field is not enclosed by double quotes, double quotes may not appear inside a field.
* A field that contains line breaks (CRLF), double quotes, and/or commas should be enclosed in double quotes.
* When a field is enclosed by double quotes, a double quote that appears inside a field must be escaped using a double quote.

When an escape character is not specified, Amperity will assume that the escape character is double quotes. This follows the RFC as closely as possible: "If double quotes are used to enclose fields, then a double quote appearing inside a field must be escaped by preceding it with another double quote."

CSV files, generally, do not have a formal specification, which allows for a wide variety of implementations that can create very specific problems.

If you notice data quality issues from a data source that uses a CSV file, consider updating that CSV file to adhere to the RFC as closely as possible, including applying a consistent approach for the use of double quotes, and then ensuring the escape character is compatible with the data provided by that data source.

For example, many Polynesian languages use an apostrophe (') or a single quote (ʻ) at the start of (and within) first, last, and location names: Hawai'i, O'ahu, Kau'i, U'ilani. In Hawai'ian, a grave accent (`\``) is often used instead of an apostrophe: Hawai\`ian. (Apostrophes within names is not unique to Polynesian languages.)

A courier quote configuration similar to ``"""`` will allow string values like:

::

   "Kau'i","Hawai'i","O'ahu","A description of 'places'"

and:

::

   Kau'i,Hawai'i,O'ahu,A description of 'places'

If the escape character is a single quote (``"'"``), similar string values must be escaped:

::

   Kau''i,Hawai''i,O''ahu,A description of ''places''

.. format-csv-double-quotes-end


.. _format-csv-pull:

Pull CSV files
==================================================

.. format-csv-pull-start

To pull CSV files to Amperity:

#. Select a :ref:`data source <format-csv-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the CSV file <format-csv-pull-couriers>`.
#. Define a :ref:`feed to associate fields in the CSV file with semantic tags <format-csv-pull-feeds>`.

.. format-csv-pull-end


.. _format-csv-pull-data-sources:

Data sources
--------------------------------------------------

.. format-csv-pull-data-sources-start

Pull CSV files to Amperity using one of the following data sources:

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

Use a feed to associate fields in the CSV file with semantic tags and a courier to pull the CSV file from its upstream data source.

* :ref:`Couriers <format-csv-pull-couriers>`
* :ref:`Feeds <format-csv-pull-feeds>`

.. format-csv-pull-load-data-end


.. _format-csv-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-csv-pull-couriers-start

A courier must specify the location of the CSV file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-csv-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-csv-pull-couriers-feed-selection>`

.. format-csv-pull-couriers-end


.. _format-csv-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the CSV file and to define formattting within the file, such as escape character, quote charcter, compression type or header row.

.. format-csv-pull-couriers-file-settings-start


.. _format-csv-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-csv-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then which files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-csv-pull-couriers-feed-selection-end


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


.. _format-csv-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-csv-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-csv-pull-feeds-end


.. _format-csv-pull-feeds-domain-sql:

Domain SQL
--------------------------------------------------

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


.. _format-csv-destination:

Send CSV files
==================================================

.. format-csv-destination-links-start

Amperity can send CSV files to downstream workflows using any of the following destinations:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-csv-destination-links-end


.. _format-csv-destination-split-outputs-start:

Split outputs
--------------------------------------------------

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-split-outputs-start
   :end-before: .. setting-common-split-outputs-end