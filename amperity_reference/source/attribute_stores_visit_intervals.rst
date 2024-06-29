.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Store visits at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        Store visits at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Store visit intervals

==================================================
Store visit intervals
==================================================

.. attribute-stores-visits-start

Use store visit attributes to build segments that support many types of campaigns. Store visit attributes are available in 30-day, 3-month, 6-month, 12-month, 1-year, and lifetime intervals.

You can access store visit interval attributes directly from the **Segment Editor**:

* L30D Stores (30 days)
* L3M Stores (3 months)
* L6M Stores (6 months)
* L12M Stores (12 months)
* LY12M Stores (12-to-24 months)
* Lifetime Stores (Lifetime)

.. attribute-stores-visits-end


.. _attribute-stores-visits-segment:

Use in segments
==================================================

.. attribute-stores-visits-segment-start

You can access 30 day visit intervals directly from the **Segment Editor**. To add these attributes to your segment, click **Add criteria**, select the **Transaction Attributes Extended** table, select a store visit interval attribute, and then apply a condition.

.. attribute-stores-visits-segment-end


.. _attribute-stores-visits-conditions:

Available conditions
==================================================

.. attribute-stores-visits-conditions-start

The following table lists the conditions that are available to store visit interval attributes.

.. note:: Store visit interval attributes have an Integer data type. All Integer data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

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
     - Returns customer records with values that are greater than or equal to the specified number of items in the interval, including the specified number of items.

       For example: if **is greater than or equal to** is set to 10, then customer records with 10 (or more) total items will be returned.

   * - **is in list**
     - Returns customer records with values that match the number of items in the interval that are specified in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are less than the specified number of items in the interval, not including the specified number of items.

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

.. attribute-stores-visits-conditions-end
