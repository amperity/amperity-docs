.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Which customers made their first order during the specified date range?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which customers made their first order during the specified date range?

.. meta::
    :content class=swiftype name=title data-type=string:
        First order

==================================================
First order
==================================================

.. attribute-compound-first-order-start

**First Order** returns a list of customers who made their first order during your chosen date range. For example, return all customers whose first order was during the previous 12 months:

.. image:: ../../images/attribute-compound-first-order-example.png
   :width: 600 px
   :alt: Customers who bought a blue shirt within the previous 12 months.
   :align: left
   :class: no-scaled-link

After you specify a date range you may apply filters to associate first purchases with specific products, brands, channels, and stores. For example, return all customers who purchased a blue shirt from your website.

.. attribute-compound-first-order-end


.. _attribute-compound-first-order-howitworks:

How this attribute works
==================================================

.. attribute-compound-first-order-howitworks-start

**First Order** represents a common approach people use when they build segments: find all of my customers who made their first order in the past N days, months, or years, and then associate that list of customers to your products and brands.

**First Order** is a *compound attribute*, which means that it's built from a combination of attributes that already exist in your data, and then appears as a single attribute that you can choose from the **Segment Editor**.

With this attribute, you can focus less on SQL and more on finding answers that align to your marketing goals and strategies. Purchase behavior attributes simplify the number of steps that are required to associate a list of customers to your products, stores, channels, and brands.

.. attribute-compound-first-order-howitworks-end

.. attribute-compound-first-order-howitworks-compound-start

.. admonition:: How does the SQL for First Order work?

   **First Order** is built from standard columns that are output by Amperity. The following example returns a list of customers whose first order was a blue shirt that they purchased online within the previous 12 months:
   
   .. image:: ../../images/attribute-compound-first-order-example.png
      :width: 500 px
      :alt: Customers who bought a blue shirt within the previous 12 months.
      :align: left
      :class: no-scaled-link

   The SQL for **First Order** works like this. It uses order datetime from the **Unified Itemized Transactions** table as its starting point:

   ::

      SELECT
        amperity_id
        ,order_datetime
        ,RANK() OVER (PARTITION BY amperity_id ORDER BY order_datetime, order_id) AS order_rank
      FROM Unified_Itemized_Transactions

   then uses the |sql_presto_function_rank| function to identify which of those orders were a customer's first order, and then returns all items that match two conditions: order rank and a date range:

   ::

      WHERE order_rank = 1
      AND order_datetime < DATE_TRUNC('day', CURRENT_TIMESTAMP - interval '12' month)

   In this example, only transactions that occurred within the previous 12 months *and* are a customer's first order are returned.

   Returns and cancellations are filtered out automatically, like this:

   ::

      AND (is_return IS NULL OR (NOT is_return))
      AND (is_cancellation IS NULL OR (NOT is_cancellation))

   You may then filter this list of customers more by applying any of the product, purchase, and store filters. When you select these filters, they are added to the WHERE statement, like this:

   ::

      AND product_category = 'shirt'
      AND product_subcategory = 'blue'
      AND purchase_channel = 'online'

   *and* they are added to the SELECT statement, like this:

   ::

      SELECT
        amperity_id
        ,order_datetime
        product_category = 'shirt'
        product_subcategory = 'blue'
        purchase_channel = 'online'
        ,RANK() OVER (PARTITION BY amperity_id ORDER BY order_datetime, order_id) AS order_rank
      FROM Unified_Itemized_Transactions

   Why are these attributes added to the WHERE statement *and* the SELECT statement? They are added to the SELECT statement to ensure that the correct ranking is applied to products, purchases, and stores *before* you apply product, purchase, and store filters to your segment.

.. attribute-compound-first-order-howitworks-compound-end

.. attribute-compound-first-order-view-the-real-sql-start

The SQL for **First Order** is more complex than what is described in the previous section. This is due to the way this attribute returns *only* a list of Amperity IDs, uses a series of common table expressions (CTEs), and takes advantage of workflows that Amperity does behind the scenes to pre-filter the product, purchase, and store attributes.

You can view the full SQL for **First Order** from the **Segment Editor**. Start a new segment and add only this attribute (along with any required conditions and filter attributes), and then click the **View SQL** link at the top of the page.

.. attribute-compound-first-order-view-the-real-sql-end


.. _attribute-compound-first-order-segments:

Add to segments
==================================================

.. attribute-compound-first-order-segments-start

To find all customers who made their first order within a specified date range, start with the **First Order** attribute located under **Purchase behaviors**:

.. attribute-compound-first-order-segments-end

.. image:: ../../images/attribute-compound-first-order.png
   :width: 600 px
   :alt: Use the first order attribute to find first orders by date range.
   :align: left
   :class: no-scaled-link

.. attribute-compound-first-order-segments-filters-start

After the attribute appears in your segment, choose a date range:

.. image:: ../../images/attribute-compound-first-order-example.png
   :width: 600 px
   :alt: Customers who bought a blue shirt within the previous 12 months.
   :align: left
   :class: no-scaled-link

After you choose a date range you may apply filters to associate these customers to specific products, brands, channels, and stores.

.. attribute-compound-first-order-segments-filters-end


.. _attribute-compound-first-order-relative-dates:

About relative dates
--------------------------------------------------

.. include:: ../../amperity_reference/source/segments_editor.rst
   :start-after: .. segments-editor-relative-dates-start
   :end-before: .. segments-editor-relative-dates-end

**Relative date values**

.. include:: ../../amperity_reference/source/segments_editor.rst
   :start-after: .. segments-editor-relative-date-values-start
   :end-before: .. segments-editor-relative-date-values-end


.. _attribute-compound-first-order-conditions:

Available conditions
==================================================

.. attribute-compound-first-order-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **was after**
     - |attribute-recommended| **More useful**

       Returns a list of customers whose first purchases were after the specified time window.

   * - **was before**
     - |attribute-recommended| **More useful**

       Returns a list of customers whose first purchases were before the specified time window.

   * - **was between**
     - |attribute-recommended| **More useful**

       Returns a list of customers whose first purchases were between two specified time windows.

   * - **was not between**
     - |attribute-stop| **Less useful**

       Returns a list of customers whose first purchases were not between two specified time windows.

   * - **was not on**
     - |attribute-stop| **Less useful**

       Returns a list of customers whose first purchases were not on the specified time.

   * - **was on**
     - Returns a list of customers whose first purchases were on the specified time.

.. attribute-compound-first-order-conditions-end


.. _attribute-compound-first-order-filter-attributes:

Filter attributes
==================================================

.. attribute-compound-first-order-filter-attributes-start

A filter attribute is a standard column that is output by Amperity and is available from the **Unified Itemized Transactions** table. When a filter attribute is associated with a purchase behavior attribute, you may use them to filter the results by specific items in your product catalog, such as by brand, by channel, by store, or by specific details about the items in your product catalog, such as color, SKU, and so on. The list of filter attributes that will be available for product catalogs depends on their availability within your **Unified Itemized Transactions** table.

.. attribute-compound-first-order-filter-attributes-end
