.. https://docs.amperity.com/legacy/


.. |source-name| replace:: Shopify
.. |plugin-name| replace:: Shopify
.. |feed-name| replace:: Customer
.. |example-filenamex| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **shopify**
.. |what-pull| replace:: customer profiles and orders


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Shopify.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Shopify.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Shopify

==================================================
Pull from Shopify
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-shopify-start
   :end-before: .. term-shopify-end

.. caution:: The API used by this connector is deprecated. New data sources cannot be configured using this connector.

.. source-shopify-api-context-start

Shopify is source of high quality data for both customer records *and* interaction records, including:

* Complete profile data, including full names, full addresses, email address, and phone number
* Orders, including order amounts, items and item quantities, location
* Prices and discounts
* Refunds and cancellations
* Product catalog details
* Abandoned carts
* Customer searches
* Guest checkout data, including email address and associated order details

.. source-shopify-api-context-end

.. source-shopify-api-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-shopify-api-get-details>`
#. :ref:`Configure authorization access scopes <source-shopify-api-configure-authorization-access-scopes>`
#. :ref:`Run courier <source-shopify-api-run-courier>`
#. :ref:`Review feed and domain table <source-shopify-api-review-data>`
#. :ref:`Add to courier group <source-shopify-api-add-to-courier-group>`

.. source-shopify-api-steps-to-pull-end


.. _source-shopify-api-get-details:

Get details
==================================================

.. source-shopify-api-get-details-start

#. Your |source-name| **Shop Name**.
#. A list of tables to be pulled to Amperity from |source-name|.

   This is done by configuring |source-name| to allow Amperity to `read data from the Shopify Admin API <https://shopify.dev/docs/admin-api/access-scopes>`__ |ext_link| using a set of authorization access scopes.

.. source-shopify-api-get-details-end


.. _source-shopify-api-configure-authorization-access-scopes:

Configure authorization access scopes
==================================================

.. source-shopify-api-configure-access-to-tables-start

You must configure read access within |source-name| to allow Amperity to pull data from tables. The following authorization access scopes must be enabled:

* `read_customers <https://shopify.dev/api/admin-rest/2022-10/resources/customer>`__ |ext_link|, from which Amperity builds the :ref:`customer <source-shopify-api-review-data-customer>` and :ref:`customer address <source-shopify-api-review-data-customer-address>` feeds
* `read_orders <https://shopify.dev/api/admin-rest/2022-10/resources/order>`__ |ext_link|, from which Amperity builds the :ref:`order <source-shopify-api-review-data-order>` and :ref:`order line <source-shopify-api-review-data-order-line>` feeds
* `read_products <https://shopify.dev/api/admin-rest/2022-10/resources/product>`__ |ext_link|, from which Amperity builds the :ref:`product <source-shopify-api-review-data-product>` and :ref:`product variant <source-shopify-api-review-data-product-variant>` feeds

.. source-shopify-api-configure-access-to-tables-end

**To configure authorization access scopes for Amperity**

.. source-shopify-api-configure-access-to-tables-steps-start

Follow the steps outlined within |source-name| documentation to `enable the required scopes <https://help.shopify.com/en/manual/apps/custom-apps#update-admin-api-scopes-for-a-custom-app>`__ |ext_link| for your instance of |source-name|.

#. Open the **Apps and sales channels** page in your |source-name| admin console.
#. Click **Develop**, and then the name of the app you are using with Amperity.
#. Click **Configuration**, and then in the **Admin API integration** section click **Edit**.
#. Amperity requires the following authorization access scopes to be enabled:

   **read_customers**

   **read_orders**

   **read_products**

   **locations_read**
#. Click **Save**.

.. source-shopify-api-configure-access-to-tables-steps-end


.. _source-shopify-api-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-shopify-api-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Select the user account you added that is associated with :ref:`authorization access scopes <source-shopify-api-configure-authorization-access-scopes>`.
#. Select the checkbox next to the table name to pull that table to Amperity from |source-name|. You may select the following tables: **Customer**, **Customer Address**, **Discount Allocations**, **Locations**, **Order**, **Order Line**, **Order Line Refund**, **Product**, and **Product Variant**.
#. Click **Create**.

