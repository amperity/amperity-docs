.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Product affinity represents product taxonomies that contain between 20 and 2000 unique values for brands, categories, and sub-categories.

.. meta::
    :content class=swiftype name=body data-type=text:
        Product affinity represents product taxonomies that contain between 20 and 2000 unique values for brands, categories, and sub-categories.

.. meta::
    :content class=swiftype name=title data-type=string:
        Product affinity model

==================================================
Product affinity model
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-product-affinity-start
   :end-before: .. term-product-affinity-end

.. model-product-affinity-about-start

Amperity models product affinity for any product taxonomy that contains between 20 and 2000 unique values, such as brand, category, subcategory, color, size, season, and style. Product affinity modeling analyzes:

* Historical data to identify customers who have purchased a product in the past and are likely to do so again.
* Lookalike audiences to identify customers who have not purchased a product, but are likely to buy because they are similar to customers who have purchased.

.. model-product-affinity-about-end


.. _model-product-affinity-use-cases:

Use cases
==================================================

.. model-product-affinity-use-cases-start

The product affinity model enables support for marketing campaigns that benefit from knowing a customer's preferences across product categories, including:

#. :ref:`Recommended audience sizes <model-product-affinity-use-cases-recommended-audiences>`
#. :ref:`Ranking customers by affinity <model-product-affinity-use-cases-customer-ranking>`

.. model-product-affinity-use-cases-end


.. _model-product-affinity-use-cases-recommended-audiences:

Recommended audience sizes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-recommended-audience-size-start
   :end-before: .. term-recommended-audience-size-end

.. model-product-affinity-use-cases-recommended-audiences-about-start

Recommended audience sizes are calculated using customer transaction data over a 30-day window. A purchase curve is generated, along with corresponding audience sizes that show what size audience would have been required to capture 50%, 70%, and 90% of purchases for a given product over the previous 30 days.

Audience sizes are inclusive of all smaller audience sizes.

* A medium audience size (70%) includes all of your customers who are in the small audience size (50%).
* A large audience size (90%) includes all of your customers who are in the small and medium audiences.

.. model-product-affinity-use-cases-recommended-audiences-about-end

.. image:: ../../images/use-cases-recommended-audience-size-all.png
   :width: 600 px
   :alt: The purchase curve.
   :align: left
   :class: no-scaled-link

.. model-product-affinity-recommended-audiences-usecase-start

Recommended audience sizes identify customers who are most likely to purchase. Use recommended audience sizes to:

* Engage with customers for product-specific sends, such as clearance sale and new arrival announcements
* Define more valuable campaigns to grow revenue for specific product categories
* Drive up conversion rates
* Drive down opt-outs
* Determine categories, products, and trends that resonate with key segments

.. model-product-affinity-recommended-audiences-usecase-end

.. model-product-affinity-use-cases-recommended-audiences-attributes-start

Attributes for recommended audience sizes are available from the **Predicted Affinity** table:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Attribute Name
     - Description
   * - **Audience Size Small**
     - A small audience is predicted to include ~50% of future purchasers, while including the fewest non-purchasers. Use a small audience size to help prevent wasted spend and reduce opt-outs.
   * - **Audience Size Medium**
     - A medium audience is predicted to include ~70% of future purchasers, though it may also include a moderate number of non-purchasers.
   * - **Audience Size Large**
     - A large audience is predicted to include ~90% of future purchasers, while also including a high number of non-purchasers.

Combine these attributes with the **Product Attribute** attribute to build audiences for a specific product category, class, or brand.

.. model-product-affinity-use-cases-recommended-audiences-attributes-end


.. _model-product-affinity-use-cases-customer-ranking:

Customer ranking
--------------------------------------------------

.. model-product-affinity-use-cases-customer-ranking-start

Use customer ranking to define an audience using the top N customers. Use customer ranking as an alternate to recommended audience sizes when an audience is too large (or small) or if a recommended audience size is unavailable for a specific product or category.

.. model-product-affinity-use-cases-customer-ranking-end

.. model-product-affinity-use-cases-customer-ranking-topn-start

Customer ranking identifies the top N customers who are most likely to purchase. Use customer ranking to:

* Provide an alternative to a recommended audience size, such as when a recommended audience size is unavailable for a specific product or category
* Serve targeted product messages to defined audiences
* Identify first-time buyer personas
* Drive up conversion rates
* Drive down opt-outs

.. model-product-affinity-use-cases-customer-ranking-topn-end

.. model-product-affinity-use-cases-customer-ranking-attribute-start

The **Ranking** attribute in the **Predicted Affinity** table ranks customer scores by product. A rank that is less than or equal to X provides the top N customers with an affinity for this product. Combine this attribute with the **Product Attribute** attribute to build customer rankings for a specific product category, class, or brand.

.. model-product-affinity-use-cases-customer-ranking-attribute-end
