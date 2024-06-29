.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |source-name| replace:: Azure Blob Storage
.. |plugin-name| replace:: Azure Blob Storage
.. |feed-name| replace:: CustomerRecords
.. |credential-type| replace:: **azure-blob-connection-string**
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: files in any supported format
.. |filter-the-list| replace:: "azu"


.. meta::
    :description lang=en:
        Configure Amperity to pull data from any Azure Blob Storage bucket.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from any Azure Blob Storage bucket.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Azure Blob Storage

==================================================
Pull from Azure Blob Storage
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-blob-storage-start
   :end-before: .. term-azure-blob-storage-end

.. source-azure-blob-storage-important-start

.. important:: Use this data source to pull data to Amperity from Azure Data Lake Storage Gen1 or Azure Data Lake Storage Gen2.

.. source-azure-blob-storage-important-end

.. source-azure-blob-storage-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-azure-blob-storage-get-details>`
#. :ref:`Configure credentials <source-azure-blob-storage-configure-credentials>`
#. :ref:`Add data source <source-azure-blob-storage-add-data-source>`

.. source-azure-blob-storage-steps-to-pull-end


.. _source-azure-blob-storage-get-details:

Get details
==================================================

.. source-azure-blob-storage-get-details-start

The |source-name| data source requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The name of the container in |source-name| from which Amperity will pull data.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - Credentials that allow Amperity to access the container. This may be done using :ref:`credentials (a connection string, a shared access signature, or a storage URI) <source-azure-blob-storage-configure-credentials>` or using :ref:`Azure Data Share <source-azure-blob-storage-configure-azure-data-share>`.

.. source-azure-blob-storage-get-details-end


.. _source-azure-blob-storage-filedrop-requirements:

Filedrop recommendations
--------------------------------------------------

.. include:: ../../shared/file-formats.rst
   :start-after: .. formats-filedrop-common-start
   :end-before: .. formats-filedrop-common-end


.. _source-azure-blob-storage-configure-credentials:

Configure credentials
==================================================

.. source-azure-blob-storage-configure-credentials-start

Use one of the following options to configure Amperity to pull data from |source-name|:

* :ref:`source-azure-blob-storage-configure-azure-credentials`
* :ref:`source-azure-blob-storage-configure-azure-data-share`

.. source-azure-blob-storage-configure-credentials-end


.. _source-azure-blob-storage-configure-azure-credentials:

Azure credentials
--------------------------------------------------

.. source-azure-blob-storage-configure-azure-credentials-start

A source that uses |source-name| credentials may use a connection string, a shared access signature, or a storage URI.

**To configure Amperity to use Microsoft Azure credentials**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - The URL for the Azure authentication endpoint. This is typically in the following format: 

       ::

          https://login.microsoftonline.com/<directory_id>/oauth2/token


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - The information needed depends on the selected credential type.

       **Connection string**

       This method uses a connection string and the name of the container from which Amperity will pull data.

       **Shared access signature**

       This method uses the Microsoft Azure account name, a shared access signature, and the name of the container from which Amperity will pull data.

       .. tip:: When using a shared access signature, create a policy in Microsoft Azure, and then generate a token for the shared access signature against that policy. This allows the policy to expire instead of the token. Manage the expiration of the token by managing the expiration of the policy.

       **Storage URI**

       This method uses the storage URI and the name of the container from which Amperity will pull data.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - :ref:`Configure a data source and feed <source-azure-blob-storage-add-data-source>` to pull data from configured location, after which the list of files (by filename and file type) will be visible from Amperity.

.. source-azure-blob-storage-configure-azure-credentials-end


.. _source-azure-blob-storage-configure-azure-data-share:

Azure Data Share
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-data-share-start
   :end-before: .. term-azure-data-share-end

.. source-azure-blob-storage-configure-azure-data-share-start

Amperity prefers to pull data from customer-managed cloud storage. This approach ensures that customers can:

* Use security policies managed in Azure Data Share to manage access to data
* Directly manage the files that are made available
* Modify access without requiring involvement by Amperity; access may be revoked at any time by either Azure account, after which data sharing ends immediately
* Directly troubleshoot incomplete or missing files

Amperity recommends to use Azure Data Share to manage access to customer-managed cloud storage in Azure. This allows managed security policies to control access to data.

.. source-azure-blob-storage-configure-azure-data-share-end

.. source-azure-blob-storage-configure-azure-data-share-after-start

After setting up Azure Data Share, a list of files (by filename and file type), along with any sample files, must be made available to allow for feed creation. These files may be placed directly into the shared location after Azure Data Share is configured.

.. source-azure-blob-storage-configure-azure-data-share-after-end

.. source-azure-blob-storage-configure-azure-data-share-remove-start

.. note:: Data that is shared with Amperity via Azure Data Share can be removed from Amperity by submitting a request for data removal to Amperity Customer Support.

.. source-azure-blob-storage-configure-azure-data-share-remove-end

**To send data to Amperity using Azure Data Share**

.. source-azure-blob-storage-configure-azure-data-share-steps-start

The following steps describe how to configure Amperity to use Azure Data Share to pull data from customer-managed Azure Blob Storage.

.. important:: These steps require configuration changes to both customer- *and* Amperity-managed Azure accounts and must be done by users with administrative access.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - The customer sends Amperity an invitation to set up data sharing.

       Amperity accepts the invitation to set up data sharing.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - The customer determines the location from which data will be shared with Amperity, and then configures the schedule for how frequently snapshots of the data will be shared.

       Amperity places shared data into a customer-dedicated Azure Blob Storage instance.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - :ref:`Configure a data source and feed <source-azure-blob-storage-add-data-source>` to pull data from the customer-dedicated Azure Blob Storage instance.

.. source-azure-blob-storage-configure-azure-data-share-steps-end


.. _source-azure-blob-storage-add-data-source:

Add data source and feed
==================================================

.. source-azure-blob-storage-add-data-source-intro-start-start

Add a data source that pulls data from an |source-name| bucket for each file that you want to pull to Amperity.

Browse the |source-name| bucket to select a file, and then review the settings for that file. Define the feed schema, and then activate the feed. Run the courier manually, and then review the data that is added to the domain table that is associated with the feed.

.. source-azure-blob-storage-add-data-source-intro-end

**To add a data source for an Amazon S3 bucket**

.. source-azure-blob-storage-add-data-source-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Sources** page to configure |source-name|.

       Click the **Add courier** button to open the **Add courier** dialog box.

       .. image:: ../../images/mockup-sources-add-01-select-source-azure-blob-storage.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       Select |source-name|. Do one of the following:

       #. Click the row in which |source-name| is located. Sources are listed alphabetically.
       #. Search for |source-name|. Start typing |filter-the-list|. The list will filter to show only matching sources.


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

          .. image:: ../../images/mockup-credentials-add-02-credential-status-azure-blob-storage.png
             :width: 380 px
             :alt: Add 
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Select the file that will be pulled to Amperity, either directly (by going into the container bucket and selecting it) or by providing a filename pattern.

       .. image:: ../../images/mockup-sources-add-03-file-settings.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       Click **Browse** to open the **File browser**. Select the file that will be pulled to Amperity, and then click **Accept**.

       Use a filename pattern to define files that will be loaded on a recurring basis, but will have small changes to the filename over time, such as having a datestamp appended to the filename.

       .. note:: For a new feed, this file is *also* used as the sample file that is used to define the schema. For an existing feed, this file must match the schema that has already been defined.

       .. image:: ../../images/mockup-sources-add-03-file-browser-azure-blob-storage.png
          :width: 500 px
          :alt: Add 
          :align: left
          :class: no-scaled-link


       Use the **PGP credential** setting to specify the credentials to use for an encrypted file.

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
     - Review the file.

       .. image:: ../../images/mockup-sources-add-03-file-formatting.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       The contents of the file may be previewed as a table and in a raw format. Switch between these views using the **Table** and **Raw** buttons, and then click **Refresh** to view the file in that format.

       .. note:: PGP encrypted files can be previewed. Apache Parquet PGP encrypted files must be less than 500 MB to be previewed.

       Amperity will infer formatting details, and then adds these details to a series of settings located along the left side of the file view. File settings include:

       * Delimiter
       * Compression
       * Escape character
       * Quote character
       * Header row

       Review the file, and then update these settings, if necessary.

       .. note:: Amperity supports the following file types: |format_avro|, |format_parquet|, |format_csv|, DSV, |format_json|, |format_ndjson|, |format_psv|, |format_tsv|, and |format_xml|.

          Refer to those reference pages for details about each of the individual file formats.

          Files that contain nested JSON (or "complex JSON") or XML may require using the legacy courier configuration.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - A feed defines the schema for a file that is loaded to Amperity, after which that data is loaded into a domain table and ready for use with workflows within Amperity.

       There are two options for feeds: use a new feed or use an existing feed.


       **Use a new feed**

       To use a new feed, choose the **Create new feed** option, select an existing source from the **Source** drop-down *or* type the name of a new data source, and then enter the name of the feed.

       .. image:: ../../images/mockup-sources-add-04-feed-new.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       After you choose a load type and save the courier configuration, you will configure the feed using the data within the sample file.


       **Use an existing feed**

       To use an existing feed, choose the **Use existing feed** option to use an existing schema.

       .. image:: ../../images/mockup-sources-add-04-feed-existing.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       This option requires this file to match all of the feed-specific settings, such as incoming field names, field types, and primary keys. The data within the file may be different.


       **Load types**

       The load type defines how data in the file will be loaded to the associated domain table.

       .. image:: ../../images/mockup-sources-add-04-feed-load-type.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       Use the **Truncate and load** option to delete all rows in the associated domain table prior to loading data.

       Use the **Load** option to load data from the selected file to the associated domain table.

       .. note:: When a file is loaded to a domain table using an existing file, the file that is loaded *must* have the same schema as the existing feed. The data in the file may be new.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link
     - Use the feed editor to do all of the following:

       * Set the primary key
       * Choose the field that best presents when the data in the table was last updated; if there is not an obvious choice, use the "Generate an updated field" option.
       * For each field in the incoming data, validate the field name and semantic tag columns in the feed. Make any necessary adjustments.
       * For tables that contain customer records, enable the "Make available to Stitch" to ensure the values in this data source are used for identity resolution.

       When finished, click **Activate**.


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link
     - Find the courier related to the feed that was just activated, and then run it manually.

       On the **Sources** page, under **Couriers**, find the courier you want to run and then select **Run** from the actions menu.

       .. image:: ../../images/mockup-courier-add-07-menu-run.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       Select a date from the calendar picker that is before today, but after the date on which the file was added to the |source-name| bucket.

       .. image:: ../../images/mockup-courier-add-07-menu-load-data.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       Leave the load options in the **Run courier** dialog box unselected, and then click **Run**.

       After the courier has run successfully, inspect the domain table that contains the data that was loaded to Amperity. After you have verified that the data is correct, you may do any of the following:

       * If the data contains customer records, edit the feed and make that data available to Stitch.
       * If the data should be loaded to Amperity on a regular basis, add the courier to a courier group that runs on the desired schedule.
       * If the data will be a foundation for custom domain tables, use Spark SQL to build out that customization.

.. source-azure-blob-storage-add-data-source-steps-end


.. _source-azure-blob-storage-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. source-azure-blob-storage-workflow-actions-start

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

       * :ref:`source-azure-blob-storage-workflow-actions-bad-archive`
       * :ref:`source-azure-blob-storage-workflow-actions-invalid-credentials`
       * :ref:`source-azure-blob-storage-workflow-actions-invalid-permissions`
       * :ref:`source-azure-blob-storage-workflow-actions-missing-file`
       * :ref:`source-azure-blob-storage-workflow-actions-pgp-error`
       * :ref:`source-azure-blob-storage-workflow-actions-unable-to-decompress-archive`

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

.. source-azure-blob-storage-workflow-actions-end


.. _source-azure-blob-storage-workflow-actions-bad-archive:

Bad archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-bad-archive-start
   :end-before: .. workflow-actions-files-generic-bad-archive-end


.. _source-azure-blob-storage-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-source-start
   :end-before: .. workflow-actions-generic-invalid-credentials-source-end


.. _source-azure-blob-storage-workflow-actions-invalid-permissions:

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


.. _source-azure-blob-storage-workflow-actions-missing-file:

Missing file
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-missing-file-start
   :end-before: .. workflow-actions-files-generic-missing-file-end


.. _source-azure-blob-storage-workflow-actions-pgp-error:

PGP error
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-pgp-error-start
   :end-before: .. workflow-actions-generic-pgp-error-end


.. _source-azure-blob-storage-workflow-actions-unable-to-decompress-archive:

Unable to decompress archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-unable-to-decompress-file-start
   :end-before: .. workflow-actions-files-unable-to-decompress-file-end