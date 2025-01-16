.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Configure and manage the Unified Scores table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Scores table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Scores table

==================================================
Unified Scores table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-scores-table-start
   :end-before: .. term-unified-scores-table-end

.. table-unified-scores-added-start

The **Unified Scores** table is added to databases in the **Customer 360** page when:

#. The Stitch QA database is added using the "Stitch QA" database template.
#. A customer 360 database is added using the "Customer 360" database template.
#. A table is added to a custom database using the **Unified Scores** table as |database_add_passthrough|.

.. table-unified-scores-added-end


.. _table-unified-scores-use-with-stitch-qa:

Use with Stitch QA
==================================================

.. table-unified-scores-use-with-stitch-qa-start

The **Unified Scores** table is the foundation for the **Detailed Examples** table in the Stitch QA database, which is the starting point for any quality review of Stitch output and is an important part of the Stitch QA workflow.

.. table-unified-scores-use-with-stitch-qa-end


.. _table-unified-scores-use-with-customer-360:

Use with Customer 360
==================================================

.. table-unified-scores-use-with-customer-360-start

The **Unified Scores** table enables using the Amperity ID to discover information about how groups of records were scored and to verify those scores against other data points.

.. important:: The **Unified Scores** table should not be used outside of the **Customer 360** page. It should not be used to build queries or segments or be configured to send data to downstream workflows.

.. table-unified-scores-use-with-customer-360-end


.. _table-unified-scores-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-scores-table-about-start
   :end-before: .. data-tables-unified-scores-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-scores-table-start
   :end-before: .. data-tables-unified-scores-table-end
