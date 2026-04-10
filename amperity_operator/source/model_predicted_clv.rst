.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        The predicted customer lifetime value (pCLV) model predicts expected revenue, likelihood of purchasing, and customer value using three independently trained machine learning models: a return classifier, an order frequency regressor, and an average order value regressor.

.. meta::
    :content class=swiftype name=body data-type=text:
        The predicted customer lifetime value (pCLV) model predicts expected revenue, likelihood of purchasing, and customer value using three independently trained machine learning models: a return classifier, an order frequency regressor, and an average order value regressor.

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

The Amperity pCLV model predicts the expected revenue for each customer, likelihood of purchasing, and their value relative to other customers over a future time window (the "prediction horizon," typically the next 365 days). Rather than relying on a single model for this complex prediction, pCLV breaks the problem into three simpler, independently trained machine learning models that are then combined to produce the final prediction.

A customer's future value is a function of three questions:

#. **Will they come back?** The Return Classifier predicts the probability that a customer will make at least one purchase during the prediction horizon.
#. **How often will they buy?** The Order Frequency Regressor predicts how many orders a returning customer will place during the prediction horizon.
#. **How much will they spend per order?** The Average Order Value Regressor predicts the average revenue per order for the customer.

These three models are combined with a simple formula:

.. code-block:: none

   Predicted CLV = P(return) x Predicted Order Frequency x Predicted Avg Order Value

You can use predicted CLV modeling to build high-value audiences that identify:

* Which customers have the highest predicted value?
* Which customers are better candidates for winback offers?
* Which customers are candidates for cultivating customer value?

.. model-predicted-clv-about-end


.. _model-predicted-clv-how-it-works:

How the model works
==================================================

.. model-predicted-clv-how-it-works-start

The pCLV model is an ensemble of three independently trained machine learning models. Each model contributes independently to the final prediction.

.. model-predicted-clv-how-it-works-end


.. _model-predicted-clv-return-classifier:

Return Classifier
--------------------------------------------------

.. model-predicted-clv-return-classifier-start

The Return Classifier predicts the probability that a customer will make at least one purchase during the prediction horizon. This is a binary classification problem (return vs. not return), and the model outputs a probability between 0 and 1.

Customers with a very low return probability will naturally have a low predicted CLV regardless of the other factors.

.. model-predicted-clv-return-classifier-end


.. _model-predicted-clv-order-frequency:

Order Frequency Regressor
--------------------------------------------------

.. model-predicted-clv-order-frequency-start

The Order Frequency Regressor predicts how many orders a returning customer will place during the prediction horizon. This is a regression problem that outputs a continuous number (e.g., 3.2 orders).

.. model-predicted-clv-order-frequency-end


.. _model-predicted-clv-avg-order-value:

Average Order Value Regressor
--------------------------------------------------

.. model-predicted-clv-avg-order-value-start

The Average Order Value Regressor predicts the average revenue per order for the customer. This is a regression that outputs a dollar amount (e.g., $85.40).

.. model-predicted-clv-avg-order-value-end


.. _model-predicted-clv-ensemble:

The ensemble
--------------------------------------------------

.. model-predicted-clv-ensemble-start

The three models are combined with a multiplicative ensemble:

.. code-block:: none

   Predicted CLV = P(return) x Predicted Order Frequency x Predicted Avg Order Value

A customer with a high probability of return but low order frequency and modest order value will have a moderate CLV, while a customer who is likely to return frequently and spend heavily will have a high CLV.

After the raw CLV is computed, a sigmoid rescaling step compresses extreme outlier predictions to produce a smoother distribution of values.

.. model-predicted-clv-ensemble-end


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

The **Predicted CLV Next 365 Days** attribute in the **Predicted CLV Attributes** table contains the total predicted customer spend over the next 365 days. You can access this attribute directly from the **Segment Editor**.

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

**Which customers are predicted to be in your top ten percent?**

.. usecase-predicted-top-10-percent-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
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
          :align: center
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
          :align: center
          :class: no-scaled-link

     - The next step is to identify customers with contactable email address in their customer profiles. Choose the **Contactable Email** attribute from the **Customer Attributes** table, and then select the "is true" operator:

       .. image:: ../../images/attribute-contactable-email-true.png
          :width: 540 px
          :alt: Find customers for whom your brand has email addresses.
          :align: left
          :class: no-scaled-link

       Keep the slider set to **AND**.

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
          :align: center
          :class: no-scaled-link

     - Send this list of customers to your favorite email marketing tool, such as Attentive or Braze, on the **Campaigns** page.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You are done building your audience. Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that describes the purpose and audience type for the segment. For example: "Predicted Top 10% High Value Customers"

       .. image:: ../../images/usecases-dialog-save-top-10-high-value-customers.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Be sure to include the brand name or the region name if you have multiple brands or have multiple regions and want to build segments that are brand- or region-specific.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-predicted-top-10-percent-howitworks-callouts-end


