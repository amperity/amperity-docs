.. 
.. https://docs.amperity.com/ampiq/
.. 

.. meta::
    :description lang=en:
        Which customers made their first order during the specified date range?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which customers made their first order during the specified date range?

.. meta::
    :content class=swiftype name=title data-type=string:
        First order

==================================================
First order
==================================================

.. include:: ../../amperity_reference/source/attribute_compound_first_order.rst
   :start-after: .. attribute-compound-first-order-start
   :end-before: .. attribute-compound-first-order-end

.. purchase-behavior-first-order-common-admonition-start

.. TODO: This admonition is shared across all purchase behavior topics.

.. admonition:: What are purchase behaviors?

   Purchase behaviors are a feature of Amperity that are built on top of standard output for transactions (orders and items). Purchase behaviors require standardized product catalog field names to be present in your standard output for transactions.

   Use purchase behaviors in segments to return a list of customers, *and then* filter that list of customers by any combination of brand, channel, individual items in your product catalog, and store.

   Purchase behaviors are available for :doc:`first order <purchase_behavior_first_order>`, :doc:`has not purchased <purchase_behavior_has_not_purchased>`, :doc:`has purchased <purchase_behavior_has_purchased>`, :doc:`most frequent order <purchase_behavior_most_frequent_order>`, :doc:`repeat order <purchase_behavior_repeat_order>`, and :doc:`total value of orders <purchase_behavior_total_value_of_orders>`.

.. purchase-behavior-first-order-common-admonition-end


.. _purchase-behavior-first-order-howitworks:

How first order works
==================================================

.. include:: ../../amperity_reference/source/attribute_compound_first_order.rst
   :start-after: .. attribute-compound-first-order-howitworks-start
   :end-before: .. attribute-compound-first-order-howitworks-end

.. segments-behaviors-first-order-tip-start

.. tip:: For more information about how **First Order** works, including an explanation of the SQL that runs behind the **Segment Editor**, review the |attribute_compound_first_order| topic in the Amperity A-Z reference.

.. segments-behaviors-first-order-tip-end


.. _purchase-behavior-first-order-useinsegment:

Use first order in a segment
==================================================

.. include:: ../../amperity_reference/source/attribute_compound_first_order.rst
   :start-after: .. attribute-compound-first-order-segments-start
   :end-before: .. attribute-compound-first-order-segments-end

.. image:: ../../images/attribute-compound-first-order.png
   :width: 600 px
   :alt: Use the first order attribute to find first orders by date range.
   :align: left
   :class: no-scaled-link

.. include:: ../../amperity_reference/source/attribute_compound_first_order.rst
   :start-after: .. attribute-compound-first-order-segments-filters-start
   :end-before: .. attribute-compound-first-order-segments-filters-end
