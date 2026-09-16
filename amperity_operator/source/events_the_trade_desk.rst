.. https://docs.amperity.com/operator/


.. |destination-name| replace:: The Trade Desk Events
.. |destination-api| replace:: The Trade Desk API
.. |plugin-name| replace:: "The Trade Desk"
.. |credential-type| replace:: "tradedesk"
.. |required-credentials| replace:: "advertiser ID" and "advertiser secret"
.. |what-send| replace:: events
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "180"
.. |filter-the-list| replace:: "trade"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours

.. meta::
    :description lang=en:
        Configure Amperity to send events to The Trade Desk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send events to The Trade Desk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configire events for The Trade Desk

==================================================
Configure events for The Trade Desk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. TODO: Sync this with ampiq/events_the_trade_desk

.. events-the-trade-desk-about-start

Use this destination to send offline measurement data to The Trade Desk, and then use that data for attribution and targeting.

Events help your brand track offline conversions--in-store sales, place visits, and other events--as they relate to your brand's marketing campaigns. Send offline measurement data to |destination-name|, and then use that data for attribution and targeting.

.. tip:: Send events to |destination-name| as soon as possible, ideally, within 1 to 3 days of the transaction date and avoid sending data older than 25 days.

.. events-the-trade-desk-about-end

.. events-the-trade-desk-api-note-start

.. note:: This destination uses the `POST /providerapi/offlineconversion endpoint <https://partner.thetradedesk.com/v3/portal/data/doc/post-providerapi-offlineconversion>`__ |ext_link| for the Data Integration API to manage events.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. events-the-trade-desk-api-note-end


.. _events-the-trade-desk-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-the-trade-desk-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - A `UID 2.0 agreement <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| and / or a `European Unified ID (EUID) agreement <https://docs.amperity.com/reference/euid.html>`__ |ext_link|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Advertiser ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-advertiser-id-start
             :end-before: .. credential-the-trade-desk-advertiser-id-end

       **Advertiser secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-advertiser-secret-start
             :end-before: .. credential-the-trade-desk-advertiser-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-find-id-and-secret-start
             :end-before: .. credential-the-trade-desk-find-id-and-secret-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Offline Data Provider ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-data-provider-id-start
             :end-before: .. setting-the-trade-desk-offline-data-provider-id-end

       **Merchant ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-merchant-id-start
             :end-before: .. setting-the-trade-desk-offline-merchant-id-end

       .. note:: 

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-merchant-versus-offline-start
             :end-before: .. setting-the-trade-desk-offline-merchant-versus-offline-end

       **Tracking tag name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-tracking-tag-name-start
             :end-before: .. setting-the-trade-desk-offline-tracking-tag-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-tracking-tag-name-context-start
             :end-before: .. setting-the-trade-desk-offline-tracking-tag-name-context-end

.. events-the-trade-desk-get-details-end


.. _events-the-trade-desk-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for The Trade Desk**

.. events-the-trade-desk-credentials-steps-start

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

       **Name and description**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-common-name-and-description-start
             :end-before: .. credential-common-name-and-description-end

       **Advertiser ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-advertiser-id-start
             :end-before: .. credential-the-trade-desk-advertiser-id-end

       **Advertiser secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-advertiser-secret-start
             :end-before: .. credential-the-trade-desk-advertiser-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-find-id-and-secret-start
             :end-before: .. credential-the-trade-desk-find-id-and-secret-end

.. events-the-trade-desk-credentials-steps-end


.. _events-the-trade-desk-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for The Trade Desk**

