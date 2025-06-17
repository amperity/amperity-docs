.. https://docs.amperity.com/operator/


.. |source-name| replace:: Google Cloud Storage
.. |plugin-name| replace:: Google Cloud Storage
.. |feed-name| replace:: CustomerRecords
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: files in any supported format
.. |credential-type| replace:: **gcs-service-account-key**
.. |filter-the-list| replace:: "google"


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Google Cloud Storage.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Google Cloud Storage.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Google Cloud Storage

==================================================
Pull from Google Cloud Storage
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-cloud-storage-start
   :end-before: .. term-google-cloud-storage-end

.. source-google-cloud-storage-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-google-cloud-storage-get-details>`
#. :ref:`Review filedrop requirements for Google Cloud Storage <source-google-cloud-storage-filedrop-requirements>`
#. :ref:`Add data source and feed <source-google-cloud-storage-add-data-source>`

.. source-google-cloud-storage-steps-to-pull-end


.. _source-google-cloud-storage-get-details:

Get details
==================================================

.. source-google-cloud-storage-get-details-start

Google Cloud Storage requires the following configuration details:

#. The name of the bucket in Cloud Storage.
#. A Cloud Storage :ref:`service account key <source-google-cloud-storage-service-account>` that is configured for the **Storage Object Admin** role.
#. A list of objects (by filename and file type) in the Cloud Storage bucket.
#. A sample for each file to simplify feed creation.

.. source-google-cloud-storage-get-details-end


.. _source-google-cloud-storage-filedrop-requirements:

Filedrop recommendations
--------------------------------------------------

.. include:: ../../shared/file-formats.rst
   :start-after: .. formats-filedrop-common-start
   :end-before: .. formats-filedrop-common-end


.. _source-google-cloud-storage-options:

Options
--------------------------------------------------

.. TODO: This probably works, but has some specific requirements: https://cloud.google.com/bigquery/docs/exporting-data

.. source-google-cloud-storage-options-start

The following sections describe optional ways to get data to Cloud Storage.

* :ref:`source-google-cloud-storage-dataflow-pubsub`

.. source-google-cloud-storage-options-end


.. _source-google-cloud-storage-dataflow-pubsub:

Dataflow, Pub/Sub
++++++++++++++++++++++++++++++++++++++++++++++++++

.. source-google-cloud-storage-dataflow-pubsub-start

Dataflow is a fully-managed service for transforming and enriching data using stream (real-time) and/or batch modes that can be configured to `use Pub/Sub to stream messages <https://cloud.google.com/pubsub/docs/pubsub-dataflow#stream_messages_from_to>`__ |ext_link| to Cloud Storage.

.. source-google-cloud-storage-dataflow-pubsub-end

.. note:: 

   .. include:: ../../shared/terms.rst
      :start-after: .. term-google-pubsub-start
      :end-before: .. term-google-pubsub-end


.. _source-google-cloud-storage-service-account:

Service account
==================================================

.. source-google-cloud-storage-service-account-start

A service account must be configured to allow Amperity to pull data from the Cloud Storage bucket:

#. A :ref:`service account key <source-google-cloud-storage-service-account-key>` must be created, and then downloaded for use when configuring Amperity.
#. The **Storage Object Admin** :ref:`role must be assigned to the service account <source-google-cloud-storage-service-account-role>`.

.. source-google-cloud-storage-service-account-end


.. _source-google-cloud-storage-service-account-key:

Service account key
--------------------------------------------------

.. source-google-cloud-storage-service-account-key-start

A service account key must be downloaded so that it may be used to configure the courier in Amperity.

.. source-google-cloud-storage-service-account-key-end

**To configure the service account key**

.. source-google-cloud-storage-service-account-key-steps-start

Service account setup:

#. Open the Cloud Platform console.
#. Click **IAM**, and then **Admin**.
#. Click the name of the project that is associated with the Cloud Storage bucket from which Amperity will pull data.
#. Click **Service Accounts**, and then select **Create Service Account**.
#. In the **Name** field, give your service account a name. For example, "Amperity GCS Connection".
#. In the **Description** field, enter a description that will remind you of the purpose of the role.
#. Click **Create**.

   .. important:: Click **Continue** and *skip every step* that allows adding additional service account permissions. These permissions will be added directly to the bucket.
   
