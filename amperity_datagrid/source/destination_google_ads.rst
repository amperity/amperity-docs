.. https://docs.amperity.com/operator/



.. |destination-name| replace:: Google Ads
.. |destination-api| replace:: Google Ads API
.. |plugin-name| replace:: "Google Customer Match"
.. |credential-type| replace:: "google-customer-match"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "540"
.. |filter-the-list| replace:: "google"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours

.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Google Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Google Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Google Ads

==================================================
Send audiences to Google Ads
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_google_ads.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-ads-start
   :end-before: .. term-google-ads-end

.. destination-google-ads-whatis-google-customer-match-start

.. admonition:: What is Google Customer Match?

   |plugin-name| is a unified ad creation tool that you can use to create and publish search, display, and video ads across the Google-owned paid media ecosystem.

   For example:

   * Use Discovery campaigns to `reach customers in the Promotions and Social tabs in Gmail <https://support.google.com/google-ads/answer/9176876>`__ |ext_link|.
   * Use `Google Ads <https://support.google.com/google-ads/answer/2567043>`__ |ext_link| to configure campaign types for search, display, video, app, local, hotel, call, smart, goal-based, and shopping.
   * Run ads within `search results on Google.com <https://support.google.com/google-ads/answer/9510373>`__ |ext_link|.
   * Run ads within the `Shopping tab on Google.com <https://support.google.com/google-ads/answer/2454022>`__ |ext_link|.
   * Send audiences to DV360, and then run video advertising campaigns in `YouTube Ads <https://www.youtube.com/intl/en_us/ads/how-it-works/>`__ |ext_link| or on web pages using any of the `available placement options <https://support.google.com/displayvideo/answer/2697401?hl=en>`__ |ext_link|. DV360 supports advertiser and partner networks.

   Use Amperity to build high-value and/or product affinity segments that are based on first-party data, and then configure Amperity to use the Google Customer Match destination to send those segments to |destination-name|.

   Once uploaded, |plugin-name| hashes each record, and then matches all records against hashed user accounts that already exist in |plugin-name| to identify segments that contain records that match the ones sent from Amperity.

   |plugin-name| builds audience lists that are reachable across the Google-owned paid media ecosystem.

   Use these audience lists for precision cross-selling, to reach and convert new customers, and to improve the retention rate for your most loyal customers.

.. destination-google-ads-whatis-google-customer-match-end

.. destination-google-ads-api-note-start

.. note:: This destination uses the `Google Audience Partner API <https://support.google.com/google-ads/answer/7361372?hl=en>`__ |ext_link|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-google-ads-api-note-end


.. _destination-google-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-google-ads-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for "Google Ads" *must* be completed within Google prior to configuring Amperity to send |what-send| to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Review user consent policy**

       :ref:`Review the user consent policy <destination-dv360-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
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

.. destination-google-ads-get-details-end


.. _destination-google-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Google Ads**

.. destination-google-ads-credentials-steps-start

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

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-google-ads-credentials-steps-end


.. _destination-google-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-google-ads-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Ads**

.. destination-google-ads-add-steps-start

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
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-google-ads-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.

.. _destination-google-ads-api-matching:

Google Ads API Matching
==================================================

.. destination-google-ads-api-matching-start

|destination-name| API matching can be done through the following list ID types:

* :ref:`Contact information, including personally identifiable information (PII) matching <destination-google-ads-api-matching-contact>`
* :ref:`European Union user consent <destination-google-ads-api-matching-eu-consent>`
* :ref:`Mobile device matching <destination-google-ads-api-matching-mobile>`
* :ref:`Advertiser-generated and assigned user ID matching <destination-google-ads-api-matching-user>`

.. destination-google-ads-api-matching-end


.. _destination-google-ads-api-matching-contact:

Contact Info Matching
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. destination-google-ads-api-matching-contact-list-start

A list can be matched to contact information that contains PII data. If a row contains a NULL value, it will be automatically filtered out by the connector and will be shown in the error logs. Each field should be matched to (at least) one of the following columns:

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity
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

.. destination-google-ads-api-matching-contact-list-end


.. _destination-google-ads-api-matching-eu-consent:

European Union user consent
--------------------------------------------------

.. destination-google-ads-api-matching-eu-consent-start

The Google Ads API uses the |ext_google_consent_object| to specify user consent signals for sending user data to Google for advertising purposes *and* for ad personalization.

.. important:: Customers must |ext_google_consent_object_faq| when uploading data for advertising to customers in the European Economic Area (EEA) and/or to adhere to the European Union (EU) user consent policy. Not including these signals may result in lower match rates.

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Required Column
     - 
     - Description
   * - **ad-personalization**
     - 
     - Sets consent for ad personalization. Possible values: **GRANTED**, **UNSPECIFIED**, or **DENIED**. Default value: **UNSPECIFIED**.

       .. important:: This value must be set to **GRANTED** to indicate that your brand has received the required user consent.

   * - **ad-user-data**
     - 
     - Sets consent for sending user data to Google for advertising purposes. Possible values: **GRANTED**, **UNSPECIFIED**, or **DENIED**. Default value: **UNSPECIFIED**.

       .. important:: This value must be set to **GRANTED** to indicate that your brand has received the required user consent.

.. destination-google-ads-api-matching-eu-consent-end


.. _destination-google-ads-api-matching-mobile:

Mobile Device ID Matching
--------------------------------------------------

.. destination-google-ads-api-matching-mobile-list-start

A list can be matched to mobile device IDs. These may be identifier for advertising (IDFA) or Google advertising IDs (AAID) for mobile devices. If a row contains a NULL value, it will be automatically filtered out by the connector and will be shown in the error logs.

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity
     - Google API Key
     - Description
   * - **Mobile Device ID**
     - **mobile-id**
     - A list of mobile device IDs provided to Amperity by the customer. For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Retains any hyphens in the mobile device ID

.. destination-google-ads-api-matching-mobile-list-end


.. _destination-google-ads-api-matching-user:

User ID Matching
--------------------------------------------------

.. destination-google-ads-api-matching-user-start

A list can be matched to advertiser-generated and assigned user IDs and/or to custom IDs created by the customer. This list of IDs must be provided to Amperity by the customer so they may be returned as part of the query data sent to |destination-name|. If a row contains a NULL value, it will be automatically filtered out by the connector and will be shown in the error logs.

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity
     - Google API Key
     - Description
   * - **User ID**
     - **user-id**
     - A list of customer IDs provided to Amperity by the customer. For this key, the connector:

       * Trims leading and trailing whitespace
       * Optional. Hashes data as SHA-256

.. destination-google-ads-api-matching-user-end

