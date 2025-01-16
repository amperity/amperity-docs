.. https://docs.amperity.com/reference/


.. |what-access| replace:: discount amount attributes
.. |what-choose| replace:: **item discount amount**, **order discount amount**, or **unit discount amount**
.. |what-find| replace:: "discount amount"


.. meta::
    :description lang=en:
        The discount amount that is applied to a single item within a transaction.

.. meta::
    :content class=swiftype name=body data-type=text:
        The discount amount that is applied to a single item within a transaction.

.. meta::
    :content class=swiftype name=title data-type=string:
        Discount amounts

==================================================
Discount amounts
==================================================

.. attribute-discount-amounts-start

Discount amounts can be present for items, orders, and units:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-item-discount-amount-start
     :end-before: .. term-item-discount-amount-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-order-discount-amount-start
     :end-before: .. term-order-discount-amount-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-unit-discount-amount-start
     :end-before: .. term-unit-discount-amount-end

.. attribute-discount-amounts-end


.. _attribute-discount-amounts-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-discount-amounts-conditions:

Available operators
==================================================

.. attribute-discount-amounts-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have a Decimal data type. All Decimal data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific discount amount, such as "4.25", "12.00", or "38.50".

       .. tip:: Use the following operators to return a range of discount amounts instead of a specific discount amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of discount amounts that are between the specified discount amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns discount amounts that are greater than the specified discount amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns discount amounts that are greater than or equal to the specified discount amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual discount amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns discount amounts that are less than the specified discount amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns discount amounts that are less than or equal to the specified discount amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "11.99" then any discount amounts less than or equal to "11.98" and any discount amounts greater than or equal to "12.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier discount amounts.

       For example, if most of your discount amounts are between "11.99" and "82.99", use "11.99" and "82.99" to return discount amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual profit amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "4.99", "5.99", and "27.22", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-discount-amounts-conditions-end
