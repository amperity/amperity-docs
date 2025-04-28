.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Attentive
.. |destination-api| replace:: SFTP
.. |plugin-name| replace:: "Attentive"
.. |credential-type| replace:: "attentive-mobile"
.. |required-credentials| replace:: "username", "hostname", and "passphrase"
.. |what-send| replace:: CSV files
.. |where-send| replace:: |destination-name|
.. |sftp-hostname| replace:: "ftp5.attentivemobile.com"
.. |remote-folder| replace:: "/folder"
.. |sftp-port| replace:: "22"
.. |filter-the-list| replace:: "att"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 24 hours

.. meta::
    :description lang=en:
        Configure Amperity to send email and phone lists to Attentive.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send email and phone lists to Attentive.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send email and phone lists to Attentive

==================================================
Send email and phone lists to Attentive
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_attentive_mobile.html>`__ |ext_link|.

.. destination-attentive-segments-start

Amperity uses the `subscriber segment upload <https://docs.attentivemobile.com/pages/developer-guides/sftp-solution/subscriber-segment-upload/#subscriber-segment-upload>`__ |ext_link| process to manage audience segments. This process does not use an endpoint and is not subject to `Attentive API rate limits <https://docs.attentive.com/pages/api-rate-limits/>`__ |ext_link|. Updates appear on the **Segments** page within your audience in |destination-name|.

.. destination-attentive-segments-end

.. destination-attentive-sftp-and-api-start

.. admonition:: Why are there two ways to send data to Attentive?

   Amperity uses the `Subscriptions <https://docs.attentive.com/openapi/reference/tag/Subscribers/>`__ |ext_link| and `Custom Attributes <https://docs.attentivemobile.com/openapi/reference/tag/Custom-Attributes/>`__ |ext_link| endpoints to send custom profile attributes to |destination-name|. Use these attributes to apply customizable data or characteristics to each of your subscribers, and then use that information to build segments for use with campaigns and journeys.

.. destination-attentive-sftp-and-api-end

.. note::

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end


.. _destination-attentive-mobile-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-attentive-mobile-get-details-table-start

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
          :start-after: .. credential-get-details-passphrase-start
          :end-before: .. credential-get-details-passphrase-end

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

.. destination-attentive-mobile-get-details-table-end


.. _destination-attentive-mobile-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Attentive**

.. destination-attentive-mobile-credentials-steps-start

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
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
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


.. destination-attentive-mobile-credentials-steps-end


.. _destination-attentive-mobile-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Attentive**

.. destination-attentive-mobile-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-sftp.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

       .. important:: Be sure to use "Segments" in the destination title so that users of Amperity who will send segments to |destination-name| will be able to identify this destination. Review the `subscriber segment upload <https://docs.attentivemobile.com/pages/developer-guides/sftp-solution/subscriber-segment-upload/#subscriber-segment-upload>`__ |ext_link| topic for specific requirements for how to format the CSV file. Do not include header rows in output.

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
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

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

          Review the `subscriber segment upload <https://docs.attentivemobile.com/pages/developer-guides/sftp-solution/subscriber-segment-upload/#subscriber-segment-upload>`__ |ext_link| topic for specific requirements for how to format the CSV file.


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


       **Use Zip64?**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-use-zip64-start
             :end-before: .. setting-common-use-zip64-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


.. destination-attentive-mobile-add-steps-end


.. _destination-attentive-add-data-template-about:

About filename templates
--------------------------------------------------

.. destination-attentive-add-data-template-intro-start

A filename template defines how the names of segments and campaigns will appear in |destination-name|.

.. destination-attentive-add-data-template-intro-end

.. destination-attentive-add-data-template-about-start

The following table shows how your segment name will appear in |destination-name|. These examples represent a one-time buyer campaign that is attempting to win a second purchase. The campaign is named "Winback" and it has sub-audiences for "Dress Shirts", "Jeans", and "Shoes". Keep these types of patterns in mind when naming campaigns, treatment groups, and sub-audiences within your campaigns that will be sent to |destination-name|.

.. list-table::
   :widths: 150 150 300
   :header-rows: 1

   * - Pattern
     - Segment name(s)
     - Description

   * - (empty)
     - WinbackDressShirts

       WinbackJeans

       WinbackShoes
     - An empty filename template setting is the equivalent of **{{ campaign_name }}{{ group_name }}**.

   * - **campaign_name**
     - Winback
     - Use this pattern for campaigns that do not have more than one treatment group or sub-audiences. This will use the name of the campaign as the name of the segment in |destination-name|.

       .. tip:: Use **{{ campaign_name }}** *instead of* **{{ list_name }}**.

   * - **campaign_name + group_name**
     - Winback_DressShirts

       Winback_Jeans

       Winback_Shoes
     - Use this pattern for campaigns that have more than one treatment group and/or have sub-audiences.

       You may use an underscore ( _ ) or a hyphen ( - ): **{{ campaign_name }}_{{ group_name }}** or **{{ campaign_name }}-{{ group_name }}**.

       You may put them next to each other (without using an underscore or hyphen): **{{ campaign_name }}{{ group_name }}**.

       You may switch the ordering: **{{ group_name }}_{{ campaign_name }}**.

       .. tip:: Be sure to use descriptive names for campaigns *and* treatment groups and be careful to not use the default treatment group names when sending campaigns to |destination-name|.

          This will ensure that downstream users in |destination-name| will be able to understand what each segment is for and won't have to view default naming patterns like "Winback_Recipient1", "WinbackRecipient2", etc.
   * - **group_name**
     - DressShirts

       Jeans

       Shoes
     - Use this pattern to only use the names of treatment groups as segment names in |destination-name|. This will omit the name of the campaign *and* the name of the sub-audience from the segment name.

.. destination-attentive-add-data-template-about-end

.. destination-attentive-add-data-template-important-start

.. important:: The filename template, as used with |destination-name| (and unlike how it is used with other destinations), **does not** build a file name. Instead the filename template defines which strings (campaign and/or treatment group) will be used as the name of a segment in |destination-name|. Spaces in campaign and treatment group names are removed.

.. destination-attentive-add-data-template-important-end



.. TODO: Add workflow resolutions from existing topics HERE.
