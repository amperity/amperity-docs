.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |destination-name| replace:: TikTok Ads Manager
.. |destination-api| replace:: Segment API
.. |plugin-name| replace:: TikTok
.. |what-send| replace:: email addresses, phone numbers, and advertising IDs (IDFAs for iOS devices or AAIDs for Android devices)
.. |filter-the-list| replace:: "tik"
.. |email-plus-send| replace:: additional identifier types
.. |oauth-type| replace:: **:tiktok access**
.. |settings-name| replace:: **TikTok Settings**
.. |what-settings| replace:: advertiser ID, custom audience, and the user ID type; the EMAIL user ID type leads to the best match rates
.. |data-template-config-settings-list| replace:: advertiser ID, custom audience, and the user ID type settings were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_tiktok|
.. |channel-link| replace:: send campaigns to |channel_tiktok|
.. |allow-for-what| replace:: audience mapping
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send custom audiences and offline events to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send custom audiences and offline events to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to TikTok Ads Manager

==================================================
Send data to TikTok Ads Manager
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-tiktok-ads-start
   :end-before: .. term-tiktok-ads-end

.. destination-tiktok-ads-custom-audiences-and-offline-events-start

Your brand can send custom audiences and offline events to |destination-name|:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Custom audiences
          :align: left
          :class: no-scaled-link
     - **Custom audiences**

       :ref:`Custom audiences <destination-tiktok-ads-custom-audiences>` help find people who already know about or have engaged with your brand. Use custom audiences for re-marketing, finding potential repeat customers, and finding lookalike audiences.

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Custom audiences
          :align: left
          :class: no-scaled-link
     - **Offline events**

       :ref:`Offline events <destination-tiktok-ads-offline-events>` help your brand track offline conversions from your marketing campaigns. Support for |ext_tiktok_ads_offline_events| is part of the TikTok Events API.

       .. tip:: Offline events must have occurred within the previous 28 days. The maximum attribution windows for

          * Click-through attribution (CTA) is 28 days
          * View-through attribution (VTA) is 7 days

          Offline events beyond these attribution windows are not matched to ads or displayed in reporting.

.. destination-tiktok-ads-custom-audiences-and-offline-events-end

.. destination-tiktok-ads-steps-to-send-start

This topic describes the steps that are required to send custom audiences and offline events to |destination-name|:

#. :ref:`Get details <destination-tiktok-ads-get-details>`
#. :ref:`Configure OAuth <destination-tiktok-ads-configure-oauth>`
#. :ref:`Custom audiences <destination-tiktok-ads-custom-audiences>`
#. :ref:`Offline events <destination-tiktok-ads-offline-events>`

.. destination-tiktok-ads-steps-to-send-end


.. _destination-tiktok-ads-get-details:

Get details
==================================================

.. destination-tiktok-ads-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The advertiser ID for your |destination-name| account.

       The advertiser ID is a nineteen character string similar to "7654321098765432109". It is available from the drop-down menu in the top right of |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - **TikTok Ads custom audiences only**

       The name of the custom audience to be managed by Amperity.

       If a custom audience already exists, the list of customers in that audience will be updated to match the list sent from Amperity. If a custom audience does not exist, Amperity will add it. Amperity does not delete custom audiences.

       .. important:: A custom audience name may contain up to 400 visible characters, after which the name will be truncated to blank characters followed by "...".


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - **TikTok Ads custom audiences only**

       The user ID type.

       This value must be one of the following: **AAID** (Google), **EMAIL** (email addresses), **IDFA** (Apple), or **PHONE** (phone numbers). Amperity is configured to send **EMAIL** *and* **PHONE** by default for AmpIQ campaigns.

       .. tip:: The **EMAIL** (email addresses) user ID type most often leads to the best match rates.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - **TikTok Ads offline events only**

       The event set ID. (The event set must exist before you can send data to it from Amperity.)

       An event set ID is a nineteen character string similar to "7654321098765432109".

       You can `create an event set ID <https://business-api.tiktok.com/portal/docs?id=1771101027431425>`__ |ext_link| from the TikTok Ads user interface.

       If the event set ID already exists, from the TikTok Ads user interface open **Assets**, then **Events**, and then from the **Offline** box select **Manage**. Each event set will have its own card; the event set ID is located under the name of the event set.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - :ref:`Authorize Amperity to send data to the customer's TikTok Ads Manager account <destination-tiktok-ads-configure-oauth>` for offline events.

       .. note:: Destinations for |destination-name| audience segments and offline profiles both use the same OAuth process, but may require different credentials and must be configured individually.

.. destination-tiktok-ads-get-details-end


