.. https://docs.amperity.com/operator/


.. |source-name| replace:: Optimizely
.. |plugin-name| replace:: Amazon S3
.. |feed-name| replace:: Decisions
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: interactions records
.. |credential-type| replace:: **iam-credential**


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Optimizely.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Optimizely.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Optimizely

==================================================
Pull from Optimizely
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-optimizely-start
   :end-before: .. term-optimizely-end

.. source-optimizely-about-start

Optimizely can send |ext_optimizely_enriched_events_export| data to Amperity via Amazon S3. Enriched events include details such as event timestamps, event IDs, event tags, event names, visitor IDs, session IDs, experiment IDs, and variation IDs.

.. source-optimizely-about-end

.. source-optimizely-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-optimizely-get-details>`
#. :ref:`Review Amazon S3 requirements for Optimizely <source-optimizely-filedrop-requirements>`
#. :ref:`Add courier <source-optimizely-add-courier>`
#. :ref:`Get sample files <source-optimizely-get-sample-files>`
#. :ref:`Add feeds <source-optimizely-add-feeds>`
#. :ref:`Add load operations <source-optimizely-add-load-operations>`
#. :ref:`Run courier <source-optimizely-run-courier>`
#. :ref:`Add to courier group <source-optimizely-add-to-courier-group>`

.. source-optimizely-steps-to-pull-end


.. _source-optimizely-get-details:

Get details
==================================================

.. source-optimizely-get-details-start

Amperity can be configured to pull data from Optimizely using Amazon S3. This requires the following configuration details:

#. Access to an |ext_optimizely_data_service| hosted in Amazon S3.
#. The Amazon Resource Name (ARN) for a role with cross-account access.
#. The name of the Amazon S3 bucket.
#. A list of objects (by filename and file type) in the Amazon S3 bucket to be pulled to Amperity. 
#. A sample for each file to simplify feed creation.

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-amazon-s3-cross-account-start
   :end-before: .. sources-add-courier-amazon-s3-cross-account-end

.. source-optimizely-get-details-end


.. _source-optimizely-filedrop-requirements:

Amazon S3 requirements
==================================================

.. source-optimizely-filedrop-requirements-start

Amazon S3 requires the following:

* Credentials that |format_common_allow_access| from the Amazon S3 bucket used by Optimizely.
* Files provided in |format_parquet| format and using the YYYY-MM-DD date format.
* Files sent from Optimizely are :ref:`located in partitions <source-optimizely-filedrop-apache-parquet-optimizely-partitions>`, one for decisions and one for events.
* Optimizely uses AWS Key Management Service for encryption.

.. source-optimizely-filedrop-requirements-end


.. _source-optimizely-filedrop-credentials:

Amazon S3 credentials
--------------------------------------------------

.. source-optimizely-filedrop-credentials-start

Amperity requires the ability to connect to, and then read data from the Amazon S3 bucket used by Optimizely. The credentials that allow that connection and the permissions to read data are entered into the Amperity user interface while configuring a courier. These credentials are created and managed by the owner of the Amazon S3 bucket. Use SnapPass to share credentials with your Amperity representative, if necessary.

.. source-optimizely-filedrop-credentials-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-snappass-start
   :end-before: .. term-snappass-end


.. _source-optimizely-filedrop-apache-parquet-optimizely-partitions:

Optimizely S3 partitions
--------------------------------------------------

.. source-optimizely-s3-partitions-start

Enriched events exports are exported to a bucket named **optimizely-events-data** that contains two partitions: decisions and conversions.

The paths to these partitions are similar to:

::

   s3://optimizely-events-data/v1/account_id=<account_id>/
   type=decisions/date={YYYY-MM-DD}/experiment=<experiment_id>

or

:: 

   s3://optimizely-events-data/v1/account_id=<account_id>/
   type=events/date={YYYY-MM-DD}/event=<event_name>

where:

* **optimizely-events-data** is the name of the Amazon S3 bucket
* **account_id** is your unique account identifier
* **date** is the creation date for the data
* **experiment_id** is the unique experiment identifier used for the **decisions** partition
* **event_name** is the event or entity identifier used for the events partition

The daily partition files are ready when **_SUCCESS** is appended to the partition path.

.. note:: Optimizely uses AWS Key Management Service for encryption. Amperity must be able to decrypt these files to pull them to the Amazon S3 or Azure Blob Storage location used by your tenant.

.. source-optimizely-s3-partitions-end


.. _source-optimizely-add-courier:

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

.. source-optimizely-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. From the **Credential** dropdown, select **Create a new credential**. This opens the **Create New Credential** dialog box. 
#. Enter a name for the credential and add the configuration settings. Click **Save**.
#. Under **S3 Settings**, add the name of the Optimizely bucket, prefix, and region.
#. Under **S3 Settings** configure the list of files to pull to Amperity. Configure the **Entities List** for each file to be loaded to Amperity. For example, two files: "decisions.parquet" and "conversions.parquet".

   ::

      [
        {
          "object/type": "file",
          "object/file-pattern": "'/path/to/decisions_YYYY-MM-DD.parquet'",
          "object/land-as": {
            "file/tag": "decisions",
            "file/content-type": "application/x-parquet"
          }
        },
        {
          "object/type": "file",
          "object/file-pattern": "'/path/to/conversions_YYYY-MM-DD.parquet'",
          "object/land-as": {
            "file/tag": "conversions",
            "file/content-type": "application/x-parquet"
          }
        }
      ]

   .. note:: The file pattern to the location at which the Optimizely files are located in Amazon S3 may have a complex directory structure that uses numerals, versions, years, months, days, and compression. For example:

      ::

         '1234567890/0987654321/2.0/'yyyy'/'MM'/'dd'/*/*.gz'

#. Under **Optimizely Settings** set the load operations to a string that is obviously incorrect, such as **df-xxxxxx**. (You may also set the load operation to empty: "{}".)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to "{}" or are not set to an obviously incorrect string the validation test for the courier configuration settings will fail.
#. Click **Save**.

.. source-optimizely-add-courier-steps-end


.. _source-optimizely-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-optimizely-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. source-optimizely-add-feed-start

.. note:: Decision and conversion events have different schemas and each will require their own feed.

.. source-optimizely-add-feed-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-optimizely-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-optimizely-add-load-operations-example-start

For example:

::

   {
     "DECISIONS-FEED-ID": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "decisions"
       }
     ],
     "CONVERSIONS-FEED-ID": [
       {
         "type": "load",
         "file": "conversions"
       }
     ]
   }

.. source-optimizely-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-optimizely-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-optimizely-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