.. _model-predicted-clv-configure:

Build a predicted CLV model
==================================================

.. model-predicted-clv-configure-start

You can build a predicted CLV model from the **Customer 360** page. Each database that contains the **Merged Customers**, **Unified Itemized Transactions**, and **Unified Transactions** tables may be configured for predictive modeling. Only one pCLV model is allowed per database.

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
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Customer 360** page, select a database, and then open the bottom--|fa-kebab|--menu and select **Predictive models**. This opens the **Predictive models** page.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Click **Add model** and select **pCLV**. The system validates that the required tables exist in your database (**Merged Customers**, **Unified Transactions**, and **Unified Itemized Transactions**).

       .. note:: Churn propensity and predicted CLV are both outputs of the predicted customer lifetime value (pCLV) model. Fields that support both models are available to queries, segments, and campaigns from the **Predicted CLV Attributes** table.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Enter a **name** for the model, an optional **description**, and select a **prediction horizon**. The prediction horizon specifies how far into the future the model predicts. Options include 90 days, 180 days, and 365 days. The default value (365 days) is fine for most use cases.

       Click **Create** to create the model.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Create and evaluate model versions. Each version contains the model's hyperparameters, lookback window (default 4 years), customer exclusions, and additional features.

       Evaluate a version to run a validation job. Review the validation results, which include metrics such as MAE, Spearman's Rank Correlation, Brier Score, and F1 Score.

       .. tip:: You can create multiple versions with different settings and compare their evaluation results to find the best-performing version for your data.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - When you are satisfied with a version's performance, click **Activate**. During activation:

       #. Select a **courier group**. The model must be attached to a courier group to activate.
       #. Select a **version** to activate. It is recommended that you select the best performing version for your use cases. 
       #. Set the **training cadence**, which is how often the model is retrained with new data. The default is every 2 weeks.
       #. Set the **inference cadence**, which is how often predictions are generated. The default is daily.

       Click **Activate** to start a full workflow that trains the model, runs inference, and adds the model output tables to the database.

.. model-predicted-clv-configure-steps-end


.. _model-predicted-clv-output-tables:

Output tables
==================================================

.. model-predicted-clv-output-tables-start

When a pCLV model is activated, a training and inference will begin. When complete, the generated **Predicted CLV Attributes** table (one row per customer) will be automatically added to the database.

.. note:: Field names shown below use "365d" as the default prediction horizon. If you configure a different horizon (e.g., 180 days), the field descriptions in the database view will reflect your configured value, though the underlying column names remain consistent.

.. model-predicted-clv-output-tables-end

.. model-predicted-clv-output-tables-table-start

.. list-table::
   :widths: 30 10 15 45
   :header-rows: 1

   * - Field
     - Type
     - Source
     - Description
   * - **amperity_id**
     - String
     - Identity resolution
     - Unique customer identifier.
   * - **predicted_probability_of_transaction_next_365d**
     - Float
     - Return Classifier
     - Probability (0-1) that this customer will make at least one purchase in the prediction horizon.
   * - **predicted_order_frequency_next_365d**
     - Float
     - Order Frequency Regressor
     - Predicted number of orders the customer will place in the prediction horizon.
   * - **predicted_average_order_revenue_next_365d**
     - Float
     - Avg Order Value Regressor
     - Predicted average revenue per order in the prediction horizon.
   * - **predicted_clv_next_365d**
     - Float
     - Ensemble
     - Final predicted customer lifetime value (the product of the three model outputs, after rescaling).
   * - **historical_order_frequency_lifetime**
     - Integer
     - Historical feature
     - Total number of orders the customer has placed historically.
   * - **days_since_last_order**
     - Integer
     - Historical feature
     - Number of days since the customer's most recent order.
   * - **predicted_customer_lifecycle_status**
     - String
     - Post-processing
     - Customer lifecycle segment: Lost, Highly at risk, At risk, Cooling down, or Active.
   * - **predicted_customer_lifetime_value_tier**
     - String
     - Post-processing
     - Value tier based on CLV percentile: Low, Medium, Bronze, Silver, Gold, or Platinum.

.. model-predicted-clv-output-tables-table-end


.. _model-predicted-clv-export-validation:

Export validation results
==================================================

.. model-predicted-clv-export-validation-start

