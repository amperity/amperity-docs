.. https://docs.amperity.com/reference/


.. |what-access| replace:: cost attributes
.. |what-choose| replace:: **item cost**, **order cost**, or **unit cost**
.. |what-find| replace:: "cost"


.. meta::
    :description lang=en:
        The underlying cost for items within a transaction.

.. meta::
    :content class=swiftype name=body data-type=text:
        The underlying cost for items within a transaction.

.. meta::
    :content class=swiftype name=title data-type=string:
        Costs

==================================================
Costs
==================================================

.. attribute-costs-start

Costs represent the underlying cost for items within a transaction:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-item-cost-start
     :end-before: .. term-item-cost-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-order-cost-start
     :end-before: .. term-order-cost-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-unit-cost-start
     :end-before: .. term-unit-cost-end

.. attribute-costs-end


.. _attribute-costs-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-costs-conditions:

Available operators
==================================================

.. attribute-costs-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have a Decimal data type. All Decimal data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific cost amount, such as "47.99", "59.99", or "79.99".

       .. tip:: Use the following operators to return a range of cost amounts instead of a specific cost amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of cost amounts that are between the specified cost amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns cost amounts that are greater than the specified cost amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns cost amounts that are greater than or equal to the specified cost amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition. Individual cost amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns cost amounts that are less than the specified cost amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns cost amounts that are less than or equal to the specified cost amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "59.99" then any cost amounts less than or equal to "59.98" and any cost amounts greater than or equal to "60.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your cost amounts are between "59.99" and "89.99", use "59.99" and "89.99" to return cost amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual revenue amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "12.45", "24.75", and "127.99", but also " " (a space) and "0" (zero). If the record has *any* value it is returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-costs-conditions-end
