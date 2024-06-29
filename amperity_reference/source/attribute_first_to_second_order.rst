.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The number of days that have elapsed between the date of the first order and the date of the second order.

.. meta::
    :content class=swiftype name=body data-type=text:
        The number of days that have elapsed between the date of the first order and the date of the second order.

.. meta::
    :content class=swiftype name=title data-type=string:
        First-to-second order

==================================================
First-to-second order
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-first-to-second-order-days-start
   :end-before: .. term-first-to-second-order-days-end


.. _attribute-first-to-seconds-segment:

Use in segments
==================================================

.. attribute-days-between-orders-first-to-second-start

You can access first-to-second order days directly from the **Segment Editor**. To add this attribute to your segment, click **Add criteria**, select the **Transaction Attributes Extended** table, select the **First To Second Order Days** attribute, apply a condition, and then specify a value.

.. attribute-days-between-orders-first-to-second-end


.. _attribute-first-to-second-conditions:

Available conditions
==================================================

.. attribute-first-to-second-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a Integer data type. All Integer data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - Returns customer records with dates that match the specified date.

   * - **is between**
     - Returns customer records with dates that are between the specified dates, not including the specified date.

   * - **is greater than**
     - Returns customer records with dates that are greater than the specified date, not including the specified date.

   * - **is greater than or equal to**
     - Returns customer records with dates that are greater than or equal to the specified date, including the specified date.

   * - **is in list**
     - Returns customer records with dates that match the dates that are specified in the list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns customer records with dates that are less than the specified date, not including the specified date.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with dates that are less than or equal to the specified date, including the specified date.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with date that do not match the specified date.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with dates that are not between the specified dates, not including the specified date.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns customer records with dates that do not match the dates that are specified in the list.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-first-to-second-conditions-end
