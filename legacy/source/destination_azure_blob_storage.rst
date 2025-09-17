.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Azure Blob Storage
.. |plugin-name| replace:: Azure Blob Storage
.. |what-send| replace:: files
.. |email-plus-send| replace:: additional attributes
.. |filter-the-list| replace:: "az"
.. |azure-container-name| replace:: "Blob Storage"
.. |azure-blob-prefix| replace:: "upload"
.. |file-format| replace:: Apache Parquet (recommended), CSV, TSV, or PSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by |destination-name| were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_azure_blob_storage|
.. |channel-link| replace:: |campaign_azure_blob_storage|


==================================================
Configure campaigns for Azure Blob Storage
==================================================

.. vale off

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_azure_blob_storage.html>`__ |ext_link|.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-blob-storage-start
   :end-before: .. term-azure-blob-storage-end

.. destination-azure-blob-storage-important-start

.. important:: Use this destination to send data from Amperity to Azure Data Lake Storage Gen1 or Azure Data Lake Storage Gen2.

.. destination-azure-blob-storage-important-end

.. destination-azure-blob-storage-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-azure-blob-storage-get-details>`
#. :ref:`Add destination <destination-azure-blob-storage-add-destination>`
#. :ref:`Add data template <destination-azure-blob-storage-add-data-template>`

.. destination-azure-blob-storage-steps-to-send-end


.. _destination-azure-blob-storage-get-details:

Get details
==================================================

.. destination-amazon-s3-get-details-start

Amperity can be configured to send data to |destination-name|. This may be done using :ref:`Azure Data Share (recommended) <destination-azure-blob-storage-azure-data-share>` or by using :ref:`Azure credentials <destination-azure-blob-storage-credentials>`.

.. destination-amazon-s3-get-details-end


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

.. note:: If you have already configured Azure Data Share for an Azure Blob Storage data source you may use the same credential for this destination. If you have not configured Azure Data Share, ask your Amperity representative to help you with those configuration steps.

.. destination-azure-blob-storage-azure-data-share-end


.. _destination-azure-blob-storage-credentials:

Use credentials
--------------------------------------------------

.. destination-azure-blob-storage-credentials-start

|destination-name| requires the following configuration details:

#. The name of the container.
#. The blob prefix.
#. The credential details.

   These vary depending on the chosen credential method: `connection string <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account>`__ |ext_link|, `shared access signature (SAS) <https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli>`__ |ext_link| token, or `storage URI <https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata>`__ |ext_link|.

   When Microsoft Azure is configured to use a shared access signature (SAS) to grant restricted access rights to Microsoft Azure storage resources, be sure to use the correct SAS token string for credentials within Amperity and that the SAS is assigned the following permissions within Microsoft Azure: READ, ADD, CREATE, WRITE, DELETE, and LIST.

#. The public key to use for PGP encryption.

.. destination-azure-blob-storage-credentials-end


.. _destination-azure-blob-storage-add-destination:

Add destination
==================================================

.. destination-azure-blob-storage-add-destination-start

Azure Blob Storage is a destination that may be configured directly from Amperity.

.. destination-azure-blob-storage-add-destination-end

**To add a destination**

.. destination-azure-blob-storage-add-destination-steps-start

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

       * The name of the container.
       * The blob prefix.
       * Credential details. These vary depending on the chosen credential method: `connection string <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account>`__ |ext_link|, `shared access signature (SAS) <https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli>`__ |ext_link| token, or `storage URI <https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata>`__ |ext_link|.
       * The public key to use for PGP encryption.

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


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
          :alt: Settings for Azure Blob Storage.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-azure-blob-storage-start
          :end-before: .. destinations-destination-settings-azure-blob-storage-end


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

.. destination-azure-blob-storage-add-destination-steps-end


.. _destination-azure-blob-storage-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-azure-blob-storage-add-data-template-steps-start

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

.. destination-azure-blob-storage-add-data-template-steps-end


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
          :align: left
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

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-azure-blob-storage-workflow-actions-invalid-credentials`
       * :ref:`destination-azure-blob-storage-workflow-actions-invalid-permissions`


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
