.. https://docs.amperity.com/operator/


.. |source-name| replace:: Adobe Commerce
.. |plugin-name| replace:: Adobe Commerce
.. |feed-name| replace:: Profiles
.. |filter-the-list| replace:: "adob"
.. |example-filename| replace:: tablename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |source-interface| replace:: the Adobe Commerce database
.. |what-pull| replace:: customer profiles and transaction histories


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Adobe Commerce.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Adobe Commerce.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Adobe Commerce

==================================================
Pull from Adobe Commerce
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-adobe-commerce-start
   :end-before: .. term-adobe-commerce-end

.. source-adobe-commerce-context-start

|source-name| is source of high quality data for both customer records *and* interaction records, including:

* Customer profiles
* Customer addresses
* Customer group
* Order details
* The addresses to which orders are shipped
* The items within each order

.. source-adobe-commerce-context-end

.. source-adobe-commerce-aka-magento-start

.. note:: |source-name| was previously known as Magento.

.. source-adobe-commerce-aka-magento-end

.. source-adobe-commerce-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-adobe-commerce-get-details>`
#. :ref:`Configure credentials <source-adobe-commerce-credentials>`
#. :ref:`Add data source and feeds <source-adobe-commerce-add-courier>`
#. :ref:`Review feeds and domain tables <source-adobe-commerce-review-data>`

.. source-adobe-commerce-steps-to-pull-end


.. _source-adobe-commerce-get-details:

Get details
==================================================

.. source-adobe-commerce-get-details-start

|source-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The hostname or IP address for the |source-name| storefront.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - |source-name| uses `OAuth-based credentials <https://devdocs.magento.com/guides/v2.3/get-started/authentication/gs-authentication-oauth.html>`__ |ext_link|, which requires all of the following settings:

       * The consumer key and consumer secret.
       * The access token and access token secret.


.. tip:: Use SnapPass to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-adobe-commerce-get-details-end


.. _source-adobe-commerce-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials.rst
   :start-after: .. credentials-sources-intro-start
   :end-before: .. credentials-sources-intro-end

**To configure credentials**

.. source-adobe-commerce-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-start
          :end-before: .. credentials-sources-configure-end

       .. image:: ../../images/mockup-sources-add-01-select-source.png
          :width: 380 px
          :alt: Add credentials for a data source.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-options-start
          :end-before: .. credentials-sources-configure-options-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-already-configured-start
          :end-before: .. credentials-sources-configure-already-configured-end

       .. image:: ../../images/mockup-credentials-add-01-select-adobe-commerce.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Add the hostname or IP address for the |source-name| storefront, the consumer key and consumer secret, and the access token and access token secret.

       .. image:: ../../images/mockup-credentials-add-01-settings-adobe-commerce.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-click-continue-start
          :end-before: .. credentials-sources-configure-click-continue-end

.. source-adobe-commerce-credentials-steps-end


.. _source-adobe-commerce-add-courier:

Add data source and feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-adobe-commerce-add-courier-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-add-source-start
          :end-before: .. sources-add-source-end

       .. image:: ../../images/mockup-sources-add-01-select-source.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-options-start
          :end-before: .. credentials-sources-configure-options-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-already-configured-start
          :end-before: .. credentials-sources-configure-already-configured-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - On the **Add courier** page, under **Select data to ingest**, enable one or more data sets to pull to Amperity:

       * **Customers**
       * **Customer Address**
       * **Customer Group**
       * **Orders**
       * **Order Address**
       * **Order Items**

       When finished, click **Create**.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-run-the-courier-start
          :end-before: .. sources-run-the-courier-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-verify-feeds-and-domain-tables-start
          :end-before: .. sources-verify-feeds-and-domain-tables-end

.. source-adobe-commerce-add-courier-steps-end


.. _source-adobe-commerce-review-data:

Review feeds and domain tables
==================================================

.. source-adobe-commerce-review-data-start

After running the |source-name| courier it creates a series of feeds and domain tables. Review the records for each domain table to ensure the right data was loaded from |source-name|.

.. source-adobe-commerce-review-data-end


.. _source-adobe-commerce-review-data-customers:

Customers
--------------------------------------------------

.. source-adobe-commerce-review-data-customer-start

The feed and domain table for customer details contains the following fields:

* **CREATED_AT**
* **CREATED_IN**
* **DEFAULT_BILLING**
* **DEFAULT_SHIPPING**
* **DISABLE_AUTO_GROUP_CHANGE**
* **EMAIL**
* **ENTITY_ID**
* **FIRSTNAME**
* **GROUP_ID**
* **LASTNAME**
* **STORE_ID**
* **UPDATED_AT**
* **WEBSITE_ID**

You may choose to apply customer profile semantic tags to the columns in this table.

.. source-adobe-commerce-review-data-customer-end


.. _source-adobe-commerce-review-data-customer-address:

Customer address
--------------------------------------------------

.. source-adobe-commerce-review-data-customer-address-start

The feed and domain table for customer addresses contains the following fields:

* **CITY**
* **COUNTRY_ID**
* **ENTITY_ID**
* **FIRSTNAME**
* **LASTNAME**
* **PARENT_ID**
* **POSTCODE**
* **REGION**
* **REGION_ID**
* **STREET**
* **TELEPHONE**
* **UPDATED_AT**

You may choose to apply customer profile semantic tags to the columns in this table.

.. source-adobe-commerce-review-data-customer-address-end


.. _source-adobe-commerce-review-data-customer-group:

Customer group
--------------------------------------------------

.. source-adobe-commerce-review-data-customer-group-start

The feed and domain table for customer group contains the following fields:

* **CODE**
* **CUSTOMER_GROUP_ID**
* **TAX_CLASS_ID**
* **TAX_CLASS_NAME**
* **VIP_DATA**

.. source-adobe-commerce-review-data-customer-group-end


.. _source-adobe-commerce-review-data-orders:

Orders
--------------------------------------------------

.. source-adobe-commerce-review-data-orders-start

The feed and domain table for orders contains the following fields:

* **ADJUSTMENT_NEGATIVE**
* **ADJUSTMENT_POSITIVE**
* **APPLIED_RULE_IDS**
* **BASE_ADJUSTMENT_NEGATIVE**
* **BASE_ADJUSTMENT_POSITIVE**
* **BASE_CURRENCY_CODE**
* **BASE_DISCOUNT_AMOUNT**
* **BASE_DISCOUNT_CANCELED**
* **BASE_DISCOUNT_INVOICED**
* **BASE_DISCOUNT_REFUNDED**
* **BASE_DISCOUNT_TAX_COMPENSATION_AMOUNT**
* **BASE_DISCOUNT_TAX_COMPENSATION_INVOICED**
* **BASE_DISCOUNT_TAX_COMPENSATION_REFUNDED**
* **BASE_GRAND_TOTAL**
* **BASE_SHIPPING_AMOUNT**
* **BASE_SHIPPING_CANCELED**
* **BASE_SHIPPING_DISCOUNT_AMOUNT**
* **BASE_SHIPPING_DISCOUNT_TAX_COMPENSATION_AMNT**
* **BASE_SHIPPING_INCL_TAX**
* **BASE_SHIPPING_INVOICED**
* **BASE_SHIPPING_REFUNDED**
* **BASE_SHIPPING_TAX_AMOUNT**
* **BASE_SHIPPING_TAX_REFUNDED**
* **BASE_SUBTOTAL**
* **BASE_SUBTOTAL_CANCELED**
* **BASE_SUBTOTAL_INVOICED**
* **BASE_SUBTOTAL_REFUNDED**
* **BASE_TAX_AMOUNT**
* **BASE_TAX_CANCELED**
* **BASE_TAX_INVOICED**
* **BASE_TAX_REFUNDED**
* **BASE_TO_GLOBAL_RATE**
* **BASE_TO_ORDER_RATE**
* **BASE_TOTAL_CANCELED**
* **BASE_TOTAL_DUE**
* **BASE_TOTAL_INVOICED**
* **BASE_TOTAL_INVOICED_COST**
* **BASE_TOTAL_ONLINE_REFUNDED**
* **BASE_TOTAL_REFUNDED**
* **BASE_TOTAL_PAID**
* **BILLING_ADDRESS_ID**
* **COUPON_CODE**
* **CREATED_AT**
* **CUSTOMER_GENDER**
* **CUSTOMER_EMAIL**
* **CUSTOMER_FIRSTNAME**
* **CUSTOMER_GROUP_ID**
* **CUSTOMER_ID**
* **CUSTOMER_IS_GUEST**
* **CUSTOMER_LASTNAME**
* **CUSTOMER_NOTE_NOTIFY**
* **DISCOUNT_AMOUNT**
* **DISCOUNT_CANCELED**
* **DISCOUNT_DESCRIPTION**
* **DISCOUNT_INVOICED**
* **DISCOUNT_REFUNDED**
* **DISCOUNT_TAX_COMPENSATION_AMOUNT**
* **DISCOUNT_TAX_COMPENSATION_INVOICED**
* **DISCOUNT_TAX_COMPENSATION_REFUNDED**
* **EMAIL_SENT**
* **ENTITY_ID**
* **GLOBAL_CURRENCY_CODE**
* **GRAND_TOTAL**
* **INCREMENT_ID**
* **IS_VIRTUAL**
* **ORDER_CURRENCY_CODE**
* **PROTECT_CODE**
* **QUOTE_ID**
* **REMOTE_IP**
* **STATUS**
* **SHIPPING_AMOUNT**
* **SHIPPING_DESCRIPTION**
* **SHIPPING_CANCELED**
* **SHIPPING_DISCOUNT_AMOUNT**
* **SHIPPING_DISCOUNT_TAX_COMPENSATION_AMOUNT**
* **SHIPPING_INCL_TAX**
* **SHIPPING_INVOICED**
* **SHIPPING_REFUNDED**
* **SHIPPING_TAX_AMOUNT**
* **SHIPPING_TAX_REFUNDED**
* **STATE**
* **STORE_CURRENCY_CODE**
* **STORE_NAME**
* **STORE_ID**
* **STORE_TO_BASE_RATE**
* **STORE_TO_ORDER_RATE**
* **SUBTOTAL**
* **SUBTOTAL_CANCELED**
* **SUBTOTAL_INCL_TAX**
* **SUBTOTAL_INVOICED**
* **SUBTOTAL_REFUNDED**
* **TAX_AMOUNT**
* **TAX_CANCELED**
* **TAX_INVOICED**
* **TAX_REFUNDED**
* **TOTAL_CANCELED**
* **TOTAL_DUE**
* **TOTAL_INVOICED**
* **TOTAL_ITEM_COUNT**
* **TOTAL_ONLINE_REFUNDED**
* **TOTAL_PAID**
* **TOTAL_QTY_ORDERED**
* **TOTAL_REFUNDED**
* **UPDATED_AT**
* **WEIGHT**
* **X_FORWARDED_FOR**

