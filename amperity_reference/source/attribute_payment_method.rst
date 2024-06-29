.. 
.. https://docs.amperity.com/reference/
.. 


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

.. attribute-payment-method-start

You can access payment methods directly from the **Segment Editor**. Add criteria to your segment, select the **Unified Itemized Transactions** table, select the **Payment Methods** attribute, apply a condition, and then specify a value.

.. attribute-payment-method-end


.. _attribute-payment-method-conditions:

Available conditions
==================================================

.. attribute-payment-method-conditions-start

The following table lists the conditions that are available to the payment method attribute.

.. note:: The payment method attribute has a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

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
