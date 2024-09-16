.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Physical addresses

.. meta::
    :content class=swiftype name=body data-type=text:
        Physical addresses

.. meta::
    :content class=swiftype name=title data-type=string:
        Physical addresses

==================================================
Physical addresses
==================================================

.. attribute-customer-profile-addresses-start

A customer's physical address includes the following:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-address-start
     :end-before: .. term-address-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-city-start
     :end-before: .. term-city-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-state-start
     :end-before: .. term-state-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-postal-start
     :end-before: .. term-postal-end

.. attribute-customer-profile-addresses-end

.. attribute-customer-profile-addresses-note-start

.. note:: When a customer has a complete physical address in their profile, they are considered to have a "contactable address".

.. attribute-customer-profile-addresses-note-end


.. _attribute-customer-profile-addresses-segment:

Use in segments
==================================================

.. attribute-customer-profile-addresses-access-start

You can access address attributes directly from the **Segment Editor**. To add these attributes to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Customer 360** table, select a combination of **Address**, **Address2**, **City**, **State**, and **Postal** attributes, apply a condition, and then specify a value.

.. attribute-customer-profile-addresses-access-end


.. _attribute-customer-profile-addresses-conditions:

Available conditions
==================================================

.. attribute-customer-profile-addresses-conditions-start

The following table lists the conditions that are available to physical address attributes.

.. note:: All physical address attributes have a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

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

.. attribute-customer-profile-addresses-conditions-end
