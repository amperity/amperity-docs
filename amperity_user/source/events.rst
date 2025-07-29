.. https://docs.amperity.com/user/


.. meta::
    :description lang=en:
        Offline events help your brand associate customer activity to your brand's marketing campaigns.

.. meta::
    :content class=swiftype name=body data-type=text:
        Offline events help your brand associate customer activity to your brand's marketing campaigns.

.. meta::
    :content class=swiftype name=title data-type=string:
        About offline events

==================================================
About offline events
==================================================

.. offline-events-overview-start

The paths your customers take before they visit an app or a website can be complex. One customer might see an offer on TikTok, another while watching a TV show, and another during a conversation with a friend. Attributing customer interactions to marketing activity is not easy, but when they can be attributed it can give your brand more ways to find new customers.

.. offline-events-overview-end

.. offline-events-what-are-offline-events-start

Offline events represent a set of fields that may be used to help your brand attribute customer purchases and activities with your brand's marketing campaigns. Tracking offline events helps your brand measure the effectiveness of marketing campaigns across channels. This is done by associating offline customer actions, such as purchases made at physical stores, with an online marketing campaign.

Offline events share similar use cases across marketing platforms; however, each marketing platform has its own terminology and requirements for using offline events. For example:

* :ref:`Braze <events-braze>` and :ref:`Klaviyo <events-klaviyo>` support offline events when sent as custom attributes for any audience.
* :ref:`Criteo <events-criteo>`, :ref:`Pinterest <events-pinterest>`, and :ref:`Snapchat <events-snapchat>` support offline events for transactions, which must be sent separately from audiences using SFTP.
* :ref:`Meta Ads Manager <events-meta-ads-manager>`, :ref:`The Trade Desk <events-the-trade-desk>`, and :ref:`TikTok Ads Manager <events-tiktok-ads-manager>` each support a complex set of offline events that are sent to REST API endpoints and require using SQL to return the unique sets of offline events that are required by each platform.
* :ref:`Google Enhanced Conversions <events-google-enhanced-conversions>` to associate first-party customer data with transactions.

Your brand may need to experiment with how offline events are provided to the marketing platforms from which your campaigns are run. Amperity is flexible; you may take any approach that works. For example: using a database tables that consolidates offline events, configuring default attributes to represent offline events for campaigns, or by using SQL to handle more complex sets of offline events.

.. offline-events-what-are-offline-events-end


.. _offline-events-destinations:

Send offline events to ...
==================================================

.. offline-events-start

Many marketing tools, especially within the paid media ecosystem, support using offline events to track the success of your marketing campaigns. Use offline events to help your brand better attribute your marketing campaigns to customer purchases and activity.

.. offline-events-end

.. offline-events-destinations-start

Amperity provides direct connections to the most popular destinations across the paid media ecosystem that support offline events.

.. offline-events-destinations-end

.. offline-events-destinations-tables-start

.. _events-braze:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-braze.png
          :width: 140 px
          :alt: Braze
          :align: center
          :class: no-scaled-link
     - Offline events may be sent to Braze as :ref:`a set of custom attributes <destination-braze-custom-attributes>` that belong to an audience. The names of these fields are determined by your brand. They may already exist in Braze, in which case you will want to shape the output that is sent from Amperity to align to the names you already have in Braze.


.. _events-criteo:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-cr1t30.png
          :width: 140 px
          :alt: Criteo
          :align: center
          :class: no-scaled-link
     - Use the :doc:`Criteo destination <destination_criteo>` to send audiences to Criteo, and then advertise to customers across paid media, including connected TV (CTV), banner ads, and video ads.

       .. tip:: Use your brand's :doc:`offline transactions data <events_criteo>` to optimize advertising targeting algorithms in Criteo. Review the `requirements for using SFTP to send transactions data to Criteo <https://help.criteo.com/kb/guide/en/how-can-i-pass-my-offline-sales-data-to-criteo-Yf95KPKbjB/Steps/775624,914151,775585>`__ |ext_link|, and then configure Amperity to send offline transactions data for the previous 24 hours on a daily basis.


.. _events-google-enhanced-conversions:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-google-ads.svg
          :width: 140 px
          :alt: Criteo
          :align: center
          :class: no-scaled-link
     - Use the :doc:`Google Ads destination <destination_google_ads>` to send audiences to Google Ads.

       .. tip:: Use your brand's :doc:`offline transactions data <events_google_enhanced_conversions>` to enhance conversion measurement in Google Ads by associating first-party customer data with transactions.


