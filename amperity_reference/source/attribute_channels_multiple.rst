.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **multi purchase channel** attribute
.. |what-choose| replace:: **multi-purchase channel**
.. |what-find| replace:: "multi purchase channel"


.. meta::
    :description lang=en:
        Which customers purchased from more than one channel?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which customers purchased from more than one channel?

.. meta::
    :content class=swiftype name=title data-type=string:
        Multichannel purchases?

==================================================
Multichannel purchases?
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-multi-channel-start
   :end-before: .. term-multi-channel-end


.. _attribute-channels-multi-purchase-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-channels-multi-purchase-examples:

Examples
==================================================

.. attribute-channels-multi-purchase-examples-start

The following topics contain examples of using multi-purchase channel:

* |usecase_customers_high_value_multichannel|

.. attribute-channels-multi-purchase-examples-end


.. _attribute-channels-multi-purchase-conditions:

Available operators
==================================================

.. attribute-channels-multi-purchase-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a **Boolean** data type. All **Boolean** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is false**
     - |attribute-recommended| **More useful**

       Returns a list of customers who do not have multichannel purchases.

   * - **is not NULL**
     - Returns a list of customers who returned an order *or* who did not return an order.

   * - **is NULL**
     - Returns customer records that do not have information about returned orders.

   * - **is true**
     - |attribute-recommended| **More useful**

       Returns a list of customers who have multichannel purchases.

.. attribute-channels-multi-purchase-conditions-end
