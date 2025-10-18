.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Churn propensity predicts each customer's likelihood to churn based on their purchase history with your brand.

.. meta::
    :content class=swiftype name=body data-type=text:
        Churn propensity predicts each customer's likelihood to churn based on their purchase history with your brand.

.. meta::
    :content class=swiftype name=title data-type=string:
        Churn propensity model

==================================================
Churn propensity model
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-churn-propensity-start
   :end-before: .. term-churn-propensity-end

.. tip:: 

   .. include:: ../../shared/terms.rst
      :start-after: .. term-preturn-start
      :end-before: .. term-preturn-end

.. model-churn-propensity-about-start

Amperity models churn propensity for each customer's unique purchase history. Some customers are seasonal shoppers, whereas other customers make monthly (or even weekly) purchases. Churn propensity modeling is based on each customer's individual p(return) score, which helps you build audiences that:

* Identify customers who are likely to churn
* Provide better insights about the root causes of customer churn to help you determine what will compel them to stay with right-timed messaging and relevant products
* Support a churn prevention campaign that contains a series of escalating win-back offers
* Optimize suppression and spend

By leveraging churn propensity modeling, you can take a proactive approach to customer retention, reduce churn rates, and improve overall customer satisfaction.

.. model-churn-propensity-about-end


.. _model-churn-propensity-use-cases:

Use cases
==================================================

.. model-churn-propensity-use-cases-start

The churn propensity model helps you build audiences to support churn prevention campaigns, including:

#. :ref:`Predicting which customers are likely to spend <model-churn-propensity-use-cases-spend>`
#. :ref:`Identifying each customer's churn lifecycle status <model-churn-propensity-use-cases-churn>`

.. model-churn-propensity-use-cases-end


.. _model-churn-propensity-use-cases-spend:

Which customers are likely to spend?
--------------------------------------------------

.. model-churn-propensity-use-cases-spend-start

The churn propensity model outputs a series of attributes that predict each customer purchase behavior in the coming year, including attributes for:

#. Average order revenue
#. Likelihood to spend
#. Order frequency
#. Total spend

Attributes that predict a customer's future purchase behavior are available from the **Predicted CLV Attributes** table:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Attribute Name
     - Description
   * - **Predicted Average Order Revenue Next 365d**
     - A customer's predicted average order revenue over the next 365 days.
   * - **Predicted CLV Next 365d**
     - The total predicted spend for a customer over the next 365 days.
   * - **Predicted Order Frequency Next 365d**
     - A customer's predicted number of orders over the next 365 days.
   * - **Predicted Probability of Transaction Next 365d**
     - The probability that a customer will purchase again in the next 365 days.

Use any combination of these attributes to build audiences that align to various stages within your churn prevention campaigns. You can access these attributes directly from the **Segment Editor**.

.. model-churn-propensity-use-cases-spend-end


.. _model-churn-propensity-use-cases-churn:

Which customers are likely to churn?
--------------------------------------------------

.. model-churn-propensity-use-cases-churn-start

The churn propensity model outputs a series of attributes that categorize your customers by:

#. Predicted lifecycle status, such as active, cooling down, at risk, and lost
#. Predicted lifetime value, such as top 1%, top 10%, and top 50%

Attributes that predict a customer's likelihood to churn, along with their predicted lifetime value, are available from the **Predicted CLV Attributes** table:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Attribute Name
     - Description
   * - **Predicted Customer Lifecycle Status**
     - A probabilistic grouping of a customer's likelihood to purchase again.

       .. include:: ../../shared/models.rst
          :start-after: .. models-churn-propensitity-tiers-repeat-start
          :end-before: .. models-churn-propensitity-tiers-repeat-end

       By grouping repeat customers into these tiers, you can:

       * Focus on retaining and nurturing customers who contribute to revenue.
       * Develop targeted campaigns that address the specific needs and preferences of different customer segments.
       * Proactively address the concerns of customers who may be considering churning.

       .. include:: ../../shared/models.rst
          :start-after: .. models-churn-propensitity-tiers-onetime-start
          :end-before: .. models-churn-propensitity-tiers-onetime-end

       By segmenting one-time buyers into different tiers, you can:

       * Create targeted messages and offers that resonate with specific groups of one-time buyers.
       * Analyze the characteristics of one-time buyers who have the highest potential to become repeat customers.
       * Offer personalized product suggestions based on a customer's initial purchase and tier.
       * Gain insights into the factors that influence one-time purchases and identify opportunities for improvement.

   * - **Predicted Customer Lifetime Value (pCLV) Tier**
     - A percentile grouping of customers by pCLV. Groupings include:

       * Platinum: top 1% of customers
       * Gold: top 1%-5% of customers
       * Silver: top 5%-10% of customers
       * Bronze: top 10%-25% of customers
       * Medium: top 25%-50% of customers
       * Low: bottom 50% of customers

       By grouping customers by pCLV percentiles, you can:

       * Identify and focus on customers who are predicted to generate the most revenue over their lifetime.
       * Develop targeted campaigns and offers that cater to the specific needs and preferences of different customer segments.
       * Allocate resources to focus on acquiring customers with high pCLV potential.
       * Implement strategies to retain and nurture high-value customers, maximizing their lifetime value.

By combining various customer attributes, you can create highly targeted churn prevention and one-time buyer campaigns that focus on your most valuable customers at the optimal time. You can access these attributes directly from the **Segment Editor**.

.. model-churn-propensity-use-cases-churn-end


.. _model-churn-propensity-configure:

Build a churn propensity model
==================================================

.. model-churn-propensity-configure-start

