.. 
.. https://docs.amperity.com/datagrid/
.. 

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

.. source-shopify-context-start

Shopify is source of high quality data for both customer records *and* interaction records, including:

* Complete profile data, including full names, full addresses, email address, and phone number
* Orders, including order amounts, items and item quantities, location
* Prices and discounts
* Refunds and cancellations
* Product catalog details
* Abandoned carts
* Customer searches
* Guest checkout data, including email address and associated order details

.. source-shopify-context-end

.. source-shopify-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-shopify-get-details>`
#. :ref:`Configure authorization access scopes <source-shopify-configure-authorization-access-scopes>`
#. :ref:`Run courier <source-shopify-run-courier>`
#. :ref:`Review feed and domain table <source-shopify-review-data>`
#. :ref:`Add to courier group <source-shopify-add-to-courier-group>`

.. source-shopify-steps-to-pull-end


.. _source-shopify-get-details:

Get details
==================================================

.. source-shopify-get-details-start

#. Your |source-name| **Shop Name**.
#. A list of tables to be pulled to Amperity from |source-name|.

   This is done by configuring |source-name| to allow Amperity to |ext_shopify_rest_admin_api_read_data| using a set of authorization access scopes.

.. source-shopify-get-details-end


.. _source-shopify-configure-authorization-access-scopes:

Configure authorization access scopes
==================================================

.. source-shopify-configure-access-to-tables-start

You must configure read access within |source-name| to allow Amperity to pull data from tables. The following authorization access scopes must be enabled:

* |ext_shopify_rest_admin_api_scope_read_customers|, from which Amperity builds the :ref:`customer <source-shopify-review-data-customer>` and :ref:`customer address <source-shopify-review-data-customer-address>` feeds
* |ext_shopify_rest_admin_api_scope_read_orders|, from which Amperity builds the :ref:`order <source-shopify-review-data-order>` and :ref:`order line <source-shopify-review-data-order-line>` feeds
* |ext_shopify_rest_admin_api_scope_read_products|, from which Amperity builds the :ref:`product <source-shopify-review-data-product>` and :ref:`product variant <source-shopify-review-data-product-variant>` feeds

.. source-shopify-configure-access-to-tables-end

**To configure authorization access scopes for Amperity**

.. source-shopify-configure-access-to-tables-steps-start

Follow the steps outlined within |source-name| documentation to |ext_shopify_rest_admin_api_scopes_steps| for your instance of |source-name|.

#. Open the **Apps and sales channels** page in your |source-name| admin console.
#. Click **Develop**, and then the name of the app you are using with Amperity.
#. Click **Configuration**, and then in the **Admin API integration** section click **Edit**.
#. Amperity requires the following authorization access scopes to be enabled:

   **read_customers**

   **read_orders**

   **read_products**

   **locations_read**
#. Click **Save**.

.. source-shopify-configure-access-to-tables-steps-end


.. _source-shopify-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-shopify-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Select the user account you added that is associated with :ref:`authorization access scopes <source-shopify-configure-authorization-access-scopes>`.
#. Select the checkbox next to the table name to pull that table to Amperity from |source-name|. You may select the following tables: **Customer**, **Customer Address**, **Discount Allocations**, **Locations**, **Order**, **Order Line**, **Order Line Refund**, **Product**, and **Product Variant**.
#. Click **Create**.

.. source-shopify-add-courier-steps-end


.. _source-shopify-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-shopify-review-data:

Review feed and domain table
==================================================

.. source-shopify-review-data-start

After running the |source-name| courier it will create a series of feeds and domain tables. Review the records for each domain table to ensure the right data was loaded from |source-name|.

.. source-shopify-review-data-end


.. _source-shopify-review-data-customer:

Customer
--------------------------------------------------

.. source-shopify-review-data-customer-start

The feed and domain table for customer details will contain the following fields:

* **created_at**
* **currency**
* **email** (assigned the **email** semantic tag)
* **first_name** (assigned the **given-name** semantic tag)
* **id** (assigned the **ck** semantic tag)
* **last_name** (assigned the **surname** semantic tag)
* **last_order_id**
* **last_order_name**
* **multipass_identifier**
* **note**
* **orders_count**
* **phone** (assigned the **phone** semantic tag)
* **state**
* **tags**
* **tax_exempt**
* **total_spent**
* **updated_at**
* **verified_email**

.. source-shopify-review-data-customer-end


.. _source-shopify-review-data-customer-address:

Customer address
--------------------------------------------------

.. source-shopify-review-data-customer-address-start

The feed and domain table for customer addresses will contain the following fields:

* **address1** (assigned the **address** semantic tag)
* **address2** (assigned the **address2** semantic tag)
* **city** (assigned the **city** semantic tag)
* **company** (assigned the **company** semantic tag)
* **country** (assigned the **country** semantic tag)
* **country_code**
* **country_name**
* **customer_id** (assigned the **ck** semantic tag)
* **default**
* **first_name** (assigned the **given-name** semantic tag)
* **id**
* **last_name** (assigned the **surname** semantic tag)
* **phone** (assigned the **phone** semantic tag)
* **province** (assigned the **state** semantic tag)
* **province_code**
* **zip** (assigned the **postal** semantic tag)

.. source-shopify-review-data-customer-address-end


.. _source-shopify-review-data-customer-tags:

Customer tags
--------------------------------------------------

.. source-shopify-review-data-customer-tags-start

The feed and domain table for customer tags will contain the following fields:

* **customer_id**
* **value**

.. source-shopify-review-data-customer-tags-end


.. _source-shopify-review-data-discount-allocation:

Discount allocation
--------------------------------------------------

.. source-shopify-review-data-discount-allocation-start

The feed and domain table for discount allocations will contain the following fields:

* **amount**
* **discount_allocation_index**
* **order_line_id** (assigned the **ck** and **pk** semantic tags)

.. source-shopify-review-data-discount-allocation-end


.. _source-shopify-review-data-discount-codes:

Discount codes
--------------------------------------------------

.. source-shopify-review-data-discount-codes-start

The feed and domain table for discount codes will contain the following fields:

* **amount**
* **code**
* **order_id** (assigned the **ck** and **pk** semantic tags)
* **type**

.. source-shopify-review-data-discount-codes-end


.. _source-shopify-review-data-locations:

Locations
--------------------------------------------------

.. source-shopify-review-data-locations-start

The feed and domain table for locations will contain the following fields:

* **active**
* **address1** (assigned the **addresss** semantic tag)
* **address2** (assigned the **addresss2** semantic tag)
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

.. source-shopify-review-data-locations-end


.. _source-shopify-review-data-order:

Order
--------------------------------------------------

.. source-shopify-review-data-order-start

The feed and domain table for orders will contain the following fields:

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

.. source-shopify-review-data-order-end


.. _source-shopify-review-data-order-line:

Order line
--------------------------------------------------

.. source-shopify-review-data-order-line-start

The feed and domain table for order lines will contain the following fields:

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

.. source-shopify-review-data-order-line-end


.. _source-shopify-review-data-order-line-refund:

Order line refund
--------------------------------------------------

.. source-shopify-review-data-order-line-refund-start

The feed and domain table for order line refunds will contain the following fields:

* **id**
* **line_item_id**
* **location_id**
* **subtotal**
* **refund_id**
* **restock_type**
* **quantity**
* **total_tax**

.. source-shopify-review-data-order-line-refund-end


.. _source-shopify-review-data-order-tags:

Order tags
--------------------------------------------------

.. source-shopify-review-data-order-tags-start

The feed and domain table for order tags will contain the following fields:

* **order_id** (assigned the **ck** and **pk** semantic tags)
* **value**

.. source-shopify-review-data-order-tags-end


.. _source-shopify-review-data-product:

Product
--------------------------------------------------

.. source-shopify-review-data-product-start

The feed and domain table for products will contain the following fields:

* **body_html**
* **created_at**
* **handle**
* **id** (assigned the **pc/product-id** semantic tag)
* **product_type**
* **published_at**
* **published_scope**
* **status**
* **tags**
* **template_suffix**
* **title**
* **updated_at**
* **vendor**

.. source-shopify-review-data-product-end


.. _source-shopify-review-data-product-tags:

Product tags
--------------------------------------------------

.. source-shopify-review-data-product-tags-start

The feed and domain table for product tags will contain the following fields:

* **product_id** (assigned the **ck** and **pk** semantic tags)
* **value**

.. source-shopify-review-data-product-tags-end


.. _source-shopify-review-data-product-variant:

Product variant
--------------------------------------------------

.. source-shopify-review-data-product-variant-start

The feed and domain table for product variants will contain the following fields:

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

.. source-shopify-review-data-product-variant-end


.. _source-shopify-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
