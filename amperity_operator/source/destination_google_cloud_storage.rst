.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Cloud Storage
.. |plugin-name| replace:: "Google Cloud Storage"
.. |credential-type| replace:: "gcs-service-account-key"
.. |required-credentials| replace:: "gcs-service-account-key"
.. |what-send| replace:: Apache Parquet (recommended), CSV, JSON, NDJSON, PSV, or TSV files
.. |where-send| replace:: any Google Cloud Storage bucket
.. |filter-the-list| replace:: "google"


.. meta::
    :description lang=en:
        Configure Amperity to send data in any file format to an Google Cloud Storage bucket.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data in any file format to an Google Cloud Storage bucket.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destination for Google Cloud Storage

==================================================
Configure destination for Google Cloud Storage
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_google_cloud_storage.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-cloud-storage-start
   :end-before: .. term-google-cloud-storage-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-configure-start
   :end-before: .. setting-common-file-configure-end


.. _destination-google-cloud-storage-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-google-cloud-storage-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Google Cloud Storage bucket details**

       You will need to know the following details about the |destination-name| bucket to which Amperity will send data.

       #. The name of the |destination-name| bucket. An object prefix is sometimes required.

          .. important::

             .. include:: ../../shared/credentials_settings.rst
                :start-after: .. credential-google-cloud-storage-bucket-name-must-match-start
                :end-before: .. credential-google-cloud-storage-bucket-name-must-match-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Credential types and settings**

       A |destination-name| :ref:`service account key <destination-google-cloud-storage-service-accounts>` must be configured for the **Storage Object Admin** role.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **File format**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-start
             :end-before: .. setting-common-file-format-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-custom-delimiter-start
             :end-before: .. setting-common-file-format-custom-delimiter-end

       .. note::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-optional-settings-start
             :end-before: .. setting-common-optional-settings-end

.. destination-google-cloud-storage-get-details-table-end


.. _destination-google-cloud-storage-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Google Cloud Storage**

.. destination-google-cloud-storage-credentials-connection-string-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Bucket name**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-cloud-storage-bucket-name-start
             :end-before: .. credential-google-cloud-storage-bucket-name-end

          .. important::

             .. include:: ../../shared/credentials_settings.rst
                :start-after: .. credential-google-cloud-storage-bucket-name-must-match-start
                :end-before: .. credential-google-cloud-storage-bucket-name-must-match-end


       **Service account key**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-cloud-storage-service-account-key-start
             :end-before: .. credential-google-cloud-storage-service-account-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-cloud-storage-service-account-key-value-start
             :end-before: .. credential-google-cloud-storage-service-account-key-value-end

.. destination-google-cloud-storage-credentials-connection-string-steps-end



.. _destination-google-cloud-storage-service-accounts:

About service accounts
--------------------------------------------------

.. destination-google-cloud-storage-service-accounts-start

A service account must be configured to allow Amperity to send data to the |destination-name| bucket:

#. A :ref:`service account key <destination-google-cloud-storage-service-account-key>` must be created, and then downloaded for use when configuring Amperity.
#. The **Storage Object Admin** :ref:`role must be assigned to the service account role <destination-google-cloud-storage-service-account-role>`.

.. destination-google-cloud-storage-service-accounts-end


.. _destination-google-cloud-storage-service-account-key:

Service account key
++++++++++++++++++++++++++++++++++++++++++++++++++

.. destination-google-cloud-storage-service-account-key-start

A service account key must be downloaded so that it may be used to configure the destination in Amperity.

.. destination-google-cloud-storage-service-account-key-end

**To configure the service account key**

.. destination-google-cloud-storage-service-account-key-steps-start

#. Open the Google Cloud Platform console.
#. Click **IAM**, and then **Admin**.
#. Click the name of the project that is associated with the |destination-name| bucket to which Amperity will send data.
#. Click **Service Accounts**, and then select **Create Service Account**.
#. In the **Name** field, give your service account a name. For example, "Amperity GCS Connection".
#. In the **Description** field, enter a description that will remind you of the purpose of the role.
#. Click **Create**.

   .. important:: Click **Continue** and *skip every step* that allows adding additional service account permissions. These permissions will be added directly to the bucket.
   
