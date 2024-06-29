.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Which customers have purchased N (or more) items during the specified time period?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which customers have purchased N (or more) items during the specified time period?

.. meta::
    :content class=swiftype name=title data-type=string:
        Has purchased

==================================================
Has purchased
==================================================

.. attribute-compound-has-purchased-start

**Has Purchased** returns a list of orders that meets the threshold that you define -- for example, exactly 4, less than 5, more than 2, or between 2 and 10 -- *and* occurred during your chosen date range. For example, return all customers who have purchased 3 (or more) times in the previous 2 years:

.. image:: ../../images/attribute-compound-has-purchased-example.png
   :width: 600 px
   :alt: Find which customers have interacted with products, channels, or brands during the specified date range.
   :align: left
   :class: no-scaled-link

After you specify a value and date range you may apply filters to associate customers who have purchased with specific products, brands, channels, and stores. For example, return all customers who have purchased wool or cotton socks from your website.

.. attribute-compound-has-purchased-end


.. _attribute-compound-has-purchased-howitworks:

How this attribute works
==================================================

.. attribute-compound-has-purchased-howitworks-start

**Has Purchased** represents a common approach people use when they build segments: start with all orders, and then associate that list of orders to the products and brands your customers purchased.

**Has Purchased** is a *compound attribute*, which means that it's built from a combination of attributes that already exist in your data, and then appears as a single attribute that you can choose from the **Segment Editor**.

With this attribute, you can focus less on SQL and more on finding answers that align to your marketing goals and strategies. Purchase behavior attributes simplify the number of steps that are required to associate a list of customers to your products, stores, channels, and brands.

.. attribute-compound-has-purchased-howitworks-end

.. attribute-compound-has-purchased-howitworks-compound-start

.. admonition:: How does the SQL for Has Purchased work?

   **Has Purchased** is built from standard columns that are output by Amperity. The following example returns a list of customers who have purchased 3 (or more) times in the previous 2 years:

   .. image:: ../../images/attribute-compound-has-purchased-example.png
      :width: 500 px
      :alt: Find which customers have interacted with products, channels, or brands during the specified date range.
      :align: left
      :class: no-scaled-link

   The SQL for **Has Purchased** works like this. It uses order ID from the **Unified Itemized Transactions** table as its starting point:

   ::

      SELECT
        amperity_id
        ,COUNT(DISTINCT order_id) AS purchase_count
      FROM Unified_Itemized_Transactions

   and finds all of the distinct orders that were made by all customers -- the "purchase count" -- and then returns all orders that match the date range:

   ::

      WHERE order_datetime < DATE_TRUNC('day', CURRENT_TIMESTAMP - interval '2' year)

   Returns and cancellations are filtered out automatically, like this:

   ::

      AND (is_return IS NULL OR (NOT is_return))
      AND (is_cancellation IS NULL OR (NOT is_cancellation))

   From that list of customers who made a purchase within that date range, **Has Purchased** uses another SELECT statement to return only customers whose purchase count meets the threshold that you defined. For example, more than 2 purchases:

   ::

      SELECT
        *
      FROM total_distinct_orders
      WHERE purchase_count > 2

   This creates a list of customers who made *at least 3 purchases* during a specific time window. From here you can apply additional filters for your products, stores, channels, and brands.

.. attribute-compound-has-purchased-howitworks-compound-end

.. attribute-compound-has-purchased-view-the-real-sql-start

The SQL for **Has Purchased** is more complex than what is described in the previous section. This is due to the way this attribute returns *only* a list of Amperity IDs, uses a series of common table expressions (CTEs), and takes advantage of workflows that Amperity does behind the scenes to pre-filter the product, purchase, and store attributes.

You can view the full SQL for **Has Purchased** from the **Segment Editor**. Start a new segment and add only this attribute (along with any required conditions and filter attributes), and then click the **View SQL** link at the top of the page.

.. attribute-compound-has-purchased-view-the-real-sql-end


.. _attribute-compound-has-purchased-segments:

Add to segments
==================================================

.. attribute-compound-has-purchased-segments-start

To find all customers who made their first order within a specified date range, start with the **Has Purchased** attribute located under **Transactional Behaviors**:

.. attribute-compound-has-purchased-segments-end

.. image:: ../../images/attribute-compound-has-purchased.png
   :width: 600 px
   :alt: Use the has purchased attribute to find which customers have interacted with products, channels, or brands during the specified date range.
   :align: left
   :class: no-scaled-link

.. attribute-compound-has-purchased-segments-filters-start

After the attribute appears in your segment, set the purchase count and choose a date range:

.. image:: ../../images/attribute-compound-has-purchased-example.png
   :width: 600 px
   :alt: Find which customers have interacted with products, channels, or brands during the specified date range.
   :align: left
   :class: no-scaled-link

After you specify a purchase count and date range you may apply filters to associate these customers to specific products, brands, channels, and stores.

.. attribute-compound-has-purchased-segments-filters-end


.. _attribute-compound-has-purchased-relative-dates:

About relative dates
--------------------------------------------------

.. include:: ../../amperity_reference/source/segments.rst
   :start-after: .. segments-howitworks-segment-condition-relative-dates-start
   :end-before: .. segments-howitworks-segment-condition-relative-dates-end

**Relative date values**

.. include:: ../../amperity_reference/source/segments.rst
   :start-after: .. segments-howitworks-segment-condition-relative-date-values-start
   :end-before: .. segments-howitworks-segment-condition-relative-date-values-end


.. _attribute-compound-has-purchased-conditions:

Available conditions
==================================================

.. attribute-compound-has-purchased-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **between**
     - Returns a list of customers whose order threshold is in-between two specified values.

   * - **exactly**
     - Returns a list of customers whose order threshold exactly matches specified value.

   * - **less than**
     - Returns a list of customers whose order threshold is less than the specified value.

   * - **more than**
     - Returns a list of customers whose order threshold is more than the specified value.

.. attribute-compound-has-purchased-conditions-end


.. _attribute-compound-has-purchased-filter-attributes:

Filter attributes
==================================================

.. attribute-compound-has-purchased-filter-attributes-start

.. include:: ../../amperity_reference/source/attribute_compound_first_order.rst
   :start-after: .. attribute-compound-first-order-filter-attributes-start
   :end-before: .. attribute-compound-first-order-filter-attributes-end

.. attribute-compound-has-purchased-filter-attributes-end
