.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Pinterest Ads Manager
.. |plugin-name| replace:: "Pinterest Offline Events"
.. |credential-type| replace:: "pinterest-offline-events"
.. |required-credentials| replace:: "conversion access token"
.. |what-send| replace:: offline conversion events
.. |where-send| replace:: |destination-name|
.. |what-enable| replace:: **timestamp**, **currency**, **email** or **phone**, and **value**
.. |allow-for-what| replace:: offline conversion events
.. |allow-for-duration| replace:: up to 48 hours for deduplication of events
.. |attributes-sent| replace:: |destination-name| requires the **timestamp**, **currency**, **email**, **value**, **order_id**, **extern_id**, **content_name**, **content_category**, **content_brand**, **item_name**, **item_category**, **item_brand**, **opt_out_typev, and **opt_out** attributes are optional.

.. meta::
    :description lang=en:
        Configure Amperity to send offline conversion events to Pinterest.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send offline conversion events to Pinterest.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure offline conversion events for Pinterest

==================================================
Configure offline conversion events for Pinterest
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pinterest-start
   :end-before: .. term-pinterest-end

.. events-pinterest-offline-events-overview-start

Send events to |destination-name| to help your brand track offline conversions that result from your marketing campaigns and improve return on ad spend (ROAS) and cost per acquisition (CPA) reporting performance within |destination-name|.

Only events that occurred within the previous seven days may be sent to |destination-name| using the `Send conversions <https://developer.pinterest.com/docs/api/v5/events-create/>`__ |ext_link| endpoint in the |destination-name| Conversions API.

.. events-pinterest-offline-events-overview-end

.. events-pinterest-offline-events-allowfor-start

.. note:: Offline conversion events require |allow-for-duration| within |destination-name|.

.. events-pinterest-offline-events-allowfor-end


.. _events-pinterest-offline-events-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-pinterest-offline-events-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Conversion access token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-pinterest-events-conversion-access-token-start
             :end-before: .. credential-pinterest-events-conversion-access-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-pinterest-events-conversion-access-token-find-start
             :end-before: .. credential-pinterest-events-conversion-access-token-find-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-pinterest-events-conversion-access-token-owner-or-admin-start
             :end-before: .. credential-pinterest-events-conversion-access-token-owner-or-admin-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Pinterest settings**

       **Ad account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-ad-account-id-start
             :end-before: .. setting-pinterest-ad-account-id-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-ad-account-id-about-start
             :end-before: .. setting-pinterest-ad-account-id-about-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Request properties**

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

.. events-pinterest-offline-events-get-details-table-end


.. _events-pinterest-offline-events-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Pinterest events**

.. events-pinterest-offline-events-credentials-steps-start

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

       **Conversion access token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-pinterest-events-conversion-access-token-start
             :end-before: .. credential-pinterest-events-conversion-access-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-pinterest-events-conversion-access-token-find-start
             :end-before: .. credential-pinterest-events-conversion-access-token-find-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-pinterest-events-conversion-access-token-owner-or-admin-start
             :end-before: .. credential-pinterest-events-conversion-access-token-owner-or-admin-end

.. events-pinterest-offline-events-credentials-steps-end


.. _events-pinterest-offline-events-offline-events-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-pinterest-offline-events-offline-events-add-destination-start

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

       **Ad account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-ad-account-id-start
             :end-before: .. setting-pinterest-ad-account-id-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-ad-account-id-about-start
             :end-before: .. setting-pinterest-ad-account-id-about-end


       **Batch size**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-events-batch-size-start
             :end-before: .. setting-pinterest-events-batch-size-end


       **Test mode**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-events-test-mode-start
             :end-before: .. setting-pinterest-events-test-mode-end

          .. important::

             .. include:: ../../shared/destination_settings.rst
                :start-after: .. setting-pinterest-events-test-mode-false-start
                :end-before: .. setting-pinterest-events-test-mode-false-end


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

