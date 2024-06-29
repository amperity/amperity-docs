.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Is a customer a one-time buyer?

.. meta::
    :content class=swiftype name=body data-type=text:
        Is a customer a one-time buyer?

.. meta::
    :content class=swiftype name=title data-type=string:
        One and done?

==================================================
One and done?
==================================================

.. TODO: The following sections are the first paragraph and the "One and Done attribute" sections from the onetime_buyers topic. Keep these synchronized.

.. include:: ../../amperity_ampiq/source/onetime_buyers.rst
   :start-after: .. onetime-buyers-about-start
   :end-before: .. onetime-buyers-about-end

.. attribute-one-and-done-start

Use a list of one-time buyers to identify combinations of products, time windows, and lookalike audiences that can be used as the starting point for campaigns that focus on turning one-time buyers into repeat customers.
   
.. attribute-one-and-done-end


.. _attribute-one-and-done-segment:

Use in segments
==================================================

.. attribute-one-and-done-find-start

To find one-time buyers, start with the **One and Done** attribute in the **Transaction Attributes Extended** table, and then set its condition to **is true**.

.. attribute-one-and-done-find-end

.. image:: ../../images/attribute-one-and-done.png
   :width: 600 px
   :alt: Choose the one and done attribute from the Segment Editor.
   :align: left
   :class: no-scaled-link

.. attribute-one-and-done-filters-start

The attribute will appear in your segment like this:

.. attribute-one-and-done-filters-end


.. _attribute-one-and-done-conditions:

Available conditions
==================================================

.. attribute-one-and-done-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a Boolean data type. All Boolean data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is false**
     - |attribute-recommended| **More useful**

       Filters your segment to include only customers with at least 2 purchases.

   * - **is not NULL**
     - Returns a list of customers who have made at least 1 purchase, which should be the same list of customers that exists when **is_false** *and* **is_true** are in a segment, both of them are set to "true", *and* you are using the **OR** condition in-between.

   * - **is NULL**
     - Returns a list of 0 customers.

   * - **is true**
     - |attribute-recommended| **More useful**

       Filters your segment to include only customers with 1 purchase.

.. attribute-one-and-done-conditions-end
