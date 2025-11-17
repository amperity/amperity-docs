.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: DV360
.. |destination-api| replace:: Google Audience Partner API
.. |plugin-name| replace:: Google Customer Match
.. |what-send| replace:: customer profiles
.. |filter-the-list| replace:: "google"
.. |email-plus-send| replace:: additional attributes
.. |credential-type| replace:: **google-customer-match**
.. |credential-details| replace:: the Google Audience Partner API refresh token
.. |oauth-typex| replace:: the OAuth credential you created for your |destination-name| account
.. |settings-name| replace:: **Settings**
.. |what-settings| replace:: product name and customer ID
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: |what-settings| settings were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_google_customer_match|
.. |channel-link| replace:: |campaign_google_dv360|
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


==================================================
Configure campaigns for DV360
==================================================

.. vale off

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_dv360.html>`__ |ext_link|.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-dv360-start
   :end-before: .. term-dv360-end

.. destination-dv360-whatis-google-customer-match-start

.. admonition:: What is Google Customer Match?

   |plugin-name| is a unified ad creation tool that you can use to create and publish search, display, and video ads across the Google-owned paid media ecosystem.

   For example:

   * Use Discovery campaigns to `reach customers in the Promotions and Social tabs in Gmail <https://support.google.com/google-ads/answer/9176876>`__ |ext_link|.
   * Use `Google Ads <https://support.google.com/google-ads/answer/2567043>`__ |ext_link|  to configure campaign types for search, display, video, app, local, hotel, call, smart, goal-based, and shopping.
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

.. destination-dv360-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-dv360-get-details>`
#. :ref:`Add destination <destination-dv360-add-destination>`
#. :ref:`Add data template <destination-dv360-add-data-template>`

.. destination-dv360-steps-to-send-end


.. _destination-dv360-get-details:

Get details
==================================================

.. destination-dv360-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: center
          :class: no-scaled-link
     - Configuration details for |destination-name|.

       The name of the product to which Amperity sends data: "Display Video Advertiser" or "Display Video Partner".

       The customer ID associated with your Google Customer Match account, along with the customer ID associated with the "Display Video Advertiser" or "Display Video Partner" account.

       .. note:: The customer ID must be 10 digits and may not contain dashes.

       A refresh token that is generated from the authentication process that authorizes Amperity to send data to the selected product. This must be a Google account with permission to access the configured customer ID and product within Google.

       .. important:: Authentication for "Display Video Advertiser" or "Display Video Partner" *must* be completed within Google prior to configuring DV360 in Amperity.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: center
          :class: no-scaled-link
     - Amperity must be `configured as a linked account in DV360 <https://support.google.com/displayvideo/answer/9134175?hl=en>`__ |ext_link| before audience lists can be sent from Amperity to partners or advertisers.

       #. In DV360, open **Advertiser Settings**, and then select **Linked Accounts**.
       #. Click **Link New Account**, and then select **External Data Partner**.
       #. Select "Amperity" from the dropdown menu, and then click **Link**.
       #. Confirm Amperity as a linked external data partner, and then click **Create Link**.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: center
          :class: no-scaled-link
     - The name of an audience in |destination-name|. The description is optional. If the audience does not exist, Amperity creates it.

       The membership duration defines the length of time in days at which individual audience members belong to the segment. The membership duration must be 0-540 inclusive or 10000 for an unlimited duration.

       .. tip:: Set this value to "0" to remove all audience members.

       The **Upload key type** must be set to one of :ref:`Contact Info <destination-dv360-api-matching-contact>` or :ref:`Mobile ID <destination-dv360-api-matching-mobile>`.

       If the **Upload key type** is set to "Mobile ID", use the **Mobile app ID** setting to provide the ID for the iOS or Android app from which the mobile ID was collected.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail four.
          :align: center
          :class: no-scaled-link
     - :ref:`Review the user consent policy <destination-dv360-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.


.. destination-dv360-get-details-end


.. _destination-dv360-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-api-oauth-reminder-start
   :end-before: .. destinations-add-destinations-api-oauth-reminder-end

**To add a destination**

.. destination-dv360-add-destination-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select-dv360.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       Enter a name for the destination and provide a description. For example: "|destination-name|" and "This sends |what-send| to |destination-name|".

       From the **Plugin** dropdown, start typing |filter-the-list| to filter the list, and then select Google Customer Match.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-dv360.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       To create a new credential for |destination-name|, generate an authorization link, and then use that link to log into your |destination-name| account. After you have completed that process, you will be provided a refresh token. Add the value for the refresh token to the **Refresh Token** setting in Amperity.

       .. important:: Authentication for "Display Video Advertiser" or "Display Video Partner" *must* be completed within Google prior to configuring DV360 in Amperity.

       .. image:: ../../images/mockup-destinations-tab-credentials-02-select-dv360.png
          :width: 500 px
          :alt: Set the following credentials for DV360.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-dv360-advertiser-or-partner.png
          :width: 500 px
          :alt: Settings for DV360: advertiser or partner?
          :align: left
          :class: no-scaled-link

       Choose "Display Video Advertiser" or "Display Video Partner".

       .. admonition:: What are advertisers? What are partners?

          **Display & Video 360 Advertisers**

          `Display & Video 360 Advertisers <https://support.google.com/displayvideo/answer/2696883>`__ |ext_link| represent individual businesses that run advertising campaigns.

          Use your `Advertiser ID <https://support.google.com/displayvideo/answer/11415707?hl=en&ref_topic=6027410>`__ |ext_link| to identify the customer ID to which Amperity should send data.

          **Display & Video 360 Partners**

          `Display & Video 360 Partners <https://support.google.com/displayvideo/answer/7622449>`__ |ext_link| represent agencies, trading desks, and large individual advertisers. Multiple advertisers are often grouped under a single partner.

          Use your partner ID to identify the customer ID to which Amperity should send data.

       After choosing the type of advertising your brand runs on DV360, add your customer ID.

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-dv360.png
          :width: 500 px
          :alt: Settings for DV360.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-dv360-add-destination-steps-end


