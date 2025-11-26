.. https://docs.amperity.com/user/


.. |destination-name| replace:: Pinterest Ads Manager


.. meta::
    :description lang=en:
        Send offline conversions from Amperity to Pinterest.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send offline conversions from Amperity to Pinterest.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline conversions to Pinterest

==================================================
Send offline conversions to Pinterest
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pinterest-start
   :end-before: .. term-pinterest-end

.. events-pinterest-overview-start

Upload a CSV file that contains `offline conversions <https://help.pinterest.com/en/business/article/upload-conversions-with-ads-manager>`__ |ext_link| to |destination-name|, after which |destination-name| will match campaigns to these conversions so your brand can review total conversions in |destination-name| as they relate to all active campaigns.

.. events-pinterest-overview-end

.. events-pinterest-overview-tip-start

.. tip:: Upload this CSV file at least once a month and send conversion data within 30 days of each conversion occurrence to |destination-name|. Keep the size of the CSV file under 5 GB with fewer than 10 million rows.

.. events-pinterest-overview-tip-end

.. caution:: This destination is available for sending events to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending events to |destination-name|.


.. _events-pinterest-build-query:

Build a query
==================================================

.. events-pinterest-build-query-start

Use a query to return the fields that align to the customer and event data fields supported by |destination-name| for use with `offline conversions <https://help.pinterest.com/en/business/article/upload-conversions-with-ads-manager>`__ |ext_link|.

For example:

.. code-block:: sql
   :linenos:

   SELECT
     mc.TO_HEX(SHA256(TO_UTF8(LOWER(TRIM(email))))) AS EMAIL
     TO_HEX(SHA256(TO_UTF8(LOWER(TRIM(mc.email))))) AS email
     ,ut.order_datetime AS event_time
     ,'checkout' AS event_type
     ,'offline' AS event_source
     ,ut.order_revenue AS value
     ,ut.order_id AS order_id
     ,ut.order_quantity AS quantity
   FROM Merged_Customers mc
   INNER JOIN Unified_Transactions ut
   ON mc.amperity_id = ut.amperity_id
   WHERE mc.email IS NOT NULL

You can download the results of this query directly from the **Query Editor** in Amperity or you can use an orchestration to send the CSV file to cloud storage or an SFTP bucket.

.. events-pinterest-build-query-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end
