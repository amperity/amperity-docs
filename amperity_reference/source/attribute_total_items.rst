.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The number of items that were purchased as part of a customer's first, second, or most recent recent order.

.. meta::
    :content class=swiftype name=body data-type=text:
        The number of items that were purchased as part of a customer's first, second, or most recent recent order.

.. meta::
    :content class=swiftype name=title data-type=string:
        Total items

==================================================
Total items
==================================================

.. attribute-total-items-common-start

Total items is a collection of attributes that represent the number of items that were purchased as part of a customer's first, second, or most recent recent order.

.. attribute-total-items-common-end


.. _attribute-total-items-segment:

Use in segments
==================================================

.. attribute-total-items-ordered-start

You can access total items attributes directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select one of **First Order Total Items**, **Latest Order Latest Items**, or **Second Order Second Items**, apply a condition, and then specify a value.

.. attribute-total-items-ordered-end


.. _attribute-total-items-ordered-conditions:

Available conditions
==================================================

.. attribute-total-items-ordered-conditions-start

The following table lists the conditions that are available to total items attributes.

.. note:: Total items attributes have an Integer data type. All Integer data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description

   * - **is**
     - Returns customer records with values that match the specified number of items in the order.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are between the specified number of items in the order.

       For example: if **is between** is set to 10 and 20, then customer records with at least 11 (but not more than 19) total items will be returned.

   * - |attribute-recommended| **More useful**

       **is greater than**
     - Returns customer records with values that are greater than the specified number of items in the order, not including the specified number of items.

       For example: if **is greater than** is set to 10, then customer records with 11 (or more) total items will be returned.

   * - |attribute-recommended| **More useful**

       **is greater than or equal to**
     - Returns customer records with values that are greater than or equal to the specified number of items in the order, including the specified number of items.

       For example: if **is greater than or equal to** is set to 10, then customer records with 10 (or more) total items will be returned.

   * - **is in list**
     - Returns customer records with values that match the number of items in the order that are specified in a list.

   * - **is less than**
     - Returns customer records with values that are less than the specified number of items in the order, not including the specified number of items.

       For example: if **is less than** is set to 20, then customer records with 19 (or fewer) total items will be returned.

   * - **is less than or equal to**
     - Returns customer records with values that are less than or equal to the specified number of items in the order, including the specified number of items.

       For example: if **is less than or equal to** is set to 20, then customer records with 20 (or fewer) total items will be returned.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the specified number of items in the order.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with values that are not between the specified number of items in the order, not including the specified number of items.

       For example: if **is not between** is set to 12 and 24, then customer records with at least 25 (but not more than 11) total items will be returned.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the number of items in the order that are specified in the list.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-total-items-ordered-conditions-end
