.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Microsoft Advertising
.. |destination-api| replace:: Microsoft Ads API
.. |plugin-name| replace:: Microsoft Ads
.. |what-send| replace:: customer data
.. |filter-the-list| replace:: "micro"
.. |oauth-type| replace:: the OAuth credential you created for your |destination-name| account
.. |settings-name| replace:: **Microsoft Ads Settings**
.. |what-settings| replace:: customer ID and account ID
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: |what-settings| settings were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_microsoft_ads|
.. |channel-link| replace:: |campaign_microsoft_ads|
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 24 hours


==================================================
Configure campaigns for Microsoft Advertising
==================================================

.. vale off

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_microsoft_ads.html>`__ |ext_link|.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-ads-start
   :end-before: .. term-microsoft-ads-end

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

.. destination-microsoft-ads-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-microsoft-ads-get-details>`
#. :ref:`Authorize Amperity access to the customer's account <destination-microsoft-ads-configure-oauth>`
#. :ref:`Add destination <destination-microsoft-ads-add-destination>`
#. :ref:`Add data template <destination-microsoft-ads-add-data-template>`

.. destination-microsoft-ads-steps-to-send-end


.. _destination-microsoft-ads-get-details:

Get details
==================================================

.. TODO: Useful link: https://docs.microsoft.com/en-us/advertising/guides/get-started?view=bingads-13#get-ids

.. destination-microsoft-ads-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The |destination-name| customer and account IDs.

       .. tip:: To get your customer and account IDs, sign into the |destination-name| web application, and then click on the **Campaigns** page. The URL for the **Campaigns** page contains two key-value pairs, one for the customer ID and the other for the account ID.

          The URL is similar to:

          ::

             https://ui.ads.microsoft.com/campaign
             /Campaigns.m?cid=12345678&aid=9876543
             21#/customer/...

          The customer ID is the number in the URL that follows the **cid** parameter. For example: "12345678".

          The account ID is the number in the URL that follows the **aid** parameter. For example: "987654321".

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The name of the list to be managed in |destination-name|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - :ref:`Authorize Amperity to send data to the customer's Microsoft Ads account <destination-microsoft-ads-configure-oauth>`.

.. destination-microsoft-ads-get-details-end


.. _destination-microsoft-ads-configure-oauth:

Configure OAuth
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oauth-start
   :end-before: .. term-oauth-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-intro-start
   :end-before: .. destinations-oauth-intro-end

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


.. _destination-microsoft-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-microsoft-ads-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-api-oauth-reminder-start
   :end-before: .. destinations-add-destinations-api-oauth-reminder-end

**To add a destination**

.. destination-microsoft-ads-add-destination-steps-start

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

       .. image:: ../../images/mockup-destinations-tab-add-01-select.png
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

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-01-select.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
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

       .. image:: ../../images/mockup-destinations-tab-add-03-settings.png
          :width: 500 px
          :alt: Settings for Microsoft Ads.
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Account ID**
            - Your account ID for |destination-name|.

          * - **Customer ID**
            - Your customer ID within |destination-name|.

              .. tip:: To get your customer and account IDs, sign into the |destination-name| web application, and then click on the **Campaigns** page. The URL for the **Campaigns** page contains two key-value pairs, one for the customer ID and the other for the account ID.

                 The URL is similar to:

                 ::

                    https://ui.ads.microsoft.com/campaign
                    /Campaigns.m?cid=12345678&aid=9876543
                    21#/customer/...

                 The customer ID is the number in the URL that follows the **cid** parameter. For example: "12345678".

                 The account ID is the number in the URL that follows the **aid** parameter. For example: "987654321".


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

.. destination-microsoft-ads-add-destination-steps-end


.. _destination-microsoft-ads-add-data-template:

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

.. destination-microsoft-ads-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details.png
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

       .. image:: ../../images/mockup-data-template-tab-add-03-settings.png
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

.. destination-microsoft-ads-add-data-template-steps-end


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
