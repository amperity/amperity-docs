.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Unified Loyalty table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Loyalty table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Loyalty table

==================================================
Unified Loyalty table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-loyalty-table-start
   :end-before: .. term-unified-loyalty-table-end

.. table-unified-loyalty-note-multiple-loyalty-ids-start

.. note:: An Amperity ID may be associated with multiple loyalty programs or may be associated with multiple accounts within the same loyalty program.

.. table-unified-loyalty-note-multiple-loyalty-ids-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-loyalty-profiles-make-available-to-stitch-start
   :end-before: .. semantics-loyalty-profiles-make-available-to-stitch-end


.. _table-unified-loyalty-add:

Add table
==================================================

.. table-unified-loyalty-add-start

The **Unified Loyalty** table is an optional table for the customer 360 database. It may be built as a passthrough table.

.. table-unified-loyalty-add-end

**To add the Unified Loyalty table**

.. table-unified-loyalty-add-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Unified Loyalty".
#. Set the build mode to **Passthrough**.
#. From the **Source Table** dropdown, select the **Unified Loyalty** table.
#. Click **Next**.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. From the **Table Semantics** dropdown, select **Unified Loyalty**.
#. Under **Version History**, select **Enable table version history**.
#. Click **Save**.

.. table-unified-loyalty-add-steps-end


.. _table-unified-loyalty-examples:

Query examples
==================================================

.. table-unified-loyalty-examples-start

The following examples show how you can analyze retention rates and customer value for your loyalty program.

* :ref:`table-unified-loyalty-example-retention-analysis`
* :ref:`table-unified-loyalty-example-value-analysis`

.. tip:: Add these queries directly to your tenant from the **Queries** page. Click **Create**, select **Folder**, and then choose from the dropdown list **Analytics Reports**.

.. table-unified-loyalty-examples-end


.. _table-unified-loyalty-example-retention-analysis:

Retention analysis
--------------------------------------------------

.. table-unified-loyalty-example-retention-analysis-start

Use a query to analyze customer retention rates by loyalty status. The following example finds active members in your brand's loyalty program based on enrollment time, and then builds retention rates by:

* Churn for customers who belong to your brand's loyalty program vs. churn for customers who do not
* Differences by when customers joined the loyalty program
* Customer value differences among groups

.. code-block:: sql

   WITH loyalty_members AS (
     SELECT DISTINCT
       amperity_id
       ,CASE
         WHEN latest_opt_in_datetime > (current_date - interval '1' year)
         THEN 'Joined in Last Year'
         ELSE 'Joined Before Last Year'
       END enrollment_period
     FROM Unified_Loyalty
     WHERE is_opted_in
   )

   SELECT
     CASE
       WHEN loy.amperity_id IS NULL
       THEN 'Not in Loyalty'
       ELSE 'In Loyalty'
     END AS Loyalty_status
     ,enrollment_period
     ,CASE 			
       WHEN latest_order_datetime >= (current_date - interval '1' year)
       AND first_order_datetime < (current_date - interval '1' year)
       THEN 'Retained'
       WHEN latest_order_datetime <= (current_date - interval '1' year)
       THEN 'Churned'
       WHEN first_order_datetime >= (current_date - interval '1' year)
       THEN 'Acquired Last Year'			
     END AS retention_status
     ,COUNT(DISTINCT tae.amperity_id) AS number_of_customers
     ,1.00*COUNT(DISTINCT tae.amperity_id) / SUM(COUNT(DISTINCT tae.amperity_id)) OVER (PARTITION BY
       CASE
         WHEN loy.amperity_id IS NULL
         THEN 'Not in Loyalty'
         ELSE 'In Loyalty'
       END,
       enrollment_period
     ) AS pct_of_loyalty_status_and_enrollment_period
     ,SUM(l12m_order_revenue) AS L12m_revenue
     ,SUM(l12m_order_revenue) / COUNT(DISTINCT tae.amperity_id) AS L12M_revenue_per_customer
     ,1.00 * SUM(l12m_order_frequency) / COUNT(DISTINCT tae.amperity_id) AS L12M_orders_per_customer
     ,CASE
       WHEN SUM(l12m_order_frequency) = 0 THEN Null
       ELSE SUM(l12m_order_revenue) / SUM(l12m_order_frequency)
     END AS L12M_average_order_value
   FROM (
     SELECT *
     FROM Transaction_Attributes_Extended
     WHERE first_order_datetime > (current_date - interval '2' year)
   ) tae
   LEFT JOIN loyalty_members loy
   ON loy.amperity_id = tae.amperity_id
   GROUP BY 1,2,3
   ORDER BY 2,3,1

.. table-unified-loyalty-example-retention-analysis-end


.. _table-unified-loyalty-example-value-analysis:

Value analysis
--------------------------------------------------

.. table-unified-loyalty-example-value-analysis-start

Use a query to analyze customer value by loyalty status. The following example finds active members in your brand's loyalty program based on enrollment time, and then compares customer value by loyalty status and enrollment period by:

* Revenue by customer during the previous 12 months
* Orders by customer during the previous 12 months
* Average order value for all purchases in the previous 12 months

.. code-block:: sql

    WITH loyalty_members AS (
     SELECT DISTINCT
       amperity_id
       ,CASE
         WHEN latest_opt_in_datetime > (current_date - interval '1' year)
         THEN 'Joined in Last Year'
         ELSE 'Joined Before Last Year'
       END enrollment_period
     FROM Unified_Loyalty
     WHERE is_opted_in
   )

   SELECT
     CASE
       WHEN loy.amperity_id IS NULL
       THEN 'Not in Loyalty'
       ELSE 'In Loyalty'
     END AS Loyalty_status
     ,enrollment_period
     ,COUNT(DISTINCT tae.amperity_id) AS number_of_customers
     ,SUM(l12m_order_revenue) AS L12m_revenue
     ,SUM(l12m_order_revenue) / COUNT(DISTINCT tae.amperity_id) AS L12M_revenue_per_customer
     ,1.00 * SUM(l12m_order_frequency) / COUNT(DISTINCT tae.amperity_id) AS L12M_orders_per_customer
     ,SUM(l12m_order_revenue) / SUM(l12m_order_frequency) AS L12M_average_order_value
   FROM Transaction_Attributes_Extended tae
   LEFT JOIN loyalty_members loy
   ON loy.amperity_id=tae.amperity_id
   GROUP BY 1,2
   ORDER BY 1,2	

.. table-unified-loyalty-example-value-analysis-end


.. _table-unified-loyalty-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-loyalty-about-start
   :end-before: .. data-tables-unified-loyalty-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-loyalty-table-start
   :end-before: .. data-tables-unified-loyalty-table-end
