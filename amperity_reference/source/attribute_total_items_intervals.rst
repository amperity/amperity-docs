.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The number of items that were purchased at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        The number of items that were purchased at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Total items intervals

==================================================
Total items intervals
==================================================

.. attribute-total-items-intervals-start

Total items interval attributes help you build audiences of customers that have purchased a certain number of items within a specific time period.

.. attribute-total-items-intervals-end

.. attribute-total-items-intervals-list-start

Total items are available at the following intervals:

* L30D Total Items (30 days)
* L3M Total Items (3 months)
* L6M Total Items (6 months)
* L12M Total Items (12 months)
* LY12M Total Items (12-to-24 months)
* Lifetime Total Items (Lifetime)

.. attribute-total-items-intervals-list-end


.. _attribute-total-items-intervals-segment:

Use in segments
==================================================

.. attribute-total-items-intervals-segment-start

You can access total items intervals directly from the **Segment Editor**. To add these attributes to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select a total items interval attribute, apply a condition, and then specify a value.

.. attribute-total-items-intervals-segment-end


.. _attribute-total-items-intervals-conditions:

Available conditions
==================================================

.. attribute-total-items-intervals-conditions-start

The following table lists the conditions that are available to total item interval attributes.

.. note:: Total item interval attributes have an Integer data type. All Integer data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - Returns customer records with values that match the specified number of items in the interval.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are between the specified number of items in the interval.

       For example: if **is between** is set to 10 and 20, then customer records with at least 11 (but not more than 19) total items will be returned.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are greater than the specified number of items in the interval, not including the specified number of items.

       For example: if **is greater than** is set to 10, then customer records with 11 (or more) total items will be returned.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are greater than or equal to the specified number of items in the interval, including the specified number of items.

       For example: if **is greater than or equal to** is set to 10, then customer records with 10 (or more) total items will be returned.

   * - **is in list**
     - Returns customer records with values that match the number of items in the interval that are specified in a list.

   * - **is less than**
     - Returns customer records with values that are less than the specified number of items in the interval, not including the specified number of items.

       For example: if **is less than** is set to 20, then customer records with 19 (or fewer) total items will be returned.

   * - **is less than or equal to**
     - Returns customer records with values that are less than or equal to the specified number of items in the interval, including the specified number of items.

       For example: if **is less than or equal to** is set to 20, then customer records with 20 (or fewer) total items will be returned.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the specified number of items in the interval.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with values that are not between the specified number of items in the interval, not including the specified number of items.

       For example: if **is not between** is set to 12 and 24, then customer records with at least 25 (but not more than 11) total items will be returned.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the number of items in the interval that are specified in the list.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-total-items-intervals-conditions-end
