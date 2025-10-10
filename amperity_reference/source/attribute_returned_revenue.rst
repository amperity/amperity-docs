.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **order returned revenue** attribute
.. |what-choose| replace:: **order returned revenue**
.. |what-find| replace:: "order returned"


.. meta::
    :description lang=en:
        The total amount of revenue for all returned items in a transaction.

.. meta::
    :content class=swiftype name=body data-type=text:
        The total amount of revenue for all returned items in a transaction.


.. meta::
    :content class=swiftype name=title data-type=string:
        Order returned revenue

==================================================
Order returned revenue
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-returned-revenue-start
   :end-before: .. term-order-returned-revenue-end


.. _attribute-returned-revenue-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-returned-revenue-conditions:

Available operators
==================================================

.. attribute-returned-revenue-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a Decimal data type. All Decimal data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific amount of returned order revenue, such as "17.99", "29.99", or "79.99".

       .. tip:: Use the following operators to return a range of returned order revenue amounts instead of a specific revenue amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of returned order revenue amounts that are between the specified returned order revenue amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns returned order revenue amounts that are greater than the specified returned order revenue amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns returned order revenue amounts that are greater than or equal to the specified returned order revenue amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition. Individual returned order revenue amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns returned order revenue amounts that are less than the specified returned order revenue amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns returned order revenue amounts that are less than or equal to the specified returned order revenue amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "11.99" then any returned order revenue amounts less than or equal to "11.98" and any returned order revenue amounts greater than or equal to "12.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your returned order revenue amounts are between "11.99" and "82.99", use "11.99" and "82.99" to return returned order revenue amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual revenue amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "4.99", "5.99", and "27.22", but also " " (a space) and "0" (zero). If the record has *any* value it is returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-returned-revenue-conditions-end