.. source-shopify-api-add-courier-steps-end


.. _source-shopify-api-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-shopify-api-review-data:

Review feed and domain table
==================================================

.. source-shopify-api-review-data-start

After running the |source-name| courier it creates a series of feeds and domain tables. Review the records for each domain table to ensure the right data was loaded from |source-name|.

.. source-shopify-api-review-data-end


.. _source-shopify-api-review-data-customer:

Customer
--------------------------------------------------

.. source-shopify-api-review-data-customer-start

The feed and domain table for customer details contains the following fields:

* **created_at**
* **currency**
* **email** Assigned the **email** semantic tag.
* **first_name** Assigned the **given-name** semantic tag.
* **id** Assigned the **ck** semantic tag.
* **last_name** Assigned the **surname** semantic tag.
* **last_order_id**
* **last_order_name**
* **multipass_identifier**
* **note**
* **orders_count**
* **phone** Assigned the **phone** semantic tag.
* **state**
* **tags**
* **tax_exempt**
* **total_spent**
* **updated_at**
* **verified_email**

.. source-shopify-api-review-data-customer-end


.. _source-shopify-api-review-data-customer-address:

Customer address
--------------------------------------------------

.. source-shopify-api-review-data-customer-address-start

The feed and domain table for customer addresses contains the following fields:

* **address1** Assigned the **address** semantic tag.
* **address2** Assigned the **address2** semantic tag.
* **city** Assigned the **city** semantic tag.
* **company** Assigned the **company** semantic tag.
* **country** Assigned the **country** semantic tag.
* **country_code**
* **country_name**
* **customer_id** Assigned the **ck** semantic tag.
* **default**
* **first_name** Assigned the **given-name** semantic tag.
* **id**
* **last_name** Assigned the **surname** semantic tag.
* **phone** Assigned the **phone** semantic tag.
* **province** Assigned the **state** semantic tag.
* **province_code**
* **zip** Assigned the **postal** semantic tag.

.. source-shopify-api-review-data-customer-address-end


.. _source-shopify-api-review-data-customer-tags:

Customer tags
--------------------------------------------------

.. source-shopify-api-review-data-customer-tags-start

The feed and domain table for customer tags contains the following fields:

* **customer_id**
* **value**

.. source-shopify-api-review-data-customer-tags-end


.. _source-shopify-api-review-data-discount-allocation:

Discount allocation
--------------------------------------------------

.. source-shopify-api-review-data-discount-allocation-start

The feed and domain table for discount allocations contains the following fields:

* **amount**
* **discount_allocation_index**
* **order_line_id** Assigned the **ck** and **pk** semantic tags.

.. source-shopify-api-review-data-discount-allocation-end


.. _source-shopify-api-review-data-discount-codes:

Discount codes
--------------------------------------------------

.. source-shopify-api-review-data-discount-codes-start

The feed and domain table for discount codes contains the following fields:

* **amount**
* **code**
* **order_id** Assigned the **ck** and **pk** semantic tags.
* **type**

.. source-shopify-api-review-data-discount-codes-end


.. _source-shopify-api-review-data-locations:

Locations
--------------------------------------------------

.. source-shopify-api-review-data-locations-start

The feed and domain table for locations contains the following fields:

* **active**
* **address1** Assigned the **addresss** semantic tag.
* **address2** Assigned the **addresss2** semantic tag.
* **city**
* **country**
* **country_code**
* **country_name**
* **created_at**
* **id**
* **legacy**
* **localized_country_name**
* **localized_province_name**
* **name**
* **phone**
* **province**
* **province_code**
* **province_name**
* **zip**

.. source-shopify-api-review-data-locations-end


.. _source-shopify-api-review-data-order:

Order
--------------------------------------------------

.. source-shopify-api-review-data-order-start

