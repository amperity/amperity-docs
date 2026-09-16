.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Attentive
.. |destination-api| replace:: SFTP
.. |plugin-name| replace:: "Attentive"
.. |credential-type| replace:: "attentive-mobile"
.. |required-credentials| replace:: "username", "hostname", and "passphrase"
.. |what-send| replace:: CSV files with email addresses **OR** phone numbers, but not both,
.. |where-send| replace:: |destination-name|
.. |sftp-hostname| replace:: "sftp.attentivemobile.com"
.. |remote-folder| replace:: "/folder"
.. |sftp-port| replace:: "22"
.. |filter-the-list| replace:: "att"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 24 hours

.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Attentive.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Attentive.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Attentive (email or phone)

====================================================
Configure campaigns for Attentive (email or phone)
====================================================

Use this topic to send a **campaign** to Attentive. To configure Attentive as a destination for sending **audiences**, see :doc:`Configure destinations for Attentive <destination_attentive_mobile>`.

.. include:: ../../amperity_operator/source/destination_attentive_mobile.rst
   :start-after: .. destination-attentive-segments-start
   :end-before: .. destination-attentive-segments-end

.. include:: ../../amperity_operator/source/destination_attentive_mobile.rst
   :start-after: .. destination-attentive-sftp-and-api-start
   :end-before: .. destination-attentive-sftp-and-api-end

.. note::

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end


.. _campaign-attentive-mobile-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-attentive-mobile-get-details-table-start

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

          Review the `subscriber segment upload <https://docs.attentivemobile.com/pages/developer-guides/sftp-solution/subscriber-segment-upload/#subscriber-segment-upload>`__ |ext_link| topic for specific requirements for how to format the CSV file.

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

.. campaign-attentive-mobile-get-details-table-end


.. _campaign-attentive-mobile-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Attentive**

.. campaign-attentive-mobile-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
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


.. campaign-attentive-mobile-credentials-steps-end


.. _campaign-attentive-mobile-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Attentive**

.. campaign-attentive-mobile-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
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
          :alt: Step two.
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
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

       .. important:: Be sure to use "Segments" in the destination title so that users of Amperity who sends segments to |destination-name| is able to identify this destination. Review the `subscriber segment upload <https://docs.attentivemobile.com/pages/developer-guides/sftp-solution/subscriber-segment-upload/#subscriber-segment-upload>`__ |ext_link| topic for specific requirements for how to format the CSV file. Do not include header rows in output.

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

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


       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. campaign-attentive-mobile-add-steps-end


.. _campaign-attentive-add-data-template-about:

About filename templates
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_attentive_mobile.rst
   :start-after: .. destination-attentive-add-data-template-intro-start
   :end-before: .. destination-attentive-add-data-template-intro-end

.. include:: ../../amperity_operator/source/destination_attentive_mobile.rst
   :start-after: .. destination-attentive-add-data-template-about-start
   :end-before: .. destination-attentive-add-data-template-about-end

.. include:: ../../amperity_operator/source/destination_attentive_mobile.rst
   :start-after: .. destination-attentive-add-data-template-important-start
   :end-before: .. destination-attentive-add-data-template-important-end



.. TODO: Add workflow resolutions from existing topics HERE.
