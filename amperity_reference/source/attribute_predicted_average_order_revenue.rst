.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        The average value of each order a customer is predicted to make if they return to make another purchase during the next 365 days.

.. meta::
    :content class=swiftype name=body data-type=text:
        The average value of each order a customer is predicted to make if they return to make another purchase during the next 365 days.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predicted average order revenue

==================================================
Predicted average order revenue
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-predicted-average-order-revenue-start
   :end-before: .. term-predicted-average-order-revenue-end

.. TODO: Add an ordered list of what this attribute is best used for right in this spot, similar to predicted_order_frequency.

.. attribute-predicted-average-order-revenue-start

Each prediction is represented by an amount, where a higher amount represents an increase in the amount of money a customer will spend (on average) during the next 365 days: a ``35.54`` score is a likelihood that a customer will spend $35.54, a ``110.03`` score is a likelihood that a customer will spend $110.03, and a ``257.35`` score is a likelihood that a customer will spend $257.35.

.. attribute-predicted-average-order-revenue-end


.. _attribute-predicted-average-order-revenue-about-clv:

About predicted CLV attributes
==================================================

.. attribute-predicted-average-order-revenue-about-clv-start

Amperity provides a set of attributes that predict customer lifetime value (CLV) during the next 365 days.

Each of these attributes provides a score that is independent of other predicted CLV attributes:

#. :doc:`Predicted CLV <attribute_predicted_clv>` represents the total value of all orders a customer is predicted to make *if they return to make another purchase* during the next 365 days.

   .. note:: Predicted CLV is the multiplication of three columns: 1) predicted probability of return, 2) predicted order frequency, and 3) predicted average order value.

      Each component of predicted CLV is also available as an individual score:

      #. :doc:`Predicted probability of transaction <attribute_predicted_transactions>` represents the likelihood that a customer will return to make another purchase during the next 365 days.
      #. :doc:`Predicted order frequency <attribute_predicted_order_frequency>` represents the number of orders a customer is predicted to make *if they return to make another purchase* during the next 365 days.
      #. Predicted average order revenue represents the average value of each order a customer is predicted to make *if they return to make another purchase* during the next 365 days.

#. :doc:`Predicted value tiers <attribute_predicted_value_tier>` group customers by pCLV: Platinum (top 1%), Gold (top 1%-5%), Silver (top 5%-10%), Bronze (top 10%-25%), Medium (top 25%-50%), and Low (bottom 50%).

Use a combination of predicted CLV attributes to identify high-value audiences for use with campaigns that focus on winning repeat customers, such as churn prevention, winback, and one-time buyer campaigns.

.. attribute-predicted-average-order-revenue-about-clv-end

.. attribute-predicted-average-order-revenue-about-clv-example-start

For example:

#. Start with predicted probability of transaction to identify customers with a very low likelihood of return.
#. Add predicted average order value to identify which of these customers would be high-value customers if they were to become a repeat customer.
#. Look for customers with a high score for predicted average order revenue who have low scores for predicted order frequency and predicted probability of transaction.

   This combination often represents a customer who is not engaged with your brand. If this customer does engage (or re-engage) with your brand, they are likely to spend more than your average customer.

.. attribute-predicted-average-order-revenue-about-clv-example-end


.. _attribute-predicted-average-order-revenue-segment:

Use in segments
==================================================

.. attribute-predicted-average-order-revenue-segment-start

To find predicted order frequencies, start with the **Predicted Average Order Value Next 365** attribute in the **Predicted CLV Attributes** table, and then select a condition. After the attribute appears in your segment, specify an amount for predicted average order revenue that aligns to the condition you selected.

.. attribute-predicted-average-order-revenue-segment-end

.. attribute-predicted-average-order-revenue-modeling-enabled-note-start

.. note:: Predicted average order revenue is available when predictive modeling is enabled for your tenant.

.. attribute-predicted-average-order-revenue-modeling-enabled-note-end


.. _attribute-predicted-average-order-revenue-conditions:

Available operators
==================================================

.. attribute-predicted-average-order-revenue-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a **decimal** data type. All **decimal** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific amount of predicted average order revenue, such as "117.99", "129.99", or "179.99".

       .. tip:: Use the following operators to return a range of predicted average order revenue amounts instead of a specific predicted average order revenue amount: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of predicted average order revenue amounts that are between the specified predicted average order revenue amounts.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns predicted average order revenue amounts that are greater than the specified predicted average order revenue amount.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns predicted average order revenue amounts that are greater than or equal to the specified predicted average order revenue amount.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition. Individual predicted average order revenue amounts are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns predicted average order revenue amounts that are less than the specified predicted average order revenue amount.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns predicted average order revenue amounts that are less than or equal to the specified predicted average order revenue amount.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "111.99" then any predicted average order revenue amounts less than or equal to "111.98" and any predicted average order revenue amounts greater than or equal to "112.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your predicted average order revenue amounts are between "111.99" and "182.99", use "111.99" and "182.99" to return predicted average order revenue amounts that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when individual revenue amounts are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "14.99", "59.99", and "127.22", but also " " (a space) and "0" (zero). If the record has *any* value it is returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-average-order-revenue-conditions-end
