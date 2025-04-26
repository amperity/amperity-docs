.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Microsoft Advertising
.. |destination-api| replace:: Bing Ads API
.. |plugin-name| replace:: "Microsoft Ads"
.. |credential-type| replace:: "microsoft-ads"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: customer profiles
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "micro"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Configure Amperity to send customer profiles to Microsoft Advertising.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profiles to Microsoft Advertising.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send customer profiles to Microsoft Advertising

==================================================
Send customer profiles to Microsoft Advertising
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_microsoft_ads.html>`__ |ext_link|.

.. destination-microsoft-ads-start

Microsoft Advertising is a pay-per-click partner syndication network, which enables multichannel advertising to global audiencess across display, mobile, video, and native channels, including Bing, Microsoft Audience Network, Microsoft News, Microsoft Edge, and Outlook.

.. destination-microsoft-ads-start

.. destination-microsoft-ads-about-start

Use the `Customer List Record - Bulk API <https://learn.microsoft.com/en-us/advertising/bulk-service/customer-list>`__ |ext_link| to push customer data to the |destination-name| partner syndication network, which enables multichannel advertising to global audiencess across display, mobile, video, and native channels. This network includes:

* Bing (and sites owned and operated by Bing, such as Bing Maps, MSN.com, Bing.de and Bing.co.uk)
* `Microsoft Audience Network <https://about.ads.microsoft.com/en-us/solutions/microsoft-audience-network>`__ |ext_link|
* Microsoft News
* Microsoft Edge
* Outlook.com
* Microsoft Start
* Access to external partners, such as Yahoo.com (and sites owned and operated by Yahoo), DuckDuckGo, AOL.com (and sites owned and operated by AOL), Xandr, and Nine.

.. destination-microsoft-ads-about-end

.. destination-microsoft-ads-api-note-start

.. note:: This destination uses the `Bing Ads API <https://docs.microsoft.com/en-us/advertising/guides/?view=bingads-13>`__ |ext_link|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-microsoft-ads-api-note-end


.. _destination-microsoft-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-microsoft-ads-get-details-table-start

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
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Account and customer IDs**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-advertising-account-and-customer-ids-start
             :end-before: .. setting-microsoft-advertising-account-and-customer-ids-end

          .. tip:: To get your customer and account IDs, sign into the |destination-name| web application, and then click on the **Campaigns** page. The URL for the **Campaigns** page will contain two key-value pairs, one for the customer ID and the other for the account ID.

             The URL is similar to:

             ::

                https://ui.ads.microsoft.com/campaign
                /Campaigns.m?cid=12345678&aid=9876543
                21#/customer/...

             The customer ID is the number in the URL that follows the **cid** parameter. For example: "12345678".

             The account ID is the number in the URL that follows the **aid** parameter. For example: "987654321".


.. destination-microsoft-ads-get-details-end


.. _destination-microsoft-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Microsoft Ads**

.. destination-microsoft-ads-credentials-steps-start

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
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-microsoft-ads-credentials-steps-end


.. _destination-microsoft-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-microsoft-ads-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Microsoft Ads**

.. destination-microsoft-ads-add-steps-start

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

       **Account and customer IDs**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-advertising-account-and-customer-ids-start
             :end-before: .. setting-microsoft-advertising-account-and-customer-ids-end

       **List name** (Required at orchestration)

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-microsoft-advertising-list-name-start
          :end-before: .. setting-microsoft-advertising-list-name-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-microsoft-ads-add-steps-end


