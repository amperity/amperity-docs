.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Unified Itemized Transactions table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Itemized Transactions table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Itemized Transactions table

==================================================
Unified Itemized Transactions table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-itemized-transactions-table-start
   :end-before: .. term-unified-itemized-transactions-table-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-itemized-transactions-example-start
   :end-before: .. data-tables-unified-itemized-transactions-example-end

.. image:: ../../images/data_table_example_uit.png
   :width: 640 px
   :alt: An example of the Unified Itemized Transactions data table.
   :align: left
   :class: no-scaled-link

.. table-unified-itemized-transactions-table-group-links-start

.. important:: Database tables for transactions must be configured in the following order:

   #. Unified Itemized Transactions
   #. :doc:`Unified Transactions <table_unified_transactions>`
   #. :doc:`Transaction Attributes Extended <table_transaction_attributes_extended>`

   The :doc:`Unified Product Catalog <table_unified_product_catalog>` table is optional and may be configured for use with building queries, database tables, and other non-audience workflows. Your brand's product catalog must be integrated into the **Unified Itemized Transactions** table before you can use product catalog attributes to build audiences, segments, and campaigns.

.. table-unified-itemized-transactions-table-group-links-end


.. _table-unified-itemized-transactions-add:

Add table
==================================================

.. table-unified-itemized-transactions-add-start

The **Unified Itemized Transactions** table is a required table for the customer 360 database when transactions are available to your tenant and fields have been tagged with **txn-items/** semantic tags. The **Unified Itemized Transactions** table is built from Stitch output and is added automatically.

.. table-unified-itemized-transactions-add-end


.. _table-unified-itemized-transactions-product-catalog-table:

Define product catalog
==================================================

Your brand's product catalog must be joined to the **Unified Itemized Transactions** table to enable the use of product catalog attributes when building audiences for use with segments and campaigns.

If your brand used the **txn-items/** group of semantics to apply tags to fields that define your product catalog, this step happens automatically. If your brand used the **pc/** group of semantics, you will need to use SQL to **LEFT JOIN** your product catalog to the **Unified Itemized Transactions** table to enable their use within segments and campaigns.

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-product-catalog-table-with-ampiq-start
   :end-before: .. term-unified-product-catalog-table-with-ampiq-end


.. _table-unified-itemized-transactions-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-itemized-transactions-table-about-start
   :end-before: .. data-tables-unified-itemized-transactions-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-itemized-transactions-table-start
   :end-before: .. data-tables-unified-itemized-transactions-table-end
