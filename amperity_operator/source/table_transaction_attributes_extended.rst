.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Transaction Attributes Extended table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Transaction Attributes Extended table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Transaction Attributes Extended table

==================================================
Transaction Attributes Extended table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-transaction-attributes-extended-table-start
   :end-before: .. term-transaction-attributes-extended-table-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-start
   :end-before: .. data-tables-transaction-attributes-extended-end

.. table-transaction-attributes-extended-table-group-links-start

.. important:: Database tables for transactions must be configured in the following order:

   #. :doc:`Unified Itemized Transactions <table_unified_itemized_transactions>`
   #. :doc:`Unified Transactions <table_unified_transactions>`
   #. Transaction Attributes Extended

   The :doc:`Unified Product Catalog <table_unified_product_catalog>` table is optional and may be configured for use with building queries, database tables, and other non-audience workflows. Your brand's product catalog must be integrated into the **Unified Itemized Transactions** table before you can use product catalog attributes to build audiences, segments, and campaigns.

.. table-transaction-attributes-extended-table-group-links-end

.. table-transaction-attributes-extended-important-start

.. important:: Many columns in the **Transaction Attributes Extended** table enable specific features within Amperity, such as segment insights, predictive scoring, and churn prevention campaigns.

   Any column that exists in the :ref:`column reference <table-transaction-attributes-extended-reference>` must maintain the exact column name and data type, even if your tenant requires custom SQL to enable the feature.

   The **l12m_order_revenue**, **l12m_order_frequency** and **l12m_total_items** attributes must not be renamed. These attributes populate the **Revenue tree** and **Historical revenue** cards on the segment summary page.

   This table may be extended to support additional use cases. The implementations for these types of use cases are always tenant-specific, but should follow a similar approach as :ref:`optional <table-transaction-attributes-extended-extend-attributes>` extensions. Custom fields are not used by segment insights and predictive scoring, but may be added to the **Transaction Attributes Extended** table.

.. table-transaction-attributes-extended-important-end


.. _table-transaction-attributes-extended-add:

Add table
==================================================

.. table-transaction-attributes-extended-add-start

The **Transaction Attributes Extended** table is a required table for the customer 360 database and is added using a SQL template.

.. table-transaction-attributes-extended-add-end

**To add the Transaction Attributes Extended table**

.. table-transaction-attributes-extended-add-steps-start

#. Open your customer 360 database in edit mode, and then click **Add Table**.
#. Name the table "Transaction_Attributes_Extended" (with underscores).
#. Set the build mode to **SQL**, and then select "Transaction Attributes Extended" from the **Apply template** dropdown.
#. Review the :ref:`list of optional attributes <table-transaction-attributes-extended-extend-attributes>` to determine if any of those should be enabled for your tenant.
#. Click **Next** to validate the SQL.
#. Select "Transaction Attributes Extended" from the **Table Semantics** dropdown, and then add a description for the table. (The description is available as a tooltip in other locations in Amperity.
#. Click **Save**.

.. table-transaction-attributes-extended-add-steps-end


.. _table-transaction-attributes-extended-extend-attributes:

Optional attributes
==================================================

.. table-transaction-attributes-extended-extend-attributes-start

You can extend the set of attributes that are available from the **Transaction Attributes Extended** table to include any of the following:

* :ref:`table-transaction-attributes-extended-extend-attributes-cancellations`
* :ref:`table-transaction-attributes-extended-extend-attributes-net-order-revenue`
* :ref:`table-transaction-attributes-extended-extend-attributes-order-costs`
* :ref:`table-transaction-attributes-extended-extend-attributes-returns`
* :ref:`table-transaction-attributes-extended-extend-attributes-rfm`

.. note:: These attributes are built into the SQL templates for the **Transaction Attributes Extended** table, but are commented out. Some sets of attributes require updates be made to both tables, while others may only require updates be made to one table. The steps for each set will link to a topic section that descibes the updates that should be made to the **Unified Transactions** table.

.. table-transaction-attributes-extended-extend-attributes-end


.. _table-transaction-attributes-extended-extend-attributes-cancellations:

