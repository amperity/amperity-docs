.. https://docs.amperity.com/user/


.. meta::
    :description lang=en:
        Events help your brand associate customer activity to your brand's marketing campaigns.

.. meta::
    :content class=swiftype name=body data-type=text:
        Events help your brand associate customer activity to your brand's marketing campaigns.

.. meta::
    :content class=swiftype name=title data-type=string:
        About events

==================================================
About events
==================================================

.. offline-events-overview-start

The paths your customers take before they visit an app or a website can be complex. One customer might see an offer on TikTok, another while watching a TV show, and another during a conversation with a friend. Attributing customer interactions to marketing activity is not easy, but when they can be attributed it can give your brand more ways to find new customers.

.. offline-events-overview-end

.. offline-events-what-are-offline-events-start

Events represent a set of fields that may be used to help your brand attribute customer purchases and activities with your brand's marketing campaigns. Tracking events helps your brand measure the effectiveness of marketing campaigns across channels. This is done by associating offline customer actions, such as purchases made at physical stores, with an online marketing campaign.

Events share similar use cases across marketing platforms. However, each marketing platform has its own terminology and requirements for using events. For example:

* :ref:`Braze <events-braze>` and :ref:`Klaviyo <events-klaviyo>` support events when sent as custom attributes for any audience.
* :ref:`Criteo <events-criteo>`, :ref:`Pinterest <events-pinterest>`, and :ref:`Snapchat <events-snapchat>` support events for transactions, which must be sent separately from audiences using SFTP.
* :ref:`Meta Ads Manager <events-meta-ads-manager>`, :ref:`The Trade Desk <events-the-trade-desk>`, and :ref:`TikTok Ads Manager <events-tiktok-ads-manager>` each support a complex set of events that are sent to REST API endpoints and require using SQL to return the unique sets of events that are required by each platform.
* :ref:`Google Enhanced Conversions <events-google-enhanced-conversions>` to associate first-party customer data with transactions.

Your brand may need to experiment with how events are provided to the marketing platforms from which your campaigns are run. Amperity is flexible and you may take any approach that works. For example: using a database tables that consolidates events, configuring default attributes to represent events for campaigns, or by using SQL to handle more complex sets of events.

.. offline-events-what-are-offline-events-end


.. _offline-events-destinations:

Send events data
==================================================

.. offline-events-start

Many marketing tools, especially within the paid media ecosystem, support using events to track the success of your marketing campaigns. Use events to help your brand better attribute your marketing campaigns to customer purchases and activity.

.. offline-events-end

.. offline-events-destinations-start

Amperity provides direct connections to the most popular destinations across the paid media ecosystem that support events.

.. offline-events-destinations-end


.. _events-braze:

Braze
--------------------------------------------------

.. events-braze-start

Events may be sent to Braze as :ref:`a set of custom attributes <destination-braze-custom-attributes>` that belong to an audience. The names of these fields are determined by your brand. They may already exist in Braze, in which case you shape the output that is sent from Amperity to align to the names you already have in Braze.

.. events-braze-end


.. _events-criteo:

Criteo
--------------------------------------------------

.. events-criteo-start

Use the :doc:`Criteo destination <destination_criteo>` to send audiences to Criteo, and then advertise to customers across paid media, including connected TV (CTV), banner ads, and video ads.

.. tip:: Use your brand's :doc:`offline transactions data <events_criteo>` to optimize advertising targeting algorithms in Criteo. Review the `requirements for using SFTP to send transactions data to Criteo <https://help.criteo.com/kb/guide/en/how-can-i-pass-my-offline-sales-data-to-criteo-Yf95KPKbjB/Steps/775624,914151,775585>`__ |ext_link|, and then configure Amperity to send offline transactions data for the previous 24 hours on a daily basis.

.. events-criteo-end


.. _events-google-enhanced-conversions:

Google Enhanced Conversions
--------------------------------------------------

.. events-google-enhanced-conversions-start

Use the :doc:`Google Ads destination <destination_google_ads>` to send audiences to Google Ads.

