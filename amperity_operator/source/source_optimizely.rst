.. https://docs.amperity.com/operator/


.. |source-name| replace:: Optimizely
.. |plugin-name| replace:: Amazon S3
.. |feed-name| replace:: Decisions
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: interactions records
.. |credential-type| replace:: **iam-credential**
.. |filter-the-list| replace:: "ama"


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

Optimizely can send `enriched exports events <https://docs.developers.optimizely.com/web/docs/enriched-events-export>`__ |ext_link| data to Amperity via Amazon S3. Enriched events include details such as event timestamps, event IDs, event tags, event names, visitor IDs, session IDs, experiment IDs, and variation IDs.

.. source-optimizely-about-end

.. source-optimizely-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-optimizely-get-details>`
#. :ref:`Review Amazon S3 requirements for Optimizely <source-optimizely-filedrop-requirements>`
#. :ref:`Add data source and feed <source-optimizely-add-data-source>`

.. source-optimizely-steps-to-pull-end


.. _source-optimizely-get-details:

Get details
==================================================

.. source-optimizely-get-details-start

Amperity can be configured to pull data from Optimizely using Amazon S3. This requires the following configuration details:

#. Access to an `Optimizely data service <https://docs.developers.optimizely.com/web/docs/access-optimizely-export-data-via-amazon-s3>`__ |ext_link| hosted in Amazon S3.
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


.. _source-optimizely-add-data-source:

Add data source and feed
==================================================

.. source-optimizely-add-data-source-intro-start-start

Add a data source that pulls data from an |source-name| bucket for each file that you want to pull to Amperity.

Browse the |source-name| bucket to select a file, and then review the settings for that file. Define the feed schema, and then activate the feed. Run the courier manually, and then review the data that is added to the domain table that is associated with the feed.

.. source-optimizely-add-data-source-intro-end

**To add a data source for an Amazon S3 bucket**

.. source-optimizely-add-data-source-steps-start

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

       .. image:: ../../images/mockup-sources-add-01-select-source.png
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
     - Select the file that will be pulled to Amperity, either directly (by going into the Amazon S3 bucket and selecting it) or by providing a filename pattern.

       .. image:: ../../images/mockup-sources-add-03-file-settings.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       Click **Browse** to open the **File browser**. Select the file that will be pulled to Amperity, and then click **Accept**.

       Use a filename pattern to define files that will be loaded on a recurring basis, but will have small changes to the filename over time, such as having a datestamp appended to the filename.

       .. note:: For a new feed, this file is *also* used as the sample file that is used to define the schema. For an existing feed, this file must match the schema that has already been defined.

       .. image:: ../../images/mockup-sources-add-03-file-browser-s3.png
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

       To use a new feed, choose the **Create new feed** option, select an existing source from the **Source** dropdown *or* type the name of a new data source, and then enter the name of the feed.

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

.. source-optimizely-add-data-source-steps-end