Cancellations
--------------------------------------------------

.. table-transaction-attributes-extended-extend-attributes-cancellations-start

You can extend the **Unified Itemized Transactions** table to show intervals for the frequency at which orders were canceled, the amount of revenue that was canceled, and the total number of items that were canceled.

.. table-transaction-attributes-extended-extend-attributes-cancellations-end

**To add extended attributes for canceled items**

.. table-transaction-attributes-extended-extend-attributes-cancellations-steps-start

#. Open the **Transaction Attributes Extended** table in the SQL editor.
#. Uncomment the **augmented_cancellations** block of SQL.
#. Uncomment the **can_attrs** block of SQL.
#. Find the **SELECT** statement at the end of the SQL template, and then uncomment the following sets of calculated intervals:

   * **Order Canceled Frequency** include 30 days, 3 months, 6 months, 12 months, 12-24 months, and lifetime.
   * **Order canceled Revenue** include 30 days, 3 months, 6 months, 12 months, 12-24 months, and lifetime.
   * **Total canceled Items** include 30 days, 3 months, 6 months, 12 months, 12-24 months, and lifetime.

   .. note:: These attributes are not grouped together within the **SELECT** statement.

#. Uncomment the **LEFT JOIN** at the end of the **SELECT** statement:

   .. code-block:: sql

      LEFT JOIN can_attrs ON attrs.amperity_id = can_attrs.amperity_id

#. Validate the SQL, and then click **Next**, and then click **Save**.

.. table-transaction-attributes-extended-extend-attributes-cancellations-steps-end


.. _table-transaction-attributes-extended-extend-attributes-net-order-revenue:

Net order revenue
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-net-order-revenue-start
   :end-before: .. term-net-order-revenue-end

**To add extended attributes for net order revenue**

.. table-transaction-attributes-extended-extend-attributes-net-order-revenue-steps-start

#. Required. :ref:`Add Net Order Revenue to the Unified Transactions table <table-unified-transactions-extend-attributes-net-order-revenue>`.
#. Open the **Transaction Attributes Extended** table in the SQL editor.
#. Find the section named "attrs", which contains a series of commented-out extended attributes for net order revenue.
#. Uncomment one or more of the following extended attributes:

   .. code-block:: sql
      :linenos:

      ,FIRST(txn.first_order.net_order_revenue IGNORE NULLS) AS first_net_order_revenue
      ,FIRST(txn.second_order.net_order_revenue IGNORE NULLS) AS second_net_order_revenue
      ,FIRST(txn.latest_order.net_order_revenue IGNORE NULLS) AS latest_net_order_revenue
      ,MAX(IF(txn.net_order_revenue > 0, txn.net_order_revenue, NULL)) AS lifetime_largest_net_order_value
      ,SUM(txn.net_order_revenue) AS lifetime_net_order_revenue
      ,SUM(IF(txn.ly12m, txn.net_order_revenue, 0)) AS LY12M_net_order_revenue
      ,SUM(IF(txn.l12m, txn.net_order_revenue, 0)) AS L12M_net_order_revenue
      ,SUM(IF(txn.l30d, txn.net_order_revenue, 0)) AS L30D_net_order_revenue
      ,SUM(IF(txn.l3m, txn.net_order_revenue, 0)) AS L3M_net_order_revenue
      ,SUM(IF(txn.l6m, txn.net_order_revenue, 0)) AS L6M_net_order_revenue

   .. note:: These attributes are grouped together within the "attrs" section.

#. Find the **SELECT** statement at the end of the SQL template, and then uncomment the following sets of calculated intervals:

   * **Average Net Item Price** include 30 days, 3 months, 6 months, 12 months, 12-24 months, and lifetime.
   * **Largest Net Order Value** includes lifetime.
   * **Net Order Revenue** include first, latest, and second orders along with 12-24 months and lifetime.
   * **Net Order Value** include 30 days, 3 months, 6 months, 12 months, 12-24 months, and lifetime.

   .. note:: These attributes are not grouped together within the **SELECT** statement.

