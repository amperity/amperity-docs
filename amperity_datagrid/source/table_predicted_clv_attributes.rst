.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Configure and manage the Predicted CLV Attributes table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Predicted CLV Attributes table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predicted CLV Attributes table

==================================================
Predicted CLV Attributes table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-predicted-clv-attributes-table-start
   :end-before: .. term-predicted-clv-attributes-table-end

.. table-predicted-clv-attributes-note-start

.. note:: The size of the **Predicted CLV Attributes** table in your tenant is based on the number of Amperity IDs.

.. table-predicted-clv-attributes-note-end


.. _table-predicted-clv-attributes-add:

Add table
==================================================

.. table-predicted-clv-attributes-add-start

Add the **Predicted CLV Attributes** table to the customer 360 database.

.. table-predicted-clv-attributes-add-end


.. _table-predicted-clv-attributes-add-as-sql:

as a SQL table
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-sql-360-table-start
   :end-before: .. term-sql-360-table-end

.. table-predicted-clv-attributes-add-as-sql-start

The **Days Since Last Order** and **Historical Order Frequency Lifetime** columns in the **Predicted CLV Attributes** table are not recommended for use with segmentation or for downstream workflows. Use SQL to build a predicted attributes table for use in the customer 360 database that omits these columns.

.. table-predicted-clv-attributes-add-as-sql-end

**To add the Predicted CLV Attributes table as a SQL table**

.. table-predicted-clv-attributes-add-as-sql-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Set **Build Mode** to "SQL", and then use a **SELECT** statement similar to the following to define the schema:

   .. code-block:: sql

      SELECT
        amperity_id AS `amperity_id`
        ,predicted_average_order_revenue_next_365d AS `average_revenue_365`
        ,predicted_clv_next_365d AS `clv_365`
        ,predicted_customer_lifecycle_status AS `purchase_likelihood`
        ,predicted_customer_lifetime_value_tier AS `value_tier`
        ,predicted_order_frequency_next_365d AS `predicted_orders_365`
        ,predicted_probability_of_transaction_next_365d AS `purchase_probability`
      FROM Predicted_CLV_Attributes

#. Hide the table from the **Visual Segment Editor** by verifying that **Show in VSE?** is unselected.
#. Click **Activate** to update the customer 360 database with your changes.

.. table-predicted-clv-attributes-add-as-sql-steps-end


.. _table-predicted-clv-attributes-add-as-passthrough:

as a passthrough table
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-passthrough-360-table-start
   :end-before: .. term-passthrough-360-table-end

**To add the Predicted CLV Attributes table as a passthrough table**

.. table-predicted-clv-attributes-add-as-passthrough-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for a database, and then click **Edit**.
#. Click **Add Table**.
#. Set **Build Mode** to "Passthrough", and then select the **Predicted CLV Attributes** table from the drop-down menu.
#. Hide the table from the **Visual Segment Editor** by verifying that **Show in VSE?** is unselected.
#. Click **Activate** to update the customer 360 database with your changes.

.. table-predicted-clv-attributes-add-as-passthrough-steps-end


.. _table-predicted-clv-attributes-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-predicted-clv-attributes-table-about-start
   :end-before: .. data-tables-predicted-clv-attributes-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-predicted-clv-attributes-table-start
   :end-before: .. data-tables-predicted-clv-attributes-table-end
