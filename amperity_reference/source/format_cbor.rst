.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About using CBOR files as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About using CBOR files as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        CBOR files

==================================================
CBOR files
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-cbor-start
   :end-before: .. term-cbor-end

.. format-cbor-streaming-ingest-start

.. note:: XML data can be sent to the |api_streaming_ingest|, after which it is converted to CBOR format and may be loaded to Amperity using an ingest query that flattens it into a tabular format.

.. format-cbor-streaming-ingest-end


.. _format-cbor-pull:

Pull CBOR files
==================================================

.. format-cbor-pull-start

To pull CBOR files to Amperity:

#. Select a :ref:`data source <format-cbor-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the CBOR file <format-cbor-pull-couriers>`.
#. Define a :ref:`feed to associate fields in the CBOR file with semantic tags <format-cbor-pull-feed>`.

.. format-cbor-pull-end


.. _format-cbor-pull-data-sources:

Data sources
--------------------------------------------------

.. format-cbor-pull-data-sources-start

Pull CBOR files to Amperity using one of the following data sources:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-cbor-pull-data-sources-end


.. _format-cbor-pull-load-data:

Load data
--------------------------------------------------

.. format-cbor-pull-load-data-start

Use a feed to associate fields in the CBOR file with semantic tags and a courier to pull the CBOR file from its upstream data source.

* :ref:`Couriers <format-cbor-pull-couriers>`
* :ref:`Feeds <format-cbor-pull-feed>`

.. format-cbor-pull-load-data-end


.. _format-cbor-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-cbor-pull-couriers-start

A courier must specify the location of the CBOR file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-cbor-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-cbor-pull-couriers-feed-selection>`

.. format-cbor-pull-couriers-end


.. _format-cbor-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-cbor-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the CBOR file and to define  formatting within the file.

.. format-cbor-pull-couriers-file-settings-start


.. _format-cbor-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-cbor-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-cbor-pull-couriers-feed-selection-end

.. format-cbor-pull-couriers-load-operations-important-start

.. important:: The ``"schema"`` must match the structure of the incoming file, including all nested groupings and data types. Set ``"nullable"`` to ``True`` to allow fields to contain **NULL** values. A CBOR file can have hundreds of fields. The ellipses (``...``) in this example represents locations within this example structure where additional fields may be present.

.. format-cbor-pull-couriers-load-operations-important-end

.. format-cbor-pull-couriers-load-operations-rowtag-start

.. tip:: Set ``rowTag`` to the element in the CBOR file that should be treated as a row in a table. The default value is ``row``.

.. format-cbor-pull-couriers-load-operations-rowtag-start


.. _format-cbor-pull-feed:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-cbor-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-cbor-pull-feeds-end


.. _format-cbor-destination:

Send CBOR files
==================================================

.. format-cbor-destination-start

.. important:: Amperity does not send CBOR files to downstream workflows.

.. format-cbor-destination-end
