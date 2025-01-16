.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **gender** attribute
.. |what-choose| replace:: **gender**
.. |what-find| replace:: "gender"


.. meta::
    :description lang=en:
        Gender

.. meta::
    :content class=swiftype name=body data-type=text:
        Gender

.. meta::
    :content class=swiftype name=title data-type=string:
        Gender

==================================================
Gender
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-gender-start
   :end-before: .. term-gender-end


.. _attribute-customer-profile-gender-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-customer-profile-gender-conditions:

Available operators
==================================================

.. attribute-customer-profile-gender-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a String data type. All String data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
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

.. attribute-customer-profile-gender-conditions-end
