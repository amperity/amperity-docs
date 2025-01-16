.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **order cancelled quantity** attribute
.. |what-choose| replace:: **order cancelled quantity**
.. |what-find| replace:: "order cancelled"


.. meta::
    :description lang=en:
        The total number of items in the original transaction that were canceled.

.. meta::
    :content class=swiftype name=body data-type=text:
        The total number of items in the original transaction that were canceled.

.. meta::
    :content class=swiftype name=title data-type=string:
        Order canceled quantity

==================================================
Order canceled quantity
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-canceled-quantity-start
   :end-before: .. term-order-canceled-quantity-end


.. _attribute-canceled-quantity-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-canceled-quantity-conditions:

Available operators
==================================================

.. attribute-canceled-quantity-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has an Integer data type. All Integer data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Returns customer records with values that match the quantity of canceled orders.

   * - **is between**
     - Returns customer records with values that are between each of the specified quantities of canceled orders.

   * - **is greater than**
     - Returns customer records with values that are greater than the quantity of canceled orders, not including the specified quantity of canceled orders.

   * - **is greater than or equal to**
     - Returns customer records with values that are greater than or equal to the quantity of canceled orders, including the specified quantity of canceled orders.

   * - **is in list**
     - Returns customer records with values that match the specified quantity of canceled orders.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are less than the quantity of canceled orders, not including the specified quantity of canceled orders.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are less than or equal to the number of quantity of canceled orders, including the specified quantity of canceled orders.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the quantity of canceled orders.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with values that are not between each of the specified quantity of canceled orders.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the specified quantity of canceled orders.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-canceled-quantity-conditions-end
