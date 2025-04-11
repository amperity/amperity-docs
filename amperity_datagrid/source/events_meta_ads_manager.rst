.. https://docs.amperity.com/operator/



.. |destination-name| replace:: Meta Ads Offline Events
.. |plugin-name| replace:: "Facebook"
.. |credential-type| replace:: "facebook"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: offline events
.. |where-send| replace:: |destination-name|
.. |what-enable| replace:: **EXTERN_ID**, **EMAIL**, **FN**, **LN**, **ST**, **CT**, **ZIP**, **COUNTRY**, **BIRTH**, **GEN**, **MADID**, and **PHONE**
.. |allow-for-what| replace:: offline events
.. |allow-for-duration| replace:: up to 24 hours
.. |attributes-sent| replace:: |destination-name| requires the **EXTERN_ID**, **EMAIL**, **FN**, **LN**, **ST**, **CT**, **ZIP**, **COUNTRY**, **BIRTH**, **GEN**, **MADID**, and **PHONE** attributes. The **MADID** (mobile advertising ID) attribute is optional.

.. meta::
    :description lang=en:
        Send offline events from Amperity to Meta Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send offline events from Amperity to Meta Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline events to Meta Ads Manager

==================================================
Send offline events to Meta Ads Manager
==================================================

.. TODO: Sync this with the updated events topics.

.. events-meta-ads-manager-overview-start

Send offline events to |destination-name| to help your brand track offline conversions that result from your marketing campaigns. Offline events may be matched with audiences in Facebook, Facebook Messenger, Instagram, and WhatsApp.

Transaction events that occurred within the previous seven days *and* contain positive values for product quantity may be sent to |destination-name| using the `Conversions API for offline events <https://developers.facebook.com/docs/marketing-api/conversions-api/offline-events>`__ |ext_link|.

.. important:: The first time transaction events are sent to |destination-name|, and when **action_source** is set to **physical_store**, up to 62 days of transactions data may be sent, after which Amperity should be configured to send updates that maintain a 7-day rolling window of transaction events.

.. events-meta-ads-manager-overview-end

.. events-meta-ads-manager-allowfor-start

.. note:: Offline events are not immediately available in |destination-name|. Allow for |allow-for-duration| after the point at which Amperity has finished sending |allow-for-what| for them to be available.

   Offline events that are sent to |destination-name| can be accessed from `Meta Events Manager <https://www.facebook.com/business/help/898185560232180?id=565900110447546>`__ |ext_link|.

.. events-meta-ads-manager-allowfor-end


.. _events-meta-ads-manager-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-meta-ads-manager-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Meta Ads Manager settings**

       **Dataset ID**
          |checkmark-required| **May be required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-meta-ads-manager-dataset-id-start
             :end-before: .. setting-meta-ads-manager-dataset-id-end


.. events-meta-ads-manager-get-details-table-end


.. _events-meta-ads-manager-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Meta Ads Manager offline events**

.. events-meta-ads-manager-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Refresh token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. events-meta-ads-manager-credentials-steps-end


.. _events-meta-ads-manager-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _events-meta-ads-manager-terms-of-service:

Terms of service
--------------------------------------------------

.. TODO: Sync this with the updated events topics.

.. events-meta-ads-manager-terms-of-service-start

The `custom audience terms of service <https://developers.facebook.com/docs/marketing-api/audiences/reference/custom-audience-terms-of-service/>`__ |ext_link| must be signed by *each business user* that is associated with your |destination-name| account. If the terms of service are not signed, a permissions error will prevent Amperity from sending data to |destination-name|.

.. events-meta-ads-manager-terms-of-service-end

.. events-meta-ads-manager-terms-of-service-error-start

The permissions error is similar to:

::

   Permissions error: To create or edit an audience with an uploaded
   customer list, please agree to the Custom Audience terms at
   https://business.facebook.com/ads/manage/customaudiences/tos/?act=123.

To resolve this error the terms of service must be signed by a business user who has a role in your |destination-name| account.

.. events-meta-ads-manager-terms-of-service-error-end


.. _events-meta-ads-manager-offline-events-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-meta-ads-manager-offline-events-add-destination-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       Enter the name of the destination and a description. For example: "|destination-name| offline events" and "Send offline events to |destination-name|.".

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       |destination-name| requires using OAuth to :ref:`authorize Amperity to send offline events to your Meta Ads Manager account <events-meta-ads-manager-credentials>`.

       .. note:: You may use the same credentials to send both custom audiences and offline events to |destination-name|.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
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
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Dataset ID**
          |checkmark-required| **May be required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-meta-ads-manager-dataset-id-start
             :end-before: .. setting-meta-ads-manager-dataset-id-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end


.. events-meta-ads-manager-offline-events-add-destination-end


.. _events-meta-ads-manager-build-segment:

Build a query
==================================================

.. events-meta-ads-manager-offline-events-build-query-start

