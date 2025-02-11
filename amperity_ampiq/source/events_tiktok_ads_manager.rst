.. https://docs.amperity.com/ampiq/


.. |destination-name| replace:: TikTok Ads


.. meta::
    :description lang=en:
        Send offline events from Amperity to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send offline events from Amperity to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline events to TikTok Ads Manager

==================================================
Send offline events to TikTok Ads Manager
==================================================

.. events-tiktok-ads-offline-events-start

Send offline events to |destination-name| to help your brand track offline conversions that result from your marketing campaigns. Support for `offline events and parameters <https://business-api.tiktok.com/portal/docs?id=1758053486938113>`__ |ext_link| is part of the TikTok Events API.

For example: When did a customer purchase? What did a customer purchase? Was it from a store or a website? How many items were purchased? Was there more than one purchase? What was the total revenue for each purchase?

.. events-tiktok-ads-offline-events-end

.. events-tiktok-ads-offline-events-attribution-windows-start

Offline events must have occurred within the previous 28 days. The maximum attribution windows for

* Click-through attribution (CTA) is 28 days
* View-through attribution (VTA) is 7 days

Offline events beyond these attribution windows are not matched to ads or displayed in reporting.

.. events-tiktok-ads-offline-events-attribution-windows-end

.. events-tiktok-ads-offline-events-allowfor-start

.. note:: Offline events are not immediately available in |destination-name|. Allow for up to 24 hours after the point at which Amperity has finished sending offline events for them to be available.

.. events-tiktok-ads-offline-events-allowfor-end


.. _events-tiktok-ads-build-query:

Build a query
==================================================

.. events-tiktok-ads-offline-events-build-query-start

Use a query to build a combination of data from the your brand's customer 360 database to represent the set of offline events that your brand wants to use within |destination-name|. A query that collects offline events for use in |destination-name| is similar to:

.. code-block:: sql

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

and **MUST** contain the following fields: **email**, **event**, **event_id**, and **event_set_id**. Review the list of supported offline events parameters while building the query.

Fields that contain PII---email address and phone numbers, for example---should have one-way SHA-256 hashing applied to them.

.. note:: Currency must be in |ext_iso_4217|. For example: "EUR", "USD", or "JPY".

.. note:: The phone number must be in e164 format. If your customer 360 database is not already standardized for e164 format, use the following line instead of **,c360.phone AS phone**:

   ::

      ,CONCAT('+1','',REGEXP_REPLACE(mc.phone,'[$\D\s]','')) AS phone_numbers

.. events-tiktok-ads-offline-events-build-query-end


.. _events-tiktok-ads-parameters:

Offline events parameters
==================================================

.. include:: ../../amperity_datagrid/source/destination_tiktok_ads.rst
   :start-after: .. destination-tiktok-ads-offline-events-parameters-start
   :end-before: .. destination-tiktok-ads-offline-events-parameters-end