The feed and domain table for orders contains the following fields:

* **app_id**
* **browser_ip**
* **buyer_accepts_marketing**
* **cancel_reason**
* **canceled_at**
* **cart_token**
* **checkout_token**
* **closed_at**
* **created_at**
* **currency**
* **current_subtotal_price**
* **current_total_discounts**
* **current_total_price**
* **current_total_tax**
* **customer_id**
* **customer_locale**
* **email**
* **estimated_taxes**
* **financial_status**
* **fulfillment_status**
* **id**
* **landing_site**
* **location_id**
* **name**
* **note**
* **number**
* **order_number**
* **phone**
* **presentment_currency**
* **processed_at**
* **processing_method**
* **referring_site**
* **source_name**
* **source_identifier**
* **source_url**
* **subtotal_price**
* **tags**
* **taxes_included**
* **test**
* **token**
* **total_discounts**
* **total_line_items_price**
* **total_outstanding**
* **total_price**
* **total_tax**
* **total_tip_received**
* **total_weight**
* **updated_at**
* **user_id**

.. source-shopify-api-review-data-order-end


.. _source-shopify-api-review-data-order-line:

Order line
--------------------------------------------------

.. source-shopify-api-review-data-order-line-start

The feed and domain table for order lines contains the following fields:

* **fulfillable_quantity**
* **fulfillment_service**
* **fulfillment_status**
* **gift_card**
* **grams**
* **id**
* **name**
* **order_id**
* **price**
* **product_id**
* **quantity**
* **requires_shipping**
* **sku**
* **taxable**
* **title**
* **total_discount**
* **variant_id**
* **variant_title**
* **vendor**

.. source-shopify-api-review-data-order-line-end


.. _source-shopify-api-review-data-order-line-refund:

Order line refund
--------------------------------------------------

.. source-shopify-api-review-data-order-line-refund-start

The feed and domain table for order line refunds contains the following fields:

* **id**
* **line_item_id**
* **location_id**
* **subtotal**
* **refund_id**
* **restock_type**
* **quantity**
* **total_tax**

.. source-shopify-api-review-data-order-line-refund-end


.. _source-shopify-api-review-data-order-tags:

Order tags
--------------------------------------------------

.. source-shopify-api-review-data-order-tags-start

The feed and domain table for order tags contains the following fields:

* **order_id** Assigned the **ck** and **pk** semantic tags.
* **value**

.. source-shopify-api-review-data-order-tags-end


.. _source-shopify-api-review-data-product:

Product
--------------------------------------------------

.. source-shopify-api-review-data-product-start

The feed and domain table for products contains the following fields:

* **body_html**
* **created_at**
* **handle**
* **id** Assigned the **pc/product-id** semantic tag.
* **product_type**
* **published_at**
* **published_scope**
* **status**
* **tags**
* **template_suffix**
* **title**
* **updated_at**
* **vendor**

.. source-shopify-api-review-data-product-end


.. _source-shopify-api-review-data-product-tags:

Product tags
--------------------------------------------------

.. source-shopify-api-review-data-product-tags-start

The feed and domain table for product tags contains the following fields:

* **product_id** Assigned the **ck** and **pk** semantic tags.
* **value**

.. source-shopify-api-review-data-product-tags-end


.. _source-shopify-api-review-data-product-variant:

Product variant
--------------------------------------------------

.. source-shopify-api-review-data-product-variant-start

The feed and domain table for product variants contains the following fields:

* **barcode**
* **compare_at_price**
* **created_at**
* **fulfillment_service**
* **grams**
* **id**
* **inventory_item_id**
* **inventory_management**
* **inventory_policy**
* **inventory_quantity**
* **option1**
* **option2**
* **option3**
* **position**
* **price**
* **product_id**
* **requires_shipping**
* **sku**
* **taxable**
* **title**
* **updated_at**
* **weight**
* **weight_unit**

.. source-shopify-api-review-data-product-variant-end


.. _source-shopify-api-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
