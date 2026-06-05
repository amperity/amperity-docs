.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Criteo
.. |what-send| replace:: email address lists
.. |what-enable| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires only email addresses. There are no optional fields.

.. meta::
    :description lang=en:
        Send events from Amperity to Criteo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send events from Amperity to Criteo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send events to Criteo

==================================================
Configure events for Criteo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-criteo-start
   :end-before: .. term-criteo-end

.. events-criteo-overview-start

A large percentage of retail sales take place in stores. By providing transactions data for sales that occurred in stores to |destination-name| your brand can use the |destination-name| identity graph to deterministically match online shoppers to events that led to a purchase. You can send events to |destination-name| as a CSV or TSV file using SFTP.

Review the `requirements for using SFTP to send transactions data to Criteo <https://help.criteo.com/kb/guide/en/how-can-i-pass-my-offline-sales-data-to-criteo-Yf95KPKbjB/Steps/775624,914151,775585>`__ |ext_link|, and then configure Amperity to connect to |destination-name| using the |destination_sftp| destination.

.. events-criteo-overview-end


.. _events-criteo-build-table:

Build a Criteo events table
==================================================

.. events-criteo-build-table-start

A **Criteo_Events** table consolidates data for in-store purchases and maps fields from the **Unified Coalesced**, **Unified Itemized Transactions**, and **Unified Transactions** tables to the offline events properties your brand measures in |destination-name|. The schema of the **Criteo_Events** table must match the `offline data format schema <https://help.retailmedia.criteo.com/kb/guide/en/offline-sales-reporting-LTjBTYw7r3/Steps/3511218,3511256,3511259,3511257>`__ |ext_link| required by |destination-name|, including SHA-256 hashed email addresses.

.. important:: Use table versioning to ensure that events can be queried for specific days by :ref:`enabling table versioning for the Criteo_Events table <historical-data-available-versions>`.

The following SQL shows an example table for consolidating |destination-name| events. If your database collects events data in other tables you will need to extend the example to support those tables.

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     uc.hashed_email AS user_key_1
     ,'email' AS user_key_type_1
     ,'customer_ID' AS user_key_type_2
     ,uit.order_id AS event_id
     ,CAST(uit.order_datetime AS timestamp) AS event_time
     ,uit.sku AS content_ids
     ,uit.item_revenue AS product_value
     ,uit.item_quantity AS product_quantity
     ,ut.store_id AS store_id
     ,'USD' AS currency
   FROM Unified_Coalesced uc
   INNER JOIN Unified_Itemized_Transactions uit
   ON uc.amperity_id = uit.amperity_id
   INNER JOIN Unified_Transactions ut
   ON uit.order_id = ut.order_id
   WHERE NOT(uc.email IS NULL)
   AND uit.channel = 'store'
   ORDER BY event_time DESC

Filter out returns and cancellations by extending the **WHERE** clause:

.. code-block:: sql

   AND uit.is_return = false
   AND uit.is_cancellation = false

Extend the table to support multiple brands by adding a **CASE** statement to the **SELECT** statement:

.. code-block:: sql

   ,CASE
     WHEN uc.brand = uit.brand
     THEN uc.hashed_link_key
   END AS user_key_2

and by extending the **WHERE** clause to filter by brands:

.. code-block:: sql

   WHERE NOT(uc.email IS NULL AND uc.link_key is NULL)
   AND uc.datasource in ('Socktown', 'Socktown_Club', 'Socktown_Australia')
   AND uit.channel = 'store'
   AND uit.brand in ('ST','STC','STA')
   ORDER BY event_time DESC

.. events-criteo-build-table-end


.. _events-criteo-build-query:

Build a query
==================================================

.. events-criteo-build-query-start

After the SFTP destination is configured, use a query to map a customer's email address and transactions data to the fields that can be sent to |destination-name|. For example, send only events from the previous day to |destination-name|:

.. code-block:: sql
   :linenos:

   WITH cte_last_version AS (
     SELECT VERSION
     FROM amperity_table_versions
     ORDER BY created_at DESC
   )

   SELECT
     user_key_1
     ,user_key_type_1
     ,user_key_2
     ,user_key_type_2
     ,event_id
     ,DATE_FORMAT(event_time,'%Y-%m-%dT%H:%i:%sZ') as event_time
     ,content_ids
     ,product_value
     ,product_quantity
     ,store_id
     ,currency
   FROM Criteo_Offline
   WHERE brand = 'Socktown'
   AND event_time >= DATE_ADD('day',-2,CURRENT_DATE)

   EXCEPT

   SELECT
     user_key_1
     ,user_key_type_1
     ,user_key_2
     ,user_key_type_2
     ,event_id
     ,DATE_FORMAT(event_time,'%Y-%m-%dT%H:%i:%sZ') AS event_time
     ,content_ids
     ,product_value
     ,product_quantity
     ,store_id
     ,currency
   FROM Criteo_Offline_versioned 
   WHERE amperity_version = (
     SELECT DISTINCT version
     FROM amperity_table_versions
     WHERE offset = 1
     AND table_name = 'Criteo_Offline'
   )
   AND brand = 'Socktown'

Use an orchestration to send the events data to |destination-name| using the |destination_sftp| destination.

.. events-criteo-build-query-end
