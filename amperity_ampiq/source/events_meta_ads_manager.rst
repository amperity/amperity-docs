.. 
.. https://docs.amperity.com/ampiq/
.. 

.. |destination-name| replace:: Meta Ads Manager
.. |what-send| replace:: offline events
.. |what-enable| replace:: **EXTERN_ID**, **EMAIL**, **FN**, **LN**, **ST**, **CT**, **ZIP**, **COUNTRY**, **BIRTH**, **GEN**, **MADID**, and **PHONE**
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 24 hours
.. |attributes-sent| replace:: |destination-name| requires the **EXTERN_ID**, **EMAIL**, **FN**, **LN**, **ST**, **CT**, **ZIP**, **COUNTRY**, **BIRTH**, **GEN**, **MADID**, and **PHONE** attributes. The **MADID** (mobile advertising ID) attribute is optional.

.. meta::
    :description lang=en:
        Send offline events from Amperity to Meta Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send offline events from Amperity to Meta Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline events to Meta Ads Manager

==================================================
Send offline events to Meta Ads Manager
==================================================

.. events-meta-ads-manager-overview-start

Send offline events to |destination-name| to help your brand track offline conversions that result from your marketing campaigns. Offline events may be matched with audiences in Facebook, Facebook Messenger, Instagram, and WhatsApp.

Transaction events that occurred within the previous seven days *and* contain positive values for product quantity may be sent to |destination-name| using the |ext_facebook_conversions_api_offline_events|.

 .. important:: The first time transaction events are sent to |destination-name|, seven days of data is sent, after which Amperity should be configured to send daily updates, which will maintain a 7-day rolling window of transaction events.

.. events-meta-ads-manager-overview-end

.. events-meta-ads-manager-allowfor-start

.. note:: Offline events are not immediately available in |destination-name|. Allow for up to 24 hours after the point at which Amperity has finished sending offline events for them to be available.

   Offline events that are sent to |destination-name| can be accessed from |ext_meta_events_manager|.

.. events-meta-ads-manager-allowfor-end


.. _events-meta-ads-manager-build-segment:

Build a query
==================================================

.. events-meta-ads-manager-offline-events-build-query-start

Use a query to build a combination of data from the **Unified Itemized Transactions**, **Unified Transactions**, and **Customer 360** tables to represent the set of offline events that your brand wants to use within |destination-name|.

A query that returns a collection offline events for use in |destination-name| is similar to:

.. code-block:: sql

   SELECT
     c360.amperity_id AS external_id
     ,c360.email AS email
     ,c360.phone AS phone
     ,c360.given_name AS given_name
     ,c360.surname AS surname
     ,c360.birthdate AS birthdate
     ,c360.gender AS gender
     ,c360.city AS city
     ,c360.state AS state
     ,c360.postal AS postal
     ,c360.country AS country
     ,uit.order_id AS order_id
     ,uit.item_quantity AS quantity
     ,uit.product_id AS product_id
     ,uit.order_datetime AS timestamp
     ,CAST(uit.item_revenue / uit.item_quantity AS DOUBLE) AS price
     ,'USD' AS currency
     ,'physical_store' AS action_source 
   FROM Unified_Itemized_Transactions uit
   LEFT JOIN Customer_360 c360 ON uit.amperity_id = c360.amperity_id
   WHERE uit.order_datetime > (CURRENT_DATE - interval '7' day)

The query **MUST** contain the following fields: **external_id**, **order_id**, **quantity**, **email** (OR **phone**), **timestamp**, **price**, and **currency**. When **action_source** is not specified the default value is "physical_store".

You may include any of the following customer profile fields to help improve match rates in |destination-name|: **given_name**, **surname**, **birthdate**, **gender**, **city**, **state**, **postal**, and **country**.

.. tip::

   Extend the **WHERE** clause to filter query results by purchase channel, purchase brand, purchase quantity, and to remove items that were returned and/or canceled.

   For example:

   .. code-block:: sql

      WHERE uit.order_datetime > (CURRENT_DATE - interval '7' day)
      AND uit.purchase_channel = 'channel'
      AND uit.purchase_brand = "ACME Essentials"
      AND uit.item_quantity > 0
      AND (c360.email IS NOT NULL OR c360.phone IS NOT NULL)
      AND (
          (is_cancellation IS NULL)
          OR (NOT is_cancellation)
      )
      AND (
          (is_return IS NULL)
          OR (NOT is_return)
      )

.. events-meta-ads-manager-offline-events-build-query-end

.. events-meta-ads-manager-offline-events-parameters-start

Review the :ref:`Conversions API parameters <events-meta-ads-manager-conversions>` section for detailed information about the columns that must be (or may be) returned by your query.

.. events-meta-ads-manager-offline-events-parameters-end


.. _events-meta-ads-manager-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _events-meta-ads-manager-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end

.. include:: ../../amperity_amp360/source/destination_meta_ads_manager.rst
   :start-after: .. sendto-meta-ads-manager-run-orchestration-warning-start
   :end-before: .. sendto-meta-ads-manager-run-orchestration-warning-end


.. _events-meta-ads-manager-conversions:

Conversions API parameters
==================================================

.. include:: ../../amperity_datagrid/source/destination_meta_ads_manager.rst
   :start-after: .. destination-meta-ads-manager-conversion-api-parameters-start
   :end-before: .. destination-meta-ads-manager-conversion-api-parameters-end
