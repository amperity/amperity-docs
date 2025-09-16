.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Build queries using Presto SQL and the Query Editor.

.. meta::
    :content class=swiftype name=body data-type=text:
        Build queries using Presto SQL and the Query Editor.

.. meta::
    :content class=swiftype name=title data-type=string:
        Build queries

==================================================
Build queries
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-query-start
   :end-before: .. term-query-end


.. _queries-tab:

Queries page
==================================================

.. queries-tab-start

The **Queries** page provides an overview of the status of every query. A table shows the status and details. Queries are listed by row. The details include the date and time at which this query last ran, along with the number of rows of records that were returned during the last completed run.

.. queries-tab-end

.. image:: ../../images/mockup-queries-tab.png
   :width: 600 px
   :alt: Use the Queries page.
   :align: left
   :class: no-scaled-link


.. _queries-editor:

Query editor
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sql-query-editor-start
   :end-before: .. term-sql-query-editor-end

.. queries-editor-start

Use the **Query Editor** to build SQL queries against tables and columns in your customer 360 database to support any downstream workflow. The **Query Editor** uses |sql_presto|.

.. queries-editor-end

.. image:: ../../images/mockup-queries-tab-sql.png
   :width: 600 px
   :alt: Use the SQL Segment Editor on the Queries page.
   :align: left
   :class: no-scaled-link

.. queries-editor-context-start

Queries may be authored using the visual **Query Editor** or the **SQL Query Editor**. Click **Create**, and then select the query editor to open. Queries that are already created have an icon that shows from which query editor they were authored.

* |fa-visual-segment| indicates the query was created using the visual **Query Editor**.
* |fa-sql-segment| indicates the query was created using the **SQL Query Editor**.

All queries must be activated before they can run as part of a scheduled workflow.

.. queries-editor-context-end

.. queries-editor-multiuser-warning-start

.. note:: Amperity is a multi-user system and the set of queries for your company is shared across all users. That means that if one user creates a draft query, another can open and edit it, so work can be easily passed between people on your team.

   However, it also means that if 2 users are editing the same thing at the same time, their changes will collide.  Amperity resolves this by applying the last set of changes saved as a whole. This will keep the query in a consistent state. But changes that were saved first will be overwritten. As a result, we strongly recommend that you coordinate changes to specific objects in Amperity with others on your team.

.. queries-editor-multiuser-warning-end


.. _queries-editor-presto-sql:

About Presto SQL
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-presto-sql-start
   :end-before: .. term-presto-sql-end

.. queries-editor-presto-sql-start

Amperity queries are built using Presto SQL to define a **SELECT** statement. Please refer to the |sql_presto| reference.

.. queries-editor-presto-sql-end

.. queries-editor-presto-sql-select-statements-start

All queries that are built via the **SQL Query Editor** are done using a |sql_presto_select| statement. In some cases, a |sql_presto_with| is used along with the **SELECT** statement. Each select statement can additional functionality, such as |sql_presto_where|, |sql_presto_left_join|, |sql_presto_group_by|, |sql_presto_order_by|, |sql_presto_limit| clauses, |sql_presto_case| expressions, |sql_presto_functions|, |sql_presto_operators|, and other components that are part of Presto SQL, which is the underlying SQL engine for both the visual **Query Editor** and **SQL Query Editor**.

.. queries-editor-presto-sql-select-statements-end

.. queries-editor-presto-sql-tip-start

.. tip:: Follow the |sql_presto_recommendations| and patterns for  |sql_presto_indentation|, |sql_presto_naming_conventions|, |sql_presto_reserved_words|, and |sql_presto_whitespace|.

.. queries-editor-presto-sql-tip-end


.. _queries-build:

Build queries
==================================================

.. queries-manage-add-start

Queries may be authored using the visual **Query Editor** or the **SQL Query Editor**. Click **Create** and then select the query editor to open. Queries that are already created have an icon that shows from which query editor they were authored. All queries must be activated before they can run as part of a scheduled workflow.

.. queries-manage-add-end


.. _queries-add:

Add query
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-sql-query-editor-start
   :end-before: .. term-sql-query-editor-end

**To add a query using the SQL Query Editor**

.. queries-add-via-sql-editor-steps-start

#. From the **Queries** page click **Create**, and then select **SQL Query**. This opens the **SQL Query Editor**.
#. Under **Database**, select a database. The **Customer 360** database is selected by default.
#. Define the query against the selected database.
#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. queries-add-via-sql-editor-steps-end


.. _queries-preview-results:

Preview results
--------------------------------------------------

.. queries-preview-results-start

You can preview the results of a SQL query by clicking the **Run Query** button. This will do one of the following things:

* Return the first 100 results of the query to the preview pane directly below the query editor.
* Return an empty table.
* Return some type of error.

Use the preview results pane to fine-tune your queries, to make sure they return the data you want, and to make sure they don't contain any errors.

.. queries-preview-results-end

.. queries-preview-results-tip-start

.. tip:: Query editor SQL queries often evaluate millions of records. This means they may take a few minutes to run. You may use other areas of Amperity while a query is being run.

   For draft queries, setting a the **LIMIT** clause to "100" while developing a query is often enough for testing and validating query results against very large data sets.

.. queries-preview-results-tip-end

**To preview query results**

.. queries-preview-results-steps-start

#. From the **Queries** page, open the menu for a query, and then select **View**. This opens a query editor.
#. Click **Run Query** to run the query. Wait for it to return results.
#. Example the columns and the data that is in them.
#. Adjust your query as necessary until it runs correctly.
#. Click **Activate**.

.. queries-preview-results-steps-end


.. _queries-editor-validate:

Validate query
--------------------------------------------------

.. queries-editor-validate-start

SQL queries are validated from the **SQL Query Editor** by clicking the **Run Query** button. The results of the query are returned in the results window. The quality of the results can be inspected, and then fine-tuned. Errors in the syntax are reported in the results window.

.. queries-editor-validate-end


.. _queries-add-to-orchestration:

