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

.. TODO: Add workflow resolutions from existing topics HERE.