.. events-the-trade-desk-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


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

       **Name and description**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-name-and-description-start
             :end-before: .. setting-common-name-and-description-end

       **Business user access**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-start
             :end-before: .. setting-common-membership-duration-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-membership-duration-minmax-start
             :end-before: .. setting-the-trade-desk-membership-duration-minmax-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-membership-duration-example-start
             :end-before: .. setting-the-trade-desk-membership-duration-example-end

       **Offline Data Provider ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-data-provider-id-start
             :end-before: .. setting-the-trade-desk-offline-data-provider-id-end

       **Merchant ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-merchant-id-start
             :end-before: .. setting-the-trade-desk-offline-merchant-id-end

       .. note:: 

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-merchant-versus-offline-start
             :end-before: .. setting-the-trade-desk-offline-merchant-versus-offline-end

       **Tracking tag name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-tracking-tag-name-start
             :end-before: .. setting-the-trade-desk-offline-tracking-tag-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-offline-tracking-tag-name-context-start
             :end-before: .. setting-the-trade-desk-offline-tracking-tag-name-context-end


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


.. events-the-trade-desk-add-steps-end


.. _events-the-trade-desk-build-segment:

Build a query
==================================================

.. events-the-trade-desk-offline-events-build-query-start

Use a query to build a combinations of data from your **Customer 360** database tables that best represent the set of events that your brand wants to use within |destination-name|.

.. events-the-trade-desk-offline-events-build-query-end

.. events-the-trade-desk-offline-events-build-query-tip-start

.. tip:: Send events to |destination-name| as soon as possible, ideally, within 1 to 3 days of the transaction date and avoid sending data older than 25 days.

.. events-the-trade-desk-offline-events-build-query-tip-end

.. events-the-trade-desk-offline-events-build-query-example-start

You can send events to |destination-name| to support your brand's use cases.

A query that returns a collection offline event is similar to:

.. code-block:: sql
   :linenos:

   SELECT 
     c360.amperity_id
     ,c360.email AS email
     ,uit.order_datetime AS timestamp
   FROM Unified_Itemized_Transactions uit
   LEFT JOIN Customer_360 c360 ON uit.amperity_id = c360.amperity_id
   WHERE uit.order_datetime > (CURRENT_DATE - interval '25' day)
   GROUP BY amperity_id

The query **MUST** contain **timestamp** and at least one of **email** or **phone**.

.. tip:: You may use **phone** as an alternative to **email**. When both are present in the same row, Amperity generates a separate event for each identifier.

.. tip:: You may use **uid2** as an attribute when Amperity is configured as a `UID2 Operator <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| for your brand. A `UID2 table <../reference/uid2.html#add-uid2-table-to-database>`__ must be configured in your customer 360 database.

   For example:

   .. code-block:: sql
      :linenos:

      SELECT 
        uid2.uid2
        ,uit.order_datetime AS timestamp
      FROM Unified_Itemized_Transactions uit
      LEFT JOIN Customer_360 c360 ON uit.amperity_id = c360.amperity_id
      LEFT JOIN (
        SELECT DISTINCT normalized_email, uid2
        FROM UID2
      ) uid2 ON LOWER(c360.email) = uid2.normalized_email


   You may use **euid** as a source attribute when your brand is a participant in `European Unified ID (EUID) <https://docs.amperity.com/reference/euid.html>`__ |ext_link|.

.. caution:: Review the list of events parameters that may be sent to |destination-name|. Compare these parameters to the fields that are available from your brand's customer 360 database to determine which fields are available to be sent to |destination-name|.

   Some parameters, such as **city**, **region**, which represents a state within the United States, and **country**, must be associated with the location in which the offline event occurred, not the location at which the customer associated with the offline event resides.

   The **eventname** parameter provides a list of options defined by |destination-name|. Your brand must choose one of the defined options.

.. events-the-trade-desk-offline-events-build-query-retail-end


.. _events-the-trade-desk-parameters-offline:

Events paramaters
==================================================

.. events-the-trade-desk-parameters-offline-start

The following table describes each of the parameters that are required by |destination-name| for events. The **TD1** - **TD10** fields represent the optional fields your brand may include to extend customer profiles to include events.

