.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Unified Preprocessed Raw table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Preprocessed Raw table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Preprocessed Raw table

==================================================
Unified Preprocessed Raw table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-preprocessed-raw-table-start
   :end-before: .. term-unified-preprocessed-raw-table-end

.. table-unified-preprocessed-raw-automatically-added-start

The **Unified Preprocessed Raw** table is automatically added to the Stitch QA database as a passthrough table when it is generated using the "Stitch QA" database template.

.. table-unified-preprocessed-raw-automatically-added-end


.. _table-unified-preprocessed-raw-use-with-stitch-qa:

Use with Stitch QA
==================================================

.. table-unified-preprocessed-raw-use-with-stitch-qa-start

Use the **Unified Preprocessed Raw** table as part of the Stitch QA process to:

* Ensure semantic tags are selected and visible to the **Queries** page
* Investigate relationships between records, especially when records appear to be assigned (not assigned) to an incorrect (correct) Amperity ID, which defines a single cluster of records
* Investigate blocklisted values

.. table-unified-preprocessed-raw-use-with-stitch-qa-end

.. include:: ../../amperity_operator/source/qa_stitch.rst
   :start-after: .. qa-stitch-enable-steps-add-database-tables-uc-and-upr-start
   :end-before: .. qa-stitch-enable-steps-add-database-tables-uc-and-upr-end


.. _table-unified-preprocessed-raw-use-with-stitch-qa-tags-keys:

Profile semantics and foreign keys
--------------------------------------------------

.. TODO: This section is identical in both **Unified Coalesced** and **Unified Preprocessing Raw** topics. They share an overlapping workflow, but should be tracked to discover if there are unique aspects that would lead these sections to evolve independently.

.. table-unified-preprocessed-raw-use-with-stitch-qa-tags-keys-start

Use the **Customer 360** page to verify that rows with profile semantic tags and foreign keys are selected to be available to the **Queries** page. Has the list of profile and/or foreign key semantics changed since the last time you have performed Stitch QA? This will occur when a data source is added that requires a new foreign key *or* in a situation where one of the less frequently used profile semantic tags is applied to a new data source.

Open the table in the **Database Explorer** and verify that all rows in the table that are associated with a semantic tag or a foreign key have a checkmark in the left column. Rows without a checkmark will not make the associated **FIELD** available to the **Queries** page. If rows do not have a checkmark, edit the table and apply the checkmark, save the table, activate the Stitch QA database, and then run the database to refresh the table.

.. table-unified-preprocessed-raw-use-with-stitch-qa-tags-keys-end


.. _table-unified-preprocessed-raw-use-with-stitch-qa-relationships-records:

Relationships between records
--------------------------------------------------

.. TODO: This section is identical in both **Unified Coalesced** and **Unified Preprocessing Raw** topics. They share an overlapping workflow, but should be tracked to discover if there are unique aspects that would lead these sections to evolve independently.

.. table-unified-preprocessed-raw-use-with-stitch-qa-relationships-records-start

Use the **Queries** page to investigate unexpected relationships between individual records that share the same Amperity ID and to investigate why records that look like they *should* belong to the same cluster of records were split.

Use a combination of the **Unified Coalesced** and **Unified Preprocessed Raw** tables to review the data that is associated with these records to help understand why groups of records were matched or why certain records were assigned to a cluster.

In some cases, you may need to investigate and compare entire clusters to better understand why (or why not) these groups of records were maintained (or split) during hierarchical comparison, a step in the Stitch process that occurs *after* pairwise comparison and scoring.

.. table-unified-preprocessed-raw-use-with-stitch-qa-relationships-records-end


.. _table-unified-preprocessed-raw-use-with-stitch-qa-blocklist-values:

Global blocklist values
--------------------------------------------------

.. TODO: This section is identical in both **Unified Coalesced** and **Unified Preprocessing Raw** topics. They share an overlapping workflow, but should be tracked to discover if there are unique aspects that would lead these sections to evolve independently.

.. table-unified-preprocessed-raw-use-with-stitch-qa-blocklist-values-start

The **Unified Coalesced** table provides additional data about individual records, such as blocklisted values, component IDs, or if a record belongs to a supersized cluster.

In some cases, groups of records may have values removed by the :ref:`global bad-values blocklist <bad-values-blocklist-global-values>` instead of the tenant-specific bad-values blocklist.

Compare records in the **Unified Coalesced** table to records in the **Unified Preprocessed Raw** table to identify which values were removed.

.. table-unified-preprocessed-raw-use-with-stitch-qa-blocklist-values-end


.. _table-unified-preprocessed-raw-use-with-customer-360:

Use with Customer 360
==================================================

.. table-unified-preprocessed-raw-use-with-customer-360-start

.. important:: The **Unified Preprocessed Raw** table should not be used outside of the **Customer 360** page. It should not be used to send data to downstream or with workflows.

.. table-unified-preprocessed-raw-use-with-customer-360-end


.. _table-unified-preprocessed-raw-cleaned-vs-uncleaned:

Cleaned vs. uncleaned data
==================================================

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-start

You can compare cleaned data to uncleaned data to improve the quality of data in the customer 360 database.

