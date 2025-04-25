.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Unified Coalesced table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Coalesced table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Coalesced table

==================================================
Unified Coalesced table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-coalesced-table-start
   :end-before: .. term-unified-coalesced-table-end

.. table-unified-coalesced-added-start

The **Unified Coalesced** table is added to databases in the **Customer 360** page when:

#. The Stitch QA database is added using the "Stitch QA" database template.
#. A customer 360 database is added using the "Customer 360" database template.
#. A table is added to a custom database using the **Unified Coalesced** table as |database_add_passthrough|.

.. table-unified-coalesced-added-end


.. _table-unified-coalesced-use-with-stitch-qa:

Use with Stitch QA
==================================================

.. table-unified-coalesced-use-with-stitch-qa-start

Use the **Unified Coalesced** table as part of the Stitch QA process to:

* Ensure semantic tags are selected and visible to the **Queries** page
* Investigate relationships between records, especially when records appear to be assigned (not assigned) to an incorrect (correct) Amperity ID, which defines a single cluster of records
* Investigate blocklisted values

.. table-unified-coalesced-use-with-stitch-qa-end

.. include:: ../../amperity_operator/source/qa_stitch.rst
   :start-after: .. qa-stitch-enable-steps-add-database-tables-uc-and-upr-start
   :end-before: .. qa-stitch-enable-steps-add-database-tables-uc-and-upr-end


.. _table-unified-coalesced-use-with-stitch-qa-tags-keys:

Profile semantics and foreign keys
--------------------------------------------------

.. TODO: This section is identical in both **Unified Coalesced** and **Unified Preprocessing Raw** topics. They share an overlapping workflow, but should be tracked to discover if there are unique aspects that would lead these sections to evolve independently.

.. table-unified-coalesced-use-with-stitch-qa-tags-keys-start

Use the **Customer 360** page to verify that rows with profile semantic tags and foreign keys are selected to be available to the **Queries** page. Has the list of profile and/or foreign key semantics changed since the last time you have performed Stitch QA? This will occur when a data source is added that requires a new foreign key *or* in a situation where one of the less frequently used profile semantic tags is applied to a new data source.

Open the table in the **Database Explorer** and verify that all rows in the table that are associated with a semantic tag or a foreign key have a checkmark in the left column. Rows without a checkmark will not make the associated **FIELD** available to the **Queries** page. If rows do not have a checkmark, edit the table and apply the checkmark, save the table, activate the Stitch QA database, and then run the database to refresh the table.

.. table-unified-coalesced-use-with-stitch-qa-tags-keys-end


.. _table-unified-coalesced-use-with-stitch-qa-relationships-records:

Relationships between records
--------------------------------------------------

.. TODO: This section is identical in both **Unified Coalesced** and **Unified Preprocessing Raw** topics. They share an overlapping workflow, but should be tracked to discover if there are unique aspects that would lead these sections to evolve independently.

.. table-unified-coalesced-use-with-stitch-qa-relationships-records-start

Use the **Queries** page to investigate unexpected relationships between individual records that share the same Amperity ID and to investigate why records that look like they *should* belong to the same cluster of records were split.

Use a combination of the **Unified Coalesced** and **Unified Preprocessed Raw** tables to review the data that is associated with these records to help understand why groups of records were matched or why certain records were assigned to a cluster.

In some cases, you may need to investigate and compare entire clusters to better understand why (or why not) these groups of records were maintained (or split) during hierarchical comparison, a step in the Stitch process that occurs *after* pairwise comparison and scoring.

.. table-unified-coalesced-use-with-stitch-qa-relationships-records-end


.. _table-unified-coalesced-use-with-stitch-qa-blocklist-values:

Global blocklist values
--------------------------------------------------

.. TODO: This section is identical in both **Unified Coalesced** and **Unified Preprocessing Raw** topics. They share an overlapping workflow, but should be tracked to discover if there are unique aspects that would lead these sections to evolve independently.

.. table-unified-coalesced-use-with-stitch-qa-blocklist-values-start

The **Unified Coalesced** table provides additional data about individual records, such as blocklisted values, component IDs, or if a record belongs to a supersized cluster.

In some cases, groups of records may have values removed by the global bad-values blocklist instead of the tenant-specific bad-values blocklist.

Compare records in the **Unified Coalesced** table to records in the **Unified Preprocessed Raw** table to identify which values were removed.

.. table-unified-coalesced-use-with-stitch-qa-blocklist-values-end


.. _table-unified-coalesced-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-coalesced-table-about-start
   :end-before: .. data-tables-unified-coalesced-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-coalesced-table-start
   :end-before: .. data-tables-unified-coalesced-table-end
