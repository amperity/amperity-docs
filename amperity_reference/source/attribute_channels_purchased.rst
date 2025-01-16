.. https://docs.amperity.com/reference/


.. |what-access| replace:: purchase channel attributes
.. |what-choose| replace:: **first order purchase channel**, **second order purchase channel**, or **latest order purchase channel**
.. |what-find| replace:: "channel"


.. meta::
    :description lang=en:
        From which channel did a transaction occur?

.. meta::
    :content class=swiftype name=body data-type=text:
        From which channel did a transaction occur?

.. meta::
    :content class=swiftype name=title data-type=string:
        Purchase channels

==================================================
Purchase channels
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-purchase-channel-start
   :end-before: .. term-purchase-channel-end


.. _attribute-channels-purchased-examples:

Examples
==================================================

.. attribute-channels-purchased-examples-start

The following topics contain examples of using purchase channels:

* |usecase_customers_website_new|

.. attribute-channels-purchased-examples-end


.. _attribute-channels-purchased-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-channels-purchased-conditions:

Available operators
==================================================

.. attribute-channels-purchased-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a String data type. All String data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
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
     - Returns customer records that start with the specified characters.

.. attribute-channels-purchased-conditions-end
