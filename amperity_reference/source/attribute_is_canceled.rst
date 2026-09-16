.. https://docs.amperity.com/reference/


.. |what-access| replace:: **is cancellation** attribute
.. |what-choose| replace:: **is cancellation**
.. |what-find| replace:: "cancel"


.. meta::
    :description lang=en:
        Did a customer cancel an item?

.. meta::
    :content class=swiftype name=body data-type=text:
        Did a customer cancel an item?

.. meta::
    :content class=swiftype name=title data-type=string:
        Is canceled?

==================================================
Is canceled?
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-is-canceled-start
   :end-before: .. term-is-canceled-end


.. _attribute-is-canceled-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-is-canceled-conditions:

Available operators
==================================================

.. attribute-is-canceled-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a **Boolean** data type. All **Boolean** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is false**
     - |attribute-recommended| **More useful**

       Returns a list of customers who did not cancel an order.

       .. tip:: Add **Is Cancellation** to your segment, and then set the condition to **is false** to ensure that your segment does not contain *any* canceled items.

   * - **is not NULL**
     - Returns a list of customers who canceled an order *or* who did not cancel an order.

   * - **is NULL**
     - Returns customer records that do not have information about canceled orders.

   * - **is true**
     - |attribute-recommended| **More useful**

       Returns a list of customers who canceled an order.

.. attribute-is-canceled-conditions-end