Add to orchestration
--------------------------------------------------

.. queries-add-to-orchestration-start

Use the **Orchestration** option to define a schedule for a query.

.. queries-add-to-orchestration-end

**To add a query to an orchestration**

.. queries-add-to-orchestration-steps-start

#. From the **Queries** page, open the menu for a query, and then select **View**. This opens a query editor.

   .. tip:: The query does not need to be in edit mode to configure an orchestration.
#. Under **Being Sent To** click **Add one now**. This opens the **Add Orchestration** dialog box.
#. Follow the steps to add an orchestration. The steps will vary depending on the destination, the data template, and the orchestration.
#. Click **Save**.

.. queries-add-to-orchestration-steps-end


.. _queries-examples:

Example queries
==================================================

.. queries-examples-start

This section contains examples of queries that you can add to your tenant:

* :ref:`queries-example-cohort-analysis`
* :ref:`queries-example-count-loyalty-by-state`
* :ref:`queries-example-days-to-second-purchase`
* :ref:`queries-example-google-analytics-reports`
* :ref:`queries-example-leaky-bucket`
* :ref:`queries-example-missing-amperity-ids`
* :ref:`queries-example-month-over-month-revenue`
* :ref:`queries-example-one-and-dones-by-category`
* :ref:`queries-example-one-and-dones-by-year`
* :ref:`queries-example-order-revenue-7-day-rolling-window`
* :ref:`queries-example-partition-predicted-clv-by-brand`
* :ref:`queries-example-percent-rank-of-purchases`
* :ref:`queries-examples-purchasers-12-month-rolling`
* :ref:`queries-example-rank-by-affinity`
* :ref:`queries-example-rank-by-amperity-id`
* :ref:`queries-example-reachable-email-by-state`
* :ref:`queries-example-return-percentiles`
* :ref:`queries-example-revenue-by-month`
* :ref:`queries-example-revenue-opportunity-1-group`
* :ref:`queries-example-revenue-opportunity-many-groups`
* :ref:`queries-example-top-20-percent-revenue`
* :ref:`queries-example-totals-by-brand`
* :ref:`queries-example-transactions-by-day`

.. important:: These queries are not meant to be copy/paste queries. Use them as examples. Most requires some customization to be used effectively within your tenant.

.. queries-examples-end


.. _queries-example-cohort-analysis:

Cohort analysis
--------------------------------------------------

.. queries-example-cohort-analysis-start

The following SQL builds a cohort analysis against the **Transaction Attributes Extended** table that returns a month-by-month view of customers acquired, split by channel, and then for each monthly cohort, how many repurchased within 60, 90, 180, and 365 days, and the channel on which customers made their repeat purchases.

.. tip:: Build cohort analysis queries for your tenant, and then send the results downstream to :doc:`your favorite analytics and/or BI tool <sendto_analytics_bi>`.

.. code-block:: sql
   :linenos:

   SELECT
     YEAR(tae.first_order_datetime) AS first_order_year
     ,MONTH(tae.first_order_datetime) AS first_order_month
     ,tae.first_order_purchase_channel
     ,COUNT(*) AS num_amp_id
     ,SUM(CASE
       WHEN tae.second_order_datetime <= tae.first_order_datetime + interval '60' day
       THEN 1
       ELSE 0
     END) AS repeat_60d
     ,SUM(CASE
       WHEN tae.second_order_purchase_channel = 'web'
       AND tae.second_order_datetime <= tae.first_order_datetime + interval '60' day
       THEN 1
       ELSE 0
     END) AS repeat_60d_web
     ,SUM(CASE
       WHEN tae.second_order_purchase_channel = 'store'
       AND tae.second_order_datetime <= tae.first_order_datetime + interval '60' day
       THEN 1
       ELSE 0
     END) AS repeat_60d_store
     ,SUM(CASE
       WHEN tae.second_order_purchase_channel = 'web'
       AND tae.second_order_datetime <= tae.first_order_datetime + interval '90' day
       THEN 1
       ELSE 0
     END) AS repeat_90d_web
     ,SUM(CASE
       WHEN tae.second_order_purchase_channel = 'store'
       AND tae.second_order_datetime <= tae.first_order_datetime + interval '90' day
       THEN 1
       ELSE 0
     END) AS repeat_90d_store
     ,SUM(CASE
       WHEN tae.second_order_purchase_channel = 'web'
       AND tae.second_order_datetime <= tae.first_order_datetime + interval '180' day
       THEN 1
       ELSE 0
     END) AS repeat_180d_web
     ,SUM(CASE
       WHEN tae.second_order_purchase_channel = 'store'
       AND tae.second_order_datetime <= tae.first_order_datetime + interval '180' day
       THEN 1
       ELSE 0
     END) AS repeat_180d_store
     ,SUM(CASE
       WHEN tae.second_order_purchase_channel = 'web'
       AND tae.second_order_datetime <= tae.first_order_datetime + interval '365' day
       THEN 1
       ELSE 0
     END) AS repeat_365d_web
     ,SUM(CASE
       WHEN tae.second_order_purchase_channel = 'store'
       AND tae.second_order_datetime <= tae.first_order_datetime + interval '365' day
       THEN 1
       ELSE 0
     END) AS repeat_365d_store
   FROM Transaction_Attributes_Extended tae
   GROUP BY 1,2,3
   ORDER BY 1,2,3

.. queries-example-cohort-analysis-end


.. _queries-example-count-loyalty-by-state:

Count loyalty by state
--------------------------------------------------

.. queries-example-count-loyalty-by-state-start

The following example counts customers in the United States, and then also in California, Oregon, Washington, Alaska, and Hawaii who also belong to the loyalty program (which is indicated when loyalty_id is not NULL):

.. code-block:: sql
   :linenos:

   SELECT
     state
     ,COUNT(amperity_id) AS TotalCustomers
   FROM
     Customer360
   WHERE (UPPER("country") = 'US'
   AND UPPER("state") in ('AK', 'CA', 'HI', 'OR', 'WA')
   AND LOWER("loyalty_id") IS NOT NULL)
   GROUP BY state

