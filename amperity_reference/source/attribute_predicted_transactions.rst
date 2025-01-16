.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        The likelihood that a customer will return to make another purchase during the next 365 days.

.. meta::
    :content class=swiftype name=body data-type=text:
        The likelihood that a customer will return to make another purchase during the next 365 days.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predicted transactions

==================================================
Predicted transactions
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-predicted-probability-of-transaction-start
   :end-before: .. term-predicted-probability-of-transaction-end

.. attribute-predicted-transactions-start

Each prediction is represented by a percentage, where a lower percentage represents a lower likelihood that a customer will return to make another purchase during the next 365 days: a "0.10" score is a 10% likelihood of return, a "0.26: score is a 26% likelihood of return, and a "0.63" score is a 63% likelihood of return.

.. attribute-predicted-transactions-end


.. _attribute-predicted-transactions-about-clv:

About predicted CLV attributes
==================================================

.. attribute-predicted-transactions-about-clv-start

Amperity provides a set of attributes that predict customer lifetime value (CLV) during the next 365 days.

Each of these attributes provides a score that is independent of other predicted CLV attributes:

#. :doc:`Predicted CLV <attribute_predicted_clv>` represents the total value of all orders a customer is predicted to make *if they return to make another purchase* during the next 365 days.

   .. note:: Predicted CLV is the multiplication of three columns: 1) predicted probability of return, 2) predicted order frequency, and 3) predicted average order value.

      Each component of predicted CLV is also available as an individual score:

      #. Predicted probability of transaction represents the likelihood that a customer will return to make another purchase during the next 365 days. For example, in the **Segment Editor**, select the **Predicted Probability Of Transactions Next 365 D** attribute, select the **is** condition, and then enter "50" into the field to return an audience of customers with a 50% probability of returning to make another purchase during the next 365 days.
      #. :doc:`Predicted order frequency <attribute_predicted_order_frequency>` represents the number of orders a customer is predicted to make *if they return to make another purchase* during the next 365 days. For example, in the **Segment Editor**, select the **Predicted Order Frequency Next 365 D** attribute, select the **is between** condition, and then enter "1" in the minimum field and "20" in the maximum field to return an audience of customers who are predicted to make a purchase up to 20 times in the next 365 days.
      #. :doc:`Predicted average order revenue <attribute_predicted_average_order_revenue>` represents the average value of each order a customer is predicted to make *if they return to make another purchase* during the next 365 days. For example, in the **Segment Editor**, select the **Predicted Average Order Revenue Next 365 D** attribute, select the **is greater than or equal to** condition, and then enter "100" in the field to return an audience who are predicted to spend 100 dollars or more in the next 365 days.

#. :doc:`Predicted value tiers <attribute_predicted_value_tier>` group customers by pCLV: Platinum (top 1%), Gold (top 1%-5%), Silver (top 5%-10%), Bronze (top 10%-25%), Medium (top 25%-50%), and Low (bottom 50%).

Use a combination of predicted CLV attributes to identify high-value audiences for use with campaigns that focus on winning repeat customers, such as churn prevention, winback, and one-time buyer campaigns.

.. attribute-predicted-transactions-about-clv-end

.. attribute-predicted-transactions-about-clv-example-start

For example:

#. Start with predicted probability of transaction to identify customers with a higher likelihood of return.
#. Add predicted order frequency to identify which of those customers are more likely to order multiple times.
#. Add predicted average order value to identify customers who are most likely to spend, on average, at least $100 per order.

.. attribute-predicted-transactions-about-clv-example-end


.. _attribute-predicted-transactions-segment:

Use in segments
==================================================

.. attribute-predicted-transactions-segment-start

To find predicted probability of transactions, start with the **Predicted Probability of Transaction Next 365** attribute in the **Predicted CLV Attributes** table, and then select a condition. After the attribute appears in your segment, specify the probability of transaction that you want to use in your segment. After the attribute appears in your segment, specify a frequency for predicted probability of transaction that aligns to the condition you selected.

.. attribute-predicted-transactions-segment-end

.. attribute-predicted-transactions-modeling-enabled-note-start

.. note:: Predicted transactions are available when predictive modeling is enabled for your tenant.

.. attribute-predicted-transactions-modeling-enabled-note-end


.. _attribute-predicted-transactions-conditions:

Available operators
==================================================

.. attribute-predicted-transactions-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a Decimal data type. All Decimal data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific probability of transaction, such as "1.2", "40.6", or "50.0".

       .. tip:: Use the following operators to return a range of probabilities instead of a specific probability: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of probabilities that are between the specified predicted probability.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns probabilities that are greater than the specified predicted probability.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns probabilities that are greater than or equal to the specified probability.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual probabilities are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns probabilities that are less than the specified predicted probability.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns probabilities that are less than or equal to the specified predicted probability.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "50.0" then any probability that is less than or equal to "49.99" and any probability that is greater than or equal to "50.01" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier probabilities.

       For example, if most of your probabilities are between "30.0" and "40.0", use "30.0" and "40.0" to return probabilities that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual probabilities are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as ".50", "59.99", and "100.0", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-predicted-transactions-conditions-end
