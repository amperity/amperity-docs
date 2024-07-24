.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Which customers have not purchased items during the specified time period?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which customers have not purchased items during the specified time period?

.. meta::
    :content class=swiftype name=title data-type=string:
        Has not purchased

==================================================
Has not purchased
==================================================

.. attribute-compound-has-not-purchased-start

**Has Not Purchased** returns all orders that occurred during your chosen date range, and then identifies all of your customers that did not make a purchase within that date range. For example, return all customers who have not purchased within the previous 3 months:

.. image:: ../../images/attribute-compound-has-not-purchased-example.png
   :width: 600 px
   :alt: Find which customers have not interacted with products, channels, or brands during the specified date range.
   :align: left
   :class: no-scaled-link

After you specify a date range you may apply filters to focus in on specific products, brands, channels, and stores, i.e. "who hasn't purchased a specific product by a specific brand from a specific channel or store." For example, return a list of customers who have not purchased a wool product online during the previous 3 months.

.. attribute-compound-has-not-purchased-end

.. attribute-compound-has-not-purchased-tip-start

.. tip:: As you add filters to this attribute, the number of customer records that is returned gets larger.

   Consider all of your brands and all of the products in your product catalog and all of your stores and your website. Consider the percentage of all of your customers who may have purchased within any time window. And then consider the number of customers you have in your Customer 360.

   For example, let's say you have 1,000,000 customers in your Customer 360. If you configure **Has Not Purchased** to return only customers who purchased last month, that might be 8,000 customers.

   **Has Not Purchased** compares the list of customers who did purchase to your total list of customers, and then returns the difference. In this example that difference is 992,000 customers.

.. attribute-compound-has-not-purchased-tip-end


.. _attribute-compound-has-not-purchased-howitworks:

How this attribute works
==================================================

.. attribute-compound-has-not-purchased-howitworks-start

**Has Not Purchased** represents a common approach people use when they build segments: which of my customers have not purchased, and then associate that list of customers to your products and brands.

**Has Not Purchased** is a *compound attribute*, which means that it's built from a combination of attributes that already exist in your data, and then appears as a single attribute that you can choose from the **Segment Editor**.

With this attribute, you can focus less on SQL and more on finding answers that align to your marketing goals and strategies. Purchase behavior attributes simplify the number of steps that are required to associate a list of customers to your products, stores, channels, and brands.

.. attribute-compound-has-not-purchased-howitworks-end


.. _attribute-compound-has-not-purchased-howitworks-sql:

As SQL
--------------------------------------------------

.. attribute-compound-has-not-purchased-howitworks-compound-start

**Has Not Purchased** is built from standard columns that are output by Amperity. It uses two steps:

#. Return purchase counts along with the list of distinct Amperity IDs that made those purchases.
#. Compares list of distinct Amperity IDs to all Amperity IDs that exist in the **Merged Customers** table.

The following example returns all customers who have not purchased:

.. image:: ../../images/attribute-compound-has-not-purchased-example.png
   :width: 500 px
   :alt: Find which customers have not interacted with products, channels, or brands during the specified date range.
   :align: left
   :class: no-scaled-link

This can be a large list!

The SQL for **Has Not Purchased** works like this. It uses order ID from the **Unified Itemized Transactions** table as its starting point:

::

   SELECT
     amperity_id
     ,COUNT(DISTINCT order_id) AS purchase_count
   FROM Unified_Itemized_Transactions

and finds all of the distinct orders that were made by all customers -- the "purchase count" -- and groups them by Amperity ID for all orders that match the date range:

::

   WHERE order_datetime < DATE_TRUNC('day', CURRENT_TIMESTAMP - interval '3' month)
   GROUP BY amperity_id

Returns and cancellations are filtered out automatically, like this:

::

   AND (is_return IS NULL OR (NOT is_return))
   AND (is_cancellation IS NULL OR (NOT is_cancellation))

You may then filter this list of customers more by applying any of the product, purchase, and store filters. When you select these filters, they are added to the WHERE statement, like this:

::

   AND product_category = 'wool'
   AND purchase_channel = 'online'

This will return a list of customers from the **Unified Itemized Transactions** table who purchased wool socks in all styles from your website.

This list of customers from the **Unified Itemized Transactions** table is then compared to the list of customers in your **Merged Customers** table. What is the **Merged Customers** table? It is the table in which *all* of your customers are located and is the foundation of your customer 360 database.

After comparing both lists, all of the customers in the **Merged Customers** table that were not in the results from the **Unified Itemized Transactions** table are returned as a list of Amperity IDs. These are the customers who have not purchased.

.. attribute-compound-has-not-purchased-howitworks-compound-end

.. attribute-compound-has-not-purchased-view-the-real-sql-start

.. note:: The SQL for **Has Not Purchased** is more complex than what is described in the previous section. This is due to the way this attribute returns *only* a list of Amperity IDs, uses a series of common table expressions (CTEs), and takes advantage of workflows that Amperity does behind the scenes to pre-filter the product, purchase, and store attributes.

   You can view the full SQL for **Has Not Purchased** from the **Segment Editor**. Start a new segment and add only this attribute (along with any required conditions and filter attributes), and then click the **View SQL** link at the top of the page.

.. attribute-compound-has-not-purchased-view-the-real-sql-end


.. _attribute-compound-has-not-purchased-howitworks-bubbles:

As a diagram
--------------------------------------------------

.. attribute-compound-has-not-purchased-howitworks-bubbles-start

The following diagram shows how **Has Not Purchased** works:

.. image:: ../../images/attribute-compound-has-not-purchased-bubbles.png
   :width: 500 px
   :alt: Compare who purchased to who did not, return all who did not.
   :align: left
   :class: no-scaled-link

The numbers in this diagram represent:

#. The **Unified Itemized Transactions** table, or the table that associates all of the items you sold with the order ID of the transaction and the customers who purchased them.
#. The **Merged Customers** table, or the table in which *all* of your customers are located and the foundation of your customer 360 database.
#. A purchase channel.
#. A product category.
#. A product gender.
#. All of the customers who purchased, inclusive of purchase channel (3), product category (4), and product gender (5).
#. All of the customers who did not purchase, and also the list of customers that is returned by **Has Not Purchased** during the date range that you choose.

.. attribute-compound-has-not-purchased-howitworks-bubbles-end


.. _attribute-compound-has-not-purchased-howitworks-larger:

Why does the audience get larger?
--------------------------------------------------

.. attribute-compound-has-not-purchased-howitworks-larger-start

As you add filters to **Has Not Purchased** the size of the audience that is returned from the **Merged Customers** table gets larger. The best way to explain this is to use a series of diagrams.

This series of diagrams steps through and shows you why your audience gets larger as you apply more filters. On the left side is the **Unified Itemized Transactions** table and on the right side is the **Merged Customers** table.

#. The following diagram shows just one filter (the white inner circle). Let's say that filter is purchase channel and that you chose "online":

   .. image:: ../../images/attribute-compound-has-not-purchased-larger-1.png
      :width: 500 px
      :alt: One filter attribute.
      :align: left
      :class: no-scaled-link

   The results of **Has Not Purchased** will return "all of your customers who did not purchase from your website."

#. The following diagram shows a *second* filter. Let's say this one adds product category and that you chose "shirts":

   .. image:: ../../images/attribute-compound-has-not-purchased-larger-2.png
      :width: 500 px
      :alt: Two filter attributes.
      :align: left
      :class: no-scaled-link

   The results from the **Unified Itemized Transactions** table is smaller because only purchases that exist in both filters are returned. This means the results for **Has Not Purchased** will be larger, and now return "all of your customers who did not purchase a shirt from your website."

#. The following diagram shows a *third* filter. Let's say this one adds product gender and that you chose "F":

   .. image:: ../../images/attribute-compound-has-not-purchased-larger-3.png
      :width: 500 px
      :alt: Three filter attributes.
      :align: left
      :class: no-scaled-link

   The results from the **Unified Itemized Transactions** table is now much smaller and the results for **Has Not Purchased** have grown larger, and now return "all of your customers who did not purchase a women's shirt from your website."

.. attribute-compound-has-not-purchased-howitworks-larger-end


.. _attribute-compound-has-not-purchased-segments:

Add to segments
==================================================

.. attribute-compound-has-not-purchased-segments-start

To find all customers who made their first order within a specified date range, start with the **Has Not Purchased** attribute located under **Purchase behaviors**:

.. attribute-compound-has-not-purchased-segments-end

.. image:: ../../images/attribute-compound-has-not-purchased.png
   :width: 600 px
   :alt: Use the has not purchased attribute to find which customers have not interacted with products, channels, or brands during the specified date range.
   :align: left
   :class: no-scaled-link

.. attribute-compound-has-not-purchased-segments-filters-start

After the attribute appears in your segment, choose a date range:

.. image:: ../../images/attribute-compound-has-not-purchased-example.png
   :width: 600 px
   :alt: Find which customers have not interacted with products, channels, or brands during the specified date range.
   :align: left
   :class: no-scaled-link

After you specify a value and date range you may apply filters to associate these customers to specific products, brands, channels, and stores.

.. attribute-compound-has-not-purchased-segments-filters-end


.. _attribute-compound-has-not-purchased-relative-dates:

About relative dates
--------------------------------------------------

.. include:: ../../amperity_reference/source/segments.rst
   :start-after: .. segments-howitworks-segment-condition-relative-dates-start
   :end-before: .. segments-howitworks-segment-condition-relative-dates-end

**Relative date values**

.. include:: ../../amperity_reference/source/segments.rst
   :start-after: .. segments-howitworks-segment-condition-relative-date-values-start
   :end-before: .. segments-howitworks-segment-condition-relative-date-values-end


.. _attribute-compound-has-not-purchased-conditions:

Available conditions
==================================================

.. attribute-compound-has-not-purchased-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **after**
     - |attribute-recommended| **More useful**

       Returns a list of customers who have not purchased after the specified time window.

   * - **before**
     - |attribute-recommended| **More useful**

       Returns a list of customers who have not purchased before the specified time window.

   * - **between**
     - |attribute-recommended| **More useful**

       Returns a list of customers who have not purchased between two specified time windows.

   * - **not between**
     - Returns a list of customers who have not made a purchase outside the dates that define the specified time window.

       For example, if you want to find customers who only purchased school supplies in the two weeks prior to the start of school, and if school started on 9/7, you could define the start of the time window as 8/24 and the end of the time window as 9/6, the **not between** condition will ensure that only customers who purchased within that time window will be returned.

   * - **not on**
     - |attribute-stop| **Less useful**

       Returns a list of customers who made a purchase on the specified date.

   * - **on**
     - Returns a list of customers who have not purchased on the specified date.

.. attribute-compound-has-not-purchased-conditions-end


.. _attribute-compound-has-not-purchased-filter-attributes:

Filter attributes
==================================================

.. include:: ../../amperity_reference/source/attribute_compound_first_order.rst
   :start-after: .. attribute-compound-first-order-filter-attributes-start
   :end-before: .. attribute-compound-first-order-filter-attributes-end
