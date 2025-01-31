.. https://docs.amperity.com/datagrid/


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

The customer 360 database is a collection of tables:

* Customer 360
* Unified Coalesced
* Unified Customer
* Merged Customers
* Unified Itemized Transactions
* Unified Transactions
* etc.

It also may contain passthrough tables that bring data from domain tables to the customer 360 database:

* Table_A
* Table_B
* Table_C
* etc.

These tables are visible from within the **Customer 360** page, the **Data Explorer**, and the **Queries** page.

A series of versioned tables is also provided, along with a table named **amperity_table_versions** that is a record of all tables. A versioned table can be accessed using a SQL query authored from the **Queries** page.

All versioned tables are appended with **_versioned**. For example:

* **Customer360_versioned**
* **Unified_Coalesced_versioned**
* **Unified_Customer_versioned**
* **Merged_Customers_versioned**
* **Unified_Scores_versioned**
* **Table_A_versioned**
* **Table_B_versioned**
* **Table_C_versioned**
* **amperity_table_versions**
* etc.

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

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-enable-table-versioning-caution-start
   :end-before: .. databases-database-howto-enable-table-versioning-caution-end


**To enable table versioning**

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-enable-table-versioning-steps-start
   :end-before: .. databases-database-howto-enable-table-versioning-steps-end


.. _historical-data-access-datetime:

Return versions by datetime
==================================================

.. historical-data-access-datetime-start

Use **datetime** to return a version that is on a specific date. For example:

.. code-block:: sql

   SELECT * 
   FROM table_a_versioned AS a
   JOIN amperity_table_versions AS v 
   ON v.version = a.amperity_version 
   WHERE v.datetime = 20200402

.. historical-data-access-datetime-end


.. _historical-data-access-created-at:

Return versions by creation date
==================================================

.. historical-data-access-created-at-start

Use **created_at** to return a version at its time of creation.

The following query returns all records from the Customer360 table with addresses that changed between yesterday and today:

.. code-block:: sql

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


.. _historical-data-view-all:

View all versioned tables
==================================================

.. historical-data-view-all-start

The **amperity_table_versions** table stores a list of available versioned tables, their offset values, and the date and time at which they were created.

Use the following query to return the list of available versioned tables:

.. code-block:: sql

   SELECT * FROM amperity_table_versions

The list of available versioned tables is similar to:

.. code-block:: mysql

   ------------------- ------------------------ -------- --------------------------
    table_name          version                  offset   created_at
   ------------------- ------------------------ -------- --------------------------
    Customer360         qdv-20200402-1234-abcd   0        2021-04-02T12:58:54.000Z
    Unified_Coalesced   qdv-20200402-1234-abcd   0        2021-04-02T12:58:54.000Z
    Unified_Customer    qdv-20200402-1234-abcd   0        2021-04-02T12:58:54.000Z
    Merged_Customers    qdv-20200402-1234-abcd   0        2021-04-02T12:58:54.000Z
    Unified_Scores      qdv-20200402-1234-abcd   0        2021-04-02T12:58:54.000Z
    Table_A             qdv-20200402-1234-abcd   0        2021-04-02T12:58:54.000Z
    Table_B             qdv-20200402-1234-abcd   0        2021-04-02T12:58:54.000Z
    Table_C             qdv-20200402-1234-abcd   0        2021-04-02T12:58:54.000Z
    ...
    Customer360         qdv-20200402-1234-abcd   1        2021-04-01T08:18:23.000Z
    Unified_Coalesced   qdv-20200402-1234-abcd   1        2021-04-01T08:18:23.000Z
    Unified_Customer    qdv-20200402-1234-abcd   1        2021-04-01T08:18:23.000Z
    Merged_Customers    qdv-20200402-1234-abcd   1        2021-04-01T08:18:23.000Z
    Unified_Scores      qdv-20200402-1234-abcd   1        2021-04-01T08:18:23.000Z
    Table_A             qdv-20200402-1234-abcd   1        2021-04-01T08:18:23.000Z
    Table_B             qdv-20200402-1234-abcd   1        2021-04-01T08:18:23.000Z
    Table_C             qdv-20200402-1234-abcd   1        2021-04-01T08:18:23.000Z
    ...
    Customer360         qdv-20200402-1234-abcd   2        2021-03-31T10:34:33.000Z
    Unified_Coalesced   qdv-20200402-1234-abcd   2        2021-03-31T10:34:33.000Z
    ...
   ------------------- ------------------------ -------- --------------------------

.. historical-data-view-all-end