.. _destination-tiktok-ads-configure-oauth:

Configure OAuth
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oauth-start
   :end-before: .. term-oauth-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-intro-start
   :end-before: .. destinations-oauth-intro-end

.. destination-tiktok-ads-configure-oauth-important-start

.. important:: TikTok Advertiser Accounts are required to use OAuth. Confirm that the account that will be used to authorize to |destination-name| has the **TikTok Ad Account Operator** or **TikTok Ad Account Admin** permission level. OAuth will not work if your account has **TikTok Ad Account Analyst** permission.

.. destination-tiktok-ads-configure-oauth-important-end

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


.. _destination-tiktok-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-tiktok-ads-custom-audiences:

Custom audiences
==================================================

.. destination-tiktok-ads-custom-audiences-start

Custom audiences help find people who already know about or have engaged with your brand. Use custom audiences for re-marketing, finding potential repeat customers, and finding lookalike audiences.

A custom audience must have at least 1000 members in |destination-name| before it can be used in an ad group.

.. destination-tiktok-ads-custom-audiences-end

.. include:: ../../amperity_ampiq/source/destination_tiktok_ads.rst
   :start-after: .. channel-tiktok-ads-important-one-time-delivery-start
   :end-before: .. channel-tiktok-ads-important-one-time-delivery-end

.. destination-tiktok-ads-api-note-start

.. note:: Amperity uses a combination of endpoints in the |destination-name| Segment API to |ext_tiktok_ads_segment_api_custom_audience_list|, |ext_tiktok_ads_segment_api_segment_audience| the list of customers to match the list of customers sent from Amperity, and then |ext_tiktok_ads_segment_api_segment_mapping|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-tiktok-ads-api-note-end


.. _destination-tiktok-ads-custom-audiences-add-destination:

Add destination
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-api-oauth-reminder-start
   :end-before: .. destinations-add-destinations-api-oauth-reminder-end

**To add a destination**

.. destination-tiktok-ads-custom-audiences-add-destination-start

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

       .. image:: ../../images/mockup-destinations-tab-add-01-select-tiktok-custom.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       Enter the name of the destination and a description. For example: "|destination-name| custom audiences" and "Send offline events to |destination-name|.".


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-tiktok-custom.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-oauth-start
          :end-before: .. destinations-intro-for-additional-settings-oauth-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-tiktok-custom.png
          :width: 500 px
          :alt: Settings for TikTok Ads custom audiences.
          :align: left
          :class: no-scaled-link

       The advertiser ID is a nineteen character string similar to "7654321098765432109". It is available from the drop-down menu in the top right of |destination-name|.

       If a custom audience already exists, the list of customers in that audience will be updated to match the list sent from Amperity. If a custom audience does not exist, Amperity will add it. Amperity does not delete custom audiences.

       The user ID type must be one of the following: **AAID** (Google), **EMAIL** (email addresses), **IDFA** (Apple), or **PHONE** (phone numbers). Amperity is configured to send **EMAIL** *and* **PHONE** by default for AmpIQ campaigns.

       .. note:: When the advertiser ID, custom audience, and the user ID type settings were are not configured as part of the destination, you must configure them as part of the data template before making this destination available to campaigns.


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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-enable-start
          :end-before: .. destinations-business-users-enable-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-tiktok-ads-custom-audiences-add-destination-end


.. _destination-tiktok-ads-custom-audiences-add-data-template:

Add data template
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. include:: ../../amperity_ampiq/source/destination_tiktok_ads.rst
   :start-after: .. channel-tiktok-ads-important-one-time-delivery-start
   :end-before: .. channel-tiktok-ads-important-one-time-delivery-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add a data template**

.. destination-tiktok-ads-custom-audiences-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details-tiktok-custom.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       Enter the name of the data template and a description. For example: "|destination-name| custom audiences" and "Send custom audiences to |destination-name|.".


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

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-tiktok-custom.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. important:: The EMAIL user ID type leads to the best match rates!

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

.. destination-tiktok-ads-custom-audiences-add-data-template-steps-end


.. _destination-tiktok-ads-offline-events:

Offline events
==================================================

.. include:: ../../amperity_ampiq/source/events_tiktok_ads_manager.rst
   :start-after: .. events-tiktok-ads-offline-events-start
   :end-before: .. events-tiktok-ads-offline-events-end

.. include:: ../../amperity_ampiq/source/events_tiktok_ads_manager.rst
   :start-after: .. events-tiktok-ads-offline-events-allowfor-start
   :end-before: .. events-tiktok-ads-offline-events-allowfor-end


