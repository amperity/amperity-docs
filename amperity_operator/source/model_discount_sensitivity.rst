.. https://docs.amperity.com/internal/



.. meta::
    :description lang=en:
        Discount sensitivity categorizes customers into three groups: full price shopper, discount opportunist, and discount seeker.

.. meta::
    :content class=swiftype name=body data-type=text:
        Discount sensitivity categorizes customers into three groups: full price shopper, discount opportunist, and discount seeker.

.. meta::
    :content class=swiftype name=title data-type=string:
        Discount sensitivity

==================================================
Discount sensitivity model
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-discount-sensitivity-start
   :end-before: .. term-discount-sensitivity-end

.. model-discount-sensitivity-types-start

Use discount sensitivity groupings to identify each customer's optimal discount level.

* A full-price shopper is a customer who is likely willing to pay the manufacturer's suggested price for an item.

  Full-price shoppers are your brand's core audience for your brand's best and newest products. Limit promotional messaging and offers to protect margin. Lead with product and brand content even throughout sales. Are often early adopters and should respond to "new arrivals" messaging.

  .. tip:: Use people-based measurement with full-price shoppers and hold out 20%. Send the same volume of offers, and then measure if the revenue per user from customers who were suppressed from the offer is consistent with the revenue per user from customers who were not suppressed.

* A discount opportunist is a customer who is more likely to purchase when a discount is available.

  Discount opportunists should receive a series of decreasing offers that seek to wean them off discounts. Use a mix of brand and offer content to protect margin and limit discount percentages. Combine with product affinitites to promote slower moving products.

* A discount seeker is a customer who is unlikely to purchase without a discount being available.

  Discount seekers are your brand's core audience for sale and clearance messaging. Promote sale-on-sale and deep clearance offers only to customers who belong to this grouping. Combine this audience with product affinitites to promote discounts on slower moving products.

.. note:: Customers who have not purchased within the modeling window, which is 3 years by default, are not assigned to a discount sensitivity grouping.

.. model-discount-sensitivity-types-end


.. _model-discount-sensitivity-use-cases:

Use cases
==================================================

.. model-discount-sensitivity-use-cases-start

Discount sensitivity modeling supports the following use cases:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Use case
     - Description

   * - **Discount optimization**
     - Identify the types of discounts at which customers are more likely to respond. Optimize discount-focused campaigns to ensure that customers who are more likely to convert with a stronger discount offer are included, while excluding customers who are more likely to pay full price.

   * - **Email segmentation**
     - Identify discount-seeking customers who are more likely to respond to offers in clearance- and sale-focused email campaigns. Protect your brand's margin by identifying customers who are more likely to pay full price, and then exclude them from clearance- and sale-focued email campaigns.

   * - **Product recommendations**
     - Use price point discount segmentation to recommend products at a customer's preferred price point.

.. model-discount-sensitivity-use-cases-end


.. _model-discount-sensitivity-configure:

Build a discount sensitivity model
==================================================

.. model-discount-sensitivity-configure-start

Ask Amperity Support to enable discount sensitivity modeling for your tenant.

.. model-discount-sensitivity-configure-end


.. _model-discount-sensitivity-segments:

Use in segments
==================================================

.. model-discount-sensitivity-segments-start

The following table describes the fields that are available when using discount sensitivity modeling in segments.

.. model-discount-sensitivity-segments-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-discount-sensitivity-table-start
   :end-before: .. data-tables-discount-sensitivity-table-end
