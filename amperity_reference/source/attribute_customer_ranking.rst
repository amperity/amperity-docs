.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Who are the top N customers who are most likely to purchase?

.. meta::
    :content class=swiftype name=body data-type=text:
        Who are the top N customers who are most likely to purchase?

.. meta::
    :content class=swiftype name=title data-type=string:
        Customer ranking

==================================================
Customer ranking
==================================================

.. include:: ../../amperity_reference/source/model_product_affinity.rst
   :start-after: .. model-product-affinity-use-cases-customer-ranking-topn-start
   :end-before: .. model-product-affinity-use-cases-customer-ranking-topn-end

.. include:: ../../amperity_reference/source/model_product_affinity.rst
   :start-after: .. model-product-affinity-use-cases-customer-ranking-start
   :end-before: .. model-product-affinity-use-cases-customer-ranking-end

.. include:: ../../amperity_reference/source/model_product_affinity.rst
   :start-after: .. model-product-affinity-use-cases-customer-ranking-attribute-start
   :end-before: .. model-product-affinity-use-cases-customer-ranking-attribute-end


.. _attribute-customer-ranking-segment:

Use in segments
==================================================

.. attribute-customer-ranking-segments-start

To find customer rankings by product, start with the **Ranking** attribute in the **Predicted Affinity** table, and then set its condition to **is less than or equal to**. After the attribute appears in your segment, specify the number of customers you want to include in the ranking. After the attribute appears in your segment specify a value or range that matches the operator.

.. attribute-customer-ranking-segments-end

.. attribute-customer-ranking-combine-with-product-start

.. important:: Combine the **Ranking** attribute with the **Product Attribute** attribute to build a customer ranking specific to the selected product attribute.

.. attribute-customer-ranking-combine-with-product-end

.. _attribute-customer-ranking-conditions:

Available operators
==================================================

.. attribute-customer-ranking-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a **integer** data type. All **integer** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Returns customer records with values that match the specified ranking.

   * - **is between**
     - Returns customer records with values that are between the specified rankings.

   * - **is greater than**
     - Returns customer records with values that are greater than the specified ranking, not including the specified ranking.

   * - **is greater than or equal to**
     - Returns customer records with values that are greater than or equal to the specified ranking, including the specified ranking.

   * - **is in list**
     - Returns customer records with values that match the rankings that are specified in a list.

   * - **is less than**
     - Returns customer records with values that are less than the specified ranking, not including the specified ranking.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with values that are less than or equal to the specified ranking, including the specified ranking.

       .. tip:: A rank that is less than or equal to X provides the top N customers with an affinity for a product.

   * - **is not**
     - Returns customer records with values that do not match the specified ranking.

   * - **is not between**
     - Returns customer records with values that are not between the specified rankings, not including the specified ankings.

   * - **is not in list**
     - Returns customer records with values that do not match the rankings that are specified in the list.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

.. attribute-customer-ranking-conditions-end
