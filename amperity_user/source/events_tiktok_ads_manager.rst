.. https://docs.amperity.com/user/


.. |destination-name| replace:: TikTok Ads


.. meta::
    :description lang=en:
        Send events from Amperity to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send events from Amperity to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send events to TikTok Ads Manager

==================================================
Send events to TikTok Ads Manager
==================================================

.. events-tiktok-ads-offline-events-start

Send events to |destination-name| to help your brand track offline conversions that result from your marketing campaigns. Support for `events and parameters <https://business-api.tiktok.com/portal/docs?id=1758053486938113>`__ |ext_link| is part of the TikTok Events API.

For example: When did a customer purchase? What did a customer purchase? Was it from a store or a website? How many items were purchased? Was there more than one purchase? What was the total revenue for each purchase?

.. events-tiktok-ads-offline-events-end

.. events-tiktok-ads-offline-events-attribution-windows-start

Events must have occurred within the previous 28 days. The maximum attribution windows for

* Click-through attribution (CTA) is 28 days
* View-through attribution (VTA) is 7 days

Events beyond these attribution windows are not matched to ads or displayed in reporting.

.. events-tiktok-ads-offline-events-attribution-windows-end

.. events-tiktok-ads-offline-events-allowfor-start

.. note:: Events are not immediately available in |destination-name|. Allow for up to 24 hours after the point at which Amperity has finished sending events for them to be available.

.. events-tiktok-ads-offline-events-allowfor-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _events-tiktok-ads-build-query:

Build a query
==================================================

.. events-tiktok-ads-offline-events-build-query-start

Use a query to build a combination of data from the your brand's customer 360 database to represent the set of events that your brand wants to use within |destination-name|. A query that collects events for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT 
     'ACME Essentials' AS brand
     ,uit.product_category AS content_category
     ,uit.product_id AS content_id
     ,uit.product_name AS content_name
     ,'product' AS content_type
     ,'USD' AS currency
     ,'email' AS email
     ,'CompletePayment' AS event
     ,'website' AS event_channel
     ,CAST(uit.order_id AS VARCHAR) AS event_id
     ,'7654321098765432109' AS event_set_id
     ,uit.order_id
     ,CONCAT('+1','',REGEXP_REPLACE(mc.phone,'[$\D\s]','')) AS phone
     ,uit.item_price AS price
     ,uit.item_quantity AS quantity
     ,uit.store_id AS shop_id
     ,uit.order_datetime AS timestamp
     ,CAST(uit.item_revenue / uit.item_quantity AS DOUBLE) AS value
   FROM Unified_Itemized_Transactions uit
   LEFT JOIN Merged_Customers mc ON uit.amperity_id = mc.amperity_id
   WHERE uit.order_datetime > (CURRENT_DATE - interval '7' day)

and **MUST** contain the following fields: **email**, **event**, **event_id**, and **event_set_id**. Review the list of supported events parameters while building the query.

Fields that contain PII--email address and phone numbers, for example--should have one-way SHA-256 hashing applied to them.

.. note:: Currency must be in |ext_iso_4217|. For example: "EUR", "USD", or "JPY".

.. note:: The phone number must be in e164 format. If your customer 360 database is not already standardized for e164 format, use the following line instead of **,c360.phone AS phone**:

   ::

      ,CONCAT('+1','',REGEXP_REPLACE(mc.phone,'[$\D\s]','')) AS phone_numbers

.. events-tiktok-ads-offline-events-build-query-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _events-tiktok-ads-parameters:

Events parameters
==================================================

.. include:: ../../amperity_operator/source/events_tiktok_ads.rst
   :start-after: .. events-tiktok-ads-offline-events-parameters-start
   :end-before: .. events-tiktok-ads-offline-events-parameters-end