You can build a churn propensity model from the **Customer 360** page. Each database that is a "customer 360" database and contains the **Merged Customers**, **Unified Itemized Transactions**, and **Unified Transactions** tables may be configured for predictive modeling. You may use other tables in that database that are unique by Amperity ID to extend predictive models.

.. model-churn-propensity-configure-end

.. important:: 

   .. include:: ../../amperity_operator/source/models.rst
      :start-after: .. models-fields-used-by-all-models-start
      :end-before: .. models-fields-used-by-all-models-end

**To build a churn propensity model**

.. model-churn-propensity-configure-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Customer 360** page, select a database, and then open the bottom--|fa-kebab|--menu and select **Predictive models**. This opens the **Predictive models page**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Next to **Predicted customer lifetime value (pCLV)**, click **Add model**. This opens the **Predictive enablement** page for churn propensity models.

       .. note:: Churn propensity and predicted CLV are both outputs of the predicted customer lifetime value (pCLV) model. Fields that support both models are available to queries, segments, and campaigns from the **Predicted CLV Attributes** table.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Choose the model start date, which is the date from which the pCLV model starts tracking customer purchase behavior. You may choose a calendar date, such as specific date like January 1, 2020 or you may choose a relative date like "today - 4 years".

       A model that uses a calendar date will always use data from that date to the present day. Over time the time window used by the model will get longer. 

       A model that uses a relative date will always have a time window with a consistent length. Over time the time window used by the model will stay the same.

       .. note:: A relative date is determined at the time a model is run, where "now" is the date on which the model is run. The time window should be at least 3 years, but may be 4 or 5, depending on how much data is available to the model in Amperity.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Select the tables from which order-level and item-level data is made available to the model.

       For order-level data, select **Unified Transactions**. For item-level data, select **Unified Itemized Transactions**.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Use the **Prediction horizon** field to specify the number of days into the future for which you want pCLV modeling. The default value ("365") is fine for most use cases.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - Use the **Customer exclusions** field to use fields in the **Customer Attributes** table to identify customers who have purchase patterns that should be excluded from pCLV modeling.

       For example, use cases for customer exclusions include:

       #. Ensuring that employees of your brand or resellers of products within your brand's product catalog are excluded.

       #. Excluding customers who do not have a contactable email address or contactable physical address from direct mail campaigns.

       .. note:: The list of fields in the **Customer Attributes** table that may be used for pCLV modeling are listed in the dropdown. Not all fields in the **Customer Attributes** table may be used with pCLV modeling.


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step seven.
          :align: center
          :class: no-scaled-link
     - Use the **Additional features** field to add more fields from the **Unified Transactions** and **Unified Itemized Transactions** tables to the pCLV model.

       For each additional feature, the model results will include features for "first", "last", and "most common". For example, if **Product Category** is added, the pCLV model results will include features for **First Purchase Product Category**, **Last Purchase Product Category**, and **Most Common Product Category**.


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step eight.
          :align: center
          :class: no-scaled-link
     - Click **Start validation**.

.. model-churn-propensity-configure-steps-end


.. _model-churn-propensity-segments:

Use in segments
==================================================

.. model-churn-propensity-segments-start

The following table describes the fields that are available when using churn propensity modeling in segments.

.. model-churn-propensity-segments-end

.. TODO: Need to bespoke this by fields for this specific modeling use case?

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-predicted-clv-attributes-table-start
   :end-before: .. data-tables-predicted-clv-attributes-table-end


.. _model-churn-propensity-customize-lifecycle-status:

Customize lifecycle status
==================================================

.. TODO: This question came up in a Slack channel. And someone pointed to a tenant that uses the following SQL to define a custom date range for churn prevention.

.. model-churn-propensity-customize-lifecycle-status-start

The lifecycle status for the main churn propensity model cannot be customized. However, you can add a custom database table that references the churn propensity model. Use a **CASE** statement to apply custom durations and names that align to how your brand wants to measure churn prevention lifecycle status.

For example:

.. code-block:: sql
   :linenos:

   WITH overrides AS (
    SELECT
      CASE
        WHEN DATEDIFF(CURRENT_DATE, latest_order_datetime) <= 346 THEN 'Active'
        WHEN DATEDIFF(CURRENT_DATE, latest_order_datetime) <= 406 THEN 'Cooling Down'
        WHEN DATEDIFF(CURRENT_DATE, latest_order_datetime) <= 448 THEN 'At Risk'
        WHEN DATEDIFF(CURRENT_DATE, latest_order_datetime) <= 508 THEN 'Highly at Risk'
        WHEN DATEDIFF(CURRENT_DATE, latest_order_datetime) > 508 THEN 'Lost'
      END AS life_cycle
      ,latest_order_datetime AS one_and_done_transaction_datetime
      ,DATEDIFF(CURRENT_DATE, latest_order_datetime) AS days_since_order
      ,c.amperity_id
      ,country
    FROM Merged_Customers c
    JOIN Transaction_Attributes_Extended tae ON c.amperity_id = tae.amperity_id
    WHERE one_and_done
   )

   SELECT
     p.amperity_id
     ,p.predicted_probability_of_transaction_next_365d
     ,p.predicted_order_frequency_next_365d
     ,p.predicted_average_order_revenue_next_365d
     ,p.predicted_clv_next_365d
     ,p.predicted_customer_lifecycle_status
     ,p.predicted_customer_lifetime_value_tier
     ,c.life_cycle
     ,c.one_and_done_transaction_datetime
     ,c.days_since_order
     ,c.country
     ,COALESCE(
       c.life_cycle
       ,p.predicted_customer_lifecycle_status
     ) AS life_cycle_final
   FROM Predicted_CLV_Attributes AS p
   LEFT JOIN overrides c ON p.amperity_id = c.amperity_id

.. model-churn-propensity-customize-lifecycle-status-end
