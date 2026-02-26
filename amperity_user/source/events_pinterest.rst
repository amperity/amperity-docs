.. https://docs.amperity.com/user/


.. |destination-name| replace:: Pinterest Ads Manager
.. |what-send| replace:: offline conversion events
.. |where-send| replace:: |destination-name|
.. |what-enable| replace:: **timestamp**, **currency**, **email** or **phone**, and **value**
.. |allow-for-what| replace:: offline conversion events
.. |allow-for-duration| replace:: up to 48 hours for deduplication of events
.. |attributes-sent| replace:: |destination-name| requires the **timestamp**, **currency**, **email**, **value**, **order_id**, **extern_id**, **content_name**, **content_category**, **content_brand**, **item_name**, **item_category**, **item_brand**, **opt_out_typev, and **opt_out** attributes are optional.


.. meta::
    :description lang=en:
        Send offline conversion events from Amperity to Pinterest.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send offline conversion events from Amperity to Pinterest.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline conversion events to Pinterest

==================================================
Send offline conversion events to Pinterest
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pinterest-start
   :end-before: .. term-pinterest-end

.. include:: ../../amperity_operator/source/events_pinterest.rst
   :start-after: .. events-pinterest-offline-events-overview-start
   :end-before: .. events-pinterest-offline-events-overview-end

.. include:: ../../amperity_operator/source/events_pinterest.rst
   :start-after: .. events-pinterest-offline-events-allowfor-start
   :end-before: .. events-pinterest-offline-events-allowfor-end


.. _events-pinterest-build-query:

Build a query
==================================================

.. include:: ../../amperity_operator/source/events_pinterest.rst
   :start-after: .. events-pinterest-offline-events-offline-events-build-query-start
   :end-before: .. events-pinterest-offline-events-offline-events-build-query-end

.. include:: ../../amperity_operator/source/events_pinterest.rst
   :start-after: .. events-pinterest-offline-events-offline-events-build-query-required-start
   :end-before: .. events-pinterest-offline-events-offline-events-build-query-required-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-pinterest-events-query-must-return-start
   :end-before: .. setting-pinterest-events-query-must-return-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-pinterest-events-query-should-return-start
   :end-before: .. setting-pinterest-events-query-should-return-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-pinterest-events-query-automatic-return-start
      :end-before: .. setting-pinterest-events-query-automatic-return-end


.. _events-pinterest-offline-events-query-orders:

Order-level events
--------------------------------------------------

.. include:: ../../amperity_operator/source/events_pinterest.rst
   :start-after: .. events-pinterest-offline-events-build-query-orders-start
   :end-before: .. events-pinterest-offline-events-build-query-orders-end


.. _events-pinterest-offline-events-build-query-items:

Item-level events
--------------------------------------------------

.. include:: ../../amperity_operator/source/events_pinterest.rst
   :start-after: .. events-pinterest-offline-events-build-query-items-start
   :end-before: .. events-pinterest-offline-events-build-query-items-end


.. _events-pinterest-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. admonition:: What is a dataset ID?

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-meta-ads-manager-dataset-id-start
      :end-before: .. setting-meta-ads-manager-dataset-id-end

   A dataset ID may need to be configured for the orchestration.

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _events-pinterest-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _events-pinterest-offline-events-conversions:

Offline events parameters
==================================================

.. include:: ../../amperity_operator/source/events_pinterest.rst
   :start-after: .. events-pinterest-offline-events-conversion-api-parameters-start
   :end-before: .. events-pinterest-offline-events-conversion-api-parameters-end


.. _events-pinterest-upload-csv:

Upload a CSV file
==================================================

.. events-pinterest-upload-csv-note-start

.. note:: This is an alternate way to upload offline conversion events to |destination-name|.

.. events-pinterest-upload-csv-start

Upload a CSV file that contains `offline conversion events <https://help.pinterest.com/en/business/article/upload-conversions-with-ads-manager>`__ |ext_link| to |destination-name|, after which |destination-name| will match campaigns to these conversions so your brand can review total conversions in |destination-name| as they relate to all active campaigns.

.. events-pinterest-upload-csv-end

.. events-pinterest-upload-csv-tip-start

.. tip:: Upload this CSV file at least once a month and send conversion data within 30 days of each conversion occurrence to |destination-name|. Keep the size of the CSV file under 5 GB with fewer than 10 million rows.

.. events-pinterest-upload-csv-tip-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _events-pinterest-build-query-for-csv-upload:

Build a query for CSV file uploads
--------------------------------------------------

.. events-pinterest-upload-csv-start

Use a query to return the fields that align to the customer and event data fields supported by |destination-name| for use with `offline conversions <https://help.pinterest.com/en/business/article/upload-conversions-with-ads-manager>`__ |ext_link|.

For example:

.. code-block:: sql
   :linenos:

   SELECT
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

You can download the results of this query directly from the **Query Editor** in Amperity or you can use an orchestration to send the CSV file to cloud storage or any SFTP site.

.. events-pinterest-upload-csv-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end
