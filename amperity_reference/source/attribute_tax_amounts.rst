.. https://docs.amperity.com/reference/


.. |what-access| replace:: tax amount attributes
.. |what-choose| replace:: **item tax amount**, **order tax amount**, or **unit tax amount**
.. |what-find| replace:: "tax amount"


.. meta::
    :description lang=en:
        The total amount of taxes associated with the purchase of an item, an order, or a unit

.. meta::
    :content class=swiftype name=body data-type=text:
        The total amount of taxes associated with the purchase of an item, an order, or a unit

.. meta::
    :content class=swiftype name=title data-type=string:
        Tax amounts

==================================================
Tax amounts
==================================================

.. attribute-tax-amounts-common-start

A tax amount is the total amount of taxes that are associated with the purchase of an item, an order, or a unit.

.. attribute-tax-amounts-common-end


.. _attribute-tax-amounts-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-tax-amounts-conditions:

Available operators
==================================================

.. attribute-tax-amounts-conditions-start

The following table lists the operators that are available to tax amount attributes.

.. note:: Tax amount attributes have a Decimal data type. All Decimal data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific tax amount, such as "3.33", "4.33", or "5.33".

       .. tip:: Use the following operators to return a range of tax amounts instead of a specific tax amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of tax amounts that are between the specified tax amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns tax amounts that are greater than the specified tax amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns tax amounts that are greater than or equal to the specified tax amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual tax amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns tax amounts that are less than the specified tax amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns tax amounts that are less than or equal to the specified tax amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "3.33" then any tax amount less than or equal to "3.32" and any tax amount greater than or equal to "3.34" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier tax amounts.

       For example, if most of your tax amounts are between "3.33" and "5.33", use "3.33" and "5.33" to return tax amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when tax amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "3.33", "4.33", and "5.33", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-tax-amounts-conditions-end
