.. https://docs.amperity.com/operator/


.. |source-name| replace:: Salesforce Sales Cloud
.. |plugin-name| replace:: Salesforce Sales Cloud
.. |feed-name| replace:: Accounts
.. |example-filename| replace:: accounts.ndjson
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: customer records
.. |credential-type| replace:: **salesforce**
.. |filter-the-list| replace:: "sales"

.. meta::
    :description lang=en:
        Configure Amperity to pull data from Salesforce Sales Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Salesforce Sales Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Salesforce Sales Cloud

==================================================
Pull from Salesforce Sales Cloud
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-sales-cloud-start
   :end-before: .. term-salesforce-sales-cloud-end

.. source-salesforce-sales-cloud-rest-api-start

Salesforce Sales Cloud is a REST API that provides data for files and reports. Amperity can pull this data from Salesforce Sales Cloud for any or all of the resources that are defined for the Salesforce account.

* Salesforce Sales Cloud query results are always loaded into Amperity in full.
* Any date range supplied indirectly via a courier group is ignored.
* No input is needed when running a query manually.

.. source-salesforce-sales-cloud-rest-api-end

.. source-salesforce-sales-cloud-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-salesforce-sales-cloud-get-details>`
#. :ref:`Add data source and feed <source-salesforce-sales-cloud-add-data-source>`

.. source-salesforce-sales-cloud-steps-to-pull-end


.. _source-salesforce-sales-cloud-get-details:

Get details
==================================================

.. source-salesforce-sales-cloud-get-details-start

Salesforce Sales Cloud requires the following configuration details:

#. The username and password of a Salesforce account configured for API access.
#. The Salesforce Sales Cloud security token that belongs to username. (The security token is not required if IP range policies are configured from the Salesforce admin console.)
#. The scheme and host for a custom Salesforce Sales Cloud URL, if used by customer.
#. If Salesforce Sales Cloud will send data to Amperity from a sandbox instance.
#. A sample for each file to simplify feed creation.

.. tip:: Use SnapPass to securely share the credentials and setup information for |source-name| between your company and your Amperity representative.

.. source-salesforce-sales-cloud-get-details-end


.. _source-salesforce-sales-cloud-add-data-source:

Add data source and feed
==================================================

.. source-salesforce-sales-cloud-add-data-source-intro-start-start

Add a data source that pulls data from an |source-name| bucket for each file that you want to pull to Amperity.

Browse the |source-name| bucket to select a file, and then review the settings for that file. Define the feed schema, and then activate the feed. Run the courier manually, and then review the data that is added to the domain table that is associated with the feed.

.. source-salesforce-sales-cloud-add-data-source-intro-end

**To add a data source for any SFTP site**

.. source-salesforce-sales-cloud-add-data-source-steps-start

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

       .. image:: ../../images/mockup-sources-add-01-select-source-sftp.png
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

          .. image:: ../../images/mockup-credentials-add-02-credential-status-sftp.png
             :width: 380 px
             :alt: Add 
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Select the file that will be pulled to Amperity, either directly (by going into the SFTP site and selecting it) or by providing a filename pattern.

       .. image:: ../../images/mockup-sources-add-03-file-settings.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       Click **Browse** to open the **File browser**. Select the file that will be pulled to Amperity, and then click **Accept**.

       Use a filename pattern to define files that will be loaded on a recurring basis, but will have small changes to the filename over time, such as having a datestamp appended to the filename.

       .. note:: For a new feed, this file is *also* used as the sample file that is used to define the schema. For an existing feed, this file must match the schema that has already been defined.

       .. image:: ../../images/mockup-sources-add-03-file-browser-sftp.png
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

       The contents of the file may be viewed as a table and in the raw format. Switch between these views using the **Table** and **Raw** buttons, and then click **Refresh** to view the file in that format.

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

.. source-salesforce-sales-cloud-add-data-source-steps-end
