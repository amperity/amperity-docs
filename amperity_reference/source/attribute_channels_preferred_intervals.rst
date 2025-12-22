.. https://docs.amperity.com/reference/


.. |what-access| replace:: preferred channel interval attributes
.. |what-choose| replace:: an interval
.. |what-find| replace:: "preferred purchase"


.. meta::
    :description lang=en:
        Which channel had the greatest number of orders during a defined interval, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        Which channel had the greatest number of orders during a defined interval, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Preferred channel intervals

==================================================
Preferred channel intervals
==================================================

.. attribute-channel-preferred-intervals-start

Preferred channel intervals represent channels with the greatest number of orders during the specified time period. Preferred channel purchase attributes are available at the following intervals:

* L30D Preferred Purchase Channel (30 days)
* L3M Preferred Purchase Channel (3 months)
* L6M Preferred Purchase Channel (6 months)
* L12M Preferred Purchase Channel (12 months)
* LY12M Preferred Purchase Channel (12-to-24 months)
* Lifetime Preferred Purchase Channel (Lifetime)

.. attribute-channel-preferred-intervals-end


.. _attribute-channel-preferred-intervals-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-channels-preferred-intervals-conditions:

Available operators
==================================================

.. attribute-channels-preferred-intervals-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have a **string** data type. All **string** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

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

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-channels-preferred-intervals-conditions-end
