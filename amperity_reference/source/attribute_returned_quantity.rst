.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **order returned quantity** attribute
.. |what-choose| replace:: **order returned quantity**
.. |what-find| replace:: "order returned"


.. meta::
    :description lang=en:
        The quantity of returned items in a transaction.

.. meta::
    :content class=swiftype name=body data-type=text:
        The quantity of returned items in a transaction.

.. meta::
    :content class=swiftype name=title data-type=string:
        Order returned quantity

==================================================
Order returned quantity
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-returned-quantity-start
   :end-before: .. term-order-returned-quantity-end


.. _attribute-returned-quantity-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-returned-quantity-conditions:

Available operators
==================================================

.. attribute-returned-quantity-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has an **integer** data type. All **integer** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Returns customer records with values that match the quantity of returned orders.

   * - **is between**
     - Returns customer records with values that are between each of the specified quantities of returned orders.

   * - **is greater than**
     - Returns customer records with values that are greater than the quantity of returned orders, not including the specified quantity of returned orders.

   * - **is greater than or equal to**
     - Returns customer records with values that are greater than or equal to the quantity of returned orders, including the specified quantity of returned orders.

   * - **is in list**
     - Returns customer records with values that match the specified quantity of returned orders.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are less than the quantity of returned orders, not including the specified quantity of returned orders.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are less than or equal to the number of quantity of returned orders, including the specified quantity of returned orders.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the quantity of returned orders.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with values that are not between each of the specified quantity of returned orders.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the specified quantity of returned orders.

   * - **is not NULL**
     - Rturns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-returned-quantity-conditions-end