.. _destination-microsoft-ads-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-braze-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-microsoft-ads-not-authorized.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-microsoft-ads-workflow-actions-email-address-required`
       * :ref:`destination-microsoft-ads-workflow-actions-expired-credentials`
       * :ref:`destination-microsoft-ads-workflow-actions-invalid-credentials`
       * :ref:`destination-microsoft-ads-workflow-actions-must-accept-terms`
       * :ref:`destination-microsoft-ads-workflow-actions-not-authorized`
       * :ref:`destination-microsoft-ads-workflow-actions-mfa-required`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-microsoft-ads-not-authorized-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-microsoft-ads-workflow-actions-end


.. _destination-microsoft-ads-workflow-actions-email-address-required:

Email address required
--------------------------------------------------

.. destination-microsoft-ads-workflow-actions-email-address-required-start

|destination-name| requires an email address to be present in the data that is sent from Amperity. The email address must be in a field named "Email".

.. destination-microsoft-ads-workflow-actions-email-address-required-end

**For campaigns**

.. destination-microsoft-ads-workflow-actions-email-address-required-campaigns-steps-start

To resolve this error, verify that "Email" is included in the list of attributes that are being sent to |destination-name|.

#. Open the **Campaigns** page, and then open the segment used with this workflow.
#. Verify that "Email" is included in the list of attributes for each treatment group that sends audiences to |destination-name|. Update the list of attributes for each treatment group if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-microsoft-ads-workflow-actions-email-address-required-campaigns-steps-start

**For orchestrations**

.. destination-microsoft-ads-workflow-actions-email-address-required-orchestrations-steps-start

To resolve this error, verify that the "Email" column is included in the query results.

#. Open the **Queries** page, and then open the query used with this workflow.
#. Verify that "Email" is included in the query results. Update the query if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-microsoft-ads-workflow-actions-email-address-required-orchestrations-steps-start


.. _destination-microsoft-ads-workflow-actions-expired-credentials:

Expired credentials
--------------------------------------------------

.. destination-microsoft-ads-workflow-actions-expired-credentials-start

The credentials for your |destination-name| account may have expired. This may require :ref:`creating a new credential <destination-microsoft-ads-workflow-actions-invalid-credentials>` for this destination.

.. destination-microsoft-ads-workflow-actions-expired-credentials-end


.. _destination-microsoft-ads-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-microsoft-ads-workflow-actions-must-accept-terms:

Must accept terms and conditions
--------------------------------------------------

.. destination-microsoft-ads-workflow-actions-must-accept-terms-start

You must accept the `Customer Match terms of use <https://help.ads.microsoft.com/#apex/ads/en/56921/1>`__ |ext_link| before you can use the `Customer List Record - Bulk API <https://learn.microsoft.com/en-us/advertising/bulk-service/customer-list>`__ |ext_link|. You must select the **I accept** option from within the |destination-name| web application.

To resolve this error, you must agree to the `Customer Match terms of use <https://help.ads.microsoft.com/#apex/ads/en/56921/1>`__ |ext_link|.

#. Log in to the |destination-name| web application, and then agree to the `Customer Match terms of use <https://help.ads.microsoft.com/#apex/ads/en/56921/1>`__ |ext_link|.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-microsoft-ads-workflow-actions-must-accept-terms-end


.. _destination-microsoft-ads-workflow-actions-not-authorized:

Not authorized
--------------------------------------------------

.. destination-microsoft-ads-workflow-actions-not-authorized-start

Amperity must have access to the correct combination of `account and customer IDs <https://learn.microsoft.com/en-us/advertising/guides/get-started>`__ |ext_link| in |destination-name|. 

To resolve this error, verify the account and customer IDs in |destination-name|, and then update the destination associated with this workflow for the correct values.

#. Open the **Destinations** page, and then open the destination that is used with this workflow. Review the **Account ID** and **Customer ID** fields that are configured in Amperity.
#. Log in to the |destination-name| web application, and then find the `account and customer IDs <https://learn.microsoft.com/en-us/advertising/guides/get-started>`__ |ext_link| that are associated with your user account.
#. Compare the **Account ID** and **Customer ID** fields configured in Amperity to the account and customer IDs that exist in |destination-name|. Update the configuration for this destination in Amperity as required.

   .. note:: This may require :ref:`creating a new credential <destination-microsoft-ads-workflow-actions-invalid-credentials>` for this destination.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-microsoft-ads-workflow-actions-not-authorized-end


.. _destination-microsoft-ads-workflow-actions-mfa-required:

Two-step authentication required
--------------------------------------------------

.. destination-microsoft-ads-workflow-actions-mfa-required-start

|destination-name| requires `two-step verification <https://support.microsoft.com/en-us/account-billing/how-to-use-two-step-verification-with-your-microsoft-account-c7910146-672f-01e9-50a0-93b4585e7eb4>`__ |ext_link| to be enabled before Amperity can send data.

.. note:: In some cases, this workflow error is caused by a sign-in risk, which represents the possibility that a given authentication request wasn't made by the identity owner. For example: a login attempt from a device that is not trusted.

To resolve this error, ensure that multi-factor authentication is enabled for your |destination-name| account.

#. Log in to the |destination-name| web application.
#. Verify that `two-step verification <https://support.microsoft.com/en-us/account-billing/how-to-use-two-step-verification-with-your-microsoft-account-c7910146-672f-01e9-50a0-93b4585e7eb4>`__ |ext_link| is enabled for your |destination-name| account.

   .. note:: This may require :ref:`creating a new credential <destination-microsoft-ads-workflow-actions-invalid-credentials>` for this destination.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-microsoft-ads-workflow-actions-mfa-required-end