.. queries-example-count-loyalty-by-state-end


.. _queries-example-customer-acquisition:

Customer acquisition
--------------------------------------------------

.. queries-example-customer-acquisition-start

The following examples show how to track customer acquisition by day for single- and multi-brand tenants.

.. queries-example-customer-acquisition-end

.. queries-example-customer-acquisition-tip-start

.. tip:: Build customer acquisition queries for your tenant, and then send the results downstream to :doc:`your favorite analytics and/or BI tool <sendto_analytics_bi>`.

.. queries-example-customer-acquisition-tip-end

**For single-brand tenants**

.. queries-example-customer-acquisition-single-brand-start

.. code-block:: sql
   :linenos:

   SELECT
     DATE(first_order_datetime) AS first_order_date
     ,COUNT(DISTINCT amperity_id) AS total_customers
     ,SUM(CASE
       WHEN one_and_done
       THEN 1
       ELSE 0
     END) AS total_one_and_done
     ,AVG(lifetime_order_revenue) AS avg_clv
     ,SUM(CASE
       WHEN L12M_order_frequency > 0
       THEN 1
       ELSE 0
     END) AS L12M_total_orders
   FROM Transaction_Attributes_Extended
   GROUP BY 1,2,3
   ORDER BY 1,2,3

.. queries-example-customer-acquisition-single-brand-end

**For multi-brand tenants**

.. queries-example-customer-acquisition-multi-brand-start

.. code-block:: sql
   :linenos:

   SELECT
     multi_purchase_brand
     ,multi_purchase_channel
     ,DATE(first_order_datetime) AS first_order_date
     ,COUNT(DISTINCT amperity_id) AS total_customers
     ,SUM(CASE
       WHEN one_and_done
       THEN 1
       ELSE 0
     END) AS total_one_and_done
     ,AVG(lifetime_order_revenue) AS avg_clv
     ,SUM(CASE
       WHEN L12M_order_frequency > 0
       THEN 1
       ELSE 0
     END) AS L12M_total_orders
   FROM Transaction_Attributes_Extended
   GROUP BY 1,2,3
   ORDER BY 1,2,3

.. queries-example-customer-acquisition-multi-brand-end


.. _queries-example-days-to-second-purchase:

Days to second purchase
--------------------------------------------------

.. queries-example-days-to-second-purchase-start

The following example shows how to return the days to second purchase starting from a date range for the first order.

.. code-block:: sql
   :linenos:

   SELECT
     days_to_second_purchase
     ,COUNT(DISTINCT amperity_id) AS "customer_count"
   FROM (
     SELECT 
       amperity_id
       ,first_order_datetime
       ,second_order_datetime
       ,DATE_DIFF('day', first_order_datetime, second_order_datetime) AS "days_to_second_purchase"
     FROM Transaction_Attributes_Extended
     WHERE (
       (
         "amperity_id" IN (
           SELECT DISTINCT "t0"."amperity_id"
           FROM "Transaction_Attributes_Extended" "t0"
           WHERE (
             "t0"."first_order_datetime" BETWEEN TIMESTAMP '2019-01-01'
             AND TIMESTAMP '2022-01-01'
             AND "t0"."second_order_datetime" IS NOT NULL
           )
         )
       )
     )
     GROUP BY amperity_id, first_order_datetime, second_order_datetime
   )
   GROUP BY 1
   ORDER BY 1 ASC


.. tip:: You can extend the **WHERE** statement to show days to second purchase by brand:

   .. code-block:: sql
      :linenos:

      WHERE (
        "t0"."first_order_datetime" BETWEEN timestamp '2019-12-01'
        AND timestamp '2023-12-28'
        AND "t0"."second_order_datetime" IS NOT NULL
        AND "t0"."first_order_purchase_brand" = 'Brand A'
        --AND "t0"."first_order_purchase_brand" = 'Brand B'
        --AND "t0"."first_order_purchase_brand" = 'Brand C'
        --AND "t0"."first_order_purchase_brand" = 'Brand ...'
        --Comment brands out when not needed
      )

.. queries-example-days-to-second-purchase-by-brand-end


.. _queries-example-google-analytics-reports:

Google Analytics reports
--------------------------------------------------

.. queries-example-google-analytics-reports-start

The following example shows how build acquisition channel reports using the **GoogleAnalytics4_TransactionalAnalytics4** table that is created by the |source_google_analytics| data source.

.. code-block:: sql
   :linenos:

   WITH first_order AS (
     SELECT DISTINCT
       ut.amperity_id
       ,order_ID
       ,first_order_datetime
     FROM Unified_Transactions ut
     INNER JOIN (
       SELECT
         amperity_id
         ,first_order_datetime
       FROM Transaction_Attributes_Extended
       WHERE first_order_datetime
       BETWEEN timestamp '2022-09-05 00:00:00'
       AND timestamp '2022-09-13 00:00:00') ta
     ON ta.amperity_id = ut.amperity_id
     AND ta.first_order_datetime = ut.order_datetime
   )

   SELECT
     sessionSource
     ,COUNT(amperity_id) new_customers
   FROM first_order
   LEFT JOIN (
     SELECT
       transactionId
       ,sessionSource
     FROM GoogleAnalytics4_TransactionalAnalytics4
   ) GA
   ON first_order.order_ID = GA.transactionId
   GROUP BY 1
   ORDER BY 2 DESC

.. queries-example-google-analytics-reports-end

.. queries-example-google-analytics-reports-columns-start

.. admonition:: What columns are available?

   You can use any column in the **GoogleAnalytics4_TransactionalAnalytics4** table to build reports:

   * **itemRevenue**
   * **transactionId**
   * **browser**
   * **sessionCampaignName**
   * **sessionSource**
   * **sessionGoogleAdsAdGroupName**
   * **date**
   * **deviceCategory**
   * **operatingSystem**
   * **sessionGoogleAdsQuery**
   * **operatingSystemVersion**
   * **sessionMedium**
   * **sessionGoogleAdsAdGroupId**

