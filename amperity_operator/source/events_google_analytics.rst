.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Analytics 4
.. |plugin-name| replace:: "Google Analytics 4"
.. |credential-type| replace:: "google-analytics-offline-events."
.. |required-credentials| replace:: "measurement ID" and "API secret"
.. |what-send| replace:: purchase events
.. |where-send| replace:: |destination-name|


.. meta::
    :description lang=en:
        Configure Amperity to send purchase events to Google Analytics 4.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send purchase events to Google Analytics 4.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure purchase events for Google Analytics 4

==================================================
Configure purchase events for Google Analytics 4
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-analytics-start
   :end-before: .. term-google-analytics-end

.. events-google-analytics-overview-start

A large percentage of retail sales take place in stores. By providing transactions data for sales that occurred in stores to |destination-name| your brand can use event-based tracking to measure user interactions and conversions.

Amperity uses the `Measurement Protocol API  <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=firebase>`__ |ext_link| to send events to |destination-name|. Use a query to map fields in the **Unified Transactions** and **Unified Itemized Transactions** tables to |destination-name| `purchase events parameters <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#purchase>`__ |ext_link|.

Use an orchestration to send purchase events parameters to |destination-name| from Amperity. Query results must include a **client_id** to ensure purchase events are associated with sessions in |destination-name|. Only purchase events that occurred within the previous 72 hours are sent to |destination-name|.

.. events-google-analytics-overview-end


.. _events-google-analytics-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-google-analytics-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Measurement ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-analytics-measurement-id-start
             :end-before: .. credential-google-analytics-measurement-id-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-analytics-measurement-id-howto-start
             :end-before: .. credential-google-analytics-measurement-id-howto-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **API secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-analytics-api-secret-start
             :end-before: .. credential-google-analytics-api-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-analytics-api-secret-howto-start
             :end-before: .. credential-google-analytics-api-secret-howto-end


.. events-google-analytics-get-details-table-end


.. _events-google-analytics-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Google Analytics 4 events**

.. events-google-analyticsr-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Measurement ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-analytics-measurement-id-start
             :end-before: .. credential-google-analytics-measurement-id-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-analytics-measurement-id-howto-start
             :end-before: .. credential-google-analytics-measurement-id-howto-end

       **API secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-analytics-api-secret-start
             :end-before: .. credential-google-analytics-api-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-google-analytics-api-secret-howto-start
             :end-before: .. credential-google-analytics-api-secret-howto-end

.. events-google-analytics-credentials-steps-end


.. _events-google-analytics-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-google-analytics-add-destination-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       Enter the name of the destination and a description. For example: "|destination-name| events" and "Send events to |destination-name|.".


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. events-google-analytics-add-destination-end


.. _events-google-analytics-build-query:

Build a query
==================================================

.. events-google-analytics-build-query-start

Information for the query that sends purchase events data to |destination-name| is likely found in three tables in your customer 360 database:

#. **Unified Transactions** has transaction-level purchase events data.
#. **Unified Itemized Transactions** has item-level purchase events data.
#. A table with unique identifiers from |destination-name|. The following example uses a table named **Google_Analytics** as the source for specific events data points required by |destination-name|.

   .. admonition:: How to build a Google Analytics table in a customer 360 database

      |destination-name| data should not be made available to Stitch, but must be available from the customer 360 database before purchase events data can be sent to |destination-name|.

      #. Configure a data source for |destination-name| data.

      #. Build a custom SQL table in your customer 360 database for |destination-name| database data.

      #. Use a **SELECT** statement and a common table expression to select columns from the |destination-name| source table. The **USER_PSEUDO_ID**, **TRANSACTION_ID**, **USER_ID** columns must be selected, along with a column with a unique value that matches a unique value in a table evaluated by Stitch and in which rows are assigned an Amperity ID.

      #. Use use an **INNER JOIN** to add the Amperity ID to rows in the |destination-name| database table using the shared unique identifier as the join key.

      For example:

      .. code-block:: sql
         :linenos:
         :emphasize-lines: 11

         WITH ranked AS (
           SELECT
             cp.amperity_id
             ,ga.*
             ,ROW_NUMBER() OVER (
               PARTITION BY cp.amperity_id
               ORDER BY ga.LAST_MODIFIED_TIMESTAMP DESC
             ) AS row_number
           FROM GA4_SOURCE_TABLE AS ga
           INNER JOIN Customer_Profiles_Table AS cp
           ON cp.CUSTOMER_ID = ga.CUSTOMER_ID
         )

         SELECT *
         FROM ranked
         WHERE row_number = 1

      Replace the names of the **CUSTOMER_ID** fields within the **INNER JOIN** with the real column names in your database.

**Example: Return results for purchase events**

