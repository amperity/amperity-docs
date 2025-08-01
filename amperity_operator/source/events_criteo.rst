.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Criteo
.. |what-send| replace:: email address lists
.. |what-enable| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires only email addresses. There are no optional fields.

.. meta::
    :description lang=en:
        Send offline events from Amperity to Criteo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send offline events from Amperity to Criteo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline events to Criteo

==================================================
Configure offline events for Criteo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-criteo-start
   :end-before: .. term-criteo-end

.. events-criteo-overview-start

A large percentage of retail sales take place in stores. By providing transactions data (offline events) for sales that occurred in stores to |destination-name| your brand can use the |destination-name| identity graph to deterministically match online shoppers and offline sales. You can send offline events to |destination-name| as a CSV or TSV file using SFTP.

Review the `requirements for using SFTP to send transactions data to Criteo <https://help.criteo.com/kb/guide/en/how-can-i-pass-my-offline-sales-data-to-criteo-Yf95KPKbjB/Steps/775624,914151,775585>`__ |ext_link|, and then configure Amperity to connect to |destination-name| using the |destination_sftp| destination.

.. events-criteo-overview-end


.. _events-criteo-build-query:

Build a query
==================================================

.. events-criteo-build-query-start

After the SFTP destination is configured, use a query to map a customer's email address and transactions data to the fields that can be sent to |destination-name|. For example:

.. code-block:: sql
   :linenos:

   SELECT
     uit.amperity_id AS user_crmid
     ,mc.email AS user_email
     ,uit.order_id AS event_id
     ,uit.item_quantity AS event_item_quantity
     ,uit.product_id AS event_item_id
     ,uit.currency AS event_currency
     ,uit.item_revenue AS event_item_price
     ,uit.order_datetime AS event_timestamp
     ,uit.store_id AS store_id
     --,uit.purchase_brand AS event_item_brand --optional
     --,uit.product_category AS event_item_category --optional
   FROM Merged_Customers mc
   INNER JOIN Unified_Itemized_Transactions uit
   ON mc.amperity_id = uit.amperity_id
   WHERE mc.email IS NOT NULL
   AND uit.is_return = false
   AND uit.is_cancellation = false

Use an orchestration to send transactions data to |destination-name| using the |destination_sftp| destination.

.. events-criteo-build-query-end
