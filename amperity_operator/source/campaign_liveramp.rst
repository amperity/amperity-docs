.. https://docs.amperity.com/operator/


.. |destination-name| replace:: LiveRamp
.. |plugin-name| replace:: "LiveRamp"
.. |credential-type| replace:: "liveramp"
.. |required-credentials| replace:: "username", "hostname", and "passphrase"
.. |what-send| replace:: CSV files
.. |where-send| replace:: |destination-name|
.. |sftp-hostname| replace:: "sftp.liveramp.com"
.. |remote-folder| replace:: "/folder"
.. |sftp-port| replace:: "22"
.. |filter-the-list| replace:: "live"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to LiveRamp.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to LiveRamp.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for LiveRamp

==================================================
Configure campaigns for LiveRamp
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-liveramp-start
   :end-before: .. term-liveramp-end

.. campaign-liveramp-start

You can associate records in Amperity to an audience in |destination-name| by sending a combination of identifier data and query data. |destination-name| uses:

* Identifier data to match records to other `identifiers <https://docs.liveramp.com/connect/en/identity-and-identifier-terms-and-concepts.html#identifier-data>`__ |ext_link| in the LiveRamp Identity Graph.
* Segment data to group records into `segments <https://docs.liveramp.com/connect/en/segment-data.html>`__ |ext_link| based on certain attributes for downstream targeting, measurement, and personalization. 

|destination-name| requires an audience ID. This may be a client customer ID from another application, it may be the |destination-name| audience ID itself (from |destination-name| data that was imported to Amperity), or it may be the Amperity ID.

.. campaign-liveramp-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-configure-start
   :end-before: .. setting-common-file-configure-end


.. _campaign-liveramp-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-liveramp-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-get-details-passphrase-start
          :end-before: .. credential-get-details-passphrase-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
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

       **Header**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-header-start
             :end-before: .. setting-common-header-end

          .. important:: |destination-name| requires a header row to be present in CSV, TSV, and PSV files.

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


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **LiveRamp file prefer`file limitations <https://docs.liveramp.com/connect/en/liveramp-data-restrictions.html>`__ |ext_link|ences**

       Sending data to |destination-name| should follow recommendations for `uploading data <https://docs.liveramp.com/connect/en/uploading-data.html>`__ |ext_link|.

       Review |destination-name| `file limitations <https://docs.liveramp.com/connect/en/liveramp-data-restrictions.html>`__ |ext_link|.

       |destination-name| supports the following `file formats <https://docs.liveramp.com/connect/en/formatting-file-data.html>`__ |ext_link|:

       * CSV
       * PSV
       * TSV

       .. important:: Be sure to enable the **Include header row in output files** option for the Amperity destination.

       |destination-name| prefers `GPG encryption <https://docs.liveramp.com/connect/en/encrypting-files-for-uploading.html>`__ |ext_link| and GZip compression.

.. campaign-liveramp-get-details-table-end


.. _campaign-liveramp-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for LiveRamp**

.. campaign-liveramp-credentials-steps-start

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
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Hostname**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-hostname-start
             :end-before: .. credential-sftp-hostname-end

       **Passphrase**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-passphrase-start
             :end-before: .. credential-sftp-passphrase-end

       **Username**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-username-start
             :end-before: .. credential-sftp-username-end


.. campaign-liveramp-credentials-steps-end


.. _campaign-liveramp-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for LiveRamp**

.. campaign-liveramp-add-steps-start

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


       **Filename template**
          .. include:: ../../shared/terms.rst
             :start-after: .. term-filename-template-start
             :end-before: .. term-filename-template-end


       **Header**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-header-start
             :end-before: .. setting-common-header-end

          .. important:: |destination-name| requires a header row to be present in CSV, TSV, and PSV files.


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


       **Use Zip64?**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-use-zip64-start
             :end-before: .. setting-common-use-zip64-end


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


.. campaign-liveramp-add-steps-end
