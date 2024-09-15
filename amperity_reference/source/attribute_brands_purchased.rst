.. 
.. https://docs.amperity.com/ampiq/
.. 


.. meta::
    :description lang=en:
        From which brands did your customers purchase?

.. meta::
    :content class=swiftype name=body data-type=text:
        From which brands did your customers purchase?

.. meta::
    :content class=swiftype name=title data-type=string:
        Purchased brands

==================================================
Purchased brands
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-purchase-brand-start
   :end-before: .. term-purchase-brand-end


.. _attribute-brands-purchased-segment:

Use in segments
==================================================

.. attribute-brands-purchased-segments-start

You can access the names of brands that were purchased by your customers directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Unified Transactions** table (for **Purchase Brand**) *or* the **Transaction Attributes Extended** table (for **First Order Purchase Brand**, **Second Order Purchase Brand**, or **Latest Order Purchase Brand**), apply a condition, and then specify a value.

.. attribute-brands-purchased-segments-end


.. _attribute-brands-purchased-conditions:

Available conditions
==================================================

.. attribute-brands-purchased-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
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
     - |attribute-recommended| **More useful**

       Returns customer records that start with the specified characters.

.. attribute-brands-purchased-conditions-end