.. queries-example-google-analytics-reports-columns-end


.. _queries-example-leaky-bucket:

Leaky bucket ratio
--------------------------------------------------

.. queries-example-leaky-bucket-start

A leaky bucket ratio tracks the difference between the customers your brand wins and loses over time.

The following query shows how to build a leaky bucket ratio by using columns in the **Customer Attributes** and **Transaction Attributes Extended** tables to find the difference between lost and won customers during the past month and the past year.

.. note:: This example assumes that the **Churn Trigger Start Datetime** and **Churn Trigger** fields are enabled in the **Customer Attributes** table. Uncomment the following sections in the SQL for the **Customer Attributes** table:

   .. code-block:: sql
      :linenos:

      /*
      ,churn_triggers_cte AS (
        SELECT
          amperity_id
          ,concat(current_event_status,' trigger') AS churn_trigger
          ,event_status_start_datetime AS churn_trigger_start_datetime
        FROM churn_triggers
      )
      */

   and:

   .. code-block:: sql

      -- LEFT JOIN churn_triggers_cte ct ON ct.amperity_id = cl.amperity_id


.. code-block:: sql
   :linenos:

   WITH leaky_bucket AS (

     SELECT
       YEAR(churn_trigger_start_datetime) AS year
       ,MONTH(churn_trigger_start_datetime) AS month
       ,SUM(IF(churn_trigger = 'Lost',1,0)) AS lost
       ,0 AS won
      FROM Customer_Attributes
      GROUP BY 1,2

      UNION ALL

      SELECT
        YEAR(first_order_datetime) AS year
        ,MONTH(first_order_datetime) AS month
        ,0 AS lost
        ,COUNT(first_order_id) AS won
      FROM Transaction_Attributes_Extended
      GROUP BY 1,2
   )

   SELECT 
     year
     ,month
     ,SUM(lost) AS lost
     ,SUM(won) AS won
     ,SUM(won) - SUM(lost) AS ratio
   FROM leaky_bucket
   GROUP BY 1,2
   ORDER BY year DESC, month DESC

.. queries-example-leaky-bucket-end


.. _queries-example-missing-amperity-ids:

Missing Amperity IDs
--------------------------------------------------

.. queries-example-missing-amperity-ids-start

Use the following example to find missing transaction IDs. The query calculates the percentage of missing Amperity IDs and customer IDs in the **Unified Transactions** table.

.. code-block:: sql
   :linenos:

   SELECT
     COUNT(DISTINCT CASE WHEN amperity_id IS NULL THEN order_id END) orders_missing_amp_id
     ,COUNT(DISTINCT CASE WHEN customer_id IS NULL THEN order_id END) orders_missing_cust_id
     ,1.0000*COUNT(DISTINCT CASE WHEN amperity_id IS NULL THEN order_id END)/COUNT(distinct order_id) pct_orders_missing_amp_id
     ,1.0000*COUNT(DISTINCT CASE WHEN customer_id IS NULL THEN order_id END)/COUNT(distinct order_id) pct_orders_missing_cust_id
   FROM (
     SELECT DISTINCT
       ,order_id
       ,amperity_id
       ,customer_id AS customer_id_value
     FROM Unified_Transactions
   )

Update the following line and replace "customer_id_value" with an actual customer ID:

::

   customer_id AS customer_id_value

.. queries-example-missing-amperity-ids-end


.. _queries-example-month-over-month-revenue:

Month-over-month revenue
--------------------------------------------------

.. queries-example-month-over-month-revenue-start

The following query returns month-over-month revenue.

.. code-block:: sql
   :linenos:

   SELECT
     MONTH(order_datetime) order_month
     ,COUNT(DISTINCT ut.amperity_id) number_customers
     ,COUNT(DISTINCT new_cust.amperity_id) number_new_customers
     ,CAST(AVG(order_revenue) AS decimal) aov
     ,1.00*SUM(order_revenue)/SUM(order_quantity) aor
     ,CAST(SUM(order_revenue) AS DECIMAL) total_revenue
   FROM (
     SELECT
       amperity_id
       ,order_datetime
       ,SUM(item_revenue) order_revenue
       ,SUM(item_quantity) order_quantity
     FROM Unified_Itemized_Transactions
     WHERE YEAR(order_datetime)=2020
     GROUP BY 1,2) ut
   LEFT JOIN (
     SELECT amperity_id
     FROM Transaction_Attributes_Extended
     WHERE year(first_order_datetime)=2020) new_cust
   ON ut.amperity_id=new_cust.amperity_id
   GROUP BY 1

.. queries-example-month-over-month-revenue-end


.. _queries-example-one-and-dones-by-category:

One and dones, by category
--------------------------------------------------

.. queries-example-one-and-dones-by-category-start

The following example shows how to return all one-and-done purchasers for a single calendar year by product category:

.. code-block:: sql
   :linenos:

   WITH new_in_21 AS (
     SELECT
       amperity_id
       ,one_and_done
     FROM Transaction_Attributes_Extended
     WHERE YEAR(first_order_datetime) = 2021
   ),

   product_categories AS (
     SELECT DISTINCT
       new_in_21.amperity_id
       ,one_and_done
       ,product_category
     FROM Unified_Itemized_Transactions uit
     INNER JOIN new_in_21 ON new_in_21.amperity_id=uit.amperity_id
   )

   SELECT
     product_category
     ,COUNT(distinct amperity_id) customer_count
     ,1.0000*SUM(CASE when one_and_done THEN 1 ELSE 0 END) / COUNT(DISTINCT amperity_id) pct_one_done
   FROM product_categories
   GROUP BY 1
   ORDER BY 3 DESC

.. queries-example-one-and-dones-by-category-end


.. _queries-example-one-and-dones-by-year:

One and dones, by year
--------------------------------------------------

.. queries-example-one-and-dones-by-year-start