Use a query to build a combination of data from the **Unified Itemized Transactions**, **Unified Transactions**, and **Customer 360** tables to represent the set of offline events that your brand wants to use within |destination-name|.

A query that returns a collection offline events for use in |destination-name| is similar to:

.. code-block:: sql

   SELECT
     c360.amperity_id AS external_id
     ,c360.email AS email
     ,c360.phone AS phone
     ,c360.given_name AS given_name
     ,c360.surname AS surname
     ,c360.birthdate AS birthdate
     ,c360.gender AS gender
     ,c360.city AS city
     ,c360.state AS state
     ,c360.postal AS postal
     ,c360.country AS country
     ,uit.order_id AS order_id
     ,uit.item_quantity AS quantity
     ,uit.product_id AS product_id
     ,uit.order_datetime AS timestamp
     ,CAST(uit.item_revenue / uit.item_quantity AS DOUBLE) AS price
     ,'USD' AS currency
     ,'physical_store' AS action_source 
   FROM Unified_Itemized_Transactions uit
   LEFT JOIN Customer_360 c360 ON uit.amperity_id = c360.amperity_id
   WHERE uit.order_datetime > (CURRENT_DATE - interval '7' day)

The query **MUST** contain the following fields: **external_id**, **order_id**, **quantity**, **email** (OR **phone**), **timestamp**, **price**, and **currency**. When **action_source** is not specified the default value is "physical_store".

You may include any of the following customer profile fields to help improve match rates in |destination-name|: **given_name**, **surname**, **birthdate**, **gender**, **city**, **state**, **postal**, and **country**.

.. tip::

   Extend the **WHERE** clause to filter query results by purchase channel, purchase brand, purchase quantity, and to remove items that were returned and/or canceled.

   For example:

   .. code-block:: sql

      WHERE uit.order_datetime > (CURRENT_DATE - interval '7' day)
      AND uit.purchase_channel = 'channel'
      AND uit.purchase_brand = "ACME Essentials"
      AND uit.item_quantity > 0
      AND (c360.email IS NOT NULL OR c360.phone IS NOT NULL)
      AND (
          (is_cancellation IS NULL)
          OR (NOT is_cancellation)
      )
      AND (
          (is_return IS NULL)
          OR (NOT is_return)
      )

.. events-meta-ads-manager-offline-events-build-query-end

.. events-meta-ads-manager-offline-events-parameters-start

Review the :ref:`Conversions API parameters <events-meta-ads-manager-conversions>` section for detailed information about the columns that must be (or may be) returned by your query.

.. events-meta-ads-manager-offline-events-parameters-end


.. _events-meta-ads-manager-conversions:

Conversions API parameters
==================================================

.. events-meta-ads-manager-conversion-api-parameters-start

The following table describes each of the parameters that are required by |destination-name| for offline events. The final row lists the optional fields your brand may include to extend the customer profile information that is associated with offline events that are returned by the query and sent to |destination-name|.

