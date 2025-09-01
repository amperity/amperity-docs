.. https://docs.amperity.com/operator/


.. |source-name| replace:: Kinesis Data Firehose
.. |plugin-name| replace:: Amazon S3
.. |feed-name| replace:: CustomerRecords
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: streamed data
.. |credential-type| replace:: **iam-credential**
.. |filter-the-list| replace:: "ama"


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
#. :ref:`Add data source and feed <source-amazon-kinesis-data-firehose-add-data-source>`

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
     - A list of objects by filename and file type in the S3 bucket to be sent to Amperity and a sample for each file to simplify feed creation.

       Review :ref:`how to configure Kinesis Data Firehose <source-amazon-kinesis-data-firehose-kinesis-data-firehose>`.

.. source-amazon-kinesis-data-firehose-get-details-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose:

Configure Kinesis Data Firehose
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-kinesis-data-firehose-start
   :end-before: .. term-amazon-kinesis-data-firehose-end

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-start

You may configure any supported data producer to use |source-name| services to automatically send real-time streaming data to |source-name|, and then make that data available to Amperity. Amperity can be configured to pull batched real-time data from any Amazon S3 location. It is recommended to send this data to a customer-managed Amazon S3 bucket, and then configure Amperity to pull data from that bucket.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-end

**To configure Kinesis Data Firehose to send data to the Amperity S3 bucket**

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-steps-start

#. Create a `cross-account role <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#cross-account-delivery-s3>`__ |ext_link| IAM role in the customer's Amazon AWS account.

   This role is required to grant |source-name| access to the Amazon S3 bucket that is part of the Amperity tenant. This role must have `s3:PutObjectAcl <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`__ |ext_link| configured as part of the list of allowed |source-name| actions.
#. Configure the `bucket policy <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html>`__ |ext_link| in the Amperity S3 bucket to allow the IAM role access to the Amperity S3 bucket.
#. Create a |source-name| `delivery stream <https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html>`__ |ext_link| in the customer's cloud infrastructure that uses this IAM role.
#. Configure the delivery stream to send data to the Amperity S3 bucket.
#. Configure applications to send data to the delivery stream.
#. Amperity requires data to be encrypted. This may be done with a policy on the Amperity S3 bucket that is configured by Amperity.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-steps-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose-record-separators:

Record separators
--------------------------------------------------

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-record-separators-start

Data records are delivered to Amazon S3 as an Amazon S3 object. If you need to ensure that individual records are available to Amperity in |source-name|, you will need to configure the delivery stream to add `a record separator <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#format>`__ |ext_link| at the end of each data record.

When using the |source-name| connector, which only accepts NDJSON files, you will need to ensure that each data record is followed by a newline character.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-record-separators-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose-filename-patterns:

Filename patterns
--------------------------------------------------

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-filename-patterns-start

Recommended `filename patterns <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ |ext_link| include:

* Using the YYYY/MM/DD/HH format when writing objects to |source-name|. This prefix will create a logical hierarchy in the bucket by year, then month, then date, and finally hour.
* Using the default |source-name| object naming pattern that increments by 1 a random string at the end of the object's filename.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-filename-patterns-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-frequency:

Delivery frequency
--------------------------------------------------

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-frequency-start

The |source-name| buffer size and interval will determine the `frequency of delivery <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#frequency>`__ |ext_link|. Incoming records will be concatenated based on the frequency of the delivery stream. 

.. warning:: If data fails to deliver to |source-name|, |source-name| will retry for up to 24 hours. If data fails to deliver within 24 hours, the data will be lost, unless it is successfully delivered to a backup location. You can re-send data if it's backed up.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-frequency-end


.. _source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-failures:

Delivery failures
--------------------------------------------------

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-failures-start

|source-name| will retry for up to 24 hours. The maximum `data storage time for Kinesis Data Firehose is 24 hours <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#retry>`__ |ext_link|. Data will be lost if delivery does not succeed within 24 hours. Consider using a secondary |source-name| bucket as a backup for data that cannot be lost.

.. note:: Delivery retries may introduce duplicates.

.. source-amazon-kinesis-data-firehose-kinesis-data-firehose-delivery-failures-end


.. _source-amazon-kinesis-data-firehose-add-data-source:

Add data source and feed
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-steps-00-intro-start
   :end-before: .. sources-steps-00-intro-end

**To add a data source for an Amazon S3 bucket**

.. source-amazon-kinesis-data-firehose-add-data-source-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-01-open-dialog-start
          :end-before: .. sources-steps-01-open-dialog-end

       .. image:: ../../images/mockup-sources-add-01-select-source.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-01-select-source-start
          :end-before: .. sources-steps-01-select-source-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-already-configured-start
          :end-before: .. credentials-sources-configure-already-configured-end

       .. tip::

          .. include:: ../../shared/credentials.rst
             :start-after: .. credentials-sources-configure-already-configured-tip-intro-start
             :end-before: .. credentials-sources-configure-already-configured-tip-intro-end

          .. image:: ../../images/mockup-credentials-add-02-credential-status-s3.png
             :width: 380 px
             :alt: Add 
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-select-file-start
          :end-before: .. sources-steps-03-select-file-end

       .. image:: ../../images/mockup-sources-add-03-file-settings.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-browse-start
          :end-before: .. sources-steps-03-browse-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-browse-note-start
          :end-before: .. sources-steps-03-browse-note-end

       .. image:: ../../images/mockup-sources-add-03-file-browser-sftp.png
          :width: 500 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-pgp-start
          :end-before: .. sources-steps-03-pgp-end

       .. image:: ../../images/mockup-sources-add-03-pgp-credential.png
          :width: 500 px
          :alt: Add 
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-start
          :end-before: .. sources-steps-04-review-end

       .. image:: ../../images/mockup-sources-add-03-file-formatting.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-contents-start
          :end-before: .. sources-steps-04-review-contents-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-pgp-start
          :end-before: .. sources-steps-04-review-pgp-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-formatting-details-start
          :end-before: .. sources-steps-04-review-formatting-details-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-file-types-start
          :end-before: .. sources-steps-04-file-types-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-options-start
          :end-before: .. sources-steps-05-feed-options-end


       **New feed**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-new-start
          :end-before: .. sources-steps-05-feed-new-end


       **Existing feed**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-existing-start
          :end-before: .. sources-steps-05-feed-existing-end


       **Pull data**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-types-start
          :end-before: .. sources-steps-05-load-types-end

       .. image:: ../../images/mockup-sources-add-04-feed-load-type.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-type-upsert-start
          :end-before: .. sources-steps-05-load-type-upsert-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-type-truncate-start
          :end-before: .. sources-steps-05-load-type-truncate-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-types-note-start
          :end-before: .. sources-steps-05-load-types-note-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-06-feed-editor-start
          :end-before: .. sources-steps-06-feed-editor-end


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-courier-start
          :end-before: .. sources-steps-07-courier-end

       .. image:: ../../images/mockup-courier-add-07-menu-run.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-calendar-start
          :end-before: .. sources-steps-07-calendar-end

       .. image:: ../../images/mockup-courier-add-07-menu-load-data.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-run-start
          :end-before: .. sources-steps-07-run-end

.. source-amazon-kinesis-data-firehose-add-data-source-steps-end