The following example shows how to return all one-and-done purchasers for a single calendar year:

.. code-block:: sql
   :linenos:

   WITH one_and_dones_2022 AS (
     SELECT
       amperity_id
     FROM Transaction_Attributes_Extended
     WHERE one_and_done AND YEAR(first_order_datetime) = 2022
   )

   SELECT
     COUNT(*) one_and_dones_2022
   FROM
     one_and_dones_2022

.. queries-example-one-and-dones-by-year-end


.. _queries-example-order-revenue-7-day-rolling-window:

Order revenue, 7-day rolling window
--------------------------------------------------

.. queries-example-order-revenue-7-day-rolling-window-start

The following example shows a rolling seven day window for order revenue.

.. code-block:: sql
   :linenos:

   SELECT
     *
   FROM (
     SELECT
       purchase_channel
       ,order_day
       ,SUM(order_revenue) OVER (PARTITION BY purchase_channel ORDER BY order_day ROWS BETWEEN 6 preceding AND current row) rolling_7_day_revenue
     FROM (
       SELECT
         purchase_channel
         ,DATE(order_datetime) order_day
         ,SUM(order_revenue) order_revenue
       FROM Unified_Transactions
       WHERE amperity_id IS NOT NULL
       AND order_datetime > (CURRENT_DATE - interval '36' day)
       GROUP BY 1,2
     )
   )
   WHERE order_day > (CURRENT_DATE - interval '30' day)
   ORDER BY 1,2

.. queries-example-order-revenue-7-day-rolling-window-end


.. _queries-example-partition-predicted-clv-by-brand:

Partition pCLV by brand
--------------------------------------------------

.. queries-example-partition-predicted-clv-by-brand-start

Use the **NTILE()** function to partition by brand, and then order by predicted customer lifetime value.

.. code-block:: sql

   NTILE(100) OVER (PARTITION BY brand ORDER BY predicted_clv desc, _uuid_pk)

.. queries-example-partition-predicted-clv-by-brand-end


.. _queries-example-percent-rank-of-purchases:

Percent rank of purchases
--------------------------------------------------

.. queries-example-percent-rank-of-purchases-start

Use the **PERCENT_RANK()** function to return the percent rank of all purchases.

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     amperity_id
     ,order_revenue
     ,PERCENT_RANK() OVER (ORDER BY order_revenue) pct_rank
   FROM Unified_Transactions
   WHERE order_datetime > DATE('2021-04-01') AND amperity_id IS NOT NULL
   ORDER BY pct_rank DESC

.. queries-example-percent-rank-of-purchases-end


.. _queries-examples-purchasers-12-month-rolling:

Purchasers, 12-month rolling window
--------------------------------------------------

.. queries-examples-purchasers-12-month-rolling-start

The following query returns a distinct count of purchasers during the previous 12 months.

.. code-block:: sql
   :linenos:

   WITH periods AS (
     SELECT DISTINCT
       YEAR(order_datetime) order_year
       ,MONTH(order_datetime) order_month
     FROM Unified_Transactions
   )

   ,amp_base AS (
     SELECT
       amperity_id
       ,order_year
       ,order_month
     FROM (
       SELECT DISTINCT
         amperity_id
       FROM Unified_Transactions
     ) ut
     CROSS JOIN periods
   )

   ,purchase_by_month AS (
     SELECT
       YEAR(order_datetime) purchase_year
       ,MONTH(order_datetime) purchase_month
       ,amperity_id AS purchase_amperity_id
       ,COUNT(distinct order_id) orders
     FROM Unified_Transactions
     GROUP BY 1,2,3
   )

   ,all_together AS (
     SELECT
       order_year
       ,order_month
       ,amperity_id
       ,SUM(orders) order_month_total
       ,SUM(SUM(orders)) OVER (
         PARTITION BY amperity_id
         ORDER BY order_year, order_month
         ROWS BETWEEN 11 preceding AND current row
       ) preceding_12_month_orders
     FROM amp_base
     LEFT JOIN purchase_by_month
     ON
       amp_base.amperity_id=purchase_by_month.purchase_amperity_id
       AND amp_base.order_year=purchase_by_month.purchase_year
       AND amp_base.order_month=purchase_by_month.purchase_month
     GROUP BY 1,2,3
   )

   ,last12_month_purchasers AS (
     SELECT
       order_year
       ,order_month
       ,COUNT(DISTINCT CASE
         WHEN preceding_12_month_orders > 0
         THEN amperity_id
       END) last_12_month_purchasers
     FROM all_together
     GROUP BY 1,2
   )

   SELECT *
   FROM last12_month_purchasers
   ORDER BY 1 DESC, 2 DESC

.. queries-examples-purchasers-12-month-rolling-end


.. _queries-example-product-replenishment-by-date:

Product replenishment by date
--------------------------------------------------

.. queries-example-product-replenishment-by-date-start

The following query shows how to return results for product replenishment use cases. The query uses first purchase dates and next purchase dates to build timeframes around which a replenishment campaign can be run.

.. important:: 

   You must configure this query to match your brand's product catalog.

   The **product_description** field represents the name of a specific product in your product catalog. Update this field to match the field in your product catalog that defines product descriptions. For example, this may be a field that returns a SKU value. Update the "'<string>'" value to match the specific name of a product.

   The **product_group** field represents a category of products within your product catalog. Update this field to match the field in your product catalog that defines product categories.

   Use the "AND product_group <> '<group>'" line to specify one or more groups. Add a line for each group. Remove the line when product categories should not returned for your product replenishment use case.

   Explore the query results and tune the query parameters to align to your brand's product catalog and replenishment use case.

