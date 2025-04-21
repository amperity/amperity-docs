.. https://docs.amperity.com/operator/


.. |source-name| replace:: Dynamic Yield
.. |plugin-name| replace:: Amazon S3
.. |feed-name| replace:: ProductCatalog
.. |filter-the-list| replace:: "ama"
.. |credential-type| replace:: **iam-credential**
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: product catalog data


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Dynamic Yield.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Dynamic Yield.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Dynamic Yield

==================================================
Pull from Dynamic Yield
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dynamic-yield-start
   :end-before: .. term-dynamic-yield-end

.. destination-dynamic-yield-s3-or-sftp-start

.. note:: This topic explains how to configure Amperity to pull data from a password-protected Amazon S3 bucket that is managed by |source-name|. You must configure |source-name| to pull data from an `Amazon S3 <https://support.dynamicyield.com/hc/en-us/articles/360038581394-Product-Feeds#product-feeds-0-0>`__ |ext_link| bucket that is managed from |source-name|.

.. destination-dynamic-yield-s3-or-sftp-end

.. source-dynamic-yield-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-dynamic-yield-get-details>`
#. :ref:`Configure cross-account roles <source-dynamic-yield-credentials-role-to-role>`
#. :ref:`Add courier <source-dynamic-yield-add-courier>`
#. :ref:`Get sample files <source-dynamic-yield-get-sample-files>`
#. :ref:`Add feeds <source-dynamic-yield-add-feeds>`
#. :ref:`Add load operations <source-dynamic-yield-add-load-operations>`
#. :ref:`Run courier <source-dynamic-yield-run-courier>`
#. :ref:`Add to courier group <source-dynamic-yield-add-to-courier-group>`

.. source-dynamic-yield-steps-to-pull-end


.. _source-dynamic-yield-get-details:

Get details
==================================================

.. source-dynamic-yield-get-details-start

Amperity can be configured to pull data from |source-name| using Amazon S3. This requires the following configuration details:

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
     - For :ref:`cross-account role assumption <source-dynamic-yield-credentials-role-to-role>` you will need the value for the **Target Role ARN**, which enables Amperity to access the customer-managed Amazon S3 bucket.

       .. note:: The values for the **Amperity Role ARN** and the **External ID** fields are provided automatically.

       .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-policy-example-intro-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-policy-example-intro-end

       .. include:: ../../shared/amazon-s3.rst
          :start-after: .. sources-amazon-s3-cross-account-roles-steps-policy-example-start
          :end-before: .. sources-amazon-s3-cross-account-roles-steps-policy-example-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - A list of objects (by filename and file type) in the S3 bucket to be sent to Amperity and a sample for each file to simplify feed creation.

       .. include:: ../../amperity_reference/source/format_csv.rst
          :start-after: .. format-csv-file-sizes-start
          :end-before: .. .. format-csv-file-sizes-end

.. source-dynamic-yield-get-details-end


.. _source-dynamic-yield-credentials-role-to-role:

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

.. source-dynamic-yield-credentials-role-to-role-steps-start

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

.. source-dynamic-yield-credentials-role-to-role-steps-end


.. _source-dynamic-yield-add-courier:

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

.. source-dynamic-yield-add-courier-entities-list-start

For example:

::

   [
     {
       "object/type": "file",
       "object/file-pattern": "'/path/to/productfeed.csv'",
       "object/land-as": {
         "file/header-rows": 1,
         "file/tag": "productfeed",
         "file/content-type": "text/csv"
       }
     }
   ]

.. source-dynamic-yield-add-courier-entities-list-end

**To add an Amazon S3 courier**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-s3-generic-start
   :end-before: .. sources-add-courier-s3-generic-end


.. _source-dynamic-yield-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-dynamic-yield-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-dynamic-yield-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-dynamic-yield-add-load-operations-example-start

For example:

::

   {
     "PRODUCT-CATALOG-FEED-ID": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "productcatalog"
       }
     ]
   }

.. source-dynamic-yield-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-dynamic-yield-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-dynamic-yield-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
