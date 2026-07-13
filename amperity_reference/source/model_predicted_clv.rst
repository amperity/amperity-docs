.. https://docs.amperity.com/reference/


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

.. model-predicted-clv-learning-lab-start

.. admonition:: Amperity Learning Lab

   Predicted CLV forecasts the total value of orders a customer will make in the next 365 days.

   Open **Learning Lab** to learn more about `predicted high value <https://amperity.com/learning-lab/predicted-high-value>`__ |ext_link|. Registration is required.

.. model-predicted-clv-learning-lab-end


.. _model-predicted-clv-use-cases:

Use cases
==================================================

.. model-predicted-clv-use-cases-start

The predicted CLV model helps you identify your highest value customers and the customers who are most likely to churn:

#. :ref:`How much will customers spend in the next year? <model-predicted-clv-use-cases-spend>`
#. :ref:`Which customers are your most valuable customers? <model-predicted-clv-use-cases-most-valuable>`
#. :ref:`Which customers are likely to churn? <model-predicted-clv-use-cases-churn>`

.. model-predicted-clv-use-cases-end


.. _model-predicted-clv-use-cases-spend:

How much will customers spend?
--------------------------------------------------

.. model-predicted-clv-use-cases-spend-start

The **Predicted CLV Next 365 Days** attribute in the **Predicted CLV Attributes** table has the total predicted customer spend over the next 365 days.

After you select this attribute you can specify the type of values you want to use for this audience, such as:

* Predicted CLV is greater than $100
* Predicted CLV is less than $400
* Predicted CLV is between $100 and $400

.. model-predicted-clv-use-cases-spend-end


.. _model-predicted-clv-use-cases-most-valuable:

Which customers are the most valuable?
--------------------------------------------------

.. include:: ../../amperity_user/source/usecase_predicted_top_10_percent.rst
   :start-after: .. usecase-predicted-top-10-percent-start
   :end-before: .. usecase-predicted-top-10-percent-end

.. include:: ../../amperity_user/source/usecase_predicted_top_10_percent.rst
   :start-after: .. usecase-predicted-top-10-percent-howitworks-start
   :end-before: .. usecase-predicted-top-10-percent-howitworks-end

.. include:: ../../amperity_user/source/usecase_predicted_top_10_percent.rst
   :start-after: .. usecase-predicted-top-10-percent-howitworks-callouts-start
   :end-before: .. usecase-predicted-top-10-percent-howitworks-callouts-end


.. _model-predicted-clv-use-cases-churn:

Which customers are likely to churn?
--------------------------------------------------

.. model-predicted-clv-use-cases-churn-start

Predicted CLV also powers churn and retention use cases. Each customer's predicted probability of transaction--also known as p(return)--and predicted customer lifecycle status let you identify customers who are likely to churn, so you can build audiences that:

* Identify customers who are likely to churn.
* Provide insight into the root causes of churn to help you determine what will compel customers to stay with right-timed messaging and relevant products.
* Support a churn prevention campaign that has a series of escalating win-back offers.
* Optimize suppression and spend.

The **Predicted Customer Lifecycle Status** attribute in the **Predicted CLV Attributes** table groups customers by their likelihood to purchase again:

.. include:: ../../shared/models.rst
   :start-after: .. models-churn-propensitity-tiers-repeat-start
   :end-before: .. models-churn-propensitity-tiers-repeat-end

.. include:: ../../shared/models.rst
   :start-after: .. models-churn-propensitity-tiers-onetime-start
   :end-before: .. models-churn-propensitity-tiers-onetime-end

Combine lifecycle status with predicted value tiers to build highly targeted churn-prevention and retention campaigns that focus on your most valuable customers at the optimal time.

.. model-predicted-clv-use-cases-churn-end
