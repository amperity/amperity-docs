.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The average for list item prices at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        The average for list item prices at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Average item prices

==================================================
Average item prices
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-list-price-start
   :end-before: .. term-list-price-end

.. attribute-price-average-item-intervals-start

Average item prices are available at the following intervals:

* L30D Average Item Price (30 days)
* L3M Average Item Price (3 months)
* L6M Average Item Price (6 months)
* L12M Average Item Price (12 months)
* LY12M Average Item Price (12-to-24 months)
* Lifetime Average Item Price (Lifetime)

.. attribute-price-average-item-intervals-end


.. _attribute-price-average-item-intervals-segment:

Use in segments
==================================================

.. attribute-price-average-item-intervals-segments-start

You can access average item price intervals directly from the **Segment Editor**. To add these attributes to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select an average item price interval attribute, and then apply a condition.

.. attribute-price-average-item-intervals-segments-end


.. _attribute-price-average-item-intervals-conditions:

Available conditions
==================================================

.. attribute-price-average-item-intervals-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have a Decimal data type. All Decimal data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific average item price, such as "9.99", "49.99", or "52.74".

       .. tip:: Use the following conditions to return a range of average item prices instead of a specific average item price: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of average item prices that are between the specified average item prices.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns average item prices that are greater than the specified average item price.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns average item prices that are greater than or equal to the specified average item price.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual average item price amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns average item prices that are less than the specified average item price.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns average item prices that are less than or equal to the specified average item price.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "10.25" then any average item price less than or equal to "10.24" and any average item price greater than or equal to "10.26" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier prices.

       For example, if most of your average item prices are between "19.99" and "99.99", use "19.99" and "99.99" to return average item prices that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual price amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "4.99", "1.25", and "99.99", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-price-average-item-intervals-conditions-end
