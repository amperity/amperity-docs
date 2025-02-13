.. https://docs.amperity.com/datagrid/


.. |destination-name| replace:: Google Ads
.. |destination-api| replace:: Google Ads API
.. |plugin-name| replace:: Google Ads
.. |what-send| replace:: customer data
.. |filter-the-list| replace:: "google"
.. |email-plus-send| replace:: additional attributes
.. |credential-type| replace:: **google-customer-match**
.. |credential-details| replace:: the Google Audience Partner API refresh token
.. |oauth-type| replace:: the OAuth credential you created for your |destination-name| account
.. |settings-name| replace:: **Google Ads Settings**
.. |what-settings| replace:: customer ID
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: customer ID setting was
.. |data-template-config-settings-list-them-vs-it| replace:: it
.. |sendto-link| replace:: |sendto_google_ads|
.. |channel-link| replace:: |campaign_google_ads|
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send data to Google Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Google Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Google Ads

==================================================
Send data to Google Ads
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-ads-start
   :end-before: .. term-google-ads-end

.. destination-google-ads-whatis-google-customer-match-start

.. admonition:: What is Google Customer Match?

   Google Customer Match is a unified ad creation tool that you can use to create and publish search, display, and video ads across the Google-owned paid media ecosystem.

   For example:

   * Use Discovery campaigns to |ext_google_gmail_ads|.
   * Use |ext_google_ads| to configure campaign types for search, display, video, app, local, hotel, call, smart, goal-based, and shopping.
   * Run ads within |ext_google_search|.
   * Run ads within the |ext_google_shopping|.
   * Send audiences to :doc:`DV360 <destination_dv360>`, and then run video advertising campaigns in `YouTube Ads <https://www.youtube.com/intl/en_us/ads/how-it-works/>`__ |ext_link| or on web pages using any of the |ext_dv360_placement_options|. DV360 supports advertiser and partner networks.

   Use Amperity to build high-value and/or product affinity segments that are based on first-party data, and then configure Amperity to use the Google Customer Match destination to send those segments to |destination-name|.

   Once uploaded, |plugin-name| hashes each record, and then matches all records against hashed user accounts that already exist in |plugin-name| to identify segments that contain records that match the ones sent from Amperity.

   |plugin-name| builds audience lists that are reachable across the Google-owned paid media ecosystem.

   Use these audience lists for precision cross-selling, to reach and convert new customers, and to improve the retention rate for your most loyal customers.

.. destination-google-ads-whatis-google-customer-match-end

.. destination-google-ads-api-note-start

.. note:: This destination uses the |ext_google_audience_partner_api|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-google-ads-api-note-end

.. destination-google-ads-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-google-ads-get-details>`
#. :ref:`Authorize Amperity access to the customer's account <destination-google-ads-configure-oauth>`
#. :ref:`Add destination <destination-google-ads-add-destination>`
#. :ref:`Add data template <destination-google-ads-add-data-template>`

.. destination-google-ads-steps-to-send-end


.. _destination-google-ads-get-details:

Get details
==================================================

