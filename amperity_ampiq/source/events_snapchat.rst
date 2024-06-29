.. 
.. https://docs.amperity.com/ampiq/
.. 

.. |destination-name| replace:: Snapchat


.. meta::
    :description lang=en:
        Send offline conversions from Amperity to Snapchat.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send offline conversions from Amperity to Snapchat.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline conversions to Snapchat

==================================================
Send offline conversions to Snapchat
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-snapchat-start
   :end-before: .. term-snapchat-end

.. events-snapchat-overview-start

Upload a CSV file that contains |ext_snapchat_offline_conversions| *and* meets |ext_snapchat_offline_conversions_file_requirements| to |destination-name|.

.. events-snapchat-overview-end


.. _events-snapchat-build-query:

Build a query
==================================================

.. events-snapchat-build-query-start

Use a query to return the fields that align to the |ext_snapchat_offline_conversions_file_requirements| that are supported by |destination-name| for use with |ext_snapchat_offline_conversions|.

For example:

.. code-block:: sql

   SELECT
     TO_HEX(SHA256(TO_UTF8(LOWER(TRIM(mc.email))))) AS email
     ,uit.order_datetime AS timestamp
     ,'purchase' AS event_type
     ,uit.item_quantity AS number_items
     ,uit.item_revenue AS price
     ,uit.order_id AS transaction_id
     ,uit.item_quantity AS quantity
   FROM Merged_Customers mc
   INNER JOIN Unified_Itemizzed_Transactions uit
   ON mc.amperity_id = uit.amperity_id
   WHERE mc.email IS NOT NULL

You can download the results of this query directly from the **Query Editor** in Amperity, and then upload the file directly to |destination-name|. Or you can use an orchestration to send the CSV file to cloud storage or an SFTP bucket.

.. events-snapchat-build-query-end