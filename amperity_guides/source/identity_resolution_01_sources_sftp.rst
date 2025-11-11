.. https://docs.amperity.com/guides/

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
        Add SFTP

==================================================
Add SFTP
==================================================

.. source-sftp-about-start

Amperity can pull data a wide variety of file types, file formats, and file sizes from |source-name|, which is a common data source across all Amperity tenants.

.. source-sftp-about-end

.. source-sftp-prerequisites-start

.. note:: Review `Pull from any SFTP site  <../operator/source_sftp.html>`__ for more information about prerequisites, requirements, and optional configurations for |source-name|. All configuration prerequisites must be completed before stepping through this workflow.

.. source-sftp-prerequisites-start

Add a data source that pulls data from |source-name|. Configure Amperity to pull one or more files, and then for each file review the settings, define the schema, activate the courier, and then run a manual workflow. Review the data that is added to the domain table.

**To add a data source for any SFTP site**

.. source-sftp-add-data-source-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - On the **Identity resolution** page in **Quick start**, from the **Add data source** dropdown select **SFTP**.

       .. image:: ../../images/mockup-guided-idres-source-sftp.png
          :width: 500 px
          :alt: Add a data source.
          :align: left
          :class: no-scaled-link

       This opens the **Add courier** dialog box.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
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

          .. image:: ../../images/mockup-credentials-add-02-credential-status-sftp.png
             :width: 380 px
             :alt: Add 
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Add a name for the data source to the **Source name** field.

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-select-file-start
          :end-before: .. sources-steps-03-select-file-end

       .. image:: ../../images/mockup-sources-add-03-file-settings.png
          :width: 380 px
          :alt: Add 
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
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-pgp-start
          :end-before: .. sources-steps-03-pgp-end

       .. image:: ../../images/mockup-sources-add-03-pgp-credential.png
          :width: 500 px
          :alt: Add 
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-start
          :end-before: .. sources-steps-04-review-end

       .. image:: ../../images/mockup-sources-add-03-file-formatting.png
          :width: 380 px
          :alt: Add 
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
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-calendar-start
          :end-before: .. sources-steps-07-calendar-end

       .. image:: ../../images/mockup-courier-add-07-menu-load-data.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       Leave the load options unselected, and then click **Run**.

.. source-sftp-add-data-source-steps-end
