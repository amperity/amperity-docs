.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use database table versioning to enable querying of historical data.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use database table versioning to enable querying of historical data.

.. meta::
    :content class=swiftype name=title data-type=string:
        Query historical data

==================================================
Query historical data
==================================================

.. historical-data-start

You can enable table versioning, after which you can query historical versions of any data table in any database. Access to historical data enables change data capture scenarios for the customer 360 database--"What changed yesterday?"--and provides additional ways to validate Stitch results and to measure the quality of transactional data. 

.. historical-data-end


.. _historical-data-howitworks:

How it works
==================================================

.. historical-data-howitworks-start

The customer 360 database is a collection of tables. For example:

* Customer 360
* Unified Coalesced
* Unified Customer
* Merged Customers
* Unified Itemized Transactions
* Unified Transactions

The customer 360 database also contains passthrough tables that bring domain tables to the customer 360 database. For example:

* Domain_Table_A
* Domain_Table_B
* Domain_Table_C

These tables are visible from the **Customer 360** page, the **Data Explorer**, and the **Queries** page.

For each table with versioning enabled a table is created with the same name with **_versioned** appended. This table has the version history for the table. A table named **amperity_table_versions** is created that contains a record of all versioned tables.

For example:

* **Customer360_versioned**
* **Unified_Coalesced_versioned**
* **Unified_Customer_versioned**
* **Merged_Customers_versioned**
* **Unified Itemized Transactions**
* **Unified Transactions**
* **Domain_Table_A_versioned**
* **Domain_Table_B_versioned**
* **Domain_Table_C_versioned**
* **amperity_table_versions**

.. historical-data-howitworks-end


.. _historical-data-available-versions:

Available versions
==================================================

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-enable-table-versioning-start
   :end-before: .. databases-database-howto-enable-table-versioning-end

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-enable-table-versioning-important-start
   :end-before: .. databases-database-howto-enable-table-versioning-important-end

.. caution:: Changes to columns within a table that is enabled for table versioning changes the schema and will cause incompatible versions to be dropped. To avoid this, add columns to the end of the table *or* :ref:`enforce static table schemas <historical-data-static-schemas>`.

**To enable table versioning**

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-enable-table-versioning-steps-start
   :end-before: .. databases-database-howto-enable-table-versioning-steps-end


.. _historical-data-static-schemas:

Static schemas
==================================================

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-enforce-static-schemas-start
   :end-before: .. databases-database-howto-enforce-static-schemas-end

**To enforce a static table schema**

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-enforce-static-schemas-steps-start
   :end-before: .. databases-database-howto-enforce-static-schemas-steps-end


.. _historical-data-access-datetime:

Return versions by date
==================================================

.. historical-data-access-datetime-start

Use **created_at** to return a version that is on a specific date. For example:

.. code-block:: sql
   :linenos:

   SELECT * 
   FROM table_a_versioned AS a
   JOIN amperity_table_versions AS v 
   ON v.version = a.amperity_version 
   WHERE v.created_at = DATE '2025-04-02'

.. historical-data-access-datetime-end


.. _historical-data-access-created-at:

Return versions by creation date
==================================================

.. historical-data-access-created-at-start

Use **created_at** to return a version at its time of creation.

The following query returns all records from the Customer360 table with addresses that changed between yesterday and today:

.. code-block:: sql
   :linenos:

   WITH Customer360_yesterday AS (
     SELECT *
     FROM Customer360_versioned
     WHERE amperity_version = (
       SELECT DISTINCT version
       FROM amperity_table_versions
       WHERE created_at >= DATE_TRUNC('day', current_timestamp - interval '1' day)
       ORDER BY created_at ASC
       LIMIT 1
     )
   )

   SELECT *
   FROM Customer360 AS ct
   LEFT JOIN Customer360_yesterday AS cy
   ON ct.amperity_id = cy.amperity_id
   AND ct.addressline1 <> cy.addressline1
   WHERE cy.amperity_id IS NOT NULL

.. historical-data-access-created-at-end


.. _historical-data-send-only-updated-records:

Use a delta to send only updated records
==================================================

.. historical-data-send-only-updated-records-start

Build a delta that identifies which records are new or updated since the previous database update, and then send only new or updated records to downstream workflows. Use this approach with large tables that have frequent updates of data.

#. Track the table version used to create each delta.

   Open the **Queries** page and create a query called "Latest_Version" with the following SQL:

   .. code-block:: sql

      SELECT DISTINCT version
      FROM amperity_table_versions
      where offset = 0

   .. tip:: Version identifiers are unique to a database. If deltas are required for multiple databases, use a latest version query for each database.

#. Use an orchestration to send the results of the "Latest_Version" query to a storage location, such as an Amazon S3 bucket. Automate this workflow to run at the same time as orchestrations that send deltas.

   .. tip:: Allow this workflow to overwrite the previous file each time it runs. Only the current version of this file is required.

#. Create a feed named "Latest_Version" and use a courier to pull the file from the storage location. Configure the courier to truncate and load this file daily, and then include the courier in the daily scheduled workflow.

   Every day this courier will load the version that was used in the previous day's workflow to today's workflow.

#. Add the "Latest_Version" table as a passthrough table to the same database from which the "Latest_Version" query is configured.

