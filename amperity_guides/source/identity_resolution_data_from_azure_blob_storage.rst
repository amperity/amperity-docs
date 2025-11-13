.. https://docs.amperity.com/guides/

.. |source-name| replace:: Azure Blob Storage

.. meta::
    :description lang=en:
        Configure Amperity to pull data from any Azure Blob Storage bucket.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from any Azure Blob Storage bucket.

.. meta::
    :content class=swiftype name=title data-type=string:
        Azure Blob Storage

==================================================
Azure Blob Storage
==================================================

.. identity-resolution-data-from-azure-blob-storage-start

Amperity can pull data in a wide variety of file types, file formats, and file sizes from |source-name|, which is a common data source across all Amperity tenants.

.. identity-resolution-data-from-azure-blob-storage-end

.. identity-resolution-data-from-azure-blob-storage-prerequisites-start

.. note:: Review `Pull from Azure Blob Storage <../operator/source_azure_blob_storage.html>`__ for more information about prerequisites, requirements, and optional configurations for |source-name|. All configuration prerequisites must be completed before stepping through this workflow.

.. identity-resolution-data-from-azure-blob-storage-prerequisites-start

**To add an inbound bridge**

.. source-azure-blob-storage-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - On the **Identity resolution** page in **Quick start**, from the **Add data source** dropdown select **Azure Blob Storage**.

       .. image:: ../../images/mockup-guided-idres-source-azure-blob-storage.png
          :width: 500 px
          :alt: Add a data source.
          :align: left
          :class: no-scaled-link

       This opens the **Add courier** dialog box.


   * - .. image:: ../../images/steps-02.png
          :width: 60px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-already-configured-start
          :end-before: .. credentials-sources-configure-already-configured-end

       .. tip::

          .. include:: ../../shared/credentials.rst
             :start-after: .. credentials-sources-configure-already-configured-tip-intro-start
             :end-before: .. credentials-sources-configure-already-configured-tip-intro-end

          .. image:: ../../images/mockup-credentials-add-02-credential-status-azure-blob-storage.png
             :width: 360 px
             :alt: Add.
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Add a name for the data source to the **Source name** field.

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-select-file-start
          :end-before: .. sources-steps-03-select-file-end

       .. image:: ../../images/mockup-sources-add-03-file-settings.png
          :width: 380 px
          :alt: Add a data source.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-browse-start
          :end-before: .. sources-steps-03-browse-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-browse-note-start
          :end-before: .. sources-steps-03-browse-note-end

       .. image:: ../../images/mockup-sources-add-03-file-browser-sftp.png
          :width: 500 px
          :alt: Add a data source.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-pgp-start
          :end-before: .. sources-steps-03-pgp-end

       .. image:: ../../images/mockup-sources-add-03-pgp-credential.png
          :width: 500 px
          :alt: Add a data source.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-start
          :end-before: .. sources-steps-04-review-end

       .. image:: ../../images/mockup-sources-add-03-file-formatting.png
          :width: 380 px
          :alt: Add.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-contents-start
          :end-before: .. sources-steps-04-review-contents-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-pgp-start
          :end-before: .. sources-steps-04-review-pgp-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-formatting-details-start
          :end-before: .. sources-steps-04-review-formatting-details-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-file-types-start
          :end-before: .. sources-steps-04-file-types-end

       Click **Save and continue**.


   * - .. image:: ../../images/steps-05.png
          :width: 60px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-calendar-start
          :end-before: .. sources-steps-07-calendar-end

       .. image:: ../../images/mockup-courier-add-07-menu-load-data.png
          :width: 380 px
          :alt: Add.
          :align: left
          :class: no-scaled-link

       Leave the load options unselected, and then click **Run**.

.. source-azure-blob-storage-add-bridge-steps-end