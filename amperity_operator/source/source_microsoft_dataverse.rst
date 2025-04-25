.. https://docs.amperity.com/operator/


.. |source-name| replace:: Microsoft Dataverse
.. |plugin-name| replace:: Microsoft Dataverse
.. |feed-name| replace:: DataverseTable
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **microsoft-dataverse**
.. |credential-details| replace:: Azure tenant ID, Azure client ID, and your Azure client secret
.. |what-pull| replace:: data tables


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
#. :ref:`Add courier <source-microsoft-dataverse-add-courier>`
#. :ref:`Get sample files <source-microsoft-dataverse-get-sample-files>`
#. :ref:`Add feeds <source-microsoft-dataverse-add-feeds>`
#. :ref:`Add load operations <source-microsoft-dataverse-add-load-operations>`
#. :ref:`Run courier <source-microsoft-dataverse-run-courier>`
#. :ref:`Add to courier group <source-microsoft-dataverse-add-to-courier-group>`

.. source-microsoft-dataverse-steps-to-pull-end


.. _source-microsoft-dataverse-get-details:

Get details
==================================================

.. source-microsoft-dataverse-get-details-start

Amperity can be configured to send |what-pull| from |source-name|.

#. The Azure tenant ID, Azure client ID, and your Azure client secret that has access to your Power Apps application.

#. The environment region, environment name, and logical table name for your Power Apps application. For example: "crm" (region), "acme" (name), and "abc123_acme" (logical table name).

.. source-microsoft-dataverse-get-details-end


.. _source-microsoft-dataverse-add-courier:

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

.. source-microsoft-dataverse-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the name of the courier. For example: "|source-name|".
#. From the **Credential** drop-down, select **Create a new credential**. This opens the **Create New Credential** page.
#. Enter a name for the credential, the |credential-details|. Click **Save**.
#. Under **Dataverse Settings**, add the catalog, database and logical table name.

   .. caution:: The database and table names **must** be a valid database and table in |source-name|. Catalog name is **optional**.
#. Configure the load operations to have the correct feed ID, operation, and file name. (The file name is the logical table name in |source-name|.)
#. Click **Save**.

.. source-microsoft-dataverse-add-courier-steps-end


.. _source-microsoft-dataverse-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-microsoft-dataverse-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. note:: A feed must be added for each table that is pulled from |source-name|.

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-microsoft-dataverse-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-microsoft-dataverse-add-courier-load-operations-example-start

For example:

::

   {
     "DATAVERSE-TABLE-FEED-ID": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "dataverse-table-name"
       }
     ]
   }

.. source-microsoft-dataverse-add-courier-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-microsoft-dataverse-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-microsoft-dataverse-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
