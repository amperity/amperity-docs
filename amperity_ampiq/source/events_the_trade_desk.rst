.. https://docs.amperity.com/ampiq/


.. |destination-name| replace:: The Trade Desk
.. |what-send| replace:: email address lists
.. |what-enable| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires only email addresses. There are no optional fields.
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Send offline events from Amperity to The Trade Desk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send offline events from Amperity to The Trade Desk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline events to The Trade Desk

==================================================
Send offline events to The Trade Desk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. events-the-trade-desk-overview-start

`Offline conversion events <https://partner.thetradedesk.com/v3/portal/data/doc/DataOfflineMeasurement>`__ |ext_link| help your brand track offline conversions---for in-store sales, place visits, and other events---for your marketing campaigns. Send offline measurement data to |destination-name|, and then use that data for attribution and targeting.

.. events-the-trade-desk-overview-end

.. _events-the-trade-desk-build-segment:

Build a query
==================================================

.. events-the-trade-desk-offline-events-build-query-start

Use a query to build a combinations of data from your **Customer 360** database tables that best represent the set of offline events that your brand wants to use within |destination-name|.

.. events-the-trade-desk-offline-events-build-query-end

.. events-the-trade-desk-offline-events-build-query-tip-start

.. tip:: Send offline events to |destination-name| as soon as possible, ideally, within 1 to 3 days of the transaction date and avoid sending data older than 25 days.

.. events-the-trade-desk-offline-events-build-query-tip-end

.. events-the-trade-desk-offline-events-build-query-example-start

You can send offline events to |destination-name| to support your brand's use cases.

A query that returns a collection offline event is similar to:

.. code-block:: sql

   SELECT 
     c360.amperity_id
     ,c360.email AS email
     ,uit.order_datetime AS timestamp
   FROM Unified_Itemized_Transactions uit
   LEFT JOIN Customer_360 c360 ON uit.amperity_id = c360.amperity_id
   WHERE uit.order_datetime > (CURRENT_DATE - interval '25' day)
   GROUP BY amperity_id

The query **MUST** contain the following fields: **email** and **timestamp**.

.. tip:: You may use **uid2** as an attribute when Amperity is configured as a `UID2 Operator <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| for your brand. For example:

   .. code-block:: sql

      SELECT 
        uid2.uid2
        ,uit.order_datetime AS timestamp
      FROM Unified_Itemized_Transactions uit
      LEFT JOIN UID2 uid2 ON uit.amperity_id = uid2.uid2
      WHERE uit.order_datetime > (CURRENT_DATE - interval '25' day)

.. caution:: Review the list of offline events parameters that may be sent to |destination-name|. Compare these parameters to the fields that are available from your brand's customer 360 database to determine which fields are available to be sent to |destination-name|.

   Some parameters, such as **city**, **region** (which represents a state within the United States), and **country**, must be associated with the location in which the offline event occurred, not the location at which the customer associated with the offline event resides.

   The **eventname** parameter provides a list of options defined by |destination-name|. Your brand must choose one of the defined options.

.. events-the-trade-desk-offline-events-build-query-retail-end


.. _events-the-trade-desk-parameters:

Offline events paramaters
==================================================

.. include:: ../../amperity_datagrid/source/events_the_trade_desk.rst
   :start-after: .. events-the-trade-desk-parameters-offline-start
   :end-before: .. events-the-trade-desk-parameters-offline-end
