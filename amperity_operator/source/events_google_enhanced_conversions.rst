.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Enhanced Conversions
.. |plugin-name| replace:: "Google Enhanced Conversions"
.. |credential-type| replace:: "google-ads"
.. |required-credentials| replace:: "Customer ID"
.. |what-send| replace:: events
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "google"
.. |hashed-fields| replace:: **email** and **phone**


.. meta::
    :description lang=en:
        Configure Amperity to send events to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send events to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for Google Enhanced Conversions

=======================================================
Configure events for Google Enhanced Conversions
=======================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-enhanced-conversions-start
   :end-before: .. term-google-enhanced-conversions-end

.. events-google-enhanced-conversions-about-start

When a customer purchases something from your brand's website, you likely collect some first-party data from that customer to complete the transaction. For example, a physical address, an email address, a phone number, and a full name.

First-party customer data that is associated with online transactions can be sent to |destination-name|, after which it can be used to enhance conversion measurement in Google Ads. For example:

* Track sales and events that happen on a website.
* Track sales that happen from a website.
* Match customers to their Google accounts, which were signed-in to when they engaged with one of your ads.
* Attribute customer engagement with a Google Ads campaign by matching data collected on your website with the signed-in Google accounts that engaged with your ads.

.. events-google-enhanced-conversions-about-end

.. 
.. .. include:: ../../shared/destination_settings.rst                            
..    :start-after: .. setting-common-sha-256-hashed-fields-start
..    :end-before: .. setting-common-sha-256-hashed-fields-end
.. 

.. TODO: Switch to the inclusion after other PRs are merged.

.. setting-common-sha-256-hashed-fields-start

.. caution:: The values for |hashed-fields| sent to |destination-name| are SHA-256 hashed automatically by Amperity before sending. Do not use the **TO_HEX()** function with the |hashed-fields| fields for queries that return results for |destination-name|.

.. setting-common-sha-256-hashed-fields-end

.. note:: For **gmail.com** and **googlemail.com** addresses, Amperity removes dots from the username portion before hashing. For example, **justin.c@gmail.com** is normalized to **justinc@gmail.com** before the SHA-256 hash is applied. This matches Google's own normalization and improves match rates for Gmail addresses.


.. _events-google-enhanced-conversions-howitworks:

How this destination works
==================================================

.. events-google-enhanced-conversions-howitworks-start

When a customer sees or clicks a Google ad and later makes a purchase, that purchase does not automatically appear in Google Ads. |destination-name| closes that gap by uploading first-party data from Amperity to Google Ads, which then matches the purchase back to the original ad interaction. The method of matching depends on where and how the purchase happened.

.. events-google-enhanced-conversions-howitworks-end


.. _events-google-enhanced-conversions-howitworks-web:

Offline web purchases
--------------------------------------------------

.. events-google-enhanced-conversions-howitworks-web-start

When a customer clicks a Google ad a **gclid** (Google Click ID) is captured in the URL at the moment of the click. The customer navigates away and returns the next day to complete a purchase on your website without clicking another ad. Google Ads has no record of that purchase because no conversion tag fired at checkout.

Amperity uploads the purchase with the original **gclid** attached. Google Ads matches the uploaded conversion back to the click and attributes the purchase to the campaign.

The **gclid** is the primary match signal for web purchases. Hashed email addresses and hashed phone numbers are optional, but should be included when available to improve match rates when the **gclid** is stale or unavailable.

**Example query**

.. code-block:: sql
   :linenos:

   SELECT
     uit.order_id
     ,oe.gclid
     ,uit.order_datetime AS timestamp
     ,mc.email
     ,mc.phone
     ,uit.unit_price
     ,uit.quantity
     ,uit.product_id
     ,'USD' AS currency_code
   FROM Unified_Itemized_Transactions uit
   JOIN Online_Events oe ON uit.amperity_id = oe.amperity_id
   JOIN Merged_Customers mc ON uit.amperity_id = mc.amperity_id
   WHERE oe.gclid IS NOT NULL

where the following fields are:

* Required: **order_id**, **gclid**, and **timestamp**.
* Recommended: **email**, **phone**, **unit_price**, **quantity**, and **currency_code**
* Optional: **product_id**, **merchant_id**, **feed_country_code**, **feed_language_code**, **local_transaction_cost**, **ad_personalization**, and **ad_user_data**
* Omit: **gbraid**, **wbraid**, and **conversion_environment**. **gbraid** and **wbraid** apply only to ``APP`` purchases.

