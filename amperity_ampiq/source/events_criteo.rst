.. https://docs.amperity.com/ampiq/


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

After the SFTP destination is configured, use a query to map a customer's email address and offline sales reporting data to the fields that can be sent to |destination-name|.

.. important:: Review the requirements for `offline sales reporting <https://help.retailmedia.criteo.com/kb/guide/en/offline-sales-reporting-LTjBTYw7r3/Steps/3511218,3511256,3511259,3511257>`__ |ext_link| before building the query that your brand will use to send offline events to |destination-name|.

The following example shows what a query that sends offline sales reporting to |destination-name| may look like for your brand.

.. code-block:: sql

   SELECT
     c.sha256_email AS user_key
     ,'email' AS user_key_type
     ,uit.order_id AS event_id
     ,uit.item_quantity AS product_quantity
     ,CONCAT('P', substr(prod.product_id, 1, 2, 3)) AS content_ids
     ,uit.item_revenue AS product_value
     ,CAST(uit.order_datetime AS timestamp) AS event_time
     ,uit.store_id AS store_id
   FROM Customer_360 c
   INNER JOIN Unified_Itemized_Transactions uit
   ON c.amperity_id = uit.amperity_id
   JOIN Product_Catalog_Table prod 
   ON uit.product_id = prod.ITEM_ID
   WHERE c.email IS NOT NULL
   AND uit.is_return = false
   AND uit.is_cancellation = false
   AND order_datetime > CURRENT_DATE - INTERVAL '1' DAY;

Use an orchestration to send transactions to |destination-name| using the |destination_sftp| destination.

.. events-criteo-build-query-end
