.. https://docs.amperity.com/operator/


.. |source-name| replace:: Google Cloud Storage
.. |plugin-name| replace:: Google Cloud Storage
.. |feed-name| replace:: CustomerRecords
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: files in any supported format
.. |credential-type| replace:: **gcs-service-account-key**


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
#. :ref:`Add courier <source-google-cloud-storage-add-courier>`
#. :ref:`Get sample files <source-google-cloud-storage-get-sample-files>`
#. :ref:`Add feeds <source-google-cloud-storage-add-feeds>`
#. :ref:`Add load operations <source-google-cloud-storage-add-load-operations>`
#. :ref:`Run courier <source-google-cloud-storage-run-courier>`
#. :ref:`Add to courier group <source-google-cloud-storage-add-to-courier-group>`

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

Dataflow is a fully-managed service for transforming and enriching data using stream (real-time) and/or batch modes that can be configured to |ext_google_pubsub_stream| to Cloud Storage.

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


.. _source-google-cloud-storage-add-courier:

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

.. source-google-cloud-storage-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. From the **Credential** drop-down, select **Create a new credential**. This opens the **Create New Credential** dialog box. 
#. Enter a name for the credential, the Cloud Storage bucket name, and the service account key. Click **Save**.

   .. important:: The bucket name must match the value of the **<<GCS_BUCKET_NAME>>** placeholder shown in the :ref:`service account key <source-google-cloud-storage-service-account-key>` example.

   .. note:: The :ref:`service account key <source-google-cloud-storage-service-account-key>` is the contents of the JSON file downloaded from Cloud Storage. Open the JSON file in a text editor, copy the key, and paste it into the **Service Account Key** field.

#. Under **Google Cloud Storage Settings** configure the list of files to pull to Amperity. Configure the **Entities List** for each file to be loaded to Amperity. For example, two files: "CustomerRecords.csv" and "TransactionRecords.csv".

   ::

      [
        {
          "object/type": "file",
          "object/file-pattern": "'CUSTOMER/ENV/CustomerRecords_'11-10-2020'.csv'",
          "object/land-as": {
            "file/header-rows": 1,
            "file/tag": "customer-records-2020",
            "file/content-type": "text/csv"
          }
        },
        {
          "archive/contents": {
            "FILENAME": {
              "subobject/land-as": {
                "file/tag": "transaction-records-2020",
                "file/content-type": "text/csv"
              }
            }
          },
          "object/type": "archive",
          "object/file-pattern": "'ARCHIVED/TransactionRecords_'11-10-2020'.zip'"
        }
      ]

#. Under **Google Cloud Storage Settings** set the load operations to a string that is obviously incorrect, such as **df-xxxxxx**. (You may also set the load operation to empty: "{}".)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to "{}" the validation test for the courier configuration settings will fail.
#. Click **Save**.

.. source-google-cloud-storage-add-courier-steps-end


.. _source-google-cloud-storage-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-google-cloud-storage-add-feeds:

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


.. _source-google-cloud-storage-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-google-cloud-storage-add-load-operations-example-start

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

.. source-google-cloud-storage-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-google-cloud-storage-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-google-cloud-storage-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end


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
