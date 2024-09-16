.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The total number of orders that that a customer has made at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        The total number of orders that that a customer has made at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Order frequency intervals

==================================================
Order frequency intervals
==================================================

.. attribute-order-frequency-intervals-start

Order frequency is the total number of orders that that a customer has made during the specified interval. Order frequencies are available at the following intervals:

* L30D Order Frequency (30 days)
* L3M Order Frequency (3 months)
* L6M Order Frequency (6 months)
* L12M Order Frequency (12 months)
* LY12M Order Frequency (12-to-24 months)
* Lifetime Order Frequency (Lifetime)

.. attribute-order-frequency-intervals-end


.. _attribute-order-frequency-intervals-segment:

Use in segments
==================================================

.. attribute-order-frequency-intervals-segment-start

You can access order frequency intervals directly from the **Segment Editor**. To add these attributes to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select an order frequency interval, and then apply a condition.

.. attribute-order-frequency-intervals-segment-end


.. _attribute-order-frequency-interval-conditions:

Available conditions
==================================================

.. attribute-order-frequency-interval-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have an Integer data type. All Integer data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - Returns customer records with values that match the specified order frequency.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are between the specified order frequency.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are greater than the specified order frequency, not including the order frequency.

   * - **is greater than or equal to**
     - Returns customer records with values that are greater than or equal to the specified order frequency, including the order frequency.

       .. tip:: Use the **Lifetime Order Frequency with the **is greater than or equal to** condition to identify unique customers who have made at least one purchase. Set the value of **is greater than or equal to** to the number of purchases you want to be the minimum lifetime order frequency for this segment.

   * - **is in list**
     - Returns customer records with values that match the order frequency that are specified in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are less than the specified order frequency, not including the order frequency.

   * - **is less than or equal to**
     - Returns customer records with values that are less than or equal to the specified order frequency, including the order frequency.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the specified order frequency.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with values that are not between the specified order frequency, not including the order frequency.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the order frequency that is specified in the list.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-order-frequency-interval-conditions-end
