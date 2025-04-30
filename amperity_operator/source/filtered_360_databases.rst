.. https://docs.amperity.com/operator/


==================================================
Filtered 360 databases
==================================================

.. TODO: Link to AmpU training video, if it's external-facing. https://learn.amperity.com/multi-database-implementation-best-practices

.. multiple-360-databases-overview-start

For tenants with more than one marketing unit, such as companies that have multiple brands and/or geographic regions, Amperity offers the ability to perform identity resolution across all marketing units, but then filter the data for each specific marketing unit into its own database.

This approach ensures that:

* Unique customer profiles exist across all marketing units
* Each marketing unit has its own set of data that is separated from any other marketing unit
* Users of Amperity only have access to the databases to which they have been given access
* Predictive modeling may be calculated for each marketing unit-specific database

.. multiple-360-databases-overview-end


.. _multiple-360-databases-requirements:

Requirements
==================================================

.. multiple-360-databases-requirements-start

To enable filtering customer 360 databases by marketing unit you must do the following:

#. All domain tables to which semantic tags are applied must :ref:`use the database-key semantic tag <multiple-360-databases-semantics>` to specify which field in that domain table identifies the marketing unit.

#. Use :ref:`custom core tables to define shared functionality <multiple-360-databases-custom-core-tables>` that should be available to each filtered 360 database.

#. Each database must :ref:`use a Database_Filter <multiple-360-databases-table>` table to identify a marketing unit.

#. :ref:`SEMI JOIN the Database_Filter table <multiple-360-databases-join>` to each table in the filtered 360 database that contains data about marketing units.

   This step ensures that data is filtered to return only data that is associated with the marketing unit that is defined in the **Database_Filter** table.

.. multiple-360-databases-requirements-end


.. _multiple-360-databases-semantics:

database-key semantic tag
==================================================

.. multiple-360-databases-semantics-start

All domain tables that contain marketing unit-specific data must have a field in that table that can be used to identify the marketing unit to which values in that table belong.

This field should be assigned the **database-key** semantic tag.

.. note:: Domain tables that contain data for a single marketing unit do not require the **database-key** semantic tag; however, for consistency across all data sources should apply the semantic tag to help prevent situations where the name of a domain table does not clearly identify the name of the marketing unit.

If the semantic tag grouping has a prefix, include the prefix in the semantic tag. For example, use the **txn-item/database-key** semantic tag to add the values of that field to the **database_key** column in the **Unified Itemized Transactions** table.

.. important:: Values associated with **database-key** should be consistent across data sources. For example, to filter by country the value for Japan should be one of "JP" or "Japan" and not a mix of both values.

   Use custom domain tables to standardize these values across data sources, if necessary.

.. multiple-360-databases-semantics-end


.. _multiple-360-databases-custom-core-tables:

Custom core tables
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-core-tables-custom-start
   :end-before: .. term-core-tables-custom-end

.. TODO: Almost the same as databases-stitched-custom-core. Keep in sync.

.. multiple-360-databases-custom-core-tables-start

.. admonition:: Sharing tables across filtered 360 databases

   Custom core tables are reusable across filtered 360 databases. Core tables store SQL logic that can be referenced by multiple databases, but can be adapted to provide database-specific logic as well. 

   For example, the **Customer Attributes** table typically requires customization to align features within that table to how your brand defines churn prevention status indicators, historical purchase lifecycles, and customer types. This table can be extended to support custom features, and each marketing unit may have different requirements.

   If each brand has unique requirements, then each filtered 360 database may require its own customized version of the **Customer Attributes** table, with each maintained separately. 

   Another option is to extend the custom core table to support database-specific logic, such as by using a **CASE** statement to enable different thresholds for considering customers "lapsed" by marketing unit. For example:

   .. code-block:: sql

      CASE
        WHEN database_key = 'ACME Essentials' THEN 730
        WHEN database_key = 'Socktown' THEN 365
      END AS lapsed_threshold

   Each filtered 360 database can then reference the custom core table:

   .. code-block:: sql

      SELECT *
      FROM Customer_Attributes_Core ca
      SEMI JOIN Database_Filter df
      ON ca.database_key = df.database_key

   When the **Customer Attributes** core table is updated, those updates will be applied to each filtered 360 database automatically.

.. multiple-360-databases-custom-core-tables-end


.. _multiple-360-databases-table:

Database_Filter table
==================================================

.. multiple-360-databases-table-start

Each filtered database must contain a **Database_Filter** table, which contains a single record with a hard-coded string value that defines a specific brand or geographic region.

For example, the **Database_Filter** table in a region-specific database for Japan would use SQL similar to:

.. code-block:: sql

   SELECT 'JP' AS database_key

.. multiple-360-databases-table-end


.. _multiple-360-databases-join:

Filter tables by marketing unit
==================================================

.. multiple-360-databases-join-start

For each table in the filtered 360 database that contains data the **database_key** column you must use a **SEMI JOIN** to ensure data within that table is filtered to match only the value defined in the **Database_Filter** table.

For example, to filter the **Unified Coalesced** table use SQL similar to:

.. code-block:: sql

   SELECT *
   FROM Unified_Coalesced uc
   SEMI JOIN Database_Filter df
   ON uc.database_key = df.database_key

.. multiple-360-databases-join-end
