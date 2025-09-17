.. https://docs.amperity.com/operator/


.. |destination-name| replace:: DV360
.. |destination-api| replace:: Google Audience Partner API
.. |plugin-name| replace:: "Google Customer Match"
.. |credential-type| replace:: "google-customer-match"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: customer profiles
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "540"
.. |filter-the-list| replace:: "google"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send customer profiles to DV360.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profiles to DV360.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for DV360

==================================================
Configure destinations for DV360
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dv360-start
   :end-before: .. term-dv360-end

.. destination-dv360-whatis-google-customer-match-start

.. admonition:: What is Google Customer Match?

   |plugin-name| is a unified ad creation tool that you can use to create and publish search, display, and video ads across the Google-owned paid media ecosystem.

   For example:

   * Use Discovery campaigns to `reach customers in the Promotions and Social tabs in Gmail <https://support.google.com/google-ads/answer/9176876>`__ |ext_link|.
   * Use `Google Ads <https://support.google.com/google-ads/answer/2567043>`__ |ext_link| to configure campaign types for search, display, video, app, local, hotel, call, smart, goal-based, and shopping.
   * Run ads within `search results on Google.com <https://support.google.com/google-ads/answer/9510373>`__ |ext_link|.
   * Run ads within the `Shopping tab on Google.com <https://support.google.com/google-ads/answer/2454022>`__ |ext_link|.
   * Send audiences to DV360, and then run video advertising campaigns in `YouTube Ads <https://www.youtube.com/intl/en_us/ads/how-it-works/>`__ |ext_link| or on web pages using any of the `available placement options <https://support.google.com/displayvideo/answer/2697401?hl=en>`__ |ext_link|. DV360 supports advertiser and partner networks.

   Use Amperity to build high-value product affinity segments that are based on first-party data, and then configure Amperity to use the Google Customer Match destination to send those segments to |destination-name|.

   Once uploaded, |plugin-name| hashes each record, and then matches all records against hashed user accounts that already exist in |plugin-name| to identify segments that contain records that match the ones sent from Amperity.

   |plugin-name| builds audience lists that are reachable across the Google-owned paid media ecosystem.

   Use these audience lists for precision cross-selling, to reach and convert new customers, and to improve the retention rate for your most loyal customers.

.. destination-dv360-whatis-google-customer-match-end

.. destination-dv360-api-note-start

.. note:: This destination uses the `Google Audience Partner API <https://support.google.com/google-ads/answer/7361372?hl=en>`__ |ext_link|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-dv360-api-note-end


