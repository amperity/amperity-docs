.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The average number of items purchased at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        The average number of items purchased at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Average number of items

==================================================
Average number of items
==================================================

.. attribute-average-items-start

Average number of items attributes identify the average order sizes (or "number of items purchased") during the specified time period. Average number of items attributes are available at the following intervals:

* L30D Average Num Items (30 days)
* L3M Average Num Items (3 months)
* L6M Average Num Items (6 months)
* L12M Average Num Items (12 months)
* LY12M Average Num Items (12-to-24 months)
* Lifetime Average Num Items (Lifetime)

.. attribute-average-items-end


.. _attribute-average-items-segment:

Use in segments
==================================================

.. attribute-average-items-segments-start

You can access averages for the number of items purchased directly from the **Segment Editor**. To add these attributes to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select an average number of items interval attribute, and then apply a condition.

.. attribute-average-items-segments-end


.. _attribute-average-items-conditions:

Available conditions
==================================================

.. attribute-average-items-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have a Decimal data type. All Decimal data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - Returns a specific average number of items, such as "4.20", "7", or "5.10".

       .. tip:: Use the following conditions to return a range of averages instead of a specific average: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of items that is between the specified averages.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns average number of items that are greater than the specified average number of items.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns average number of items that are greater than or equal to the specified average number of items.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual average number of items are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns average number of items that are less than the specified average number of items.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns average number of items that are less than or equal to the specified average number of items.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "4.50" then any average number of items less than or equal to "4.49" and any average number of items greater than or equal to "4.51" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier discount amounts.

       For example, if most of your average number of items are between "2.10" and "3.20", use "2.10" and "3.20" to return averages that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual profit amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "4.10", "10", and ".90", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-average-items-conditions-end