.. destination-google-ads-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Configuration details for |destination-name|.

       The name of the product to which Amperity will send data: "Google Ads".

       The customer ID associated with your Google Customer Match account, along with the customer ID associated with the "Google Ads" account.

       .. note:: The customer ID must be 10 digits and may not contain dashes.

       A refresh token that is generated from the OAuth process that :ref:`authorizes Amperity to send data to the selected product <destination-google-ads-configure-oauth>`. This must be a Google account with permission to access the configured customer ID and product within Google.

       .. important:: OAuth for "Google Ads" *must* be completed within Google prior to configuring OAuth in Amperity.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - The name of an audience in |destination-name|. The description is optional. If the audience does not exist, Amperity will create it.

       The membership duration defines the length of time (in days) at which individual audience members will belong to the segment. The membership duration must be between 0-540 (inclusive) or 10000 for an unlimited duration.

       .. tip:: Set this value to "0" to remove all audience members.

       The **Upload key type** must be set to one of :ref:`Contact Info <destination-google-ads-api-matching-contact>`, :ref:`User ID <destination-google-ads-api-matching-user>`, or :ref:`Mobile ID <destination-google-ads-api-matching-mobile>`.

       If the **Upload key type** is set to "Mobile ID", use the **Mobile app ID** setting to provide the ID for the iOS or Android app from which the mobile ID was collected.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - :ref:`Review the user consent policy <destination-google-ads-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.


.. destination-dv360-get-details-end


.. _destination-google-ads-configure-oauth:

Configure OAuth
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oauth-start
   :end-before: .. term-oauth-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-intro-start
   :end-before: .. destinations-oauth-intro-end

.. important:: OAuth for "Google Ads" *must* be completed within Google prior to configuring OAuth in Amperity.

**To configure OAuth**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-1-start
          :end-before: .. destinations-oauth-configure-step-1-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-2-start
          :end-before: .. destinations-oauth-configure-step-2-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-3-start
          :end-before: .. destinations-oauth-configure-step-3-end


.. _destination-google-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-google-ads-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-api-oauth-reminder-start
   :end-before: .. destinations-add-destinations-api-oauth-reminder-end

**To add a destination**

.. destination-google-ads-add-destination-steps-start

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

       .. image:: ../../images/mockup-destinations-tab-add-01-select-google-ads.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

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

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-google-ads.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-02-select-google-ads.png
          :width: 500 px
          :alt: Set the following credentials for Google Ads.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-oauth-refresh-token-start
          :end-before: .. destinations-intro-for-additional-settings-oauth-refresh-token-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-google-ads.png
          :width: 500 px
          :alt: Settings for Google Ads.
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Audience name**
            - The name of an audience in |destination-name|. If the audience does not exist, Amperity will create it.

          * - **Audience description**
            - An optional description of the audience.

          * - **Customer ID**
            - The customer ID associated with your Google Customer Match account, along with the customer ID associated with the "Google Ads" account.

              .. note:: The customer ID must be 10 digits and may not contain dashes.

          * - **Customer product**
            - The name of the product to which Amperity will send data. Choose "Google Ads".

          * - **Membership duration**
            - The membership duration defines the length of time (in days) at which individual audience members will belong to the segment. The membership duration must be between 0-540 (inclusive) or 10000 for an unlimited duration.

              .. tip:: Set this value to "0" to remove all audience members.

          * - **Upload key type**
            - The **Upload key type** must be set to one of :ref:`Contact Info <destination-google-ads-api-matching-contact>`, :ref:`User ID <destination-google-ads-api-matching-user>`, or :ref:`Mobile ID <destination-google-ads-api-matching-mobile>`.

          * - **Mobile app ID**
            - If the **Upload key type** is set to "Mobile ID", use the **Mobile app ID** setting to provide the ID for the iOS or Android app from which the mobile ID was collected.


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


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-google-ads-add-destination-steps-end


.. _destination-google-ads-add-data-template:

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

.. destination-google-ads-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details-google-ads.png
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

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-google-ads.png
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

.. destination-google-ads-add-data-template-steps-end


.. _source-google-ads-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. source-google-ads-workflow-actions-start

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
          :alt: The Workflow page, showing a workflow with errors.
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

       .. image:: ../../images/workflow-actions-google-ads-2fa-required.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`source-google-ads-workflow-actions-cannot-update-audience`
       * :ref:`source-google-ads-workflow-actions-expired-token`
       * :ref:`source-google-ads-workflow-actions-incomplete-account-setup`
       * :ref:`source-google-ads-workflow-actions-invalid-credentials`
       * :ref:`source-google-ads-workflow-actions-missing-required-attributes`
       * :ref:`source-google-ads-workflow-actions-2fa-required`
       * :ref:`source-google-ads-workflow-actions-user-cannot-access-audience`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
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

.. source-google-ads-workflow-actions-end


.. _source-google-ads-workflow-actions-cannot-update-audience:

Cannot update audience
--------------------------------------------------

.. source-google-ads-workflow-actions-cannot-update-audience-start

Amperity uses a refresh token that is generated from your |destination-name| user account to access audiences that are associated with your |destination-name| customer ID. The user for whom the refresh token is created must have permission to update audiences in the |destination-name| account that is associated with the customer ID.

To resolve this error, verify that the user account can update audiences.

#. Open the |ext_google_ads_management_console|, and then sign in to your |destination-name| account.
#. Verify that the user has permission to update audiences that are associated with the customer ID.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. source-google-ads-workflow-actions-cannot-update-audience-start


.. _source-google-ads-workflow-actions-expired-token:

Expired token
--------------------------------------------------

.. source-google-ads-workflow-actions-expired-token-start

The token used with |destination-name| has expired.

To resolve this error, refresh the token that is used with |destination-name|.

#. Open the |ext_google_ads_management_console|, and then sign in to your |destination-name| account.
#. Refresh the token that is associated with your |destination-name| account.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. source-google-ads-workflow-actions-expired-token-start


.. _source-google-ads-workflow-actions-incomplete-account-setup:

Incomplete account setup
--------------------------------------------------

.. source-google-ads-workflow-actions-incomplete-account-setup-start

Amperity cannot send data to an account in |destination-name| that is not set up completely. For example, this error can occur when an account is an a "DRAFT" state in |destination-name|.

To resolve this error, verify that your |destination-name| account is set up correctly.

#. Open the |ext_google_ads_management_console|, and then sign in to your |destination-name| account.
#. Verify the current state of your account. Complete any steps that are required to set up your |destination-name| account.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. source-google-ads-workflow-actions-incomplete-account-setup-start


.. _source-google-ads-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _source-google-ads-workflow-actions-missing-required-attributes:

Missing required field(s)
--------------------------------------------------

.. destination-google-ads-workflow-actions-missing-required-field-start

One (or more) required attributes are missing. |destination-name| :ref:`requires the following attributes for contact matching <destination-google-ads-api-matching-contact>`: **firstname**, **lastname**, **email**, **phone**, **country**, and **zip**.

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


.. _source-google-ads-workflow-actions-2fa-required:

Two-factor authentication required
--------------------------------------------------

.. destination-google-ads-workflow-actions-missing-required-field-start

|destination-name| requires two-factor authentication to be enabled.

To resolve this error, ensure that two-factor authentication is enabled for your |destination-name| account.

#. Open the |ext_google_ads_management_console|, and then sign in to your |destination-name| account.
#. Verify that two-factor authentication is enabled for your account.

   Click on your username.

   Click on **Manage Account**. Under **Security** enable the option for two-step verification.

#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-google-ads-workflow-actions-missing-required-field-end


.. _source-google-ads-workflow-actions-user-cannot-access-audience:

User cannot access audience
--------------------------------------------------

.. source-google-ads-workflow-actions-user-cannot-access-audience-start

When the |destination-name| user account that is associated with the Amperity workflow does not have |ext_google_ads_permissions| the linked client account, Amperity will be unable to complete the workflow.

To resolve this error, verify the permissions associated with the user account in |destination-name|.

#. Open the |ext_google_ads_management_console|, and then sign in to your |destination-name| account.
#. Verify that |destination-name| user account that is associated with the Amperity workflow has |ext_google_ads_permissions| the linked client account.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. source-google-ads-workflow-actions-user-cannot-access-audience-start


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