.. events-google-enhanced-conversions-howitworks-web-end


.. _events-google-enhanced-conversions-howitworks-app:

Offline app purchases
--------------------------------------------------

.. events-google-enhanced-conversions-howitworks-app-start

App purchases use different click identifiers depending on which direction the ad interaction went:

* **gbraid** The customer clicked a web ad and was directed to your iOS app.
* **wbraid** The customer clicked an iOS app ad and was directed to a webpage before completing the purchase in-app.

These identifiers work the same way as **gclid** for matching. Include hashed email and phone as supplementary identifiers.

You may also set ``conversion_environment`` to ``APP`` to record that the conversion occurred in an app. This field is only available to allowlisted Google Ads accounts. Omit it if your account is not allowlisted.

**Example query**

.. code-block:: sql
   :linenos:

   SELECT
     uit.order_id
     ,oe.gbraid
     ,oe.wbraid
     ,uit.order_datetime AS timestamp
     ,mc.email
     ,mc.phone
     ,uit.unit_price
     ,uit.quantity
     ,uit.product_id
     ,'USD' AS currency_code
     ,'APP' AS conversion_environment
   FROM Unified_Itemized_Transactions uit
   JOIN Online_Events oe ON uit.amperity_id = oe.amperity_id
   JOIN Merged_Customers mc ON uit.amperity_id = mc.amperity_id
   WHERE oe.gbraid IS NOT NULL
      OR oe.wbraid IS NOT NULL

where the following fields are:

* Required: **order_id**, **timestamp**, and at least one of **gbraid** or **wbraid**
* Recommended: **email**, **phone**, **unit_price**, **quantity**, and **currency_code**
* Optional: **product_id**, **merchant_id**, **ad_personalization**, **ad_user_data**, and **conversion_environment**.
* Omit: **gclid**


.. events-google-enhanced-conversions-howitworks-app-end


.. _events-google-enhanced-conversions-howitworks-store:

In-store purchases
--------------------------------------------------

.. events-google-enhanced-conversions-howitworks-store-start

A customer sees a Google ad, does not click it, and later walks into a physical store to make a purchase. The only link between the purchase and the ad is the customer's identity.

Amperity uploads the transaction with hashed email and phone. Google Ads matches those values against the signed-in Google accounts that previously engaged with your ads. If the customer's email or phone on file with you matches their Google account, the purchase is attributed to the campaign.

**Email and phone are both required for in-store attribution.** Without at least one of them, Google has nothing to match against. Include both whenever your point-of-sale system captures them. Each additional identifier improves the chance of a successful match. Amperity SHA-256 hashes email and phone values automatically before upload.

**conversion_environment** does not apply to in-store purchases because neither ``APP`` nor ``WEB`` is accurate for describing a store transaction.

**Example query**

.. code-block:: sql
   :linenos:

   SELECT
     uit.order_id
     ,uit.order_datetime AS timestamp
     ,mc.email
     ,mc.phone
     ,uit.unit_price
     ,uit.quantity
     ,uit.product_id
     ,'USD' AS currency_code
   FROM Unified_Itemized_Transactions uit
   JOIN Merged_Customers mc ON uit.amperity_id = mc.amperity_id
   WHERE mc.email IS NOT NULL
      OR mc.phone IS NOT NULL

where the following fields are:

* Required: **order_id**, **timestamp**, and at least one of **email** or **phone**
* Recommended: **email**, **phone**, **unit_price**, **quantity**, and **currency_code**

  .. important:: Rows where both **email** and **phone** are **NULL** are dropped before upload. They cannot be matched and are excluded. Filter them out in your query, as shown above, to keep row counts accurate.

* Optional: **product_id**, **merchant_id**, **feed_country_code**, **feed_language_code**, **local_transaction_cost**, **ad_personalization**, and **ad_user_data**
* Omit: **gclid**, **gbraid**, **wbraid**, and **conversion_environment**.

.. events-google-enhanced-conversions-howitworks-store-end


.. _events-google-enhanced-conversions-howitworks-consolidated:

Multiple purchase channels in the same query
--------------------------------------------------

.. events-google-enhanced-conversions-howitworks-consolidated-start

If your events data consolidates web, app, and in-store purchases into a single events table, you can send all three to |destination-name| in one query. Each row must include:

