.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The unique identifiers for your brand's physical locations.

.. meta::
    :content class=swiftype name=body data-type=text:
        The unique identifiers for your brand's physical locations.

.. meta::
    :content class=swiftype name=title data-type=string:
        Store IDs

==================================================
Store IDs
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-store-id-start
   :end-before: .. term-store-id-end


.. _attribute-store-id-segment:

Use in segments
==================================================

.. attribute-stores-id-start

You can access store IDs directly from the **Segment Editor**. To add these attributes to your segment, click **Add criteria**, select the **Transaction Attributes Extended** table, select the **Store ID** attribute or one of **First Store ID**, **Second Store ID**, and **Latest Store ID**, and then apply a condition.

.. attribute-stores-id-end


.. _attribute-stores-id-conditions:

Available conditions
==================================================

.. attribute-stores-id-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

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

.. attribute-stores-id-conditions-end
