.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the PII table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the PII table.

.. meta::
    :content class=swiftype name=title data-type=string:
        PII table

==================================================
PII table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-table-start
   :end-before: .. term-pii-table-end

.. table-pii-sections-start

You can add a PII table to your customer 360 database, and then use it to build queries to support various downstream use cases:

#. :ref:`Add PII table <table-pii-add-table>`
#. :ref:`Add query <table-pii-add-query>`
#. :ref:`Add data template <table-pii-add-data-template>`
#. :ref:`Send results <table-pii-add-send-results>`

.. table-pii-sections-end


.. _table-pii-add-table:

Add table
==================================================

.. table-pii-add-table-start

Add a PII table :ref:`using a SQL query <table-pii-add-table-sql-query>` that pulls all fields that contain customer profile data from the **Unified Coalesced** table.

.. table-pii-add-table-end


.. _table-pii-add-table-sql-query:

SQL query for PII table
-----------------------------------------

.. table-pii-add-table-sql-query-start

Use a SQL query similar to:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS amperity_id
     ,given_name AS given_name
     ,surname AS surname
     ,full_name AS full_name
     ,generational_suffix AS suffix
     ,email AS email
     ,CASE
       WHEN phone LIKE ''
         OR phone LIKE ' '
         OR phone IS NULL
       THEN NULL
       ELSE CONCAT('+1','',REGEXP_REPLACE(phone,'[^0123456789]',''))
     END AS phone
     ,address AS address
     ,address2 AS address_line_2
     ,city AS city
     ,CASE
       WHEN LENGTH(state) = 2
       THEN state
       ELSE NULL
     END AS state
     ,postal AS postal
     ,birthdate AS birthdate
     ,CASE
       WHEN gender = 'M'
       THEN 'm' 
       WHEN gender = 'F' 
       THEN 'f'
       ELSE NULL
     END AS gender
     ,company AS company
   FROM Unified_Coalesced

The **CASE** statements do the following:

* For phone numbers: ensure that only fields with actual phone numbers are added to the PII table, along with consistent formatting. Any phone number that is empty or does not contain a value will not be added.
* For states: ensure that only values that are two characters, such as "WA", "NY", or "CA", are added to the PII table. Any state that is not two characters will not be added.
* For gender: ensure that only M and F values are added to the table.

.. tip:: You may use any SQL you want to build this table. For example, you could convert all state values that are spelled out to a two character value. Downstream uses cases should be the main driver for how data is shaped in this table.

.. table-pii-add-table-sql-query-end


.. _table-pii-add-query:

Add query
==================================================

.. table-pii-add-segment-start

After the PII table is created you can build queries that return records from the PII table. For example, by using a PII table as part of a query, you can query against the widest possible range of email addresses to help identify the specific email address that is used by an individual on Facebook or Google.

.. table-pii-add-segment-end

**To show matching records from a PII table**

.. table-pii-add-segment-steps-start

#. From the **Queries** page click **Create**, and then select **SQL Query**. This opens the **SQL Query Editor**.
#. Define the query using Presto SQL syntax.
#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. table-pii-add-segment-steps-end


.. _table-pii-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. table-pii-add-data-template-start

Use data templates to enable the use of the PII table across a variety of downstream use cases and destinations. For example. you can run the same query against the PII table, and then send results to Facebook, Google, and Braze.

.. table-pii-add-data-template-end


.. _table-pii-add-send-results:

Send results
==================================================

.. table-pii-add-send-results-start

To send the query results that use fields in the PII table, make sure to use a data template that shapes the results to the destination's field patterns and that the destination itself is configured correctly. After verifying that the results are sent to the destination correctly, add the workflow to an orchestration and apply a schedule.

.. table-pii-add-send-results-end
