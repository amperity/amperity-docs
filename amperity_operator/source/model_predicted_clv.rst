.. https://docs.amperity.com/operator/



.. meta::
    :description lang=en:
        Customer lifetime value (CLV) predicts what your customers will spend in the next year using predicted probability of purchase, predicted number of orders, and predicted order value.

.. meta::
    :content class=swiftype name=body data-type=text:
        Customer lifetime value (CLV) predicts what your customers will spend in the next year using predicted probability of purchase, predicted number of orders, and predicted order value.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predicted CLV model

==================================================
Predicted CLV model
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pclv-start
   :end-before: .. term-pclv-end

.. model-predicted-clv-about-start

Amperity models predicted customer lifetime value (CLV) by comparing what customers spent in the previous year to their predicted spend in the coming year, and then predicts for each customer their:

#. Probability of purchase
#. Number of orders
#. Average order value

You can use predicted CLV modeling to build high-value audiences that identify:

* Which customers have the highest predicted value?
* Which customers will respond better to special offers and perks?
* What are the best personalized experiences for your top customers, such as personalized rewards, offers, and content?
* Which customers have individual price preferences?

.. model-predicted-clv-about-end


.. _model-predicted-clv-use-cases:

Use cases
==================================================

.. model-predicted-clv-use-cases-start

The predicted CLV model helps you identify your highest value customers by year or by value tier:

#. :ref:`How much will customers spend in the next year? <model-predicted-clv-use-cases-spend>`
#. :ref:`Which customers are your most valuable customers? <model-predicted-clv-use-cases-most-valuable>`

.. model-predicted-clv-use-cases-end


.. _model-predicted-clv-use-cases-spend:

How much will customers spend?
--------------------------------------------------

.. model-predicted-clv-use-cases-spend-start

The **Predicted CLV Next 365d** attribute in the **Predicted CLV Attributes** table contains the total predicted customer spend over the next 365 days. You can access this attribute directly from the **Segment Editor**.

After you select this attribute you can specify the type of values you want to use for this audience, such as:

* Predicted CLV is greater than $100
* Predicted CLV is less than $400
* Predicted CLV is between $100 and $400

.. model-predicted-clv-use-cases-spend-end


.. _model-predicted-clv-use-cases-most-valuable:

Which customers are the most valuable?
--------------------------------------------------

.. TODO: Reset this to include from ampiq/usecase_predicted_top_10_percent

.. usecase-predicted-top-10-percent-start

When predictive modeling is enabled for your tenant you can use output from the |predicted customer lifetime value (CLV) model|, which helps you identify your highest value customers by value tier. Each tier represents a percentile grouping of customers by predicted value:

* Platinum represents the top 1%
* Gold represents customers who fall between 1% and 5%
* Silver represents customers who fall between 5% and 10%

Select all three of these predicted value tiers to build an audience that contains customers who are predicted to be in your top 10% (inclusive) high value customers.

.. usecase-predicted-top-10-percent-end

.. usecase-predicted-top-10-percent-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that returns customers who are predicted to be your top 10% highest value customers.

.. usecase-predicted-top-10-percent-howitworks-end

**WHICH CUSTOMERS ARE PREDICTED TO BE YOUR TOP 10%?**

.. usecase-predicted-top-10-percent-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: left
          :class: no-scaled-link

     - Open the **Segment Editor**, look in the lower-right of the page and make sure your customer 360 database is selected.

       .. image:: ../../images/mockup-segments-tab-database-and-tables-small.png
          :width: 350 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt:   Return a list of the customers with a predicted platinum, gold, or silver value.
          :align: left
          :class: no-scaled-link

     - The first step is to identify customers whose predicted customer lifetime value is platinum, gold, or silver. Choose the **Predicted Customer Lifetime Value Tier** attribute from the **Predicted CLV Attributes** table, select the "is in list" operator, and then select "Platinum", "Gold", *and* "Silver" from the list:

       .. image:: ../../images/usecases-predicted-value-tier-is-in-list.png
          :width: 540 px
          :alt: Find customers with a predicted platinum, gold, or silver value.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them should belong to a future campaign.
	   
   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Return a list of customers for whom your brand has email addresses.
          :align: left
          :class: no-scaled-link

     - The next step is to identify customers with contactable email address in their customer profiles. Choose the **Contactable Email** attribute from the **Customer Attributes** table, and then select the "is true" operator:

       .. image:: ../../images/attribute-contactable-email-true.png
          :width: 540 px
          :alt: Find customers for whom your brand has email addresses.
          :align: left
          :class: no-scaled-link

       Keep the and/or slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to view updated values for the combination of customers who have a predicted platinum, gold, or silver *and* a contactable email address.

       .. tip:: Use the **Is Opted Into Email** attribute from the **Customer Attributes** table to include only customers who are opted into receiving email messages from your brand.

          .. image:: ../../images/usecase-generic-email-optin.png
             :width: 540 px
             :alt: Find customers for whom your brand has an opted-in email address.
             :align: left
             :class: no-scaled-link

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Send customer list to your favorite email marketing tool.
          :align: left
          :class: no-scaled-link

     - Send this list of customers to your favorite email marketing tool (i.e. Attentive) on the **Campaigns** page.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Save your segment.
          :align: left
          :class: no-scaled-link
     - You're done building your audience! Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "Predicted Top 10% High Value Customers"

       .. image:: ../../images/usecases-dialog-save-top-10-high-value-customers.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions and want to build segments that are brand- and/or region-specific.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Segment insights page
          :align: left
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-predicted-top-10-percent-howitworks-callouts-end


