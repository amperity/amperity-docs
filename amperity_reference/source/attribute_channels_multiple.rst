.. 
.. https://docs.amperity.com/ampiq/
.. 


.. meta::
    :description lang=en:
        Which customers purchased from more than one channel?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which customers purchased from more than one channel?

.. meta::
    :content class=swiftype name=title data-type=string:
        Multi-channel purchases?

==================================================
Multi-channel purchases?
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-multi-channel-start
   :end-before: .. term-multi-channel-end


.. _attribute-channels-multi-purchase-segment:

Use in segments
==================================================

.. attribute-channels-multi-purchase-start

You can access multichannel purchases directly from the **Segment Editor**. To add this attribute to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select the **Multi Purchase Channel** attribute, and then apply a condition.

.. attribute-channels-multi-purchase-end


.. _attribute-channels-multi-purchase-examples:

Examples
==================================================

.. attribute-channels-multi-purchase-examples-start

The following topics contain examples of using multi-purchase channel:

* |usecase_customers_high_value_multichannel|

.. attribute-channels-multi-purchase-examples-end


.. _attribute-channels-multi-purchase-conditions:

Available conditions
==================================================

.. attribute-channels-multi-purchase-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a Boolean data type. All Boolean data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
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
