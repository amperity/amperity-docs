.. https://docs.amperity.com/operator/


.. |destination-name| replace:: TikTok Ads Manager
.. |plugin-name| replace:: "TikTok Ads Events"
.. |credential-type| replace:: "tiktok-offline-events"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: events
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "tik"
.. |allow-for-what| replace:: audience mapping
.. |allow-for-duration| replace:: up to 10 hours


.. meta::
    :description lang=en:
        Configure Amperity to send events to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send events to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for TikTok Ads

==================================================
Configure events for TikTok Ads
==================================================

.. events-tiktok-ads-start

Events help your brand track offline conversions from your marketing campaigns on |destination-name|. Support for sending `events and parameters <https://business-api.tiktok.com/portal/docs?id=1758053486938113>`__ |ext_link| is part of the TikTok Events API.

.. events-tiktok-ads-end

.. events-tiktok-ads-attribution-windows-start

.. tip:: Events must have occurred within the previous 28 days. The maximum attribution windows for

   * Click-through attribution (CTA) is 28 days
   * View-through attribution (VTA) is 7 days

   Events beyond these attribution windows are not matched to ads or displayed in reporting.

.. events-tiktok-ads-attribution-windows-end


.. _events-tiktok-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-tiktok-ads-get-details-table-start

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

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-tiktok-ads-manager-oauth-requirements-start
             :end-before: .. credential-tiktok-ads-manager-oauth-requirements-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Advertiser ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-advertiser-id-start
             :end-before: .. setting-tiktok-ads-manager-advertiser-id-end

       **Event set ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-id-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-id-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-id-context-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-id-context-end

       **Event set name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-name-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-name-end

       **Event source**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-source-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-source-end

.. events-tiktok-ads-get-details-end


.. _events-tiktok-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. events-tiktok-ads-configure-oauth-important-start

.. important:: TikTok Advertiser Accounts are required to use OAuth. Confirm that the account that is used to authorize to |destination-name| has the **TikTok Ad Account Operator** or **TikTok Ad Account Admin** permission level. OAuth will not work if your account has **TikTok Ad Account Analyst** permission.

.. events-tiktok-ads-configure-oauth-important-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for TikTok Ads Manager**

.. events-tiktok-ads-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Refresh token**

          |checkmark-required| **Required**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-oauth-refresh-token-start
          :end-before: .. credential-oauth-refresh-token-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-tiktok-ads-manager-oauth-requirements-start
          :end-before: .. credential-tiktok-ads-manager-oauth-requirements-end

.. events-tiktok-ads-credentials-steps-end


.. _events-tiktok-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _events-tiktok-ads-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for TikTok Ads Manager**

.. events-tiktok-ads-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
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
          :alt: Step three.
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
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Advertiser ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-advertiser-id-start
             :end-before: .. setting-tiktok-ads-manager-advertiser-id-end

       **Event set ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-id-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-id-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-id-context-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-id-context-end

       **Event set name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-name-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-name-end

       **Event source**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-source-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-source-end

       **Auto tracking?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-auto-tracking-start
             :end-before: .. setting-tiktok-ads-manager-offline-auto-tracking-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. events-tiktok-ads-add-steps-end


.. _events-tiktok-ads-offline-events-parameters:

Events parameters
==================================================

.. events-tiktok-ads-offline-events-parameters-start

The following table describes each of the parameters that are required by |destination-name| for events.

The fields are listed alphabetically, but may be returned by a query in any order.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field name
     - Description

   * - **agent**
     - Web events only. A non-hashed user agent from the user's device. This field should be sent along with **ip** when both are available. (Amperity renames this field to "(user_agent)" when events are sent to TikTok Ads Manager.)

   * - **brand**
     - The brand name of the product item.


   * - **content_category**
     - A product category.


   * - **content_id**
     - A product identifier.


   * - **content_name**
     - The name of a product.


   * - **content_type**
     - A product or product type.

   * - **cookie_id**
     - Web events only. A unique ID that matches website visitor events with ads on TikTok. (Amperity renames this field to "(ttp)" when events are sent to TikTok Ads Manager.)

   * - **currency**
     - The |ext_iso_4217| code for the currency that is associated with the offline event. For example: "USD".


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

       .. important:: The value for **event** must be one of the supported offline event types defined by |destination-name|. A partial list of event types--ones that are more likely to align to your Amperity use cases--is described in the following table.

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

       The value for **event** is used to categorize offline conversions within the |destination-name| user interface and may not be customized. Use the event type that best associates how your brand wants to use events within |destination-name|.


   * - **event_channel**
     - The event channel type. Must be one of the following values: **email**, **website**, **phone_call**, **in_store**, **crm**, or **other**.


   * - **event_id**
     - **Required**. The unique identifier for the offline event. |destination-name| recommends that the value for **event_id** be a string of 32 characters that includes any combination of numeric digits (0-9), uppercase letters (A-Z), and lowercase letters (a-z).


   * - **event_set_id**
     - **Required**. The event set ID. (The event set must exist before you can send data to it from Amperity.)

       An event set ID is a nineteen character string similar to "7654321098765432109".

       You can find the event set ID from the TikTok Ads user interface. Click **Assets**, then **Events**, and then from the **Offline** box select **Manage**. Each event set have its own card. The event set ID is located under the name of the event set.


   * - **event_source**
     - The type of event to be uploaded to TikTok Ads Manager. May be one of "web" or "offline".

       Use "web" for events that took place on your website and were collected using the `payload helper <https://business-api.tiktok.com/portal/docs?id=1807346079965186>`__ |ext_link|. Use "offline" for events that took place in a physical store and are measured by an offline event set ID.

       .. note:: This value is specified from the **Event source** setting in the destination that is configured to send events to |destination-name|. This value should not be specified in the query that returns the set of events.

   * - **ip**
     - Web events only. A non-hashed public IP address for the user's device. May be an IPv4 or an IPv6 address, full or compressed. This field should be sent along with **agent** when both are available. 


   * - **order_id**
     - The unique ID for a transaction.


   * - **phone**
     - **Recommended**.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

       .. note:: A phone number must be in |ext_e164_format|, which represents a phone number as a number up to fifteen digits in length (without spaces) that starts with a + symbol. For example: +12061234567.


   * - **price**
     - The price of a product or service.


   * - **quantity**
     - The number of items associated with an offline event.


   * - **shop_id**
     - The unique ID for a physical store location or for your brand's website.


   * - **tiktok_click_id**
     - Web events only. A parameter that is appended to a landing page URL whenever a user clicks on an ad in TikTok. (Amperity renames this field to "ttclid" when events are sent to TikTok Ads Manager.)


   * - **timestamp**
     - The date and time at which the offline event occurred. The timestamp should use |ext_iso_8601| formatting.


   * - **value**
     - The value associated with the offline event.

       .. note:: This value is required for revenue reports within |destination-name|.

.. events-tiktok-ads-offline-events-parameters-end
