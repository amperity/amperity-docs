.. https://docs.amperity.com/internal/



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
Send offline events to Criteo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-criteo-start
   :end-before: .. term-criteo-end

.. events-criteo-overview-start

You can send transactions data (offline events) to |destination-name| as a CSV or TSV file using SFTP.

Review the |ext_criteo_sftp|, and then configure Amperity to connect to |destination-name| using the |destination_sftp| destination.

.. events-criteo-overview-end


.. _events-criteo-build-query:

Build a query
==================================================

.. events-criteo-build-query-start

After the SFTP destination is configured, use a query to map a customer's email address and transactions data to the fields that can be sent to |destination-name|. For example:

.. code-block:: sql

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
