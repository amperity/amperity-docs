.. https://docs.amperity.com/datagrid/


.. |destination-name| replace:: The Trade Desk
.. |destination-api| replace:: The Trade Desk API
.. |plugin-name| replace:: The Trade Desk
.. |what-send| replace:: audience lists
.. |filter-the-list| replace:: "trad"
.. |email-plus-send| replace:: additional attributes
.. |credential-type| replace:: **tradedesk**
.. |credential-details| replace:: the The Trade Desk API key and API secret
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: segment name and membership duration settings
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_tdd|
.. |channel-link| replace:: |campaign_tdd|
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send data to The Trade Desk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to The Trade Desk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to The Trade Desk

==================================================
Send data to The Trade Desk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. destination-the-trade-desk-whatis-20-start

.. admonition:: What is UID 2.0?

   .. include:: ../../shared/terms.rst
      :start-after: .. term-unified-id-20-start
      :end-before: .. term-unified-id-20-end

   |destination-name| supports using `UID 2.0 <https://unifiedid.com/docs/intro>`__ |ext_link| to help establish your customers' identities without using third-party data. UID 2.0 enables publisher websites, mobile apps, and Connected TV (CTV) apps to monetize through programmatic workflows, while offering user transparency and privacy controls that meet local market requirements.

.. destination-the-trade-desk-whatis-20-end

.. destination-the-trade-desk-custom-audiences-and-offline-events-start

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

       Amperity can manage :ref:`custom audiences <destination-the-trade-desk-custom-audiences>` for |destination-name| demand-side platform, from which your brand can reach those audiences throughout their entire digital journey and across every channel and device, including:

       * Display advertising on ABC, ESPN, the Wall Street Journal, live sporting events (Major League Baseball), in-store advertising at WalMart, and more.
       * Video advertising on over-the-top (OTT) and connected TV (CTV) apps and platforms, such as Disney+, Major League Baseball, Hulu, Fox, Vevo, Paramount+, and more.
       * Audio advertising in-between songs and during podcasts across Spotify, Pandora, SoundCloud, iHeart, and more.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Custom audiences
          :align: left
          :class: no-scaled-link
     - **Offline events**

       :ref:`Offline events <destination-the-trade-desk-offline-events>` help your brand track offline conversions---for in-store sales, place visits, and other events---for your marketing campaigns. Send offline measurement data to |destination-name|, and then use that data for attribution and targeting.

       .. tip:: Send offline events to |destination-name| as soon as possible, ideally, within 1 to 3 days of the transaction date and avoid sending data older than 25 days.

       .. admonition:: United States audiences only

          Your brand should only send offline events that occurred within the United States to |destination-name|.

.. destination-the-trade-desk-custom-audiences-and-offline-events-end

.. destination-the-trade-desk-api-note-start

.. note:: This destination uses the `The Trade Desk API <https://api.thetradedesk.com/v3/portal/data/doc/UnifiedIDs>`__ |ext_link| to manage audiences and send offline events.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-the-trade-desk-api-note-end

