.. https://docs.amperity.com/datagrid/


.. |destination-name| replace:: Throtle
.. |plugin-name| replace:: Amazon S3
.. |what-send| replace:: customer profile data
.. |email-plus-send| replace:: additional attributes
.. |filter-the-list| replace:: "thr"
.. |s3-bucket-name| replace:: "throtle-import"
.. |s3-prefix| replace:: "upload"
.. |file-format| replace:: CSV, TSV, or PSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by |destination-name| were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_throtle|
.. |channel-link| replace:: send campaign results


.. meta::
    :description lang=en:
        Configure Amperity to send data to Throtle.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Throtle.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Throtle

==================================================
Send data to Throtle
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-throtle-start
   :end-before: .. term-throtle-end

.. destination-throtle-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-throtle-get-details>`
#. :ref:`Configure cross-account roles <destination-throtle-credentials-role-to-role>`
#. :ref:`Add destination <destination-throtle-add-destination>`
#. :ref:`Add data template <destination-throtle-add-data-template>`

.. destination-throtle-steps-to-send-end


.. _destination-throtle-get-details:

Get details
==================================================

.. destination-throtle-get-details-start

Amperity can be configured to send data to a customer-managed Amazon S3 bucket :ref:`using cross-account roles <destination-throtle-credentials-role-to-role>`, and then connect |destination-name| to that Amazon S3 bucket.

.. destination-throtle-get-details-end


.. _destination-throtle-credentials-role-to-role:

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

.. destination-throtle-credentials-role-to-role-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-destinations-configure-start
          :end-before: .. credentials-destinations-configure-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-destinations-configure-options-start
          :end-before: .. credentials-destinations-configure-options-end


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

.. destination-throtle-credentials-role-to-role-steps-end


.. _destination-throtle-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

.. destination-throtle-add-destination-important-start

.. important:: You must use |s3-prefix| for the prefix value. The name of the |plugin-name| bucket is provided to you by |destination-name|.

.. destination-throtle-add-destination-important-end

**To add a destination**

.. destination-throtle-add-destination-steps-start

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

       .. important:: Use the :doc:`Amazon S3 <destination_amazon_s3>` destination that is built into Amperity to send data to a customer-managed Amazon S3 bucket, from which |destination-name| is configured to pull data.

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

       * The Amazon Resource Name (ARN) for a role with cross-account access.
       * The name of the |plugin-name| bucket.

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
          :alt: Settings for Optimizely.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-amazon-s3-start
          :end-before: .. destinations-destination-settings-amazon-s3-end


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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-enable-start
          :end-before: .. destinations-business-users-enable-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-allow-start
          :end-before: .. destinations-business-users-allow-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-throtle-add-destination-steps-end


.. _destination-throtle-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-throtle-add-data-template-steps-start

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

.. destination-throtle-add-data-template-steps-end
