.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Amazon S3
.. |plugin-name| replace:: "Amazon S3"
.. |credential-type| replace:: "iam-credential" or "iam-role-to-role"
.. |required-credentials| replace:: "iam-credential" or "iam-role-to-role"
.. |what-send| replace:: Apache Parquet (recommended), CSV, JSON, NDJSON, PSV, or TSV files
.. |where-send| replace:: any Amazon S3 bucket
.. |filter-the-list| replace:: "amaz"


.. meta::
    :description lang=en:
        Configure Amperity to campaigns to an Amazon S3 bucket.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to campaigns to an Amazon S3 bucket.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Amazon S3

==================================================
Configure campaigns for Amazon S3
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-s3-about-start
   :end-before: .. setting-amazon-s3-about-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-configure-start
   :end-before: .. setting-common-file-configure-end


.. _campaign-amazon-s3-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-amazon-s3-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Amazon S3 bucket details**

       You will need to know the following details about the |destination-name| bucket to which Amperity will send data.

       #. The name of the |destination-name| bucket. An S3 prefix is sometimes required.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Credential types and settings**

       Amperity supports the following credential types for |destination-name|:

       #. :ref:`IAM role-to-role (recommended) <destination-amazon-s3-credentials-role-to-role>`

          For cross-account role assumption you will need the value for the IAM role ARN that allows Amperity to add data to an Amazon S3 bucket that is managed by your brand.

          The values for the **Amperity Role ARN** and the **External ID** fields are provided by Amperity.

       #. :ref:`IAM credentials <destination-amazon-s3-credentials-iam>`


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **File format**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-start
             :end-before: .. setting-common-file-format-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-custom-delimiter-start
             :end-before: .. setting-common-file-format-custom-delimiter-end

       .. note::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-optional-settings-start
             :end-before: .. setting-common-optional-settings-end

.. campaign-amazon-s3-get-details-table-end


.. _campaign-amazon-s3-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

Amperity supports the following credential types for |destination-name|:

#. :ref:`IAM role-to-role (recommended) <destination-amazon-s3-credentials-role-to-role>`
#. :ref:`IAM credentials <destination-amazon-s3-credentials-iam>`

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end


.. _campaign-amazon-s3-credentials-role-to-role:

IAM role-to-role
--------------------------------------------------

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-amazon-s3-cross-account-roles-overview-start
   :end-before: .. credential-amazon-s3-cross-account-roles-overview-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-amazon-s3-cross-account-roles-context-start
   :end-before: .. credential-amazon-s3-cross-account-roles-context-end

.. note:: 

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-cross-account-roles-setup-start
      :end-before: .. credential-amazon-s3-cross-account-roles-setup-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-amazon-s3-aws-access-point-start
   :end-before: .. credential-amazon-s3-aws-access-point-end

**To configure an S3 bucket for cross-account role assumption**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-amazon-s3-cross-account-roles-steps-intro-done-by-admins-start
   :end-before: .. credential-amazon-s3-cross-account-roles-steps-intro-done-by-admins-end

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-multiple-start
          :end-before: .. credential-steps-select-type-multiple-end

       From the **Credential type** dropdown, select **iam-role-to-role**.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - The settings that are available for a credential are determined by the credential type. For the **iam-role-to-role** credential type, configure the following settings, and then click **Save**.

       .. image:: ../../images/mockup-credentials-add-01-settings-amazon-s3-role-to-role-all.png
          :width: 360 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-amazon-s3-cross-account-roles-steps-settings-required-start
          :end-before: .. credential-amazon-s3-cross-account-roles-steps-settings-required-end

       **Amazon S3 bucket name**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-bucket-name-start
             :end-before: .. credential-amazon-s3-bucket-name-end

          .. note:: 

             .. include:: ../../shared/credentials_settings.rst
                :start-after: .. credential-amazon-s3-trust-policy-start
                :end-before: .. credential-amazon-s3-trust-policy-end

       **Target role ARN**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-target-role-arn-start
             :end-before: .. credential-amazon-s3-target-role-arn-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-cross-account-roles-steps-settings-provided-start
             :end-before: .. credential-amazon-s3-cross-account-roles-steps-settings-provided-end

       **Amperity role ARN**
          |setting-provided-by-amperity| **Provided by Amperity**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-amperity-role-arn-start
             :end-before: .. credential-amazon-s3-amperity-role-arn-end

       **External ID**
          |setting-provided-by-amperity| **Provided by Amperity**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-external-id-start
             :end-before: .. credential-amazon-s3-external-id-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-amazon-s3-cross-account-roles-steps-policy-example-intro-start
          :end-before: .. credential-amazon-s3-cross-account-roles-steps-policy-example-intro-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-amazon-s3-cross-account-roles-steps-policy-example-start
          :end-before: .. credential-amazon-s3-cross-account-roles-steps-policy-example-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-amazon-s3-cross-account-roles-steps-save-credentials-start
          :end-before: .. credential-amazon-s3-cross-account-roles-steps-save-credentials-end


