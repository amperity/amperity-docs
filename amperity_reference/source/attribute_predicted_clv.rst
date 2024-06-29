.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The total value of all orders a customer is predicted to make if they return to make another purchase during the next 365 days.

.. meta::
    :content class=swiftype name=body data-type=text:
        The total value of all orders a customer is predicted to make if they return to make another purchase during the next 365 days.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predicted CLV

==================================================
Predicted CLV
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pclv-start
   :end-before: .. term-pclv-end

.. attribute-predicted-clv-start

Each prediction is represented by an amount, where a higher amount represents an increase in the amount of money a customer will spend (in total) during the next 365 days: a ``25.75`` score is a likelihood that a customer will spend $25.75, a ``140.45`` score is a likelihood that a customer will spend $140.45, and a ``295.25`` score is a likelihood that a customer will spend $295.25.

.. attribute-predicted-clv-end


.. _attribute-predicted-clv-about-clv:

About predicted CLV attributes
==================================================

.. attribute-predicted-clv-about-clv-start

AmpIQ provides a set of attributes that predict customer lifetime value (CLV) during the next 365 days.

Each of these attributes provides a score that is independent of other predicted CLV attributes:

#. Predicted CLV represents the total value of all orders a customer is predicted to make *if they return to make another purchase* during the next 365 days.

   .. note:: Predicted CLV is the multiplication of three columns: 1) predicted probability of return, 2) predicted order frequency, and 3) predicted average order value.

      Each component of predicted CLV is also available as an individual score:

      #. :doc:`Predicted probability of transaction <attribute_predicted_transactions>` represents the likelihood that a customer will return to make another purchase during the next 365 days.
      #. :doc:`Predicted order frequency <attribute_predicted_order_frequency>` represents the number of orders a customer is predicted to make *if they return to make another purchase* during the next 365 days.
      #. :doc:`Predicted average order revenue <attribute_predicted_average_order_revenue>` represents the average value of each order a customer is predicted to make *if they return to make another purchase* during the next 365 days.

#. :doc:`Predicted value tiers <attribute_predicted_value_tier>` group customers by pCLV: Platinum (top 1%),  Gold (top 1%-5%),  Silver (top 5%-10%),  Bronze (top 10%-25%),  Medium (top 25%-50%), and Low (bottom 50%).

Use a combination of predicted CLV attributes to identify high-value audiences for use with campaigns that focus on winning repeat customers, such as churn prevention, winback, and one-time buyer campaigns.

.. attribute-predicted-clv-about-clv-end

.. attribute-predicted-clv-about-clv-example-start

For example:

#. Start with predicted probability of transaction to identify customers with a higher likelihood of return.
#. Add predicted CLV to identify which of these customers would be high-value customers if they were to become a repeat customer, regardless of the number of purchases or average order amount.

.. attribute-predicted-clv-about-clv-example-end


.. _attribute-predicted-clv-examples:

Examples
==================================================

.. attribute-predicted-clv-examples-start

The following topics contain examples of using predicted CLV:

* |usecase_customers_lapsing|

.. attribute-predicted-clv-examples-end


.. _attribute-predicted-clv-segment:

Use in segments
==================================================

.. attribute-predicted-clv-segment-start

To apply predicted CLV to your segment, start with the **Predicted CLV Next 365** in the **Predicted CLV Attributes** table, and then set its condition to **is greater than or equal to**.

.. attribute-predicted-clv-segment-end

.. image:: ../../images/attribute-predicted-clv.png
   :width: 600 px
   :alt: Choose the predicted CLV attribute from the Segment Editor.
   :align: left
   :class: no-scaled-link

.. attribute-predicted-clv-filters-start

After the attribute appears in your segment, specify an amount for predicted customer lifetime value that aligns to the condition you selected. For example, to find customers for whom customer lifetime value is predicted to be greater than or equal to $2000:

.. attribute-predicted-clv-filters-end

.. image:: ../../images/attribute-predicted-clv-example.png
   :width: 600 px
   :alt: Find customers for whom customer lifetime value is predicted to be greater than or equal to $2000.
   :align: left
   :class: no-scaled-link

.. attribute-predicted-clv-modeling-enabled-note-start

.. note:: Predicted CLV is available to users of AmpIQ when predictive modeling is enabled for your tenant.

.. attribute-predicted-clv-modeling-enabled-note-end


.. _attribute-predicted-clv-conditions:

Available conditions
==================================================

.. attribute-predicted-clv-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a Decimal data type. All Decimal data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Returns a specific amount of predicted customer lifetime value, such as "117.99", "129.99", or "179.99".

       .. tip:: Use the following conditions to return a range of predicted customer lifetime values instead of a specific predicted customer lifetime value: **is between**, **is greater than**, **is greater than or equal to**, **is less than**, and **is less than or equal to**.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns a range of predicted customer lifetime values that are between the specified predicted customer lifetime values.

   * - **is greater than**
     - |attribute-recommended| **More useful**

       Returns predicted customer lifetime values that are greater than the specified predicted customer lifetime value.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns predicted customer lifetime values that are greater than or equal to the specified predicted customer lifetime value.

   * - **is in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is in list** condition; individual predicted customer lifetime values are not typically made available in a list.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns predicted customer lifetime values that are less than the specified predicted customer lifetime value.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns predicted customer lifetime values that are less than or equal to the specified predicted customer lifetime value.

   * - **is not**
     - |attribute-stop| **Less useful**

       Avoid using the **is not** condition.

       For example, if you specified "111.99" then any predicted customer lifetime values less than or equal to "111.98" and any predicted customer lifetime values greater than or equal to "112.00" would be returned.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Discovers outlier revenue.

       For example, if most of your predicted customer lifetime values are between "111.99" and "182.99", use "111.99" and "182.99" to return predicted customer lifetime values that were less than and greater than those values.

   * - **is not in list**
     - |attribute-stop| **Less useful**

       Avoid using the **is not in list** condition when predicted customer lifetime values are not made available as a list.

   * - **is not NULL**
     - Returns customer records that have a value, such as "14.99", "59.99", and "127.22", but also " " (a space) and "0" (zero). If the record has *any* value it will be returned.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-predicted-clv-conditions-end
