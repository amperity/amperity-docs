.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About using Apache Avro files as a data source for Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About using Apache Avro files as a data source for Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Apache Avro files

==================================================
Apache Avro files
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-apache-avro-start
   :end-before: .. term-apache-avro-end

.. format-avro-start

Apache Avro may be used with any upstream or downstream customer environment that supports the use of Avro. Avro offers the most compact file format available for use with Amperity.

.. format-avro-end


.. _format-avro-pull:

Pull Avro files
==================================================

.. format-avro-pull-start

To pull Avro files to Amperity:

#. Select a :ref:`data source <format-avro-pull-data-sources>`.
#. Configure a courier for :ref:`the location and name of the Avro file <format-avro-pull-couriers>`.
#. Define a :ref:`feed to associate fields in the Avro file with semantic tags <format-avro-pull-feeds>`.

.. format-avro-pull-end


.. _format-avro-pull-data-sources:

Data sources
--------------------------------------------------

.. format-avro-pull-data-sources-start

Pull Apache Avro files to Amperity using one of the following data sources:

* |source_sftp_any|
* |source_amazon_s3|
* |source_azure_blob_storage|
* |source_google_cloud_storage|
* |source_sftp_amperity|

.. format-avro-pull-data-sources-end


.. _format-avro-pull-load-data:

Load data
--------------------------------------------------

.. format-avro-pull-load-data-start

Use a feed to associate fields in the Apache Avro file with semantic tags and a courier to pull the Apache Avro file from its upstream data source.

* :ref:`Couriers <format-avro-pull-couriers>`
* :ref:`Feeds <format-avro-pull-feeds>`

.. format-avro-pull-load-data-end


.. _format-avro-pull-couriers:

Couriers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. format-avro-pull-couriers-start

A courier must specify the location of the Apache Avro file, and then define how that file is to be pulled to Amperity.

#. :ref:`File settings <format-avro-pull-couriers-file-settings>`
#. :ref:`Feed selection <format-avro-pull-couriers-feed-selection>`

.. format-avro-pull-couriers-end


.. _format-avro-pull-couriers-file-settings:

File settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-avro-pull-couriers-file-settings-start

Use the **File settings** section of the courier configuration page to specify the path to the Apache Avro file and to define  formatting within the file.

.. format-avro-pull-couriers-file-settings-start


.. _format-avro-pull-couriers-feed-selection:

Feed selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-avro-pull-couriers-feed-selection-start

Use the **Feed selection** section of the courier configuration page to identify the feed for which this courier pulls data, and then which files are loaded.

From the **Load type** dropdown select one of:

* **Load** Use this option to load data to the associated domain table.
* **Spark** Use this option to load data when the Apache Avro file contains complex types, such as **records**, **enums**, **arrays**, **maps**, **unions**, and **fixed**.
* **Truncate and load** Use this option to delete all rows in the associated domain table, and then load data.

.. format-avro-pull-couriers-feed-selection-end


.. _format-avro-pull-feeds:

Feeds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. format-avro-pull-feeds-start

Apply :ref:`profile (PII) semantics <semantics-profile>` to customer records and :ref:`transaction <semantics-itemized-transactions>`, and product catalog semantics to interaction records. Use :ref:`blocking key (bk), foreign key (fk), and separation key (sk) <semantics-keys>` semantic tags to define how Amperity should understand values that exist across data sources.

.. format-avro-pull-feeds-end


.. _format-avro-destination:

Send Avro files
==================================================

.. format-avro-destination-start

.. important:: Amperity does not send Avro files to downstream workflows.

.. format-avro-destination-end
