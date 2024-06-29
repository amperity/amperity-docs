.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        From which channel did a transaction occur during a defined interval, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        From which channel did a transaction occur during a defined interval, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Purchased channel intervals

==================================================
Purchased channel intervals
==================================================

.. attribute-channel-purchased-intervals-about-start

Purchased channel attributes represent the count of the distinct channels (online, in store, etc.) through which a customer interacted with your brand during during the specified time period.

.. attribute-channel-purchased-intervals-about-end

.. attribute-channel-purchased-intervals-start

Purchased channel attributes are available at the following intervals:

* L30D Purchase Channels (30 days)
* L3M Purchase Channels (3 months)
* L6M Purchase Channels (6 months)
* L12M Purchase Channels (12 months)
* LY12M Purchase Channels (12-to-24 months)
* Lifetime Purchase Channels (Lifetime)

.. attribute-channel-purchased-intervals-end


.. _attribute-channel-purchased-intervals-segment:

Use in segments
==================================================

.. attribute-channel-purchased-intervals-segment-start

You can access purchased channel intervals directly from the **Segment Editor**. To add this attribute to your segment, click **Add criteria**, select the **Transaction Attributes Extended** table, select a purchase channel interval attribute, and then apply a condition.

.. attribute-channel-purchased-intervals-segment-end


.. _attribute-channel-purchased-intervals-conditions:

Available conditions
==================================================

.. attribute-channel-purchased-intervals-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have an Integer data type. All Integer data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - Returns customer records with values that match the specified purchase channel interval.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are between the specified purchase channel intervals, not including the specified purchase channel interval.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are greater than the specified purchase channel interval, not including the specified purchase channel interval.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are greater than or equal to the specified purchase channel interval, including the specified purchase channel interval.

   * - **is in list**
     - Returns customer records with values that match the purchase channel intervals that are specified in the list.

   * - **is less than**
     - Returns customer records with values that are less than the specified purchase channel interval, not including the specified purchase channel interval.

   * - **is less than or equal to**
     - Returns customer records with values that are less than or equal to the specified purchase channel interval, including the specified purchase channel interval.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the specified purchase channel interval.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with values that are not between the specified purchase channel intervals, not including the specified purchase channel interval.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the purchase channel intervals that are specified in the list.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-channel-purchased-intervals-conditions-end