.. _events-klaviyo:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-klaviyo.png
          :width: 140 px
          :alt: Klaviyo
          :align: center
          :class: no-scaled-link
     - Offline events may be sent to Klaviyo as :ref:`a set of custom fields <destination-klaviyo-customer-profile-parameters>` that belong to an audience. The names of these fields are determined by your brand. They may already exist in Klaviyo, in which case you will want to shape the output that is sent from Amperity to align to the names you already have in Klaviyo. Use the **properties** field to define the custom attributes as key/value pairs.


.. _events-meta-ads-manager:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-meta.png
          :width: 140 px
          :alt: Meta Ads Manager
          :align: center
          :class: no-scaled-link
     - Meta Ads Manageris a unified ad creation tool that your brand can use to create and publish ads to Facebook, Messenger, Instagram and the Meta Audience Network. When you send data to Facebook using the Facebook Ads destination, your data will be available from Meta Ads Manager.

       :doc:`Send a rolling 7-day window of offline events <events_meta_ads_manager>` to Meta Ads Manager to help your brand track offline conversions that result from your marketing campaigns. Offline events may be matched with audiences in Facebook, Facebook Messenger, Instagram, and WhatsApp.


.. _events-pinterest:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-pinterest.png
          :width: 140 px
          :alt: Pinterest
          :align: center
          :class: no-scaled-link
     - Pinterest is a visual discovery engine on which your brand can engage with your customers. Upload a CSV file that contains offline conversions to Pinterest Ads Manager, after which Pinterest Ads Manager will match campaigns to these conversions so your brand can review total conversions in Pinterest Ads Manager as they relate to all active campaigns.

       :doc:`Send offline events <events_pinterest>` to Pinterest at least once a month and send conversion data within 30 days of each conversion occurrence to Pinterest Ads Manager.


.. _events-snapchat:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-snapchat.png
          :width: 140 px
          :alt: Snapchat
          :align: center
          :class: no-scaled-link
     - Snapchat is a social media platform that allows users to access pictures and messages for a short time. Snapchat provides a self-serve platform from which brands can manage ads and advertising campaigns.

       :doc:`Send offline events <events_snapchat>` to Snapchat as a CSV file that contains `offline conversions <https://businesshelp.snapchat.com/s/article/upload-offline-events>`__ |ext_link| *and* meets `events file requirements <https://businesshelp.snapchat.com/s/article/event-file-requirements?language=en_US>`__ |ext_link| to Snapchat.


.. _events-the-trade-desk:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-thetradedesk.png
          :width: 140 px
          :alt: The Trade Desk
          :align: center
          :class: no-scaled-link
     - The Trade Desk is a platform for wide internet advertising and enables the use of UID 2.0 for first-party paid media advertising. Send your best audiences from Amperity to the The Trade Desk, and then reach audiences across connected TVs, live sporting events, and advertising platforms like Disney Advertising (Disney+, Hulu, ESPN), Paramount Advertising, and more.

       :doc:`Send offline events <events_the_trade_desk>` to The Trade Desk as soon as possible, ideally, within 1 to 3 days of the transaction date and avoid sending data older than 25 days. Offline events should be sent for United States audiences only.


.. _events-tiktok-ads-manager:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-tiktok.png
          :width: 140 px
          :alt: TikTok Ads
          :align: center
          :class: no-scaled-link
     - TikTok is the world’s leading destination for short-form mobile videos. TikTok’s mission is to capture and present the world’s creativity, knowledge, and moments that matter in everyday life. Send audiences to TikTok Ads Manager directly from Amperity.

       Send :doc:`offline events to TikTok Ads Manager <events_tiktok_ads_manager>` to help your brand track offline conversions that result from your marketing campaigns. Support for offline events is part of the TikTok Events API.

       For example: When did a customer purchase? What did a customer purchase? Was it from a store or a website? How many items were purchased? Was there more than one purchase? What was the total revenue for each purchase?

       When offline events are shared with TikTok, they can better inform our measurement systems by providing insights into offline customer actions such as in-store purchases, offline subscriptions, purchases and more.

.. offline-events-destinations-tables-end
