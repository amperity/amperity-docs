.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Did your customers make a repeat purchase within the last 365 days?

.. meta::
    :content class=swiftype name=body data-type=text:
        Did your customers make a repeat purchase within the last 365 days?

.. meta::
    :content class=swiftype name=title data-type=string:
        Repeat within 365 days?

==================================================
Repeat within 365 days?
==================================================

.. include:: ../../amperity_ampiq/source/onetime_buyers.rst
   :start-after: .. onetime-buyers-about-start
   :end-before: .. onetime-buyers-about-end

.. attribute-repeat-365-start

Use the following attributes as longer-term indicators of one-time buyers transitioning into becoming repeat customers:

* :ref:`... of first order? <attribute-repeat-365-first>`
* :ref:`... of second order? <attribute-repeat-365-second>`

.. attribute-repeat-365-end


.. _attribute-repeat-365-first:

Of first order?
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-first-order-is-retained-start
   :end-before: .. term-first-order-is-retained-end

.. attribute-repeat-365-first-start

You can access if a customer made a second purchase within 365 days of their first purchase from the **Segment Editor**. To add this attribute to your segment, click **Add criteria**, select the **Transaction Attributes Extended** table, select the **First Order Is Retained** attribute, apply a condition, and then specify a value.

.. attribute-repeat-365-first-end

.. image:: ../../images/attribute-first-order-is-retained.png
   :width: 600 px
   :alt: Choose the first order is retained attribute from the Segment Editor.
   :align: left
   :class: no-scaled-link


.. _attribute-repeat-365-second:

Of second order?
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-second-order-is-retained-start
   :end-before: .. term-second-order-is-retained-end


.. _attribute-repeat-365-second-segment:

Use in segments
==================================================

.. attribute-repeat-365-second-start

You can access if a customer made a third purchase within 365 days of their second purchase from the **Segment Editor**. To add this attribute to your segment, click **Add criteria**, select the **Transaction Attributes Extended** table, select the **Second Order Is Retained** attribute, and then apply an condition.

.. attribute-repeat-365-second-end


.. _attribute-repeat-365-conditions:

Available conditions
==================================================

.. attribute-repeat-365-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have a Boolean data type. All Boolean data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is false**
     - |attribute-recommended| **More useful**

       Returns a list of customers who do not made a repeat purchase within the specified time window.

   * - **is not NULL**
     - Returns a list of customers who did *or* did not make a repeat purchase within the specified time window.

   * - **is NULL**
     - Returns customer records that do not have information about repeat orders.

   * - **is true**
     - |attribute-recommended| **More useful**

       Returns a list of customers who have made repeat orders.

.. attribute-repeat-365-conditions-end