.. tip:: Use your brand's :doc:`offline transactions data <events_google_enhanced_conversions>` to enhance conversion measurement in Google Ads by associating first-party customer data with transactions.

.. events-google-enhanced-conversions-end


.. _events-klaviyo:

Klaviyo
--------------------------------------------------

.. events-klaviyo-start

Events may be sent to Klaviyo as :ref:`a set of custom fields <destination-klaviyo-customer-profile-parameters>` that belong to an audience. The names of these fields are determined by your brand. They may already exist in Klaviyo, in which case you shape the output that is sent from Amperity to align to the names you already have in Klaviyo. Use the **properties** field to define the custom attributes as key-value pairs.

.. events-klaviyo-end


.. _events-meta-ads-manager:

Meta Ads Manager
--------------------------------------------------

.. events-meta-ads-manager-start

Meta Ads Manageris a unified ad creation tool that your brand can use to create and publish ads to Facebook, Messenger, Instagram and the Meta Audience Network. When you send data to Facebook using the Facebook Ads destination, your data will be available from Meta Ads Manager.

:doc:`Send a rolling 7-day window of events <events_meta_ads_manager>` to Meta Ads Manager to help your brand track offline conversions that result from your marketing campaigns. Events may be matched with audiences in Facebook, Facebook Messenger, Instagram, and WhatsApp.

.. events-meta-ads-manager-end


.. _events-pinterest:

Pinterest
--------------------------------------------------

.. events-pinterest-start

Pinterest is a visual discovery engine on which your brand can engage with your customers. Upload a CSV file that contains offline conversions to Pinterest Ads Manager, after which Pinterest Ads Manager will match campaigns to these conversions so your brand can review total conversions in Pinterest Ads Manager as they relate to all active campaigns.

:doc:`Send events <events_pinterest>` to Pinterest at least once a month and send conversion data within 30 days of each conversion occurrence to Pinterest Ads Manager.

.. events-pinterest-end


.. _events-snapchat:

Snapchat
--------------------------------------------------

.. events-snapchat-start

Snapchat is a social media platform for accessing pictures and messages for a short time. Snapchat provides a self-serve platform from which brands can manage ads and advertising campaigns.

:doc:`Send events <events_snapchat>` to Snapchat as a CSV file that contains `offline conversions <https://businesshelp.snapchat.com/s/article/upload-offline-events>`__ |ext_link| *and* meets `events file requirements <https://businesshelp.snapchat.com/s/article/event-file-requirements?language=en_US>`__ |ext_link| to Snapchat.

.. events-snapchat-end


.. _events-the-trade-desk:

The Trade Desk
--------------------------------------------------

.. events-the-trade-desk-start

The Trade Desk is a platform for wide internet advertising and enables the use of UID 2.0 for first-party paid media advertising. Send your best audiences from Amperity to the The Trade Desk, and then reach audiences across connected TVs, live sporting events, and advertising platforms like Disney Advertising (Disney+, Hulu, ESPN), Paramount Advertising, and more.

:doc:`Send events <events_the_trade_desk>` to The Trade Desk as soon as possible, ideally, within 1 to 3 days of the transaction date and avoid sending data older than 25 days. Events should be sent for United States audiences only.

.. events-the-trade-desk-end


.. _events-tiktok-ads-manager:

TikTok Ads Manager
--------------------------------------------------

.. events-tiktok-ads-manager-start

TikTok is the world's leading destination for short-form mobile videos. TikTok's mission is to capture and present the world's creativity, knowledge, and moments that matter in everyday life. Send audiences to TikTok Ads Manager directly from Amperity.

Send :doc:`events to TikTok Ads Manager <events_tiktok_ads_manager>` to help your brand track offline conversions that result from your marketing campaigns. Support for events is part of the TikTok Events API.

For example: When did a customer purchase? What did a customer purchase? Was it from a store or a website? How many items were purchased? Was there more than one purchase? What was the total revenue for each purchase?

When events are shared with TikTok, they can better inform measurement systems by providing insights into offline customer actions such as in-store purchases, offline subscriptions, purchases and more.

.. events-tiktok-ads-manager-end
