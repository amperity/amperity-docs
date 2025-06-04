.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About NDJSON files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        About NDJSON files, when used as a data source for Amperity or when sent from Amperity to a downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        File format: NDJSON

==================================================
File format: NDJSON
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-ndjson-start
   :end-before: .. term-ndjson-end


.. _format-ndjson-pull:

Pull NDJSON files
==================================================

.. format-ndjson-pull-start

To pull NDJSON files to Amperity:

#. Select a :ref:`data source <format-ndjson-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the NDJSON file <format-ndjson-pull-couriers>`.
#. Define a :ref:`feed to associate the fields that were selected from the NDJSON file with semantic tags <format-ndjson-pull-feed>` for customer profiles and interactions, as necessary.

.. format-ndjson-pull-end


.. _format-ndjson-pull-data-sources:

Data sources
--------------------------------------------------

.. format-ndjson-pull-data-sources-start

Pull NDJSON files to Amperity using one of the following data sources:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-ndjson-pull-data-sources-end


.. _format-ndjson-pull-load-data:

Load data
--------------------------------------------------

.. format-ndjson-pull-load-data-start

Use a feed to associate fields in the NDJSON file with semantic tags and a courier to pull the NDJSON file from its upstream data source.

* :ref:`Couriers <format-ndjson-pull-couriers>`
* :ref:`Feeds <format-ndjson-pull-feed>`

.. format-ndjson-pull-load-data-end


.. _format-ndjson-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-ndjson-pull-couriers-start

A courier must specify the location of the NDJSON file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-ndjson-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-ndjson-pull-couriers-feed-selection>`

.. format-ndjson-pull-couriers-end


.. _format-ndjson-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-ndjson-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the NDJSON file and to define formattting within the file.

.. format-ndjson-pull-couriers-file-settings-start


.. _format-ndjson-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-ndjson-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then which files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-ndjson-pull-couriers-feed-selection-end


.. _format-ndjson-pull-feed:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-ndjson-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-ndjson-pull-feeds-end


.. _format-ndjson-destination:

Send NDJSON files
==================================================

.. format-ndjson-destination-links-start

Amperity can send NDJSON files to downstream workflows using any of the following destinations:

* |destination_sftp_any|
* |destination_amazon_s3|
* |destination_azure_blob_storage|
* |destination_google_cloud_storage|

.. format-ndjson-destination-links-end