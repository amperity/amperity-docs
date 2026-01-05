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

.. note:: These attributes have an **integer** data type. All **integer** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".|attribute-recommended| **More useful**

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Returns customer records with values that match the number of distinct brands a customer purchased.

   * - **is between**
     - Returns customer records with values that are between each of the specified numbers of distinct brands a customer purchased.

   * - **is greater than**
     - Returns customer records with values that are greater than the number of distinct brands a customer purchased, not including the specified number of purchases.

   * - **is greater than or equal to**
     - Returns customer records with values that are greater than or equal to the number of distinct brands a customer purchased, including the specified number of purchases.

   * - **is in list**
     - Returns customer records with values that match the specified number of distinct brands a customer purchased.

   * - **is less than**
     - Returns customer records with values that are less than the number of distinct brands a customer purchased, not including the specified number of purchases.

   * - **is less than or equal to**
     - Returns customer records with values that are less than or equal to the number of distinct brands a customer purchased, including the specified number of purchases.

   * - **is not**
     - Returns customer records with values that do not match the number of distinct brands a customer purchased.

   * - **is not between**
     - Returns customer records with values that are not between each of the specified numbers of distinct brands a customer purchased.

   * - **is not in list**
     - Returns records with values that do not match the specified number of distinct brands a customer purchased.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-brands-preferred-intervals-conditions-end
