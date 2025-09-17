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
        Configure destinations for Google Ads

==================================================
Configure destinations for Google Ads
==================================================

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

   Use Amperity to build high-value product affinity segments that are based on first-party data, and then configure Amperity to use the Google Customer Match destination to send those segments to |destination-name|.

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
          :align: center
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
          :align: center
          :class: no-scaled-link
     - **Review user consent policy**

       :ref:`Review the user consent policy <destination-dv360-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
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

.. destination-google-ads-add-steps-end


.. _destination-google-ads-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-google-ads-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-google-ads-2fa-required.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-google-ads-workflow-actions-cannot-update-audience`
       * :ref:`destination-google-ads-workflow-actions-expired-token`
       * :ref:`destination-google-ads-workflow-actions-incomplete-account-setup`
       * :ref:`destination-google-ads-workflow-actions-invalid-credentials`
       * :ref:`destination-google-ads-workflow-actions-missing-required-attributes`
       * :ref:`destination-google-ads-workflow-actions-2fa-required`
       * :ref:`destination-google-ads-workflow-actions-user-cannot-access-audience`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-google-ads-2fa-required-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-google-ads-workflow-actions-end


.. _destination-google-ads-workflow-actions-cannot-update-audience:

Cannot update audience
--------------------------------------------------

.. destination-google-ads-workflow-actions-cannot-update-audience-start

Amperity uses a refresh token that is generated from your |destination-name| user account to access audiences that are associated with your |destination-name| customer ID. The user for whom the refresh token is created must have permission to update audiences in the |destination-name| account that is associated with the customer ID.

To resolve this error, verify that the user account can update audiences.

#. Open the `Google Ads management console <https://ads.google.com>`__ |ext_link|, and then sign in to your |destination-name| account.
#. Verify that the user has permission to update audiences that are associated with the customer ID.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-google-ads-workflow-actions-cannot-update-audience-start


.. _destination-google-ads-workflow-actions-expired-token:

Expired token
--------------------------------------------------

.. destination-google-ads-workflow-actions-expired-token-start

The token used with |destination-name| has expired.

To resolve this error, refresh the token that is used with |destination-name|.

#. Open the `Google Ads management console <https://ads.google.com>`__ |ext_link|, and then sign in to your |destination-name| account.
#. Refresh the token that is associated with your |destination-name| account.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-google-ads-workflow-actions-expired-token-start


.. _destination-google-ads-workflow-actions-incomplete-account-setup:

Incomplete account setup
--------------------------------------------------

.. destination-google-ads-workflow-actions-incomplete-account-setup-start

Amperity cannot send data to an account in |destination-name| that is not set up completely. For example, this error can occur when an account is an a "DRAFT" state in |destination-name|.

To resolve this error, verify that your |destination-name| account is set up correctly.

#. Open the `Google Ads management console <https://ads.google.com>`__ |ext_link|, and then sign in to your |destination-name| account.
#. Verify the current state of your account. Complete any steps that are required to set up your |destination-name| account.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-google-ads-workflow-actions-incomplete-account-setup-start


.. _destination-google-ads-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-google-ads-workflow-actions-missing-required-attributes:

Missing required fields
--------------------------------------------------

.. destination-google-ads-workflow-actions-missing-required-field-start

One or more required attributes are missing. |destination-name| :ref:`requires the following attributes for contact matching <destination-google-ads-api-matching-contact>`: **firstname**, **lastname**, **email**, **phone**, **country**, and **zip**.

.. destination-google-ads-workflow-actions-missing-required-field-end

**For campaigns**

.. destination-google-ads-workflow-actions-missing-required-field-campaigns-steps-start

To resolve this error, update the list of attributes to include all required fields.

#. Open the **Campaigns** page, and then open the segment used with this workflow.
#. Verify that :ref:`all required attributes are associated with each treatment group that is being sent to <destination-google-ads-api-matching-contact>` |destination-name|. Update the list of attributes if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-google-ads-workflow-actions-missing-required-field-campaigns-steps-start

**For orchestrations**

.. destination-google-ads-workflow-actions-missing-required-field-orchestrations-steps-start

To resolve this error, update the results of the query to include all required fields.

#. Open the **Queries** page, and then open the query used with this workflow.
#. Verify that :ref:`all required attributes are included in the query results <destination-google-ads-api-matching-contact>`. Update the query if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-google-ads-workflow-actions-missing-required-field-orchestrations-steps-start


.. _destination-google-ads-workflow-actions-2fa-required:

Two-factor authentication required
--------------------------------------------------

.. destination-google-ads-workflow-actions-missing-required-field-start

|destination-name| requires two-factor authentication to be enabled.

To resolve this error, ensure that two-factor authentication is enabled for your |destination-name| account.

#. Open the `Google Ads management console <https://ads.google.com>`__ |ext_link|, and then sign in to your |destination-name| account.
#. Verify that two-factor authentication is enabled for your account.

   Click on your username.

   Click on **Manage Account**. Under **Security** enable the option for two-step verification.

#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-google-ads-workflow-actions-missing-required-field-end


.. _destination-google-ads-workflow-actions-user-cannot-access-audience:

User cannot access audience
--------------------------------------------------

.. destination-google-ads-workflow-actions-user-cannot-access-audience-start

When the |destination-name| user account that is associated with the Amperity workflow does not have `permission to view, edit, and manage <https://support.google.com/google-ads/answer/9977851?sjid=9166665541180738738-NA>`__ |ext_link| the linked client account, Amperity will be unable to complete the workflow.

To resolve this error, verify the permissions associated with the user account in |destination-name|.

#. Open the `Google Ads management console <https://ads.google.com>`__ |ext_link|, and then sign in to your |destination-name| account.
#. Verify that |destination-name| user account that is associated with the Amperity workflow has `permission to view, edit, and manage <https://support.google.com/google-ads/answer/9977851?sjid=9166665541180738738-NA>`__ |ext_link| the linked client account.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-google-ads-workflow-actions-user-cannot-access-audience-start


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

A list can be matched to contact information that contains PII data. If a row contains a NULL value, it will be automatically filtered out by the connector and is shown in the error logs. Each field should be matched to one of the following columns:

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

The Google Ads API uses the `Consent object <https://developers.google.com/google-ads/api/reference/rpc/v15/Consent>`__ |ext_link| to specify user consent signals for sending user data to Google for advertising purposes *and* for ad personalization.

.. important:: Customers must `send the required user consent signals <https://support.google.com/google-ads/answer/14310715>`__ |ext_link| when uploading data for advertising to customers in the European Economic Area (EEA) and to adhere to the European Union (EU) user consent policy. Not including these signals may result in lower match rates.

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

A list can be matched to mobile device IDs. These may be identifier for advertising (IDFA) or Google advertising IDs (AAID) for mobile devices. If a row contains a NULL value, it will be automatically filtered out by the connector and is shown in the error logs.

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

A list can be matched to advertiser-generated and assigned user IDs or to custom IDs created by the customer. This list of IDs must be provided to Amperity by the customer so they may be returned as part of the query data sent to |destination-name|. If a row contains a NULL value, it will be automatically filtered out by the connector and is shown in the error logs.

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