.. events-pinterest-offline-events-offline-events-add-destination-end


.. _events-pinterest-offline-events-build-segment:

Build a query
==================================================

.. events-pinterest-offline-events-offline-events-build-query-start

Use a query to build a combination of data from the **Unified Transactions** and **Customer 360** tables to send offline conversion events to |destination-name|.

.. events-pinterest-offline-events-offline-events-build-query-end

.. events-pinterest-offline-events-offline-events-build-query-required-start

Review the :ref:`Conversions API parameters <events-pinterest-offline-events-conversions>` section for detailed information about the columns returned by your query.

.. events-pinterest-offline-events-offline-events-build-query-required-end

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


.. _events-pinterest-offline-events-build-query-orders:

Order-level events
--------------------------------------------------

.. events-pinterest-offline-events-build-query-orders-start

A query that returns a collection of order-level events for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     c360.customer_id AS external_id
     ,c360.given_name AS fn
     ,c360.surname AS ln
     ,c360.phone AS ph
     ,c360.email AS em
     ,c360.city AS ct
     ,c360.state AS st
     ,c360.postal AS zp
     ,c360.country AS country
     ,c360.birthdate AS db
     ,ut.currency AS currency
     ,ut.order_id AS order_id
     ,ut.order_quantity AS num_items
     ,ut.order_datetime AS event_time
     ,ut.order_revenue AS value
   FROM Unified_Transactions ut
   LEFT JOIN Customer_360 c360 ON ut.amperity_id = c360.amperity_id
   WHERE ut.order_datetime > (CURRENT_DATE - interval '7' day)

.. events-pinterest-offline-events-build-query-orders-end


.. _events-pinterest-offline-events-build-query-items:

Item-level events
--------------------------------------------------

.. events-pinterest-offline-events-build-query-items-start

A query that returns a collection of item-level events for use in |destination-name| is more complex. Review the tables available in your tenant and review the available parameters in the parameters in the `Send conversions <https://developer.pinterest.com/docs/api/v5/events-create/>`__ |ext_link| to determine which combinations of attributes in your tenant can be mapped to properties in the **Send conversions** endpoint.

The following example uses the **Customer 360**, **Unified Itemized Transactions**, and **Unified Transactions** tables.

.. code-block:: sql

   WITH customer_hashed AS (
     SELECT
       amperity_id
       ,c360.email AS em
       ,c360.phone AS ph
       ,c360.given_name AS fn
       ,c360.surname AS ln
       ,CONCAT(
         CAST(YEAR(c360.birthdate) AS VARCHAR), '-',
         LPAD(CAST(MONTH(c360.birthdate) AS VARCHAR), 2, '0'), '-',
         LPAD(CAST(DAY(c360.birthdate) AS VARCHAR), 2, '0')
       ) AS db
       ,c360.city AS ct
       ,c360.state AS st
       ,c360.postal AS zp
       ,c360.country AS country
       ,c360 customer_id AS external_id
     FROM Customer_360
     WHERE email IS NOT NULL
     OR phone IS NOT NULL
   ),

   itemized_rollup AS (
     SELECT
       order_id,
       SUM(item_quantity) AS num_items,
       SUM(item_revenue) AS total_item_revenue,
       ARRAY_AGG(
         MAP(
           ARRAY['id', 'item_price', 'quantity'],
           ARRAY[product_id, CAST(item_revenue AS VARCHAR), CAST(item_quantity AS VARCHAR)]
         )
         ORDER BY product_id
       ) AS contents
     FROM Unified_Itemized_Transactions
     WHERE is_return IS NULL
     AND is_cancellation IS NULL
     AND item_revenue >= 0
     GROUP BY order_id
   ),

   order_events AS (
     SELECT
       ut.amperity_id
       ,ut.order_id
       ,'checkout' AS event_name
       ,TO_UNIXTIME(ut.order_datetime) AS event_time
       ,ut.order_id AS event_id
       ,'USD' AS currency
       ,CAST(ut.order_revenue AS VARCHAR) AS value
     FROM Unified_Transactions ut
     WHERE ut.amperity_id IS NOT NULL
   ),

   pinterest_events AS (
     SELECT
       ,oe.event_name
       ,oe.event_time
       ,oe.event_id
       ,oe.event_source_url
       ,oe.action_source
       ,c.em
       ,c.ph
       ,c.fn
       ,c.ln
       ,c.ge
       ,c.db
       ,c.ct
       ,c.st
       ,c.zp
       ,c.country
       ,c.external_id
       ,oe.currency
       ,oe.value
       ,ir.num_items
       ,ir.contents
     FROM order_events oe
     JOIN customer_hashed c  ON oe.amperity_id = c.amperity_id
     LEFT JOIN itemized_rollup ir ON oe.order_id    = ir.order_id
   )

   SELECT *
   FROM pinterest_events
   ORDER BY event_time DESC

