.. https://docs.amperity.com/operator/


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
     - A small audience is predicted to incude ~50% of future purchasers, while including the fewest non-purchasers. Use a small audience size to help prevent wasted spend and reduce opt-outs.
   * - **Audience Size Medium**
     - A medium audience is predicted to include ~70% of future purchasers, though it may also include a moderate number of non-purchasers.
   * - **Audience Size Large**
     - A large audience is predicted to include ~90% of future purchasers, while also including a high number of non-purchasers.

Combine these attributes with the **Product Attribute** attribute to build audiences for a specific product category, class, or brand. You can access these attributes directly from the **Segment Editor**.

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

The **Ranking** attribute in the **Predicted Affinity** table ranks customer scores by product. A rank that is less than or equal to X provides the top N customers with an affinity for this product. Combine this attribute with the **Product Attribute** attribute to build customer rankings for a specific product category, class, or brand. You can access this attribute directly from the **Segment Editor**.

.. model-product-affinity-use-cases-customer-ranking-attribute-end


.. _model-product-affinity-configure:

Build a product affinity model
==================================================

.. model-product-affinity-configure-start

You can build a product affinity model from the **Customer 360** page. Each database that is a "customer 360" database and contains the **Merged Customers**, **Unified Itemized Transactions**, and **Unified Transactions** tables may be configured for predictive modeling. You may use other tables in that database that are unique by Amperity ID to extend predictive models.

.. model-product-affinity-configure-end

.. important:: 

   .. include:: ../../amperity_operator/source/models.rst
      :start-after: .. models-fields-used-by-all-models-start
      :end-before: .. models-fields-used-by-all-models-end

**To build a product affinity model**

.. model-product-affinity-configure-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - Open the **Customer 360** page, select a database, and then open the bottom--|fa-kebab|--menu and select **Predictive models**. This opens the **Predictive models page**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - Next to **Product affinity**, click **Add model**.

       Select the product group for which the product affinity model will be built, and then click **Continue**. This opens the **Predictive enablement** page for product affinity models.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - Use the **Customer exclusions** field to use fields in the **Customer Attributes** table to identify customers who have purchase patterns that should be excluded from product affinity modeling.

       For example, use cases for customer exclusions include:

       #. Ensuring that employees of your brand or resellers of products within your brand's product catalog are excluded.

       #. Excluding customers who do not have a contactable email address or contactable physical address from direct mail campaigns.

       .. note:: The list of fields in the **Customer Attributes** table that may be used for pCLV modeling are listed in the dropdown. Not all fields in the **Customer Attributes** table may be used with pCLV modeling.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - Use the **Additional features** field to add more fields from the **Unified Transactions** and **Unified Itemized Transactions** tables to the pCLV model.

       For each additional feature, the model results will include features for "first", "last", and "most common". For example, if **Product Category** is added, the pCLV model results will include features for **First Purchase Product Category**, **Last Purchase Product Category**, and **Most Common Product Category**.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - Configure values.

       Use the **Top N** field to define the number of distinct values the product affinity model will be trained on, based on popularity in the last year. For example, a value of "50" means the product affinity model will be trainined on the 50 most popular values for the specified product category by number of purchases in the past year. Default value: "50".

       Use the **Exclude these values** and **Include these values** fields to exclude or include specific values from the 50 most popular values. These entries are case-sensitive. For example: "purchase", "Purchase", and "PURCHASE" are three different values.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: center
          :class: no-scaled-link
     - Set product thresholds.

       Use the **Last 30 days purchaser holdout** field to set the number of unique purchasers that must exist within the last 30 days for a given product to appear in the audience size. Default value: "500".

       Use the **Last year purchaser** field to set the number of unique purchasers that must exist within the last year for predictions to appear for a given product attribute. Default value: "1000".


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: center
          :class: no-scaled-link
     - Define audience sizes. Each size is defined as a percentage of the total number of customers in the audience that are required to meet an individual audience size. The product affinity model will select which customers need to be in the audience so that it captures each threshold within the next 30 days. Default values: "0.5" (small), "0.7" (medium), and "0.9" (large).


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step 8.
          :align: center
          :class: no-scaled-link
     - Click **Start validation**.

.. model-product-affinity-configure-steps-end


.. _model-product-affinity-segments:

Use in segments
==================================================

.. model-product-affinity-segments-start

The following table describes the fields that are available when using product affinity modeling in segments.

.. model-product-affinity-segments-end

.. TODO: Need to bespoke this by fields for this specific modeling use case?

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-affinity-table-start
   :end-before: .. data-tables-affinity-table-end
