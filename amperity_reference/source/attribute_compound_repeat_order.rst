.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Who made a repeat purchase during the specified date range?

.. meta::
    :content class=swiftype name=body data-type=text:
        Who made a repeat purchase during the specified date range?

.. meta::
    :content class=swiftype name=title data-type=string:
        Repeat order

==================================================
Repeat order
==================================================

.. attribute-compound-repeat-order-start

**Repeat Order** returns a list of customers who have made a repeat purchase during the chosen date range. For example, return all customers who made a repeat purchase within the previous 6 months:

.. image:: ../../images/attribute-compound-repeat-order-example.png
   :width: 600 px
   :alt: Customers who own the base game and need to buy an expansion pack.
   :align: left
   :class: no-scaled-link

.. important:: **Repeat Order** identifies a repeat purchase by comparing purchases within the chosen date range to all purchases. For example, a customer who first purchased 2 years ago, and then purchased again last month would be returned by a relative date range "today - 1 month". A customer who first purchased 10 years ago, and then purchased again last month would also be returned. As well as a customer who first purchased 2 months ago, and then purchased again last month.

After you specify a date range you may apply filters to associate repeat orders to specific products, brands, channels, and stores. For example, return all customers who made a repeat purchase of shoes from your ACME Footwear brand.

.. attribute-compound-repeat-order-end


.. _attribute-compound-repeat-order-howitworks:

How this attribute works
==================================================

.. attribute-compound-repeat-order-howitworks-start

**Repeat Order** represents a common approach people use when they build segments: find customers who have purchased more than one time within a time window, and then associate those customers to specific products and brands.

**Repeat Order** is a *compound attribute*, which means that it's built from a combination of attributes that already exist in your data, and then appears as a single attribute that you can choose from the **Segment Editor**.

With this attribute, you can focus less on SQL and more on finding answers that align to your marketing goals and strategies. Purchase behavior attributes simplify the number of steps that are required to associate a list of customers to your products, stores, channels, and brands.

.. attribute-compound-repeat-order-howitworks-end

.. attribute-compound-repeat-order-howitworks-compound-start

.. admonition:: How does the SQL for Repeat Order work?

   **Repeat Order** is built from standard columns that are output by Amperity. The following example returns a list of customers who have purchased at least one component of a game during the previous 3 years:

   .. image:: ../../images/attribute-compound-repeat-order-example.png
      :width: 500 px
      :alt: Customers who own the base game and need to buy an expansion pack.
      :align: left
      :class: no-scaled-link

   The SQL for **Repeat Order** works like this. It uses two common table expressions (CTEs) to find two lists: a list of first orders and a list of distinct orders.

   To build the list of first orders, **Repeat Order** uses order datetime from the **Unified Itemized Transactions** table as its starting point:

   ::

      SELECT
        amperity_id
        ,order_datetime AS first_order_datetime
        ,RANK() OVER (PARTITION BY amperity_id ORDER BY order_datetime, order_id) AS order_rank
      FROM Unified_Itemized_Transactions

   then uses the |sql_presto_function_rank| function to identify which of those orders were repeat orders, and then returns all items that match two conditions: order rank and a date range:

   ::

      WHERE order_rank = 1
      AND order_datetime < DATE_TRUNC('day', CURRENT_TIMESTAMP - interval '36' month)

   This returns the first order for all customers who purchased during the previous 3 years.

   Returns and cancellations are filtered out automatically, like this:

   ::

      AND (is_return IS NULL OR (NOT is_return))
      AND (is_cancellation IS NULL OR (NOT is_cancellation))

   To build the list of distinct orders, **Repeat Order** uses order datetime from the **Unified Itemized Transactions** table to find all of the distinct orders that were made during the same time period:

   ::

      SELECT DISTINCT
        uit.amperity_id
      FROM (
        SELECT
          amperity_id
          ,order_datetime AS distinct_order_datetime
        FROM Unified_Itemized_Transactions
      )

   To identify which customers made a repeat purchase during this time window, the first order CTE is joined to the distinct order CTE:

   ::

      INNER JOIN first_order_datetime
      ON distinct_order_datetime

   (Note that "first_order_datetime" and "distinct_order_datetime" names do not represent the real names of the CTEs that are joined; these names identify the two sources that are joined together as part of the steps within the SQL that identify your repeat customers.)

   Returns and cancellations are then filtered out automatically, like this:

   ::

      AND (
        is_return IS NULL
        OR (NOT is_return)
      )

   You may then filter this list of customers more by applying any of the product, purchase, and store filters. When you select these filters, they are added to the WHERE statement, like this:

   ::

      AND product_category = 'game'
      AND product_subcategory IN ('base', 'expansion', 'pack')
      AND purchase_brand = 'Fearless Creatures'