#. At least one match signal: **gclid**, **gbraid**, or **wbraid**
#. A customer identifier: **email** or **phone**

Fields that do not apply to a given channel are **NULL**. The connector sends only the fields that are present and drops rows where no match signal exists.

.. code-block:: sql
   :emphasize-lines: 4-8,13,17-21
   :linenos:

   SELECT
     events.order_id
     ,events.event_datetime AS timestamp
     ,events.gclid
     ,events.gbraid
     ,events.wbraid
     ,mc.email
     ,mc.phone
     ,uit.unit_price
     ,uit.quantity
     ,uit.product_id
     ,'USD' AS currency_code
     ,events.conversion_environment
   FROM Customer_Events events
   JOIN Unified_Itemized_Transactions uit ON events.order_id = uit.order_id
   LEFT JOIN Merged_Customers mc ON events.amperity_id = mc.amperity_id
   WHERE events.gclid IS NOT NULL
      OR events.gbraid IS NOT NULL
      OR events.wbraid IS NOT NULL
      OR mc.email IS NOT NULL
      OR mc.phone IS NOT NULL

The source table must have values that map correctly across all three purchase channels:

#. **gclid** is set for web purchases. It is **NULL** for app and in-store purchases.
#. **gbraid** is set when a customer clicked a web ad and was directed to your iOS app. It is **NULL** for web and in-store purchases.
#. **wbraid** is set when a customer clicked an iOS app ad and was directed to a webpage. It is **NULL** for web and in-store purchases.
#. **email** and **phone** are the primary match signals for in-store purchases, and supplement click IDs for web and app purchases. Amperity hashes both automatically before upload. Do not hash them in the query.
#. **conversion_environment** should be ``WEB`` or ``APP`` when known. Set to **NULL** for in-store purchases. This field is only available to allowlisted Google Ads accounts; omit **conversion_environment** if your account is not allowlisted.
#. The **WHERE** clause ensures every row has at least one match signal. Rows that do not satisfy this condition are dropped by the connector before upload.

.. events-google-enhanced-conversions-howitworks-consolidated-end


.. _events-google-enhanced-conversions-howitworks-sftp:

Optional. In-store, physical addresses
--------------------------------------------------

.. events-google-enhanced-conversions-howitworks-sftp-start

For retailers with large in-store transaction volumes, Google offers a `separate program called Store Sales <https://support.google.com/google-ads/answer/10018336>`__ |ext_link| that supports physical address as a match identifier. This is useful when customers have provided a mailing address but not an email or phone number.

Store Sales is a distinct Google Ads program from Enhanced Conversions. It requires allowlisting by Google and has minimum volume thresholds: at least 30,000 in-store transactions and 500,000 ad interactions within the previous 90 days. If your account does not meet these thresholds, use the in-store purchases approach described above instead.

When using Store Sales, Amperity exports a formatted CSV file via :doc:`SFTP <destination_sftp>`, which is then uploaded to Google Ads through the UI or API. The CSV file uses a two-row header structure required by Google:

* The first row has metadata, such as timezone, loyalty rate, or transaction upload rate.
* The second row has column names. Google hashes PII automatically on upload, or you can pre-hash using SHA-256.

**Identifiers supported by Store Sales**

Store Sales supports more identifiers per customer than the Enhanced Conversions API path:

* Email addresses: up to 3 per customer
* Phone numbers: up to 3 per customer. Phone numbers must be in `E.164 format <https://en.wikipedia.org/wiki/E.164>`__ |ext_link| format
* Physical address, including first name, last name, street, city, state, postal code, and country

Include as many identifiers as your data has. Each additional identifier helps improve match rates.

**When to use this instead of the in-store API path**

Use Store Sales instead of in-store purchases when:

* Your account is allowlisted for the Store Sales program.
* You have customers whose physical address is known, but email and phone are not. Those customers cannot be matched using |destination-name|.
* Your in-store transaction volume exceeds program thresholds.

Use the in-store API path for purchases when:

* Your account is not enrolled in Store Sales.
* Your customers reliably provide email or phone at checkout.
* You want a single automated pipeline that handles web, app, and in-store conversions.

.. events-google-enhanced-conversions-howitworks-sftp-end


