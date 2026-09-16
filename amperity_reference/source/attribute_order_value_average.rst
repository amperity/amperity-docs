.. https://docs.amperity.com/reference/


.. |what-access| replace:: average order value interval attributes
.. |what-choose| replace:: an interval
.. |what-find| replace:: "average order"


.. meta::
    :description lang=en:
        The average order value for customer transactions at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        The average order value for customer transactions at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Average order value intervals

==================================================
Average order value intervals
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-average-order-value-start
   :end-before: .. term-average-order-value-end

.. attribute-order-value-average-intervals-start

Average order values are calculated for the following intervals:

* L30D Average Order Value (30 days)
* L3M Average Order Value (3 months)
* L6M Average Order Value (6 months)
* L12M Average Order Value (12 months)
* LY12M Average Order Value (12-to-24 months)
* Lifetime Average Order Value (Lifetime)

.. attribute-order-value-average-intervals-end


.. _attribute-order-value-average-intervals-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-order-value-average-conditions:

Available operators
==================================================

.. attribute-order-value-average-conditions-start

The following table lists the operators that are available to average order value interval attributes.

.. note:: Average order value interval attributes have a **decimal** data type. All **decimal** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific average order value amounts, such as "167.99", "123.99", or "79.99".

       .. tip:: Use the following operators to return a range of average order value amounts instead of a specific average order value amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of average order value amounts that are between the specified average order value amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns average order value amounts that are greater than the specified average order value amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns average order value amounts that are greater than or equal to the specified average order value amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition. Individual average order value amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns average order value amounts that are less than the specified average order value amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns average order value amounts that are less than or equal to the specified average order value amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "150.00" then any average order value amounts less than or equal to "149.99" and any average order value amounts greater than or equal to "150.01" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your average order value amounts are between "100.00" and "140.00", use "100.00" and "150.00" to return average order value amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual subtotal amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "14.99", "59.99", and "127.22", but also " " (a space) and "0" (zero). If the record has *any* value it is returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-order-value-average-conditions-end
