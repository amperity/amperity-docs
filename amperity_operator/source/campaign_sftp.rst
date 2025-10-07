.. https://docs.amperity.com/operator/


.. |destination-name| replace:: SFTP
.. |plugin-name| replace:: "SFTP"
.. |credential-type| replace:: "passphrase" or "private-key"
.. |required-credentials| replace:: credential
.. |what-send| replace:: Apache Parquet, CSV, JSON, NDJSON, PSV, or TSV files
.. |where-send| replace:: any SFTP site
.. |sftp-hostname| replace:: "sftp.socktown.com"
.. |remote-folder| replace:: "/folder/name"
.. |sftp-port| replace:: "22"
.. |filter-the-list| replace:: "sftp"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to SFTP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to SFTP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for SFTP

==================================================
Configure campaigns for SFTP
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-sftp-about-start
   :end-before: .. setting-sftp-about-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-configure-start
   :end-before: .. setting-common-file-configure-end


.. _campaign-sftp-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-sftp-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-get-details-both-types-start
          :end-before: .. credential-get-details-both-types-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **File format**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-start
             :end-before: .. setting-common-file-format-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-file-format-custom-delimiter-start
             :end-before: .. setting-common-file-format-custom-delimiter-end

       **Remote folder**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-remote-folder-start
             :end-before: .. setting-common-remote-folder-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-remote-folder-forward-slash-start
             :end-before: .. setting-common-remote-folder-forward-slash-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-remote-folder-spaces-start
             :end-before: .. setting-common-remote-folder-spaces-end

       .. note::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-optional-settings-start
             :end-before: .. setting-common-optional-settings-end

.. campaign-sftp-get-details-table-end


.. _campaign-sftp-get-details-amperity:

Included SFTP site
--------------------------------------------------

.. campaign-sftp-get-details-amperity-start

Every Amperity tenant includes an SFTP site with a hostname of ``<tenant>.sftp.amperity.com``. For example, if your company name is **ACME**, then your tenant's SFTP hostname is ``acme.sftp.amperity.com``. The hostname is always all lowercase.

.. note:: The SFTP site is provisioned by an Amperity administrator *after* the initial tenant creation. As such, the SFTP site is not immediately available, but this is not a long process. When the SFTP site is ready, Amperity uses SnapPass to send you the connection details. If you wish to use RSA key-based authentication, please provide the public key to your Amperity administrator when requesting SFTP access.

Once this site is provisioned, you may configure the SFTP site as an SFTP source or an SFTP destination to support any desired workflow. External customer processes can be configured to connect to the site using SFTP, after which they can add data to or pick up data from the site to support any external workflow.

.. caution:: The SFTP server has a 30-day limit on data and after 30 days, data may be moved automatically to an archive location. This location is still accessible to Amperity in case it becomes necessary to reuse it.

.. important:: The hostname for the SFTP site is always ``<tenant-name>.sftp.amperity.com``. Some older tenants may still be using the legacy address ``sftp.amperity.com``, if so, please contact your Amperity administrator about migrating.

.. campaign-sftp-get-details-amperity-end


.. _campaign-sftp-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for SFTP**

.. campaign-sftp-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-multiple-start
          :end-before: .. credential-steps-select-type-multiple-end

       From the **Credential type** dropdown, select |credential-type|.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - The settings that are available for a credential are determined by the credential type and by the settings that are required by the SFTP site. The following credential settings are available for SFTP sites.

       Configure the settings that are required by the SFTP site to which Amperity connects, and then click **Save**.

       **Host public key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-host-public-key-start
             :end-before: .. credential-sftp-host-public-key-end

       **Hostname**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-hostname-start
             :end-before: .. credential-sftp-hostname-end

       **Passphrase**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-passphrase-start
             :end-before: .. credential-sftp-passphrase-end

       **Port**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-port-start
             :end-before: .. credential-sftp-port-end

       **Private key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-private-key-start
             :end-before: .. credential-sftp-private-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-private-key-required-start
             :end-before: .. credential-sftp-private-key-required-end

       **Username**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-username-start
             :end-before: .. credential-sftp-username-end


.. campaign-sftp-credentials-steps-end


.. _campaign-sftp-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for SFTP**

.. campaign-sftp-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-sftp.png
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
          :align: left
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
          :align: left
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
          :align: left
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


       **Line ending**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-line-ending-start
             :end-before: .. setting-common-line-ending-end


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


       **Remote folder**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-remote-folder-start
             :end-before: .. setting-common-remote-folder-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-remote-folder-forward-slash-start
             :end-before: .. setting-common-remote-folder-forward-slash-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-remote-folder-spaces-start
             :end-before: .. setting-common-remote-folder-spaces-end


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
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end


.. campaign-sftp-add-steps-end


.. _campaign-sftp-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. campaign-sftp-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: left
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

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-sftp-workflow-actions-invalid-credentials`
       * :ref:`destination-sftp-workflow-actions-sftp-unavailable`


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

.. campaign-sftp-workflow-actions-end


.. _campaign-sftp-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _campaign-sftp-workflow-actions-sftp-unavailable:

SFTP site unavailable
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-sftp-generic-unavailable-start
   :end-before: .. workflow-actions-sftp-generic-unavailable-end
