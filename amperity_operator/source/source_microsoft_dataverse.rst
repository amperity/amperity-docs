.. https://docs.amperity.com/operator/


.. |source-name| replace:: Microsoft Dataverse
.. |plugin-name| replace:: Microsoft Dataverse
.. |feed-name| replace:: DataverseTable
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **microsoft-dataverse**
.. |credential-details| replace:: Azure tenant ID, Azure client ID, and your Azure client secret
.. |what-pull| replace:: data tables
.. |filter-the-list| replace:: "data"

.. meta::
    :description lang=en:
        Configure Amperity to pull data from Microsoft Dataverse.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Microsoft Dataverse.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Microsoft Dataverse

==================================================
Pull from Microsoft Dataverse
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-dataverse-start
   :end-before: .. term-microsoft-dataverse-end

.. source-microsoft-dataverse-about-start

Use this connector to pull database tables from |source-name| to Amperity.

.. source-microsoft-dataverse-about-end

.. source-microsoft-dataverse-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-microsoft-dataverse-get-details>`
#. :ref:`Add data source and feed <source-microsoft-dataverse-add-data-source>`

.. source-microsoft-dataverse-steps-to-pull-end


.. _source-microsoft-dataverse-get-details:

Get details
==================================================

.. source-microsoft-dataverse-get-details-start

.. vale off

Amperity can be configured to send |what-pull| from |source-name|.

#. The Azure tenant ID, Azure client ID, and your Azure client secret that has access to your Power Apps application.

#. The environment region, environment name, and logical table name for your Power Apps application. For example: "crm" (region), "acme" (name), and "abc123_acme" (logical table name).

.. vale on

.. source-microsoft-dataverse-get-details-end


.. _source-microsoft-dataverse-add-data-source:

Add data source and feed
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-steps-00-intro-start
   :end-before: .. sources-steps-00-intro-end

**To add a data source for Microsoft Dataverse**

.. source-microsoft-dataverse-add-data-source-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-01-open-dialog-start
          :end-before: .. sources-steps-01-open-dialog-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-01-select-source-start
          :end-before: .. sources-steps-01-select-source-end


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


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **Power Apps Environment Region**

          |checkmark-required| **Required**

          The region in which your Power Apps data center is located. For example: "crm".

       **Power Apps Environment Name**

          |checkmark-required| **Required**

          The unique name for your Power Apps environment. For example: "acme".

       **Dataverse Table Logical Name**

          |checkmark-required| **Required**

          The logical name for the Dataverse table from which Amperity pulls data. For example: "abc123_customer".


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-options-start
          :end-before: .. sources-steps-05-feed-options-end


       **New feed**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-new-start
          :end-before: .. sources-steps-05-feed-new-end


       **Existing feed**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-existing-start
          :end-before: .. sources-steps-05-feed-existing-end


       **Pull data**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-types-start
          :end-before: .. sources-steps-05-load-types-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-type-upsert-start
          :end-before: .. sources-steps-05-load-type-upsert-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-type-truncate-start
          :end-before: .. sources-steps-05-load-type-truncate-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-types-note-start
          :end-before: .. sources-steps-05-load-types-note-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-06-feed-editor-start
          :end-before: .. sources-steps-06-feed-editor-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-courier-start
          :end-before: .. sources-steps-07-courier-end

       .. image:: ../../images/mockup-courier-add-07-menu-run.png
          :width: 380 px
          :alt: Add
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-calendar-start
          :end-before: .. sources-steps-07-calendar-end

       .. image:: ../../images/mockup-courier-add-07-menu-load-data.png
          :width: 380 px
          :alt: Add
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-run-start
          :end-before: .. sources-steps-07-run-end

.. source-microsoft-dataverse-add-data-source-steps-end