#. Validate the SQL, and then click **Next**.
#. Click **Save**.

.. table-transaction-attributes-extended-extend-attributes-net-order-revenue-steps-end


.. _table-transaction-attributes-extended-extend-attributes-order-costs:

Order costs
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-cost-start
   :end-before: .. term-order-cost-end

**To add extended attributes for order cost**

.. table-transaction-attributes-extended-extend-attributes-order-costs-steps-start

#. Required. :ref:`Add Order Cost to the Unified Transactions table <table-unified-transactions-extend-attributes-order-costs>`.
#. Open the **Transaction Attributes Extended** table in the SQL editor.
#. Find the section named "attrs", which contains a series of commented-out extended attributes for order costs.
#. Uncomment one or more of the following extended attributes:

   .. code-block:: sql
      :linenos:

      ,FIRST(txn.first_order.order_cost IGNORE NULLS) AS first_order_cost
      ,FIRST(txn.latest_order.order_cost IGNORE NULLS) AS latest_order_cost
      ,FIRST(txn.second_order.order_cost IGNORE NULLS) AS second_order_cost
      ,SUM(IF(txn.l30d, txn.order_cost, 0)) AS L30D_order_cost
      ,SUM(IF(txn.l3m, txn.order_cost, 0)) AS L3M_order_cost
      ,SUM(IF(txn.l6m, txn.order_cost, 0)) AS L6M_order_cost
      ,SUM(IF(txn.l12m, txn.order_cost, 0)) AS L12M_order_cost
      ,SUM(IF(txn.ly12m, txn.order_cost, 0)) AS LY12M_order_cost
      ,SUM(txn.order_cost) AS lifetime_order_cost

   .. note:: These attributes are grouped together within the "attrs" section.

#. Find the **SELECT** statement at the end of the SQL template, and then for each of the attributes enabled within "attrs", uncomment the line to add the extended attribute to the **Transaction Attributes Extended** table:

   .. code-block:: sql
      :linenos:

      ,CAST(attrs.first_order_cost AS decimal(38,2)) AS first_order_cost
      ,CAST(attrs.latest_order_cost AS decimal(38,2)) AS latest_order_cost
      ,CAST(attrs.second_order_cost AS decimal(38,2)) AS second_order_cost
      ,CAST(attrs.L30d_order_cost AS decimal(38,2))
      ,CAST(attrs.l3m_order_cost AS decimal(38,2))
      ,CAST(attrs.l6m_order_cost AS decimal(38,2))
      ,CAST(attrs.l12m_order_cost AS decimal(38,2))
      ,CAST(attrs.ly12m_order_cost AS decimal(38,2))
      ,CAST(attrs.lifetime_order_cost AS decimal(38,2))

   .. note:: These attributes are not grouped together within the **SELECT** statement.

#. Validate the SQL, and then click **Next**.
#. Click **Save**.

.. table-transaction-attributes-extended-extend-attributes-order-costs-steps-end


.. _table-transaction-attributes-extended-extend-attributes-returns:

Returns
--------------------------------------------------

.. table-transaction-attributes-extended-extend-attributes-returns-start

You can extend the **Unified Itemized Transactions** table to show intervals for the frequency at which orders were returned, the amount of revenue that was returned, and the total number of items that were returned.

.. table-transaction-attributes-extended-extend-attributes-returns-end

**To add extended attributes for returned items**

.. table-transaction-attributes-extended-extend-attributes-returns-steps-start

#. Open the **Transaction Attributes Extended** table in the SQL editor.
#. Uncomment the **augmented_returns** block of SQL.
#. Uncomment the **ret_attrs** block of SQL.
#. Find the **SELECT** statement at the end of the SQL template, and then uncomment the following sets of calculated intervals:

   * **Order Returned Frequency** include 30 days, 3 months, 6 months, 12 months, 12-24 months, and lifetime.
   * **Order Returned Revenue** include 30 days, 3 months, 6 months, 12 months, 12-24 months, and lifetime.
   * **Total Returned Items** include 30 days, 3 months, 6 months, 12 months, 12-24 months, and lifetime.

   .. note:: These attributes are not grouped together within the **SELECT** statement.