The following SQL example shows how to return purchase events data from three tables and combine them into a single results set that is mapped to the event names required by |destination-name|.

.. code-block:: sql
   :linenos:

   WITH Unified_Transactions_Mapped AS (
     SELECT
       amperity_id
       ,Currency AS currency
       ,Store_ID AS location_id
       ,Order_Shipping_Amount AS shipping
       ,Order_Tax_Amount AS tax
       ,Order_Datetime AS timestamp
       ,Coupon_Code AS coupon
       ,CASE
         WHEN DATE_DIFF('day', DATE(Order_Datetime), CURRENT_DATE) >= 540 THEN 'new'
         ELSE 'returning'
       END AS customer_type
     FROM Unified_Transactions
   ),
   Unified_Itemized_Transactions_Mapped AS (
     SELECT
       amperity_id
       ,Item_Discount_Amount AS discount
       ,Purchase_Brand AS item_brand
       ,Product_Category AS item_category
       ,Product_ID AS item_id
       ,Product_Name AS item_name
       ,Item_List_Price AS price
       ,Item_Quantity AS quantity
     FROM Unified_Itemized_Transactions
   )

   SELECT
     ut.amperity_id
     ,ga.USER_PSEUDO_ID AS client_id
     ,ga.TRANSACTION_ID AS transaction_id
     ,ga.USER_ID AS user_id
     ,ut.currency
     ,ut.location_id
     ,ut.shipping
     ,ut.tax
     ,ut.timestamp
     ,ut.coupon
     ,ut.customer_type
     ,uit.discount
     ,uit.item_brand
     ,uit.item_category
     ,uit.item_id
     ,uit.item_name
     ,uit.price
     ,uit.quantity
   FROM Unified_Transactions_Mapped ut
   LEFT JOIN Unified_Itemized_Transactions_Mapped uit ON ut.amperity_id = uit.amperity_id
   LEFT JOIN Google_Analytics ga ON ut.amperity_id = ga.amperity_id

Extend the SQL to include :ref:`any of the additional fields <events-google-analytics-event-parameters>` that are accepted by |destination-name|.

Use an orchestration to send purchase events data to |destination-name|.

.. caution:: The SQL that your brand requires may be different, depending on which table is the source for unique identifiers from |destination-name|.

.. events-google-analytics-build-query-end


.. _events-google-analytics-event-parameters:

GA4 events parameters
==================================================

.. events-google-analytics-event-parameters-start

The following table describes each of the purchase events parameters that are supported by |destination-name|. Use a query to map fields in the **Unified Transactions** and **Unified Itemized Transactions** tables to `purchase events parameters <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#purchase>`__ |ext_link|.

The following |destination-name| purchase events parameters must be returned by the query: **client_id**, **currency**, **item_id**, **item_name**, **price**, and **transaction_id**.

All fields, including optional fields, are listed alphabetically, but may be returned by a query in any order.

.. events-google-analytics-event-parameters-end