.. _destination-dv360-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-dv360-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for "Display Video Advertiser" or "Display Video Partner" *must* be completed within Google prior to configuring Amperity to send |what-send| to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **DV360 configuration**

          Amperity must be `configured as a linked account in DV360 <https://support.google.com/displayvideo/answer/9134175?hl=en>`__ |ext_link| before audience lists can be sent from Amperity to partners or advertisers.

       #. In DV360, open **Advertiser Settings**, and then select **Linked Accounts**.
       #. Click **Link New Account**, and then select **External Data Partner**.
       #. Select "Amperity" from the dropdown menu, and then click **Link**.
       #. Confirm Amperity as a linked external data partner, and then click **Create Link**.


       .. admonition:: What are advertisers? What are partners?

          **Display & Video 360 Advertisers**

          `Display & Video 360 Advertisers <https://support.google.com/displayvideo/answer/2696883>`__ |ext_link| represent individual businesses that run advertising campaigns.

          Use your `Advertiser ID <https://support.google.com/displayvideo/answer/11415707?hl=en&ref_topic=6027410>`__ |ext_link| to identify the customer ID to which Amperity should send data.

          **Display & Video 360 Partners**

          `Display & Video 360 Partners <https://support.google.com/displayvideo/answer/7622449>`__ |ext_link| represent agencies, trading desks, and large individual advertisers. Multiple advertisers are often grouped under a single partner.

          Use your partner ID to identify the customer ID to which Amperity should send data.

       After choosing the type of advertising your brand runs on DV360, add your customer ID.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Review user consent policy**

       :ref:`Review the user consent policy <destination-dv360-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-customer-id-start
             :end-before: .. setting-google-ads-customer-id-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-audience-name-start
             :end-before: .. setting-google-ads-audience-name-end

       **Audience description** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-audience-description-start
             :end-before: .. setting-google-ads-audience-description-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-start
             :end-before: .. setting-common-membership-duration-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-frequency-start
             :end-before: .. setting-common-membership-duration-frequency-end

       **Upload key type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-upload-key-type-start
             :end-before: .. setting-google-ads-upload-key-type-end

       **Mobile app ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-mobile-app-id-start
             :end-before: .. setting-google-ads-mobile-app-id-end

.. destination-dv360-get-details-end


.. _destination-dv360-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Google Ads**

.. destination-dv360-credentials-steps-start

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

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-dv360-credentials-steps-end


.. _destination-dv360-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-dv360-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Ads**

.. destination-dv360-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
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
          :align: center
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
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

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
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-customer-id-start
             :end-before: .. setting-google-ads-customer-id-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-audience-name-start
             :end-before: .. setting-google-ads-audience-name-end

       **Audience description** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-audience-description-start
             :end-before: .. setting-google-ads-audience-description-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-start
             :end-before: .. setting-common-membership-duration-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-frequency-start
             :end-before: .. setting-common-membership-duration-frequency-end

       **Upload key type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-upload-key-type-start
             :end-before: .. setting-google-ads-upload-key-type-end

       **Mobile app ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-mobile-app-id-start
             :end-before: .. setting-google-ads-mobile-app-id-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-dv360-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.


.. _destination-dv360-api-matching:

Google Audience Partner API Matching
==================================================

.. destination-dv360-api-matching-start

|destination-name| matching can be done through the following list ID types:

* :ref:`Contact information, including personally identifiable information (PII) matching <destination-dv360-api-matching-contact>`
* :ref:`European Union user consent <destination-dv360-api-matching-eu-consent>`
* :ref:`Mobile device matching <destination-dv360-api-matching-mobile>`

.. destination-dv360-api-matching-end


.. _destination-dv360-api-matching-contact:

Contact Info Matching
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. destination-dv360-api-matching-contact-list-start

A list can be matched to contact information that contains PII data. If a row contains a NULL value, it will be automatically filtered out by the connector and is shown in the error logs. Each field should be matched to one of the following columns:

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity Column
     - Google API Key
     - Description
   * - **Email Address**
     - **email**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Hashes data as SHA-256

   * - **Phone Number**
     - **phone**
     - Converts each phone number to |ext_e164_format| which represents a phone number as a number up to fifteen digits in length (without spaces) that starts with a + symbol. For example: +12061234567.

       For this key, the connector:

       * Trims leading and trailing whitespace
       * Hashes data as SHA-256

   * - **Last Name**
     - **lastname**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Removes spaces in-between
       * Converts to lower-case
       * Hashes data as SHA-256

   * - **First Name**
     - **firstname**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Removes spaces in-between
       * Converts to lower-case
       * Hashes data as SHA-256

   * - **Zip Code**
     - **zip**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case

   * - **Country Code**
     - **country**
     - A two-letter country code in |ext_iso_31661alpha2| format.

       For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to upper-case

.. destination-dv360-api-matching-contact-list-end


.. _destination-dv360-api-matching-eu-consent:

European Union user consent
--------------------------------------------------

.. destination-dv360-api-matching-eu-consent-start

The Google Ads API uses the `Consent object <https://developers.google.com/google-ads/api/reference/rpc/v15/Consent>`__ |ext_link| to specify user consent signals for sending user data to Google for advertising purposes *and* for ad personalization.

.. important:: Customers must `send the required user consent signals <https://support.google.com/google-ads/answer/14310715>`__ |ext_link| when uploading data for advertising to customers in the European Economic Area (EEA) and to adhere to the European Union (EU) user consent policy.

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Required Column
     - 
     - Description
   * - **ad-personalization**
     - 
     - Sets consent for ad personalization. Possible values: **GRANTED**, **UNSPECIFIED**, or **DENIED**.

       .. important:: This value must be set to **GRANTED** to indicate that your brand has received the required user consent.

   * - **ad-user-data**
     - 
     - Sets consent for sending user data to Google for advertising purposes. Possible values: **GRANTED**, **UNSPECIFIED**, or **DENIED**.

       .. important:: This value must be set to **GRANTED** to indicate that your brand has received the required user consent.

.. destination-dv360-api-matching-eu-consent-end


.. _destination-dv360-api-matching-mobile:

Mobile Device ID Matching
--------------------------------------------------

.. destination-dv360-api-matching-mobile-list-start

A list can be matched to mobile device IDs. These may be identifier for advertising (IDFA) or Google advertising IDs (AAID) for mobile devices. If a row contains a NULL value, it will be automatically filtered out by the connector and is shown in the error logs.

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity Column
     - Google API Key
     - Description
   * - **Mobile Device ID**
     - **mobile-id**
     - A list of mobile device IDs provided to Amperity by the customer. For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Retains any hyphens in the mobile device ID

.. destination-dv360-api-matching-mobile-list-end
