.. 
.. https://docs.amperity.com/reference/
.. 


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

Use any combination of these attributes to build audiences that align to various stages within your churn prevention campaigns. You can access these attributes directly from the Segment Editor:

.. image:: ../../images/attribute-predicted-transactions.png
   :width: 600 px
   :alt: Choose the predicted probability of transactions attribute from the Segment Editor.
   :align: left
   :class: no-scaled-link

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

       * Focus on retaining and nurturing customers who contribute significantly to revenue.
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
       * Allocate resources more effectively by focusing on acquiring customers with high pCLV potential.
       * Implement strategies to retain and nurture high-value customers, maximizing their lifetime value.

By combining various customer attributes, you can create highly targeted churn prevention and one-time buyer campaigns that focus on your most valuable customers at the optimal time. You can access these attributes directly from the segment editor:

.. image:: ../../images/attribute-predicted-lifecycle-status.png
   :width: 600 px
   :alt: Choose the predicted lifecycle status attribute from the Segment Editor.
   :align: left
   :class: no-scaled-link

.. model-churn-propensity-use-cases-churn-end
