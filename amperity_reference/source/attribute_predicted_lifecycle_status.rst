.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        The likelihood repeat customers and one-time buyers will purchase again, grouped by tiers including "active", "cooling down", "at risk", "highly at risk", and "lost".

.. meta::
    :content class=swiftype name=body data-type=text:
        The likelihood repeat customers and one-time buyers will purchase again, grouped by tiers including "active", "cooling down", "at risk", "highly at risk", and "lost".

.. meta::
    :content class=swiftype name=title data-type=string:
        Predicted lifecycle status

==================================================
Predicted lifecycle status
==================================================

.. attribute-predicted-lifecycle-status-start

Predicted lifecycle status represents the likelihood to purchase again, grouped by tiers: "active", "cooling down", "at risk", "highly at risk", and "lost". These tiers are used for two types of customers: repeat customers and one-time buyers.

.. attribute-predicted-lifecycle-status-end

**Repeat customers**

.. attribute-predicted-lifecycle-status-repeat-start

For repeat customers, lifecycle status groupings use the following thresholds:

#. A repeat customer with an "active" lifecycle status has a greater than 60% likelihood to purchase again.
#. A repeat customer with a "cooling down" lifecycle status has a 50-60% likelihood to purchase again.
#. A repeat customer with an "at risk" lifecycle status has a 35-50% likelihood to purchase again.
#. A repeat customer with a "highly at risk" lifecycle status has a 20-35% likelihood to purchase again.
#. A repeat customer with a "lost" lifecycle status has a less than 20% likelihood to purchase again.

.. attribute-predicted-lifecycle-status-repeat-end

**One-time buyers**

.. attribute-predicted-lifecycle-status-onetime-start

For one-time buyers, lifecycle status groupings use the following thresholds:

#. A one-time buyer with an "active" lifecycle status made a purchase within the last 60 days.
#. A one-time buyer with a "cooling down" lifecycle status made a purchase 60-120 days ago.
#. A one-time buyer with an "at risk" lifecycle status made a purchase 120-180 days ago.
#. A one-time buyer with a "highly at risk" lifecycle status made a purchase 180-240 days ago.
#. A one-time buyer with a "lost" lifecycle status made a purchase more than 240 days ago.

.. attribute-predicted-lifecycle-status-onetime-end


.. _attribute-predicted-lifecycle-status-segment:

Use in segments
==================================================

.. attribute-predicted-lifecycle-status-segment-start

To find predicted lifecycle status, start with the **Predicted Customer Lifecycle Status** attribute in the **Predicted CLV Attributes** table, and then select the **is in list** condition. After the attribute appears in your segment, set the list values to include all of the thresholds you want to use in your segment. For example, choose the **is in list** attribute, and then set predicted lifecycle status to **Active**, **At risk**, and **Cooling down**.

.. attribute-predicted-lifecycle-status-segment-end

.. attribute-predicted-lifecycle-status-modeling-enabled-note-start

.. note:: Predicted lifecycle status is available when predictive modeling is enabled for your tenant.

.. attribute-predicted-lifecycle-status-modeling-enabled-note-end


.. _attribute-predicted-lifecycle-status-conditions:

Available operators
==================================================

.. attribute-predicted-lifecycle-status-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a String data type. All String data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description

   * - **contains**
     - |attribute-recommended| **More useful**

       Returns customer records with values that match a string of characters.

   * - **does not contain**
     - Returns customer records with values that do not match a string of characters.

   * - **ends with**
     - Returns customer records with values that end with the specified characters.

   * - **is empty**
     - Returns customer records that do not have a value in this field.

   * - **is exactly**
     - |attribute-recommended| **More useful**

       Returns all customer records with values that match the specified characters.

       For example, "Active" will return "active" and not "cooling down", "at risk", "highly at risk" or "lost".

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-predicted-lifecycle-status-conditions-end
