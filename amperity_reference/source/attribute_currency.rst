.. https://docs.amperity.com/reference/


.. |what-access| replace:: **currency** attribute
.. |what-choose| replace:: **currency**
.. |what-find| replace:: "currency"


.. meta::
    :description lang=en:
        What currency was used to pay for an item?

.. meta::
    :content class=swiftype name=body data-type=text:
        What currency was used to pay for an item?

.. meta::
    :content class=swiftype name=title data-type=string:
        Currency

==================================================
Currency
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-currency-start
   :end-before: .. term-currency-end


.. _attribute-currency-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-currency-conditions:

Available operators
==================================================

.. attribute-currency-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a **string** data type. All **string** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

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
     - |attribute-recommended| **More useful**

       Returns all customer records with values that match the specified characters.

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - |attribute-recommended| **More useful**

       Returns customer records that start with the specified characters.

.. attribute-currency-conditions-end
