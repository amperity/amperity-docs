.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Azure Blob Storage
.. |plugin-name| replace:: "Azure Blob Storage"
.. |credential-type| replace:: "azure-blob-connection-string", "azure-blob-shared-access-signature", or "azure-blob-storage-uri"
.. |required-credentials| replace:: "azure-blob-connection-string", "azure-blob-shared-access-signature", or "azure-blob-storage-uri"
.. |what-send| replace:: Apache Parquet (recommended), CSV, JSON, NDJSON, PSV, or TSV files
.. |where-send| replace:: any Azure Blob Storage container
.. |filter-the-list| replace:: "azure"


.. meta::
    :description lang=en:
        Configure Amperity to send data in any file format to an Azure Blob Storage container.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data in any file format to an Azure Blob Storage container.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Azure Blob Storage

==================================================
Configure destinations for Azure Blob Storage
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-azure-blob-storage-about-start
   :end-before: .. setting-azure-blob-storage-about-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-configure-start
   :end-before: .. setting-common-file-configure-end


.. _destination-azure-blob-storage-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-azure-blob-storage-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Azure Blob Storage container details**

       You will need to know the following details about the |destination-name| container to which Amperity will send data.

       #. The name of the |destination-name| container. A blob prefix is sometimes required.

       #. .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-cloud-storage-bucket-name-must-match-start
             :end-before: .. credential-google-cloud-storage-bucket-name-must-match-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Credential types and settings**

       Amperity supports the following credential types for |destination-name|:

       #. :ref:`Connection string <destination-azure-blob-storage-credentials-connection-string>`
       #. :ref:`Shared access signature <destination-azure-blob-storage-credentials-shared-access-signature>`
       #. :ref:`Storage URI <destination-azure-blob-storage-credentials-storage-uri>`


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
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

.. destination-azure-blob-storage-get-details-table-end


.. _destination-azure-blob-storage-azure-data-share:

Use Azure Data Share
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-data-share-start
   :end-before: .. term-azure-data-share-end

.. destination-azure-blob-storage-azure-data-share-start

Amperity prefers to send data to customer-managed cloud storage. This approach ensures that customers can:

* Use security policies managed in Azure Data Share to manage access to data
* Directly manage the files that are made available
* Modify access without requiring involvement by Amperity; access may be revoked at any time by either Azure account, after which data sharing ends immediately
* Directly troubleshoot incomplete or missing files

Amperity recommends to use Azure Data Share to manage access to customer-managed cloud storage in Azure. This allows managed security policies to control access to data.

.. TODO: Link to the source topic after this gets moved back into /datagrid.

.. note:: If you have already configured Azure Data Share for an Azure Blob Storage data source you may use the same process credential for this destination. If you have not configured Azure Data Share, ask your Amperity representative to help you with those configuration steps.

.. destination-azure-blob-storage-azure-data-share-end


.. _destination-azure-blob-storage-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

Amperity supports the following credential types for |destination-name|:

#. :ref:`Connection string <destination-azure-blob-storage-credentials-connection-string>`
#. :ref:`Shared access signature <destination-azure-blob-storage-credentials-shared-access-signature>`
#. :ref:`Storage URI <destination-azure-blob-storage-credentials-storage-uri>`

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end


.. _destination-azure-blob-storage-credentials-connection-string:

Connection string
--------------------------------------------------

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-azure-blob-storage-connection-string-overview-start
   :end-before: .. credential-azure-blob-storage-connection-string-overview-end

**To configure credentials using a connection string**

.. destination-azure-blob-storage-credentials-connection-string-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-multiple-start
          :end-before: .. credential-steps-select-type-multiple-end

       From the **Credential type** dropdown, select **azure-blob-connection-string**.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - The settings that are available for a credential are determined by the credential type. For the **azure-blob-connection-string** credential type, configure the following settings, and then click **Save**.

       .. image:: ../../images/mockup-credentials-add-01-settings-azure-blob-storage-connection-string.png
          :width: 360 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Connection string**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-azure-blob-storage-connection-string-start
             :end-before: .. credential-azure-blob-storage-connection-string-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-azure-blob-storage-connection-string-example-start
             :end-before: .. credential-azure-blob-storage-connection-string-example-end

       **Container**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-azure-blob-storage-container-start
             :end-before: .. credential-azure-blob-storage-container-end


