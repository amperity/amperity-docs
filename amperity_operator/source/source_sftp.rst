.. https://docs.amperity.com/operator/


.. |source-name| replace:: SFTP
.. |plugin-name| replace:: SFTP
.. |feed-name| replace:: CustomerRecords
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **passphrase**
.. |sftp-hostname| replace:: **sftp.[domain-name].com**
.. |what-pull| replace:: files in any supported format
.. |filter-the-list| replace:: "sftp"


.. meta::
    :description lang=en:
        Configure Amperity to pull data from any SFTP site.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from any SFTP site.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from any SFTP site

==================================================
Pull from any SFTP site
==================================================

.. source-sftp-common-start

SFTP is a common way to make data sources available to Amperity. For example: files are made available from a SFTP site and are frequently refreshed. Use a courier to connect to the SFTP site and pull the refreshed files to Amperity on a regular basis.

.. note:: When using SFTP as a data source, a sample file is often required to set up the initial feed and courier processes.

.. source-sftp-common-end

.. source-sftp-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-sftp-get-details>`
#. :ref:`Add data source <source-sftp-add-data-source>`

.. source-sftp-steps-to-pull-end


.. _source-sftp-get-details:

Get details
==================================================

.. source-sftp-get-details-start

The |source-name| data source requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The hostname and port for the SFTP site from which data will be pulled. For example, "sftp.acme.com" and "20".

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The username and passphrase.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The host public key (if encryption is configured).

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - A private key when the "private-key" credential type is selected.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The public key to use for PGP encryption.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The remote folder from which Amperity will pull data.

       .. important:: A "/" (forward slash) must be used as the first character for this value. For example: "/folder/name".

       The location must contain the list of files (by filename and file type, e.g. "accounts.csv", "customers.ndjson", "email-list.tsv", and so on) that are to be pulled to Amperity. A sample of each file is used during feed creation.

.. source-sftp-get-details-end


.. _source-sftp-get-details-amperity:

Included SFTP site
--------------------------------------------------

.. source-sftp-get-details-amperity-start

Every Amperity tenant includes an SFTP site with a hostname of ``<tenant>.sftp.amperity.com``. For example, if your company name is **ACME**, then your tenant's SFTP hostname is ``acme.sftp.amperity.com``. (The hostname is always all lowercase.)

.. note:: The SFTP site is provisioned by an Amperity administrator *after* the initial tenant creation. As such, the SFTP site is not immediately available, but this is not a long process. When the SFTP site is ready, Amperity will use SnapPass to send you the connection details. If you wish to use RSA key-based authentication, please provide the public key to your Amperity administrator when requesting SFTP access.

Once this site is provisioned, you may configure the SFTP site as an SFTP source or an SFTP destination to support any desired workflow. External customer processes can be configured to connect to the site using SFTP, after which they can add data to or pick up data from the site to support any external workflow.

.. caution:: The SFTP server has a 30-day limit on data and after 30 days, data may be moved automatically to an archive location. This location is still accessible to Amperity in case it becomes necessary to reuse it.

.. important:: The hostname for the SFTP site is always ``<tenant-name>.sftp.amperity.com``. Some older tenants may still be using the legacy address ``sftp.amperity.com``, if so, please contact your Amperity administrator about migrating.

.. source-sftp-get-details-amperity-end


.. _source-sftp-filedrop-requirements:

Filedrop recommendations
--------------------------------------------------

.. include:: ../../shared/file-formats.rst
   :start-after: .. formats-filedrop-common-start
   :end-before: .. formats-filedrop-common-end


.. _source-sftp-add-data-source:

Add data source and feed
==================================================

.. source-sftp-add-data-source-intro-start-start

Add a data source that pulls data from an |source-name| bucket for each file that you want to pull to Amperity.

Browse the |source-name| bucket to select a file, and then review the settings for that file. Define the feed schema, and then activate the feed. Run the courier manually, and then review the data that is added to the domain table that is associated with the feed.

.. source-sftp-add-data-source-intro-end

**To add a data source for any SFTP site**

.. source-sftp-add-data-source-steps-start

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

.. source-sftp-add-data-source-steps-end


.. _source-sftp-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. source-sftp-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-sftp-unavailable.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |source-name|, including:

       * :ref:`source-sftp-workflow-actions-bad-archive`
       * :ref:`source-sftp-workflow-actions-invalid-credentials`
       * :ref:`source-sftp-workflow-actions-missing-file`
       * :ref:`source-sftp-workflow-actions-sftp-unavailable`
       * :ref:`source-sftp-workflow-actions-pgp-error`
       * :ref:`source-sftp-workflow-actions-unable-to-decompress-archive`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-sftp-unavailable-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. source-sftp-workflow-actions-end


.. _source-sftp-workflow-actions-bad-archive:

Bad archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-bad-archive-start
   :end-before: .. workflow-actions-files-generic-bad-archive-end


.. _source-sftp-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-source-start
   :end-before: .. workflow-actions-generic-invalid-credentials-source-end


.. _source-sftp-workflow-actions-missing-file:

Missing file
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-missing-file-start
   :end-before: .. workflow-actions-files-generic-missing-file-end


.. _source-sftp-workflow-actions-pgp-error:

PGP error
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-pgp-error-start
   :end-before: .. workflow-actions-generic-pgp-error-end


.. _source-sftp-workflow-actions-sftp-unavailable:

SFTP site unavailable
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-sftp-generic-unavailable-start
   :end-before: .. workflow-actions-sftp-generic-unavailable-end


.. _source-sftp-workflow-actions-unable-to-decompress-archive:

Unable to decompress archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-unable-to-decompress-file-start
   :end-before: .. workflow-actions-files-unable-to-decompress-file-end