.. _destination-tiktok-ads-offline-events-build-query:

Build a query
--------------------------------------------------

.. include:: ../../amperity_ampiq/source/events_tiktok_ads_manager.rst
   :start-after: .. events-tiktok-ads-offline-events-build-query-start
   :end-before: .. events-tiktok-ads-offline-events-build-query-end


.. _destination-tiktok-ads-offline-events-add-destination:

Add destination
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-api-oauth-reminder-start
   :end-before: .. destinations-add-destinations-api-oauth-reminder-end

**To add a destination**

.. destination-tiktok-ads-offline-events-add-destination-start

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

       .. image:: ../../images/mockup-destinations-tab-add-01-select-tiktok-offline.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       Enter the name of the destination and a description. For example: "|destination-name| offline events" and "Send offline events to |destination-name|.".


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-tiktok-offline.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       |destination-name| requires using OAuth to :ref:`authorize Amperity to send offline events to your TikTok Ads Manager account <destination-tiktok-ads-configure-oauth>`.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-tiktok-offline.png
          :width: 500 px
          :alt: Settings for TikTok Ads offline events.
          :align: left
          :class: no-scaled-link

       The advertiser ID is a nineteen character string similar to "7654321098765432109". It is available from the drop-down menu in the top right of |destination-name|.


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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-enable-start
          :end-before: .. destinations-business-users-enable-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-tiktok-ads-offline-events-add-destination-end


.. _destination-tiktok-ads-offline-events-add-data-template:

Add data template
--------------------------------------------------

.. destination-tiktok-ads-offline-events-add-data-template-start

Offline events must be sent using a query and orchestration. The data template associated with offline events should not be made available to the **Campaigns** editor.

.. destination-tiktok-ads-offline-events-add-data-template-end

**To add a data template**

.. destination-tiktok-ads-offline-events-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details-tiktok-offline.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       Enter the name of the data template and a description. For example: "|destination-name| offline events" and "Send offline events to |destination-name|.".


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access-no-campaigns.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       Add the **Event Set ID**.

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-tiktok-offline.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       An event set ID is a nineteen character string similar to "7654321098765432109".

       You can `create an event set ID <https://business-api.tiktok.com/portal/docs?id=1771101027431425>`__ |ext_link| from the TikTok Ads user interface.

       If the event set ID already exists, from the TikTok Ads user interface open **Assets**, then **Events**, and then from the **Offline** box select **Manage**. Each event set will have its own card; the event set ID is located under the name of the event set.

       .. note:: If the event set ID is not specified in the data template it must be specified at orchestration.


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

.. destination-tiktok-ads-offline-events-add-data-template-steps-end


