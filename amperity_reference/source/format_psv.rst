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


.. _format-psv-file-sizes:

File sizes
==================================================

.. format-psv-file-sizes-start

The size of a PSV file cannot exceed 10 GB. A PSV file that is larger than 10 GB must be split into smaller files before it is made available to Amperity. The total number of PSV files in a single ingest job cannot exceed 500,000.

.. format-psv-file-sizes-end


.. _format-psv-pull:

Pull PSV files
==================================================

.. format-psv-pull-start

To pull PSV files to Amperity:

#. Select a :ref:`data source <format-psv-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the PSV file <format-json-streaming-pull-couriers>`.
#. Define a :ref:`feed to associate the fields that were selected from the PSV file with semantic tags <format-json-streaming-pull-feed>` for customer profiles and interactions, as necessary.

.. format-psv-pull-end


.. _format-psv-pull-data-sources:

Data sources
--------------------------------------------------

.. format-psv-pull-data-sources-start

Pull PSV files to Amperity using one of the following data sources:

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

Use a feed to associate fields in the PSV file with semantic tags and a courier to pull the PSV file from its upstream data source.

* :ref:`Couriers <format-psv-pull-couriers>`
* :ref:`Feeds <format-psv-pull-feeds>`

.. format-psv-pull-load-data-end


.. _format-psv-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-psv-pull-couriers-start

A courier must specify the location of the PSV file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-psv-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-psv-pull-couriers-feed-selection>`

.. format-psv-pull-couriers-end


.. _format-psv-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the PSV file and to define formattting within the file, such as escape character, quote charcter, compression type or header row.

.. format-psv-pull-couriers-file-settings-start


.. _format-psv-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-psv-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then which files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-psv-pull-couriers-feed-selection-end


.. _format-psv-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-psv-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-psv-pull-feeds-end


.. _format-psv-pull-feeds-domain-sql:

Domain SQL
--------------------------------------------------

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


.. _format-psv-destination:

Send PSV files
==================================================

.. format-psv-destination-links-start

Amperity can send PSV files to downstream workflows using any of the following destinations:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-psv-destination-links-end


.. _format-psv-destination-split-outputs-start:

Split outputs
--------------------------------------------------

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-split-outputs-start
   :end-before: .. setting-common-split-outputs-end