#. From the **Service Accounts** page, click the name of the service account that was created for Amperity.
#. Click **Add Key**, and then select **Create new key**.
#. Select the **JSON** key type, and then click **Create**.

   The key is downloaded as a JSON file to your local computer. This key is required to connect Amperity to your Cloud Storage bucket. If necessary, provide this key to your Amperity representative using |ext_snappass|.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-snappass-start
      :end-before: .. term-snappass-end

.. source-google-cloud-storage-service-account-key-steps-end

**Example**

.. source-google-cloud-storage-service-account-key-example-start

.. code-block:: json

   {
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "client_email": "<<GCS_BUCKET_NAME>>@<<GCS_PROJECT_ID>>.iam.gserviceaccount.com",
     "client_id": "redacted",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/<<GCS_BUCKET_NAME>>%40<<GCS_PROJECT_ID>>.iam.gserviceaccount.com",
     "private_key_id": "redacted",
     "private_key": "redacted",
     "project_id": "<<GCS_PROJECT_ID>>",
     "token_uri": "https://oauth2.googleapis.com/token",
     "type": "service_account"
   }

.. source-google-cloud-storage-service-account-key-example-end


.. _source-google-cloud-storage-service-account-role:

Service account role
--------------------------------------------------

.. source-google-cloud-storage-service-account-role-start

The **Storage Object Admin** role must be assigned to the service account.

.. source-google-cloud-storage-service-account-role-end

**To configure the service account role**

.. source-google-cloud-storage-service-account-role-steps-start

#. Open the Cloud Platform console.
#. Click **Storage**, and then **Browser**.
#. Click the name of the bucket from which Amperity will pull data.
#. Click the **Permissions** tab, and then click **Add**.
#. Enter the email address of the Cloud Storage service account.
#. Under **Role**, choose **Storage Object Admin**.

   .. important:: Amperity requires the **Storage Object Admin** role for the courier that is assigned to pull data from Cloud Storage.
#. Click **Save**.

.. source-google-cloud-storage-service-account-role-steps-end


.. _source-google-cloud-storage-add-data-source:

Add data source and feed
==================================================

.. source-google-cloud-storage-add-data-source-intro-start-start

Add a data source that pulls data from an |source-name| bucket for each file that you want to pull to Amperity.

Browse the |source-name| bucket to select a file, and then review the settings for that file. Define the feed schema, and then activate the feed. Run the courier manually, and then review the data that is added to the domain table that is associated with the feed.

.. source-google-cloud-storage-add-data-source-intro-end

**To add a data source for an Amazon S3 bucket**

.. source-google-cloud-storage-add-data-source-steps-start

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

       .. image:: ../../images/mockup-sources-add-03-file-browser-google-cloud-storage.png
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

.. source-google-cloud-storage-add-data-source-steps-end


.. _source-google-cloud-storage-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. source-google-cloud-storage-workflow-actions-start

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

       .. image:: ../../images/mockup-destinations-tab-workflow-error.png
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
          :alt: The Workflow page, showing a workflow with errors.
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

       .. image:: ../../images/workflow-actions-s3-generic-invalid-bucket-name.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |source-name|, including:

       * :ref:`source-google-cloud-storage-workflow-actions-bad-archive`
       * :ref:`source-google-cloud-storage-workflow-actions-invalid-credentials`
       * :ref:`source-google-cloud-storage-workflow-actions-missing-file`
       * :ref:`source-google-cloud-storage-workflow-actions-pgp-error`
       * :ref:`source-google-cloud-storage-workflow-actions-unable-to-decompress-archive`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-s3-generic-invalid-bucket-name-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. source-google-cloud-storage-workflow-actions-end


.. _source-google-cloud-storage-workflow-actions-bad-archive:

Bad archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-bad-archive-start
   :end-before: .. workflow-actions-files-generic-bad-archive-end


.. _source-google-cloud-storage-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-source-start
   :end-before: .. workflow-actions-generic-invalid-credentials-source-end


.. _source-google-cloud-storage-workflow-actions-missing-file:

Missing file
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-missing-file-start
   :end-before: .. workflow-actions-files-generic-missing-file-end


.. _source-google-cloud-storage-workflow-actions-pgp-error:

PGP error
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-pgp-error-start
   :end-before: .. workflow-actions-generic-pgp-error-end


.. _source-google-cloud-storage-workflow-actions-unable-to-decompress-archive:

Unable to decompress archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-unable-to-decompress-file-start
   :end-before: .. workflow-actions-files-unable-to-decompress-file-end