.. code-block:: sql
   :linenos:

   WITH product_purchases AS (
     SELECT
       amperity_id
       ,product_description
       ,order_datetime
     FROM Unified_Itemized_Transactions
     WHERE product_description = '<string>'
     AND item_list_price > 0
     AND product_group <> '<group>'
     AND item_revenue > 0
   )

   ,product_purchase_pairs AS (
     SELECT
       t1.amperity_id
       ,t1.product_description
       ,t1.order_datetime AS first_purchase_date
       ,MIN(t2.order_datetime) AS next_purchase_date
     FROM product_purchases t1
     JOIN product_purchases t2 ON t1.amperity_id = t2.amperity_id
     AND t1.product_description = t2.product_description
     AND t1.order_datetime < t2.order_datetime
     GROUP BY t1.amperity_id
              ,t1.product_description
              ,t1.order_datetime
   )

   SELECT *
   FROM (
     SELECT
       DATE_DIFF(
         'day'
         ,first_purchase_date
         ,next_purchase_date
       ) AS days_between_purchases
       ,COUNT(*) AS number_of_customers
     FROM product_purchase_pairs
     GROUP BY DATE_DIFF ('day', first_purchase_date, next_purchase_date)
     ORDER BY days_between_purchases
   )
   WHERE days_between_purchases > 0

.. queries-example-product-replenishment-by-date-end


.. _queries-example-product-replenishment-by-decile:

Product replenishment by decile
--------------------------------------------------

.. queries-example-product-replenishment-by-decile-start

The following query shows how to return results for product replenishment use cases. The query uses first purchase dates and next purchase dates to build timeframes, and then groups customers into deciles.

.. important:: You must configure this query to match your brand's product catalog.

   The **product_description** field represents the name of a specific product in your product catalog. Update this field to match the field in your product catalog that defines product descriptions. For example, this may be a field that returns a SKU value. Update the "'<string>'" value to match the specific name of a product.

   The **product_group** field represents a category of products within your product catalog. Update this field to match the field in your product catalog that defines product categories.

   Use the "AND product_group <> '<group>'" line to specify one or more groups. Add a line for each group. Remove the line when product categories should not returned for your product replenishment use case.

   Explore the query results and tune the query parameters to align to your brand's product catalog and replenishment use case.

.. code-block:: sql
   :linenos:

   WITH product_purchases AS (
     SELECT
       amperity_id
       ,product_description
       ,order_datetime
     FROM Unified_Itemized_Transactions
     WHERE item_list_price > 0
     AND product_group <> 'SAMPLE'
     AND item_revenue > 0
   )

   ,product_purchase_pairs AS (
     SELECT
       t1.amperity_id
       ,t1.product_description
       ,t1.order_datetime AS first_purchase_date
       ,MIN(t2.order_datetime) AS next_purchase_date
     FROM product_purchases t1
     JOIN product_purchases t2 ON t1.amperity_id = t2.amperity_id
     AND t1.product_description = t2.product_description
     AND t1.order_datetime < t2.order_datetime
     GROUP BY t1.amperity_id
              ,t1.product_description
              ,t1.order_datetime
   )

   ,days_diff AS (
     SELECT
       amperity_id
       ,product_description
       ,DATE_DIFF(
         'day'
         ,first_purchase_date
         ,next_purchase_date
       ) AS days_between_purchases
     FROM product_purchase_pairs
   )

   ,deciles AS (
     SELECT
       amperity_id
       ,product_description
       ,days_between_purchases
       ,NTILE(10) OVER (
         PARTITION BY product_description
         ORDER BY days_between_purchases ASC
       ) AS decile
     FROM days_diff
     WHERE days_between_purchases > 0
   )

   SELECT *
   FROM (
     SELECT
       product_description
       ,AVG(days_between_purchases) AS average_days_between
       ,COUNT(amperity_id) AS count_replenishments
       ,COUNT(DISTINCT amperity_id) AS count_customers
       ,MAX(CASE
         WHEN decile = 1 THEN days_between_purchases
         END) AS "Maximum days (1st decile)"
       ,MAX(CASE
         WHEN decile = 2 THEN days_between_purchases
         END) AS "2nd decile"
       ,MAX(CASE
         WHEN decile = 3 THEN days_between_purchases
         END) AS "3rd decile"
       ,MAX(CASE
         WHEN decile = 4 THEN days_between_purchases
         END) AS "4th decile"
       ,MAX(CASE
         WHEN decile = 5 THEN days_between_purchases
         END) AS "5th decile"
       ,MAX(CASE
         WHEN decile = 6 THEN days_between_purchases
         END) AS "6th decile"
       ,MAX(CASE
         WHEN decile = 7 THEN days_between_purchases
         END) AS "7th decile"
       ,MAX(CASE
         WHEN decile = 8 THEN days_between_purchases
         END) AS "8th decile"
       ,MAX(CASE
         WHEN decile = 9 THEN days_between_purchases
         END) AS "9th decile"
       ,MAX(CASE
         WHEN decile = 10 THEN days_between_purchases
         END) AS "Minimum days (10th decile)"
     FROM deciles
     GROUP BY 1
     ORDER BY 3 DESC
   )

.. queries-example-product-replenishment-by-decile-end


.. _queries-example-products-by-revenue:

Products by revenue
--------------------------------------------------

.. queries-example-products-by-revenue-start

Use the following example to return your top 5 products by revenue.

.. code-block:: sql
   :linenos:

   SELECT
     product_id
     ,SUM(item_revenue) AS total_revenue
   FROM Unified_Itemized_Transactions
   WHERE
     DATE_TRUNC('month', order_datetime) = DATE_TRUNC('month', CURRENT_DATE)
   GROUP BY product_id
   ORDER BY total_revenue DESC
   LIMIT 5

Use the **LIMIT** clause to configure the top N products.

.. queries-example-products-by-revenue-end


.. _queries-example-rank-by-affinity:

Rank by product affinity
--------------------------------------------------

.. queries-example-rank-by-affinity-start

The following query shows an example of how to rank customers by product affinity:

