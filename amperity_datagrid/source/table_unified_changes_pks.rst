.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Configure and manage the Unified Changes PKS (primary keys) table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Changes PKS (primary keys) table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Changes PKS table

==================================================
Unified Changes PKS table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-changes-pks-table-start
   :end-before: .. term-unified-changes-pks-table-end

.. table-unified-changes-pks-automatically-added-start

The **Unified Changes PKS** table is automatically added to the Stitch QA database as a passthrough table when it is generated using the "Stitch QA" database template.

.. table-unified-changes-pks-automatically-added-end

.. table-unified-changes-pks-thirty-days-start

.. note:: Thirty days of history are stored by default for the **Unified Changes Clusters** and **Unified Changes PKS** tables. This :ref:`number of days <configure-stitch-general-performance-history>` is configurable.

.. table-unified-changes-pks-thirty-days-end


.. _table-unified-changes-pks-use-with-stitch-qa:

Use with Stitch QA
==================================================

.. table-unified-changes-pks-use-with-stitch-qa-start

Use the **Unified Changes PKS** table as part of the Stitch QA process to compare the previous state of primary keys to the current state and understand why a primary key was added, deleted, reassigned, or updated.

.. table-unified-changes-pks-use-with-stitch-qa-end


.. _table-unified-changes-pks-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-changes-pks-table-about-start
   :end-before: .. data-tables-unified-changes-pks-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-changes-pks-table-start
   :end-before: .. data-tables-unified-changes-pks-table-end
