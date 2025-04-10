.. https://docs.amperity.com/ampiq/


.. |destination-name| replace:: Google Enhanced Conversions
.. |what-send| replace:: first-party customer data that is associated with transactions
.. |what-enablex| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires first-party data that is associated with transactions.


.. meta::
    :description lang=en:
        Configure Amperity to send offline events to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send offline events to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline events to Google Enhanced Conversions

==================================================
Send offline events to Google Enhanced Conversions
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-enhanced-conversions-start
   :end-before: .. term-google-enhanced-conversions-end

.. include:: ../../amperity_datagrid/source/events_google_enhanced_conversions.rst
   :start-after: .. destination-google-enhanced-conversions-about-start
   :end-before: .. destination-google-enhanced-conversions-about-end


.. _events-google-enhanced-conversions-build-query:

Build a query
==================================================

.. events-google-enhanced-conversions-build-query-start

After the destination is configured, use a query to collect first-party data that is associated with transactions. Use SHA-256 hashing for all customer profile fields that are returned by the query.

For example:

.. code-block:: sql

   SELECT
     SHA256(c.email) AS Email,
     SHA256(c.phone) AS Phone,
     SHA256(c.given_name) AS FirstName,
     SHA256(c.surname) AS LastName
   FROM Customer_360 c
   JOIN Unified_Transactions t ON c.amperity_id = t.amperity_id
   WHERE t.order_datetime >= DATE_ADD('day', -30, CURRENT_DATE)

.. events-google-enhanced-conversions-build-query-end
