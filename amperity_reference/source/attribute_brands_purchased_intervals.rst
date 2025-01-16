.. https://docs.amperity.com/reference/


.. |what-access| replace:: purchase brands interval attributes
.. |what-choose| replace:: an interval
.. |what-find| replace:: "purchase brands"


.. meta::
    :description lang=en:
        From which brands did your customers purchase at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=body data-type=text:
        From which brands did your customers purchase at defined intervals, such as 30 days, 3 months, or 12 months.

.. meta::
    :content class=swiftype name=title data-type=string:
        Purchased brand intervals

==================================================
Purchased brand intervals
==================================================

.. attribute-brands-purchased-intervals-start

Purchased brand intervals count the number of distinct brands a customer interacted with during the specified time period. Purchased brands are available at the following intervals:

* L30D Purchase Brands (30 days)
* L3M Purchase Brands (3 months)
* L6M Purchase Brands (6 months)
* L12M Purchase Brands (12 months)
* LY12M Purchase Brands (12-to-24 months)
* Lifetime Purchase Brands (Lifetime)

.. attribute-brands-purchased-intervals-end


.. _attribute-brands-purchased-intervals-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-brands-purchase-intervals-conditions:

Available operators
==================================================

.. attribute-brands-purchase-intervals-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have a Integer data type. All Integer data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Returns customer records with values that match the number of distinct brands a customer purchased.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are between each of the specified numbers of distinct brands a customer purchased.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are greater than the number of distinct brands a customer purchased, not including the specified number of purchases.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are greater than or equal to the number of distinct brands a customer purchased, including the specified number of purchases.

   * - **is in list**
     - Returns customer records with values that match the specified number of distinct brands a customer purchased.

   * - **is less than**
     - Returns customer records with values that are less than the number of distinct brands a customer purchased, not including the specified number of purchases.

   * - **is less than or equal to**
     - Returns customer records with values that are less than or equal to the number of distinct brands a customer purchased, including the specified number of purchases.

   * - **is not**
     - |attribute-stop| **Less useful**

       Returns customer records with values that do not match the number of distinct brands a customer purchased.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns customer records with values that are not between each of the specified numbers of distinct brands a customer purchased.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Returns records with values that do not match the specified number of distinct brands a customer purchased.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-brands-purchase-intervals-conditions-end