.. campaign-amazon-s3-credentials-role-to-role-steps-end


.. _campaign-amazon-s3-credentials-iam:

IAM credentials
--------------------------------------------------

.. campaign-amazon-s3-credentials-iam-start

IAM credentials require an access key, which is in two parts:

#. An access key ID
#. A secret access key

Both parts are required to authenticate requests to Amazon AWS resources.

.. campaign-amazon-s3-credentials-iam-end

**To configure an S3 bucket for IAM credentials**

.. campaign-amazon-s3-credentials-iam-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-multiple-start
          :end-before: .. credential-steps-select-type-multiple-end

       From the **Credential type** dropdown, select **iam-credential**.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - The settings that are available for a credential are determined by the credential type. For the **iam-credential** credential type, configure the following settings, and then click **Save**.

       .. image:: ../../images/mockup-credentials-add-01-settings-amazon-s3-iam-all.png
          :width: 360 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       **IAM access key**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-iam-access-key-start
             :end-before: .. credential-amazon-s3-iam-access-key-end

       **IAM secret key**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-iam-secret-key-start
             :end-before: .. credential-amazon-s3-iam-secret-key-end

       **IAM role ARN**
          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-iam-role-arn-start
             :end-before: .. credential-amazon-s3-iam-role-arn-end

       **Amazon S3 bucket name**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-s3-bucket-name-start
             :end-before: .. credential-amazon-s3-bucket-name-end


.. campaign-amazon-s3-credentials-iam-steps-end


.. _campaign-amazon-s3-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Amazon S3**

.. campaign-amazon-s3-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-s3.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-select-credential-start
          :end-before: .. campaigns-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-test-connection-start
             :end-before: .. campaigns-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Compression**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-compression-start
             :end-before: .. setting-common-compression-end


       **Escape character**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-escape-character-start
             :end-before: .. setting-common-escape-character-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-escape-character-unspecified-start
             :end-before: .. setting-common-escape-character-unspecified-end


       **File format**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-start
             :end-before: .. setting-common-file-format-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-custom-delimiter-start
             :end-before: .. setting-common-file-format-custom-delimiter-end

          **Apache Parquet files only**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-apache-parquet-start
             :end-before: .. setting-common-file-format-apache-parquet-end


       **Filename template**
          .. include:: ../../shared/terms.rst
             :start-after: .. term-filename-template-start
             :end-before: .. term-filename-template-end


       **Header**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-header-start
             :end-before: .. setting-common-header-end


       **PGP public key**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-pgp-public-key-start
             :end-before: .. setting-common-pgp-public-key-end


       **Quote mode**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-quote-mode-start
             :end-before: .. setting-common-quote-mode-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-quote-mode-none-start
             :end-before: .. setting-common-quote-mode-none-end

       **S3 prefix**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-s3-prefix-start
             :end-before: .. setting-amazon-s3-prefix-end

       **Success file**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-success-file-start
             :end-before: .. setting-common-success-file-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-success-file-downstream-start
             :end-before: .. setting-common-success-file-downstream-end


       **Split outputs**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-split-outputs-start
             :end-before: .. setting-common-split-outputs-end


       **Use Zip64?**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-use-zip64-start
             :end-before: .. setting-common-use-zip64-end


       **Row Number**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-row-number-start
             :end-before: .. setting-common-row-number-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-row-number-column-name-start
             :end-before: .. setting-common-row-number-column-name-end

       **Campaign file settings**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end


.. campaign-amazon-s3-add-steps-end


.. _campaign-amazon-s3-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. campaign-amazon-s3-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

       .. image:: ../../images/mockup-destinations-tab-workflow-error.png
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
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-two-start
          :end-before: .. workflow-actions-common-table-section-two-end

       .. image:: ../../images/mockups-workflow-failed.png
          :width: 500 px
          :alt: The Workflow page, showing a workflow with errors.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-a-start
          :end-before: .. workflow-actions-common-table-section-three-a-end

       .. image:: ../../images/workflow-actions-s3-generic-invalid-bucket-name.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-amazon-s3-workflow-actions-invalid-bucket-name`
       * :ref:`destination-amazon-s3-workflow-actions-invalid-credentials`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-s3-generic-invalid-bucket-name-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. campaign-amazon-s3-workflow-actions-end


.. _campaign-amazon-s3-workflow-actions-invalid-bucket-name:

Invalid bucket name
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-s3-generic-incorrect-bucket-name-destination-start
   :end-before: .. workflow-actions-s3-generic-incorrect-bucket-name-destination-end


.. _campaign-amazon-s3-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end
