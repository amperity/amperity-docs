.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Unified Loyalty Events table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Loyalty Events table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Loyalty Events table

==================================================
Unified Loyalty Events table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-loyalty-events-table-start
   :end-before: .. term-unified-loyalty-events-table-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-loyalty-events-make-available-to-stitch-start
   :end-before: .. semantics-loyalty-events-make-available-to-stitch-end


.. _table-unified-loyalty-events-add:

Add table
==================================================

.. table-unified-loyalty-events-add-start

The **Unified Loyalty Events** table is an optional table for the customer 360 database. It may be built as a passthrough table.

.. table-unified-loyalty-events-add-end

**To add the Unified Loyalty Events table**

.. table-unified-loyalty-events-add-steps-start

#. From the **Customer 360** page, select the **Databases** tab, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Unified Loyalty Events".
#. Set the build mode to **Passthrough**.
#. From the **Source Table** dropdown, select the **Unified Loyalty Events** table.
#. Click **Next**.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. From the **Table Semantics** dropdown, select **Unified Loyalty Events**.
#. Under **Version History**, select **Enable table version history**.
#. Click **Save**.

.. table-unified-loyalty-events-add-steps-end


.. _table-unified-loyalty-events-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-loyalty-events-about-start
   :end-before: .. data-tables-unified-loyalty-events-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-loyalty-events-table-start
   :end-before: .. data-tables-unified-loyalty-events-table-end
