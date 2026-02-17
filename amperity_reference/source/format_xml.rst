.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About XML files, when used as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About XML files, when used as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        XML files

==================================================
XML files
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-xml-start
   :end-before: .. term-xml-end

.. format-xml-streaming-ingest-start

.. note:: XML data that is sent to the |api_streaming_ingest| is converted to :doc:`CBOR format <format_cbor>`.

.. format-xml-streaming-ingest-end


.. _format-xml-pull:

Pull XML files
==================================================

.. format-xml-pull-start

To pull XML files to Amperity:

#. Select a :ref:`data source <format-xml-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the XML file <format-xml-pull-couriers>`.
#. Define a :ref:`feed to associate the fields that were selected from the XML file with semantic tags <format-xml-pull-feed>` for customer profiles and interactions, as necessary.

.. format-xml-pull-end


.. _format-xml-pull-data-sources:

Data sources
--------------------------------------------------

.. format-xml-pull-data-sources-start

Pull XML files to Amperity using one of the following data sources:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-xml-pull-data-sources-end


.. _format-xml-pull-load-data:

Load data
--------------------------------------------------

.. format-xml-pull-load-data-start

Use a feed to associate fields in the XML file with semantic tags and a courier to pull the XML file from its upstream data source.

* :ref:`Couriers <format-xml-pull-couriers>`
* :ref:`Feeds <format-xml-pull-feed>`

.. format-xml-pull-load-data-end


.. _format-xml-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-xml-pull-couriers-start

A courier must specify the location of the XML file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-xml-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-xml-pull-couriers-feed-selection>`

.. format-xml-pull-couriers-end


.. _format-xml-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-xml-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the XML file and to define formatting within the file.

.. format-xml-pull-couriers-file-settings-start


.. _format-xml-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-xml-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Spark** Use this option to load data when the XML file contains complex types, such as within the **complexType** element.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-xml-pull-couriers-feed-selection-end


.. _format-xml-pull-feed:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-xml-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-xml-pull-feeds-end


.. _format-xml-destination:

Send XML files
==================================================

.. format-xml-destination-start

.. important:: Amperity does not send XML files to downstream workflows.

.. format-xml-destination-end
