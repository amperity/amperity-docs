.. https://docs.amperity.com/operator/


.. |source-name| replace:: Salesforce Marketing Cloud
.. |plugin-name| replace:: Salesforce Marketing Cloud
.. |feed-name| replace:: EmailCampaign
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **passphrase**
.. |sftp-hostname| replace:: **sftp.[instance].salesforce.com**
.. |what-pull| replace:: email campaigns data


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Salesforce Marketing Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Salesforce Marketing Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Salesforce Marketing Cloud

==================================================
Pull from Salesforce Marketing Cloud
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-marketing-cloud-start
   :end-before: .. term-salesforce-marketing-cloud-end

.. source-salesforce-marketing-cloud-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-salesforce-marketing-cloud-get-details>`
#. :ref:`Add courier <source-salesforce-marketing-cloud-add-courier>`
#. :ref:`Get sample files <source-salesforce-marketing-cloud-get-sample-files>`
#. :ref:`Add feeds <source-salesforce-marketing-cloud-add-feeds>`
#. :ref:`Add load operations <source-salesforce-marketing-cloud-add-load-operations>`
#. :ref:`Run courier <source-salesforce-marketing-cloud-run-courier>`
#. :ref:`Add to courier group <source-salesforce-marketing-cloud-add-to-courier-group>`

.. source-salesforce-marketing-cloud-steps-to-pull-end


.. _source-salesforce-marketing-cloud-get-details:

Get details
==================================================

.. source-salesforce-marketing-cloud-get-details-start

|source-name| requires the following configuration details:

#. The username.
#. The passphrase.
#. The host public key (if encryption is configured).
#. The hostname.
#. A list of objects (by filename and file type, e.g. "accounts.csv", "customers.csv", "email-list.csv", and so on) in the |source-name| SFTP location to be sent to Amperity. This location is also referred to as the "Export" folder from the perspective of |source-name|.
#. A sample for each file to simplify feed creation.
#. Review the `Marketing Cloud SFTP Guide <https://help.salesforce.com/articleView?id=mc_es_enhanced_ftp_guide.htm>`__ |ext_link| to answer questions about configuring and managing |source-name|.
#. The name of the directory within the |source-name| SFTP server from which data should is pulled. Use the **Import Location** field to define a non-default directory.

.. source-salesforce-marketing-cloud-get-details-end


.. _source-salesforce-marketing-cloud-subscriber-key:

Subscriber key
--------------------------------------------------

.. source-salesforce-marketing-cloud-subscriber-key-start

The subscriber key is an identifier in |source-name|. When a subscriber key is provided to Amperity for a workflow that will send data back to |source-name|, you should configure this workflow to carry the subscriber key through to the customer 360 database so that it may be included in the query that defines the results to be sent.

Use a customer key semantic tag for the subscriber key field when configuring the feed, and then ensure this field is available to the **Customer 360**, **Queries**, and/or **Segments** pages. Map this field to the |source-name| **subscriber_key** using a data template.
 
.. source-salesforce-marketing-cloud-subscriber-key-end


.. _source-salesforce-marketing-cloud-add-courier:

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

.. source-salesforce-marketing-cloud-add-courier-entities-list-start

For example:

::

   [
     {
       "object/type": "file",
       "object/file-pattern": "'/path/to/customer-record.csv'",
       "object/land-as": {
         "file/header-rows": 1,
         "file/tag": "customer-record-files",
         "file/content-type": "text/csv"
       }
     }
   ]

.. source-salesforce-marketing-cloud-add-courier-entities-list-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-entities-list-note-sftp-only-start
   :end-before: .. sources-add-courier-entities-list-note-sftp-only-end

**To add a courier**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-sftp-only-start
   :end-before: .. sources-add-courier-sftp-only-end


.. _source-salesforce-marketing-cloud-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-salesforce-marketing-cloud-add-feeds:

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


.. _source-salesforce-marketing-cloud-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-salesforce-marketing-cloud-add-load-operations-example-start

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

.. source-salesforce-marketing-cloud-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-salesforce-marketing-cloud-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-salesforce-marketing-cloud-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end


.. _source-salesforce-marketing-cloud-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. source-salesforce-marketing-cloud-workflow-actions-start

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

       * :ref:`source-salesforce-marketing-cloud-workflow-actions-bad-archive`
       * :ref:`source-salesforce-marketing-cloud-workflow-actions-invalid-credentials`
       * :ref:`source-salesforce-marketing-cloud-workflow-actions-missing-file`
       * :ref:`source-salesforce-marketing-cloud-workflow-actions-pgp-error`
       * :ref:`source-salesforce-marketing-cloud-workflow-actions-sftp-unavailable`
       * :ref:`source-salesforce-marketing-cloud-workflow-actions-unable-to-decompress-archive`

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

.. source-salesforce-marketing-cloud-workflow-actions-end


.. _source-salesforce-marketing-cloud-workflow-actions-bad-archive:

Bad archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-bad-archive-start
   :end-before: .. workflow-actions-files-generic-bad-archive-end


.. _source-salesforce-marketing-cloud-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-source-start
   :end-before: .. workflow-actions-generic-invalid-credentials-source-end


.. _source-salesforce-marketing-cloud-workflow-actions-missing-file:

Missing file
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-generic-missing-file-start
   :end-before: .. workflow-actions-files-generic-missing-file-end


.. _source-salesforce-marketing-cloud-workflow-actions-pgp-error:

PGP error
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-pgp-error-start
   :end-before: .. workflow-actions-generic-pgp-error-end


.. _source-salesforce-marketing-cloud-workflow-actions-sftp-unavailable:

SFTP site unavailable
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-sftp-generic-unavailable-start
   :end-before: .. workflow-actions-sftp-generic-unavailable-end


.. _source-salesforce-marketing-cloud-workflow-actions-unable-to-decompress-archive:

Unable to decompress archive
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-files-unable-to-decompress-file-start
   :end-before: .. workflow-actions-files-unable-to-decompress-file-end
