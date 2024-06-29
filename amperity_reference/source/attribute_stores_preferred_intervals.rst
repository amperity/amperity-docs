.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Preferred stores at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        Preferred stores at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Preferred store intervals

==================================================
Preferred store intervals
==================================================

.. attribute-stores-preferred-start

Preferred store interval attributes identify the store with the greatest number of orders during the specified time period. Preferred store ID attributes are available at the following intervals:

* L30D Preferred Store ID (30 days)
* L3M Preferred Store ID (3 months)
* L6M Preferred Store ID (6 months)
* L12M Preferred Store ID (12 months)
* LY12M Preferred Store ID (12-to-24 months)
* Lifetime Preferred Store ID (Lifetime)

.. attribute-stores-preferred-end


.. _attribute-stores-preferred-segment:

Use in segments
==================================================

.. attribute-stores-preferred-segment-start

You can access 30 day preferred store intervals directly from the **Segment Editor**. To add these attributes to your segment, click **Add criteria**, select the **Transaction Attributes Extended** table, select a preferred store interval attribute, and then apply a condition.

.. attribute-stores-preferred-segment-end


.. _attribute-stores-preferred-conditions:

Available conditions
==================================================

.. attribute-stores-preferred-conditions-start

The following table lists the conditions that are available to preferred store interval attributes.

.. note:: Preferred store interval attributes have a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description

   * - **contains**
     - Returns customer records with values that match a string of characters.

   * - **does not contain**
     - Returns customer records with values that do not match a string of characters.

   * - **ends with**
     - Returns customer records with values that end with the specified characters.

   * - **is empty**
     - |attribute-stop| **Less useful**

       Returns customer records that do not have a value in this field.

   * - **is exactly**
     - |attribute-recommended| **More useful**

       Returns all customer records with values that match the specified characters.

   * - **is not empty**
     - |attribute-stop| **Less useful**

       Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-stores-preferred-conditions-end