* The **Unified Preprocessed Raw** table contains a row from every table that is associated with an Amperity ID and contains the results of Stitch processing. Values in this table are "cleaned" data.
* The **Unified Coalesced** table contains the data exactly as it was processed by Stitch. Values in this table are "uncleaned data".

Use a query similar to the following to join fields in the **Unified Preprocessed Raw** table to the **Unified Coalesced** table, and then compare the results.

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-end

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-sql-start

.. code-block:: sql
   :linenos:

   SELECT
     upr.amperity_id AS "upr_amperity_id"
     ,uc.has_blv
     ,uc.address AS "uc_address"
     ,upr.address AS "upr_address"
     -- ,uc.birthdate AS "uc_birthdate"
     -- ,upr.birthdate AS "upr_birthdate"
     ,uc.city AS "uc_city"
     ,upr.city AS "upr_city"
     ,uc.email AS "uc_email"
     ,upr.email AS "upr_email"
     ,upr.login_trimmed AS "upr_login_trimmed"
     -- ,uc.gender AS "uc_gender"
     -- ,upr.gender AS "upr_gender"
     ,uc.given_name AS "uc_given_name"
     ,upr.given_name AS "upr_given_name"
     ,uc.phone AS "uc_phone"
     ,upr.phone AS "upr_phone"
     ,upr.po_box AS "upr_po_box"
     ,uc.postal AS "uc_postal"
     ,upr.postal AS "upr_postal"
     ,uc.generational_suffix AS "uc_generational_suffix"
     ,upr.sk_generational_suffix AS "upr_sk_generational_suffix"
     ,upr.sk_given_name AS "upr_sk_given_name"
     ,uc.state AS "uc_state"
     ,upr.state AS "upr_state"
     ,uc.surname AS "uc_surname"
     ,upr.surname AS "upr_surname"
     ,upr.datasource AS "upr_datasource"
     ,upr.pk AS "pk"
     ,upr.supersized_id AS "upr_supersized_id"
     -- ,upr.component_id AS "upr_component_id"
     -- ,upr.int_id AS "upr_int_id"
   FROM Unified_Coalesced uc
   JOIN Unified_Preprocessed_Raw upr
   ON uc.rep_ds=upr.datasource AND uc.rep_pk=upr.pk
   WHERE UPPER(uc.address) <> upr.address
   -- WHERE UPPER(uc.given_name) <> up.given_name
   -- WHERE UPPER(uc.gender) <> upr.gender
   -- WHERE UPPER(uc.postal) <> upr.postal
   -- WHERE UPPER(uc.email) <> upr.email
   -- WHERE UPPER(uc.city) <> upr.city
   -- WHERE UPPER(uc.phone) <> upr.phone
   -- WHERE uc.amperity_id = 'amperity-id'
   LIMIT 1000

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-sql-end


.. _table-unified-preprocessed-raw-cleaned-vs-uncleaned-compare:

Compare semantic values
--------------------------------------------------

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-compare-start

Use this query to compare raw values and cleaned values for any set of semantics that were used by Stitch.

Within the **SELECT** statement, semantics are grouped in pairs. For example:

::

   ,uc.phone AS "uc_phone"
   ,upr.phone AS "upr_phone"

Comment and uncomment semantic pairs as needed, depending on the semantic values you want to compare.

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-compare-end


.. _table-unified-preprocessed-raw-cleaned-vs-uncleaned-explore:

Explore cleaned values
--------------------------------------------------

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-explore-start

Use the **WHERE** clauses to explore only cleaned values. Comment and uncomment this group of clauses, as necessary:

::

   WHERE UPPER(uc.address) <> upr.address
   -- WHERE UPPER(uc.given_name) <> up.given_name
   -- WHERE UPPER(uc.gender) <> upr.gender
   -- WHERE UPPER(uc.postal) <> upr.postal
   -- WHERE UPPER(uc.email) <> upr.email
   -- WHERE UPPER(uc.city) <> upr.city
   -- WHERE UPPER(uc.phone) <> upr.phone

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-explore-end


.. _table-unified-preprocessed-raw-cleaned-vs-uncleaned-filter:

Filter by Amperity IDs
--------------------------------------------------

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-filter-start

Filter by Amperity IDs to take a closer look a specific group of records, such as for overclustering and underclustering.

Use a series of **WHERE** clauses to compare specific Amperity IDs:

::

   -- WHERE uc.amperity_id = 'amperity-id-1'
   -- WHERE uc.amperity_id = 'amperity-id-2'
   -- WHERE uc.amperity_id = 'amperity-id-3'

This can help identify situations where the bad-values blocklist isn't blocking specific values. Compare the values in the **Unified Preprocessed Raw** table to the values in the **Unified Coalesced** table and verify that values were correctly added to the **blv_** columns.

.. table-unified-preprocessed-raw-cleaned-vs-uncleaned-filter-end


.. _table-unified-preprocessed-raw-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-preprocessed-raw-about-start
   :end-before: .. data-tables-unified-preprocessed-raw-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-preprocessed-raw-table-start
   :end-before: .. data-tables-unified-preprocessed-raw-table-end