.. attribute-compound-repeat-order-howitworks-compound-end

.. attribute-compound-repeat-order-view-the-real-sql-start

The SQL for **Repeat Order** is more complex than what is described in the previous section. This is due to the way this attribute returns *only* a list of Amperity IDs, uses a series of common table expressions (CTEs), and takes advantage of workflows that Amperity does behind the scenes to pre-filter the product, purchase, and store attributes.

You can view the full SQL for **Repeat Order** from the **Segment Editor**. Start a new segment and add only this attribute (along with any required conditions and filter attributes), and then click the **View SQL** link at the top of the page.

.. attribute-compound-repeat-order-view-the-real-sql-end


.. _attribute-compound-repeat-order-segments:

Add to segments
==================================================

.. attribute-compound-repeat-order-segments-start

To find all customers who made their first order within a specified date range, start with the **Repeat Order** attribute located under **Purchase behaviors**:

.. attribute-compound-repeat-order-segments-end

.. image:: ../../images/attribute-compound-repeat-order.png
   :width: 600 px
   :alt: Use the repeat order attribute to find repeat orders by date range.
   :align: left
   :class: no-scaled-link

.. attribute-compound-repeat-order-segments-filters-start

After the attribute appears in your segment, choose a date range:

.. image:: ../../images/attribute-compound-repeat-order-example.png
   :width: 600 px
   :alt: Customers who own the base game and need to buy an expansion pack.
   :align: left
   :class: no-scaled-link

After you specify a date range you may apply filters to associate these customers to specific products, brands, channels, and stores.

.. attribute-compound-repeat-order-segments-filters-end


.. _attribute-compound-repeat-order-relative-dates:

About relative dates
--------------------------------------------------

.. include:: ../../amperity_reference/source/segments.rst
   :start-after: .. segments-howitworks-segment-condition-relative-dates-start
   :end-before: .. segments-howitworks-segment-condition-relative-dates-end

**Relative date values**

.. include:: ../../amperity_reference/source/segments.rst
   :start-after: .. segments-howitworks-segment-condition-relative-date-values-start
   :end-before: .. segments-howitworks-segment-condition-relative-date-values-end


.. _attribute-compound-repeat-order-conditions:

Available conditions
==================================================

.. attribute-compound-repeat-order-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **was after**
     - |attribute-recommended| **More useful**

       Returns a list of customers where repeat purchases were after the specified time window.

   * - **was before**
     - |attribute-recommended| **More useful**

       Returns a list of customers where repeat purchases were before the specified time window.

   * - **was between**
     - |attribute-recommended| **More useful**

       Returns a list of customers where repeat purchases were between two specified time windows.

   * - **was not between**
     - |attribute-stop| **Less useful**

       Returns a list of customers where repeat purchases were not between two specified time windows.

   * - **was not on**
     - |attribute-stop| **Less useful**

       Returns a list of customers where repeat purchases were not on the specified date.

   * - **was on**
     - Returns a list of customers where repeat purchases were on the specified date.

.. attribute-compound-repeat-order-conditions-end


.. _attribute-compound-repeat-order-filter-attributes:

Filter attributes
==================================================

.. include:: ../../amperity_reference/source/attribute_compound_first_order.rst
   :start-after: .. attribute-compound-first-order-filter-attributes-start
   :end-before: .. attribute-compound-first-order-filter-attributes-end