You may choose to apply itemized transaction semantic tags to the columns in this table.

.. source-adobe-commerce-review-data-orders-end


.. _source-adobe-commerce-review-data-order-address:

Order address
--------------------------------------------------

.. source-adobe-commerce-review-data-order-address-start

The feed and domain table for order address contains the following fields:

* **ADDRESS_TYPE**
* **CITY**
* **COMPANY**
* **COUNTRY_ID**
* **CUSTOMER_ADDRESS_ID**
* **EMAIL**
* **ENTITY_ID**
* **FIRSTNAME**
* **LASTNAME**
* **PARENT_ID**
* **POSTCODE**
* **QUOTE_ADDRESS_ID**
* **REGION**
* **REGION_CODE**
* **REGION_ID**
* **STREET**
* **TELEPHONE**

You may choose to apply customer profile semantic tags to the columns in this table.

.. source-adobe-commerce-review-data-order-address-end


.. _source-adobe-commerce-review-data-order-items:

Order items
--------------------------------------------------

.. source-adobe-commerce-review-data-order-items-start

The feed and domain table for order items contains the following fields:

* **AMOUNT_REFUNDED**
* **BASE_AMOUNT_REFUNDED**
* **BASE_DISCOUNT_AMOUNT**
* **BASE_DISCOUNT_INVOICED**
* **BASE_DISCOUNT_TAX_COMPENSATION_AMOUNT**
* **BASE_DISCOUNT_TAX_COMPENSATION_INVOICED**
* **BASE_ORIGINAL_PRICE**
* **BASE_PRICE**
* **BASE_PRICE_INCL_TAX**
* **BASE_ROW_INVOICED**
* **BASE_ROW_TOTAL**
* **BASE_ROW_TOTAL_INCL_TAX**
* **BASE_TAX_AMOUNT**
* **BASE_TAX_INVOICED**
* **CREATED_AT**
* **DISCOUNT_AMOUNT**
* **DISCOUNT_INVOICED**
* **DISCOUNT_PERCENT**
* **DISCOUNT_TAX_COMPENSATION_AMOUNT**
* **DISCOUNT_TAX_COMPENSATION_CANCELED**
* **FREE_SHIPPING**
* **IS_QTY_DECIMAL**
* **IS_VIRTUAL**
* **ITEM_ID**
* **NAME**
* **NO_DISCOUNT**
* **ORDER_ID**
* **ORIGINAL_PRICE**
* **PARENT_ITEM_ID**
* **PRODUCT_ID**
* **PRODUCT_OPTION**
* **PRODUCT_TYPE**
* **QTY_CANCELED**
* **QTY_ORDERED**
* **QTY_INVOICED**
* **QTY_REFUNDED**
* **QTY_RETURNED**
* **QTY_SHIPPED**
* **QUOTE_ITEM_ID**
* **ROW_INVOICED**
* **ROW_TOTAL**
* **PRICE**
* **PRICE_INCL_TAX**
* **ROW_WEIGHT**
* **ROW_TOTAL_INCL_TAX**
* **SKU**
* **STORE_ID**
* **TAX_AMOUNT**
* **TAX_CANCELED**
* **TAX_INVOICED**
* **TAX_PERCENT**
* **UPDATED_AT**
* **WEEE_TAX_APPLIED**
* **WEIGHT**

You may choose to apply itemized transaction semantic tags to the columns in this table.

.. source-adobe-commerce-review-data-order-items-end