#. Use a query to identify new and updated records since the previous database run.

   Open the **Queries** page and create a query with the following SQL:

   .. code-block:: sql

      SELECT *
      FROM [table_name]

      except

      SELECT tv.*
      FROM [table_name]_versioned tv
      JOIN Latest_Version lv
      ON tv.amperity_version = lv.version

   The results of this query will be only the new and updated records.

#. Use an orchestration to send results of this query--a list of new and updated records--to a downstream workflow.

.. historical-data-send-only-updated-records-end

.. historical-data-send-only-updated-records-append-start

.. admonition:: Deltas for tables that only append records

   For tables that append updated records and **never** update older records you can create incremental exports without using table versions.

   For example, the **Campaign_Results** table appends information about campaigns using the current date as the delivery date. Information about campaigns for the previous day exist. Use the following SQL to send an incremental export of campaign activity:

   .. code-block:: sql

      SELECT *
      FROM Campaign_Recipients
      WHERE delivery_date = current_date - INTERVAL '1' DAY

   This approach has some risks.
   
   * A workflow that is delayed may cause this query to run on a different day than intended.
   * A campaign that runs between midnight and this query will not be included in the query results until the following day.
   * Timezones can affect the timing of orchestrations.

.. historical-data-send-only-updated-records-append-end


.. _historical-data-send-only-offsets:

Use offsets to send smaller deltas
==================================================

.. historical-data-send-only-offsets-start

Use an offset value to limit the number of records sent to a downstream workflow that allows upserts. For example, using 5 as the offset will return a list of records that is smaller that the full table.

For example:

.. code-block:: sql

   SELECT *
   FROM TABLE

   EXCEPT

   SELECT a.*
   FROM TABLE_versioned a
   JOIN (SELECT DISTINCT version
     FROM amperity_table_versions
     WHERE v.offset = 5) AS v
   ON v.version = a.amperity_version

.. note:: This approach is less reliable than :ref:`using a delta <historical-data-send-only-updated-records>` because it is more likely to contain multiple record updates even if it is unlikely to miss sending any incremental records.

   The downstream workflow **must** allow upserts.

.. admonition:: What about using "offset 1"?

   An offset of 1 is an unreliable version indicator.

   Deltas that identify new or updated data between table versions must be done against data that was sent to downstream workflows.

   It is possible for more than one version to exist for the previous day, but only one version represents the data sent to downstream workflows.

   For example, a manual database run creates new table versions but does not run any orchestrations and does not send data to a downstream workflow. If the manual run occurred after the automated run, the offset that represents data sent to downstream workflows is "offset 2".

   The :ref:`created_at <historical-data-access-created-at>` can have the same behavior.

.. historical-data-send-only-offsets-end


.. _historical-data-view-all:

View all versioned tables
==================================================

.. historical-data-view-all-start

The **amperity_table_versions** table stores a list of versioned tables, their offset values, and the date and time at which they were created.

Use the following query to return the list of available versioned tables:

.. code-block:: sql

   SELECT * FROM amperity_table_versions

The list of available versioned tables is similar to:

.. code-block:: mysql

   ------------------- ------------------------ -------- --------------------------
    table_name          version                  offset   created_at
   ------------------- ------------------------ -------- --------------------------
    Customer360         qdv-20250402-1234-abcd   0        2025-04-02T12:58:54.000Z
    Unified_Coalesced   qdv-20250402-1234-abcd   0        2025-04-02T12:58:54.000Z
    Unified_Customer    qdv-20250402-1234-abcd   0        2025-04-02T12:58:54.000Z
    Merged_Customers    qdv-20250402-1234-abcd   0        2025-04-02T12:58:54.000Z
    Unified_Scores      qdv-20250402-1234-abcd   0        2025-04-02T12:58:54.000Z
    Table_A             qdv-20250402-1234-abcd   0        2025-04-02T12:58:54.000Z
    Table_B             qdv-20250402-1234-abcd   0        2025-04-02T12:58:54.000Z
    Table_C             qdv-20250402-1234-abcd   0        2025-04-02T12:58:54.000Z
    ...
    Customer360         qdv-20250402-1234-egfh   1        2025-04-01T08:18:23.000Z
    Unified_Coalesced   qdv-20250402-1234-egfh   1        2025-04-01T08:18:23.000Z
    Unified_Customer    qdv-20250402-1234-egfh   1        2025-04-01T08:18:23.000Z
    Merged_Customers    qdv-20250402-1234-egfh   1        2025-04-01T08:18:23.000Z
    Unified_Scores      qdv-20250402-1234-egfh   1        2025-04-01T08:18:23.000Z
    Table_A             qdv-20250402-1234-egfh   1        2025-04-01T08:18:23.000Z
    Table_B             qdv-20250402-1234-egfh   1        2025-04-01T08:18:23.000Z
    Table_C             qdv-20250402-1234-egfh   1        2025-04-01T08:18:23.000Z
    ...
    Customer360         qdv-20200402-1234-ijkl   2        2025-03-31T10:34:33.000Z
    Unified_Coalesced   qdv-20200402-1234-ijkl   2        2025-03-31T10:34:33.000Z
    ...
   ------------------- ------------------------ -------- --------------------------

.. historical-data-view-all-end
