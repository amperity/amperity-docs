.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Names

.. meta::
    :content class=swiftype name=body data-type=text:
        Names

.. meta::
    :content class=swiftype name=title data-type=string:
        Names

==================================================
Names
==================================================

.. attribute-customer-profile-names-start

A customer's name includes the following:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-given-name-start
     :end-before: .. term-given-name-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-surname-start
     :end-before: .. term-surname-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-full-name-start
     :end-before: .. term-full-name-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-generational-suffix-start
     :end-before: .. term-generational-suffix-end

.. attribute-customer-profile-names-end


.. _attribute-customer-profile-names-segment:

Use in segments
==================================================

.. attribute-customer-profile-names-access-start

You can access name attributes directly from the **Segment Editor**. To add these attributes to your segment, click **Add criteria**, select the **Customer 360** table, select a combination of **Given Name**, **Surname**, **Full Name**, and **Generational Suffix** attributes, apply a condition, and then specify a value.

.. attribute-customer-profile-names-access-end


.. _attribute-customer-profile-names-conditions:

Available conditions
==================================================

.. attribute-customer-profile-names-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

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

.. attribute-customer-profile-names-conditions-end
