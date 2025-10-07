.. https://docs.amperity.com/user/


.. meta::
    :description lang=en:
        Which customers made their first purchase during the specified date range?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which customers made their first purchase during the specified date range?

.. meta::
    :content class=swiftype name=title data-type=string:
        First purchase

==================================================
First purchase
==================================================

.. include:: ../../amperity_reference/source/attribute_purchase_behavior_first_purchase.rst
   :start-after: .. attribute-purchase-behavior-first-purchase-start
   :end-before: .. attribute-purchase-behavior-first-purchase-end

.. purchase-behavior-first-purchase-common-admonition-start

.. TODO: This admonition is shared across all purchase behavior topics.

.. admonition:: What are purchase behaviors?

   Purchase behaviors are a feature of Amperity that are built on top of standard output for transactions. Purchase behaviors require standardized product catalog field names to be present in your standard output for transactions.

   Use purchase behaviors in segments to return a list of customers, *and then* filter that list of customers by any combination of brand, channel, individual items in your product catalog, and store.

   Purchase behaviors are available for :doc:`first purchase <purchase_behavior_first_purchase>`, :doc:`has not purchased <purchase_behavior_has_not_purchased>`, :doc:`has purchased <purchase_behavior_has_purchased>`, :doc:`most frequent order <purchase_behavior_most_frequent_order>`, :doc:`repeat purchase <purchase_behavior_repeat_purchase>`, and :doc:`total value of orders <purchase_behavior_total_value_of_orders>`.

.. purchase-behavior-first-purchase-common-admonition-end


.. _purchase-behavior-first-purchase-howitworks:

How first purchase works
==================================================

.. include:: ../../amperity_reference/source/attribute_purchase_behavior_first_purchase.rst
   :start-after: .. attribute-purchase-behavior-first-purchase-howitworks-start
   :end-before: .. attribute-purchase-behavior-first-purchase-howitworks-end

.. segments-behaviors-first-purchase-tip-start

.. tip:: For more information about how **First purchase** works, including an explanation of the SQL that runs behind the **Segment Editor**, review the |attribute_purchase_behavior_first_purchase| topic in the Amperity A-Z reference.

.. segments-behaviors-first-purchase-tip-end


.. _purchase-behavior-first-purchase-useinsegment:

Use first purchase in a segment
==================================================

.. include:: ../../amperity_reference/source/attribute_purchase_behavior_first_purchase.rst
   :start-after: .. attribute-purchase-behavior-first-purchase-segments-start
   :end-before: .. attribute-purchase-behavior-first-purchase-segments-end


.. _purchase-behavior-first-purchase-conditions:

Available conditions
==================================================

.. include:: ../../amperity_reference/source/attribute_purchase_behavior_first_purchase.rst
   :start-after: .. attribute-purchase-behavior-first-purchase-conditions-start
   :end-before: .. attribute-purchase-behavior-first-purchase-conditions-end


.. _purchase-behavior-first-purchase-filter-attributes:

Filter attributes
==================================================

.. attribute-purchase-behavior-first-purchase-filter-attributes-start

A filter attribute is a standard column that is output by Amperity and is available from the **Unified Itemized Transactions** table. When a filter attribute is associated with a purchase behavior attribute, you may use them to filter the results by specific items in your product catalog, such as by brand, by channel, by store, or by specific details about the items in your product catalog, such as color, or SKU. The list of filter attributes that will be available for product catalogs depends on their availability within your **Unified Itemized Transactions** table.

.. attribute-purchase-behavior-first-purchase-filter-attributes-end
