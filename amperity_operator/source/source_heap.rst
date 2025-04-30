.. https://docs.amperity.com/operator/


.. |source-name| replace:: Heap
.. |plugin-name| replace:: Amazon S3
.. |feed-name| replace:: Users
.. |credential-type| replace:: **iam-credential**
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: clickstream events for users, page views, and sessions


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Heap.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Heap.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Heap

==================================================
Pull from Heap
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-heap-start
   :end-before: .. term-heap-end

.. source-heap-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-heap-get-details>`
#. :ref:`Add courier <source-heap-add-courier>`
#. :ref:`Get sample files <source-heap-get-sample-files>`
#. :ref:`Add feeds <source-heap-add-feeds>`
#. :ref:`Add load operations <source-heap-add-load-operations>`
#. :ref:`Run courier <source-heap-run-courier>`
#. :ref:`Add to courier group <source-heap-add-to-courier-group>`

.. source-heap-steps-to-pull-end


.. _source-heap-howitworks:

How this source works
==================================================

.. source-heap-howitworks-start

Amperity can pull |what-pull| from |source-name|.

.. source-heap-howitworks-end

.. image:: ../../images/source-heap.png
   :width: 600 px
   :alt: Pull clickstream data for users, page views, and sessions to Amperity from Heap.
   :align: left

.. source-heap-howitworks-callouts-start

A |source-name| data source works like this:

#. Clickstream data is generated when your customers visit your websites and apps.

   |source-name| is configured to capture this data, and then make it available for use outside of |source-name| using the Heap Connector for S3.
#. Clickstream data is loaded to a customer-managed Amazon S3 bucket.
#. Amperity pulls data from the customer-managed Amazon S3 bucket, assigning semantic tags for clickstream events and for customer profile data.
#. Domain tables within Amperity are refreshed.
#. Customer profiles are made available to Stitch. All data is passed to your customer 360 database. The Amperity ID links records across data sources for each unique customer.

.. source-heap-howitworks-callouts-note-end


.. _source-heap-get-details:

Get details
==================================================

.. source-heap-get-details-start

Amperity can be configured to pull data from |source-name| using Amazon S3. This requires the following configuration details:

#. |source-name| must be configured to use `Heap Connect for S3 <https://help.heap.io/hc/en-us/articles/18700055185308-S3-Integration>`__ |ext_link|. This will send data from |source-name| to a customer-managed Amazon S3 bucket.
#. The Amazon Resource Name (ARN) for a role with cross-account access.
#. The name of the customer-managed Amazon S3 bucket.
#. A list of objects (by filename and file type) in the customer-managed Amazon S3 bucket to be pulled to Amperity. 
#. A sample for each file to simplify feed creation.

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-amazon-s3-cross-account-start
   :end-before: .. sources-add-courier-amazon-s3-cross-account-end

.. source-heap-get-details-end


.. _source-heap-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. tip::

   .. include:: ../../amperity_reference/source/couriers.rst
      :start-after: .. couriers-run-without-load-operations-start
      :end-before: .. couriers-run-without-load-operations-end

**Example entities list**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-entities-list-intro-s3-generic-start
   :end-before: .. sources-add-courier-entities-list-intro-s3-generic-end

.. source-heap-add-courier-entities-list-start

For example:

::

   [
     {
       "object/type": "file",
       "object/file-pattern": "'path/to/users'-YYYY-MM-dd'.avro'",
       "object/land-as": {
         "file/tag": "FILE_NAME",
         "file/content-type": "application/avro"
       }
     }
   ]

.. source-heap-add-courier-entities-list-end

**To add an Amazon S3 courier**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-s3-generic-start
   :end-before: .. sources-add-courier-s3-generic-end


.. _source-heap-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-heap-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-heap-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-heap-add-load-operations-example-start

For example:

::

   {
     "USERS-FEED-ID": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "users"
       }
     ]
   }

.. source-heap-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-heap-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-heap-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
