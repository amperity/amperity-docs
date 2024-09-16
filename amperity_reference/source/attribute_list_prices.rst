.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The manufacturer’s suggested retail price (MSRP) for all units of this item, before shipping, tax, or discount amounts.

.. meta::
    :content class=swiftype name=body data-type=text:
        The manufacturer’s suggested retail price (MSRP) for all units of this item, before shipping, tax, or discount amounts.

.. meta::
    :content class=swiftype name=title data-type=string:
        List prices

==================================================
List prices
==================================================

.. attribute-list-prices-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-list-price-start
   :end-before: .. term-list-price-end

* .. include:: ../../shared/terms.rst
     :start-after: .. term-item-list-price-start
     :end-before: .. term-item-list-price-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-order-list-price-start
     :end-before: .. term-order-list-price-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-unit-list-price-start
     :end-before: .. term-unit-list-price-end

.. attribute-list-prices-end


.. _attribute-list-prices-segment:

Use in segments
==================================================

.. attribute-list-prices-access-start

You can access list price attributes directly from the **Segment Editor**. To add these attributes to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Unified Itemized Transactions** table (for **Item List Price** and **Unit List Price**) *or* the **Unified Transactions** table (for **Order List Price**), apply a condition, and then specify a value.

.. attribute-list-prices-access-end


.. _attribute-list-prices-conditions:

Available conditions
==================================================

.. attribute-list-prices-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have a Decimal data type. All Decimal data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific list price, such as "9.99", "49.99", or "52.74".

       .. tip:: Use the following conditions to return a range of list prices instead of a specific list price: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of list prices that are between the specified list prices.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns list prices that are greater than the specified list price.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns list prices that are greater than or equal to the specified list price.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual list price amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns list prices that are less than the specified list price.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns list prices that are less than or equal to the specified list price.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "10.25" then any list price less than or equal to "10.24" and any list price greater than or equal to "10.26" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       **is not between** discovers outlier prices.

       For example, if most of your list prices are between "19.99" and "99.99", use "19.99" and "99.99" to return list prices that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual price amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "4.99", "1.25", and "99.99", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - **is NULL** returns customer records that do not have a value.

.. attribute-list-prices-conditions-end
