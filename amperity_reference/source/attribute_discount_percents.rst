.. https://docs.amperity.com/reference/


.. |what-access| replace:: discount percent attributes
.. |what-choose| replace:: **item discount percent**, **order discount percent**, or **unit discount percent**
.. |what-find| replace:: "discount percent"


.. meta::
    :description lang=en:
        The percentage discount that is applied to a single item in a transaction.

.. meta::
    :content class=swiftype name=body data-type=text:
        The percentage discount that is applied to a single item in a transaction.

.. meta::
    :content class=swiftype name=title data-type=string:
        Discount percent

==================================================
Discount percent
==================================================

.. attribute-discount-percent-start

Discount percents are available for items and orders:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-item-discount-percent-start
     :end-before: .. term-item-discount-percent-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-order-discount-percent-start
     :end-before: .. term-order-discount-percent-end

.. attribute-discount-percent-end


.. _attribute-discount-percent-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-discount-percents-conditions:

Available operators
==================================================

.. attribute-discount-percents-conditions-start

The following table lists the operators that are available to discount percent attributes.

.. note:: Discount percent attributes have a **decimal** data type. All **decimal** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Returns a specific discount percent, such as ".20", ".50", or ".10".

       .. tip:: Use the following operators to return a range of discount percents instead of a specific discount amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of discount percents that are between the specified discount percents.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns discount percents that are greater than the specified discount percent.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns discount percents that are greater than or equal to the specified discount percent.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition. Individual discount percents are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns discount percents that are less than the specified discount percent.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns discount percents that are less than or equal to the specified discount percent.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified ".50" then any discount percents less than or equal to ".49" and any discount percents greater than or equal to ".51" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier discount amounts.

       For example, if most of your discount percents are between ".10" and ".20", use ".10" and ".20" to return discount percents that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual profit amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as ".10", ".20", and ".90", but also " " (a space) and "0" (zero). If the record has *any* value it is returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-discount-percents-conditions-end