.. code-block:: sql
   :linenos:

   WITH rankings AS (
     SELECT
       amperity_id
       ,product_attribute
       ,RANK() OVER (PARTITION BY amperity_id ORDER BY ranking) rec_ranking
     FROM Predicted_Affinity_Table
     WHERE ranking < 10000000
   )
   ,top_5_by_customers AS (
     SELECT
       amperity_id
       ,MAX(CASE WHEN rec_ranking=1 THEN product_attribute END) prod_ranking_1
       ,MAX(CASE WHEN rec_ranking=2 THEN product_attribute END) prod_ranking_2
       ,MAX(CASE WHEN rec_ranking=3 THEN product_attribute END) prod_ranking_3
       ,MAX(CASE WHEN rec_ranking=4 THEN product_attribute END) prod_ranking_4
       ,MAX(CASE WHEN rec_ranking=5 THEN product_attribute END) prod_ranking_5
     FROM rankings
     GROUP BY 1
   )

   SELECT *
   FROM top_5_by_customers


Use the **WHERE** clause to set the maximum threshold for product affinity:

::

   WHERE ranking < some_value

For example, if the threshold is "10000000" then a customer is more than ten millionth in product affinity, then that customer is not included in the ranking.

.. queries-example-rank-by-affinity-end


.. _queries-example-rank-by-amperity-id:

Rank by Amperity ID
--------------------------------------------------

.. queries-example-rank-by-amperity-id-start

Use the **RANK()** function to find the largest transactions by Amperity ID, and then return them in ascending order:

.. code-block:: sql
   :linenos:

   WITH ranked_transactions AS (
     SELECT
       t.orderid
       ,t.amperity_id
       ,t.transactiontotal
       ,RANK() OVER (
         PARTITION BY t.amperity_id
         ORDER BY t.transactiontotal DESC
       ) AS rank
     FROM TransactionsEcomm t
     ORDER BY t.amperity_id, rank ASC
     LIMIT 100
   )
   SELECT * FROM ranked_transactions WHERE rank = 1

.. queries-example-rank-by-amperity-id-end


.. _queries-example-reachable-email-by-state:

Reachable email, by state
--------------------------------------------------

.. queries-example-reachable-email-by-state-start

The following example shows how to return a list of customers with reachable email addresses, by state:

.. code-block:: sql
   :linenos:

   SELECT
     COUNT(amperity_id) AS count
     ,state
     ,SUM(email_count) AS has_email
   FROM (
     SELECT
       c.amperity_id
       ,state
       ,IF(e.amperity_id IS NULL,0,1) AS email_count
     FROM Customer_360 c
     LEFT JOIN (
       SELECT DISTINCT amperity_id FROM Email_Table agg
       WHERE agg.email_opt_out_field = 'No'
       AND agg.email_out_status = 'opt-in'
     ) e ON e.amperity_id = c.amperity_id
   WHERE state IS NOT NULL)
   GROUP BY state

.. queries-example-reachable-email-by-state-end


.. _queries-example-return-percentiles:

Return percentiles
--------------------------------------------------

.. queries-example-return-percentiles-start

Return tenth percentiles:

.. code-block:: sql
   :linenos:

   SELECT
     tier*.1 AS tier
     ,MIN(lifetime_order_revenue) lifetime_revenue_amount
   FROM (
     SELECT
       amperity_id
       ,lifetime_order_revenue
       ,NTILE(10) OVER (ORDER BY lifetime_order_revenue) tier
     FROM Transaction_Attributes_Extended
   )
   GROUP BY 1
   ORDER BY 1


Return percentiles by 4:

.. code-block:: sql
   :linenos:

   SELECT
     tier*.25 tier
     ,MIN(lifetime_order_revenue) lifetime_revenue_amount
   FROM (
     SELECT DISTINCT
       amperity_id
       ,lifetime_order_revenue
       ,NTILE(4) OVER (ORDER BY lifetime_order_revenue) tier
     FROM Transaction_Attributes_Extended
   )
   GROUP BY 1
   ORDER BY 1

.. queries-example-return-percentiles-end


.. _queries-example-revenue-by-month:

Revenue by month
--------------------------------------------------

.. queries-example-revenue-by-month-intro-start

The following query returns three values for each month in a calendar year: revenue for customers who are in your top 20 percent, total revenue, and the percent of total revenue your top 20 percent customers represent.

.. queries-example-revenue-by-month-intro-end

.. queries-example-revenue-by-month-statement-start

.. code-block:: sql
   :linenos:

   SELECT
     month
     ,SUM(CASE
            WHEN top_20
            THEN revenue
            ELSE NULL
          END) revenue
     ,SUM(revenue) total_revenue
     ,1.00*SUM(CASE
                 WHEN top_20
                 THEN revenue
                 ELSE NULL
               END)/SUM(revenue) percent
   FROM (
     SELECT
       month
       ,amperity_id
       ,revenue
       ,CASE
         WHEN rank IN (9,10) THEN TRUE
         ELSE FALSE
       END AS top_20
     FROM (
       SELECT
         MONTH(order_datetime) AS month
         ,amperity_id
         ,SUM(order_revenue) revenue
         ,NTILE(10) OVER (ORDER BY SUM(order_revenue)) rank
       FROM Unified_Transactions
       WHERE YEAR(order_datetime)=2022
       GROUP BY 1,2
     )
   )
   GROUP BY 1
   ORDER BY month ASC

.. queries-example-revenue-by-month-statement-end


.. _queries-example-revenue-opportunity-1-group:

Revenue opportunity, 1 group
--------------------------------------------------

.. queries-example-revenue-opportunity-1-group-start

Use the following example to size revenue opportunity for a single group, such as for "one-and-done" or for "repeat purchaser". This query is most effective when run against the **Transaction Attributes Extended** table, but may be useful when run against other tables. Customize the **WHERE** clause in the **WITH** statement to define the group. Customize the main **SELECT** statement to define the time periods to measure.