After running a model validation, you can export the results to Databricks, Snowflake, or Google BigQuery. Create an outbound bridge, then select the **predictive_tables** dataset.

.. note:: Only the most recent validation run for each model version can be exported.

The dataset contains the actual customer spend and churn status for all customers in the holdout dataset and the scores from the model and comparison baseline. The format of the table is:

.. model-predicted-clv-export-validation-end

.. model-predicted-clv-export-validation-table-start

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Column name
     - Description
   * - **amperity_id**
     - The unique customer identifier.
   * - **predicted_probability_of_transaction_next_365d**
     - The predicted likelihood (0-1) of a customer transacting in the prediction horizon.
   * - **predicted_order_frequency_next_365d**
     - Assuming a customer will transact, the predicted number of orders they will make in the prediction horizon.
   * - **predicted_average_order_revenue_next_365d**
     - Assuming a customer will transact, the predicted average value per order for any orders in the prediction horizon.
   * - **predicted_clv_next_365d**
     - The total predicted spend over the prediction horizon, calculated as predicted_probability_of_transaction_next_365d * predicted_order_frequency_next_365d * predicted_average_order_revenue_next_365d.
   * - **historical_order_frequency_lifetime**
     - The customer's lifetime number of orders as of the start of the evaluation window.
   * - **days_since_last_order**
     - The days since the customer's last order, as of the start of the evaluation window.
   * - **naive_predicted_clv_next_365d**
     - The total expected spend over the prediction horizon, using the naive baseline. The baseline carries forward a customer's spend during the preceding period equal to the prediction horizon and assumes they will do the same in the prediction horizon.
   * - **predicted_customer_lifecycle_status**
     - Customer lifecycle segment: Lost, Highly at risk, At risk, Cooling down, or Active.
   * - **predicted_customer_lifetime_value_tier**
     - Value tier based on CLV percentile: Low, Medium, Bronze, Silver, Gold, or Platinum.
   * - **_actual_returned**
     - The customer's actual transaction status in the evaluation window. 1 for return, 0 for churn.
   * - **_actual_order_freq**
     - The customer's actual order amount in the evaluation window.
   * - **_actual_average_order_value**
     - The customer's actual average order value in the evaluation window.
   * - **_actual_clv**
     - The customer's actual spend in the evaluation window.

.. model-predicted-clv-export-validation-table-end


.. _model-predicted-clv-validation-metrics:

Validation metrics
==================================================

.. model-predicted-clv-validation-metrics-start

The following metrics are available after running a model validation:

.. model-predicted-clv-validation-metrics-end

.. model-predicted-clv-validation-metrics-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Metric
     - Description
   * - **Churn Baseline**
     - The number of days without a purchase after which a customer is considered "churned" for validation purposes. Default: 90 days.
   * - **MAE (Mean Absolute Error)**
     - Average dollar difference between predicted and actual CLV. Lower is better.
   * - **Spearman's Rank Correlation**
     - Measures how well the model ranks customers from highest to lowest value, regardless of exact dollar accuracy. Ranges from -1 to 1; higher is better.
   * - **Brier Score**
     - Measures calibration of the churn/return probability predictions. Ranges from 0 to 1; lower is better.
   * - **F1 Score**
     - Harmonic mean of precision and recall for the return classifier. Higher is better.

.. model-predicted-clv-validation-metrics-table-end


.. _model-predicted-clv-advanced-settings:

Advanced settings
==================================================

.. model-predicted-clv-advanced-settings-start

The following settings appear on the **Advanced** tab and apply across all three sub-models.

.. model-predicted-clv-advanced-settings-end

.. model-predicted-clv-advanced-settings-table-start

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - **Max Train Size**
     - 50,000,000
     - Limits how many customer records are used to train the model. Larger datasets are downsampled to this limit.
   * - **Balance Labels**
     - true
     - Whether to balance the training data by downsampling the majority class and upsampling the minority class for the return classifier.
   * - **Filter Outliers**
     - false
     - Whether customers flagged as outliers (above the 99.5th percentile on lifetime order value, average order value, or order frequency) are excluded from training. When false, they are flagged but still included.
   * - **Customer Exclusions**
     - is_outlier, is_test_account
     - Boolean fields from the customer attributes table used to exclude specific customers from training.

.. model-predicted-clv-advanced-settings-table-end


.. _model-predicted-clv-hyperparameters:

Hyperparameters
==================================================

.. model-predicted-clv-hyperparameters-start

Each of the three sub-models (Return Classifier, Order Frequency Regressor, Avg Order Value Regressor) can independently select a model type and tune its hyperparameters. These settings appear in the **Advanced** tab under expandable sections for each sub-model.

