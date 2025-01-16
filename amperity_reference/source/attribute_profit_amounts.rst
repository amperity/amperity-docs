.. https://docs.amperity.com/reference/


.. |what-access| replace:: profit amount attributes
.. |what-choose| replace:: **item profit**, **order profit**, or **unit profit**
.. |what-find| replace:: "profit"


.. meta::
    :description lang=en:
        The amount earned when an item or unit of an item are sold or when an order is completed.

.. meta::
    :content class=swiftype name=body data-type=text:
        The amount earned when an item or unit of an item are sold or when an order is completed.

.. meta::
    :content class=swiftype name=title data-type=string:
        Profit amounts

==================================================
Profit amounts
==================================================

.. attribute-profits-start

Profit represents the amount earned when an item or unit of an item are sold or when an order is completed:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-item-profit-start
     :end-before: .. term-item-profit-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-order-profit-start
     :end-before: .. term-order-profit-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-unit-profit-start
     :end-before: .. term-unit-profit-end

.. attribute-profits-end


.. _attribute-profits-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-profits-conditions:

Available operators
==================================================

.. attribute-profits-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have a Decimal data type. All Decimal data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific profit amount, such as "4.25", "12.00", or "38.50".

       .. tip:: Use the following operators to return a range of profit amounts instead of a specific amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of profit amounts that are between the specified profit amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns profit amounts that are greater than the specified profit amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns profit amounts that are greater than or equal to the specified profit amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual profit amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns profit amounts that are less than the specified profit amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns profit amounts that are less than or equal to the specified profit amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "11.99" then any profit amounts less than or equal to "11.98" and any profit amounts greater than or equal to "12.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier profit amounts.

       For example, if most of your profit amounts are between "11.99" and "82.99", use "11.99" and "82.99" to return profit amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual profit amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "4.99", "5.99", and "27.22", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-profits-conditions-end