.. events-google-analytics-event-parameters-table-start

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field name
     - Description

   * - **affiliation**
     - **Optional**

       A product affiliation, such as a supplying company or a brick-and-mortar store location. Applies only to individual items within a transaction and is part of the **items** array.


   * - **client_id**
     - **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-google-analytics-start
          :end-before: .. term-google-analytics-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-client-id-ga4-start
          :end-before: .. term-client-id-ga4-end

       The **client_id** is required to associate purchase events with existing sessions of |destination-name|. Must be a non-empty string. For example: ``310123456.1739876543``.


   * - **coupon**
     - **Optional**

       A coupon name or coupon code associated with item-specific purchase events. Applies only to individual items within a transaction and is part of the **items** array.


   * - **currency**
     - **Required**

       A three character alphabetic |ext_iso_4217| currency code. For example: "USD", "JPY", "EUR", or "GBP".


   * - **customer_type**
     - **Optional**

       Indicates a new or returning known customer. A new known customer hasn't purchased within a given time window. A returning known customer has purchased within a given time window.

       The values for **customer_type** must be "new" or "returning". |destination-name| uses 540 days as the default window.

       .. important:: If the customer is unknown leave the value blank. For example, when the customer checks out as a guest.


   * - **discount**
     - **Optional**

       The item-level discount. Applies only to individual items within a transaction and is part of the **items** array.


   * - **item_brand**
     - **Optional**

       The brand for an item. Applies only to individual items within a transaction and is part of the **items** array.


   * - **item_category**
     - **Optional**

       A series of event parameters that describe the item using your brand's product catalog taxonomy. Use **item_category** for the first level within a product catalog taxonomy. Applies only to individual items within a transaction and is part of the **items** array.

       * Use **item_category2** for second level within a product catalog taxonomy.
       * Use **item_category3** for third level within a product catalog taxonomy.
       * Use **item_category4** for fourth level within a product catalog taxonomy.
       * Use **item_category5** for fifth level within a product catalog taxonomy.


   * - **item_id**
     - **Required**

       A unique ID for an item, such as a stock keeping unit (SKU). Applies only to individual items within a transaction and is part of the **items** array.


   * - **item_name**
     - **Required**

       The name of an item. Applies only to individual items within a transaction and is part of the **items** array.


   * - **items**
     - **Required**

       An array of item-level details for a transaction, including **affiliation**, **coupon**, **discount**, **index**, **item_brand**, **item_category fields**, **item_id**, **item_list_id**, **item_list_name**, **item_name**, **item_variant**, **location_id**, **price**, and **quantity**.


   * - **location_id**
     - **Optional**

       The physical location of the store at which the transaction occurred. Applies only to individual items within a transaction and is part of the **items** array.

       `Google place IDs <https://developers.google.com/maps/documentation/places/web-service/place-id>`__ |ext_link| uniquely identify physical locations in Google Places and Google Maps. Place IDs can be mapped to physical store locations. For example: "ChIJEw2sg_lAkFQR25Oh_sq8qRY".


   * - **price**
     - **Required**

       The unit price of an item. Applies only to individual items within a transaction and is part of the **items** array.

       .. note:: Use the **discount** purchase events parameter for discounts to the unit price.


   * - **quantity**
     - **Required**

       The quantity of items purchased. If a quantity is not specified the quantity is "1". Applies only to individual items within a transaction.


   * - **shipping**
     - **Optional**

       The shipping cost for a transaction.


   * - **tax**
     - **Optional**

       The cost for taxes associated with a transaction.


   * - **timestamp**
     - **Recommended**

       An |ext_iso_8601| timestamp of when the purchase event occurred. For example: "2025-01-12T14:21:56.000Z".

       .. important:: The timestamp must be within 72 hours of sending to |destination-name|. The current time is used when the value for **timestamp** is not provided. Events that occurred outside of the 72 hour window are not sent.


   * - **transaction_id**
     - **Required**

       A unique identifier within |destination-name| data for a transaction. For example: ``316123456``.


   * - **user_id**
     - **Recommended**

       A unique user identifier within |destination-name| that links events to known users. Must be a non-empty string. For example: ``12345678``.


   * - **value**
     - **Required**

       The monetary value of the event.

       .. important:: Amperity calculates the total **value** for a transaction using the **price** and **quantity** purchase events paramaters. **value** is the sum of the price and quantity for all items purchased in a single transaction, not including shipping costs or taxes.

.. events-google-analytics-event-parameters-table-end


.. _events-google-analytics-event-map-parameters:

Map Amperity attributes to GA4 events parameters
==================================================

.. events-google-analytics-event-map-parameters-start

The following table describes how to map `purchase events parameters <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#purchase>`__ |ext_link| that are supported by |destination-name| to attribues in Amperity standard output.

All fields, including optional fields, are listed alphabetically, but may be returned by a query in any order.

.. events-google-analytics-event-map-parameters-end