.. model-predicted-clv-hyperparameters-end


.. _model-predicted-clv-hyperparameters-random-forest:

Random Forest (recommended)
--------------------------------------------------

.. model-predicted-clv-hyperparameters-rf-start

The default model type. Builds many independent decision trees and averages their predictions.

.. list-table::
   :widths: 25 15 15 45
   :header-rows: 1

   * - Parameter
     - Default
     - Range
     - Description
   * - **Max Depth**
     - 10
     - 1-30
     - Maximum depth of each decision tree. Deeper trees capture more complex patterns but risk overfitting.
   * - **Num Trees**
     - 100
     - 1-500
     - Number of trees in the forest. More trees generally improve accuracy at the cost of computation time.
   * - **Max Bins**
     - 102
     - 2-256
     - Number of bins used to discretize continuous features.
   * - **Feature Subset Strategy**
     - auto
     - auto, all, sqrt, onethird, log2
     - How many features to consider at each split.
   * - **Impurity**
     - gini (classifier) / variance (regressors)
     - gini, entropy (classifier) / variance (regressors)
     - The metric used to evaluate splits.

.. model-predicted-clv-hyperparameters-rf-end


.. _model-predicted-clv-hyperparameters-gbt:

Gradient Boosted Trees
--------------------------------------------------

.. model-predicted-clv-hyperparameters-gbt-start

Builds trees sequentially, with each new tree correcting the errors of the previous ones. Can be more powerful than Random Forest but more sensitive to tuning.

.. list-table::
   :widths: 25 15 15 45
   :header-rows: 1

   * - Parameter
     - Default
     - Range
     - Description
   * - **Max Depth**
     - 10
     - 1-30
     - Maximum depth of each decision tree.
   * - **Max Iterations**
     - 100
     - 1-500
     - Number of boosting rounds (trees built sequentially). More iterations can improve accuracy but risk overfitting.
   * - **Step Size**
     - 0.1
     - 0.01-1.0
     - Learning rate. Smaller values require more iterations but tend to generalize better.
   * - **Max Bins**
     - 102
     - 2-256
     - Number of bins used to discretize continuous features.
   * - **Loss Type**
     - logistic (classifier) / squared (regressors)
     - logistic, squared, absolute (classifier) / squared, absolute (regressors)
     - The loss function the model optimizes.

.. model-predicted-clv-hyperparameters-gbt-end


.. _model-predicted-clv-hyperparameters-logistic-regression:

Logistic Regression
--------------------------------------------------

.. model-predicted-clv-hyperparameters-lr-start

A classification model that predicts probabilities by fitting a linear decision boundary through a sigmoid function. Faster to train than tree-based methods and more interpretable, but less able to capture complex nonlinear patterns.

.. note:: Logistic Regression is only applicable to the Return Classifier (probability of purchase) and is not used for the regression sub-models.

.. list-table::
   :widths: 25 15 15 45
   :header-rows: 1

   * - Parameter
     - Default
     - Range
     - Description
   * - **Max Iterations**
     - 100
     - 1-1000
     - Maximum number of optimization iterations.
   * - **Regularization**
     - 0.0
     - 0.0+
     - Strength of regularization penalty. Higher values reduce overfitting.
   * - **Elastic Net Param**
     - 0.0
     - 0.0-1.0
     - Balance between L1 (lasso) and L2 (ridge) regularization. 0.0 = pure L2, 1.0 = pure L1.

.. model-predicted-clv-hyperparameters-lr-end


.. _model-predicted-clv-example-features:

Example features
==================================================

.. model-predicted-clv-example-features-start

The pCLV models include 200+ input features generated from input data that have been derived and refined from years of pCLV modeling. Example features include:

* lifetime_order_frequency
* lifetime_order_recency
* days_since_latest_order
* days_since_first_order
* lifetime_order_total_amount
* lifetime_average_order_value
* lifetime_largest_order_value
* l{12m,6m,3m,30d}_order_frequency
* l{12m,6m,3m,30d}_average_order_value
* l{12m,6m,3m,30d}_order_total_amount
* num_holiday_orders
* total_holiday_order_amount

.. model-predicted-clv-example-features-end


.. _model-predicted-clv-segments:

Use in segments
==================================================

.. model-predicted-clv-segments-start

The following table describes the fields that are available when using predicted customer lifetime value (CLV) modeling in segments.

.. model-predicted-clv-segments-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-predicted-clv-attributes-table-start
   :end-before: .. data-tables-predicted-clv-attributes-table-end

