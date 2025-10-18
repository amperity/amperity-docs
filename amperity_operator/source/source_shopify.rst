.. https://docs.amperity.com/operator/


.. |source-name| replace:: Shopify
.. |plugin-name| replace:: Shopify
.. |feed-name| replace:: Customers
.. |example-filename| replace:: tablename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |source-interface| replace:: the `Shopify REST Admin API <https://shopify.dev/docs/admin-api/rest/reference>`__ |ext_link|
.. |what-pull| replace:: customer records and interaction records


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
#. :ref:`Add courier <source-shopify-add-courier>`
#. :ref:`Get sample tables <source-shopify-get-sample-tables>`
#. :ref:`Add feeds <source-shopify-add-feeds>`
#. :ref:`Add load operations <source-shopify-add-load-operations>`
#. :ref:`Run courier <source-shopify-run-courier>`
#. :ref:`Add to courier group <source-shopify-add-to-courier-group>`

.. source-shopify-steps-to-pull-end


.. _source-shopify-get-details:

Get details
==================================================

.. source-shopify-get-details-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-details-fivetran-overview-start
   :end-before: .. sources-get-details-fivetran-overview-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-details-fivetran-request-to-enable-start
   :end-before: .. sources-get-details-fivetran-request-to-enable-end

The |source-name| data source requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: center
          :class: no-scaled-link
     - Permission to connect FiveTran to Shopify.

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-get-details-fivetran-connect-start
          :end-before: .. sources-get-details-fivetran-connect-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-get-details-fivetran-does-not-store-data-start
          :end-before: .. sources-get-details-fivetran-does-not-store-data-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: center
          :class: no-scaled-link
     - A Shopify shop name, which is the same as ``shop-name`` in your Shopify URL: ``shop-name.myshopify.com``.

       .. important:: Each unique shop name must be configured as a data source.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: center
          :class: no-scaled-link
     - A Shopify username for an account with permission to `read data from the Shopify Admin API <https://shopify.dev/docs/admin-api/access-scopes>`__ |ext_link|, specifically, the ability to ``read_all_orders``, ``read_customers``, ``read_draft_orders``, ``read_fulfillments``, ``read_inventory``, ``read_price_rules``, ``read_product``, and ``read_shipping``.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail four.
          :align: center
          :class: no-scaled-link
     - The passphrase for the Shopify username.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-get-details-fivetran-access-to-snowflake-start
          :end-before: .. sources-get-details-fivetran-access-to-snowflake-start

       Shopify data tables typically include: **Collection**, **Collection_Product**, **Customer**, **Customer_Address**, **Order**, **Order_Adjustment**, **Order_Line**, **Order_Line_Refund**, **Order_Shipping_Line**, **Product**, **Product_Variant**, **Refund**, and **Transactions**.

.. source-shopify-get-details-end


.. _source-shopify-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-consolidate-start
   :end-before: .. sources-add-courier-fivetran-consolidate-end

**Example table list**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-table-list-start
   :end-before: .. sources-add-courier-fivetran-table-list-end

.. source-shopify-add-courier-example-table-list-start

For example:

::

   [
     "AMPERITY_A1BO987C.SHOPIFY_ACME.CUSTOMER",
     "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER",
     "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER_LINE",
     "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER_SHIPPING_LINE",
     "AMPERITY_A1BO987C.SHOPIFY_ACME.PRODUCT",
     "AMPERITY_A1BO987C.SHOPIFY_ACME.TRANSACTION",
   ]

.. source-shopify-add-courier-example-table-list-end

**Example stage name**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-stage-name-start
   :end-before: .. sources-add-courier-fivetran-stage-name-end

.. source-shopify-add-courier-example-stage-name-start

For example:

::

   AMPERITY_A1BO987C.SHOPIFY_ACME.ACME_STAGE

.. source-shopify-add-courier-example-stage-name-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-load-operation-start
   :end-before: .. sources-add-courier-fivetran-load-operation-end

.. source-shopify-add-courier-example-load-operation-start

For example:

::

   {
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.CUSTOMER"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER_LINE"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER_SHIPPING_LINE"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.PRODUCT"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.TRANSACTION"
       }
     ]
   }

.. source-shopify-add-courier-example-load-operation-end

**To add a courier for Snowflake table objects**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-start
   :end-before: .. sources-add-courier-fivetran-end


.. _source-shopify-get-sample-tables:

Get sample tables
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-fivetran-start
   :end-before: .. sources-get-sample-files-fivetran-end


.. _source-shopify-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-note-file-start
   :end-before: .. sources-add-feed-note-file-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-shopify-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-fivetran-start
   :end-before: .. sources-add-load-operation-example-intro-fivetran-end

.. source-shopify-add-load-operations-example-start

For example:

::

   {
     "df-A1B2C3": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.CUSTOMER"
       }
     ],
     "df-D4E5F6": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER"
       }
     ],
     "df-G7H8I9": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER_LINE"
       }
     ],
     "df-J0K1L2": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.ORDER_SHIPPING_LINE"
       }
     ],
     "df-M3N4O5": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.PRODUCT"
       }
     ],
     "df-P6Q7R8": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.SHOPIFY_ACME.TRANSACTION"
       }
     ]
   }

.. source-shopify-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


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
