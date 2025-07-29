.. https://docs.amperity.com/user/


.. meta::
    :description lang=en:
        An RFM score is an approximation that measures individual scores for recency, frequency, and monetary, along with a combined score.

.. meta::
    :content class=swiftype name=body data-type=text:
        An RFM score is an approximation that measures individual scores for recency, frequency, and monetary, along with a combined score.

.. meta::
    :content class=swiftype name=title data-type=string:
        Recency, frequency, monetary

==================================================
Recency, frequency, monetary
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-rfm-start
   :end-before: .. term-rfm-end


.. _rfm-scores:

RFM scores
==================================================

.. rfm-scores-start

RFM scores are available as out-of-the-box attributes in Amperity standard output. These attributes -- **L12M Recency**, **L12M Frequency**, and **L12M Monetary** -- can be found in the **Transaction Attributes Extended** table and are built from historical data for the previous 12 months. Use the scores in these attributes to quickly build useful audiences around how much your customers spend, how often they purchase, and how recently they purchase.

.. rfm-scores-end

.. rfm-scores-note-start

.. note:: RFM scores, because they are historically-based and only cover a rolling 1-year window, are generally less accurate than :doc:`(p)CLV attributes <model_predicted_clv>`, which is available when you enable Amperity predictive analytics in your tenant. (p)CLV attributes provide better answers than RFM scores for the following questions: "How much will customers spend in the next year?" and "Which customers are your most valuable customers?"

.. rfm-scores-note-end


.. _rfm-percentiles:

RFM percentiles
==================================================

.. attribute-rfm-scoring-start

Each RFM score is split into ten percentile groups. The lowest percentile is 1 and the highest percentile is 10. Each percentile represents 10% of the customers who belong to that segment.

* 10 represents the 90-100th percentile and the customers who have the highest recency, frequency, or monetary scores.
* 9 represents the 80-90th percentile
* 8 represents the 70-80th percentile
* 7 represents the 60-70th percentile
* 6 represents the 50-60th percentile
* 5 represents the 40-50th percentile
* 4 represents the 30-40th percentile
* 3 represents the 20-30th percentile
* 2 represents the 10-20th percentile
* 1 represents the 0-10th percentile and the customers who have the lowest recency, frequency, or monetary scores.

.. tip:: Combine percentiles to build larger groups of customers. For example 9 and 10 together represent the "top 20%" while 8, 9, and 10 represent the "top 30%".

.. attribute-rfm-scoring-end


.. _rfm-example-top-20-revenue:

Example: Top 20% revenue during the previous year
==================================================

.. include:: ../../amperity_user/source/usecase_customers_top20_revenue.rst
   :start-after: .. usecase-customers-top-20-revenue-start
   :end-before: .. usecase-customers-top-20-revenue-end

.. include:: ../../amperity_user/source/usecase_customers_top20_revenue.rst
   :start-after: .. usecase-customers-top-20-revenue-howitworks-start
   :end-before: .. usecase-customers-top-20-revenue-howitworks-end

.. include:: ../../amperity_user/source/usecase_customers_top20_revenue.rst
   :start-after: .. usecase-customers-top-20-revenue-howitworks-callouts-start
   :end-before: .. usecase-customers-top-20-revenue-callouts-end

.. rfm-example-top-20-revenue-extend-start

.. admonition:: Can you combine RFM attributes?

   Yes. For example, you can extend the top 20% revenue list to also include customers who are in your top-30 percent for purchase frequency.

   Click **+ Add Attribute**, choose the **L12M Frequency** attribute from the **Transaction Attributes Extended** table, select the "is in list" operator, and then select "8", "9", and "10":

   .. image:: ../../images/attribute-rfm-monetary-frequency-top-20.png
      :width: 540 px
      :alt: Who are your top 20-percent customers for revenue and purchase frequency in the previous year?
      :align: left
      :class: no-scaled-link

.. rfm-example-top-20-revenue-extend-end


.. _rfm-percentiles-combined-scores:

How combined RFM scores work
==================================================

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-score-howitworks-start
   :end-before: .. attribute-rfm-score-howitworks-end


.. _rfm-more-examples:

More scenarios
==================================================

.. rfm-more-examples-start

The following sections don't walk through how to configure attributes in the **Segment Editor**, but they do describe situations in which using RFM scores can help you build useful audiences for your campaigns.

* :ref:`Direct mail campaigns <rfm-example-direct-mail>`
* :ref:`High F, low R scores <rfm-example-high-m-low-r>`
* :ref:`High M, low F scores <rfm-example-high-m-low-f>`
* :ref:`High R, low F and M scores <rfm-example-high-r-low-f-m>`
* :ref:`High R and F, low M scores <rfm-example-high-r-and-f-low-m>`

.. rfm-more-examples-end


.. _rfm-example-direct-mail:

Direct mail campaigns
--------------------------------------------------

.. rfm-example-direct-mail-start

RFM scores were originally designed to support direct mail campaigns in the pre-digital age. RFM metrics can help you identify future customer behavior. A customer who has purchased recently is more likely to purchase again. A customer who has visited your website (and interacted with your brand) is more likely to visit again. A customer who spends a lot of money is more likely to keep spending a lot of money.

Direct mail provides a physical touchpoint that can help you make a positive impression on your customers. Many direct-to-consumer companies prefer direct mail campaigns because there are more formats and approaches that you can use to accurately represent your brand.

With the right audiences targeted correctly, you can use RFM analysis to help your direct mail campaign stand out in the age of pervasive digital advertising and overflowing email inboxes.

Use RFM scores to identify households that are more likely to be receptive to the messages you want to include in your direct mail campaigns.

.. rfm-example-direct-mail-end


.. _rfm-example-high-m-low-r:

High F, low R scores
--------------------------------------------------

.. rfm-example-high-m-low-r-start

A high frequency score and low recency score represents a customer who has recently stopped buying from your brand. Use this combination of scores as an indicator for customers who may require special offers to entice them back to spending money with your brand.

.. rfm-example-high-m-low-r-end


.. _rfm-example-high-m-low-f:

High M, low F scores
--------------------------------------------------

.. rfm-example-high-m-low-f-start

A high monetary score and low frequency score represents a customer who spends a lot of money, but shops infrequently.

For example, a customer may buy tractor and lawnmower supplies from a tractor supply company in the early spring to prepare for the seasonal upkeep of their small farm.

RFM analysis can help you identify this customer and build campaigns around loyalty programs and special summer sales. Use high monetary scores as an indicator for customers who do not require discounts.

.. rfm-example-high-m-low-f-end


.. _rfm-example-high-r-low-f-m:

High R, low F and M scores
--------------------------------------------------

.. rfm-example-high-r-low-f-m-start

A high recency score combined low frequency and monetary scores will build an audience of new customers who probably won't spend a lot of money in the future. Use this combination of scores as an indicator for customers that might respond to special offers, but consider the low spend to be an indicator of customers who may have a low response rate to more typical marketing campaigns.

.. rfm-example-high-r-low-f-m-end


.. _rfm-example-high-r-and-f-low-m:

High R and F, low M scores
--------------------------------------------------

.. rfm-example-high-r-and-f-low-m-start

High recency and frequency scores combined with a low monetary score will build an audience of active customers who purchase frequently, but do not spend a lot of money.

Use this combination of scores as an indicator for customers who should not receive discounts. These customers already shop regularly, the challenge is growing their spend. Use cross-sell and upsell campaigns to improve spend amounts and consider inviting customers who respond to those campaigns into your loyalty program.

.. rfm-example-high-r-and-f-low-m-end
