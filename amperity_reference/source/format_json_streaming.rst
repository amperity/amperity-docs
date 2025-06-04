.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About using streaming JSON files as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About using streaming JSON files as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: Streaming JSON

==================================================
File format: Streaming JSON
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-streaming-json-start
   :end-before: .. term-streaming-json-end


.. _format-json-streaming-pull:

Pull streaming JSON files
==================================================

.. format-json-streaming-pull-start

To pull streaming JSON files to Amperity:

#. Select a :ref:`data source <format-json-streaming-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the streaming JSON file <format-json-streaming-pull-couriers>`.
#. Define a :ref:`feed to associate the fields that were selected from the streaming JSON file with semantic tags <format-json-streaming-pull-feed>` for customer profiles and interactions, as necessary.

.. format-json-streaming-pull-end


.. _format-json-streaming-pull-data-sources:

Data sources
--------------------------------------------------

.. format-json-streaming-pull-data-sources-start

Pull streaming JSON files to Amperity using one of the following data sources:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-json-streaming-pull-data-sources-end


.. _format-json-streaming-pull-load-data:

Load data
--------------------------------------------------

.. format-json-pull-load-data-start

Use a feed to associate fields in the streaming JSON file with semantic tags and a courier to pull the streaming JSON file from its upstream data source.

* :ref:`Couriers <format-json-pull-couriers>`
* :ref:`Feeds <format-json-pull-feed>`

.. format-json-pull-load-data-end


.. _format-json-streaming-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-json-streaming-pull-couriers-start

A courier must specify the location of the streaming JSON file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-json-streaming-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-json-streaming-pull-couriers-feed-selection>`

.. format-json-streaming-pull-couriers-end


.. _format-json-streaming-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-json-streaming-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the streaming JSON file and to define formattting within the file.

.. format-json-streaming-pull-couriers-file-settings-start


.. _format-json-streaming-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-json-streaming-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-json-streaming-pull-couriers-feed-selection-end


.. _format-json-streaming-pull-feed:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-json-streaming-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-json-streaming-pull-feeds-end


.. _format-json-streaming-destination:

Send streaming JSON files
==================================================

.. format-json-streaming-destination-start

.. important:: Amperity does not send streaming JSON files to downstream workflows.

.. format-json-streaming-destination-end
