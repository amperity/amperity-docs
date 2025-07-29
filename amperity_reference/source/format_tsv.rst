.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About TSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About TSV files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        TSV files

==================================================
TSV files
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

The size of a TSV file cannot exceed 10 GB. A TSV file that is larger than 10 GB must be split into smaller files before it is made available to Amperity. The total number of TSV files in a single ingest job cannot exceed 500,000.

.. format-tsv-file-sizes-end


.. _format-tsv-pull:

Pull TSV files
==================================================

.. format-tsv-pull-start

To pull TSV files to Amperity:

#. Select a :ref:`data source <format-tsv-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the TSV file <format-tsv-pull-couriers>`.
#. Define a :ref:`feed to associate fields in the TSV file with semantic tags <format-tsv-pull-feeds>`.

.. format-tsv-pull-end


.. _format-tsv-pull-data-sources:

Data sources
--------------------------------------------------

.. format-tsv-pull-data-sources-start

Pull TSV files to Amperity using one of the following data sources:

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

Use a feed to associate fields in the TSV file with semantic tags and a courier to pull the TSV file from its upstream data source.

* :ref:`Couriers <format-tsv-pull-couriers>`
* :ref:`Feeds <format-tsv-pull-feeds>`

.. format-tsv-pull-load-data-end


.. _format-tsv-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-tsv-pull-couriers-start

A courier must specify the location of the TSV file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-tsv-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-tsv-pull-couriers-feed-selection>`

.. format-tsv-pull-couriers-end


.. _format-tsv-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the TSV file and to define formattting within the file, such as escape character, quote charcter, compression type or header row.

.. format-tsv-pull-couriers-file-settings-start


.. _format-tsv-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-tsv-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then which files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-tsv-pull-couriers-feed-selection-end


.. _format-tsv-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-tsv-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-tsv-pull-feeds-end


.. _format-tsv-pull-feeds-domain-sql:

Domain SQL
--------------------------------------------------

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


.. _format-tsv-destination:

Send TSV files
==================================================

.. format-tsv-destination-links-start

Amperity can send TSV files to downstream workflows using any of the following destinations:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-tsv-destination-links-end


.. _format-tsv-destination-split-outputs-start:

Split outputs
--------------------------------------------------

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-split-outputs-start
   :end-before: .. setting-common-split-outputs-end
