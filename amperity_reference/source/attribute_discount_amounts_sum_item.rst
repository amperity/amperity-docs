.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The total of all discount amounts that were applied to each item within a transaction.

.. meta::
    :content class=swiftype name=body data-type=text:
        The total of all discount amounts that were applied to each item within a transaction.

.. meta::
    :content class=swiftype name=title data-type=string:
        Sum of item discounts

==================================================
Sum of item discounts
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sum-of-discount-amounts-start
   :end-before: .. term-sum-of-discount-amounts-end


.. _attribute-sum-of-item-discount-segment:

Use in segments
==================================================

.. attribute-discount-amounts-sum-of-items-start

You can access the sum-of-item discount attribute directly from the **Segment Editor**. To add these attributes to your segment, click **Add criteria**, select the **Unified Itemized Transactions** table, select the **Sum of Item Discount Amount** attribute, and then apply a condition.

.. attribute-discount-amounts-sum-of-items-end


.. _attribute-discount-amounts-sum-of-items-conditions:

Available conditions
==================================================

.. attribute-discount-amounts-sum-of-items-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have a Decimal data type. All Decimal data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific total for all item discount amounts, such as "42.34", "18.00", or "8.50".

       .. tip:: Use the following conditions to return a range of totals for all item discount amounts instead of a specific discount amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of totals for all item discount amounts that are between the specified totals for all item discount amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns totals for all item discount amounts that are greater than the specified discount amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns totals for all item discount amounts that are greater than or equal to the specified discount amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual totals for all item discount amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns totals for all item discount amounts that are less than the specified discount amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns totals for all item discount amounts that are less than or equal to the specified discount amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "11.99" then any totals for all item discount amounts less than or equal to "11.98" and any totals for all item discount amounts greater than or equal to "12.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier discount amounts.

       For example, if most of your totals for all item discount amounts are between "11.99" and "82.99", use "11.99" and "82.99" to return discount amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual discount amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "4.99", "5.99", and "27.22", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-discount-amounts-sum-of-items-conditions-end
