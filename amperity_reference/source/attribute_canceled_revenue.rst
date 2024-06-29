.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The total amount of revenue for all canceled items in the transaction.

.. meta::
    :content class=swiftype name=body data-type=text:
        The total amount of revenue for all canceled items in the transaction.

.. meta::
    :content class=swiftype name=title data-type=string:
        Order canceled revenue

==================================================
Order canceled revenue
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-canceled-revenue-start
   :end-before: .. term-order-canceled-revenue-end


.. _attribute-canceled-revenue-segment:

Use in segments
==================================================

.. attribute-canceled-revenue-start

You can access canceled order revenue directly from the **Segment Editor**. To add this attribute to your segment, click **Add criteria**, select the **Unified Transactions** table, select the **Order canceled Revenue** attribute, and then apply a condition.

.. attribute-canceled-revenue-end


.. _attribute-canceled-revenue-conditions:

Available conditions
==================================================

.. attribute-canceled-revenue-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a Decimal data type. All Decimal data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific amount of canceled order revenue, such as "17.99", "29.99", or "79.99".

       .. tip:: Use the following conditions to return a range of canceled order revenue amounts instead of a specific canceled order revenue amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of canceled order revenue amounts that are between the specified canceled order revenue amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns canceled order revenue amounts that are greater than the specified canceled order revenue amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns canceled order revenue amounts that are greater than or equal to the specified canceled order revenue amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual canceled order revenue amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns canceled order revenue amounts that are less than the specified canceled order revenue amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns canceled order revenue amounts that are less than or equal to the specified canceled order revenue amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "11.99" then any canceled order revenue amounts less than or equal to "11.98" and any canceled order revenue amounts greater than or equal to "12.00" would be canceled.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your canceled order revenue amounts are between "11.99" and "82.99", use "11.99" and "82.99" to return canceled order revenue amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual revenue amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "4.99", "5.99", and "27.22", but also " " (a space) and "0" (zero). If the record has *any* value it will be canceled.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-canceled-revenue-conditions-end
