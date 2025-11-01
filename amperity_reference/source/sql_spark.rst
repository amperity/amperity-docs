.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Use Spark SQL to build custom views for data sources and to build database tables.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use Spark SQL to build custom views for data sources and to build database tables.

.. meta::
    :content class=swiftype name=title data-type=string:
        About Spark SQL

==================================================
About Spark SQL
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-spark-sql-start
   :end-before: .. term-spark-sql-end


.. _sql-spark-why-should-i-use-this:

Why should you use this reference?
==================================================

.. sql-spark-why-should-i-use-this-start

The **Sources** and **Databases** pages use Spark SQL as the underlying SQL engine. Amperity database tables, custom domain tables, and ingest queries are built almost exclusively by using a **SELECT** statement and window functions, along with the clauses, operators, expressions, and functions you would expect to be available.

Please refer to this reference first, and then to the official Spark SQL documentation for `SELECT statements <https://spark.apache.org/docs/3.5.5/sql-ref-syntax.html#data-retrieval-statements>`__ |ext_link| and the `list of built-in functions <https://spark.apache.org/docs/latest/api/sql/index.html>`__ |ext_link|.

.. sql-spark-why-should-i-use-this-end


.. _sql-spark-about:

About Spark SQL
==================================================

.. sql-spark-about-start

Use Spark SQL to define all SQL queries related to the following areas of Amperity:

* Ingesting data, including ingest queries
* Processing data into domain tables
* Building custom domain tables
* Loading data into Stitch
* Running Stitch
* Loading the results of Stitch into the customer 360 database
* Defining tables in the customer 360 database

.. sql-spark-about-end

.. sql-spark-note-spark-vs-presto-start

.. note:: Spark SQL is used to define all SQL queries related to the Stitch process up to and including building the tables in the customer 360 database. Presto SQL is used to define SQL queries for segments. Why both?

   * Spark SQL performs better in more traditional processes like machine learning and ETL-like processes that are resource intensive.
   * Presto SQL performs better when running real-time queries against cloud datasets.

.. sql-spark-note-spark-vs-presto-end

.. sql-spark-tip-hive-start

.. tip:: Amperity uses |ext_sparksql_version_current|.

.. sql-spark-tip-hive-end


.. _sql-spark-recommendations:

Recommendations
==================================================

.. sql-spark-recommendations-start

This is a list of recommendations for using Spark SQL with Amperity.

.. sql-spark-recommendations-end


.. _sql-spark-recommendation-general:

General
--------------------------------------------------

.. sql-spark-recommendation-general-start

**Do**

* Use consistent and descriptive identifiers and names.
* Include comments in SQL code where necessary. Use the C style opening ``/*`` and closing ``*/`` where possible. Otherwise precede comments with ``--`` and finish them with a new line.
* Make judicious use of white space and indentation to make code easier to read.
* Store ISO-8601 compliant date and time information: ``YYYY-MM-DD HH:MM:SS.SSSSS``.
* Try to use only standard SQL functions instead of vendor-specific functions for reasons of portability.
* Keep code succinct and devoid of redundant SQL, such as unnecessary quoting or parentheses or **WHERE** clauses that can otherwise be derived.
* Convert string values to lowercase. For example: **LOWER(column_name) = 'value'**.
* Code review complex SQL statements.
* Treat varchars as string values.
* Use one-way SHA-256 hashes for fields that contain PII data.
* Ensure that window functions are complete and use **OVER()** and **PARTITION BY**.

  .. note:: **ORDER BY** is not required when a window function has aggregate functions, such as **AVG()** or **SUM()**, but the behavior of the window function can change. For example:

     * If **ORDER BY** is included, **SUM()** calculates the running sum within a partition in order.
     * If **ORDER BY** is excluded, **SUM()** calculates the sum of all values within a partition.

* Use single backticks around column names when they contain spaces or special characters, when they are fully numeric, or when the column name is also a :ref:`reserved word <sql-spark-recommendation-reserved-words>`.

**Avoid**

* Reserved keyword names that are used as identifiers.
* CamelCase, with the exception of the table name. CamelCase is more difficult to scan.
* Descriptive prefixes or `Hungarian notation <https://en.wikipedia.org/wiki/Hungarian_notation>`__ |ext_link| such as ``sp_`` or ``tbl``.
* Plurals. Use the more natural collective term where possible instead. For example staff instead of employees or people instead of individuals.
* Quote identifiers. Use SQL92 double quotes for portability, if possible.
* Object-oriented design principles with SQL or database structures.
* Boolean values wrapped in quotes. Use **TRUE** and **FALSE** without quotes.
* Large tables defined within the **NOT IN** expression of a **WHERE** statement. Large tables run slowly and may result in out-of-memory errors.

.. sql-spark-recommendation-general-end


.. _sql-spark-recommendation-add-comments:

Add comments
--------------------------------------------------

.. sql-spark-recommendation-add-comments-start

Be sure to add comments to all SQL code that defines database tables or performs any type of pre-ingest processing, such as an ingest query.

Code comments should describe:

* The purpose of the table, especially for an intermediate table that is consumed by other tables in a database.
* The purpose of any sub-queries.
* Situations where data is coalesced into single fields. Be sure to note what the rule is so that future maintainers of that SQL statement can apply it to their changes. For example: "Items are populated in the following order, when available: from loyalty tables, then POS tables, and then any historical tables."
* Non-obvious actions within the SQL statement. For example, when inserting static text as a date value or when joining on fields that appear to have different data types.

.. sql-spark-recommendation-add-comments-end


.. _sql-spark-recommendation-avoid-multiple-passes:

Avoid multiple passes
--------------------------------------------------

.. sql-spark-recommendation-avoid-multiple-passes-start

In some cases information from Amperity must be added to the data ingest process so that Amperity can correctly shape the data prior to the Stitch process. This should be done in a single pass.

#. At the end of processing on day 1 create a "feedback segment" that contains the data to be shaped on day 2, and then output that segment data so that it may be ingested by Amperity on day 2.
#. On day 2 ingest data from the customer's sources normally, and then ingest the feedback segment.
#. Join the day 2 data to the feedback segment, and then shape the results for Stitch.
#. Ensure the data is made available to Stitch, and then run Stitch.
#. Repeat the feedback segment process on subsequent days if necessary.

.. sql-spark-recommendation-avoid-multiple-passes-end


.. _sql-spark-recommendation-commas:

Commas
--------------------------------------------------

.. sql-spark-recommendation-commas-start

Commas are used as separators in SQL queries and are typically added at the end of a line, like this:

.. code-block:: sql
   :linenos:

   SELECT 
     amperity_id AS amperity_id,
     max(given_name) AS given_name,
     max(surname) AS surname,
     max(email) AS email,
     max(phone) AS phone,
     max(address) AS address,
     max(city) AS city,
     max(state) AS state,
     max(postal) AS postal,
     max(birthdate) AS birthdate,
     max(gender) AS gender
   FROM Unified_Coalesced
   GROUP BY amperity_id

Adding the comma at the start of the row is recommended for two reasons:

#. It makes it visually obvious that a comma was not missed.
#. It allows a field to be commented out without breaking anything else in the query.

For example:

.. code-block:: sql
   :linenos:

   SELECT 
     amperity_id AS amperity_id
     ,max(given_name) AS given_name
     ,max(surname) AS surname
     ,max(email) AS email
     ,max(phone) AS phone
     ,max(address) AS address
   --  ,max(address_2) AS address_line_two
     ,max(city) AS city
     ,max(state) AS state
     ,max(postal) AS postal
     ,max(birthdate) AS birthdate
     ,max(gender) AS gender
   FROM Unified_Coalesced
   GROUP BY amperity_id

.. sql-spark-recommendation-commas-end


.. _sql-spark-recommendation-escape-characters:

Escape characters
--------------------------------------------------

.. sql-spark-recommendation-escape-characters-start

Use a backslash ( ``\`` ) as an escape character for strings that contain single and double quotes. For example:

::

   ,CASE
     WHEN store_name = 'Macy\'s'
     THEN 'Macy\'s' ELSE 'Other'
   END AS store_name

.. important:: A backslash ( ``\`` ) contained within a regular expression MUST be escaped using another backslash. For example, a regular expression that matches a single numeric digit should be ``\\d`` and not ``\d``.

.. sql-spark-recommendation-escape-characters-end


.. _sql-spark-recommendation-faster-operations-are-better:

Faster operations are better
--------------------------------------------------

.. sql-spark-recommendation-faster-operations-are-better-start

The costs of operations in Spark SQL depends on many things. In general, faster operations are better because they cost less.

The following types of actions have a minimal affect on Spark SQL performance:

* **COALESCE()** runs across rows, but stops when it finds the first value.
* Row-atomic functions, such as **CONCAT()**, operate on a single row, which keeps the dataset small.
* Value-atomic functions, such as type conversions and **TRIM()**, operate on a single value.
* **UNION** appends one set of rows to another, without deduplication.


A query runs faster when:

* **SELECT** statements are restricted to specific columns
* **WHERE** clauses are restricted to specific rows


A query runs slower when:

* A **JOIN** operation :ref:`introduces skew <sql-spark-skew-avoiding-join-operations>`.

* **SELECT DISTINCT** operations are present. Use **DISTINCT** only when necessary.

  A **SELECT DISTINCT** operation may require data to be shuffled between workers, which is expensive.

  .. note:: A **UNION** operation deduplicates data, a **UNION ALL** operation does not.

* A **PARTITION BY** clause in a window function :ref:`introduces skew <sql-spark-skew-avoiding-partition-by>`.

* A global **ORDER BY** operation can be difficult to partition and may require shuffling data across workers.

.. sql-spark-recommendation-faster-operations-are-better-end


.. _sql-spark-recommendation-filter-then-combine:

Filter, then combine
--------------------------------------------------

.. sql-spark-recommendation-filter-then-combine-start

A pattern that filters out unneeded rows and selects only necessary columns is much faster than first gathering together all of the information that may be required.

**Do this**

.. code-block:: sql
   :linenos:

   SELECT
     uct.amperity_id
     ,uct.first_name
     ,uct.last_name
     ,ecomm.last_order_date
   FROM (
     SELECT
       amperity_id
       ,first_name
       ,last_name
     FROM Unified
     WHERE datasource <> 'Example'
     GROUP BY amperity_id
   ) AS uct
   LEFT JOIN ecomm ON (ecomm.amperity_id = uct.amperity_id)

**Not this**

.. code-block:: sql
   :linenos:

   SELECT
     uct.amperity_id
     ,uct.first_name
     ,uct.last_name
     ,ecomm.last_order_date
   FROM Unified
   LEFT JOIN ecomm ON (ecomm.amperity_id = uct.amperity_id)
   WHERE Unified.datasource <> 'Example'

.. sql-spark-recommendation-filter-then-combine-end


.. _sql-spark-recommendation-filter-null-values-then-join:

Filter NULL values, then join
--------------------------------------------------

.. sql-spark-recommendation-filter-null-values-then-join-start

In some cases the presence of **NULL** values can cause skew when joined to other tables. You can reduce skew by filtering out **NULL** values prior to the **JOIN** operation. For example:

.. code-block:: sql
   :linenos:

   LEFT JOIN (
     SELECT *
     FROM Merged_Customers
     WHERE email IS NOT NULL
   ) mc
   ON table_A.email = mc.email

.. sql-spark-recommendation-filter-null-values-then-join-end


.. _sql-spark-recommendation-indentation:

Indentation
--------------------------------------------------

.. sql-spark-recommendation-indentation-start

To ensure that SQL is readable it is important that standards of indentation are followed.

.. sql-spark-recommendation-indentation-end


.. _sql-spark-recommendation-indentation-formalisms:

Formalisms
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-indentation-formalisms-start

Make use of **BETWEEN** where possible instead of combining multiple statements with **AND**. Similarly, use **IN()** instead of multiple **OR** clauses. Where a value needs to be interpreted before leaving the database use the **CASE** expression. **CASE** statements can be nested to form more complex logical structures. Avoid the use of **UNION** clauses and temporary tables where possible.

.. sql-spark-recommendation-indentation-formalisms-end


.. _sql-spark-recommendation-indentation-joins:

Join operations
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-indentation-joins-start

Joins should be aligned with the **FROM** and grouped with a new line where necessary.

.. sql-spark-recommendation-indentation-joins-end


.. _sql-spark-recommendation-indentation-subqueries:

Subqueries
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-indentation-subqueries-start

Subqueries should be aligned to the line above them, but then follow standard indentation patters from that location. Sometimes it will make sense to have the closing parenthesis on a new line at the same character position as its opening partner—this is especially true where you have nested subqueries.

.. sql-spark-recommendation-indentation-subqueries-end


.. _sql-spark-recommendation-limit-extra-work:

Limit extra work
--------------------------------------------------

.. sql-spark-recommendation-limit-extra-work-start

Limit the work done by a SQL query to improve overall performance. The following examples show how to use window functions to create subsections, order them by date, and then pick the first one.

**Do this**

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id,
     FIRST_VALUE(LOWER(EMAIL)) OVER
       (PARTITION BY amperity_id)
       AS email_address,
     CAST('2017-12-22' AS DATE) as merged_date
   FROM FlatFiles_CampsiteGawEmailListDec2017
   WHERE EMAIL IS NOT NULL
   ORDER BY merged_date

This example performs better and achieves the same result.

**Not this**

.. code-block:: sql
   :linenos:

   SELECT DISTINCT  
     amperity_id
     ,FIRST_VALUE(LOWER(EMAIL_ADDRESS_)) OVER
       (PARTITION BY amperity_id ORDER BY merged_date DESC)
       AS email_address
     ,FIRST_VALUE(merged_date) OVER
       (PARTITION BY LOWER(EMAIL_ADDRESS_) ORDER BY merged_date DESC)
       AS mergeddate
     FROM (
       SELECT
         amperity_id
         ,EMAIL_ADDRESS_
         ,CAST('2017-12-22' AS DATE) as merged_date
       FROM FlatFiles_TevaSweepstakesDecember2017
       WHERE EMAIL_ADDRESS_ IS NOT NULL)
     WHERE merged_date IS NOT NULL)

This example does extra work to set all dates to the same value and is slower.

.. sql-spark-recommendation-limit-extra-work-end


.. _sql-spark-recommendation-limit-tables:

Limit tables
--------------------------------------------------

.. sql-spark-recommendation-limit-tables-start

A database should only include tables that are useful to downstream activity, such as building segments or for a database export. As a general rule, segment authors must *never* use any tables with a name that starts with "Unified" to build a segment. Use the passthrough option to make available certain domain tables that contain data that is useful for segmentation.

.. sql-spark-recommendation-limit-tables-end


.. _sql-spark-recommendation-naming-conventions:

Naming conventions
--------------------------------------------------

.. sql-spark-recommendation-naming-conventions-start

Ensure the name is unique and does not exist as a reserved keyword. Keep the length to a maximum of 30 bytes—in practice this is 30 characters unless you are using multi-byte character set. Names must begin with a letter and may not end with an underscore. Only use letters, numbers, and underscores in names. Avoid the use of multiple consecutive underscores, as they can be hard to read. Use underscores where you would include a space in the name. For example "first name" becomes "first_name". Avoid abbreviations and if you have to use them make sure they are commonly understood.

.. code-block:: sql

   SELECT first_name
   FROM Customer360

