.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use the Transactions QA process to improve the quality of your transactions data.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use the Transactions QA process to improve the quality of your transactions data.

.. meta::
    :content class=swiftype name=title data-type=string:
        Transactions QA

==================================================
Transactions QA
==================================================

.. qa-transaction-about-start

Transactions QA is a process that validates the quality of interactions records. Use the collection of SQL queries provided by Amperity during the validation process.

.. stitch-qa-about-end


.. _qa-transaction-add-queries:

Add transaction QA queries
==================================================

.. database-interactions-transactions-query-qa-start

Use transactions QA queries to validate the quality of interaction records in the customer 360 database.

The recommended way to add transactions QA queries to your tenant is to use the "Transactions QA" query template. You can do this after you have added the customer 360 database and it contains the required tables.

.. database-interactions-transactions-query-qa-end

**To add Transaction QA queries**

.. database-interactions-transactions-query-qa-steps-start

#. From the **Segments** page click **Create**, and then select **Add Folder**. This opens the **Create Folder** dialog box.
#. Enter the name for the folder. For example: Transactions QA.
#. From the **Template** dropdown, select **Transactions QA**.
#. Click **Create**. This creates a folder, into which a collection of draft queries are added. Review the queries for more information about how each query works.

.. database-interactions-transactions-query-qa-steps-end


.. _qa-transaction-rollup-validation-queries:

Rollup validation queries
==================================================

.. qa-transaction-rollup-validation-queries-start

Run the following rollup queries, download the results, and then share the results with external stakeholders. Modify these queries as necessary to include all monetary fields.

.. qa-transaction-rollup-validation-queries-end


.. _qa-transaction-rollup-validation-queries-item:

for item-level rollups
--------------------------------------------------

.. qa-transaction-rollup-validation-queries-item-start

.. code-block:: sql
   :linenos:

   SELECT
     ,YEAR(order_datetime) AS order_year
     ,MONTH(order_datetime) AS order_month
     ,SUM(item_revenue) AS sum_item_revenue
     -- Uncomment the following lines if the fields are available
     -- ,SUM(item_cost) AS sum_item_cost
     -- ,SUM(item_list_price) AS sum_item_list_price
     -- OR:
     -- ,SUM(unit_list_price*item_quantity)
     -- ,SUM(item_subtotal) AS sum_item_subtotal
     -- ,SUM(item_discount_dollar_amount) AS sum_item_discount_dollar_amount
     ,SUM(item_quantity) AS sum_item_quantity
   FROM Unified_Itemized_Transactions
   GROUP BY 1, 2

.. qa-transaction-rollup-validation-queries-item-end


.. _qa-transaction-rollup-validation-queries-order:

for order-level rollups
--------------------------------------------------

.. qa-transaction-rollup-validation-queries-order-start

.. code-block:: sql
   :linenos:

   SELECT
     ,YEAR(order_datetime)
     ,MONTH(order_datetime)
     ,SUM(order_revenue)
     -- Uncomment the following lines if the fields are available
     --,SUM(order_cost)
     --,SUM(order_profit)
     --,SUM(order_subtotal)
     --,SUM(sum_item_discounts)
     --,SUM(order_discount_amount)
     ,SUM(order_quantity)
   FROM Unified_Transactions
   GROUP BY 1, 2

.. qa-transaction-rollup-validation-queries-order-end


.. _qa-transaction-prioritize-amperity-id:

Prioritize Amperity IDs
==================================================

.. qa-transaction-prioritize-amperity-id-start

If multiple Amperity IDs exist for interaction records after the Stitch process or after the use of foreign keys, use SQL to ensure that only one Amperity ID is associated to each interaction record.

.. qa-transaction-prioritize-amperity-id-end

**To prioritize Amperity IDs by most recent transaction**

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-first-value-example-prioritize-by-order-id-start
   :end-before: .. sql-spark-function-first-value-example-prioritize-by-order-id-end