.. _destination-tiktok-ads-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-tiktok-ads-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-tiktok-ads-advertiser-not-found.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-tiktok-ads-workflow-actions-advertiser-not-found`
       * :ref:`destination-tiktok-ads-workflow-actions-invalid-credentials`
       * :ref:`destination-tiktok-ads-workflow-actions-missing-advertiser-permissions`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-tiktok-ads-advertiser-not-found-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-tiktok-ads-workflow-actions-end


.. _destination-tiktok-ads-workflow-actions-advertiser-not-found:

Advertiser not found
--------------------------------------------------

.. destination-tiktok-ads-workflow-actions-advertiser-not-found-start

Amperity may only send data to an advertiser account ID that already exists within |destination-name|. When Amperity cannot find the advertiser account ID within |destination-name|, this may be due to any of the following:

#. An Amperity configuration issue related to the destination *or* the data template that is associated with that destination.
#. An advertiser account ID that is not associated with an approved advertising account in |destination-name|.

.. destination-tiktok-ads-workflow-actions-advertiser-not-found-end

.. destination-tiktok-ads-workflow-actions-advertiser-not-found-steps-start

To resolve this error, determine the cause of the configuration issue.

#. Open the Amperity **Destinations** page in a new browser tab.

   Review the configuration for the destination and data template that is associated with this workflow.
#. Open |ext_tiktok_ads_business_center| and verify that the advertising account exists, is approved, and has a valid advertiser account ID.
#. Update the configuration for Amperity to match the correct advertiser account ID.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-tiktok-ads-workflow-actions-advertiser-not-found-steps-start


.. _destination-tiktok-ads-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-tiktok-ads-workflow-actions-missing-advertiser-permissions:

Missing advertiser permissions
--------------------------------------------------

.. destination-tiktok-ads-workflow-actions-missing-advertiser-permissions-start

The business user that is associated with your |destination-name| account is the same business user that provides credentials for Amperity to manage audiences in |destination-name|.

This business user *must* have permission to manage audiences, which requires that business user to be assigned to one of the following roles:

* Admin
* Operator (recommended)

.. destination-tiktok-ads-workflow-actions-missing-advertiser-permissions-end

.. destination-tiktok-ads-workflow-actions-missing-advertiser-permissions-steps-start

To resolve this error, verify that the business user is assigned to the **Operator** role.

#. Open |ext_tiktok_ads_business_center|.

   Verify the role to which the business user that provides credentials for Amperity is assigned. The business user must be assigned to the **Operator** role.
#. Open the Amperity **Credentials** page in a new tab, and regenerate the authorization link for the business user who is assigned to the **Operator** role.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-tiktok-ads-workflow-actions-missing-advertiser-permissions-steps-start


.. _destination-tiktok-ads-offline-events-parameters:

Offline events parameters
==================================================

.. destination-tiktok-ads-offline-events-parameters-start

The following table describes each of the parameters that are required by |destination-name| for offline events.

The fields are listed alphabetically, but may be returned by a query in any order.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field name
     - Description


   * - **brand**
     - **Optional**. The brand name of the product item.


   * - **content_category**
     - **Optional**. A product category.


   * - **content_id**
     - **Optional**. A product identifier.


   * - **content_name**
     - **Optional**. The name of a product.


   * - **content_type**
     - **Optional**. A product or product type.


   * - **currency**
     - **Optional**. The |ext_iso_4217| code for the currency that is associated with the offline event. For example: "USD".


   * - **email**
     - **Required**. The email associated with the order. 

       .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end


   * - **event**
     - **Required**

       The type of offline event.

       Add **event** to your query and then set a value:

       ::

          ,event AS 'CompletePayment'

       .. important:: The value for **event** must be one of the supported offline event types defined by |destination-name|. A partial list of event types---ones that are more likely to align to your Amperity use cases---is described in the following table.

       The value for **event** must be one of the following:

       **AddPaymentInfo**
         Use when the offline event is associated with a customer adding their payment information as part of the checkout process on your brand's website.

       **AddToCart**
         Use when the offline event is associated with a customer adding a product in your product catalog to the cart on your brand's website.

       **CompletePayment**
         Use when the offline event is associated with a completed transaction, either in-store or from your brand's website.

       **CompleteRegistration**
         Use when the offline event is associated with a customer signing up for something, such as joining your brand's loyalty program or creating an accounnt on your brand's website.

       **Contact**
         Use when the offline event is associated with a customer's interaction with your brand's customer support team.

       **Download**
         Use when the offline event is associated with a customer downloading something from your brand's website.

       **PlaceAnOrder**
         Use when the offline event is associated with a customer placing an order from your brand's website.

       **Subscribe**
         Use when the offline event is associated with a customer subscribing to something, such as your brand's loyalty program or notifications (email or SMS).

       The value for **event** is used to categorize offline conversions within the |destination-name| user interface and may not be customized. Use the event type that best associates how your brand wants to use offline events within |destination-name|.

   * - **event_channel**
     - **Optional**. The event channel type. Must be one of the following values: **email**, **website**, **phone_call**, **in_store**, **crm**, or **other**.

   * - **event_id**
     - **Required**. The unique identifier for the offline event. |destination-name| recommends that the value for **event_id** be a string of 32 characters that includes any combination of numeric digits (0-9), uppercase letters (A-Z), and lowercase letters (a-z).

   * - **event_set_id**
     - **Required**. The event set ID. (The event set must exist before you can send data to it from Amperity.)

       An event set ID is a nineteen character string similar to "7654321098765432109".

       You can find the event set ID from the TikTok Ads user interface. Click **Assets**, then **Events**, and then from the **Offline** box select **Manage**. Each event set will have its own card; the event set ID is located under the name of the event set.

   * - **order_id**
     - **Optional**. The unique ID for a transaction.

   * - **phone**
     - **Recommended**.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

       .. note:: A phone number must be in |ext_e164_format|, which represents a phone number as a number up to fifteen digits in length (without spaces) that starts with a + symbol. For example: +12061234567.


   * - **price**
     - **Optional**. The price of a product or service.


   * - **quantity**
     - **Optional**. The number of items associated with an offline event.


   * - **shop_id**
     - The unique ID for a physical store location or for your brand's website.


   * - **timestamp**
     - The date and time at which the offline event occurred. The timestamp should use |ext_iso_8601| formatting.


   * - **value**
     - **Optional** The value associated with the offline event.

       .. note:: This value is required for revenue reports within |destination-name|.

.. destination-tiktok-ads-offline-events-parameters-end
