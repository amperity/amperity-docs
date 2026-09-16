.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Unified Product Catalog table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Product Catalog table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Product Catalog table

==================================================
Unified Product Catalog table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-product-catalog-table-start
   :end-before: .. term-unified-product-catalog-table-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-product-catalog-table-with-ampiq-start
   :end-before: .. term-unified-product-catalog-table-with-ampiq-end


.. _table-unified-product-catalog-add:

Add table
==================================================

.. table-unified-product-catalog-add-start

The **Unified Product Catalog** table is a required table for the customer 360 database when transactions and itemized transaction data is available to your tenant and fields are tagged with **pc/** semantic tags. The **Unified Product Catalog** table is built as a passthrough table.

.. table-unified-product-catalog-add-end

**To add the Unified Product Catalog table**

.. table-unified-product-catalog-add-steps-start

#. From the **Customer 360** page, select the **Databases** tab, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Unified_Product_Catalog".
#. Set the build mode to **Passthrough**.
#. From the **Source Table** dropdown, select the **Unified Product Catalog** table.
#. Click **Next**.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Verify that semantic tags were applied correctly.

   .. tip:: You can clear incorrectly tagged semantics individually or for the entire table. To clear semantic tags for the entire table, under **Semantic Suggestions** click **Clear semantics**.
#. From the **Table Semantics** dropdown, select **Unified Product Catalog**.
#. Click **Save**.

.. table-unified-product-catalog-add-steps-end


.. _table-unified-product-catalog-product-catalog-table:

Define product catalog
==================================================

.. include:: ../../amperity_operator/source/add_predicted_models.rst
   :start-after: .. add-predicted-models-product-catalog-start
   :end-before: .. add-predicted-models-product-catalog-end


.. _table-unified-product-catalog-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-product-catalog-table-about-start
   :end-before: .. data-tables-unified-product-catalog-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-product-catalog-table-start
   :end-before: .. data-tables-unified-product-catalog-table-end