#. From the **Service Accounts** page, click the name of the service account that was created for Amperity.
#. Click **Add Key**, and then select **Create new key**.
#. Select the **JSON** key type, and then click **Create**.

   The key is downloaded as a JSON file to your local computer. This key is required to connect Amperity to your |destination-name| bucket. If necessary, provide this key to your Amperity representative using |ext_snappass|.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-snappass-start
      :end-before: .. term-snappass-end

.. destination-google-cloud-storage-service-account-key-steps-end

.. _destination-google-cloud-storage-service-account-key-example:

**Example**

.. destination-google-cloud-storage-service-account-key-example-start

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

.. destination-google-cloud-storage-service-account-key-example-end


.. _destination-google-cloud-storage-service-account-role:

Service account role
++++++++++++++++++++++++++++++++++++++++++++++++++

.. destination-google-cloud-storage-service-account-role-start

The **Storage Object Admin** role must be assigned to the service account.

.. destination-google-cloud-storage-service-account-role-end

**To configure the service account role**

.. destination-google-cloud-storage-service-account-role-steps-start

#. Open the Google Cloud Platform console.
#. Click **Storage**, and then **Browser**.
#. Click the name of the bucket from which Amperity will pull data.
#. Click the **Permissions** tab, and then click **Add**.
#. Enter the email address of the |destination-name| service account.
#. Under **Role**, choose **Storage Object Admin**.

   .. important:: Amperity requires the **Storage Object Admin** role for the courier that is assigned to pull data from |destination-name|.
#. Click **Save**.

.. destination-google-cloud-storage-service-account-role-steps-end


.. _destination-google-cloud-storage-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Cloud Storage**

.. destination-google-cloud-storage-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-google-cloud-storage.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Compression**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-compression-start
             :end-before: .. setting-common-compression-end


       **Escape character**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-escape-character-start
             :end-before: .. setting-common-escape-character-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-escape-character-unspecified-start
             :end-before: .. setting-common-escape-character-unspecified-end


       **File format**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-start
             :end-before: .. setting-common-file-format-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-custom-delimiter-start
             :end-before: .. setting-common-file-format-custom-delimiter-end

          **Apache Parquet files only**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-apache-parquet-start
             :end-before: .. setting-common-file-format-apache-parquet-end


       **Filename template**
          .. include:: ../../shared/terms.rst
             :start-after: .. term-filename-template-start
             :end-before: .. term-filename-template-end


       **Header**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-header-start
             :end-before: .. setting-common-header-end


       **Object prefix**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-cloud-storage-object-prefix-start
             :end-before: .. setting-google-cloud-storage-object-prefix-end


       **PGP public key**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-pgp-public-key-start
             :end-before: .. setting-common-pgp-public-key-end


       **Quote mode**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-quote-mode-start
             :end-before: .. setting-common-quote-mode-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-quote-mode-none-start
             :end-before: .. setting-common-quote-mode-none-end


       **Success file**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-success-file-start
             :end-before: .. setting-common-success-file-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-success-file-downstream-start
             :end-before: .. setting-common-success-file-downstream-end


       **Use Zip64?**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-use-zip64-start
             :end-before: .. setting-common-use-zip64-end

       **Row Number**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-row-number-start
             :end-before: .. setting-common-row-number-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-row-number-column-name-start
             :end-before: .. setting-common-row-number-column-name-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


.. destination-google-cloud-storage-add-steps-end


.. _destination-google-cloud-storage-workflow-actions:

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
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

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

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-google-cloud-storage-workflow-actions-invalid-credentials`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-gcs-invalid-credentials-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-google-cloud-storage-workflow-actions-end


.. _destination-google-cloud-storage-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end