.. _events-google-enhanced-conversions-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-google-enhanced-conversions-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Configure Google Ads**

       Enable enhanced conversions for leads in Google Ads:

       #. `Enable conversion tracking in Google Ads <https://developers.google.com/google-ads/api/docs/conversions/enhanced-conversions/leads-setup>`__ |ext_link|.
       #. Accept customer data terms and opt-in to enhanced conversions for leads.
       #. Set up tagging through Google Tag Manager.
       #. Create at least one ConversionAction.

          The conversion_action_type must be set to **UPLOAD_CLICKS**.

          .. note:: Amperity will automatically create a ConversionAction with the name you provide if one does not already exist in Google Ads.

       #. `Configure Google tag settings <https://support.google.com/google-ads/answer/11021502#configure>`__ |ext_link| to enable enhanced conversions for leads.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Events data**

       Load to Amperity data that tracks events data for carts, items in carts, and customer consent. This dataset should include the Google Ads click ID. Some of this data :ref:`may be sent to Google Enhanced Conversions for customer attribution <events-google-enhanced-conversions-fields>`.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for "Google Enhanced Conversions" *must* be completed within Google before configuring Amperity to send ads to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-customer-id-end

.. events-google-enhanced-conversions-get-details-table-end


.. _events-google-enhanced-conversions-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure OAuth**

.. events-google-enhanced-conversions-credentials-steps-start

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

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. events-google-enhanced-conversions-credentials-steps-end


.. _events-google-enhanced-conversions-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Enhanced Conversions**

.. events-google-enhanced-conversions-add-steps-start

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

       **Conversion action name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-action-name-start
             :end-before: .. setting-google-enhanced-conversions-action-name-end

       **Customer ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-customer-id-end


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


.. events-google-enhanced-conversions-add-steps-end


.. _events-google-enhanced-conversions-fields:

Fields for enhanced conversions
==================================================

.. events-google-enhanced-conversions-fields-start

Fields for enhanced conversions must include hashed customer profile data--email addresses and phone numbers--and should include a transaction identifier and the Google Ads click ID.

The following table describes the fields that may be sent to |destination-name| for customer attribution. You should send as many of these fields as you can for each potential attribution to customer activity.

.. important:: The **order_id** field is required. Each conversion must also include at least one of: **gclid**, **gbraid**, **wbraid**, **email**, or **phone**. Rows that do not meet these requirements are dropped before upload. When a batch is uploaded, row-level failures do not fail the entire batch (``partialFailure`` is enabled). Each conversion supports a maximum of five user identifiers (email and phone combined).

.. events-google-enhanced-conversions-fields-end