The fields are listed alphabetically, but may be returned by the query in any order.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field name
     - Description

   * - **cat**
     - **Optional**, but **Recommended** when transaction details are included with events. See **item_code**, **price**, and **qty**.

       The name of a product in your product catalog.

       This value is most often associated with the **Product Category** field in the **Unified Itemized Transactions** table. Include **product_category** in the **SELECT** statement.

       For example:

       .. code-block:: sql

          ,product_category


   * - **city**
     - **Optional**

       The name of the city in which the offline event occurred.


   * - **country**
     - **Optional**

       The three-letter country code for the country in which the offline event occurred.

       .. note:: Events should only be sent to |destination-name| when they occurred within the United States.

          Use a **WHERE** clause to limit query results to only events that occurred within the United States.

          .. code-block:: sql

             WHERE country = 'USA'

       .. important:: When **country** is included in offline results, **region** must also be included.


   * - **email**
     - **Required** unless **phone** is provided.

       The email address that is associated with the offline event.

       .. note:: Amperity converts email addresses to a UID 2.0 value, and then sends them to |destination-name|, after which they are available from within |destination-name| as a **UID2** or **EUID** ID type. Rows without a valid UID 2.0 value or with an empty value are removed by Amperity before sending.

   * - **euid**
     - **Optional**

       You may use **euid** as an attribute when is a participant in `European Unified ID (EUID) <https://docs.amperity.com/reference/euid.html>`__ |ext_link|.

       For example:

       .. code-block:: sql

          SELECT 
            euid.euid
            ,uit.order_datetime AS timestamp
          FROM Unified_Itemized_Transactions uit
          LEFT JOIN EUID euid ON uit.amperity_id = euid.euid
          WHERE uit.order_datetime > (CURRENT_DATE - interval '25' day)


   * - **eventname**
     - **Optional**, but **Required** for sending product catalogs alongside events.

       An event name groups your brand's events a specific category type for events as defined by |destination-name|.

       The event name that most frequently is associated with events for retail transactions is "purchase", but the event name may be any of the event names that are described in the following table:

       .. list-table::
          :widths: 25 75
          :header-rows: 0

          * - **addtocart**
            - A user added an item to the shopping cart.

          * - **direction**
            - A user requested and received directions to a physical location for your brand.

          * - **login**
            - A user logged in to a site

          * - **messagebusiness**
            - A user sent a message to your brand using a form or email.

          * - **purchase**
            - Default. A user completed a purchase.

              .. tip:: Recommended for *all* retail events.

          * - **searchcategory**
            - A user searched for a category

          * - **searchitem**
            - A user searched for an item.

          * - **sitevisit**
            - A user visited a website.

          * - **startcheckout**
            - A user started the checkout process.

          * - **viewcart**
            - A user viewed the contents of their cart.

          * - **viewitem**
            - A user viewed an item.

          * - **wishlistitem**
            - A user added an item to a wish list.


   * - **item_code**
     - **Optional**, but **Required** when transaction details are included with events. See **cat**, **price**, and **qty**.

       The unique identifier for a product in your brand's product catalog.

       This value is most often associated with the **Product ID** field in the **Unified Itemized Transactions** table. Include **product_id** in the **SELECT** statement.

       For example:

       .. code-block:: sql

          ,product_id



   * - **orderid**
     - **Recommended**

       A unique identifier for the transaction. The value for this field is a string with a maximum of 64 characters.

       .. note:: This field should be included with events to help |destination-name| deduplicate conversion events.

       This value is most often associated with the **Order ID** field in the **Unified Transactions** table. Include **order_id** in the **SELECT** statement.

       For example:

       .. code-block:: sql

          ,order_id


   * - **phone**
     - **Required** unless **email** is provided.

       The phone number associated with the offline event. Phone numbers are normalized to E.164 format and converted to a UID 2.0 value before being sent to |destination-name|.

       .. note:: A row that has both **email** and **phone** generates two events, one for each identifier.

       This value is most often associated with the **Phone** field in the **Customer 360** table. Include **phone** in the **SELECT** statement.

       For example:

       .. code-block:: sql

          ,c360.phone AS phone


   * - **price**
     - **Optional**, but **Recommended** when transaction details are included with events. See **cat**, **item_code**, and **qty**.

       The price of each item that is associated with an offline event. For example: "$9.99"

       This value is most often associated with the **Item Price** field in the **Unified Itemized Transactions** table. Include **item_price** in the **SELECT** statement.

       For example:

       .. code-block:: sql

          ,item_price


   * - **qty**
     - **Optional**, but **Recommended** when transaction details are included with events. See **cat**, **item_code**, and **price**.

       The number of items that are associated with an offline event. For example: "10".


       This value is most often associated with the **Item Quantity** field in the **Unified Itemized Transactions** table. Include **item_quantity** in the **SELECT** statement.

       For example:

       .. code-block:: sql

          ,item_quantity


   * - **region**
     - **Optional**, but **Required** when **country** is included with events.

       The region in which the offline event occurred. For the United States, **region** refers to the state in which the offline event occurred.

       Include **state** and **country** in the **SELECT** statement when **country** is also returned in the query results.

       For example:

       .. code-block:: sql

          ,country
          ,state

       .. tip:: Use a **WHERE** clause to limit query results to only events that occurred in specific states.

          .. code-block:: sql

             WHERE state = 'CA'


   * - **storeid**
     - **Optional**

       A unique identifier for the location in which the offline event occurred. For retail transactions, this is most often a unique ID for a store or for a website.

       This value is most often associated with the **Store ID** field in the **Unified Transactions** table. Include **store_id** in the **SELECT** statement.

       For example:

       .. code-block:: sql

          ,store_id

       If you do not need to track events by individual physical stores, you may use a purchase channel to define this value. For example:

       .. code-block:: sql

          ,purchase_channel AS store_id


   * - **TD1** - **TD10**
     - **Optional**

       A series of optional fields that may be used for category or other organization. The value for these fields is a string with a maximum of 64 characters.


   * - **timestamp**
     - **Required**

       A field in a database table that has the date and time at which the offline event occurred.

       For retail-focused events this is most often the **Order Datetime** field in the **Unified Transactions** table, but it may be from a different table depending on your use case or how your brand has configured Amperity. Within the **SELECT** statement, return **Order Datetime**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,order_datetime AS timestamp


   * - **uid2**
     - **Optional**

       You may use **uid2** as an attribute when Amperity is configured as a `UID2 Operator <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| for your brand.

       For example:

       .. code-block:: sql

          SELECT 
            uid2.uid2
            ,uit.order_datetime AS timestamp
          FROM Unified_Itemized_Transactions uit
          LEFT JOIN UID2 uid2 ON uit.amperity_id = uid2.uid2
          WHERE uit.order_datetime > (CURRENT_DATE - interval '25' day)


   * - **value**
     - **Recommended**

       The monetary value of the offline event to your brand. The value for this field must be a decimal.

       .. note:: This field should be included with events to help |destination-name| deduplicate conversion events.

       For retail-focused events this is most often the **Order Value** field in the **Unified Transactions** table, but it may be from a different table depending on your use case or how your brand has configured Amperity. Within the **SELECT** statement, return **Order Value**, and then rename it to the field name required by |destination-name|.

       For example:

       .. code-block:: sql

          ,order_value AS value


   * - **valuecurrency**
     - **Optional**

       The currency that was associated with the offline event.

       For retail-focused events this is most often the **Currency** field in the **Unified Transactions** table, but it may be from a different table depending on your use case or how your brand has configured Amperity. Include **currency** in the **SELECT** statement.

       For example:

       .. code-block:: sql

          ,currency


.. events-the-trade-desk-parameters-offline-end
