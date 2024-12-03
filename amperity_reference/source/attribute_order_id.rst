.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The unique order ID for each transaction between your brand and your customers.

.. meta::
    :content class=swiftype name=body data-type=text:
        The unique order ID for each transaction between your brand and your customers.

.. meta::
    :content class=swiftype name=title data-type=string:
        Order IDs

==================================================
Order IDs
==================================================

.. attribute-datetimes-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-id-start
   :end-before: .. term-order-id-end

* .. include:: ../../shared/terms.rst
     :start-after: .. term-first-order-id-start
     :end-before: .. term-first-order-id-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-latest-order-id-start
     :end-before: .. term-latest-order-id-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-second-order-id-start
     :end-before: .. term-second-order-id-end

.. attribute-datetimes-end


.. _attribute-order-id-segment:

Use in segments
==================================================

.. attribute-order-id-base-start

You can access order ID attributes directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source (for **First Order ID**, **Latest Order ID**, and **Second Order ID**) *or* the **Unified Transactions** table (for **Order ID**), apply a condition, and then specify a value.

.. attribute-order-id-base-end


.. _attribute-order-id-base-conditions:

Available conditions
==================================================

.. attribute-order-id-base-conditions-start

The following table lists the conditions that are available to order ID attributes.

.. note:: Order ID attributes have a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

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
     - Returns customer records that do not have a value in this field.

   * - **is exactly**
     - Returns all customer records with values that match the specified characters.

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-order-id-base-conditions-end
