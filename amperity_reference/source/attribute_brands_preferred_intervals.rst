.. https://docs.amperity.com/reference/


.. |what-access| replace:: preferred brand interval attributes
.. |what-choose| replace:: an interval
.. |what-find| replace:: "preferred brand"


.. meta::
    :description lang=en:
        Which brands had the greatest number of orders during the specified time period?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which brands had the greatest number of orders during the specified time period?

.. meta::
    :content class=swiftype name=title data-type=string:
        Preferred brand intervals

==================================================
Preferred brand intervals
==================================================

.. attribute-brands-preferred-intervals-start

Preferred brand purchase intervals identify the names of brands with the greatest number of orders during the specified time period.

Preferred brand purchases are available at the following intervals:

* L30D Preferred Brands (30 days)
* L3M Preferred Brands (3 months)
* L6M Preferred Brands (6 months)
* L12M Preferred Brands (12 months)
* LY12M Preferred Brands (12-to-24 months)
* Lifetime Preferred Brands (Lifetime)

.. attribute-brands-preferred-intervals-end


.. _attribute-brands-preferred-intervals-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-brands-preferred-intervals-conditions:

Available operators
==================================================

.. attribute-brands-preferred-intervals-conditions-start

The following operators are available to purchase brand intervals.

.. note:: These attributes have an **string** data type. All **string** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".|attribute-recommended| **More useful**

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description

   * - Operator
     - Description

   * - **contains**
     - Returns purchase brand intervals with values that match a string of characters.

   * - **does not contain**
     - Returns purchase brand intervals with values that do not match a string of characters.

   * - **ends with**
     - Returns purchase brand intervals with values that end with the specified characters.

   * - **is empty**
     - Returns purchase brand intervals that do not have a value in this field.

   * - **is exactly**
     - Returns all purchase brand intervals with values that match the specified characters.

   * - **is not empty**
     - Returns purchase brand intervals that have a value in this field.

   * - **is not exactly**
     - Returns purchase brand intervals that do not match the specified characters.

   * - **starts with**
     - Returns purchase brand intervals that start with the specified characters.

.. attribute-brands-preferred-intervals-conditions-end
