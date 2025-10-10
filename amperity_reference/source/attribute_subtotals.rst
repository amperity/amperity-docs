.. https://docs.amperity.com/reference/


.. |what-access| replace:: subtotal attributes
.. |what-choose| replace:: **item subtotal**, **order subtotal**, or **unit subtotal**
.. |what-find| replace:: "subtotal"


.. meta::
    :description lang=en:
        Amounts before discounts are applied.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amounts before discounts are applied.

.. meta::
    :content class=swiftype name=title data-type=string:
        Subtotals

==================================================
Subtotals
==================================================

.. attribute-subtotals-start

Subtotals represents amounts before discounts are applied.

* .. include:: ../../shared/terms.rst
     :start-after: .. term-item-subtotal-start
     :end-before: .. term-item-subtotal-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-order-subtotal-start
     :end-before: .. term-order-subtotal-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-unit-subtotal-start
     :end-before: .. term-unit-subtotal-end

.. attribute-subtotals-end


.. _attribute-subtotals-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-subtotals-conditions:

Available operators
==================================================

.. attribute-subtotals-conditions-start

The following table lists the operators that are available to subtotal attributes.

.. note:: Subtotal attributes have a Decimal data type. All Decimal data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific subtotal amount, such as "17.99", "29.99", or "79.99".

       .. tip:: Use the following operators to return a range of subtotal amounts instead of a specific subtotal amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of subtotal amounts that are between the specified subtotal amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns subtotal amounts that are greater than the specified subtotal amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns subtotal amounts that are greater than or equal to the specified subtotal amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition. Individual subtotal amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns subtotals amounts that are less than the specified subtotal amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns subtotal amounts that are less than or equal to the specified subtotal amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "11.99" then any subtotal amounts less than or equal to "11.98" and any subtotal amounts greater than or equal to "12.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your subtotals amounts are between "11.99" and "82.99", use "11.99" and "82.99" to return subtotals amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual subtotal amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "14.99", "59.99", and "127.22", but also " " (a space) and "0" (zero). If the record has *any* value it is returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-subtotals-conditions-end
