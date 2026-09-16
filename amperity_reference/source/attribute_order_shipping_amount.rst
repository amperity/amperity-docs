.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **order shipping amount** attribute
.. |what-choose| replace:: **order shipping amount**
.. |what-find| replace:: "order shipping"


.. meta::
    :description lang=en:
        The amount of shipping for each order.

.. meta::
    :content class=swiftype name=body data-type=text:
        The amount of shipping for each order.

.. meta::
    :content class=swiftype name=title data-type=string:
        Shipping amounts

==================================================
Shipping amounts
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-shipping-amount-start
   :end-before: .. term-order-shipping-amount-end


.. _attribute-shipping-amount-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-shipping-amount-conditions:

Available operators
==================================================

.. attribute-shipping-amount-conditions-start

The following table lists the operators that are available to order shipping amounts.

.. note:: Order shipping amounts have a **decimal** data type. All **decimal** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific order shipping amount, such as "117.99", "129.99", or "179.99".

       .. tip:: Use the following operators to return a range of order shipping amounts instead of a specific shipping amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of order shipping amounts that are between the specified order shipping amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns order shipping amounts that are greater than the specified order shipping amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns order shipping amounts that are greater than or equal to the specified order shipping amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition. Individual order shipping amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns order shipping amounts that are less than the specified order shipping amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns order shipping amounts that are less than or equal to the specified order shipping amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "111.99" then any order shipping amounts less than or equal to "111.98" and any order shipping amounts greater than or equal to "112.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your order shipping amounts are between "111.99" and "182.99", use "111.99" and "182.99" to return order shipping amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual revenue amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "14.99", "59.99", and "127.22", but also " " (a space) and "0" (zero). If the record has *any* value it is returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-shipping-amount-conditions-end
