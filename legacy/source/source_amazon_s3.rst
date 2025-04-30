.. https://docs.amperity.com/legacy/


.. |source-name| replace:: Amazon S3
.. |plugin-name| replace:: Amazon S3
.. |feed-name| replace:: CustomerRecords
.. |credential-type| replace:: **iam-credential**
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: files in any supported format
.. |filter-the-list| replace:: "ama"


==================================================
Pull from Amazon S3 (Legacy)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-s3-start
   :end-before: .. term-amazon-s3-end

.. source-amazon-s3-legacy-about-start

Amperity can pull data from Amazon S3. A common scenario: a file is output from a customer data source with a consistent datestamp pattern appended to a static file name, added to an Amazon S3 bucket, and then updated on a regular basis. Amazon S3 can be a source for any number of file types and formats. A courier can be configured to ingest multiple file types and formats as a fileset.

.. source-amazon-s3-legacy-about-end

.. source-amazon-s3-legacy-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-amazon-s3-legacy-get-details>`
#. :ref:`Configure cross-account roles <source-amazon-s3-legacy-credentials-role-to-role>`
#. :ref:`Add courier <source-amazon-s3-legacy-add-courier>`
#. :ref:`Get sample files <source-amazon-s3-legacy-get-sample-files>`
#. :ref:`Add feeds <source-amazon-s3-legacy-add-feeds>`
#. :ref:`Add load operations <source-amazon-s3-legacy-add-load-operations>`
#. :ref:`Run courier <source-amazon-s3-legacy-run-courier>`
#. :ref:`Add to courier group <source-amazon-s3-legacy-add-to-courier-group>`

.. source-amazon-s3-legacy-steps-to-pull-end


.. _source-amazon-s3-legacy-get-details:

Get details
==================================================

.. source-amazon-s3-legacy-get-details-start

The |source-name| destination requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The name of the S3 bucket from which data will be pulled to Amperity.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - For :ref:`cross-account role assumption <source-amazon-s3-legacy-credentials-role-to-role>` you will need the value for the **Target Role ARN**, which enables Amperity to access the customer-managed Amazon S3 bucket.

       .. note:: The values for the **Amperity Role ARN** and the **External ID** fields are provided automatically.

       .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-policy-example-intro-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-policy-example-intro-end

       .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-policy-example-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-policy-example-end

.. source-amazon-s3-legacy-get-details-end


.. _source-amazon-s3-legacy-credentials-role-to-role:

Configure cross-account roles
==================================================

.. include:: ../../shared/amazon-s3.rst
   :start-after: .. sources-amazon-s3-cross-account-roles-overview-start
   :end-before: .. sources-amazon-s3-cross-account-roles-overview-end

.. include:: ../../shared/amazon-s3.rst
   :start-after: .. sources-amazon-s3-cross-account-roles-context-start
   :end-before: .. sources-amazon-s3-cross-account-roles-context-end

.. note::

   .. include:: ../../shared/amazon-s3.rst
      :start-after: .. sources-amazon-s3-cross-account-roles-setup-start
      :end-before: .. sources-amazon-s3-cross-account-roles-setup-end

.. include:: ../../shared/amazon-s3.rst
   :start-after: .. sources-amazon-s3-aws-access-point-start
   :end-before: .. sources-amazon-s3-aws-access-point-end

**To configure an S3 bucket for cross-account role assumption**

.. include:: ../../shared/amazon-s3.rst
   :start-after: .. sources-amazon-s3-cross-account-roles-steps-intro-done-by-admins-start
   :end-before: .. sources-amazon-s3-cross-account-roles-steps-intro-done-by-admins-end

.. source-amazon-s3-legacy-credentials-role-to-role-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-start
          :end-before: .. credentials-sources-configure-end

       .. image:: ../../images/mockup-sources-add-01-select-source.png
          :width: 380 px
          :alt: Add credentials for a data source.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-options-start
          :end-before: .. credentials-sources-configure-options-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-add-source-intro-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-add-source-intro-end

       .. image:: ../../images/mockup-credentials-add-01-settings-amazon-s3-role-to-role.png
          :width: 360 px
          :alt: Select the iam-role-to-role credential type.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-settings-intro-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-settings-intro-end

       .. image:: ../../images/mockup-credentials-add-01-settings-amazon-s3-role-to-role-all.png
          :width: 360 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-settings-details-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-settings-details-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-policy-example-intro-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-policy-example-intro-end

       .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-policy-example-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-policy-example-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-save-credentials-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-save-credentials-end

.. source-amazon-s3-legacy-credentials-role-to-role-steps-end


.. _source-amazon-s3-legacy-add-courier:

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
   :start-after: .. sources-add-courier-entities-list-intro-s3-generic-start
   :end-before: .. sources-add-courier-entities-list-intro-s3-generic-end

.. source-amazon-s3-legacy-add-courier-entities-list-start

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

.. source-amazon-s3-legacy-add-courier-entities-list-end

**To add a courier for Amazon S3**

.. source-amazon-s3-legacy-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.
#. Enter the name of the courier. For example: "|source-name|".
#. Credentials allow Amperity to connect to |source-name|. Give the courier a name, and then select a credential from the **Credential** dropdown.

#. Under **Amazon S3 Settings**, add the name of the Amazon S3 bucket and prefix.
#. Under **Amazon S3 Settings** configure the list of files to pull to Amperity. Configure the **Entities List** for each file to be loaded to Amperity.
#. Under **Amazon S3 Settings** set the load operations to a string that is obviously incorrect, such as **df-xxxxxx**. (You may also set the load operation to empty: "{}".)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to "{}" the validation test for the courier configuration settings will fail.
#. Click **Save**.

.. source-amazon-s3-legacy-add-courier-steps-end


.. _source-amazon-s3-legacy-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-amazon-s3-legacy-add-feeds:

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


.. _source-amazon-s3-legacy-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-amazon-s3-legacy-add-load-operations-example-start

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

.. source-amazon-s3-legacy-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-amazon-s3-legacy-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-amazon-s3-legacy-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