.. sql-spark-recommendation-naming-conventions-end


.. _sql-spark-recommendation-naming-convention-alias-names:

Alias names
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-naming-convention-alias-names-start

An alias assigns a temporary name to a column or a table that only exists for the duration of a query. An alias is defined after the **AS** keyword.

For columns::

   SELECT column_name AS alias_name
   FROM table_name;

For tables::

   SELECT column_names
   FROM table_name AS alias_name;

When using an alias:

* Assign names that relate to the column or table.
  .. important:: "Do not use an alias when its name matches the original column name.
* Always use the **AS** keyword to ensure readability.
  .. tip:: Include the **AS** keyword when aliasing columns in a 'SELECT' statement.
* For computed data--**SUM()** or **AVG()**--use the name you would give it were it a column defined in the schema.
* Always wrap an aliased field name with single back ticks:

  .. code-block:: none

     `given_name`

The following example shows using aliases to add clarity to a **SELECT** statement that selects columns from more than one table. The "c360" alias refers to the **Customer 360** table and the "el" alias refers to the **Email_List** table:

.. code-block:: sql

   SELECT c360.email, c360.given_name, c360.surname, el.status
   FROM Customer360 c360

   LEFT JOIN Email_List el ON c360.email = el.email
   WHERE status IS NOT NULL

.. sql-spark-recommendation-naming-convention-alias-names-end


.. _sql-spark-recommendation-naming-convention-column-names:

Column names
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-naming-convention-column-names-start

Always use the singular name. Where possible avoid simply using id as the primary identifier for the table. Do not add a column with the same name as its table and vice versa. Always use lowercase except where it may make sense not to, such as with proper nouns.

.. sql-spark-recommendation-naming-convention-column-names-end


.. _sql-spark-recommendation-naming-convention-correlation-names:

Correlation names
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-naming-convention-correlation-names-start

A correlation name assigns a temporary name to a table. A correlation name is defined within the FROM clause after the table name. For example:

.. code-block:: none

   FROM table_name correlation_name;

When using correlations:

* Assign names that relate to the table. For example: a table named "Merged_Customers" should have a correlation name of "um".
* Always use the first letter of the table as the first letter of the correlation.
* Append numbers as necessary to ensure unique correlation names.
* Only use the correlation name within the rest of same query.

.. sql-spark-recommendation-naming-convention-correlation-names-end

.. _sql-spark-recommendation-naming-convention-suffix-names:

Suffix names
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-naming-convention-suffix-names-start

The following suffixes represent patterns that should be applied to column names in SQL tables. These patterns help ensure the purpose of columns can be easily understood by all users. Use the correct suffixes, use them consistently, and use them everywhere they are appropriate.

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Suffix
     - Description
   * - **_id**
     - A unique identifier such as a column that is a primary key.
   * - **_status**
     - A flag value or some other status of any type such as "publication_status".
   * - **_total**
     - The total or sum of a collection of values.
   * - **_num**
     - Denotes the field contains any kind of number.
   * - **_name**
     - Signifies a name such as "first_name".
   * - **_seq**
     - Contains a contiguous sequence of values.
   * - **_date**
     - Denotes a column that contains the date of something.
   * - **_tally**
     - A count.
   * - **_size**
     - The size of something such as a file size or clothing.
   * - **_addr**
     - An address for the record could be physical or intangible such as "ip_addr".

.. sql-spark-recommendation-naming-convention-suffix-names-end


.. _sql-spark-recommendation-naming-convention-table-names:

Table names
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-naming-convention-table-names-start

Table names must be unique within the same database or database generation fails.

.. sql-spark-recommendation-naming-convention-table-names-end


.. _sql-spark-style-guide-null-values:

NULL values
--------------------------------------------------

.. sql-spark-style-guide-null-values-start

Functions may fail when they encounter a **NULL** value and others may return **NULL** values if any of their arguments return **NULL** values. `Spark SQL handles NULL values in a variety of ways. <https://spark.apache.org/docs/3.5.5/sql-ref-null-semantics.html>`__ |ext_link|

.. sql-spark-style-guide-null-values-end


.. _sql-spark-recommendation-one-way-sha256-hashes:

One-way SHA-256 hashes
--------------------------------------------------

.. sql-spark-recommendation-one-way-sha256-hashes-start

Apply one-way SHA-256 hashes to fields that contain PII data. A one-way hash ensures that data can no longer be recognizable as valid PII, but still allows that data to identified by downstream processes.

.. sql-spark-recommendation-one-way-sha256-hashes-end

.. sql-spark-recommendation-one-way-sha256-hash-syntax-start

A one-way SHA-256 hash has the following syntax:

.. code-block:: none

   SHA2(LOWER(TRIM(FIELD)),256) AS FIELD

and uses the following Spark SQL functions:

* **SHA2()** hashes data with a one-way SHA-256 hash.
* **LOWER()** sets all characters to lowercase.
* **TRIM()** removes leading and trailing whitespace.
* **FIELD** is the name of the field that contains PII data.

For example:

.. code-block:: none

   SHA2(LOWER(TRIM(email)),256) AS email

.. sql-spark-recommendation-one-way-sha256-hash-syntax-end


.. _sql-spark-recommendation-reserved-words:

Reserved words
--------------------------------------------------

.. sql-spark-recommendation-reserved-words-start

Always use uppercase for the reserved keywords like **SELECT** and **WHERE**. It is best to avoid the abbreviated keywords and use the full length ones where available (prefer **ABSOLUTE** to **ABS**). Do not use database server specific keywords where an ANSI SQL keyword already exists performing the same function. This helps to make code more portable.

.. sql-spark-recommendation-reserved-words-end


Reserved keywords
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-reserved-keywords-start

The following keywords are reserved and must be double-quoted to be used as an identifier.

* **ALTER**
* **AND**
* **AS**
* **BETWEEN**
* **BY**
* **CASE**
* **CAST**
* **CONSTRAINT**
* **CREATE**
* **CROSS**
* **CUBE**
* **CURRENT_DATE**
* **CURRENT_TIME**
* **CURRENT_TIMESTAMP**
* **CURRENT_USER**
* **DEALLOCATE**
* **DELETE**
* **DESCRIBE**
* **DISTINCT**
* **DROP**
* **ELSE**
* **END**
* **ESCAPE**
* **EXCEPT**
* **EXECUTE**
* **EXISTS**
* **EXTRACT**
* **FALSE**
* **FOR**
* **FROM**
* **FULL**
* **GROUP**
* **GROUPING**
* **HAVING**
* **IN**
* **INNER**
* **INSERT**
* **INTERSECT**
* **INTO**
* **IS**
* **JOIN**
* **LEFT**
* **LIKE**
* **LOCALTIME**
* **LOCALTIMESTAMP**
* **NATURAL**
* **NORMALIZE**
* **NOT**
* **NULL**
* **ON**
* **OR**
* **ORDER**
* **OUTER**
* **PREPARE**
* **RECURSIVE**
* **RIGHT**
* **ROLLUP**
* **SELECT**
* **TABLE**
* **THEN**
* **TRUE**
* **UESCAPE**
* **UNION**
* **UNNEST**
* **USING**
* **VALUES**
* **WHEN**
* **WHERE**
* **WITH**

.. sql-spark-reserved-keywords-end


.. _sql-spark-skew:

Skew
--------------------------------------------------

.. sql-spark-skew-start

When Spark SQL runs domain tables and database tables it partitions the work and distributes each partition to an individual executor. When each partition is equal in size each executor is assigned an equal amount of work.

Skew occurs when one partition is assigned a greater amount of work than other partitions. All of the executors assigned lesser amounts of work will finish first, and then wait for the executor that was assigned the greater amount of work to finish.

Skew increases the amount of time it takes to finish processing. Small amounts of skew are common and are sometimes unavoidable. Large amounts of skew can lead to increased costs and increased runtimes.

.. sql-spark-skew-end


.. _sql-spark-skew-common-causes:

Common causes of skew
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-skew-common-causes-start

Common causes of skew include:

