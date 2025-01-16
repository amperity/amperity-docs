.. https://docs.amperity.com/datagrid/


.. |source-name| replace:: Amperity SFTP
.. |plugin-name| replace:: SFTP
.. |feed-name| replace:: CustomerRecords
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **passphrase**
.. |sftp-hostname| replace:: **[tenant-name].sftp.amperity.com**
.. |what-pull| replace:: files in any supported format


.. meta::
    :description lang=en:
        Configure Amperity to pull data to included SFTP storage.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data to included SFTP storage.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull to Amperity SFTP

==================================================
Pull to Amperity SFTP
==================================================

.. about-tenant-sftp-start

Every Amperity tenant includes an SFTP site with a hostname of ``<tenant>.sftp.amperity.com``. For example, if your company name is **ACME**, then your tenant's SFTP hostname is ``acme.sftp.amperity.com``. (The hostname is always all lowercase.)

The SFTP site is provisioned by an Amperity administrator after the initial tenant creation. As such, the SFTP site is not immediately available, but this is not a long process. When the SFTP site is ready, Amperity will use SnapPass to send you the connection details. If you wish to use RSA key-based authentication, please provide the public key to your Amperity administrator when requesting SFTP access.

.. about-tenant-sftp-end

.. about-tenant-sftp-provisioned-start

Once provisioned, you may configure the SFTP site to support any desired SFTP workflow. External customer processes can be configured to connect to the site using SFTP, after which they can add data to or pick up data from the site to support any upstream or downstream workflow.

.. about-tenant-sftp-provisioned-end

.. about-tenant-sftp-provisioned-start

.. note:: The SFTP server has a 30-day limit on data and after 30 days, data will be removed.

   The hostname for the SFTP site is always |sftp-hostname|. Some older tenants may still be using the legacy address ``sftp.amperity.com``, if so, please contact your Amperity administrator about migrating.

.. about-tenant-sftp-note-end


.. _source-sftp-amperity-list:

Data sources
==================================================

.. source-sftp-amperity-list-start

Any data source that can send data to an SFTP site can be configured to send data to the Amperity SFTP site. File paths must begin with the tenant name and must be lowercase. For example, if the tenant name is **ACME** then all file paths must be prefixed with ``/acme/``.

.. source-sftp-amperity-list-end


.. _source-sftp-amperity-get-details:

Get details
==================================================

.. source-sftp-amperity-get-details-start

An Amperity SFTP site requires the following configuration details:

#. The username.
#. The passphrase.
#. The host public key.
#. The hostname. This is always ``[tenant].sftp.amperity.com``. For example, if your tenant name is ACME the hostname is ``acme.sftp.amperity.com``.
#. A list of objects (by filename and file type, e.g. "accounts.csv", "customers.ndjson", "email-list.tsv", and so on) in the SFTP location to be sent to Amperity.
#. A sample for each file to simplify feed creation.

.. source-sftp-amperity-get-details-end

.. source-sftp-amperity-get-details-account-info-start

.. hint:: Ask your Amperity representative for the username, passphrase, and public key or ask your Amperity representative to configure a courier that uses the Amperity SFTP site on your behalf, after which you can copy the settings and add additional couriers for data sources as required.

.. source-sftp-amperity-get-details-account-info-end


.. _source-sftp-amperity-filedrop-requirements:

Filedrop recommendations
--------------------------------------------------

.. include:: ../../shared/file-formats.rst
   :start-after: .. formats-filedrop-common-start
   :end-before: .. formats-filedrop-common-end


.. _source-sftp-amperity-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. tip::

   .. include:: ../../amperity_reference/source/couriers.rst
      :start-after: .. couriers-run-without-load-operations-start
      :end-before: .. couriers-run-without-load-operations-end

**Example entities list**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-entities-list-intro-sftp-only-start
   :end-before: .. sources-add-courier-entities-list-intro-sftp-only-end

.. source-sftp-amperity-add-courier-entities-list-start

For example:

::

   [
     {
       "object/type": "file",
       "object/file-pattern": "'/path/to/CustomerRecords.csv'",
       "object/land-as": {
         "file/header-rows": 1,
         "file/tag": "customer-records-2019",
         "file/content-type": "text/csv"
       }
     },
     {
       "object/type": "file",
       "object/file-pattern": "'/path/to/TransactionRecords.csv'",
       "object/land-as": {
         "file/header-rows": 1,
         "file/tag": "transaction-records-2019",
         "file/content-type": "text/csv"
       }
     }
   ]

.. source-sftp-amperity-add-courier-entities-list-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-entities-list-note-sftp-only-start
   :end-before: .. sources-add-courier-entities-list-note-sftp-only-end

**To add a courier**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-sftp-only-start
   :end-before: .. sources-add-courier-sftp-only-end


.. _source-sftp-amperity-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-sftp-amperity-add-feeds:

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


.. _source-sftp-amperity-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-sftp-amperity-add-load-operations-example-start

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

.. source-sftp-amperity-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-sftp-amperity-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-sftp-amperity-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end


.. _source-sftp-amperity-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. source-sftp-amperity-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-sftp-unavailable.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |source-name|, including:

       * :ref:`source-sftp-amperity-workflow-actions-bad-archive`
       * :ref:`source-sftp-amperity-workflow-actions-invalid-credentials`
       * :ref:`source-sftp-amperity-workflow-actions-missing-file`
       * :ref:`source-sftp-amperity-workflow-actions-pgp-error`
       * :ref:`source-sftp-amperity-workflow-actions-sftp-unavailable`
       * :ref:`source-sftp-amperity-workflow-actions-unable-to-decompress-archive`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-sftp-unavailable-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. source-sftp-amperity-workflow-actions-end


.. _source-sftp-amperity-workflow-actions-bad-archive:

Bad archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-bad-archive-start
   :end-before: .. workflow-actions-files-generic-bad-archive-end


.. _source-sftp-amperity-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-source-start
   :end-before: .. workflow-actions-generic-invalid-credentials-source-end


.. _source-sftp-amperity-workflow-actions-missing-file:

Missing file
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-missing-file-start
   :end-before: .. workflow-actions-files-generic-missing-file-end


.. _source-sftp-amperity-workflow-actions-pgp-error:

PGP error
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-pgp-error-start
   :end-before: .. workflow-actions-generic-pgp-error-end


.. _source-sftp-amperity-workflow-actions-sftp-unavailable:

SFTP site unavailable
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-sftp-generic-unavailable-start
   :end-before: .. workflow-actions-sftp-generic-unavailable-end


.. _source-sftp-amperity-workflow-actions-unable-to-decompress-archive:

Unable to decompress archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-unable-to-decompress-file-start
   :end-before: .. workflow-actions-files-unable-to-decompress-file-end