.. destination-azure-blob-storage-credentials-connection-string-steps-end


.. _destination-azure-blob-storage-credentials-shared-access-signature:

Shared access signature
--------------------------------------------------

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-azure-blob-storage-shared-access-signature-overview-start
   :end-before: .. credential-azure-blob-storage-shared-access-signature-overview-end

.. important:: 

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-shared-access-signature-permissions-start
      :end-before: .. credential-azure-blob-storage-shared-access-signature-permissions-end

**To configure credentials using a shared access signature**

.. destination-azure-blob-storage-credentials-shared-access-signature-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

       .. image:: ../../images/mockup-credentials-add-01-settings-azure-blob-storage-shared-access-signature.png
          :width: 440 px
          :alt: Configure credentials for any Azure Blob Storage container.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-multiple-start
          :end-before: .. credential-steps-select-type-multiple-end

       From the **Credential type** dropdown, select **azure-blob-shared-access-signature**.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - The settings that are available for a credential are determined by the credential type. For the **azure-blob-shared-access-signature** credential type, configure the following settings, and then click **Save**.

       .. image:: ../../images/mockup-credentials-add-01-settings-azure-blob-storage-shared-access-signature.png
          :width: 360 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Account name**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-azure-blob-storage-account-name-start
             :end-before: .. credential-azure-blob-storage-account-name-end

       **Container**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-azure-blob-storage-container-start
             :end-before: .. credential-azure-blob-storage-container-end

       **Shared access signature**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-azure-blob-storage-shared-access-signature-start
             :end-before: .. credential-azure-blob-storage-shared-access-signature-end


.. destination-azure-blob-storage-credentials-shared-access-signature-steps-end


.. _destination-azure-blob-storage-credentials-storage-uri:

Storage URI
--------------------------------------------------

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-azure-blob-storage-storage-uri-overview-start
   :end-before: .. credential-azure-blob-storage-storage-uri-overview-end

**To configure credentials using a storage URI**

.. destination-azure-blob-storage-credentials-storage-uri-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

       .. image:: ../../images/mockup-credentials-add-01-settings-azure-blob-storage-storage-uri.png
          :width: 440 px
          :alt: Configure credentials for any Azure Blob Storage container.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-multiple-start
          :end-before: .. credential-steps-select-type-multiple-end

       From the **Credential type** dropdown, select **azure-blob-storage-uri**.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - The settings that are available for a credential are determined by the credential type. For the **azure-blob-storage-uri** credential type, configure the following settings, and then click **Save**.

       .. image:: ../../images/mockup-credentials-add-01-settings-azure-blob-storage-storage-uri.png
          :width: 360 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Container**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-azure-blob-storage-container-start
             :end-before: .. credential-azure-blob-storage-container-end

       **Storage URI**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-azure-blob-storage-storage-uri-start
             :end-before: .. credential-azure-blob-storage-storage-uri-end

.. destination-azure-blob-storage-credentials-storage-uri-steps-end


.. _destination-azure-blob-storage-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Azure Blob Storage**

.. destination-azure-blob-storage-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-azure-blob-storage.png
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
          :align: center
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
          :align: center
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
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Blob prefix**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-azure-blob-storage-blob-prefix-start
             :end-before: .. setting-azure-blob-storage-blob-prefix-end

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


       **Split outputs**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-split-outputs-start
             :end-before: .. setting-common-split-outputs-end


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
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


.. destination-azure-blob-storage-add-steps-end


.. _destination-azure-blob-storage-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-azure-blob-storage-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

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
          :align: center
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
          :align: center
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

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-azure-blob-storage-workflow-actions-invalid-credentials`
       * :ref:`destination-azure-blob-storage-workflow-actions-invalid-permissions`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
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

.. destination-azure-blob-storage-workflow-actions-end


.. _destination-azure-blob-storage-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-azure-blob-storage-workflow-actions-invalid-permissions:

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