The fields are listed alphabetically, but may be returned by a query in any order.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field name
     - Description

   * - **action_source**
     - **Optional**

       Action sources group offline events into categories and enable ad measurmeent and custom audience creation abilities from within the |destination-name| user interface. The default value for **action_source** is **physical_store**.

       Add **action_source** to your query and then set a value:

       ::

          ,'physical_store' AS action_source

       The value for **action_source** must be one of the following:

       **app**
         Use when the offline conversion was made from a mobile app.

       **business_messaging**
         Use when the offline conversion was made from ads associated with Facebook Messenger, Instagram, or WhatsApp.

       **chat**
         Use when the offline conversion was made over a messaging app, SMS, or online messaging feature.

       **email**
         Use when the offline conversion happened over email.

       **other**
         Use when the offline conversion occurred by some other workflow.

       **phone_call**
         Use when the offline conversion was made over a phone call.

       **physical_store**
         **Default** Use when the offline conversion was made in-person at a physical store location.

         .. note:: The first time transaction events are sent to |destination-name|, and when **action_source** is set to **physical_store**, up to 62 days of transactions data may be sent, after which Amperity should be configured to send updates that maintain a 7-day rolling window of transaction events.

            For example, the initial send:

            ::

               ,'physical_store' AS action_source
               ...
               WHERE uit.order_datetime > (CURRENT_DATE - interval '62' day)

            Update "62" to "7" before the next send to maintain a 7-day rolling window.

       **system_generated**
         Use when the offline conversion occurred automatically, such as from a subscription renewal or monthly auto-pay.

       **website**
         Use when the offline conversion was made on a website.

         When **action_source** is set to **website** the following fields are required: **client_user_agent**, **event_id**, and **event_source_url**. These fields must be in the results that are sent to |destination-name|; missing or empty values are filtered from the results.

         * The value for **client_user_agent** must be the user agent for the browser corresponding to the event.

         * The value for **event_id** is a unique string chosen by advertiser.

         * The value for **event_source_url** should be browser URL at which the event occurred.

         **event_id** and **event_source_url** are `server event parameters <https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event/>`__ |ext_link| for the Conversions API.

       The value for **action_source** is used by the Conversions API to categorize offline conversions within the |destination-name| user interface and may not be customized. Use the action source that best associates how your brand wants to use offline conversions within |destination-name|.

       When **action_source** is not specified the default value is "physical_store".

   * - **currency**
     - **Required**

       A value for **currency** is required by the Conversions API for offline events. Currency must be a valid |ext_iso_4217| three-digit currency code, such as "USD" (United States dollar), "AUD" (Australian dollar), "CAD" (Canadian dollar), "EUR" (Euro), "JPY" (Japanese yen) or "MXN" (Mexican peso).

       Add **currency** to your query, and then set a value:

       ::

          ,'USD' AS currency

       .. note:: When viewing parameters in the |destination-name| user interface, **price**, **quantity**, and **currency** are combined to be shown as **value**, which represents the sum of price times quantity, shown in the currency used for the transaction.

   * - **email** *and/or* **phone**
     - **Required**

       You must send an email address *or* a phone number to |destination-name|; you may configure the query to send both.

       Add at least one of **email** or **phone** to your query:

       ::

          ,c360.email AS email
          ,c360.phone AS phone

       .. note:: Amperity performs the same actions for email addresses and phone numbers when sending to the Conversions API as when sending to the Marketing API.

   * - **event_name**
     - **Optional**

       Identifies an offline event within |destination-name|.

       .. note:: The default value for **event_name** is "Purchase". 

          This value may be set to one of: "ViewContent", "Search", "AddToCart", "AddToWishlist", "InitiateCheckout", "AddPaymentInfo", "Purchase", "Lead", or "Other".


   * - **external_id**
     - **Recommended**

       The **amperity_id** field **MUST** be renamed to **external_id**.

       Add **external_id** to your query:

       ::

          ,c360.amperity_id AS external_id

       .. note:: Amperity performs the same actions for the external ID when sending to the Conversions API as when sending to the Marketing API.

   * - **order_id**
     - **Optional**

       The order ID that is associated with the offline event.

       **When transactions data is available**

       Use the **Order ID** field that is available from the **Unified Itemized Transactions** or **Unified Transactions** tables:

       ::

          ,uit.order_id AS order_id

       .. important:: The number of rows that results from the query will not be the same as the number of events that are uploaded to |destination-name|.

          This is because transactions within the query are grouped by **Order ID** as the data is sent to |destination-name|.

          Grouping by **Order ID** ensures that individual events are combined to describe a complete transaction.

          Amperity performs the **GROUP BY** action automatically if a **GROUP BY** clause is not set to "order_id".


   * - **phone**
     - See **email**.

   * - **price**
     - **Required**

       The price that is associated with the offline event.

       .. note:: When viewing parameters in the |destination-name| user interface, **price**, **quantity**, and **currency** are combined to be shown as **value**, which represents the sum of price times quantity, shown in the currency used for the transaction.

       **When transactions data is available**

       Calculate **price** by dividing item revenue by item quantity. These fields are available from the **Unified Itemized Transactions** or **Unified Transactions** tables:

       ::

          ,CAST(
            uit.item_revenue / uit.item_quantity AS DOUBLE
          ) AS price


   * - **product_id**
     - **Optional**

       A unique product identifier that can be associated with the offline event.

       **When transactions data is available**

       Use the **Product ID** field that is available from the **Unified Itemized Transactions** or **Unified Transactions** tables:

       ::

          ,uit.product_id AS product_id


   * - **quantity** *or* **value**
     - **Required**

       A field that describes a quantity or a value amount associated with the offline event.

       .. note:: When viewing parameters in the |destination-name| user interface, **price**, **quantity** (or **value**), and **currency** are combined to be shown as **value**, which represents the sum of price times quantity, shown in the currency used for the transaction.

       **When transactions data is available**

       Use the **Item Quantity** field from the **Unified Itemized Transactions** or **Unified Transactions** tables to define **quantity**:

       ::

          ,uit.item_quantity AS quantity


   * - **timestamp**
     - **Required**

       A Unix timestamp (in seconds) that indicates when the offline event occurred.

       .. note:: When viewing parameters in the |destination-name| user interface, **timestamp** is shown as **event_time**.

       **When transactions data is available**

       Use the **Order Datetime** field from the **Unified Itemized Transactions** or **Unified Transactions** tables to define **timestamp**:

       ::

          ,uit.order_datetime AS timestamp

       Use a **WHERE** clause to limit the number of days to a maximum of seven:

       ::

          WHERE uit.order_datetime > (
            CURRENT_DATE - interval '7' day
          )


   * - **value**
     - See **quantity**.

   * - Optional profile attributes
     - You may include any of the profile attributes that are supported by the Marketing API, including **Gender**, **Birthdate**, **First Name**, **Last Name**, **City**, **State**, **Zip Code**, and **Country Code**.

.. events-meta-ads-manager-conversion-api-parameters-end