.. _destination-dv360-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add a data template**

.. destination-dv360-add-data-template-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-start
          :end-before: .. destinations-data-template-open-template-end

       .. image:: ../../images/mockup-data-template-tab-add-01-details-dv360.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-name-start
          :end-before: .. destinations-data-template-open-template-name-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2
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
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-dv360.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-note-start
          :end-before: .. destinations-data-template-verify-config-settings-note-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
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

.. destination-dv360-add-data-template-steps-end


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

A list can be matched to contact information that contains PII data. If a row contains a **NULL** value, it will be automatically filtered out by the connector and is shown in the error logs. Each field should be matched to one of the following columns:

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
       * Hashes data as one-way SHA-256

   * - **Phone Number**
     - **phone**
     - Converts each phone number to |ext_e164_format| which represents a phone number as a number up to fifteen digits in length (without spaces) that starts with a + symbol. For example: +12061234567.

       For this key, the connector:

       * Trims leading and trailing whitespace
       * Hashes data as one-way SHA-256

   * - **Last Name**
     - **lastname**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Removes spaces in-between
       * Converts to lower-case
       * Hashes data as one-way SHA-256

   * - **First Name**
     - **firstname**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Removes spaces in-between
       * Converts to lower-case
       * Hashes data as one-way SHA-256

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

.. important:: Customers must `send the required user consent signals <https://support.google.com/google-ads/answer/14310715>`__ |ext_link| when uploading data for advertising to customers in the European Economic Area (EEA) or to adhere to the European Union (EU) user consent policy.

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

A list can be matched to mobile device IDs. These may be identifier for advertising (IDFA) or Google advertising IDs (AAID) for mobile devices. If a row contains a **NULL** value, it will be automatically filtered out by the connector and is shown in the error logs.

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
