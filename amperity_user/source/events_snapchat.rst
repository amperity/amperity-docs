.. https://docs.amperity.com/user/


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

Upload a CSV file that contains `offline conversions <https://businesshelp.snapchat.com/s/article/upload-offline-events>`__ |ext_link| *and* meets `events file requirements <https://businesshelp.snapchat.com/s/article/event-file-requirements?language=en_US>`__ |ext_link| to |destination-name|.

.. events-snapchat-overview-end

.. caution:: This destination is available for sending offline events to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending offline events to |destination-name|.


.. _events-snapchat-build-query:

Build a query
==================================================

.. events-snapchat-build-query-start

Use a query to return the fields that align to the `events file requirements <https://businesshelp.snapchat.com/s/article/event-file-requirements?language=en_US>`__ |ext_link| that are supported by |destination-name| for use with `offline conversions <https://businesshelp.snapchat.com/s/article/upload-offline-events>`__ |ext_link|.

For example:

.. code-block:: sql
   :linenos:

   SELECT
     TO_HEX(SHA256(TO_UTF8(LOWER(TRIM(mc.email))))) AS email
     ,uit.order_datetime AS timestamp
     ,'purchase' AS event_type
     ,uit.item_quantity AS number_items
     ,uit.item_revenue AS price
     ,uit.order_id AS transaction_id
     ,uit.item_quantity AS quantity
   FROM Merged_Customers mc
   INNER JOIN Unified_Itemized_Transactions uit
   ON mc.amperity_id = uit.amperity_id
   WHERE mc.email IS NOT NULL

You can download the results of this query directly from the **Query Editor** in Amperity, and then upload the file directly to |destination-name|. Or you can use an orchestration to send the CSV file to cloud storage or an SFTP bucket.

.. events-snapchat-build-query-end
