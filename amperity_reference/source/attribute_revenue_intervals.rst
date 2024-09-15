.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The total amount of revenue for all items in a transaction after discounts are applied, ignoring returns and/or cancellations, at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        The total amount of revenue for all items in a transaction after discounts are applied, ignoring returns and/or cancellations, at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Order revenue intervals

==================================================
Order revenue intervals
==================================================

.. attribute-order-revenue-intervals-start

Order revenue is the total amount of revenue for all items in a transaction after discounts are applied, ignoring returns and/or cancellations. Order revenue is available at the following intervals:

* L30D Order Revenue (30 days)
* L3M Order Revenue (3 months)
* L6M Order Revenue (6 months)
* L12M Order Revenue (12 months)
* LY12M Order Revenue (12-to-24 months)
* Lifetime Order Revenue (Lifetime)

.. attribute-order-revenue-intervals-end


.. _attribute-order-revenue-intervals-examples:

Examples
==================================================

.. attribute-order-revenue-intervals-examples-start

The following topics contain examples of using order revenue intervals:

* |usecase_customers_high_value_multichannel|

.. attribute-order-revenue-intervals-examples-end


.. _attribute-order-revenue-intervals-segment:

Use in segments
==================================================

.. attribute-order-revenue-intervals-segment-start

You can access order revenue intervals directly from the **Segment Editor**. To add these attributes to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select an order revenue interval, and then apply a condition.

.. attribute-order-revenue-intervals-segment-end


.. _attribute-order-revenue-interval-conditions:

Available conditions
==================================================

.. attribute-order-revenue-interval-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have a Decimal data type. All Decimal data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific amount of revenue, such as "17.99", "29.99", or "79.99".

       .. tip:: Use the following conditions to return a range of revenue amounts instead of a specific revenue amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of revenue amounts that are between the specified revenue amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns revenue amounts that are greater than the specified revenue amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns revenue amounts that are greater than or equal to the specified revenue amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual revenue amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns revenue amounts that are less than the specified revenue amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns revenue amounts that are less than or equal to the specified revenue amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "11.99" then any revenue amounts less than or equal to "11.98" and any revenue amounts greater than or equal to "12.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your revenue amounts are between "11.99" and "82.99", use "11.99" and "82.99" to return revenue amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual revenue amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "14.99", "59.99", and "127.22", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-order-revenue-interval-conditions-end