.. _model-predicted-clv-configure:

Build a predicted CLV model
==================================================

.. model-predicted-clv-configure-start

You can build a predicted CLV model from the **Customer 360** page. Each database that is a "customer 360" database and contains the **Merged Customers**, **Unified Itemized Transactions**, and **Unified Transactions** tables may be configured for predictive modeling. You may use other tables in that database that are unique by Amperity ID to extend predictive models.

.. model-predicted-clv-configure-end

.. important:: 

   .. include:: ../../amperity_operator/source/models.rst
      :start-after: .. models-fields-used-by-all-models-start
      :end-before: .. models-fields-used-by-all-models-end

**To build a predicted CLV model**

.. model-predicted-clv-configure-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Customer 360** page, select a database, and then open the bottom (|fa-kebab|) menu and select **Predictive models**. This opens the **Predictive models page**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Next to **Predicted customer lifetime value (pCLV)**, click **Add model**. This opens the **Predictive enablement** page for predicted CLV models.

       .. note:: Churn propensity and predicted CLV are both outputs of the predicted customer lifetime value (pCLV) model. Fields that support both models are available to queries, segments, and campaigns from the **Predicted CLV Attributes** table.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Choose the model start date, which is the date from which the pCLV model starts tracking customer purchase behavior. You may choose a calendar date, such as specific date like January 1st, 2020 or you may choose a relative date like "today - 4 years".

       A model that uses a calendar date will always use data from that date to the present day. Over time the time window used by the model will get longer. 

       A model that uses a relative date will always have a time window with a consistent length. Over time the time window used by the model will stay the same.

       .. note:: A relative date is determined at the time a model is run, where "now" is the date on which the model is run. The time window should be at least 3 years, but may be 4 or 5, depending on how much data is available to the model in Amperity.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Select the tables from which order- and item-level data is made available to the model.

       For order-level data, select **Unified Transactions**. For item-level data, select **Unified Itemized Transactions**.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - Use the **Prediction horizon** field to specify the number of days into the future for which you want pCLV modeling. The default value ("365") is fine for most use cases.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link
     - Use the **Customer exclusions** field to use fields in the **Customer Attributes** table to identify customers who have purchase patterns that should be excluded from pCLV modeling.

       For example, use cases for customer exclusions include:

       #. Ensuring that employees of your brand or resellers of products within your brand's product catalog are excluded.

       #. Excluding customers who do not have a contactable email address or contactable physical address from direct mail campaigns.

       .. note:: The list of fields in the **Customer Attributes** table that may be used for pCLV modeling are listed in the dropdown. Not all fields in the **Customer Attributes** table may be used with pCLV modeling.


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link
     - Use the **Additional features** field to add more fields from the **Unified Transactions** and **Unified Itemized Transactions** tables to the pCLV model.

       For each additional feature, the model results will include features for "first", "last", and "most common". For example, if **Product Category** is added, the pCLV model results will include features for **First Purchase Product Category**, **Last Purchase Product Category**, and **Most Common Product Category**.


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step 8.
          :align: left
          :class: no-scaled-link
     - Click **Start validation**.

.. model-predicted-clv-configure-steps-end


.. _model-predicted-clv-segments:

Use in segments
==================================================

.. model-predicted-clv-segments-start

The following table describes the fields that are available when using predicted customer lifetime value (CLV) modeling in segments.

.. model-predicted-clv-segments-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-predicted-clv-attributes-table-start
   :end-before: .. data-tables-predicted-clv-attributes-table-end