.. events-google-enhanced-conversions-fields-table-start

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity
     - Google
     - Description
   * - Varies.
     - **ad_personalization**
     - The customer consent status for personalization for Google Ads.

       .. note:: This field should be in the table that has online events data for websites and mobile apps collected by Google Ads, but may be located in a table for consent tracking.


   * - Varies.
     - **ad_user_data**
     - The customer consent status for Google Ads.

       .. note:: This field should be in the table that has online events data for websites and mobile apps collected by Google Ads, but may be located in a table for consent tracking.


   * - Varies.
     - **conversion_environment**
     - The environment in which the conversion occurred. Valid values are ``APP`` or ``WEB``.

       .. note:: This field is only available to allowlisted customers. ``UNSPECIFIED`` and ``UNKNOWN`` are API-internal values and cannot be set by users.

       .. note:: This field should be in the table that has online events data for websites and mobile apps collected by Google Ads.


   * - Varies.
     - **currency_code**
     - The `currency code <https://developers.google.com/google-ads/api/data/codes-formats#currency_codes>`__ |ext_link| for the conversion_value.


   * - **Email**
     - **email**
     - The email address for the customer.

       Amperity automatically normalizes email addresses by converting to lowercase, trimming spaces, removing dots from Gmail addresses, and then using SHA-256 to hash the value before uploading to |destination-name|.

       .. tip:: Use the **email** field in the **Merged Customers** table.


   * - Varies.
     - **feed_language_code**
     - The language code used in Google services to set the language of an advertising feed.


   * - Varies.
     - **feed_country_code**
     - The country code used in Google services to set the language of an advertising feed.


   * - Varies.
     - **gbraid**
     - A gbraid is a URL parameter present when a user clicks on an ad on the web, and then is directed to your brand's iOS app.

       .. note:: This field should be in the table that has online events data for websites and mobile apps collected by Google Ads.


   * - Varies.
     - **gclid**
     - A `gclid <https://support.google.com/google-ads/answer/9744275>`__ |ext_link| is an identifier captured from URL parameters when a customer clicks on an ad, and then navigates to your brand's website.

       This is the best identifier for online events and Google Ads.

       .. important:: Send all relevant data for a conversion even if the **gclid** is unavailable. Conversions data that only includes user-provided data is still useful.

       .. note:: This field should be in the table that has online events data for websites and mobile apps collected by Google Ads.


   * - **Item Cost**
     - **local_transaction_cost**
     - The individual cost for each item in the order.

       .. tip:: Use the **Item Cost** field in the **Unified Itemized Transactions** table.


   * - **Store ID**
     - **merchant_id**
     - A store ID is a unique identifier for the location of a store.

       .. tip:: Use the **Store ID** field in the **Unified Itemized Transactions** table.


   * - **Order ID**
     - **order_id**
     - An order ID is the unique identifier for the order. It links together all items in the same transaction. For returns and cancellations, the order ID is the unique identifier for the original order, including returned or canceled items.

       |destination-name| refers to this as the transaction ID for the conversion. This field is required.

       .. important:: Order IDs must be unique per conversion action. Duplicate order IDs within the same conversion action are ignored by Google Ads.

       .. tip:: Use the **Order ID** field in the **Unified Itemized Transactions** table.


   * - **Phone**
     - **phone**
     - The phone number for the customer.

       Amperity automatically normalizes phone numbers by converting to `E.164 format <https://en.wikipedia.org/wiki/E.164>`__ |ext_link| format, and then using SHA-256 to hash the value before uploading to |destination-name|.

       .. tip:: Use the **phone** field in the **Merged Customers** table.


   * - **Product ID**
     - **product_id**
     - The unique identifier for a product.

       .. tip:: Use the **Product ID** field in the **Unified Itemized Transactions** table.


   * - **Item Quantity**
     - **quantity**
     - Item quantity is the total number of items in an order. For returned and canceled items, item quantity is the total number of returned or canceled items.

       .. tip:: Use the **Item Quantity** field in the **Unified Itemized Transactions** table.


   * - Varies.
     - **timestamp**
     - The date and time of the conversion. The value must have a timezone and the format must be ``yyyy-mm-dd hh:mm:ss+|-hh:mm``. Daylight Savings Time (DST) may be ignored.

       .. note:: This field should be in the table that has online events data for websites and mobile apps collected by Google Ads *or* it may be the **Order Datetime** field in the **Unified Itemized Transactions** table.


   * - **Unit List Price**
     - **unit_price**
     - Unit list price is the manufacturer's suggested retail price (MSRP) for a single unit of an item.

       .. note:: Amperity calculates the conversion value sent to |destination-name| as ``SUM(unit_price * quantity)`` aggregated by order ID. This value is not a directly configurable field.

       .. tip:: Use the **Unit List Price** field in the **Unified Itemized Transactions** table.


   * - Varies.
     - **wbraid**
     - A **wbraid** is a URL parameter that is present when a user clicks on an ad in an iOS app and is directed to a webpage.

       .. note:: This field should be in the table that has online events data for websites and mobile apps collected by Google Ads.

.. events-google-enhanced-conversions-fields-table-end


.. _events-google-enhanced-conversions-api-reference:

Google Ads API reference
==================================================

.. vale off

.. events-google-enhanced-conversions-api-reference-start

Amperity uses the `Google Ads API v24 <https://developers.google.com/google-ads/api/reference/rpc/v24/>`__ |ext_link| to send data to |destination-name|. The following services are called:

* `GoogleAdsService.SearchStream <https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsService#searchstream>`__ |ext_link|

  Used to retrieve conversion tracking settings and look up existing conversion actions.

* `ConversionUploadService.UploadClickConversions <https://developers.google.com/google-ads/api/reference/rpc/v24/ConversionUploadService#uploadclickconversions>`__ |ext_link|

  Used to upload click conversions. Batches are capped at 2,000 rows.

* `ConversionActionService.MutateConversionActions <https://developers.google.com/google-ads/api/reference/rpc/v24/ConversionActionService#mutateconversionactions>`__ |ext_link|

  Used to create a conversion action when one with the configured name does not already exist.

.. events-google-enhanced-conversions-api-reference-end

.. vale on
