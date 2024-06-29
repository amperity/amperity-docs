.. 
.. https://docs.amperity.com/reference/
.. 


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

Amperity models predicted CLV by comparing what customers spent in the previous year to their predicted spend in the coming year, and then determines for each customer their:

#. Predicted probability of purchase
#. Predicted number of orders
#. Predicted average order value

Use predicted CLV modeling to build high-value audiences that identify:

* Which customers have the highest predicted value?
* Which customers will respond better to special offers and perks?
* What are the best personalized experiences for your best customers?
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

The **Predicted CLV Next 365d** attribute in the **Predicted CLV Attributes** table contains the total predicted customer spend over the next 365 days. You can access this attribute directly from the segment editor:

.. image:: ../../images/attribute-predicted-clv.png
   :width: 600 px
   :alt: Choose the predicted CLV attribute from the Segment Editor.
   :align: left
   :class: no-scaled-link

After you select this attribute you can specify the type of values you want to use for this audience, such as:

* Predicted value is greater than $100
* Predicted value is less than $400
* Predicted value is between $100 and $400

.. model-predicted-clv-use-cases-spend-end


.. _model-predicted-clv-use-cases-most-valuable:

Which customers are the most valuable?
--------------------------------------------------

.. include:: ../../amperity_ampiq/source/usecase_predicted_top_10_percent.rst
   :start-after: .. usecase-predicted-top-10-percent-start
   :end-before: .. usecase-predicted-top-10-percent-end

.. include:: ../../amperity_ampiq/source/usecase_predicted_top_10_percent.rst
   :start-after: .. usecase-predicted-top-10-percent-howitworks-start
   :end-before: .. usecase-predicted-top-10-percent-howitworks-end

.. include:: ../../amperity_ampiq/source/usecase_predicted_top_10_percent.rst
   :start-after: .. usecase-predicted-top-10-percent-howitworks-callouts-start
   :end-before: .. usecase-predicted-top-10-percent-howitworks-callouts-end