.. destination-the-trade-desk-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-the-trade-desk-get-details>`
#. :ref:`Custom audiences <destination-the-trade-desk-custom-audiences>`
#. :ref:`Offline events <destination-the-trade-desk-offline-events>`

.. destination-the-trade-desk-steps-to-send-end


.. _destination-the-trade-desk-get-details:

Get details
==================================================

.. destination-the-trade-desk-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **UID 2.0 agreement**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unified-id-20-start
          :end-before: .. term-unified-id-20-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-the-trade-desk-uid2-agreement-start
          :end-before: .. setting-the-trade-desk-uid2-agreement-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - Configuration details for |destination-name|.

       * The advertiser ID
       * The advertiser secret

       .. tip:: You can find the advertiser ID and secret key from the management console within |destination-name|. Open **Preferences**, and then **First Party Data Credentials**. The advertiser ID and secret key are shown there.

       .. important:: Your brand must have a UID 2.0 agreement in-place with |destination-name| before configuring this destination.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - The name of a segment in |destination-name|.

       Membership duration defines the length of time (in days) at which individual audience members will belong to the segment in |destination-name|. The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the default duration. The maximum value is "180".

       .. tip:: Set this value to "0" to remove all audience members.

       .. caution:: The membership duration is measured in days. Adjust the membership duration value to be greater than (or equal to) than the frequency at which your brand will send campaigns or orchestrations from Amperity.

          For example, if your brand sends a campaign to |destination-name| every 30 days, then the membership duration should be set to "30". If your brand sends a campaign every 14 days, then the membership duration should be set to "14".

          If a campaign is sent every 30 days, but the membership duration is 14, then the audience size for the last 16 days of the duration window will be 0.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail four.
          :align: left
          :class: no-scaled-link
     - You may use a query to build the list of email addresses or you may select the **email** attribute from the attribute editor in your campaigns.

       .. important:: The **email** column is required and may not be aliased.

       **Example query**

       .. include:: ../../shared/sendtos.rst
          :start-after: .. sendtos-build-query-email-only-start
          :end-before: .. sendtos-build-query-email-only-end

       .. include:: ../../amperity_amp360/source/destination_the_trade_desk.rst
          :start-after: .. sendto-the-trade-desk-build-query-start
          :end-before: .. sendto-the-trade-desk-build-query-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail five.
          :align: left
          :class: no-scaled-link
     - **The Trade Desk offline events only**

       A tracking tag name must be provided. The value for the tracking tag name is a string with a maximum of 256 characters. The tracking tag name will appear in the UI for |destination-name| exactly as it is entered in the configuration for a destination in Amperity that is configured to send offline events to |destination-name|.

       .. important:: The tracking tag name must be unique across all offline tracking tags, especially if shared between an advertiser and an offline provider. The tracking tag name must not duplicate any previous name for the same advertiser and offline data provider ID.

          |destination-name| uses a combination of the tracking tag name, your brand's advertiser ID, and offline data provider ID to build an offline tracking tag ID your brand can use to help measure the success of your marketing campaigns.

       A :ref:`query that defines the set of offline events <destination-the-trade-desk-offline-events-build-query>` to be sent to |destination-name|.


.. destination-the-trade-desk-get-details-end


.. _destination-the-trade-desk-custom-audiences:

Custom audiences
==================================================

.. destination-the-trade-desk-custom-audiences-start

Send custom audiences to manage audiences for |destination-name| demand-side platform, from which your brand can reach audiences throughout their entire digital journey and across every channel and device.

This includes:

* Display advertising on major networks, in major newspapers, live sporting events, and in-store advertising
* Video advertising on over-the-top (OTT) and connected TV (CTV) apps and platforms
* Audio advertising placed in-between songs and during podcasts

.. destination-the-trade-desk-custom-audiences-end

.. destination-the-trade-desk-custom-audiences-usaonly-start

.. important:: Your brand should only send custom audiences that contain customers who reside within the United States to |destination-name|.

.. destination-the-trade-desk-custom-audiences-usaonly-start


.. _destination-the-trade-desk-custom-audiences-add-destination:

Add destination
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-the-trade-desk-add-destination-steps-start

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

       .. image:: ../../images/mockup-destinations-tab-add-01-select-the-trade-desk.png
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

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-the-trade-desk.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-02-select-the-trade-desk.png
          :width: 500 px
          :alt: Set the following credentials for The Trade Desk.
          :align: left
          :class: no-scaled-link

       Add the advertiser ID and secret key for your account with |destination-name|.

       .. tip:: You can find the advertiser ID and secret key from the management console within |destination-name|. Open **Preferences**, and then **First Party Data Credentials**. The advertiser ID and secret key are shown there.

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-the-trade-desk.png
          :width: 500 px
          :alt: Settings for The Trade Desk.
          :align: left
          :class: no-scaled-link

       Optional. You may define a segment name and membership duration (in days) for individual audience members. These may be left blank, and then specified with a data template.

       .. tip:: The membership duration is measured in days. The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the recommended duration, but this value should be greater than (or equal to) the frequency at which your brand sends campaigns or orchestrations to |destination-name|.

          For example, if your brand sends a campaign to |destination-name| every 30 days, then the membership duration should be set to "30". If your brand sends a campaign every 14 days, then the membership duration should be set to "14".

          Set this value to "0" to clear out the audience in the segment.

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

.. destination-the-trade-desk-add-destination-steps-end


.. _destination-the-trade-desk-custom-audiences-add-data-template:

Add data template
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add a data template**

.. destination-the-trade-desk-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details-the-trade-desk.png
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

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-the-trade-desk.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. tip:: The membership duration is measured in days. The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the recommended duration, but this value should be greater than (or equal to) the frequency at which your brand sends campaigns or orchestrations to |destination-name|.

          For example, if your brand sends a campaign to |destination-name| every 30 days, then the membership duration should be set to "30". If your brand sends a campaign every 14 days, then the membership duration should be set to "14".

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


.. _destination-the-trade-desk-offline-events:

Offline events
==================================================

.. include:: ../../amperity_ampiq/source/events_the_trade_desk.rst
   :start-after: .. events-the-trade-desk-overview-start
   :end-before: .. events-the-trade-desk-overview-end

.. include:: ../../amperity_ampiq/source/events_the_trade_desk.rst
   :start-after: .. events-the-trade-desk-usa-only-start
   :end-before: .. events-the-trade-desk-usa-only-end


.. _destination-the-trade-desk-offline-events-build-query:

Build a query
--------------------------------------------------

.. include:: ../../amperity_ampiq/source/events_the_trade_desk.rst
   :start-after: .. events-the-trade-desk-offline-events-build-query-start
   :end-before: .. events-the-trade-desk-offline-events-build-query-end

.. include:: ../../amperity_ampiq/source/events_the_trade_desk.rst
   :start-after: .. events-the-trade-desk-offline-events-build-query-tip-start
   :end-before: .. events-the-trade-desk-offline-events-build-query-tip-end

.. include:: ../../amperity_ampiq/source/events_the_trade_desk.rst
   :start-after: .. events-the-trade-desk-offline-events-build-query-example-start
   :end-before: .. events-the-trade-desk-offline-events-build-query-retail-end


.. _destination-the-trade-desk-offline-events-add-destination:

Add destination
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-api-oauth-reminder-start
   :end-before: .. destinations-add-destinations-api-oauth-reminder-end

**To add a destination**

.. destination-the-trade-desk-offline-events-add-destination-steps-start

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
          :alt: Settings for The Trade Desk.
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Tracking tag name**
            - A tracking tag name must be provided. The value for the tracking tag name is a string with a maximum of 256 characters. The tracking tag name will appear in the UI for |destination-name| exactly as it is entered in the configuration for a destination in Amperity that is configured to send offline events to |destination-name|.

              .. important:: The tracking tag name must be unique across all offline tracking tags, especially if shared between an advertiser and an offline provider. The tracking tag name must not duplicate any previous name for the same advertiser and offline data provider ID.

                 |destination-name| uses a combination of the tracking tag name, your brand's advertiser ID, and offline data provider ID to build an offline tracking tag ID your brand can use to help measure the success of your marketing campaigns.


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

.. destination-the-trade-desk-offline-events-add-destination-steps-end


.. _destination-the-trade-desk-offline-events-add-data-template:

Add data template
--------------------------------------------------

.. destination-meta-ads-manager-offline-events-add-data-template-start

Offline events must be sent using a query and orchestration. The data template associated with offline events should not be made available to the **Campaigns** editor.

.. destination-meta-ads-manager-offline-events-add-data-template-end

**To add a data template**

.. destination-the-trade-desk-offline-events-add-data-template-steps

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details-meta-ads-offline.png
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

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-meta-ads-offline.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       The name of the segment in |destination-name|. The membership duration defines the length of time (in days) at which individual audience members will belong to the segment. The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the recommended duration. Set this value to "0" to clear out the audience in the segment.

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

.. destination-the-trade-desk-offline-events-add-data-template-end


.. _destination-the-trade-desk-parameters-offline-events:

Offline events paramaters
==================================================

.. destination-the-trade-desk-parameters-offline-events-start

The following table describes each of the parameters that are required by |destination-name| for offline events. The **TD1** - **TD10** fields represent the optional fields your brand may include to extend customer profiles to include offline events.

The fields are listed alphabetically, but may be returned by the query in any order.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field name
     - Description

   * - **cat**
     - **Optional**; **Recommended** when transaction details are included with offline events. See **item_code**, **name**, **price**, and **qty**.

       The name of a product in your product catalog.

       This value is most often associated with the **Product Category** field in the **Unified Itemized Transactions** table. Within the **SELECT** statement, return **Product Category**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,product_category AS cat


   * - **city**
     - **Optional**

       The name of the city in which the offline event occurred.


   * - **country**
     - **Optional**

       The three-letter country code for the country in which the offline event occurred.

       .. note:: Offline events should only be sent to |destination-name| when they occurred within the United States.

          Use a **WHERE** clause to limit query results to only offline events that occurred within the United States.

          .. code-block:: sql

             WHERE country = 'USA'

       .. important:: When **country** is included in offline results, **region** must also be included.


   * - **email**
     - **Required**

       The email address that is associated with the offline event.

       .. note:: Amperity converts email addresses to a UID 2.0 value, and then sends them to |destination-name|, after which they are available from within |destination-name| as a **UID2** ID type. Rows that are sent to |destination-name| that do not have a UID 2.0 value or have an empty value are removed by |destination-name|.

          You may use **uid2** as an attribute when Amperity is configured as a `UID2 Operator <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| for your brand.

   * - **eventname**
     - **Optional**; **Required** for sending product catalogs alongside offline events.

       An event name groups your brand's offline events a specific category type for offline events as defined by |destination-name|.

       The event name that most frequently is associated with offline events for retail transactions is "purchase", but the event name may be any of the event names that are described in the following table (listed alphabetically):

       .. list-table::
          :widths: 25 75
          :header-rows: 0

          * - **addtocart**
            - A user added an item to the shopping cart.

          * - **direction**
            - A user requested and received directions to a physical location for your brand.

          * - **login**
            - A user logged in to a site

          * - **messagebusiness**
            - A user sent a message to your brand using a form or email.

          * - **purchase**
            - Default. A user completed a purchase.

              .. tip:: Recommended for *all* retail offline events.

          * - **searchcategory**
            - A user searched for a category

          * - **searchitem**
            - A user searched for an item.

          * - **sitevisit**
            - A user visited a website.

          * - **startcheckout**
            - A user started the checkout process.

          * - **viewcart**
            - A user viewed the contents of their cart.

          * - **viewitem**
            - A user viewed an item.

          * - **wishlistitem**
            - A user added an item to a wish list.


   * - **item_code**
     - **Optional**; **Required** when transaction details are included with offline events. See **cat**, **name**, **price**, and **qty**.

       The unique identifier for a product in your brand's product catalog.

       This value is most often associated with the **Product ID** field in the **Unified Itemized Transactions** table. Within the **SELECT** statement, return **Product ID**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,product_id AS item_code


   * - **name**
     - **Optional**; **Recommended** when transaction details are included with offline events. See **cat**, **item_code**, **price**, and **qty**.

       The name of a product in your brand's product catalog.

       This value is most often associated with the **Product Name** field in the **Unified Itemized Transactions** table. Within the **SELECT** statement, return **Product Name**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,product_name AS name


   * - **orderid**
     - **Recommended**

       A unique identifier for the transaction. The value for this field is a string with a maximum of 64 characters.

       .. note:: This field should be included with offline events to help |destination-name| deduplicate conversion events.

       This value is most often associated with the **Order ID** field in the **Unified Transactions** table. Within the **SELECT** statement, return **Order ID**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,order_id AS orderid


   * - **price**
     - **Optional**; **Recommended** when transaction details are included with offline events. See **cat**, **item_code**, **name**, and **qty**.

       The price of each item that is associated with an offline event. For example: "$9.99"

       This value is most often associated with the **Item Price** field in the **Unified Itemized Transactions** table. Within the **SELECT** statement, return **Item Price**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,item_price AS price


   * - **qty**
     - **Optional**; **Recommended** when transaction details are included with offline events. See **cat**, **item_code**, and **price**.

       The number of items that are associated with an offline event. For example: "10".


       This value is most often associated with the **Item Quantity** field in the **Unified Itemized Transactions** table. Within the **SELECT** statement, return **Item Quantity**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,item_quantity AS qty


   * - **region**
     - **Optional**; **Required** when **country** is included with offline events.

       The region in which the offline event occurred. For the United States, **region** refers to the state in which the offline event occurred.

       Within the **SELECT** statement, return **region** in the query results when **country** is also returned in the query results. This is done typically by mapping a column in a database table to **region**.

       For example:

       .. code-block:: sql

          ,country AS country
          ,state AS region

       .. tip:: Use a **WHERE** clause to limit query results to only offline events that occurred in specific states.

          .. code-block:: sql

             WHERE state = 'CA'


   * - **storeid**
     - **Optional**

       A unique identifier for the location in which the offline event occurred. For retail transactions, this is most often a unique ID for a store or for a website.

       This value is most often associated with the **Store ID** field in the **Unified Transactions** table. Within the **SELECT** statement, return **Store ID**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,store_id AS storeid

       If you don't need to track offline events by individual physical stores, you may use a purchase channel to define this value. For example:

       .. code-block:: sql

          ,purchase_channel AS storeid


   * - **TD1** - **TD10**
     - **Optional**

       A series of optional fields that may be used for category or other organization. The value for these fields is a string with a maximum of 64 characters.


   * - **timestamp**
     - **Required**

       A field in a database table that contains the date and time at which the offline event occurred.

       For retail-focused offline events this is most often the **Order Datetime** field in the **Unified Transactions** table, but it may be from a different table depending on your use case and/or how your brand has configured Amperity. Within the **SELECT** statement, return **Order Datetime**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,order_datetime AS timestamp


   * - **uid2**
     - **Optional**

       You may use **uid2** as an attribute when Amperity is configured as a `UID2 Operator <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| for your brand.

       For example:

       .. code-block:: sql

          SELECT 
            uid2.uid2
            ,uit.order_datetime AS timestamp
          FROM Unified_Itemized_Transactions uit
          LEFT JOIN UID2 uid2 ON uit.amperity_id = uid2.uid2
          WHERE uit.order_datetime > (CURRENT_DATE - interval '25' day)


   * - **value**
     - **Recommended**

       The monetary value of the offline event to your brand. The value for this field must be a decimal.

       .. note:: This field should be included with offline events to help |destination-name| deduplicate conversion events.

       For retail-focused offline events this is most often the **Order Value** field in the **Unified Transactions** table, but it may be from a different table depending on your use case and/or how your brand has configured Amperity. Within the **SELECT** statement, return **Order Value**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,order_value AS value


   * - **valuecurrency**
     - **Optional**

       The currency that was associated with the offline event.

       For retail-focused offline events this is most often the **Currency** field in the **Unified Transactions** table, but it may be from a different table depending on your use case and/or how your brand has configured Amperity. Within the **SELECT** statement, return **Currency**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,currency AS valuecurrency


.. destination-the-trade-desk-parameters-offline-events-end
