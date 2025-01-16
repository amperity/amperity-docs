.. https://docs.amperity.com/datagrid/


.. |source-name| replace:: Azure Blob Storage
.. |plugin-name| replace:: Azure Blob Storage
.. |feed-name| replace:: CustomerRecords
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: files in any supported format
.. |credential-type| replace:: **azure-blob-connection-string**


.. meta::
    :description lang=en:
        Configure Amperity to pull data from (legacy) Azure Blob Storage.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from (legacy) Azure Blob Storage.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Azure Blob Storage (legacy)

==================================================
Pull from Azure Blob Storage (Legacy)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-blob-storage-start
   :end-before: .. term-azure-blob-storage-end

.. source-azure-blob-storage-legacy-important-start

.. important:: Use this data source to pull data to Amperity from Azure Data Lake Storage Gen1 or Azure Data Lake Storage Gen2.

.. source-azure-blob-storage-legacy-important-end

.. source-azure-blob-storage-legacy-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-azure-blob-storage-legacy-get-details>`
#. :ref:`Add courier <source-azure-blob-storage-legacy-add-courier>`
#. :ref:`Get sample files <source-azure-blob-storage-legacy-get-sample-files>`
#. :ref:`Add feeds <source-azure-blob-storage-legacy-add-feeds>`
#. :ref:`Add load operations <source-azure-blob-storage-legacy-add-load-operations>`
#. :ref:`Run courier <source-azure-blob-storage-legacy-run-courier>`
#. :ref:`Add to courier group <source-azure-blob-storage-legacy-add-to-courier-group>`

.. source-azure-blob-storage-legacy-steps-to-pull-end


.. _source-azure-blob-storage-legacy-get-details:

Get details
==================================================

.. source-azure-blob-storage-legacy-get-details-start

Amperity can be configured to pull data from Azure Blob Storage. This may be done using :ref:`Azure Data Share <source-azure-blob-storage-legacy-azure-data-share>` or by using :ref:`Azure Blob Storage credentials <source-azure-blob-storage-legacy-credentials>`.

.. source-azure-blob-storage-legacy-get-details-end


.. _source-azure-blob-storage-legacy-filedrop-requirements:

Filedrop recommendations
--------------------------------------------------

.. include:: ../../shared/file-formats.rst
   :start-after: .. formats-filedrop-common-start
   :end-before: .. formats-filedrop-common-end


.. _source-azure-blob-storage-legacy-azure-data-share:

Use Azure Data Share
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-data-share-start
   :end-before: .. term-azure-data-share-end

.. source-azure-blob-storage-legacy-azure-data-share-start

Amperity prefers to pull data from customer-managed cloud storage. This approach ensures that customers can:

* Use security policies managed in Azure Data Share to manage access to data
* Directly manage the files that are made available
* Modify access without requiring involvement by Amperity; access may be revoked at any time by either Azure account, after which data sharing ends immediately
* Directly troubleshoot incomplete or missing files

Amperity recommends to use Azure Data Share to manage access to customer-managed cloud storage in Azure. This allows managed security policies to control access to data.

.. source-azure-blob-storage-legacy-azure-data-share-end

.. source-azure-blob-storage-legacy-azure-data-share-after-start

After setting up Azure Data Share, a list of files (by filename and file type), along with any sample files, must be made available to allow for feed creation. These files may be placed directly into the shared location after Azure Data Share is configured.

.. source-azure-blob-storage-legacy-azure-data-share-after-end

**To send data to Amperity using Azure Data Share**

.. source-azure-blob-storage-legacy-azure-data-share-steps-start

The following steps describe how to configure Amperity to use Azure Data Share to pull data from customer-managed Azure Blob Storage.

.. important:: These steps require configuration changes to both customer- *and* Amperity-managed Azure accounts and must be done by users with administrative access. 

#. The customer sends Amperity an invitation to set up data sharing.
#. Amperity accepts the invitation to set up data sharing.
#. The customer determines the location from which data will be shared with Amperity.
#. The customer schedules snapshots of the data to be shared, including the frequency of data sharing.
#. Amperity places shared data into customer-dedicated Azure Blob Storage instance.
#. Amperity configures a courier to pull data from that location into Amperity.

.. note:: Data that is shared with Amperity via Azure Data Share can be removed from Amperity by submitting a request for data removal to Amperity Customer Support.

.. source-azure-blob-storage-legacy-azure-data-share-steps-end


.. _source-azure-blob-storage-legacy-credentials:

Use credentials
--------------------------------------------------

.. source-azure-blob-storage-legacy-credentials-start

A source that uses credentials to send data to Amperity from |source-name| requires the following information be sent to Amperity via SnapPass:

#. The URL for the Azure authentication endpoint. This is typically in the format of ``https://login.microsoftonline.com/<directory_id>/oauth2/token``.
#. The information needed for the selected credentials method: shared access credentials, a storage URI, or a connection string.
#. The name of the container, the blob prefix, and credential details. (These vary depending on the chosen credential method.)
#. A list of files (by filename and file type) in Azure Blob Storage to be sent to Amperity.
#. A sample for each file to simplify feed creation.

.. source-azure-blob-storage-legacy-credentials-end


.. _source-azure-blob-storage-legacy-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. tip::

   .. include:: ../../amperity_reference/source/couriers.rst
      :start-after: .. couriers-run-without-load-operations-start
      :end-before: .. couriers-run-without-load-operations-end


.. _source-azure-blob-storage-legacy-add-courier-for-data-share:

for Azure Data Share
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-data-share-start
   :end-before: .. term-azure-data-share-end

.. source-azure-blob-storage-legacy-add-courier-for-data-share-start

Review :ref:`source-azure-blob-storage-legacy-azure-data-share` for more information about using Azure Data Share.

.. source-azure-blob-storage-legacy-add-courier-for-data-share-end

**To add a courier**

.. source-azure-blob-storage-legacy-add-courier-for-data-share-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**. You may switch to using **azure-blob-storage-uri** or **azure-blob-shared-access-signature**.
#. Under **Azure Blob Storage Settings**, add the name of the container and the blob prefix.
#. Under **Azure Blob Storage Settings** configure the list of files to pull to Amperity. Configure the **Entities List** for each file to be loaded to Amperity. For example, two files: "CustomerRecords.csv" and "TransactionRecords.csv".

   ::

      [
        {
          "object/type": "file",
          "object/file-pattern": "'/path/to/CustomerRecords.csv'",
          "object/land-as": {
            "file/header-rows": 1,
            "file/tag": "customer-records-2019",
            "file/content-type": "text/csv"
          }
        },
        {
          "object/type": "file",
          "object/file-pattern": "'/path/to/TransactionRecords.csv'",
          "object/land-as": {
            "file/header-rows": 1,
            "file/tag": "transaction-records-2019",
            "file/content-type": "text/csv"
          }
        }
      ]

#. Under **Azure Blob Storage Settings** set the load operations to a string that is obviously incorrect, such as **df-xxxxxx**. (You may also set the load operation to empty: "{}".)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to "{}" or are not set to an obviously incorrect string the validation test for the courier configuration settings will fail.
#. Click **Save**.

.. source-azure-blob-storage-legacy-add-courier-for-data-share-steps-end



.. _source-azure-blob-storage-legacy-add-courier-for-credentials:

for Azure credentials
--------------------------------------------------

.. source-azure-blob-storage-legacy-add-courier-for-credentials-start

Credentials options to access Azure Blob Storage include shared access signatures, connection strings, and storage URLs.

.. source-azure-blob-storage-legacy-add-courier-for-credentials-end

**To add a courier**

.. source-azure-blob-storage-legacy-add-courier-for-credentials-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**. You may switch to using **azure-blob-storage-uri** or **azure-blob-shared-access-signature**.
#. From the **Credential** drop-down, select **Create a new credential**. This opens the **Create New Credential** dialog box. 
#. Enter a name for the credential, any credential type-specific settings, and then click **Save**.

   For the "azure-blob-connection-string" credential type, enter the name of the credential and the connection string.

   For the "azure-blob-storage-uri" credential type, enter the name of the credential and the URI for the Azure Data Lake Storage instance.

   For the "azure-blob-shared-access-signature" credential type, enter the name of the credential, the account name, and the shared access signature.
#. Under **Azure Blob Storage Settings**, add the name of the container and the blob prefix.
#. Under **Azure Blob Storage Settings** configure the list of files to pull to Amperity. Configure the **Entities List** for each file to be loaded to Amperity. For example, two files: "CustomerRecords.csv" and "TransactionRecords.csv".

   ::

      [
        {
          "object/type": "file",
          "object/file-pattern": "'/path/to/CustomerRecords.csv'",
          "object/land-as": {
            "file/header-rows": 1,
            "file/tag": "customer-records-2019",
            "file/content-type": "text/csv"
          }
        },
        {
          "object/type": "file",
          "object/file-pattern": "'/path/to/TransactionRecords.csv'",
          "object/land-as": {
            "file/header-rows": 1,
            "file/tag": "transaction-records-2019",
            "file/content-type": "text/csv"
          }
        }
      ]

#. Under **Azure Blob Storage Settings** set the load operations to a string that is obviously incorrect, such as **df-xxxxxx**. (You may also set the load operation to empty: "{}".)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to "{}" the validation test for the courier configuration settings will fail.
#. Click **Save**.

.. source-azure-blob-storage-legacy-add-courier-for-credentials-steps-end


.. _source-azure-blob-storage-legacy-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-azure-blob-storage-legacy-add-feeds:

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


.. _source-azure-blob-storage-legacy-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-azure-blob-storage-legacy-add-load-operations-example-start

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

.. source-azure-blob-storage-legacy-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-azure-blob-storage-legacy-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-azure-blob-storage-legacy-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end


.. _source-azure-blob-storage-legacy-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. source-azure-blob-storage-legacy-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-source-start
          :end-before: .. workflow-actions-common-table-section-one-a-source-end

       .. image:: ../../images/mockup-destinations-tab-workflow-error-sources.png
          :width: 500 px
          :alt: Review a notifications error.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-b-start
          :end-before: .. workflow-actions-common-table-section-one-b-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-two-start
          :end-before: .. workflow-actions-common-table-section-two-end

       .. image:: ../../images/mockups-workflow-failed.png
          :width: 500 px
          :alt: The workflow tab, showing a workflow with errors.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-a-start
          :end-before: .. workflow-actions-common-table-section-three-a-end

       .. image:: ../../images/workflow-actions-azure-invalid-permissions.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |source-name|, including:

       * :ref:`source-azure-blob-storage-legacy-workflow-actions-bad-archive`
       * :ref:`source-azure-blob-storage-legacy-workflow-actions-invalid-credentials`
       * :ref:`source-azure-blob-storage-legacy-workflow-actions-invalid-permissions`
       * :ref:`source-azure-blob-storage-legacy-workflow-actions-missing-file`
       * :ref:`source-azure-blob-storage-legacy-workflow-actions-pgp-error`
       * :ref:`source-azure-blob-storage-legacy-workflow-actions-unable-to-decompress-archive`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-azure-invalid-permissions-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. source-azure-blob-storage-legacy-workflow-actions-end


.. _source-azure-blob-storage-legacy-workflow-actions-bad-archive:

Bad archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-bad-archive-start
   :end-before: .. workflow-actions-files-generic-bad-archive-end


.. _source-azure-blob-storage-legacy-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-source-start
   :end-before: .. workflow-actions-generic-invalid-credentials-source-end


.. _source-azure-blob-storage-legacy-workflow-actions-invalid-permissions:

Invalid permissions
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-azure-sas-intro-start
   :end-before: .. workflow-actions-azure-sas-intro-end

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-azure-sas-whatis-start
   :end-before: .. workflow-actions-azure-sas-whatis-end

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-azure-sas-invalid-permissions-start
   :end-before: .. workflow-actions-azure-sas-invalid-permissions-end

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-azure-sas-report-problem-start
   :end-before: .. workflow-actions-azure-sas-report-problem-end

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-azure-sas-steps-start
   :end-before: .. workflow-actions-azure-sas-steps-end


.. _source-azure-blob-storage-legacy-workflow-actions-missing-file:

Missing file
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-missing-file-start
   :end-before: .. workflow-actions-files-generic-missing-file-end


.. _source-azure-blob-storage-legacy-workflow-actions-pgp-error:

PGP error
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-pgp-error-start
   :end-before: .. workflow-actions-generic-pgp-error-end


.. _source-azure-blob-storage-legacy-workflow-actions-unable-to-decompress-archive:

Unable to decompress archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-unable-to-decompress-file-start
   :end-before: .. workflow-actions-files-unable-to-decompress-file-end
