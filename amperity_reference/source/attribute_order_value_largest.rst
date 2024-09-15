.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The largest order that is associated with a customer, ignoring returns and/or cancellations, for a customer’s entire purchase history.

.. meta::
    :content class=swiftype name=body data-type=text:
        The largest order that is associated with a customer, ignoring returns and/or cancellations, for a customer’s entire purchase history.

.. meta::
    :content class=swiftype name=title data-type=string:
        Largest order value

==================================================
Largest order value
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-lifetime-largest-order-value-start
   :end-before: .. term-lifetime-largest-order-value-end

.. attribute-order-value-largest-list-start

Largest order values are available at the following intervals:

* L30D Largest Order Value (30 days)
* Lifetime Largest Order Value (Lifetime)

.. attribute-order-value-largest-list-end


.. _attribute-order-value-segment:

Use in segments
==================================================

.. attribute-order-value-largest-start

You can access largest order values directly from the **Segment Editor**. To add this attribute to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select a largest order value attribute, apply a condition, and then specify a value.

.. attribute-order-value-largest-end


.. _attribute-order-value-largest-conditions:

Available conditions
==================================================

.. attribute-order-value-largest-conditions-start

The following table lists the conditions that are available to largest order value interval attributes.

.. note:: Largest order value interval attributes have a Decimal data type. All Decimal data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific amount of largest order values, such as "167.99", "123.99", or "79.99".

       .. tip:: Use the following conditions to return a range of largest order value amounts instead of a specific largest order value amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of largest order value amounts that are between the specified largest order value amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns largest order value amounts that are greater than the specified largest order value amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns largest order value amounts that are greater than or equal to the specified largest order value amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual largest order value amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns largest order value amounts that are less than the specified largest order value amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns largest order value amounts that are less than or equal to the specified largest order value amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "150.00" then any largest order value amounts less than or equal to "149.99" and any largest order value amounts greater than or equal to "150.01" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your largest order value amounts are between "100.00" and "140.00", use "100.00" and "150.00" to return largest order value amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual subtotal amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "14.99", "59.99", and "127.22", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-order-value-largest-conditions-end