#. Uncomment the **LEFT JOIN** at the end of the **SELECT** statement:

   .. code-block:: sql

      LEFT JOIN ret_attrs ON attrs.amperity_id = ret_attrs.amperity_id

#. Validate the SQL, and then click **Next**, and then click **Save**.

.. table-transaction-attributes-extended-extend-attributes-returns-steps-end


.. _table-transaction-attributes-extended-extend-attributes-rfm:

RFM
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-rfm-start
   :end-before: .. term-rfm-end

**To add extended attributes for RFM**

.. table-transaction-attributes-extended-extend-attributes-rfm-steps-start

#. Open the **Transaction Attributes Extended** table in the SQL editor.
#. Uncomment the **l12m_rfm** block of SQL. Use the **NTILE()** function to calculate recency, frequency, and monetary scores as deciles.
#. In the **attrs** block of SQL, uncomment the calculations for RFM attributes:

   .. code-block:: sql
      :linenos:

      ,FIRST(rfm.recency) AS L12M_recency
      ,FIRST(rfm.frequency) AS L12M_frequency
      ,FIRST(rfm.monetary) AS L12M_monetary
      ,FIRST(rfm.score) AS L12M_rfm_score

   and then uncomment the **LEFT JOIN** in the same section:

   .. code-block:: sql

      LEFT JOIN l12m_rfm rfm ON txn.amperity_id = rfm.amperity_id

#. Find the **SELECT** statement at the end of the SQL template, and then uncomment the following extended attributes:

   .. code-block:: sql
      :linenos:

      ,attrs.L12M_rfm_score
      ,attrs.L12M_recency
      ,attrs.L12M_frequency
      ,attrs.L12M_monetary

#. Validate the SQL, and then click **Next**, and then click **Save**.

.. table-transaction-attributes-extended-extend-attributes-rfm-steps-end


.. _table-transaction-attributes-extended-reference:

Column reference
==================================================

.. transaction-attributes-extended-start

Extended transaction attributes are presented as a single table with many columns, including an Amperity ID, and fit into the following categories:

* :ref:`Customer flags <table-transaction-attributes-extended-reference-customer-flags>`
* :ref:`Customer orders <table-transaction-attributes-extended-reference-customer-orders>`
* :ref:`Date differences <table-transaction-attributes-extended-reference-date-differences>`
* :ref:`Time period rollups <table-transaction-attributes-extended-reference-period-rollups>`
* :ref:`RFM <table-transaction-attributes-extended-reference-rfm>`

.. transaction-attributes-extended-end


.. _table-transaction-attributes-extended-reference-customer-flags:

Customer flags
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-customer-flags-start
   :end-before: .. data-tables-transaction-attributes-extended-customer-flags-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-customer-flags-table-start
   :end-before: .. data-tables-transaction-attributes-extended-customer-flags-table-end


.. _table-transaction-attributes-extended-reference-customer-orders:

Customer orders
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-customer-orders-start
   :end-before: .. data-tables-transaction-attributes-extended-customer-orders-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-customer-orders-table-start
   :end-before: .. data-tables-transaction-attributes-extended-customer-orders-table-end


.. _table-transaction-attributes-extended-reference-date-differences:

Date differences
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-date-differences-start
   :end-before: .. data-tables-transaction-attributes-extended-date-differences-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-date-differences-table-start
   :end-before: .. data-tables-transaction-attributes-extended-date-differences-table-start


.. _table-transaction-attributes-extended-reference-period-rollups:

Time period rollups
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-period-rollups-start
   :end-before: .. data-tables-transaction-attributes-extended-period-rollups-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-period-rollups-table-start
   :end-before: .. data-tables-transaction-attributes-extended-period-rollups-table-end


.. _table-transaction-attributes-extended-reference-rfm:

RFM
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-rfm-start
   :end-before: .. data-tables-transaction-attributes-extended-rfm-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-rfm-table-start
   :end-before: .. data-tables-transaction-attributes-extended-rfm-table-end
