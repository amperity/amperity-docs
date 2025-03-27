.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Google Cloud Storage
.. |plugin-name| replace:: Google Cloud Storage
.. |what-send| replace:: files
.. |email-plus-send| replace:: additional attributes
.. |filter-the-list| replace:: "google"
.. |file-format| replace:: Apache Parquet (recommended), CSV, TSV, or PSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by |destination-name| were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_google_cloud_storage|
.. |channel-link| replace:: |campaign_google_cloud_storage|


==================================================
Send data to Google Cloud Storage
==================================================

.. note:: This topic contains information for configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination for sending query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/datagrid/destination_google_cloud_storage.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-cloud-storage-start
   :end-before: .. term-google-cloud-storage-end

.. destination-google-cloud-storage-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-google-cloud-storage-get-details>`
#. :ref:`Add destination <destination-google-cloud-storage-add-destination>`
#. :ref:`Add data template <destination-google-cloud-storage-add-data-template>`

.. destination-google-cloud-storage-steps-to-send-end


.. _destination-google-cloud-storage-get-details:

Get details
==================================================

.. destination-google-cloud-storage-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - A |destination-name| :ref:`service account key <destination-google-cloud-storage-service-account>` that is configured for the **Storage Object Admin** role.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The name of the |destination-name| bucket to which Amperity will send data and its prefix.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The public key to use for PGP encryption.

.. destination-google-cloud-storage-get-details-end

.. destination-google-cloud-storage-get-details-account-info-start

.. admonition:: How do I find |destination-name| account information?

   You can find all of this information after you log into |destination-name|.

.. destination-google-cloud-storage-get-details-account-info-end


.. _destination-google-cloud-storage-service-account:

Service account
==================================================

.. destination-google-cloud-storage-service-account-start

A service account must be configured to allow Amperity to send data to the Cloud Storage bucket:

#. A :ref:`service account key <destination-google-cloud-storage-service-account-key>` must be created, and then downloaded for use when configuring Amperity.
#. The **Storage Object Admin** :ref:`role must be assigned to the service account <destination-google-cloud-storage-service-account-role>`.

.. destination-google-cloud-storage-service-account-end


.. _destination-google-cloud-storage-service-account-key:

Service account key
--------------------------------------------------

.. destination-google-cloud-storage-service-account-key-start

A service account key must be downloaded so that it may be used to configure the destination in Amperity.

.. destination-google-cloud-storage-service-account-key-end

**To configure the service account key**

.. destination-google-cloud-storage-service-account-key-steps-start

#. Open the Cloud Platform console.
#. Click **IAM**, and then **Admin**.
#. Click the name of the project that is associated with the Cloud Storage bucket to which Amperity will send data.
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

.. destination-google-cloud-storage-service-account-key-steps-end

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
--------------------------------------------------

.. destination-google-cloud-storage-service-account-role-start

The **Storage Object Admin** role must be assigned to the service account.

.. destination-google-cloud-storage-service-account-role-end

**To configure the service account role**

.. destination-google-cloud-storage-service-account-role-steps-start

#. Open the Cloud Platform console.
#. Click **Storage**, and then **Browser**.
#. Click the name of the bucket from which Amperity will pull data.
#. Click the **Permissions** tab, and then click **Add**.
#. Enter the email address of the Cloud Storage service account.
#. Under **Role**, choose **Storage Object Admin**.

   .. important:: Amperity requires the **Storage Object Admin** role for the courier that is assigned to pull data from Cloud Storage.
#. Click **Save**.

.. destination-google-cloud-storage-service-account-role-steps-end


.. _destination-google-cloud-storage-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

.. destination-google-cloud-storage-add-destination-important-start

.. important:: The bucket name must match the value of the ``<<GCS_BUCKET_NAME>>`` placeholder shown in the :ref:`service account key <destination-google-cloud-storage-service-account-key>` example.

.. destination-google-cloud-storage-add-destination-important-end

**To add a destination**

.. destination-google-cloud-storage-add-destination-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-name-and-description-start
          :end-before: .. destinations-add-name-and-description-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-01-select.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       |destination-name| has the following settings:

       * The name of the bucket to which Amperity will send data.
       * The service account key.

         The service account key is the contents of the JSON file downloaded from Cloud Storage. Open the JSON file in a text editor, select all of the content in the JSON file, copy it, and then paste it into the **Service Account Key** field.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings.png
          :width: 500 px
          :alt: Settings for Google Cloud Storage.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-google-cloud-storage-start
          :end-before: .. destinations-destination-settings-google-cloud-storage-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-google-cloud-storage-add-destination-steps-end


.. _destination-google-cloud-storage-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-google-cloud-storage-add-data-template-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-start
          :end-before: .. destinations-data-template-open-template-end

       .. image:: ../../images/mockup-data-template-tab-add-01-details.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-name-start
          :end-before: .. destinations-data-template-open-template-name-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-allow-campaigns-start
          :end-before: .. destinations-data-template-business-users-allow-campaigns-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       .. image:: ../../images/mockup-data-template-tab-add-03-settings.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-note-start
          :end-before: .. destinations-data-template-verify-config-settings-note-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-start
          :end-before: .. destinations-data-template-save-end

       .. image:: ../../images/mockup-destinations-tab-add-05-save.png
          :width: 500 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-after-start
          :end-before: .. destinations-data-template-save-after-end

.. destination-google-cloud-storage-add-data-template-steps-end


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
