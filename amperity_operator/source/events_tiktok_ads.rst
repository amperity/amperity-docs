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
.. |hashed-fields| replace:: **email**, **phone**, and **external_id**


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

Events help your brand track offline and web conversions from your marketing campaigns on |destination-name|. Support for sending `events and parameters <https://business-api.tiktok.com/portal/docs?id=1758053486938113>`__ |ext_link| is part of the TikTok Events API.

.. events-tiktok-ads-end

.. events-tiktok-ads-attribution-windows-start

.. tip:: Events must have occurred within the previous 28 days. The maximum attribution windows for

   * Click-through attribution (CTA) is 28 days
   * View-through attribution (VTA) is 7 days

   Events beyond these attribution windows are not matched to ads or displayed in reporting.

.. events-tiktok-ads-attribution-windows-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sha-256-hashed-fields-start
   :end-before: .. setting-common-sha-256-hashed-fields-end

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

       **Event source ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-id-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-id-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-id-context-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-id-context-end

       **Event source**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-source-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-source-end

       **Fixed event name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-events-fixed-event-name-start
             :end-before: .. setting-tiktok-ads-manager-events-fixed-event-name-end

       **Limited data use**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-events-limited-data-use-start
             :end-before: .. setting-tiktok-ads-manager-events-limited-data-use-end

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

       **Event source ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-id-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-id-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-set-id-context-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-set-id-context-end

       **Event source**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-event-source-start
             :end-before: .. setting-tiktok-ads-manager-offline-event-source-end

       **Auto tracking?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-offline-auto-tracking-start
             :end-before: .. setting-tiktok-ads-manager-offline-auto-tracking-end

       **Fixed event name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-events-fixed-event-name-start
             :end-before: .. setting-tiktok-ads-manager-events-fixed-event-name-end

       **Limited data use**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-events-limited-data-use-start
             :end-before: .. setting-tiktok-ads-manager-events-limited-data-use-end


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

The following table describes each of the parameters that are supported by |destination-name| for offline and web events.

.. important:: If **Event source ID**, **Advertiser ID**, and **Event name** are not correctly configured, TikTok will return an error without an explanation of the problem. Verify that the **Event source ID**, **Advertiser ID**, and **Event name** are correct before troubleshooting other issues.

The fields are listed alphabetically, but may be returned by a query in any order.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field name
     - Description

   * - **agent**
     - Web events only. A non-hashed user agent from the user's device. This field should be sent along with **ip** when both are available. (Amperity sends this field as **user_agent** in the user object.)

   * - **brand**
     - The brand name of the product item. Sent in the contents array.


   * - **content_category**
     - A product category. Sent in the contents array.


   * - **content_id**
     - A product identifier. TikTok recommends using **sku_id** or **item_group_id** if available.


   * - **content_name**
     - The name of a product. Sent in the contents array.


   * - **content_type**
     - The type of content in the event. Set to "product" when **content_id** is a sku_id, or "product_group" when **content_id** is an item_group_id. Defaults to "product" when blank.

   * - **cookie_id**
     - Web events only. A unique ID that matches website visitor events with ads on TikTok. (Amperity sends this field as **ttp** (TikTok Pixel cookie) in the user object.)

   * - **currency**
     - The |ext_iso_4217| code for the currency that is associated with the event. For example: "USD". Defaults to "USD" if blank.


   * - **description**
     - A description of the event. Sent in properties.


   * - **email**
     - At least one identity field, **email** or **phone**, is required for offline events. At least one of **email**, **phone**, or **external_id** is required for web events.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

       .. note:: PII fields (**email**, **phone**, and **external_id**) are normalized and SHA-256 hashed automatically before sending. Values that already match the 64-character lowercase hex pattern are passed through as-is to prevent double-hashing.


   * - **event**
     - The event name for each row. For example: "CompletePayment". If this column is missing from the dataset, the **Fixed event name** connector setting is used. One of the two is required.

       The value for **event** is used to categorize conversions within the |destination-name| user interface. Use the event type that best associates how your brand wants to use events within |destination-name|.

       Add **event** to your query and then set a value, for example:

       ::

          ,event AS 'AddPaymentInfo'

       The value for **event** may be one of the supported event types defined by |destination-name|. The following is a partial list of event types that align to common Amperity use cases. See the `TikTok supported events documentation <https://business-api.tiktok.com/portal/docs/supported-events/v1.3>`__ |ext_link| for a full list of event values.

       .. caution:: Names of event types are case-sensitive.

       **AddPaymentInfo**
         Use when the conversion event is associated with a customer adding their payment information as part of the checkout process on your brand's website.

       **AddToCart**
         Use when the conversion event is associated with a customer adding a product in your product catalog to the cart on your brand's website.

       **CompletePayment**
         Use when the conversion event is associated with a completed transaction, either in-store or from your brand's website.

       **CompleteRegistration**
         Use when the conversion event is associated with a customer signing up for something, such as joining your brand's loyalty program or creating an account on your brand's website.

       **Contact**
         Use when the conversion event is associated with a customer's interaction with your brand's customer support team.

       **Download**
         Use when the conversion event is associated with a customer downloading something from your brand's website.

       **PlaceAnOrder**
         Use when the conversion event is associated with a customer placing an order from your brand's website.

       **Subscribe**
         Use when the conversion event is associated with a customer subscribing to something, such as your brand's loyalty program or notifications (email or SMS).


   * - **event_id**
     - The unique identifier for the event. A string of 32 characters A-Z, a-z, 0-9. An **event_id** is auto-generated from a hash of the **email**, **phone**, **event**, and **timestamp** if omitted. Used for deduplication.


   * - **external_id**
     - Web events only. An external identifier for the user. Trimmed and SHA-256 hashed before sending. At least one of **email**, **phone**, or **external_id** is required for web events.


   * - **ip**
     - Web events only. A non-hashed public IP address for the user's device. May be an IPv4 or an IPv6 address, full or compressed. This field should be sent along with **agent** when both are available.


   * - **locale**
     - Web events only. The locale of the user. Sent in the user object.


   * - **order_id**
     - The unique ID for a transaction. Sent in properties.


   * - **page_url**
     - Web events only. **Required for web events.** The URL of the page where the event occurred.


   * - **phone**
     - At least one identity field (**email** or **phone**) is required for offline events. At least one of **email**, **phone**, or **external_id** is required for web events.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

       .. note:: Phone numbers are normalized to `E.164 format <https://en.wikipedia.org/wiki/E.164>`__ |ext_link| format (US region) and SHA-256 hashed automatically before sending.


   * - **price**
     - The price of a product or service. Used with **quantity** to compute the **value** field; both columns must be present for the value to be sent to TikTok.


   * - **quantity**
     - The number of items associated with the event. Used with **price** to compute the **value** field; both columns must be present for the value to be sent to TikTok.


   * - **referrer_url**
     - Web events only. The referrer URL. Sent as **referrer** in the page object.


   * - **shop_id**
     - The unique ID for a physical store location or for your brand's website. Sent in properties.


   * - **tiktok_click_id**
     - Web events only. A parameter that is appended to a landing page URL whenever a user clicks on an ad in TikTok. (Amperity sends this field as **ttclid** in the user object.)


   * - **timestamp**
     - **Required**. The date and time at which the event occurred. Accepts |ext_iso_8601| format, Unix seconds, or Unix milliseconds.


   * - **value**
     - Computed automatically as the sum of (price * quantity) when both columns are present. You do not supply this field directly.

       .. note:: This value is required for revenue reports within |destination-name|.

.. events-tiktok-ads-offline-events-parameters-end