.. events-google-analytics-event-map-parameters-table-start

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - GA4 event parameter
     - Amperity attribute

   * - **affiliation**
     - Varies.

       A product affiliation, such as a supplying company or a brick-and-mortar store location. Applies only to individual items within a transaction and is part of the **items** array.

       Use the **Store ID** field in the **Unified Transactions** table when the value for **location_id** is a `Google Place ID <https://developers.google.com/maps/documentation/places/web-service/place-id>`__ |ext_link|.


   * - **client_id**
     - **USER_PSEUDO_ID**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-google-analytics-start
          :end-before: .. term-google-analytics-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-client-id-ga4-start
          :end-before: .. term-client-id-ga4-end

       The **client_id** is required to associate events with existing sessions of |destination-name|. Must be a non-empty numeric string. For example: ``310123456.1739876543``.

       The source for **client_id** is a table in your customer 360 database with |destination-name| data that has been evaluated by Stitch and has rows of data assigned an Amperity ID. The client ID is available from a field named **USER_PSEUDO_ID**.


   * - **coupon**
     - Varies.

       A coupon name or coupon code associated with item-specific purchase events.

       The source for **coupon** is a table in your customer 360 database with the coupon name or coupon code.


   * - **currency**
     - **Currency**

       |destination-name| requires the value for currency to be a three character alphabetic |ext_iso_4217| currency code. For example: "USD", "JPY", "EUR", or "GBP".

       Use the **Currency** field in the **Unified Itemized Transactions** table when its values are three character alphabetic ISO 4217 currency codes.


   * - **customer_type**
     - **Customer Type** (custom field)

       Indicates a new or returning known customer. A new known customer hasn't purchased within a given time window. A returning known customer has purchased within a given time window.

       The values for **customer_type** must be "new" or "returning". |destination-name| uses 540 days as the default window.

       Use the **Latest Order Datetime** field in the **Unified Transactions** table to identify customers who have or have not purchased within a given time window. Define the time window, and then return customers who have purchased as "returning" and customers who have not as "new".

       .. important:: If the customer is unknown leave the value blank. For example, when the customer checks out as a guest.


   * - **discount**
     - **Item Discount Amount**

       The item-level discount. Applies only to individual items within a transaction and is part of the **items** array.

       Use the **Item Discount Amount** field in the **Unified Itemized Transactions** table.


   * - **item_brand**
     - **Purchase Brand**

       The brand for an item. Applies only to individual items within a transaction and is part of the **items** array.

       Use the **Purchase Brand** field in the **Unified Itemized Transactions** table.


   * - **item_category**
     - **Product Category**

       A series of event parameters that describe the item using your brand's product catalog taxonomy. Use **item_category** for the first level within a product catalog taxonomy. Applies only to individual items within a transaction and is part of the **items** array.

       * Use **item_category2** for second level within a product catalog taxonomy.
       * Use **item_category3** for third level within a product catalog taxonomy.
       * Use **item_category4** for fourth level within a product catalog taxonomy.
       * Use **item_category5** for fifth level within a product catalog taxonomy.

       Use the **Product Category** field in the **Unified Itemized Transactions** table for the first level, along with other levels from the same table if they are available.


   * - **item_id**
     - **Product ID**

       A unique ID for an item, such as a stock keeping unit (SKU). Applies only to individual items within a transaction and is part of the **items** array.

       Use the **Product ID** field in the **Unified Itemized Transactions** table.


   * - **item_name**
     - **Product Name**

       The name of an item. Applies only to individual items within a transaction and is part of the **items** array.

       Use the **Product Name** field in the **Unified Itemized Transactions** table.


   * - **location_id**
     - **Place ID** or **Store ID**

       The physical location of the store at which the transaction occurred. Applies only to individual items within a transaction and is part of the **items** array.

       Use `Google place IDs <https://developers.google.com/maps/documentation/places/web-service/place-id>`__ |ext_link| if your brand has mapped physical store locations to place IDs and has made that data available to your customer 360 database in Amperity. For example: "ChIJEw2sg_lAkFQR25Oh_sq8qRY".

       Use the **Store ID** field in the **Unified Transactions** table if place IDs are unavailable.


   * - **price**
     - **Item List Price**

       The unit price of an item. Applies only to individual items within a transaction and is part of the **items** array.

       .. note:: Use the **discount** purchase events parameter for discounts to the unit price.

       Use the **Item List Price** field in the **Unified Itemized Transactions** table.


   * - **quantity**
     - **Item Quantity**

       The quantity of items purchased. If a quantity is not specified the quantity is "1". Applies only to individual items within a transaction.

       Use the **Item Quantity** field in the **Unified Itemized Transactions** table.


   * - **shipping**
     - **Order Shipping Amount**

       The shipping cost for a transaction.

       Use the **Order Shipping Amount** field in the **Unified Transactions** table.


   * - **tax**
     - **Order Tax Amount**

       The cost for taxes associated with a transaction.

       Use the **Order Tax Amount** field in the **Unified Transactions** table.


   * - **timestamp**
     - **Order Datetime**

       An |ext_iso_8601| timestamp of when the purchase event occurred. For example: "2025-01-12T14:21:56.000Z".

       .. important:: The timestamp must be within 72 hours of sending to |destination-name|. The current time is used when the value for **timestamp** is not provided. Events that occurred outside of the 72 hour window are not sent.

       Use the **Order Datetime** field in the **Unified Transactions** table.


   * - **transaction_id**
     - **TRANSACTION_ID**

       A unique identifier within |destination-name| data for a transaction. For example: ``316123456``.

       The **transaction_id** is required for deduplicating purchase events and must be a non-empty numeric string.

       The source for **transaction_id** is a table in your customer 360 database with |destination-name| data that has been evaluated by Stitch and has rows of data assigned an Amperity ID. The transaction ID is available from a field named **TRANSACTION_ID**.


   * - **user_id**
     - **USER_ID**

       A unique user identifier within |destination-name| that links events to known users. Must be a non-empty string. For example: ``12345678``.

       The source for **user_id** is a table in your customer 360 database with |destination-name| data that has been evaluated by Stitch and has rows of data assigned an Amperity ID. The user ID is available from a field named **USER_ID**.

.. events-google-analytics-event-map-parameters-table-end
