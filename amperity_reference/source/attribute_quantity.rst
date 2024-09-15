.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The quantity of items and of orders.

.. meta::
    :content class=swiftype name=body data-type=text:
        The quantity of items and of orders.

.. meta::
    :content class=swiftype name=title data-type=string:
        Quantity

==================================================
Quantity
==================================================

.. attribute-quantity-start

Quantities are available for items and orders:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-item-quantity-start
     :end-before: .. term-item-quantity-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-order-quantity-start
     :end-before: .. term-order-quantity-end

.. attribute-quantity-end


.. _attribute-quantity-segment:

Use in segments
==================================================

.. attribute-quantity-access-start

You can access quantity attributes directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Unified Itemized Transactions** table (for **Item Quantity**) *or* the **Unified Transactions** table (for **Order Quantity**), apply a condition, and then specify a value.

.. attribute-quantity-access-end


.. _attribute-quantity-conditions:

Available conditions
==================================================

.. attribute-quantity-conditions-start

The following table lists the conditions that are available to quantity attributes.

.. note:: Quantity attributes have an Integer data type. All Integer data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - Returns customer records with quantities that match the specified quantity.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns customer records with quantities that are between the specified quantities, not including the specified quantity.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns customer records with quantities that are greater than the specified quantity, not including the specified quantity.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with quantities that are greater than or equal to the specified quantity, including the specified quantity.

   * - **is in list**
     - Returns customer records with quantities that match the quantities that are specified in the list.

   * - **is less than**
     - Returns customer records with quantities that are less than the specified quantity, not including the specified quantity.

   * - **is less than or equal to**
     - Returns customer records with quantities that are less than or equal to the specified quantity, including the specified quantity.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with quantities that do not match the specified quantity.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with quantities that are not between the specified quantities, not including the specified quantity.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns customer records with quantities that do not match the quantities that are specified in the list.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-quantity-conditions-end
