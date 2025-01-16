.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Configure and manage the Transaction Attributes table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Transaction Attributes table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Transaction Attributes table

==================================================
Transaction Attributes table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-transaction-attributes-table-start
   :end-before: .. term-transaction-attributes-table-end

.. table-transaction-attributes-table-group-links-start

.. important:: Database tables for transactions must be configured in the following order:

   #. :doc:`Unified Itemized Transactions <table_unified_itemized_transactions>`
   #. :doc:`Unified Transactions <table_unified_transactions>`
   #. :doc:`Transaction Attributes Extended <table_transaction_attributes_extended>`
   #. Transaction Attributes (this topic)

   The :doc:`Unified Product Catalog <table_unified_product_catalog>` table is optional and may be configured for use with building queries, database tables, and other non-audience workflows. Your brand's product catalog must be integrated into the **Unified Itemized Transactions** table before you can use product catalog attributes to build audiences, segments, and campaigns.

.. table-transaction-attributes-table-group-links-end


.. _table-transaction-attributes-add:

Add table
==================================================

.. table-transaction-attributes-add-start

The **Transaction Attributes** table is a required table for the customer 360 database and is added using a SQL template.

.. table-transaction-attributes-add-end

**To add the Transaction Attributes table**

.. table-transaction-attributes-add-steps-start

#. Open your customer 360 database in edit mode, and then click **Add Table**.
#. Name the table "Transaction_Attributes" (with underscores).
#. Set the build mode to **SQL**, and then select "Transaction Attributes" from the **Apply template** drop-down.
#. Click **Next** to validate the SQL.
#. Select "Transaction Attributes" from the **Table Semantics** drop-down, and then add a description for the table. (The description is available as a tooltip in other locations in Amperity.
#. Click **Save**.

.. table-transaction-attributes-add-steps-end


.. _table-transaction-attributes-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-table-about-start
   :end-before: .. data-tables-transaction-attributes-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-table-start
   :end-before: .. data-tables-transaction-attributes-table-end
