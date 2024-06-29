.. 
.. https://docs.amperity.com/reference/
.. 


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

.. attribute-is-return-start

You can access is return directly from the **Segment Editor**. To add this attribute to your segment, click **Add criteria**, select the **Unified Itemized Transactions** table, select the **Is Return** attribute, and then apply a condition.

.. attribute-is-return-end


.. _attribute-is-return-conditions:

Available conditions
==================================================

.. attribute-is-return-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a Boolean data type. All Boolean data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
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