.. events-pinterest-offline-events-build-query-items-end


.. _events-pinterest-offline-events-conversions:

Offline events parameters
==================================================

.. events-pinterest-offline-events-conversion-api-parameters-start

The following table describes each of the parameters that are required by |destination-name| for offline events. Refer to the `Send conversions <https://developer.pinterest.com/docs/api/v5/events-create/>`__ |ext_link| endpoint documentation for more information about parameters, making requests, and ensuring that the shape of the data sent to |destination-name| from Amperity matches what |destination-name| expects to be in the request.

The fields are listed alphabetically, but may be returned by a query in any order.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Amperity field name
     - Pinterest field name
     - Description

   * - None.
     - **action_source**
     - **Automatic**

       The location at which the conversion event occurred. The value for **action_source** is assigned automatically and is set to **offline**.


   * - **Birthdate**
     - **db**
     - **Optional**

       A birthdate, in YYYYMMDD format.

       .. note:: **db** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **db** before sending to |destination-name|.


   * - **City**
     - **ct**
     - **Optional**

       A city name, in lowercase with punctuation and spaces removed.

       .. note:: **ct** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **ct** before sending to |destination-name|.


   * - Varies.
     - **click_id**
     - **Optional**

       A unique identifier used by |destination-name| to identify users based on information sent with promoted traffic. This identifier is in the ``_epik`` cookie or in the ``&epik=`` query parameter in a URL.

       .. note;: **click_id** is part of the **user_data** object in the **Send conversions** endpoint.


   * - **Country**
     - **country**
     - **Optional**

       A two-character |ext_iso_31661alpha2| country code, in lowercase.

       .. note:: **country** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **country** before sending to |destination-name|.


   * - **Currency**
     - **currency**
     - **Required**

       |destination-name| requires the value for currency to be a three character alphabetic |ext_iso_4217| currency code. For example: "USD".

       Use the **Currency** field in the **Unified Transactions** table when its values are three character alphabetic ISO 4217 currency codes.

       .. note:: **currency** is part of the **custom_data** object in the **Send conversions** endpoint.


   * - **Email**
     - **em**
     - **Required**

       An email address, in lowercase.

       .. note:: **em** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **em** before sending to |destination-name|.


   * - None.
     - **event_id**
     - **Optional**

       A deterministic idenfier created by Amperity that uniquely identifies an offline event.

       .. note:: The value for **event_id** helps |destination-name| deduplicate events sent from Amperity using the Conversion API with other events captured by Pinterest tracking. Deduplication occurs within 48 hours of receiving events sent to the Conversions API.

       When an order ID exists, **event_id** is generated as

       .. code-block:: none

          SHA256(order_id | event_name | event_time)

       When an order ID does not exist, **event_id** is an empty string.

       .. note:: Amperity automatically applies SHA-256 hashing to **event_id** before sending to |destination-name|.


   * - None.
     - **event_name**
     - **Automatic**

       The type of user event. The value for **event_name** is assigned automatically and is set to **checkout**. Only checkout event types are supported.


   * - Varies.
     - **external_id**
     - **Required**

       An SHA-256 hashed string that uniquely identifies a user within your customer data. For example: a user ID, a loyalty ID, or a customer ID.

       .. note:: **external_id** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **external_id** before sending to |destination-name|.


   * - **Gender**
     - **ge**
     - **Optional**

       A gender identifier, in lowercase. Must be one of "f", "m", or "n" for non-binary gender.

       .. note:: **ge** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **gender**.


   * - **Given Name**
     - **fn**
     - **Optional**

       A first name, in lowercase.

       .. note:: **fn** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **fn** before sending to |destination-name|.


   * - Varies.
     - **hashed_maids**
     - **Optional**

       Unique identifiers for Google Advertising IDs (GAIDs) or Apple's Identifier for Advertisers (IDFAs).

       .. note:: **hashed_maids** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **hashed_maids**.


   * - Varies.
     - **opt_out**
     - **Optional**

       Indicates when a user has opted out of tracking for web conversion events or ad personalization in |destination-name|.

       .. note:: Opt out data is available from data sources that capture when users

          * Disable personalized advertising on iOS or Android mobile devices
          * Configure web browsers to "not track"
          * Opt of web or offline conversion events


   * - None.
     - **opt_out_type**
     - **Required** when **opt_out** is "true".

       Use **opt_out_type** for situations where a customer's **opt_out** preference is known. When the **opt_out** parameter is "true" the value of **opt_out_type** must be "ldp". When **opt_out_type** is "ldp" |destination-name| enforces `limited data processing <https://help.pinterest.com/en/business/article/limited-data-processing>`__ |ext_link|.


   * - **Order ID**
     - **order_id**
     - **Recommended**

       The unique identifier for an order. |destination-name| uses order IDs, when available, for deduplicating events. 

       .. note:: When an **order_id** is available Amperity will:

          #. Group offline transaction events by unique order ID
          #. Use **order_id** to build the SHA-256 hash for **event_id**


   * - None.
     - **partner_name**
     - **Automatic**

       The identifier for the third-party partner responsible for sending events to the |destination-name| Conversions AI. The value for **partner_name** is assigned automatically and is set to **ss-amperity**.


   * - **Phone**
     - **ph**
     - **Recommended**.

       A phone number with only digits, country code, area code, and number.

       .. note:: **ph** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **ph** before sending to |destination-name|.


   * - **Postal**
     - **zp**
     - **Optional**

       A postal code with only digits.

       .. note:: **zp** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **zp** before sending to |destination-name|.


   * - **State**
     - **st**
     - **Optional**

       A two-letter code for a state or province, in lowercase.

       .. note:: **st** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **st** before sending to |destination-name|.


   * - **Surname**
     - **ln**
     - **Optional**

       A last name, in lowercase.

       .. note:: **ln** is part of the **user_data** object in the **Send conversions** endpoint.

          Amperity automatically applies SHA-256 hashing to **ln** before sending to |destination-name|.


   * - **Order Datetime**
     - **event_time**
     - **Required**

       An |ext_iso_8601| timestamp for the date and time at which the offline conversion event occurred. For example: "2025-01-12T14:21:56.000Z".

       .. important:: All timestamps sent to |destination-name| must have occurred within the previous seven days. Events that occurred outside of the seven day window are not sent.


   * - **Order Revenue**
     - **value**
     - **Required** when **price** and **quantity** are unavailable.

       The total price for the offline conversion event, not including tax or shipping costs.

       You may configure the SQL query to use item-level details to calculate order revenue. Use the **Unified Itemized Transactions** table and calculate order revenue using **Item Price** and **Item Quantity** for all units of items associated with a unique **Order ID**.

       .. note:: **value** is part of the **custom_data** object in the **Send conversions** endpoint.

.. events-pinterest-offline-events-conversion-api-parameters-end
