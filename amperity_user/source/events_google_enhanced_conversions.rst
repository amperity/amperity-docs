.. https://docs.amperity.com/user/


.. |destination-name| replace:: Google Enhanced Conversions
.. |what-send| replace:: first-party customer data associated with transactions
.. |what-enablex| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires first-party data that is associated with transactions.


.. meta::
    :description lang=en:
        Send online events from Amperity to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send online events from Amperity to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send online events to Google Enhanced Conversions

=================================================
Send online events to Google Enhanced Conversions
=================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-enhanced-conversions-start
   :end-before: .. term-google-enhanced-conversions-end

.. include:: ../../amperity_operator/source/events_google_enhanced_conversions.rst
   :start-after: .. events-google-enhanced-conversions-about-start
   :end-before: .. events-google-enhanced-conversions-about-end

.. include:: ../../amperity_operator/source/events_google_enhanced_conversions.rst
   :start-after: .. events-google-enhanced-conversions-offline-start
   :end-before: .. events-google-enhanced-conversions-offline-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _events-google-enhanced-conversions-build-query:

Build a query
==================================================

.. events-google-enhanced-conversions-build-query-start

After the destination is configured, use a query to collect first-party data that is associated with transactions. Use SHA-256 hashing for all customer profile fields that are returned by the query.

For example:

.. code-block:: sql
   :linenos:

   SELECT
     SHA256(c.email) AS Email,
     SHA256(c.phone) AS Phone,
     SHA256(c.given_name) AS FirstName,
     SHA256(c.surname) AS LastName
   FROM Customer_360 c
   JOIN Unified_Transactions t ON c.amperity_id = t.amperity_id
   WHERE t.order_datetime >= DATE_ADD('day', -30, CURRENT_DATE)

Extend the SQL to include :ref:`any of the additional fields <events-google-enhanced-conversions-fields>` that are accepted by |destination-name|.

.. events-google-enhanced-conversions-build-query-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end

.. _events-google-enhanced-conversions-fields:

Fields for enhanced conversions
==================================================

.. include:: ../../amperity_operator/source/events_google_enhanced_conversions.rst
   :start-after: .. events-google-enhanced-conversions-fields-start
   :end-before: .. events-google-enhanced-conversions-fields-end

.. include:: ../../amperity_operator/source/events_google_enhanced_conversions.rst
   :start-after: .. events-google-enhanced-conversions-fields-table-start
   :end-before: .. events-google-enhanced-conversions-fields-table-end