.. code-block:: sql
   :linenos:

   WITH customers AS (
     SELECT
       amperity_id
     FROM Transaction_Attributes_Extended
     WHERE one_and_done
   )

   SELECT
     COUNT(DISTINCT tae.amperity_id) AS num_customers
     ,AVG(lifetime_average_order_value) AS lt_aov
     ,AVG(L12M_average_order_value) AS l12m_aov
     ,AVG(lifetime_order_revenue) AS lt_rev
     ,AVG(l12m_order_revenue) AS l12m_rev
     ,AVG(lifetime_average_item_price) AS lt_aur
     ,AVG(l12m_average_item_price) AS l12m_aur
     ,AVG(lifetime_order_frequency) AS avg_lt_orders
     ,AVG(l12m_order_frequency) AS avg_l12m_orders
     ,SUM(l12m_order_revenue) AS total_l12m_revenue
   FROM customers cust
   INNER JOIN Transaction_Attributes_Extended tae
   ON cust.amperity_id=tae.amperity_id

.. queries-example-revenue-opportunity-1-group-end


.. _queries-example-revenue-opportunity-many-groups:

Revenue opportunity, many groups
--------------------------------------------------

.. queries-example-revenue-opportunity-many-groups-start

Use the following example to size revenue opportunity for multiple groups, such as moving from "one-and-done" to "repeat purchaser". This query is most effective when run against the **Transaction Attributes Extended** table, but may be useful when run against other tables. Customize the **WITH** statement to define a list of fields to be used for comparing movements between groups. Customize the main **SELECT** statement to define the time periods for which this movement will be measured.

.. code-block:: sql
   :linenos:

   WITH customers AS (
     SELECT
       amperity_id
       ,multi_purchase_channel
     FROM Transaction_Attributes_Extended
   )

   SELECT
     cust.multi_purchase_channel
     ,COUNT(DISTINCT tae.amperity_id) AS num_customers
     ,AVG(lifetime_average_order_value) AS lt_aov
     ,AVG(L12M_average_order_value) AS l12m_aov
     ,AVG(lifetime_order_revenue) AS lt_rev
     ,AVG(l12m_order_revenue) AS l12m_rev
     ,AVG(lifetime_average_item_price) AS lt_aur
     ,AVG(l12m_average_item_price) AS l12m_aur
     ,AVG(lifetime_order_frequency) AS avg_lt_orders
     ,AVG(l12m_order_frequency) AS avg_l12m_orders
     ,SUM(l12m_order_revenue) AS total_l12m_revenue
   FROM customers cust
   INNER_JOIN Transaction_Attributes_Extended tae
   ON cust.amperity_id=tae.amperity_id
   GROUP BY 1

.. queries-example-revenue-opportunity-many-groups-end


.. _queries-example-top-20-percent-revenue:

Top 20% revenue during previous year
--------------------------------------------------

.. include:: ../../amperity_user/source/usecase_customers_top20_revenue.rst
   :start-after: .. usecase-customers-top-20-revenue-start
   :end-before: .. usecase-customers-top-20-revenue-end

.. queries-example-top-20-percent-revenue-start

The following example returns your top 20 percent of customers by revenue:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,L12M_monetary
   FROM Transaction_Attributes_Extended
   WHERE L12M_monetary >= 9

.. queries-example-top-20-percent-revenue-end


.. _queries-example-totals-by-brand:

Totals by brand
--------------------------------------------------

.. queries-example-totals-by-brand-start

Use the **SUM()** function to build totals for quantity, returns, and revenue:

* :ref:`queries-example-total-quantity-by-brand`
* :ref:`queries-example-total-returns-by-brand`
* :ref:`queries-example-total-revenue-by-brand`

.. queries-example-totals-by-brand-end


.. _queries-example-total-quantity-by-brand:

Total quantity by brand
++++++++++++++++++++++++++++++++++++++++++++++++++

.. queries-example-total-quantity-by-brand-start

Use the **SUM()** function to return total quantity by brand, and then sort in descending order:

.. code-block:: sql
   :linenos:

   SELECT
     purchase_brand
     ,SUM(order_quantity) AS total_quantity
   FROM Unified_Transactions
   GROUP BY 1
   ORDER BY 1 DESC

.. queries-example-total-quantity-by-brand-end


.. _queries-example-total-returns-by-brand:

Total returns by brand
++++++++++++++++++++++++++++++++++++++++++++++++++

.. queries-example-total-returns-by-brand-start

Use the **SUM()** function to return total returns by brand, and then sort in descending order:

.. code-block:: sql
   :linenos:

   SELECT
     purchase_brand
     ,SUM(order_returned_revenue) AS total_returns
   FROM Unified_Transactions
   GROUP BY 1
   ORDER BY 1 DESC

.. queries-example-total-returns-by-brand-end


.. _queries-example-total-revenue-by-brand:

Total revenue by brand
++++++++++++++++++++++++++++++++++++++++++++++++++

.. queries-example-total-revenue-by-brand-start

Use the **SUM()** function to return total revenue by brand, and then sort in descending order:

.. code-block:: sql
   :linenos:

   SELECT
     purchase_brand
     ,SUM(order_revenue) AS total_revenue
   FROM Unified_Transactions
   GROUP BY 1
   ORDER BY 1 DESC

.. queries-example-total-revenue-by-brand-end


.. _queries-example-transactions-by-day:

Transactions by day
--------------------------------------------------

.. queries-example-transactions-by-day-start

Use the following example to generate a breakdown of customer and order metrics by day. This query must be run against the **Unified Transactions** table. Export the results of this query to BI tools like Tableau or desktop tools like Google Sheets or Microsoft Excel.

.. code-block:: sql
   :linenos:

   SELECT
     DATE(order_datetime) AS day_of_order
     ,purchase_brand
     ,purchase_channel
     ,SUM(order_revenue) AS total_revenue
     ,AVG(order_revenue) AS aov
     ,COUNT(DISTINCT order_id) AS orders
     ,COUNT(DISTINCT amperity_id) AS customers
     ,SUM(order_quantity) AS total_items
     ,AVG(order_quantity) AS avg_items
     ,SUM(order_returned_revenue) AS total_returned_revenue
   FROM Unified_Transactions
   GROUP BY 1,2,3
   ORDER BY 1,2,3

.. queries-example-transactions-by-day-end
