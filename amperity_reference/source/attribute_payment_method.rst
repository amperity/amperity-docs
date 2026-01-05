.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **payment methods** attribute
.. |what-choose| replace:: **payment methods**
.. |what-find| replace:: "payment methods"


.. meta::
    :description lang=en:
        How did your customers pay for the items they have purchased?

.. meta::
    :content class=swiftype name=body data-type=text:
        How did your customers pay for the items they have purchased?

.. meta::
    :content class=swiftype name=title data-type=string:
        Payment methods

==================================================
Payment methods
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-payment-method-start
   :end-before: .. term-payment-method-end


.. _attribute-payment-method-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-payment-method-conditions:

Available operators
==================================================

.. attribute-payment-method-conditions-start

The following table lists the operators that are available to the payment method attribute.

.. note:: The payment method attribute has a **string** data type. All **string** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

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
     - |attribute-stop| **Less useful**

       Returns customer records that do not have a value in this field.

   * - **is exactly**
     - Returns all customer records with values that match the specified characters.

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-payment-method-conditions-end
