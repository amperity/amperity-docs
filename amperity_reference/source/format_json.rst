.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About JSON files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About JSON files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        JSON files

==================================================
JSON files
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-json-start
   :end-before: .. term-json-end

.. format-json-streaming-ingest-start

.. note:: JSON data that is sent to the |api_streaming_ingest| is converted to :doc:`NDJSON format <format_ndjson>`.

.. format-json-streaming-ingest-end


.. _format-json-pull:

Pull JSON files
==================================================

.. format-json-pull-start

To pull JSON files to Amperity:

#. Select a :ref:`filedrop data source <format-json-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the JSON file <format-json-pull-couriers>`.
#. Define a :ref:`feed to associate the fields in the JSON file with semantic tags <format-json-pull-feed>` for customer profiles and interactions, as necessary.

.. format-json-pull-end


.. _format-json-pull-data-sources:

Data sources
--------------------------------------------------

.. format-json-pull-data-sources-start

Pull JSON files to Amperity using any one of the following data sources:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-json-pull-data-sources-end


.. _format-json-pull-data-sources-recommendations:

Recommendations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-json-pull-data-sources-recommendations-start

When using JSON files, it is recommend to:

* Do use simple nested data structures. Do not use nested array data structures

  **DO**

  .. code-block:: json

     {
       "employee":{ "name":"John", "age":30, "city":"New York" }
     }

  **DO NOT**

  .. code-block:: json

     {
       "employees":[ "John", "Anna", "Peter" ]
     }

* Quote string data
* Quote date values and use the supported date format
* Ensure numeric data is not quoted
* Encode files in UTF-8 or UTF-16. Amperity automatically detects the 2-byte header present with the UTF-16 encoding format. If the 2-byte header is missing, the file is treated as UTF-8.

  .. caution::

     .. include:: ../../shared/file-formats.rst
        :start-after: .. formats-json-rfc-8259-start
        :end-before: .. formats-json-rfc-8259-end

* Compress files prior to encryption using ZIP, GZIP, or TAR
* Encrypt files using PGP. Compression will not reduce the size of an encrypted file

.. format-json-pull-data-sources-recommendations-end


.. _format-json-pull-load-data:

Load data
--------------------------------------------------

.. format-json-pull-load-data-start

Use a feed to associate fields in the JSON file with semantic tags and a courier to pull the JSON file from its upstream data source.

* :ref:`Couriers <format-json-pull-couriers>`
* :ref:`Feeds <format-json-pull-feed>`

.. format-json-pull-load-data-end


.. _format-json-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-json-pull-couriers-start

A courier must specify the location of the JSON file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-json-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-json-pull-couriers-feed-selection>`

.. format-json-pull-couriers-end


.. _format-json-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-json-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the JSON file and to define formattting within the file.

.. format-json-pull-couriers-file-settings-start


.. _format-json-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-json-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Spark** Use this option to load data when the JSON file contains complex types, such as nested objects and arrays.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-json-pull-couriers-feed-selection-end


.. _format-json-pull-feed:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-json-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-json-pull-feeds-end

.. format-json-pull-feeds-important-start

.. important:: A feed uses the first record in a JSON file to determine its schema in the **Feed Editor**. If records contain optional fields and those records are *not the first record* you must add those fields to the feed definition manually.

.. format-json-pull-feeds-important-end


.. _format-json-destination:

Send JSON files
==================================================

.. format-json-destination-links-start

Amperity can send JSON files to downstream workflows using any of the following destinations:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-json-destination-links-end
