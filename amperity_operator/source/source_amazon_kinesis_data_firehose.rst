.. https://docs.amperity.com/operator/


.. |source-name| replace:: Kinesis Data Firehose
.. |plugin-name| replace:: Amazon S3
.. |feed-name| replace:: CustomerRecords
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: streamed data
.. |credential-type| replace:: **iam-credential**


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Amazon Kinesis Data Firehose.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Amazon Kinesis Data Firehose.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Amazon Kinesis Data Firehose

==================================================
Pull from Amazon Kinesis Data Firehose
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-kinesis-data-firehose-start
   :end-before: .. term-amazon-kinesis-data-firehose-end

.. source-amazon-kinesis-data-firehose-about-start

Amperity can pull data from Amazon |source-name| via Amazon S3. A common scenario: a Firehose delivery stream is configured to send streaming data to an Amazon S3 bucket, generating numerous files with a consistent datestamp pattern appended to a generated file name. |source-name| can be a source for any number of file types and formats. Couriers can be configured to pull NDJSON files.

.. source-amazon-kinesis-data-firehose-about-end

.. source-amazon-kinesis-data-firehose-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-amazon-kinesis-data-firehose-get-details>`
#. :ref:`Configure Amazon Kinesis Data Firehose <source-amazon-kinesis-data-firehose-kinesis-data-firehose>`
#. :ref:`Add courier <source-amazon-kinesis-data-firehose-add-courier>`
#. :ref:`Get sample files <source-amazon-kinesis-data-firehose-get-sample-files>`
#. :ref:`Add feeds <source-amazon-kinesis-data-firehose-add-feeds>`
#. :ref:`Add load operations <source-amazon-kinesis-data-firehose-add-load-operations>`
#. :ref:`Run courier <source-amazon-kinesis-data-firehose-run-courier>`
#. :ref:`Add to courier group <source-amazon-kinesis-data-firehose-add-to-courier-group>`

.. source-amazon-kinesis-data-firehose-steps-to-pull-end


.. _source-amazon-kinesis-data-firehose-get-details:

Get details
==================================================

.. source-amazon-kinesis-data-firehose-get-details-start

The |source-name| destination requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The name of the S3 bucket from which data will be pulled to Amperity, which is also the bucket to which the Firehose delivery stream will write data.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - For cross-account role assumption you will need the value for the **Target Role ARN**, which enables Amperity to access the customer-managed Amazon S3 bucket.

       .. note:: The values for the **Amperity Role ARN** and the **External ID** fields are provided automatically.

       .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-policy-example-intro-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-policy-example-intro-end

       .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-policy-example-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-policy-example-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - A list of objects (by filename and file type) in the S3 bucket to be sent to Amperity and a sample for each file to simplify feed creation.

       Review :ref:`how to configure Kinesis Data Firehose <source-amazon-kinesis-data-firehose-kinesis-data-firehose>`.

.. source-amazon-kinesis-data-firehose-get-details-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose:

Configure Kinesis Data Firehose
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-kinesis-data-firehose-start
   :end-before: .. term-amazon-kinesis-data-firehose-end

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-start

You may configure any supported data producer to use |source-name| services to automatically send real-time streaming data to |source-name|, and then make that data available to Amperity. Amperity can be configured to pull the real-time data (in batches) from any Amazon S3 location. It is recommended to send this data to a customer-managed Amazon S3 bucket, and then configure Amperity to pull data from that bucket.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-end

**To configure Kinesis Data Firehose to send data to the Amperity S3 bucket**

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-steps-start

#. Create a |ext_aws_cross_account_role| IAM role in the customer's Amazon AWS account.

   This role is required to grant |source-name| access to the Amazon S3 bucket that is part of the Amperity tenant. This role must have |ext_aws_s3putobjectacl| configured as part of the list of allowed |source-name| actions.
#. Configure the |ext_aws_bucket_policy| in the Amperity S3 bucket to allow the IAM role access to the Amperity S3 bucket.
#. Create a |source-name| |ext_aws_kinesis_delivery_stream| in the customer's cloud infrastructure that uses this IAM role.
#. Configure the delivery stream to send data to the Amperity S3 bucket.
#. Configure applications to send data to the delivery stream.
#. Amperity requires data to be encrypted. This may be done with a policy on the Amperity S3 bucket that is configured by Amperity.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-steps-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose-record-separators:

Record separators
--------------------------------------------------

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-record-separators-start

Data records are delivered to Amazon S3 as an Amazon S3 object. If you need to ensure that individual records are available to Amperity in |source-name|, you will need to configure the delivery stream to add |ext_aws_kinesis_record_separators| at the end of each data record.

When using the |source-name| connector, which only accepts NDJSON files, you will need to ensure that each data record is followed by a newline character.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-record-separators-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose-filename-patterns:

Filename patterns
--------------------------------------------------

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-filename-patterns-start

Recommended |ext_aws_kinesis_filename_patterns| include:

* Using the YYYY/MM/DD/HH format when writing objects to |source-name|. This prefix will create a logical hierarchy in the bucket by year, then month, then date, and finally hour.
* Using the default |source-name| object naming pattern that increments (by an increase of 1) a random string at the end of the object's filename.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-filename-patterns-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-frequency:

Delivery frequency
--------------------------------------------------

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-frequency-start

The |source-name| buffer size and interval will determine the |ext_aws_kinesis_delivery_frequency|. Incoming records will be concatenated based on the frequency of the delivery stream. 

.. warning:: If data fails to deliver to |source-name|, |source-name| will retry for up to 24 hours. If data fails to deliver within 24 hours, the data will be lost, unless it is successfully delivered to a backup location. (You can re-send data if it's backed up.)

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-frequency-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-failures:

Delivery failures
--------------------------------------------------

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-failures-start

|source-name| will retry for up to 24 hours. The maximum |ext_aws_kinesis_delivery_failures|. Data will be lost if delivery does not succeed within 24 hours. Consider using a secondary |source-name| bucket as a backup for data that cannot be lost.

.. note:: Delivery retries may introduce duplicates.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-failures-end


.. _source-amazon-kinesis-data-firehose-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. tip::

   .. include:: ../../amperity_reference/source/couriers.rst
      :start-after: .. couriers-run-without-load-operations-start
      :end-before: .. couriers-run-without-load-operations-end

**To add a courier**

.. source-amazon-kinesis-data-firehose-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. From the **Credential** dropdown, select **Create a new credential**. This opens the **Create New Credential** dialog box. 
#. Enter a name for the credential, the IAM access key, and the IAM secret key. Click **Save**.
#. Under **Settings**, add the name of the S3 bucket to which the Firehose delivery stream will write.
#. Configure the list of files to pull to Amperity. Configure the **Entities List** for each file to be loaded to Amperity. For example, the files from two different streams: "customer-records" and "transaction-records".

   ::

      [
        {
          "object/type": "file",
          "object/file-pattern": "'/production/customer-records/'yyyy/MM/dd'/*.ndjson'",
          "object/land-as": {
            "file/tag": "customer-records",
            "file/content-type": "application/x-ndjson"
          }
        },
        {
          "object/type": "file",
          "object/file-pattern": "'/production/transaction-records/'yyyy/MM/dd'/*.ndjson'",
          "object/land-as": {
            "file/tag": "transaction-records",
            "file/content-type": "application/x-ndjson"
          }
        }
      ]

#. Under **Settings** set the load operations to a string that is obviously incorrect, such as **df-xxxxxx**. (You may also set the load operation to empty: "{}".)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to "{}" the validation test for the courier configuration settings will fail.
#. Click **Save**.

.. source-amazon-kinesis-data-firehose-add-courier-steps-end


.. _source-amazon-kinesis-data-firehose-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-amazon-kinesis-data-firehose-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-note-file-start
   :end-before: .. sources-add-feed-note-file-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-amazon-kinesis-data-firehose-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-amazon-kinesis-data-firehose-add-load-operations-example-start

For example:

::

   {
     "CUSTOMER-RECORDS-FEED-ID": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "customer-records"
       }
     ],
     "TRANSACTION-RECORDS-FEED-ID": [
       {
         "type": "load",
         "file": "transaction-records"
       }
     ]
   }

.. source-amazon-kinesis-data-firehose-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-amazon-kinesis-data-firehose-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-amazon-kinesis-data-firehose-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