* Unintended duplication of values in upstream tables. Removing this duplication helps prevent skew.
* Values that are not needed in the final output, including **NULL** values or placeholders for **NULL** values, such as "1900-01-01". Filter these values out to prevent them from causing skew.

  If these values are required, one approach is to replace them with a primary key. For example:

  .. code-block:: none

     COALESCE(NULLIF({field}, ‘{bad_value}'), _uuid_pk)

  .. note:: Replacing a value that causes skew with primary key works because:

     * A primary key is a well-distributed field. All records have a unique primary key, which ensures that distribution of work is even across executors.
     * The value of a primary key will never match to a value on the other side of a **JOIN** operation. The non-match is the same result as what would happen with the bad **NULL** or placeholder value the primary key replaced.

.. sql-spark-skew-common-causes-end


.. _sql-spark-skew-avoiding:

Avoiding skew
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-skew-avoiding-start

To avoid large amounts of skew:

* Ensure :ref:`window functions <sql-spark-with-clause>` are partitioned by fields in a **PARTITION BY()** clause.

  .. caution:: A window function without a **PARTITION BY()** clause is calculated by a single executor.

* Ensure that fields that are used to join tables within :ref:`JOIN operations <sql-spark-join-clause>` are well-distributed.

.. sql-spark-skew-avoiding-end


.. _sql-spark-skew-avoiding-join-operations:

JOIN operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. sql-spark-skew-avoiding-join-operations-start

One-to-many and many-to-many :ref:`JOIN operations <sql-spark-join-clause>` result in tables with duplicated results. This is sometimes the intended outcome, but more often it is unintended.

One-to-many and many-to-many **JOIN** operations often cause incorrect aggregate calculations. High duplication rates lead to skew, increased costs, and increased runtimes. A small amount of duplication repeated across many **JOIN** operations can cause exponential growth in the number of records for a given join key.

Avoid duplication in **JOIN** operations by:

* Setting good values for primary keys, especially for domain tables.
* Avoiding using all fields in the table as primary key values. This may introduce bad data or lead to higher rates of duplication.
* Confirming the uniqueness of fields before using them in a **JOIN** operation.
* Avoiding the use of :ref:`DISTINCT <sql-spark-select-distinct-statement>` statements. Use the :ref:`GROUP BY <sql-spark-group-by-clause>` clause instead.

  Fields in a **GROUP BY** clause are always unique by grouping and can be used in a **JOIN** operation without risk of duplication.
* Using the **db/unique** semantic tag on fields that are supposed to be unique.

  This semantic tag adds an extra check to ensure that table results are unique by that field. If unexpected duplication occurs it shows as a warning in database notiications.

The following SQL query can help find **JOIN** operations with high duplication rates.

.. code-block:: none
   :linenos:

   SELECT
     {field1}
     ,COUNT(*)
   FROM {table}
   GROUP BY 1
   ORDER BY 2 DESC
   LIMIT 100

.. sql-spark-skew-avoiding-join-operations-end

.. sql-spark-skew-avoiding-join-operations-note-start

.. note:: **JOIN** operations are processed in the defined order. Even when join keys are unique for each table and are evenly distributed, they can cause skew when more than two tables are joined. For example:

   .. code-block:: none
      :linenos:
      :emphasize-lines: 2-4

      SELECT
        {field1}
        ,{field2}
        ,{field3}
      FROM {tableA} a
      LEFT JOIN {tableB} b
      ON a.{joinkey}1 = b.{joinkey}1
      LEFT JOIN {tableC} c
      ON b.{joinkey}2 = c.{joinkey}2

   If "Table A" has many keys that are not present in "Table B" then the **LEFT JOIN** operation between those tables will result in an intermediate table with many records where the value is **NULL**. This creates skew during the second **JOIN** operation between tables B and C.

.. sql-spark-skew-avoiding-join-operations-note-end


.. _sql-spark-skew-avoiding-partition-by:

PARTITION BY clauses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. sql-spark-skew-avoiding-partition-by-start

Use a query to help identify which field is causing skew in a **PARTITION BY** clause :ref:`within a window function <sql-spark-window-functions>`. Run the following query for each ``{field}`` in the **PARTITION BY** clause:

.. code-block:: none
   :linenos:
   :emphasize-lines: 2-5

   SELECT
     {field1}
     ,{field2}
     ,{field3}
     ,{field4}
     ,COUNT(*)
   FROM {table}
   GROUP BY 1,2,3,4
   ORDER BY 5 DESC
   LIMIT 100

Fields that appear more often are sources of skew. A field that appears more often than others may be causing a high amount of skew and should be filtered out or :ref:`converted to a primary key <sql-spark-skew-common-causes>`.

.. sql-spark-skew-avoiding-partition-by-end


.. _sql-spark-skew-avoiding-frequency-cardinality:

High frequency, low cardinality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. sql-spark-skew-avoiding-frequency-cardinality-start

In some situations a **JOIN** operation must be done using a high frequency or low cardinality field. For example the "action type" for email engagement data may have a small number of types: "send", "open", "click". A **JOIN** operation on the "action type" will cause a single executor to process all of the "send" action types.

Salting and hashing the joining keys can turn high frequency or low cardinality fields into values that can be spread across a greater number of executors. This will reduce skew, but will also increase the total amount of data that needs processing.

Ask your Amperity representative about using salting and hashing to mitigate skew with high frequency or low cardinality fields.

.. sql-spark-skew-avoiding-frequency-cardinality-end


.. _sql-spark-recommendation-subqueries:

Subqueries
--------------------------------------------------

.. sql-spark-recommendation-subqueries-start

A subquery can be useful for shaping data prior to running a query. A subquery is a task that is required to be completed before additional processing can be performed. A well-formed subquery is fast and low risk. A poorly formed subquery will affect performance. Keep the following tips in mind when using a subquery:

#. Do not join to an outer query from a subquery, as it may cause the subquery to run recursively for every value of the join key in the outer query. This may cause the subquery to run many times, or even millions of times. This type of subquery is sometimes referred to as a correlated subquery. The best way to avoid them is to never join between the inner and outer queries.
#. Each level of a subquery adds overhead. The fewer levels within a subquery, the easier it is to optimize the query. Try to flatten queries using joins instead of using additional levels. If you need to pull data into a subquery for multiple fields, try to use a single subquery instead of many.
#. Remove columns or use as few columns in a subquery as possible. For example, use:

   .. code-block:: none

      SELECT
        column_1
       ,column_2
      FROM

   instead of

   .. code-block:: none

      SELECT
        *
      FROM

   This will reduce the amount of data that must be processed. 

.. sql-spark-recommendation-subqueries-end


.. _sql-spark-recommendation-whitespace:

Whitespace
--------------------------------------------------

.. sql-spark-recommendation-whitespace-start

To make the code easier to read it is important that the correct complement of spacing is used. Do not crowd code or remove natural language spaces.

.. sql-spark-recommendation-whitespace-end


.. _sql-spark-recommendation-whitespace-line-spacing:

Line spacing
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-whitespace-line-spacing-start

Always include newlines and vertical space:

* before **AND** or **OR**
* after semicolons to separate queries for easier reading
* after each keyword definition
* before a comma when separating multiple columns into logical groups
* to separate code into related sections, which helps to ease the readability of large chunks of code.

Putting commas and conjunctions at the start of the line makes it easier to comment out a single line without disturbing the rest of the query

.. code-block:: sql
   :linenos:

   SELECT a.title
     ,a.release_date
     --,a.recording_date
     ,a.production_date
   FROM albums AS a
   WHERE a.title = 'Charcoal Lane'
     OR a.title = 'The New Danger'

.. sql-spark-recommendation-whitespace-line-spacing-end


.. _sql-spark-recommendation-whitespace-spaces:

Spaces
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-recommendation-whitespace-spaces-start

Spaces should be used to line up the code so that the root keywords all start on the same character boundary, and also so that this makes it easy to keep track of where you are in a query that may be multiple layers deep.

.. code-block:: sql
   :linenos:

   (SELECT f.species_name
     ,AVG(f.height) AS `average_height`
     ,AVG(f.diameter) AS `average_diameter`
   FROM flora AS f
   WHERE f.species_name = 'Banksia'
     OR f.species_name = 'Sheoak'
     OR f.species_name = 'Wattle'
   GROUP BY f.species_name, f.observation_date)

   UNION ALL

   (SELECT b.species_name
     ,AVG(b.height) AS `average_height`
     ,AVG(b.diameter) AS `average_diameter`
   FROM botanic_garden_flora AS b
   WHERE b.species_name = 'Banksia'
     OR b.species_name = 'Sheoak'
     OR b.species_name = 'Wattle'
   GROUP BY b.species_name, b.observation_date)

Although not exhaustive always include spaces:

* before and after equals ( = )
* after commas ( , )
* surrounding apostrophes ( ' ) where not within parentheses or with a trailing comma or semicolon.

.. code-block:: sql
   :linenos:

   SELECT a.title, a.release_date, a.recording_date
   FROM albums AS a
   WHERE a.title = 'Charcoal Lane'
     OR a.title = 'The New Danger'

.. sql-spark-recommendation-whitespace-spaces-end


.. _sql-spark-with-clause:

WITH clause
==================================================

.. sql-spark-with-clause-start

The **WITH** clause defines a `common table expression (CTE) <https://spark.apache.org/docs/3.5.5/sql-ref-syntax-qry-select-cte.html>`__ |ext_link|.

.. sql-spark-with-clause-end

.. sql-spark-with-clause-caution-start

.. caution:: A window function with an **OVER** statement that does not include a **PARTITION BY** clause often leads to performance issues when the **OVER** statement is asked to run across a large number of rows.

.. sql-spark-with-clause-caution-end


.. _sql-spark-lateral-view-clause:

LATERAL VIEW clause
==================================================

.. sql-spark-lateral-view-clause-start

The **LATERAL VIEW** clause generates a virtual table containing one or more rows, where each row is applied to the original output row.

Use **LATERAL VIEW OUTER** to return **NULL** if the input array or map is empty or **NULL**.

.. note:: The **LATERAL VIEW** clause is often used along with the **EXPLODE** generator function.

For example, the following common table expression generates virtual tables for email and physical addresses:

.. code-block:: sql
   :linenos:

   WITH
     emails AS (
       SELECT
         unique_id
         ,UPPER(em.email_address) AS email_address
       FROM customer_table
       LATERAL VIEW OUTER EXPLODE(email) AS em
     ),
     addresses AS (
       SELECT
         unique_id
         ,UPPER(ad.address) AS `address`
         ,UPPER(ad.address2) AS `address2`
         ,UPPER(ad.city) AS `city`
         ,UPPER(ad.state) AS `state`
         ,UPPER(ad.country) AS `country`
         ,ad.zip AS `postal`
         ,ad.zip4 AS `postal4`
       FROM customer_table
       LATERAL VIEW OUTER EXPLODE(address) AS ad
     ),

after which you can use the **SELECT** statement to select individual columns from the virtual tables, and then join them:

.. code-block:: sql
   :linenos:

   SELECT
     c.unique_id AS `uuid`
     ,a.address
     ,a.address2
     ,a.city
     ,a.state
     ,a.country
     ,a.postal
     ,a.postal4
     ,e.email_address AS `email`
   FROM customer_table c
   LEFT JOIN emails e ON e.unique_id = c.unique_id
   LEFT JOIN addresses a ON a.v = c.unique_id

.. sql-spark-lateral-view-clause-end


.. _sql-spark-select-statement:

SELECT statement
==================================================

.. sql-spark-select-statement-start

The **SELECT** statement is used to define a set of data to be returned from a data table. The set of returned data is often referred to as the result-set. Use the **SELECT** statement to retrieve rows from any table.

.. sql-spark-select-statement-end


.. _sql-spark-select-distinct-statement:

SELECT DISTINCT statement
==================================================

.. sql-spark-select-distinct-statement-start

The **SELECT DISTINCT** statement is used instead of **SELECT** to return only distinct rows of data.

.. sql-spark-select-distinct-statement-end


.. _sql-spark-from-clause:

FROM clause
==================================================

.. sql-spark-from-clause-start

The **FROM** clause specifies the name of the data table against which the SQL query is run and is part of every **SELECT** statement.

.. sql-spark-from-clause-end


.. _sql-spark-join-clause:

JOIN operations
==================================================

.. sql-spark-join-clause-start

Spark SQL supports all **JOIN** operations available in standard SQL.

.. warning:: Joining on fields with many matching values can be slow and can :ref:`introduce skew <sql-spark-skew>`. Spark SQL finds the match between each possible pair of matching values and the number of pairs goes up by the product of the matching duplicates in each table.

   Joining two tables with 1 million records in each table, where each record in one table matches only 1 record in the other will result in 1 million pairs.

   Joining two tables with 1 million records in each table, where all the records match will result in 1 trillion records.

   :ref:`One-to-many and many-to-many JOIN operations <sql-spark-skew-avoiding-join-operations>` often cause incorrect aggregate calculations. High duplication rates lead to skew, increased costs, and increased runtimes.

.. sql-spark-join-clause-end


.. _sql-spark-join-on-clause:

ON() clause
--------------------------------------------------

.. sql-spark-join-on-clause-start

Use the **ON()** clause to specify the join criteria. Contents of the **ON()** clause **must** be wrapped in parentheses.

For example:

.. code-block:: sql
   :linenos:

   FULL JOIN table_name AS tn
   ON (Members.`amperity_id` = tn.`Members_PK`)

.. sql-spark-join-on-clause-end


.. _sql-spark-join-using-clause:

USING() clause
--------------------------------------------------

.. sql-spark-join-using-clause-start

The **USING()** clause can be applied on column names to specify the join criteria. Contents of the **USING()** clause **must** be wrapped in parentheses.

For example:

.. code-block:: sql
   :linenos:

   FULL JOIN table_name AS tn
   USING (column_name)

.. sql-spark-join-using-clause-end


.. _sql-spark-cross-join-clause:

CROSS JOIN
--------------------------------------------------

.. sql-spark-cross-join-clause-start

A **CROSS JOIN** returns a Cartesian product. A Cartesian product combines every item in the first table with every item in the second. For example, if table A has three items and table B has three items, the Cartesian product is 9 pairs.

A **CROSS JOIN** should be avoided due to typical size of tables in Amperity databases, which can often have millions of rows.

A Cartesian product in Amperity between any two tables is often a very, very large number of pairs and, as a result, is an expensive operation. It is recommended to optimize your Spark SQL queries to avoid implicit cross joins.

.. tip:: Take steps to avoid implicit cross-joins:

   #. Use the **ON()** or **USING()** clauses with any **JOIN** statement.
   #. For situations where you need to run a **SELECT** statement like 

      ::

         SELECT * FROM Table_A, Table_B

      first filter out **NULL** values before running the **SELECT** statement.

.. sql-spark-cross-join-clause-end


.. _sql-spark-full-outer-join-clause:

FULL OUTER JOIN
--------------------------------------------------

.. sql-spark-full-outer-join-clause-start

A **FULL OUTER JOIN** returns all of the rows in both tables A and B, no matter whether there is a row in the other table with the same key value. Where there is a matching key value, columns from the other table will be brought in, where there is no matching value for key columns from the other table will be set to **NULL**. While there is no filtering applied in a **FULL OUTER JOIN**, rows that match on the key are only included once, so the row count of the results will always be at most equal to the count of table A + the count of table B, and is considerably smaller.

.. sql-spark-full-outer-join-clause-end


.. _sql-spark-inner-join-clause:

INNER JOIN
--------------------------------------------------

.. sql-spark-inner-join-clause-start

An **INNER JOIN** returns only those rows where there are values for the field key in both tables. Any rows in either table A or table B that have a value for key that does not appear in the other table are not returned.

.. sql-spark-inner-join-clause-end


.. _sql-spark-left-join-clause:

LEFT JOIN
--------------------------------------------------

.. sql-spark-left-join-clause-start

The **LEFT JOIN** clause joins rows from two tables. For a **LEFT JOIN**, each row in the left table is joined with all matching rows from the right table. For rows with no match in the right table, the join is completed with **NULL** to represent column values.

For example:

.. code-block:: sql

   SELECT *
   FROM (VALUES 1, 2) t("left")
   LEFT JOIN (VALUES 1, 1) u("right")
   ON t."left" = u."right";

will return a table similar to:

.. code-block:: mysql

   -------- --------
    left     right
   -------- --------
    1        1
    1        1
    2        NULL
   -------- --------

.. sql-spark-left-join-clause-end

.. sql-spark-left-join-clause-note-start

.. note:: In some situations you may want to use an **LEFT ANTI JOIN**. A **LEFT ANTI JOIN** returns values from the left-side table when they do not have matches on the right-side table. Use a **LEFT ANTI JOIN** to avoid performance issues that may be caused by a broadcast join.

.. sql-spark-left-join-clause-note-end


.. _sql-spark-outer-join-clause:

OUTER JOIN
--------------------------------------------------

.. sql-spark-outer-join-clause-start

An **OUTER JOIN** clause brings all of the rows from the named table--left for **LEFT JOIN**, right for **RIGHT JOIN**--but the overlapping rows can be removed by adding the condition **WHERE <key value in the other table> IS NULL**. You can do the same to select the non-intersecting portion of a **FULL OUTER** join by using **OR** with both key values as **IS NULL**.

Same as **LEFT JOIN** and **RIGHT JOIN**.

.. sql-spark-outer-join-clause-end


.. _sql-spark-right-join-clause:

RIGHT JOIN
--------------------------------------------------

.. sql-spark-right-join-clause-start

The **RIGHT JOIN** clause joins rows from two tables. For a **RIGHT JOIN**, each row in the right table is joined with all matching rows from the left table. For rows with no match in the left table, the join is completed with **NULL** to represent column values.

.. sql-spark-right-join-clause-end


.. _sql-spark-where-clause:

WHERE clause
==================================================

.. sql-spark-where-clause-start

The **WHERE** clause is used to filter records, and then return only those records that match the specified condition and value.

The **WHERE** clause can be combined with the **AND**, **OR**, and **NOT** operators and the **IN**, **NOT IN**, **EXISTS**, and **NOT EXISTS** expressions.

.. sql-spark-where-clause-end


.. _sql-spark-where-clause-operator-and:

AND operator
--------------------------------------------------

.. sql-spark-where-clause-operator-and-start

The **AND** operator is used to filter records based on more than one condition and displays a record if all the conditions separated by **AND** are **TRUE**.

.. sql-spark-where-clause-operator-and-end


.. _sql-spark-where-clause-operator-or:

OR operator
--------------------------------------------------

.. sql-spark-where-clause-operator-or-start

The **OR** operator is used to filter records based on more than one condition and displays a record if any of the conditions separated by **OR** is **TRUE**.

.. sql-spark-where-clause-operator-or-end


.. _sql-spark-where-clause-operator-not:

NOT operator
--------------------------------------------------

.. sql-spark-where-clause-operator-not-start

The **NOT** operator displays a record if the condition is **NOT TRUE**.

.. sql-spark-where-clause-operator-not-end


.. _sql-spark-where-clause-expression-in:

IN expression
--------------------------------------------------

.. sql-spark-where-clause-expression-in-start

The **IN** expression returns a **TRUE** or **FALSE** value or **UNKNOWN** when the returned list contains **NULL**.

.. tip:: The **IN** expression is equivalent to the **OR** operator. For example: **IN (a, b)** is equivalent to **a OR b**.

.. sql-spark-where-clause-expression-in-end


.. _sql-spark-where-clause-expression-not-in:

NOT IN expression
--------------------------------------------------

.. sql-spark-where-clause-expression-not-in-start

The **NOT IN** expression returns a **TRUE** or **FALSE** value or **UNKNOWN** when the returned list contains **NULL**. Use **WHERE** followed by **NOT IN** when the argument within the **NOT IN** expression is:

* A small table with no more than a few thousand rows *and* is not expected to grow over time.
* A hard-coded list of values. For example:

  ::

     WHERE color NOT IN ('red', 'blue', 'green')

.. sql-spark-where-clause-expression-not-in-end

.. sql-spark-where-clause-expression-not-in-warning-start

.. warning:: The use of **WHERE** followed by **NOT IN** will cause performance issues when the argument within **NOT IN** is a large table or large query. This is because Spark SQL will implement the table or query as a broadcast join, and then attempt to broadcast that table or query to every worker node in the Spark cluster. This may cause Spark SQL to run slowly or result in out-of-memory errors.

   To prevent slow queries or out-of-memory errors use a **LEFT ANTI JOIN** operation instead of a **WHERE** followed by **NOT IN** a table or a query. For example:

   .. code-block:: sql

      SELECT *
      FROM table_a
      LEFT ANTI JOIN (SELECT id FROM table_b) AS remove
      ON table_a.id = remove.id

   instead of:

   .. code-block:: sql

      SELECT *
      FROM table_a
      WHERE table_a.id NOT IN (SELECT id FROM table_b)

.. sql-spark-where-clause-expression-not-in-warning-end


.. _sql-spark-where-clause-expression-exists:

EXISTS expression
--------------------------------------------------

.. sql-spark-where-clause-expression-exists-start

The **EXISTS** expression returns **TRUE** when the subquery to which it refers returns one or more rows, or returns **FALSE**.

.. sql-spark-where-clause-expression-exists-end


.. _sql-spark-where-clause-expression-not-exists:

NOT EXISTS expression
--------------------------------------------------

.. sql-spark-where-clause-expression-not-exists-start

The **NOT EXISTS** returns **TRUE** when the subquery to which it refers returns no rows or zero rows, or returns **FALSE**.

.. tip:: The **NOT EXISTS** expression runs the same way in Spark SQL *and* Presto SQL. This is useful for running the same query in the **Customer 360** *and* the **Queries** pages. For example:

   .. code-block:: sql

      SELECT *
      FROM table_a
      WHERE table_a.id NOT EXISTS (SELECT id FROM table_b)

   is similar to:

   .. code-block:: sql

      SELECT *
      FROM table_a
      LEFT ANTI JOIN (SELECT id FROM table_b) AS remove
      ON table_a.id = remove.id

   The important difference is **WHERE** followed by **NOT EXISTS** runs the same way in both Spark SQL and Presto SQL, wheres **LEFT ANTI JOIN** may only be used in Spark SQL.

.. sql-spark-where-clause-expression-not-exists-end


.. _sql-spark-case-expression:

CASE expression
==================================================

.. sql-spark-case-expression-start

The standard SQL **CASE** expression has two forms: simple and searched.

.. note:: If a **CASE** expression is too long, add a new line between **WHEN** and **THEN** clauses to make the line more readable.

.. sql-spark-case-expression-end


.. _sql-spark-case-expression-simple:

Simple form
--------------------------------------------------

.. sql-spark-case-expression-simple-start

The simple form searches each value expression from left to right until it finds one that equals expression:

.. code-block:: none

   CASE expression
     WHEN value THEN result
     [ WHEN ... ]
     [ ELSE result ]
   END

The result for the matching value is returned.

If no match is found, the result from the **ELSE** clause is returned if it exists, otherwise **NULL** is returned:

.. code-block:: none

   SELECT a,
     CASE a
       WHEN 1 THEN 'one'
       WHEN 2 THEN 'two'
       ELSE 'many'
     END

.. sql-spark-case-expression-simple-end


.. _sql-spark-case-expression-searched:

Searched form
--------------------------------------------------

.. sql-spark-case-expression-searched-start

The searched form evaluates each boolean condition from left to right until one is true and returns the matching result:

.. code-block:: sql

   CASE
     WHEN condition THEN result
     [ WHEN ... ]
     [ ELSE result ]
   END

If no conditions are true, the result from the **ELSE** clause is returned if it exists, otherwise **NULL** is returned:

.. code-block:: sql

   SELECT a, b,
     CASE
       WHEN a = 1 THEN 'aaa'
       WHEN b = 2 THEN 'bbb'
       ELSE 'ccc'
     END

.. sql-spark-case-expression-searched-end


.. _sql-spark-group-by-clause:

GROUP BY clause
==================================================

.. sql-spark-group-by-clause-start

The **GROUP BY** clause divides the output of a **SELECT** statement into groups of rows containing matching values. A simple **GROUP BY** clause may contain any expression composed of input columns or it may be an ordinal number selecting an output column by position, starting at one.

The following queries are equivalent. They both group the output by the nationkey input column with the first query using the ordinal position of the output column and the second query using the input column name:

.. code-block:: sql

   SELECT
     COUNT(*)
     ,nationkey
   FROM customer
   GROUP BY 2

is equivalent to:

.. code-block:: sql

   SELECT
     COUNT(*)
     ,nationkey
   FROM customer
   GROUP BY nationkey

**GROUP BY** clauses can group output by input column names not appearing in the output of a select statement. For example, the following query generates row counts for the customer table using the input column "mktsegment":

.. code-block:: sql

   SELECT
     COUNT(*)
   FROM customer
   GROUP BY mktsegment

returns a table similar to:

.. code-block:: mysql

     _col0
    -------
     29968
     30142
     30189
     29949
     29752
    (5 rows)

When a **GROUP BY** clause is used in a **SELECT** statement all output expressions must be either aggregate functions or columns present in the **GROUP BY** clause.

.. sql-spark-group-by-clause-end


.. _sql-spark-having-clause:

HAVING clause
==================================================

.. sql-spark-having-clause-start

The **HAVING** clause is used to sort a result set by one or more output expressions. Use in conjunction with aggregate functions and the **GROUP BY** clause to control which groups are selected. A **HAVING** clause eliminates groups that do not satisfy the given conditions and filters groups after groups and aggregates are computed.

For example:

.. code-block:: sql
   :linenos:

   SELECT
     COUNT(*)
     ,segment
     ,key
     ,CAST(SUM(actual_loyalty) AS bigint) AS loyalty
   FROM Customer360
   GROUP BY segment, key
   HAVING SUM(actual_loyalty) > 5700000
   ORDER BY loyalty DESC;

returns a table similar to:

.. code-block:: mysql

   ------- ------------ ------ ----------
    id      segment      key    loyalty
   ------- ------------ ------ ----------
    1272    CARS         19     5856939
    1253    PLANES       14     5794887
    1248    HOTELS       9      5784628
    1243    HOTELS       12     5757371
    1231    CARS         3      5753216
    1251    CARS         2      5719140
    1247    PLANES       8      5701952
   ------- ------------ ------ ----------

.. sql-spark-having-clause-end


.. _sql-spark-window-functions:

Window functions
==================================================

.. sql-spark-window-functions-start

Window functions are a way to evaluate rows around each row as it is being evaluated. Window functions are flexible for controlling how a window is made and which rows to consider.

Most window functions only require a small subset and use **GROUP BY** to group using the unique values of a specific field, and then selecting a row from that group.

.. caution:: From a performance point of view, window functions tend to be performant when the **OVER()** function includes a **PARTITION BY** clause over a well-distributed field.

A common use in Amperity might look like this:

.. code-block:: none

   FIRST_VALUE(LOWER(EMAIL_ADDRESS_)) OVER (
     PARTITION BY amperity_id
     ORDER BY merged_date DESC
   ) AS email_address,

It says "Group the records by amperity_id, and for each group return the one with the latest merged_date". Alternately: "Return the most recent email address for each customer." The window function bits do the following:

* **FIRST_VALUE(<field name>)** The **FIRST_VALUE()** window function picks the first record out of some set of records. In this case, it is selecting from the window or partition, whichever is defined next.
* **OVER()** The **OVER()** function sets up the window in which records are found. This function should include both **PARTITION BY** and **ORDER_BY** functions.
* **PARTITION BY amperity_id** The **PARTITION BY <field name>** function behaves in a way analogous to a **GROUP BY** in that it groups all records with unique values for the specified field together. So here it creates a subset of rows for each Amperity ID.
* **ORDER BY merged_date DESC** The **ORDER BY()** function is just like it is in a **SELECT** statement, it sorts the rows being operated on. The only difference is that in this case, it is only sorting the rows within the partition, so in this example it is sorting the rows for each Amperity ID. And **DESC** simply says sort in descending order, so most recent date is first.
* **AS <field name>** The final clause of the statement above is not part of the window function at all, but is the **AS** statement you've used before to set the name of the projected column. In this example the results will be put in a column with the name email address.

.. sql-spark-window-functions-end


.. _sql-spark-order-by-clause:

ORDER BY clause
==================================================

.. sql-spark-order-by-clause-start

The **ORDER BY** clause is used to sort a result set by one or more output expressions.

.. code-block:: none

   ORDER BY expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...]

Each expression may be composed of output columns or it may be an ordinal number selecting an output column by position, starting at one.

The default sort order is ascending (**ASC**). **NULL** values will sort first when the sort order is ascending and will sort last when the sort order is descending (**DESC**). Use **NULLS FIRST** to sort **NULL** values first, regardless of sort order. Use **NULLS LAST** to sort **NULL** values last, regardless of sort order.

The **ORDER BY** clause is evaluated as the last step of a query after any **GROUP BY** or **HAVING** clause.

.. sql-spark-order-by-clause-end


.. _sql-spark-limit-clause:

LIMIT clause
==================================================

.. sql-spark-limit-clause-start

The **LIMIT** clause restricts the number of rows in the result set. The following example queries a large table, but the limit clause restricts the output to only have five rows (because the query lacks an **ORDER BY**, exactly which rows are returned is arbitrary):

.. code-block:: sql

   SELECT orderdate
   FROM orders
   LIMIT 5

returns a table similar to:

.. code-block:: mysql

    o_orderdate
   -------------
    1996-04-14
    1992-01-15
    1995-02-01
    1995-11-12
    1992-04-26
    (5 rows)

.. sql-spark-limit-clause-end


.. _sql-spark-operators:

Operators
==================================================

.. sql-spark-operators-start

An operator compares two data items, and then returns a result.

.. sql-spark-operators-end


.. _sql-spark-operator-between:

BETWEEN
--------------------------------------------------

.. sql-spark-operator-between-start

Use the **BETWEEN** operator to test if a value falls within the specified range using the syntax value **BETWEEN** min **AND** max:

.. code-block:: none

   SELECT 3 BETWEEN 2 AND 6

The statement shown above is equivalent to the following statement:

.. code-block:: none

   SELECT 3 >= 2 AND 3 <= 6

**Presence of NULL evaluates to NULL**

The presence of **NULL** will result in the statement evaluating to **NULL**:

.. code-block:: none

   SELECT NULL BETWEEN 2 AND 4

and:

.. code-block:: none

   SELECT 2 BETWEEN NULL AND 6

**String arguments must be of same type**

Use the **BETWEEN** operator to evaluate string arguments as long as the value, min, and max parameters are of the same type:

.. code-block:: none

   SELECT 'Paul' BETWEEN 'John' AND 'Ringo'

whereas this query will produce an error:

.. code-block:: none

   SELECT '2.3' BETWEEN 'John' AND '35.2'

.. sql-spark-operator-between-end


.. _sql-spark-operator-comparison:

Comparison operators
--------------------------------------------------

.. sql-spark-operator-comparison-start

The following comparison operators are available:

========   ===========
Operator   Description
========   ===========
**<**      Less than
**>**      Greater than
**<=**     Less than or equal to
**>=**     Greater than or equal to
**=**      Equal
**<>**     Not equal
**!=**     Not equal (non-standard but popular syntax)
========   ===========

.. sql-spark-operator-comparison-end


.. _sql-spark-operator-comparison-all:

ALL
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-operator-comparison-all-start

Use **ALL** together with comparison operators in the following way:

.. code-block:: none

    expression operator ALL ( subquery )

For example:

.. code-block:: none

   SELECT 21 < ALL (VALUES 19, 20, 21); -- false

Examples of **ALL** comparison operator combinations:

====================    ===========
Expression              Meaning
====================    ===========
A = ALL (subquery)      Evaluates to **TRUE** when A is equal to all values.
A <> ALL (subquery)     Evaluates to **TRUE** when A does not match any value.
A < ALL (subquery)      Evaluates to **TRUE** when A is smaller than the smallest value.
====================    ===========

.. sql-spark-operator-comparison-all-end


.. _sql-spark-operator-comparison-any:

ANY
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-operator-comparison-any-start

Use **ANY** together with comparison operators in the following way:

.. code-block:: none

   expression operator ANY ( subquery )

For example:

.. code-block:: none

   SELECT 21 < ALL (VALUES 19, 20, 21); -- false

Examples of **ANY** comparison operator combinations:

====================    ===========
Expression              Meaning
====================    ===========
A = ANY (subquery)      Evaluates to **TRUE** when A is equal to any of the values.

                        .. note:: This form is equivalent to A IN (subquery).
A <> ANY (subquery)     Evaluates to **TRUE** when A does not match one or more values.
A < ANY (subquery)      Evaluates to **TRUE** when A is smaller than the biggest value.
====================    ===========

.. sql-spark-operator-comparison-any-end


.. _sql-spark-operator-comparison-some:

SOME
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-operator-comparison-some-start

Use **SOME** together with comparison operators in the following way:

.. code-block:: none

   expression operator SOME ( subquery )

For example:

.. code-block:: none

   SELECT 42 >= SOME (SELECT 41 UNION ALL SELECT 42 UNION ALL SELECT 43); -- true

Examples of **SOME** comparison operator combinations:

====================    ===========
Expression              Meaning
====================    ===========
A = SOME (subquery)     Evaluates to **TRUE** when A is equal to any of the values.

                        .. note:: This form is equivalent to A IN (subquery).

A <> SOME (subquery)    Evaluates to **TRUE** when A does not match one or more values.
A < SOME (subquery)     Evaluates to **TRUE** when A is smaller than the biggest value.
====================    ===========

.. sql-spark-operator-comparison-some-end


.. _sql-spark-operator-is-null:

IS NULL
--------------------------------------------------

.. sql-spark-operator-is-null-start

The **IS NULL** operator tests whether a value is **NULL**. This operator works for all data types.

Using **NULL** with **IS NULL** evaluates to **TRUE**:

.. code-block:: none

   SELECT NULL IS NULL

But any other constant does not evaluate to **FALSE**:

.. code-block:: none

   SELECT 3.0 IS NULL

.. sql-spark-operator-is-null-end


.. _sql-spark-operator-is-not-null:

IS NOT NULL
--------------------------------------------------

.. sql-spark-operator-is-not-null-start

The **IS NOT NULL** operator tests whether a value is not **NULL**. This operator works for all data types.

Using **NULL** with **IS NOT NULL** evaluates to **FALSE**:

.. code-block:: none

   SELECT NULL IS NOT NULL

But any other constant evaluates **TRUE**:

.. code-block:: none

   SELECT 3.0 IS NOT NULL

.. sql-spark-operator-is-not-null-end


.. _sql-spark-pivot-operator:

PIVOT operator
==================================================

.. sql-spark-pivot-operator-start

The **PIVOT** operator allows data to be reshaped into a new table. Use values from within a field to define column names, and then group rows by those values and by other fields, such as the Amperity ID. A pivot must declare *how* data is to be reshaped -- **SUM()**, **MAX()**, or by some other grouping or aggregation -- and then must declare from which field in the existing table the new column names are derived.

For example, a transactions table has a field with three values: **PUR** (purchases), **RET** (returns), and **OTH** (other). Use **PIVOT** to return a table that contains columns named **Purchases**, **Returns**, and **Other**, each containing the sum for that value in the transactions table, and then a row for each Amperity ID and brand:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,brand
     ,PUR AS Purchases
     ,RET AS Returns
     ,OTH AS Other
   FROM transactions
   PIVOT
     (
       SUM(net_amount)
       FOR category IN ('PUR', 'RET', 'OTH')
     )

.. sql-spark-pivot-operator-end


.. _sql-spark-functions:

Functions
==================================================

.. sql-spark-functions-start

A function is a SQL statement that accepts input parameters, performs actions, and then returns results.

.. sql-spark-functions-end

.. sql-spark-functions-note-start

.. note:: Amperity uses a subset of the complete list of functions available in |ext_sparksql_version_current|, many of which can be useful depending on the type of query.

.. sql-spark-functions-note-end

.. sql-spark-functions-list-start

The following list contains some of the most frequently used functions for building segments via the **SQL Segment Editor** (alphabetized):

* :ref:`sql-spark-function-abs`
* :ref:`sql-spark-function-avg`
* :ref:`sql-spark-function-cast`
* :ref:`sql-spark-function-coalesce`
* :ref:`sql-spark-function-collect-list`
* :ref:`sql-spark-function-collect-set`
* :ref:`sql-spark-function-concat`
* :ref:`sql-spark-function-count`
* :ref:`sql-spark-function-count-distinct`
* :ref:`sql-spark-function-current-date`
* :ref:`sql-spark-function-current-timestamp`
* :ref:`sql-spark-function-date`
* :ref:`sql-spark-function-date-add`
* :ref:`sql-spark-function-date-trunc`
* :ref:`sql-spark-function-datediff`
* :ref:`sql-spark-function-decode`
* :ref:`sql-spark-function-dense-rank`
* :ref:`sql-spark-function-explode`
* :ref:`sql-spark-function-first-value`
* :ref:`sql-spark-function-if`
* :ref:`sql-spark-function-isnotnull`
* :ref:`sql-spark-function-isnull`
* :ref:`sql-spark-function-last`
* :ref:`sql-spark-function-least`
* :ref:`sql-spark-function-left`
* :ref:`sql-spark-function-length`
* :ref:`sql-spark-function-locate`
* :ref:`sql-spark-function-lower`
* :ref:`sql-spark-function-max`
* :ref:`sql-spark-function-min`
* :ref:`sql-spark-function-months-between`
* :ref:`sql-spark-function-now`
* :ref:`sql-spark-function-ntile`
* :ref:`sql-spark-function-nullif`
* :ref:`sql-spark-function-rand`
* :ref:`sql-spark-function-rank`
* :ref:`sql-spark-function-regexp-extract`
* :ref:`sql-spark-function-regexp-replace`
* :ref:`sql-spark-function-rlike`
* :ref:`sql-spark-function-round`
* :ref:`sql-spark-function-row-number`
* :ref:`sql-spark-function-sha2`
* :ref:`sql-spark-function-split`
* :ref:`sql-spark-function-strpos`
* :ref:`sql-spark-function-substr`
* :ref:`sql-spark-function-substring`
* :ref:`sql-spark-function-sum`
* :ref:`sql-spark-function-to-date`
* :ref:`sql-spark-function-to-timestamp`
* :ref:`sql-spark-function-translate`
* :ref:`sql-spark-function-trim`
* :ref:`sql-spark-function-upper`

.. sql-spark-functions-list-end


.. _sql-spark-function-abs:

ABS()
--------------------------------------------------

.. sql-spark-function-abs-start

Use the **ABS(expression)** function to return the absolute value of "expression".

.. sql-spark-function-abs-end


.. _sql-spark-function-abs-example-status-by-range:

Coalesce to empty (non-NULL) values
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-abs-example-apply-status-by-date-range-start

The following example is a common table expression that uses the **ABS()** function within a **CASE** statement to determine the how many days have passed since a customer's most recent purchase, and then to apply a lifecycle status to each set of customers who fall into each range: active, lapsed, dormant, prospect, or no status.

.. code-block:: sql
   :linenos:

   customer_lifecycle_status AS (
     SELECT
       c.amperity_id
       ,CASE
         WHEN ABS(DATEDIFF(tae.latest_order_datetime, current_date)) <= 365 THEN 'active'
         WHEN ABS(DATEDIFF(tae.latest_order_datetime, current_date)) > 365 THEN ''
         AND ABS(DATEDIFF(tae.latest_order_datetime, current_date)) <= 730 THEN 'lapsed'
         WHEN ABS(DATEDIFF(tae.latest_order_datetime, current_date)) > 730 THEN 'dormant'
         ELSE 'prospect'
       END AS lifecycle_status
     FROM Customer_360 c
     LEFT JOIN Transaction_Attributes_Extended tae
     ON c.amperity_id = tae.amperity_id
   ),

.. sql-spark-function-abs-example-apply-status-by-date-range-end


.. _sql-spark-function-avg:

AVG()
--------------------------------------------------

.. sql-spark-function-avg-start

Use the **AVG(x)** function to return the average of all input values.

.. sql-spark-function-avg-end


.. _sql-spark-function-cast:

CAST()
--------------------------------------------------

.. sql-spark-function-cast-start

Use the **CAST(field-or-expression AS type)** function to cast a "field" or an "expression" as "type". For example, to cast a varchar to a numeric or cast a date or datetime to a timestamp.

For example:

.. code-block:: sql

   CAST(order_date AS timestamp)

.. sql-spark-function-cast-end


.. _sql-spark-function-coalesce:

COALESCE()
--------------------------------------------------

.. sql-spark-function-coalesce-start

Use the **COALESCE(column_name, value)** function to return the first non-**NULL** argument. Use a value of ``""``, ``0``, or ``1``.

.. tip:: Some functions fails if they encounter NULL values. Use this function prior to the **CONCAT()** and **SUM()** functions to ensure they do not encounter **NULL** values.

.. sql-spark-function-coalesce-end

.. sql-spark-function-concat-note-about-null-start

.. note:: The **CONCAT()** function will return **NULL** if the value of any field is **NULL**. Use the **COALESCE()** function to coalesce to a zero-length string prior to concatenation. For example, use:

   .. code-block:: none

      CONCAT(COALESCE(firstname, ""), " ", COALESE(lastname, ""))

   to concatenate a **FullName** field.

.. sql-spark-function-concat-note-about-null-end


.. _sql-spark-function-coalesce-example-coalesce-to-empty-non-null-values:

Coalesce to empty (non-NULL) values
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-coalesce-example-coalesce-to-empty-non-null-start

.. code-block:: none

   ,COALESCE(column_name, "")

.. sql-spark-function-coalesce-example-coalesce-to-empty-non-null-end


.. _sql-spark-function-coalesce-example-coalesce-to-0-non-null-values:

Coalesce to 0 (non-NULL) values
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-coalesce-example-coalesce-to-0-non-null-values-start

.. code-block:: none

   ,COALESCE(column_name, 0)

.. sql-spark-function-coalesce-example-coalesce-to-0-non-null-values-end


.. _sql-spark-function-coalesce-example-coalesce-to-1-non-null-values:

Coalesce to 1 (non-NULL) values
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-coalesce-example-coalesce-to-1-non-null-values-start

.. code-block:: none

   ,COALESCE(column_name, 1)

.. sql-spark-function-coalesce-example-coalesce-to-1-non-null-values-end


.. _sql-spark-function-coalesce-example-coalesce-primary-keys:

Coalesce to primary keys
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-coalesce-example-coalesce-primary-keys-start

Values that are not needed in the final output, including **NULL** values or placeholders for **NULL** values, such as "1900-01-01" can be filtered out to prevent them from causing skew. If values are required, you can replace them with a primary key.

For example:

.. code-block:: none

   COALESCE(NULLIF({field}, ‘{bad_value}'), _uuid_pk)

.. sql-spark-function-coalesce-example-coalesce-primary-keys-end


.. _sql-spark-function-coalesce-example-handle-multiple-delimiter-types:

Multiple delimiter types
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_operator/source/blocklist_bad_values.rst
   :start-after: .. bad-values-blocklist-advanced-custom-domain-tables-start
   :end-before: .. bad-values-blocklist-advanced-custom-domain-tables-end


.. _sql-spark-function-coalesce-example-get-the-first-non-null-value:

Get the first non-NULL value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-coalesce-example-get-the-first-non-null-value-start

.. code-block:: none

   ,COALESCE(order_quantity, canceled_quantity, order_quantity) AS qty_coalesce

.. sql-spark-function-coalesce-example-get-the-first-non-null-value-end


.. _sql-spark-function-coalesce-example-add-column-account-for-null:

Add columns (accounting for NULL values)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-coalesce-example-add-column-account-for-null-start

.. code-block:: sql
   :linenos:

   COALESCE(order_quantity,0)
     + COALESCE(canceled_quantity,0)
     + COALESCE(canceled_quantity,0)
   AS qty_sum

.. sql-spark-function-coalesce-example-add-column-account-for-null-end


.. _sql-spark-function-coalesce-example-standardize-values-for-usa-states:

Standardize values for USA states
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-coalesce-example-standardize-values-for-usa-states-start

The following example standardizes values for all fifty states in the United States to only a two-character value, such as AK, AL, and AR. The **CASE** statement uses the following strings to determine:

#. The correct two-character value
#. The correct spelled out value
#. Other variations that appear in the data, which may be common (or known) abbreviations, misspellings, slang, or shortcuts

.. TODO: The following code block blows up if the directive is set to "sql". Keep it set to "none".

.. code-block:: none
   :linenos:

   CASE
     WHEN UPPER(TRIM(COALESCE(state))) IN ('AL','ALABAMA', 'BAMA') THEN 'AL'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('AK','ALASKA') THEN 'AK'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('AZ','ARIZONA') THEN 'AZ'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('AR','ARKANSAS') THEN 'AR'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('CA','CALIF','CALIFORNIA','CALIFORNIZ','CALIFRONIA') THEN 'CA'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('CO','COLORADO') THEN 'CO'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('CT','CONNECTICUT', 'CONNETICUT') THEN 'CT'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('DE','DELAWARE', 'DELWARE') THEN 'DE'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('FL','FLORIDA') THEN 'FL'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('GA','GEORGIA') THEN 'GA'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('HI','HAWAII', 'HAWAI\'I') THEN 'HI'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('ID','IDAHO') THEN 'ID'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('IL','ILLINOIS') THEN 'IL'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('IN','INDIANA') THEN 'IN'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('IA','IOWA') THEN 'IA'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('KS','KANSAS') THEN 'KS'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('KY','KENTUCKY') THEN 'KY'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('LA','LOUISIANA', 'LOUSIANA') THEN 'LA'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('ME','MAINE') THEN 'ME'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('MD','MARYLAND') THEN 'MD'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('MA','MASS','MASSACHUSETES','MASSACHUSETTS','MASSACHUSETTES') THEN 'MA'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('MI','MICHIGAN') THEN 'MI'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('MN','MINNESOTA') THEN 'MN'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('MS','MISSISSIPPI') THEN 'MS'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('MO','MISSOURI') THEN 'MO'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('MT','MONTANA') THEN 'MT'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('NE','NEBRASKA') THEN 'NE'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('NV','NEVADA') THEN 'NV'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('NH','NEW HAMPSHIRE') THEN 'NH'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('NJ','NEW JERSEY', 'JERSEY') THEN 'NJ'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('NM','NEW MEXICO') THEN 'NM'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('NY','NEW YORK') THEN 'NY'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('NC','NORTH CAROLINA') THEN 'NC'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('ND','NORTH DAKOTA') THEN 'ND'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('OH','OHIO') THEN 'OH'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('OK','OKLAHOMA') THEN 'OK'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('OR','ORE','OREGON','OREGONE') THEN 'OR'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('PA','PENNSYLVANIA') THEN 'PA'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('RI','RHODE ISLAND') THEN 'RI'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('SC','SOUTH CAROLINA') THEN 'SC'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('SD','SOUTH DAKOTA') THEN 'SD'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('TN','TENNESSEE') THEN 'TN'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('TX','TEXAS') THEN 'TX'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('UT','UTAH') THEN 'UT'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('VT','VERMONT') THEN 'VT'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('VA','VIRGINIA') THEN 'VA'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('WA','WASHINGTON') THEN 'WA'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('WV','WEST VIRGINIA') THEN 'WV'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('WI','WISCONSIN') THEN 'WI'
     WHEN UPPER(TRIM(COALESCE(state))) IN ('WY','WYOMING') THEN 'WY'
   ELSE NULL

.. sql-spark-function-coalesce-example-standardize-values-for-usa-states-end


.. _sql-spark-function-collect-list:

COLLECT_LIST()
--------------------------------------------------

.. sql-spark-function-collect-list-start

Use the **COLLECT_LIST(expression)** function to collect and return a list of non-unique elements, as defined by "expression".

.. note:: This function is non-deterministic because it depends on the order of the list of non-unique elements that are returned, which may be non-deterministic. Wrap the **COLLECT_LIST()** function in a **SORT_ARRAY()** function to return a deterministic list of non-unique elements.

.. sql-spark-function-collect-list-end


.. _sql-spark-function-collect-list-example-return-array-of-ordered-ids:

Return array of ordered IDs
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-collect-list-example-return-array-of-ordered-ids-start

Collect a list from the **Unified Transactions** table, and then returned it as an array of order IDs:

.. code-block:: sql
   :linenos:

   SELECT
     COLLECT_LIST(ut.order_id) AS array_order_ids 
   FROM Unified_Transactions AS ut 

.. sql-spark-function-collect-list-example-return-array-of-ordered-ids-end


.. _sql-spark-function-collect-set:

COLLECT_SET()
--------------------------------------------------

.. sql-spark-function-collect-set-start

Use the **COLLECT_LIST(expression)** function to collect and return a set of unique elements.

.. note:: This function is non-deterministic because it depends on the order of the list of unique elements that are returned, which may be non-deterministic. Wrap the **COLLECT_SET()** function in a **SORT_ARRAY()** function to return a deterministic list of unique elements.

.. sql-spark-function-collect-set-end


.. _sql-spark-function-concat:

CONCAT()
--------------------------------------------------

.. sql-spark-function-concat-start

Use the **CONCAT(column1, column2, columnN)** function to return a concatenation of all columns. This function returns **NULL** if any value of any field is **NULL**. Use the **COALESCE()** function to map fields to zero-length string values prior to using this function.

.. sql-spark-function-concat-end


.. _sql-spark-function-concat-example-concatenate-to-full-name:

Concatenate to full name
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-concat-example-concatenate-to-full-name-start

.. code-block:: none

   ,CONCAT(COALESCE(firstname, ""), " ", COALESE(lastname, ""))

.. sql-spark-function-concat-example-concatenate-to-full-name-end


.. _sql-spark-function-concat-example-concatenate-order-ids-and-dates:

Concatenate order IDs and dates
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-concat-example-concatenate-order-ids-and-dates-start

.. code-block:: none

   ,CONCAT(order_id, order_date) AS order_id

.. sql-spark-function-concat-example-concatenate-order-ids-and-dates-end


.. _sql-spark-function-concat-example-add-1-to-phone-numbers:

Add a +1 to phone numbers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-concat-example-add-1-to-phone-numbers-start

The following **CASE** statement uses the **TRIM()** function to find empty or NULL phone numbers, sets them to **NULL**, and then standardizes all phone numbers to add a +1:

.. code-block:: sql
   :linenos:

   CASE
     WHEN TRIM(phone) LIKE ''
     OR TRIM(phone) IS NULL
     THEN NULL
     ELSE CONCAT('+1','',REGEXP_REPLACE(phone,'[^0123456789]',''))
   END AS phone

.. sql-spark-function-concat-example-add-1-to-phone-numbers-end


.. _sql-spark-function-concat-ws:

CONCAT_WS()
--------------------------------------------------

.. sql-spark-function-concat-ws-start

Use the **CONCAT_WS(separator, [string | array(string)]+** function to return a concatenation of "string" or an "array" of "string", as separated by "separator".

.. sql-spark-function-concat-ws-end


.. _sql-spark-function-concat-ws-example-combine-postal-codes:

Combine five and four digit postal codes
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-concat-ws-example-combine-postal-codes-start

Some data sources do not contain fields for complete postal codes and instead contain fields that separate the five and four digit codes. Some use cases require a single field for postal codes that includes both components, after which the **postal** semantic tag is applied.

The following example shows how to use a **CASE** statement to do the following:

#. Find situations where the five and four digit codes are both present, and then combine them.
#. Find situations where only the five-digit code is present, and then use only the five-digit code.
#. Uses the **CONCAT_WS** function to return "zip_code" and "zip_code_plus_four" separated by "-".
#. Use **NULL** for situations where the five-digit code is not present.
#. Return as the **postal** field, to which the **postal** semantic tag may be applied.

.. code-block:: sql
   :linenos:

   ,CASE
     WHEN zip_code != '(NULL)'
     AND zip_code_plus_four != '(NULL)'
     THEN CONCAT_WS('-',zip_code, zip_code_plus_four)

     WHEN zip_code != '(NULL)'
     THEN zip_code

     ELSE NULL
   END AS postal

.. sql-spark-function-concat-ws-example-combine-postal-codes-end


.. _sql-spark-function-concat-ws-example-build-single-field:

Combine five and four digit postal codes
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-concat-ws-example-build-single-field-start

The following example concatenates columns into a single field, where "ACME" represents a hardcoded value present in the filename.

.. code-block:: sql
   :linenos:

   SELECT
     'ACME' AS Brand_Name
     ,CONCAT_WS('-',
                ,'ACME'
                ,card_number) AS Loyalty_ID
     ,CONCAT_WS(' '
                ,residential_unit_number
                ,residential_street_number
                ,residential_street) AS residential_address
     ,*
   FROM Loyalty_ACME
   CLUSTER BY card_number

.. sql-spark-function-concat-ws-example-build-single-field-end


.. _sql-spark-function-count:

COUNT()
--------------------------------------------------

.. sql-spark-function-count-start

Use the **COUNT(*)** function to return the total number of rows, including rows with unique and non-NULL values.

Use the **COUNT(expression)** function to return the number of non-NULL rows for "expression".

.. code-block:: none

   COUNT(*) AS `L12M_order_channels`,

or:

.. code-block:: sql
   :linenos:

   -- Join for one-time customers
   LEFT JOIN (
     SELECT
       amperity_id
       ,CASE
          WHEN COUNT(*) = 1 THEN '1X Customer'
          WHEN COUNT(*) > 1 THEN 'Repeat Customer'
       END AS repeat_purchaser
     FROM Unified_Transactions
     GROUP BY amperity_id
   ) AS onetime ON onetime.amperity_id = customers.amperity_id

or:

.. code-block:: none

   COUNT(channel) AS `channel_frequency`

.. sql-spark-function-count-end


.. _sql-spark-function-count-distinct:

COUNT(DISTINCT)
--------------------------------------------------

.. sql-spark-function-count-distinct-start

Use the **COUNT(DISTINCT expression)** function to return the number of unique and non-NULL rows for "expression". For example:

.. code-block:: none

   ,COUNT(DISTINCT tx.channel) AS `L12M_order_channels`

.. sql-spark-function-count-distinct-end


.. _sql-spark-function-current-date:

CURRENT_DATE()
--------------------------------------------------

.. sql-spark-function-current-date-start

Use the **CURRENT_DATE()** function to return the current date at the start of the query evaluation.

.. note:: You may use **CURRENT_DATE** without the parentheses to return the current date at the start of query evaluation.

.. sql-spark-function-current-date-end

.. sql-spark-function-current-date-volatile-table-start

.. TODO: Keep this synchronized with amperity_sql_spark/current_date.rst

.. important:: A table that uses the **CURRENT_DATE()** function is considered a "volatile table" and is always refreshed when :ref:`running a database with a normal refresh <databases-database-howto-run-normal>`.

.. sql-spark-function-current-date-volatile-table-end


.. _sql-spark-function-current-timestamp:

CURRENT_TIMESTAMP()
--------------------------------------------------

.. sql-spark-function-current-timestamp-start

Use the **CURRENT_TIMESTAMP()** function to return the current timestamp at the start of the query evaluation. All calls of **CURRENT_TIMESTAMP()** within the same query will return the same timestamp.

.. note:: You may use **CURRENT_TIMESTAMP** without the parentheses to return the current timestamp at the start of query evaluation.

.. sql-spark-function-current-timestamp-end

.. sql-spark-function-current-timestamp-volatile-table-start

.. TODO: Keep this synchronized with amperity_sql_spark/current_timestamp.rst

.. important:: A table that uses the **CURRENT_TIMESTAMP()** function is considered a "volatile table" and is always refreshed when :ref:`running a database with a normal refresh <databases-database-howto-run-normal>`.

.. sql-spark-function-current-timestamp-volatile-table-end


.. _sql-spark-function-date:

DATE()
--------------------------------------------------

.. sql-spark-function-date-start

Use the **DATE(expression)** function to cast the value of "expression" to a date data type.

.. sql-spark-function-date-end


.. _sql-spark-function-date-example-compare-dates-by-date-range:

Compare dates by date range
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-date-example-compare-dates-by-date-range-start

The following SELECT statement returns all orders between November 22, 2019 and November 21, 2020. The **DATE()** function compares the value of the **order_datetime** field in customer data to the date range.

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,MIN(order_datetime) AS min_order_date
     ,COUNT(DISTINCT order_id) AS orders
     ,SUM(order_revenue) AS order_revenue
   FROM Unified_Transactions
   WHERE amperity_id IS NOT NULL
   AND DATE(order_datetime) >= DATE('2019-11-22')
   AND DATE(order_datetime) <= DATE('2020-11-21')

.. sql-spark-function-date-example-compare-dates-by-date-range-end


.. _sql-spark-function-date-example-convert-datetime-to-date-range:

Convert DATETIME() to DATE()
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-date-example-convert-datetime-to-date-start

The following examples will convert attributes that are in **DATETIME()** to **DATE()**.

To do the type conversion once, use:

.. code-block:: sql

   DATE(MAX(order_datetime))

To do the type conversion for every row, use:

.. code-block:: sql

   MAX(DATE(order_datetime))

For example, to return **order_datetime** as a date, and not a datetime, for each Amperity ID:

.. code-block:: sql
   :linenos:

   SELECT
     ut.amperity_id
     ,DATE(MAX(ut.order_datetime)) AS latest_order_date
   FROM Unified_Transactions AS ut
   GROUP BY 1

.. sql-spark-function-date-example-convert-datetime-to-date-end


.. _sql-spark-function-date-add:

DATE_ADD()
--------------------------------------------------

.. sql-spark-function-date-add-start

Use the **DATE_ADD(startdate, number)** function to return the "number" of days after "startdate".

.. sql-spark-function-date-add-end


.. _sql-spark-function-date-trunc:

DATE_TRUNC()
--------------------------------------------------

.. sql-spark-function-date-trunc-start

Use the **DATE_TRUNC(format, timestamp)** function to return a "timestamp" truncated to "format". A timestamp is represented by a column in Amperity data that contains a valid timestamp.

Format may be any of the following:

* **YEAR**
* **YYYY**
* **YY**
* **MON**
* **MONTH**
* **MM**
* **DAY**
* **DD**

.. note:: **HOUR**, **MINUTE**, **SECOND**, **WEEK**, and **QUARTER** are also valid format values.

.. sql-spark-function-date-trunc-end


.. _sql-spark-function-date-trunc-example-return-purchases-by-day:

Return purchases by day
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-date-trunc-example-return-purchases-by-day-start

To return last purchase by day:

.. code-block:: none

   DATE_TRUNC('DAY',LastPurchase)

.. sql-spark-function-date-trunc-example-return-purchases-by-day-end


.. _sql-spark-function-date-trunc-example-return-purchases-by-month:

Return purchases by month
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-date-trunc-example-return-purchases-by-month-start

To return last purchase by month:

.. code-block:: none

   DATE_TRUNC('MONTH',LastPurchase)

.. sql-spark-function-date-trunc-example-return-purchases-by-month-end


.. _sql-spark-function-date-trunc-example-return-purchases-by-year:

Return purchases by year
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-date-trunc-example-return-purchases-by-year-start

To return last purchase by year:

.. code-block:: none

   DATE_TRUNC('YEAR',LastPurchase)

.. sql-spark-function-date-trunc-example-return-purchases-by-year-end


.. _sql-spark-function-datediff:

DATEDIFF()
--------------------------------------------------

.. sql-spark-function-datediff-start

Use the **DATEDIFF(enddate, startdate)** function to return the number of days between "startdate" and "enddate".

.. sql-spark-function-datediff-end


.. _sql-spark-function-datediff-example-find-early-repeat-purchasers:

Find early repeat purchasers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-datediff-example-find-early-repeat-purchasers-start

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,CASE
       WHEN DATEDIFF(second_order_date, first_order_date) <= 30 THEN true
       WHEN DATEDIFF(second_order_date, first_order_date) > 30 THEN false
       WHEN DATEDIFF(CURRENT_DATE(), first_order_date) > 30 THEN false
     END AS early_repeat_purchaser
   FROM Transaction_Attributes_Extended

.. sql-spark-function-datediff-example-find-early-repeat-purchasers-end


.. _sql-spark-function-datediff-example-find-transactions-within-30-days:

Find transactions within 30 days
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-datediff-example-find-transactions-within-30-days-start

.. code-block:: sql
   :linenos:

   L30D_transactions AS (
     SELECT
       *
     FROM Unified_Transactions
     WHERE DATEDIFF(CURRENT_DATE(), order_date) <= 30
   ),

.. sql-spark-function-datediff-example-find-transactions-within-30-days-end


.. _sql-spark-function-datediff-example-categorize-by-named-age-group:

Categorize by named age group
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-datediff-example-categorize-by-named-age-group-start

.. code-block:: sql
   :linenos:

   CASE
     WHEN DATEDIFF(CURRENT_DATE(), customers.birth_dt) < 7300 THEN 'Gen Z'
     WHEN DATEDIFF(CURRENT_DATE(), customers.birth_dt) < 14600 THEN 'Millenials'
     WHEN DATEDIFF(CURRENT_DATE(), customers.birth_dt) < 21900 THEN 'Gen X'
     WHEN DATEDIFF(CURRENT_DATE(), customers.birth_dt) < 29200 THEN 'Boomers'
   ELSE 'Older than Boomers'

.. sql-spark-function-datediff-example-categorize-by-named-age-group-end


.. _sql-spark-function-decode:

DECODE()
--------------------------------------------------

.. sql-spark-function-decode-start

Use the **DECODE(binary,charset)** function to decode the value of "binary" using the character set specified by "charset", such as US-ASCII, UTF-16, or UTF-8.

.. tip:: Use the **UNBASE64()** function to convert a string to binary by using it in place of "binary" within the **DECODE()** function:

   ::

      DECODE(UNBASE64(column_name),charset)

.. sql-spark-function-decode-end


.. _sql-spark-function-decode-example-identify-non-us-ascii-email:

Identify email not using US-ASCII
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-decode-example-identify-non-us-ascii-email-start

The following **CASE** statement decodes customer emails, identifies customer emails that are not encoded using the US-ASCII character set, and then sets them to **NULL**.

.. code-block:: sql
   :linenos:

   CASE
     WHEN UPPER(DECODE(UNBASE64(customer_email),'US-ASCII')) = 'UNDEFINED'
     THEN NULL
     ELSE UPPER(DECODE(UNBASE64(customer_email),'US-ASCII'))
   END AS email,

.. sql-spark-function-decode-example-identify-non-us-ascii-email-end


.. _sql-spark-function-dense-rank:

DENSE_RANK()
--------------------------------------------------

.. sql-spark-function-dense-rank-start

Use the **DENSE_RANK()** function to compute the rank of a value in a group of values. **DENSE_RANK** will assign the same rank to rows with the same value and will not create gaps in the ranked sequence.

.. note:: The **DENSE_RANK** and **RANK()** functions both assign a rank to rows with the same value. The difference is that **RANK()** creates gaps in the sequence. The following example shows rows that are ranked in ascending order by column B:

   .. code-block:: mysql

      ------- ------- ------------ ------
       col_A   col_B   dense_rank   rank
      ------- ------- ------------ ------
       A       30      3            4
       A       20      2            3
       A       20      2            3
       A       10      1            1
       A       10      1            1
      ------- ------- ------------ ------

.. sql-spark-function-dense-rank-end


.. _sql-spark-function-explode:

EXPLODE()
--------------------------------------------------

.. sql-spark-function-explode-start

Use the **EXPLODE(expression)** function to use "expression" to:

#. Separate elements of an array into multiple columns
#. Separate elements of a map into multiple rows and columns

.. sql-spark-function-explode-end


.. _sql-spark-function-explode-example-load-xml-as-ingest-query:

Load XML data as ingest query
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-explode-example-load-xml-as-ingest-query-start

.. note:: This example uses an |ext_download_sales_transactions| as the data source for sales transactions.

Use the **EXPLODE()** function to process sales transaction data into a table using an ingest query similar to:

.. code-block:: sql
   :linenos:

   WITH explodedData AS (
     SELECT
       salesTransactionId
       ,EXPLODE(salesOrder.tenders.tender) AS tender
     FROM PosXml
   )

   SELECT
     salesTransactionId
     ,tender.type AS type
     ,tender.amount AS amount
   FROM explodedData

.. sql-spark-function-explode-example-load-xml-as-ingest-query-end


.. _sql-spark-function-first-value:

FIRST_VALUE()
--------------------------------------------------

.. sql-spark-function-first-value-start

Use the **FIRST_VALUE(expression)** function to return the first value of "expression".

Use the **FIRST_VALUE(expression, isIgnoreNull)** function to return only non-**NULL** values.

.. sql-spark-function-first-value-end


.. _sql-spark-function-first-value-example-prioritize-by-order-id:

Prioritize Amperity ID by order ID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-first-value-example-prioritize-by-order-id-start

The following SQL prioritizes the Amperity ID by the most recent order ID:

.. code-block:: sql
   :linenos:

   WITH amp_priority AS (
     SELECT DISTINCT
       ut.order_id
       ,ut.datasource
       ,FIRST_VALUE(uc.amperity_id) OVER (
         PARTITION BY ut.order_id, ut.datasource
         ORDER BY uc.update_dt DESC
       ) AS amperity_id
     FROM (SELECT amperity_id, datasource, update_dt FROM Unified_Coalesced) uc
     JOIN (SELECT amperity_id, datasource, order_id FROM Unified_Transactions) ut
     ON uc.amperity_id = ut.amperity_id
   )

   SELECT t.* FROM table_name t
   JOIN amp_priority ap ON t.order_id=ap.order_id

.. sql-spark-function-first-value-example-prioritize-by-order-id-end


.. _sql-spark-function-if:

IF()
--------------------------------------------------

.. sql-spark-function-if-start

Use the **IF(expression1, expression2, expression3)** function to return "expression2" when "expression1" evaluates to "true", otherwise return "expression3".

.. sql-spark-function-if-end


.. _sql-spark-function-if-example-build-birthdate:

Build birthdate
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-if-example-build-birthdate-start

If incoming data contains birthdate data split by day, month, and year, you can build a complete birthdate using an ingest query. For example, incoming data has the following fields:

.. code-block:: mysql

   ----- ------- ------
    day   month  year    
   ----- ------- ------
    08    12     1969
    11    25     1978
    09    15     1981
   ----- ------- ------

The following example uses the **IF()** function to concatenate three fields together using a forward slash ( / ) as a separator:

.. code-block:: sql
   :linenos:

   SELECT
     *
     ,IF(
       birth_month != '0' AND birth_day != '0' AND  birth_year != '0', 
       birth_month||'/'||birth_day||'/'||birth_year, NULL
     ) AS birthdate
   FROM Source_Table

.. sql-spark-function-if-example-build-birthdate-end


.. _sql-spark-function-isnotnull:

ISNOTNULL()
--------------------------------------------------

.. sql-spark-function-isnotnull-start

Use the **ISNOTNULL(expression)** function to return true when "expression" is **NOT NULL**.

.. sql-spark-function-isnotnull-end


.. _sql-spark-function-isnull:

ISNULL()
--------------------------------------------------

.. sql-spark-function-isnull-start

Use the **ISNULL(expression)** function to return true when "expression" is **NULL**.

.. sql-spark-function-isnull-end


.. _sql-spark-function-last:

LAST()
--------------------------------------------------

.. sql-spark-function-last-start

Use the **LAST(expression)** function to return the last value of "expression".

Use the **LAST(expression, isIgnoreNull)** function to return only non-**NULL** values.

.. sql-spark-function-last-end


.. _sql-spark-function-last-example-most-recent-store-id:

Most recent store ID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-last-example-most-recent-store-id-start

.. code-block:: none

   LAST(store_id) AS last_store_id

.. sql-spark-function-last-example-most-recent-store-id-end


.. _sql-spark-function-least:

LEAST()
--------------------------------------------------

.. sql-spark-function-least-start

Use the **LEAST(column_name, column_name)** function to return the column with the lowest value among the values of all named columns.

.. sql-spark-function-least-end


.. _sql-spark-function-left:

LEFT()
--------------------------------------------------

.. sql-spark-function-left-start

Use the **LEFT(string, length)** function to return the leftmost "length" from "string". An empty string is returned when "length" is less than or equal to 0.

.. sql-spark-function-left-end


.. _sql-spark-function-left-example-set-partitions-by-characters:

Set partitions by characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-ntile-example-large-dataset-start
   :end-before: .. sql-spark-function-ntile-example-large-dataset-end

.. sql-spark-function-left-example-set-partitions-by-characters-note-start

.. note:: Partitioning **LEFT(amperity_id, 1)** to use more characters--**LEFT(amperity_id, 2)**--will improve distribution and the error rate.

.. sql-spark-function-left-example-set-partitions-by-characters-note-end


.. _sql-spark-function-length:

LENGTH()
--------------------------------------------------

.. sql-spark-function-length-start

Use the **LENGTH(expression)** function to return one of the following:

* The character length for string data, inclusive of trailing spaces.
* The number of bytes for binary data, inclusive of binary zeroes.

.. sql-spark-function-length-end


.. _sql-spark-function-length-example-return-states-as-2-characters:

Return states as 2 characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-length-example-return-states-as-2-characters-start

The following example uses the **LENGTH()** function to identify columns with two character values for states, such as AK, AL, and AR, and then sets columns without two character values to **NULL**:

.. code-block:: sql
   :linenos:

   CASE
     WHEN LENGTH(state) = 2
     THEN state
     ELSE NULL
   END AS state

.. sql-spark-function-length-example-return-states-as-2-characters-end


.. _sql-spark-function-locate:

LOCATE
--------------------------------------------------

.. sql-spark-function-locate-start

Use the **LOCATE(substring, string[, position])** function to return the first position of the first occurrence of "substring" in "string" after "position". The given position and return value are 1-based.

.. note:: The **STRPOS()** function is the same as the **LOCATE()** function.

.. sql-spark-function-locate-end


.. _sql-spark-function-lower:

LOWER()
--------------------------------------------------

.. sql-spark-function-lower-start

Use the **LOWER(string)** function to convert "string" to lowercase.

.. sql-spark-function-lower-end


.. _sql-spark-function-lpad:

LPAD()
--------------------------------------------------

.. sql-spark-function-lpad-start

Use the **LPAD(string, length, padding)** function to return "string" left-padded with "padding" to a length of "length".

.. note:: If "string" is longer than "length", the return value is shortened to "length".

.. sql-spark-function-lpad-end


.. _sql-spark-function-lpad-example-postal-codes:

Clean postal codes prior to Stitch
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-lpad-example-postal-codes-start

The following example will ensure postal codes have consistent character counts prior to making them available to Stitch:

.. code-block:: sql

  ,LPAD(postal,5,'0') as postal

.. note:: This example is for United States-only postal codes, requires using a custom domain table, and is only useful for ad hoc cleanup of a small number of postal codes. This example is not a substitute for address standardization.

.. sql-spark-function-lpad-example-postal-codes-end


.. _sql-spark-function-lpad-example-first-five:

Return first five characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-lpad-example-first-five-start

The following example returns only the first five characters from the **stay_location** field:

.. code-block:: sql

  ,LPAD(stay_location,5,'0') AS stay_location

.. sql-spark-function-lpad-example-first-five-end


.. _sql-spark-function-max:

MAX()
--------------------------------------------------

.. sql-spark-function-max-start

Use the **MAX(expression)** function to return the maximum value of "expression".

.. sql-spark-function-max-end


.. _sql-spark-function-min:

MIN()
--------------------------------------------------

.. sql-spark-function-min-start

Use the **MIN(expression)** function to return the minimum value of "expression".

.. sql-spark-function-min-end


.. _sql-spark-function-months-between:

MONTHS_BETWEEN()
--------------------------------------------------

.. sql-spark-function-months-between-start

Use the **MONTHS_BETWEEN(timestamp1, timestamp2)** function to return the number of months in-between two timestamps. If "timestamp1" is later than "timestamp2", the value returned is positive.

.. sql-spark-function-months-between-end


.. _sql-spark-function-months-between-example-order-and-today:

Months between order and today
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-months-between-example-order-and-today-start

.. code-block:: sql
   :linenos:

   L12M_transactions AS (
     SELECT
       *
     FROM Unified_Transactions
     WHERE MONTHS_BETWEEN(CURRENT_DATE(), order_date) <= 12
   ),

.. sql-spark-function-months-between-example-order-and-today-end


.. _sql-spark-function-now:

NOW()
--------------------------------------------------

.. sql-spark-function-now-start

Use the **NOW()** function to return the current timestamp as of the start of the query.

.. sql-spark-function-now-end


.. _sql-spark-function-ntile:

NTILE()
--------------------------------------------------

.. sql-spark-function-ntile-start

Use the **NTILE(n)** function to divide rows for a window partition into "n" buckets, ranging from 1 to n.

Use the **NTILE(n, int)** function to specify the number of buckets into which rows are divided as "int".

.. sql-spark-function-ntile-end


.. _sql-spark-function-ntile-example-large-dataset:

Compute ntiles over large datasets
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-ntile-example-compute-start

The following example shows a window function that divides rows into 10 buckets and uses a combination of **PARTITION BY** and the **LEFT()** function to define the buckets using the first characters of the Amperity ID:

.. code-block:: sql
   :linenos:

   Top_10 AS (
     SELECT DISTINCT
       amperity_id
       ,CLV_Spend
       ,NTILE(10) OVER (PARTITION BY LEFT(amperity_id, 1) ORDER BY CLV_Spend DESC) AS CLVPercentile

     FROM (
       SELECT 
         amperity_id
         ,SUM(Customer_Lifetime_Spend) AS CLV_Spend
       FROM customer_360_v
       WHERE Customer_Lifetime_Spend IS NOT NULL
       GROUP BY amperity_id
     )
   ),

.. sql-spark-function-ntile-example-compute-end


.. _sql-spark-function-ntile-example-partition-pclv-by-brand:

Partition predicted CLV by brand
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-ntile-example-partition-pclv-by-brand-start

The following example shows how to separate values into brand tiers using predicted customer lifetime value.

.. code-block:: sql

   NTILE(100) OVER (PARTITION BY brand ORDER BY predicted_clv desc, _uuid_pk)

.. sql-spark-function-ntile-example-partition-pclv-by-brand-end


.. _sql-spark-function-nullif:

NULLIF()
--------------------------------------------------

.. sql-spark-function-nullif-start

Use the **NULLIF(expression1, expression2)** function to return **NULL** if "expression1" is equal to "expression2".

.. sql-spark-function-nullif-end


.. _sql-spark-function-nullif-example-ingest-query:

Return NULL for empty string values
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-nullif-example-ingest-query-start

The following **SELECT** statement is an ingest query that returns **NULL** if the field is empty after trimming whitespace from before and after the initial value:

.. code-block:: sql
   :linenos:

   SELECT
     NULLIF(TRIM(BrandName),'') AS BrandName
     ,NULLIF(TRIM(AttributeName),'') AS AttributeName
     ,NULLIF(TRIM(Priority),'') AS Priority
   FROM Customer_Table

.. sql-spark-function-nullif-example-ingest-query-end


.. _sql-spark-function-ntile-example-bucket-rfm-scores:

Bucket RFM scores
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-ntile-example-bucket-rfm-scores-start

.. code-block:: sql
   :linenos:

   L12M_rfm AS (
     SELECT
       a.amperity_id
       ,NTILE(5) OVER (PARTITION BY amperity_id ORDER BY b.order_date ASC) AS `L12M_recency_score`
       ,NTILE(5) OVER (PARTITION BY amperity_id ORDER BY a.L12M_order_frequency ASC) AS `L12M_frequency_score`
       ,NTILE(5) OVER (PARTITION BY amperity_id ORDER BY a.L12M_order_total_amount ASC) AS `L12M_monetary_score`
     FROM L12M_attributes AS `a`
     JOIN (
       SELECT
         amperity_id
         ,order_date
       FROM latest_order
       WHERE MONTHS_BETWEEN(CURRENT_DATE(), order_date) <= 12
     ) AS `b` ON a.amperity_id = b.amperity_id
   )

.. sql-spark-function-ntile-example-bucket-rfm-scores-end


.. _sql-spark-function-rand:

RAND()
--------------------------------------------------

.. sql-spark-function-rand-start

Use the **RAND([0,1])** function to return a random value with independent and identically distributed (IID) uniformly distributed values.

.. sql-spark-function-rand-end

.. sql-spark-function-rand-volatile-table-start

.. TODO: Keep this synchronized with amperity_sql_spark/current_date.rst

.. important:: A table that uses the **RAND()** function is considered a "volatile table" and is always refreshed when :ref:`running a database with a normal refresh <databases-database-howto-run-normal>`.

.. sql-spark-function-rand-volatile-table-end


.. _sql-spark-function-rank:

RANK()
--------------------------------------------------

.. sql-spark-function-rank-start

Use the **RANK(value, value)** function to return the rank of a value in a group of values. The result is one plus the number of rows preceding or equal to the current row.

.. sql-spark-function-rank-end


.. _sql-spark-function-regexp-extract:

REGEXP_EXTRACT()
--------------------------------------------------

.. sql-spark-function-regexp-extract-start

Use the **REGEXP_EXTRACT(string, pattern, id)** function to replace every instance of the substring matched by the "regex" pattern from "string".

.. sql-spark-function-regexp-extract-end


.. _sql-spark-function-regexp-extract-example-names:

Extract first and last names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-regexp-extract-example-names-start

Some data sources do not contain fields that can be directly assigned the **given-name** and **surname** semantic tags. These tags are important to downstream Stitch processes. When a field is present in the data source that contains data that can be tagged with the **full-name** semantic tag, you can use domain SQL to extract the first and last name details from that field, add them as new columns, and then apply the correct semantic tags.

Use the **REGEXP_EXTRACT()** function to:

#. Trim whitespace from before (or after) the first and last names.
#. Individually extract the first and last names from the field that contains the full name.
#. Add columns for the first and last names.

The following example shows part of a **SELECT** statement that extracts first and last names from the **BILLING_NAME** field, and then adds columns for first and last names:

.. code-block:: sql
   :linenos:

   ,REGEXP_EXTRACT(TRIM(BILLING_NAME),'(^\\S*)',1) AS GIVEN_NAME
   ,REGEXP_EXTRACT(TRIM(BILLING_NAME),'((?<=\\s).*)',1) AS SURNAME
   ,TRIM(BILLING_NAME) AS `BILLING_NAME`

.. sql-spark-function-regexp-extract-example-names-end


.. _sql-spark-function-regexp-replace:

REGEXP_REPLACE()
--------------------------------------------------

.. sql-spark-function-regexp-replace-start

Use the **REGEXP_REPLACE(string, regex)** function to remove every instance of the substring matched by the "regex" pattern from "string".

Use the **REGEXP_REPLACE(string, regex, replace)** function to replace every instance of the substring.

.. sql-spark-function-regexp-replace-end


.. _sql-spark-function-regexp-replace-example-remove-whitespace:

Remove whitespace
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-regexp-replace-example-remove-whitespace-start

.. code-block:: sql

   NULLIF(REGEXP_REPLACE(field, '^\\s*(\\S.*\\S)\\s*$', '\\1'), '')

.. sql-spark-function-regexp-replace-example-remove-whitespace-end


.. _sql-spark-function-right:

RIGHT()
--------------------------------------------------

.. sql-spark-function-right-start

Use the **RIGHT(string, length)** function to return characters from a string equal to length.

.. sql-spark-function-right-end


.. _sql-spark-function-right-return-email-domain:

Return only email address domains
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-right-return-email-domain-start

You can use the **RIGHT()** function, along with the **CHAR_LENGTH()** and **INSTR()** functions, to remove all characters that are not to the right of the "@" symbol in an email address, returning only the domain. The syntax is:

.. code-block:: sql

   RIGHT(string, CHAR_LENGTH(expression) - INSTR(string, substring)) AS email_domain

For example:

.. code-block:: sql

   RIGHT(email, CHAR_LENGTH(email) - INSTR(email, '@')) AS email_domain

.. sql-spark-function-right-return-email-domain-end


.. _sql-spark-function-rlike:

RLIKE()
--------------------------------------------------

.. sql-spark-function-rlike-start

Use the **RLIKE(string, 'expression')** function to return true when "string" matches "expression".

.. sql-spark-function-rlike-end

.. sql-spark-function-rlike-caution-start

.. caution:: A backslash ( ``\`` ) contained within a regular expression **MUST** be escaped using another backslash. For example, a regular expression that matches a single numeric digit should be ``\\d`` and not ``\d``.

.. sql-spark-function-rlike-caution-end


.. _sql-spark-function-rlike-example-validate-email:

Validate email addresses
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-rlike-example-validate-email-start

The following example shows using the **RLIKE()** function within a **CASE** statement to return valid email addresses:

.. code-block:: sql
   :linenos:

   CASE
     WHEN email RLIKE('^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')
     AND email_completion > 0 THEN true
     ELSE false
   END AS contactable_email

.. sql-spark-function-rlike-example-validate-email-end


.. _sql-spark-function-rlike-example-validate-phone:

Validate phone numbers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-rlike-example-validate-phone-start

The following example shows using the **RLIKE()** function within a **CASE** statement to return valid phone numbers:

.. code-block:: sql
   :linenos:

   CASE
     WHEN phone RLIKE('^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')
     AND phone_completion > 0 THEN true
     ELSE false
   END AS contactable_phone

.. sql-spark-function-rlike-example-validate-phone-end


.. _sql-spark-function-round:

ROUND()
--------------------------------------------------

.. sql-spark-function-round-start

Use the **ROUND(expression, x)** function to return "expression" rounded to "x" decimal places.

.. sql-spark-function-round-end


.. _sql-spark-function-round-example-rounded-sum:

Return rounded sum
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-round-example-rounded-sum-start

The following example returns the sum of a, b, and c rounded to two decimal places as the score:

.. code-block:: none

   ROUND((CAST(a AS float) + CAST(b AS float) + CAST(c AS float)) / 3, 2) AS AbcScore,

.. sql-spark-function-round-example-rounded-sum-end


.. _sql-spark-function-row-number:

ROW_NUMBER()
--------------------------------------------------

.. sql-spark-function-row-number-start

Use the **ROW_NUMBER()** function within a window function to assign a unique, sequential number to each row, starting with 1. For example:

.. code-block:: none

   ROW_NUMBER() OVER (PARTITION BY amperity_id ORDER BY order_date DESC) AS `rn`

.. sql-spark-function-row-number-end


.. _sql-spark-function-sha2:

SHA2()
--------------------------------------------------

.. sql-spark-function-sha2-start

Use the **SHA2(expression, 256)** function to apply one-way SHA-256 hashes to fields, such as those that contain PII data to ensure they are no longer recognizable as valid PII.

For example:

.. code-block:: none

   SHA2(LOWER(TRIM(email)),256) AS email

.. sql-spark-function-sha2-end


.. _sql-spark-function-sha2-example-rehash-data:

Rehash PII data
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-sha2-example-rehash-data-start

Some segments send results downstream to support CCPA and GDPR workflows. Some CCPA and GDPR workflows send this data back to Amperity, which typically requires the data to be hashed using a domain table.

For example, to hash the name, email, and phone fields in a table named "tohash_ccpa":

.. code-block:: sql
   :linenos:

   SELECT
     *
     ,SHA2(UPPER(TRIM(firstname))) AS Hash_firstname
     ,SHA2(UPPER(TRIM(lastname))) AS Hash_lastname
     ,SHA2(UPPER(TRIM(email))) AS Hash_email
     ,SHA2(UPPER(TRIM(phone_number))) AS Hash_phone
   FROM tohash_ccpa

.. sql-spark-function-sha2-example-rehash-data-end


.. _sql-spark-function-split:

SPLIT()
--------------------------------------------------

.. sql-spark-function-split-start

Use the **SPLIT(string, regex)** function to split a "string" at occurances that match "regex", and then return the results.

.. note:: In Spark SQL, the index starts at 0.

.. sql-spark-function-split-end


.. _sql-spark-function-split-example-index-position:

Split using index position
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-split-example-index-position-start

Specify an index to split a string at occurrences that match the index. If the index is larger than the number of available characters, or if the specified index position is out of range, the function will return **NULL**. For example:

.. code-block:: sql

   SPLIT(GIFTCARDCODE,'-')[4]

.. note:: In Spark SQL, the index starts at 0.

.. sql-spark-function-split-example-index-position-end

.. sql-spark-function-split-example-index-position-compare-to-presto-start

.. tip:: Use the **SPLIT_PART()** function in Presto SQL. For example:

   .. code-block:: sql

      TRIM(SPLIT_PART(GIFTCARDCODE, '-', 1))

   In Presto SQL, the index starts at 1.

.. sql-spark-function-split-example-index-position-compare-to-presto-end


.. _sql-spark-function-split-example-return-username:

Return username from email
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-split-example-return-username-start

To return only the username from an email address (the characters before the @ symbol):

.. code-block:: none

   SPLIT(REGEXP_REPLACE(LOWER(email), '[.]+', ''), '@')[0] AS email_username

.. sql-spark-function-split-example-return-username-end


.. _sql-spark-function-split-example-parse-fields-with-multiple-separators:

Parse fields with multiple separators
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-split-example-parse-fields-with-multiple-separators-start

Sometimes incoming data contains data that should be tagged with more than one semantic tag, but also contain different separators within the incoming field. For example:

.. code-block:: mysql

   ----------- ---------- ------------------- ------- ---------------------- -------
    firstName   lastName   street              poBox   location               zip
   ----------- ---------- ------------------- ------- ---------------------- -------
    John        Smith      123 Main            #101    US - Yelm , WA         98597
    Andy        Jones      456 South Avenue            US - Bellingham, WA    98115
    Anne        Andersen   999 S. Bergen Way           US - Seattle ,WA       98104
   ----------- ---------- ------------------- ------- ---------------------- -------

where "location" represents country, city, and state, always separated with a dash ( - ) between the country and city, and then a comma ( , ) between the city and the state. Some fields contain extra white space between and around the strings.

The "location" field needs to be split into individual city, state, and country fields, the two delimiters can be removed, along with the extra whitespace.

Use domain SQL similar to the following:

.. code-block:: sql
   :linenos:

   SELECT
     location
     ,TRIM(SPLIT(location, '-')[0]) AS country
     ,TRIM(SPLIT(SPLIT(location, '-')[1],',')[0]) AS city
     ,TRIM(SPLIT(location, ',')[1]) AS state
   FROM domain_table

and then tag the city, state, and country fields with the appropriate semantic tags.

.. sql-spark-function-split-example-parse-fields-with-multiple-separators-end


.. _sql-spark-function-strpos:

STRPOS()
--------------------------------------------------

.. sql-spark-function-strpos-start

Use the **STRPOS(substring, string[, position])** function to return the first position of the first occurrence of "substring" in "string" after "position". The given position and return value are 1-based.

.. note:: The **LOCATE()** function is the same as the **STRPOS()** function.

.. sql-spark-function-strpos-end


.. _sql-spark-function-substr:

SUBSTR()
--------------------------------------------------

.. sql-spark-function-substr-start

Use the **SUBSTR(string, position, length)** function to return the substring of "string" that starts at "position" for the specified "length".

.. sql-spark-function-substr-end


.. _sql-spark-function-substr-example-return-as-lowercase:

Return string as lowercase
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-substr-example-return-as-lowercase-start

To return as lowercase the string contained in the "Gender" field, and then only the first character of that string:

.. code-block:: none

   SUBSTR(LOWER(Gender),1,1) as GEN

.. sql-spark-function-substr-example-return-as-lowercase-end


.. _sql-spark-function-substring:

SUBSTRING()
--------------------------------------------------

.. sql-spark-function-substring-start

Use the **SUBSTRING(string, position[, length])** function to return the substring of "string" that starts at "position" for the specified "length".

.. note:: The "length" parameter is optional. Use it to return only the number of characters specified by "length". When not specified, **SUBSTRING()** uses "position" to determine the number of characters to return. For example:

   ::

      SELECT SUBSTRING('Amperity', 5)

   returns "erity".

   ::

      SELECT SUBSTRING('Amperity', -3)

   returns "ity".

   ::

      SELECT SUBSTRING('Amperity', 5, 1)

   returns "e".

.. sql-spark-function-substring-end


.. _sql-spark-function-substring-example-remove-country-codes:

Remove country code from phone numbers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-substring-example-remove-country-codes-start

The following example returns phone numbers from multiple tables, and then removes "+1 ", "+1-", "1 " and "1-".

.. code-block:: none
   :linenos:

   SELECT
     COALESCE(email,'NULL')||COALESCE(phone,'NULL') AS pk
     ,MAX(email) AS email
     ,MAX(phone) AS phone
   FROM (
     SELECT
       sms.email
       ,CASE
         WHEN sms.phone LIKE '+1%' THEN SUBSTRING(sms.phone,3) 
         WHEN sms.phone LIKE '1%' THEN SUBSTRING(sms.phone,2) 
         ELSE sms.phone
       END AS phone
     FROM Attentive_Mobile_SMS sms
     UNION
     SELECT
       sub.Email
       ,CASE
         WHEN sub.phone LIKE '+1%' THEN SUBSTRING(sub.phone,3) 
         WHEN sub.phone LIKE '1%' THEN SUBSTRING(sub.phone,2) 
         ELSE sub.phone
       END AS phone 
     FROM Attentive_Mobile_Subscribers sub
   )
   GROUP BY 1

.. sql-spark-function-substring-example-remove-country-codes-end


.. _sql-spark-function-substr-example-parse-fields-from-dat-file:

Parse fields from DAT file
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-substr-example-parse-fields-from-dat-file-start

The following example shows an ingest query that parses fields from a DAT file. Each field (fields 1-6) has a starting point within the DAT file (1, 21, 52, 63, 69, 70) and a length (20, 30, 10, 15, 1, 140). Use an ordinal, such as "_c0", to define each source field within the DAT file.

.. code-block:: none
   :linenos:

   SELECT
     ,NULLIF(TRIM(SUBSTR(`_c0`,1,20)),'') AS Field1
     ,NULLIF(TRIM(SUBSTR(`_c0`,21,30)),'') AS Field2
     ,NULLIF(TRIM(SUBSTR(`_c0`,52,10)),'') AS Field3
     ,NULLIF(TRIM(SUBSTR(`_c0`,63,15)),'') AS Field4
     ,NULLIF(TRIM(SUBSTR(`_c0`,69,1)),'') AS Field5
     ,NULLIF(TRIM(SUBSTR(`_c0`,70,140)),'') AS Field6
   FROM DAT_FILE_NAME

.. sql-spark-function-substr-example-parse-fields-from-dat-file-end


.. _sql-spark-function-sum:

SUM()
--------------------------------------------------

.. sql-spark-function-sum-start

Use the **SUM(expression)** to return a sum calculated from values defined in "expression".

Use the **COALESCE()** function to map fields with **NULL** values to zero prior to using this function.

.. sql-spark-function-sum-end

.. sql-spark-function-sum-note-about-null-start

.. note:: The **SUM()** function will return **NULL** if the value of any field is **NULL**. In some situations you must use the **COALESCE()** function to coalesce to a zero-length string prior to concatenation. For example:

   .. code-block:: none

      SUM(COALESCE(lifetimeValue,0))

.. sql-spark-function-sum-note-about-null-end


.. _sql-spark-function-to-date:

TO_DATE()
--------------------------------------------------

.. sql-spark-function-to-date-ingest-warning-start

.. caution:: Do not use this function when writing ingest queries. Instead, use the datetime picker in the **Feed Editor** to define a date.

.. sql-spark-function-to-date-ingest-warning-end

.. sql-spark-function-to-date-start

Use the **TO_DATE(timestamp)** function to parse "timestamp".

Use the **TO_DATE(timestamp +/- interval)** function to parse "timestamp", and then add ( + ) or subtract ( - ) "interval", where "interval" is one of "hours", "minutes", or "days".

A date format is not required.

.. tip:: This function returns **NULL** when the input is invalid.

.. sql-spark-function-to-date-end


.. _sql-spark-function-to-date-example-find-date-six-hours-ago:

Find a date six hours ago
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-to-date-example-find-date-six-hours-ago-start

Use a minus sign ( - ) to subtract from a value. For example. to find 6 hours before the current time:

.. code-block:: none

   TO_DATE(CURRENT_TIMESTAMP - 6 HOURS)

.. sql-spark-function-to-date-example-find-date-six-hours-ago-end


.. _sql-spark-function-to-date-example-2-digit-years:

Correct 2-digit years
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-to-date-example-2-digit-years-start

Converting an incorrectly ingested date in the year 19xx is not as simple as adding 365*2000 years. Lots of things can go wrong. In some cases you may need to correct birthdates so that people are not born in the future. The recommended approach is to parse the date correctly, and then re-parse it.

The following example shows two ways to do this:

#. The first **TO_DATE()** function shows how to use the current year as a breakpoint, which assumes that birthdates do not occur in the future and that the majority of people are less than 100 years old.
#. The second **TO_DATE()** function shows to handle birthdates that occur after the year 2000.

.. code-block:: sql
   :linenos:

   SELECT
     customer_id
     ,birth_dt
     ,TO_DATE(
       CONCAT_WS(
         '-'
         ,INT(IF(SPLIT(birth_dt, "/")[2] > INT(DATE_FORMAT(CURRENT_DATE(), 'yy')), SPLIT(birth_dt, "/")[2] + 1900, SPLIT(birth_dt, "/")[2] + 2000))
         ,SPLIT(birth_dt, "/")[0]
         ,SPLIT(birth_dt, "/")[1]
       )
       ,'yyyy-MM-dd'
     ) AS birth_dt_corrected
     ,TO_DATE(
       CONCAT_WS(
         '-'
         ,INT(SPLIT(birth_dt, "/")[2]) + 2000
         ,SPLIT(birth_dt, "/")[0]
         ,SPLIT(birth_dt, "/")[1]
       )
       ,'yyyy-MM-dd'
     ) AS birth_dt_twentyfirstcentury
   FROM CustomersPOS

.. sql-spark-function-to-date-example-2-digit-years-end


.. _sql-spark-function-to-timestamp:

TO_TIMESTAMP()
--------------------------------------------------

.. sql-spark-function-to-timestamp-ingest-warning-start

.. caution:: Do not use this function when writing ingest queries. Instead, use the datetime picker in the **Feed Editor** to define a timestamp.

.. sql-spark-function-to-timestamp-ingest-warning-end

.. sql-spark-function-to-timestamp-start

Use the **TO_TIMESTAMP(expression, format)** function to return "expression" in the (optional) "format".

.. sql-spark-function-to-timestamp-end


.. _sql-spark-function-translate:

TRANSLATE()
--------------------------------------------------

.. sql-spark-function-translate-start

Use the **TRANSLATE(input, from, to)** function to replace the "from" characters in "input" with the "to" characters.

This function is useful for direct replacement of bad characters, simple cleanup tasks, and other situations that do not require any context or the use of regular expressions.

For example, **TRANSLATE(abcde, cd, 45)** will translate "abcde" to "ab45e".

.. tip:: Use the **REGEXP_REPLACE()** function to replace characters in string values using a regular expression.

.. sql-spark-function-translate-end


.. _sql-spark-function-trim:

TRIM()
--------------------------------------------------

.. sql-spark-function-trim-start

Use the **TRIM(string)** function to remove leading and trailing characters from "string".

Use **LEADING**, **TRAILING**, or **BOTH** as keywords to define the location from which characters are removed, and then **FROM** to specify the string to which the keyword is applied. **BOTH** is the default keyword.

.. sql-spark-function-trim-end

.. sql-spark-function-trim-tip-start

The **TRIM(string)** function assumes it should trim spaces, which means all that is required to trim leading or trailing spaces is to specify the column name. For example:

.. code-block:: none

   TRIM('column_name')

.. sql-spark-function-trim-tip-end


.. _sql-spark-function-trim-example-clean-phone-numbers:

Clean phone numbers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-trim-example-phone-numbers-start

The following example uses the **TRIM()** function to find empty or NULL phone numbers, sets them to **NULL**, and then standardizes all phone numbers to add a +1:

.. code-block:: none
   :linenos:

   CASE
     WHEN TRIM(phone) LIKE ''
     OR TRIM(phone) IS NULL
     THEN NULL
     ELSE CONCAT('+1','',REGEXP_REPLACE(phone,'[^0123456789]',''))
   END AS phone

.. sql-spark-function-trim-example-phone-numbers-end


.. _sql-spark-function-trim-example-leading:

Trim leading characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-trim-example-leading-start

.. code-block:: none

   SELECT TRIM(LEADING '123' FROM '123string')

returns:

.. code-block:: none

   string

.. sql-spark-function-trim-example-leading-end


.. _sql-spark-function-trim-example-trailing:

Trim trailing characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-trim-example-trailing-start

.. code-block:: none

   SELECT TRIM(TRAILING 'ing' FROM '123string')

returns:

.. code-block:: none

   123str

.. sql-spark-function-trim-example-trailing-end


.. _sql-spark-function-trim-example-both:

Trim leading and trailing characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-trim-example-both-start

.. code-block:: none

   SELECT TRIM(BOTH '12g' FROM '123string')

returns:

.. code-block:: none

   3strin

.. sql-spark-function-trim-example-both-end


.. _sql-spark-function-trim-example-both-uppercase:

Trim, then set to uppercase
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-spark-function-trim-example-both-uppercase-start

.. code-block:: none

   TRIM(UPPER(field)) AS field

.. sql-spark-function-trim-example-both-uppercase-end


.. _sql-spark-function-unix-timestamp:

UNIX_TIMESTAMP()
--------------------------------------------------

.. sql-spark-function-unix-timestamp-start

Use the **UNIX_TIMESTAMP(time, format)** function to return the UNIX timestamp for "time" in the specified "format".

For example:

.. code-block:: none

   UNIX_TIMESTAMP('2021-11-10', 'yyyy-MM-dd');

will return:

::

   1636612010

.. sql-spark-function-unix-timestamp-end


.. _sql-spark-function-upper:

UPPER()
--------------------------------------------------

.. sql-spark-function-upper-start

Use the **UPPER(string)** function to convert "string" to uppercase.

.. sql-spark-function-upper-end
