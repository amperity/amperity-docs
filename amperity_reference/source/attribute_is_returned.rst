.. https://docs.amperity.com/reference/


.. |what-access| replace:: **is returned** attribute
.. |what-choose| replace:: **is returned**
.. |what-find| replace:: "return"


.. meta::
    :description lang=en:
        Did a customer return an item?

.. meta::
    :content class=swiftype name=body data-type=text:
        Did a customer return an item?

.. meta::
    :content class=swiftype name=title data-type=string:
        Is returned?

==================================================
Is returned?
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-is-return-start
   :end-before: .. term-is-return-end


.. _attribute-is-return-access-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-is-return-conditions:

Available operators
==================================================

.. attribute-is-return-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a Boolean data type. All Boolean data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is false**
     - |attribute-recommended| **More useful**

       Returns a list of customers who did not return an item.

       .. tip:: Add **Is Returned** to your segment, and then set the condition to **is false** to ensure that your segment does not contain *any* returned items.

   * - **is not NULL**
     - Returns a list of customers who returned an item *or* who did not return an item.

   * - **is NULL**
     - Returns customer records that do not have information about returned items.

   * - **is true**
     - |attribute-recommended| **More useful**

       Returns a list of customers who returned an item.

.. attribute-is-return-conditions-end
