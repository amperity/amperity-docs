.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Unified Customer table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Customer table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Customer table

==================================================
Unified Customer table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-customers-table-start
   :end-before: .. term-unified-customers-table-end


.. _table-unified-customers-add:

Add table
==================================================

.. table-unified-customers-add-start

The **Unified Customer** table is a required table for the customer 360 database and is always built as a passthrough table from Stitch output.

.. table-unified-customers-add-end

.. table-unified-customers-add-important-start

.. important:: This table is added automatically when the "Customer 360" template is used to add the customer 360 database. Using a template is the recommended way to add the **Unified Customer** table.

.. table-unified-customers-add-important-end

**To add the Unified Customer table**

.. table-unified-customers-add-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Unified_Customer".
#. Set the build mode to **Passthrough**.
#. From the **Source Table** dropdown, select the **Unified Customer** table.
#. Click **Next**.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Verify that semantic tags--**given_name**, **surname**, **email**, **phone**, **address**, **city**, **state**, **postal**, **birthdate**, **gender**, etc.--were applied to all PII fields correctly.

   .. tip:: You can clear incorrectly tagged semantics individually or for the entire table. To clear semantic tags for the entire table, under **Semantic Suggestions** click **Clear semantics**.
#. From the **Table Semantics** dropdown, select **Unified Customer**.
#. Click **Save**.

.. table-unified-customers-add-steps-end


.. _table-unified-customers-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-customers-table-about-start
   :end-before: .. data-tables-unified-customers-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-customers-table-start
   :end-before: .. data-tables-unified-customers-table-end
