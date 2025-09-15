.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Use Presto SQL to build queries for analysis or for sending audiences and query results to any downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use Presto SQL to build queries for analysis or for sending audiences and query results to any downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        About Presto SQL

==================================================
About Presto SQL
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-presto-sql-start
   :end-before: .. term-presto-sql-end


.. _sql-presto-why-should-i-use-this:

Why should I use this reference?
==================================================

.. sql-presto-why-should-i-use-this-start

The **SQL Segment Editor** in the **Queries** and **Segment** tabs uses Presto SQL as the underlying SQL engine. Amperity segments are built almost exclusively by using the **SELECT** statement, along with the clauses, operators, expressions, and functions you would expect to be available.

This reference is focused on how Presto SQL is used with Amperity and is not focused on anything that you would not expect to do from the **Queries** and **Segment** tabs in Amperity.

Please refer to this reference first, and then to the official `Presto SQL <https://prestodb.io/docs/current/index.html>`__ |ext_link| documentation.

.. sql-presto-why-should-i-use-this-end


.. _sql-presto-aws-vs-azure:

Amazon AWS vs. Azure
==================================================

.. sql-presto-aws-vs-azure-start

Amperity uses different versions of Presto SQL, depending on if the tenant runs in Amazon AWS or Microsoft Azure.

* Tenants that run in Amazon AWS run `Athena engine version 2 <https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference.html#engine-versions-reference-0002>`__ |ext_link|.
* Tenants in Azure run Trino, version 346: `release notes <https://trino.io/docs/current/release/release-346.html>`__ |ext_link|, `SELECT statement reference <https://trino.io/docs/current/sql/select.html>`__ |ext_link| (for current version), `functions reference <https://trino.io/docs/current/functions.html>`__ |ext_link| (for current version).

Amperity behaves the same on either platform when using Presto SQL to build segments from within the **Segments** tab, with the following exceptions:

#. The way Presto SQL handles `fixed precision rounding for a DECIMAL data type <https://prestodb.io/docs/current/language/types.html#fixed-precision>`__ |ext_link| was changed in Presto SQL version 0.198. A decimal without an explicit type specifier--for example, 1.2--is parsed as a ``DOUBLE`` on tenants that run in Amazon AWS and as a ``DECIMAL`` on tenants that run in Azure.

.. sql-presto-aws-vs-azure-end


.. _sql-presto-style-guide:

Recommendations
==================================================

.. sql-presto-style-guide-start

This is a list of recommendations for using Presto SQL with Amperity segments.

.. sql-presto-style-guide-end


.. _sql-presto-style-guide-general:

General
--------------------------------------------------

.. sql-presto-style-guide-general-start

**Do**

* Use consistent and descriptive identifiers and names.
* Make judicious use of white space and indentation to make code easier to read.
* Store ISO-8601 compliant time and date information (YYYY-MM-DD HH:MM:SS.SSSSS).
* Try to use only standard SQL functions instead of vendor-specific functions for reasons of portability.
* Keep code succinct and devoid of redundant SQL, such as unnecessary quoting or parentheses or **WHERE** clauses that can otherwise be derived.
* Include comments in SQL code where necessary.

  You may use the C-language style slash and asterisk opening (``/*``) and closing (``*/``) pair of delimiters to enclose comments single- and multi-line comments, as long as comments are not nested.

  You may precede single-line comments using ``--``.

* Convert string values to lowercase. For example: ``LOWER("column_name") = 'value'``.
* Code review complex SQL statements.
* Keep the **Segments** page free of draft segments as much as possible.
* Ensure segments are run automatically.
* Use one-way SHA-256 hashes for fields that contain PII data.
* Use double quotes (``""``) for database table and field names. Use single quotes (``''``) for values used in comparisons. For example: ``"State" = 'Washington'``.
* Use :ref:`parentheses to group the contents <sql-presto-where-parentheses>` of **AND**, **OR**, and **NOT** operators within complex SQL to ensure that each element within the **WHERE** clause runs in the correct order.

**Avoid**

* Using reserved keyword names as identifiers.
* CamelCase, with the exception of the table name. CamelCase is difficult to scan quickly.
* Descriptive prefixes or `Hungarian notation <https://en.wikipedia.org/wiki/Hungarian_notation>`__ |ext_link| such as ``sp_`` or ``tbl``.
* Plurals. Use the more natural collective term where possible instead. For example staff instead of employees or people instead of individuals.
* Quote identifiers. Use SQL92 double quotes for portability, if possible.
* Object-oriented design principles with SQL or database structures.

.. sql-presto-style-guide-general-end


.. _sql-presto-style-guide-commas:

Commas
--------------------------------------------------

.. sql-presto-style-guide-commas-start

Commas are used as separators in SQL queries and are often added at the end of a line, like this:

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

.. sql-presto-style-guide-commas-end


.. _sql-presto-style-guide-indentation:

Indentation
--------------------------------------------------

.. sql-presto-style-guide-indentation-start

To ensure that SQL is readable it is important that standards of indentation are followed. Use a two-character indentation pattern for SQL queries as often as possible to help ensure consistency and readability. A two-character indentation pattern also helps minimize the width of the query, making it easier to read on the page and less likely to wrap or run off the page to the right.

.. sql-presto-style-guide-indentation-end


.. _sql-presto-style-guide-indentation-formalisms:

Formalisms
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-indentation-formalisms-start

Make use of **BETWEEN** where possible instead of combining multiple statements with **AND**. Similarly use **IN()** instead of multiple **OR** clauses. Where a value needs to be interpreted before leaving the database use the **CASE** expression. **CASE** expressions can be nested to form more complex logical structures. Avoid the use of **UNION** clauses and temporary tables where possible. If the schema can be optimized to remove the reliance on these features then it most likely should be.

.. code-block:: sql
   :linenos:

   SELECT CASE postcode
     WHEN 'BN1' THEN 'Brighton'
     WHEN 'EH1' THEN 'Edinburgh'
     END AS 'city_uk'
   FROM office_locations
   WHERE country = 'United Kingdom'
     AND opening_time BETWEEN 8 AND 9
     AND postcode IN ('EH1', 'BN1', 'NN1', 'KW1')

.. sql-presto-style-guide-indentation-formalisms-end


.. _sql-presto-style-guide-indentation-joins:

Joins
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-indentation-joins-start

Joins should be aligned with the **FROM** clause and grouped with a new line where necessary. Indenting the **ON** and **AND** statements in a **JOIN** is optional, but can make it easier to see individual joins when many are present.

.. code-block:: sql
   :linenos:

   SELECT r.last_name
   FROM riders AS r
   INNER JOIN bikes AS b
     ON r.bike_vin_num = b.vin_num
     AND b.engine_tally > 2
   INNER JOIN crew AS c
     ON r.crew_chief_last_name = c.last_name
     AND c.chief = 'Y';

.. sql-presto-style-guide-indentation-joins-end


.. _sql-presto-style-guide-indentation-subqueries:

Subqueries
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-indentation-subqueries-start

Subqueries should be aligned to the line above them, but then follow standard indentation patters from that location. Sometimes it will make sense to have the closing parenthesis on a new line at the same character position as its opening partner—this is especially true where you have nested subqueries.

.. code-block:: sql
   :linenos:

   SELECT r.last_name,
     (SELECT MAX(YEAR(championship_date))
     FROM champions AS c
     WHERE c.last_name = r.last_name
       AND c.confirmed = 'Y') AS `last_championship_year`
   FROM riders AS r
   WHERE r.last_name IN
     (SELECT c.last_name
     FROM champions AS c
     WHERE YEAR(championship_date) > '2008'
       AND c.confirmed = 'Y');

.. sql-presto-style-guide-indentation-subqueries-end


.. _sql-presto-style-guide-naming-conventions:

Naming conventions
--------------------------------------------------

.. sql-presto-style-guide-naming-conventions-start

Ensure the name is unique and does not exist as a reserved keyword. Keep the length to a maximum of 30 bytes, which is 30 characters unless you are using multi-byte character set.

Names must begin with a letter and may not end with an underscore. Only use letters, numbers, and underscores in names.

Use underscores where you would naturally include a space in the name. For example, "first name" becomes "first_name". Avoid the use of multiple consecutive underscores because they can be hard to read.

Avoid abbreviations and if you have to use them make sure they are commonly understood.

.. code-block:: sql

   SELECT first_name
   FROM Customer360

.. sql-presto-style-guide-naming-conventions-end


.. _sql-presto-style-guide-naming-conventions-alias:

Alias names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-naming-conventions-alias-start

An alias assigns a temporary name to a column or a table that only exists for the duration of a query. An alias is defined after the **AS** keyword.

For columns::

   SELECT column_name AS alias_name
   FROM table_name;

For tables::

   SELECT column_names
   FROM table_name AS alias_name;

When using an alias:

* Assign names that clearly relate to the column or table.

  .. important:: Do not use an alias when its name matches the original column name.

* Always use the AS keyword to ensure readability.

  ..tip:: Include the **AS** keyword when aliasing columns in a **SELECT** statement.

* For computed data -- **SUM()** or **AVG()** -- use the name you would give it were it a column defined in the schema.
* Always wrap an aliased field name with single back ticks::

     `given_name`


The following example shows using aliases to add clarity to a **SELECT** statement that selects columns from more than one table. The "c360" alias refers to the ``Customer360`` table and the "el" alias refers to the ``Email_List`` table:

.. code-block:: sql
   :linenos:

   SELECT c360.email, c360.given_name, c360.surname, el.status
   FROM Customer360 c360

   LEFT JOIN Email_List el ON c360.email = el.email
   WHERE status IS NOT NULL

.. sql-presto-style-guide-naming-conventions-alias-end


.. _sql-presto-style-guide-naming-conventions-columns:

Column names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-naming-conventions-columns-start

Always use the singular name. Where possible avoid simply using id as the primary identifier for the table. Do not add a column with the same name as its table and vice versa. Always use lowercase except where it may make sense not to, such as with proper nouns.

.. sql-presto-style-guide-naming-conventions-columns-end


.. _sql-presto-style-guide-naming-conventions-correlation:

Correlation names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-naming-conventions-correlation-start

A correlation name assigns a temporary name to a table. A correlation name is defined within the **FROM** clause after the table name.

Syntax::

   FROM table_name correlation_name

Example:

   FROM Merged_Customers mc

When using correlations:

* Assign names that clearly relate to the table. For example: a table named "Merged_Customers" should have a correlation name of "mc".
* Always use the first letter of the table as the first letter of the correlation.
* Append additional alphanumeric characters as necessary's to ensure unique correlation names.
* Ensure that correlation names are used only within the same query.

.. sql-presto-style-guide-naming-conventions-correlation-end


.. _sql-presto-style-guide-naming-conventions-suffixes:

Suffix names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-naming-conventions-suffixes-start

The following suffixes represent patterns that should be applied to column names in SQL tables. These patterns help ensure the purpose of columns can be easily understood by all users. Use the correct suffixes, use them consistently, and use them everywhere they are appropriate.

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Suffix
     - Description
   * - **_id**
     - A unique identifier such as a column that is a primary key.
   * - **_status**
     - A flag value or some other status of any type such as ``publication_status``.
   * - **_total**
     - The total or sum of a collection of values.
   * - **_num**
     - Denotes the field contains any kind of number.
   * - **_name**
     - Signifies a name such as ``first_name``.
   * - **_seq**
     - Contains a contiguous sequence of values.
   * - **_date**
     - Denotes a column that contains the date of something.
   * - **_tally**
     - A count.
   * - **_size**
     - The size of something such as a file size or clothing.
   * - **_addr**
     - An address for the record could be physical or intangible such as ``ip_addr``.

.. sql-presto-style-guide-naming-conventions-suffixes-end


.. _sql-presto-style-guide-naming-conventions-tables:

Table names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-naming-conventions-tables-start

Use a collective name or, less ideally, a plural form. For example (in order of preference) staff and employees. Do not prefix with tbl or any other such descriptive prefix or Hungarian notation. Never give a table the same name as one of its columns and vice versa. Avoid, where possible, concatenating two table names together to create the name of a relationship table. Rather than cars_mechanics prefer services.

.. sql-presto-style-guide-naming-conventions-tables-end


.. _sql-presto-style-guide-null-values:

NULL values
--------------------------------------------------

.. sql-presto-style-guide-null-values-start

Functions may fail when they encounter a **NULL** value and others may return **NULL** values if any of their arguments return **NULL** values.

* Use the **COALESCE()** function to convert to a zero-length string when using the **CONCAT()** and **SUM()** functions.
* Use the **COALESCE()** function to to identify math. For example, multiplication will return **NULL** if any field is **NULL**. For example, because ``1`` is the identity for multiplication, use ``COALESCE(myColumn, 1)``

.. sql-presto-style-guide-null-values-end


.. _sql-presto-style-guide-reserved-words:

Reserved words
--------------------------------------------------

.. sql-presto-style-guide-reserved-words-start

Always use uppercase for the reserved keywords like **SELECT** and **WHERE**. It is best to avoid the abbreviated keywords and use the full length ones where available (prefer **ABSOLUTE** to **ABS**). Do not use database server specific keywords where an ANSI SQL keyword already exists performing the same function. This helps to make code more portable.

.. code-block:: sql
   :linenos:

   SELECT model_num
   FROM Phones AS p
   WHERE p.release_date > '2014-09-30'

.. sql-presto-style-guide-reserved-words-end


.. _sql-presto-style-guide-reserved-keywords:

Reserved keywords
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-reserved-keywords-start

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

.. sql-presto-style-guide-reserved-keywords-end


.. _sql-presto-style-guide-one-way-sha256-hashes:

One-way SHA-256 hashes
--------------------------------------------------

.. sql-presto-style-guide-one-way-sha256-hashes-start

Apply one-way SHA-256 hashes to fields that contain PII data. A one-way hash ensures that data can no longer be recognizable as valid PII, yet still allows that data to applied to segments that report on users who were flagged for removal or deletion and helps ensure that removed or obfuscated data is not sent from Amperity.

.. sql-presto-style-guide-one-way-sha256-hashes-end

.. sql-presto-style-guide-one-way-sha256-hash-syntax-start

A one-way SHA-256 hash has the following syntax:

.. code-block:: none

   TO_HEX(SHA256(TO_UTF8(UPPER(TRIM(FIELD)))))

and uses the following Presto SQL functions:

* ``TRIM()`` removes whitespace from the field.
* ``UPPER()`` sets all characters to upper-case. 
* ``TO_UTF8()`` converts the data into a binary format.
* ``SHA256()`` hashes data with a one-way SHA-256 hash.
* ``TO_HEX()`` converts the binary data into a string.

.. sql-presto-style-guide-one-way-sha256-hash-syntax-end


.. _sql-presto-style-guide-whitespace:

Whitespace
--------------------------------------------------

.. sql-presto-style-guide-whitespace-start

To make the code easier to read it is important that the correct complement of spacing is used. Do not crowd code or remove natural language spaces.

.. sql-presto-style-guide-whitespace-end


.. _sql-presto-style-guide-whitespace-line-spacing:

Line spacing
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-whitespace-line-spacing-start

Always include newlines/vertical space:

* before **AND** or **OR**
* after semicolons to separate queries for easier reading
* after each keyword definition
* before a comma when separating multiple columns into logical groups
* to separate code into related sections, which helps to ease the readability of large chunks of code.

Putting commas and conjunctions at the start of the line makes it easier to comment out a single line without disturbing the rest of the query

.. code-block:: sql
   :linenos:

   SELECT
     a.title
     ,a.release_date
     --,a.recording_date
     ,a.production_date
   FROM albums AS a
   WHERE a.title = 'Charcoal Lane'
     OR a.title = 'The New Danger';

.. sql-presto-style-guide-whitespace-line-spacing-end


.. _sql-presto-style-guide-whitespace-spaces:

Spaces
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-style-guide-whitespace-spaces-start

Spaces should be used to line up the code so that the root keywords all start on the same character boundary, and also so that  This makes it easy to keep track of where you are in a query that may be multiple layers deep.

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

* before and after equals (``=``)
* after commas (``,``)
* surrounding apostrophes (``'``), but not within parentheses or with a trailing comma or semicolon.

.. code-block:: sql
   :linenos:

   SELECT
     a.title
     ,a.release_date
     ,a.recording_date
   FROM albums AS a
   WHERE a.title = 'Charcoal Lane'
     OR a.title = 'The New Danger'

.. sql-presto-style-guide-whitespace-spaces-end


.. _sql-presto-style-guide-example-query:

Example SELECT statement
--------------------------------------------------

.. sql-presto-style-guide-example-query-start

The following example shows selecting the Amperity ID, purchase date, and order ID, and then uses two window functions to rank by transaction totals, and then put in descending order to sort the most recent purchase date first:

.. code-block:: sql
   :linenos:

   SELECT
     t.Amperity_Id,
     t.purchasedate,
     t.orderid,
     rank() OVER (PARTITION BY t.Amperity_Id
                  ORDER BY t.transactiontotal DESC) AS rank,
     t.transactiontotal,
     sum(t.transactiontotal) OVER (PARTITION BY t.Amperity_Id
                                   ORDER BY t.purchasedate) AS rolling_sum
   FROM
     TransactionsEcomm t
   ORDER BY t.Amperity_Id, rank
   LIMIT 100

.. sql-presto-style-guide-example-query-end


.. _sql-presto-with:

WITH clause
==================================================

.. sql-presto-with-start

The **WITH** clause defines a common table expression (CTE).

.. sql-presto-with-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-cte-start
   :end-before: .. term-cte-end

.. sql-presto-with-clause-example-multiple-ctes-start

The following example shows using multiple CTEs:

.. code-block:: sql
   :linenos:

   WITH new_in_21 AS (
     SELECT
       amperity_id
       ,one_and_done
     FROM Transaction_Attributes
     WHERE YEAR(first_order_datetime) = 2025
   ),

   product_categories AS (
     SELECT DISTINCT
       new_in_21.amperity_id
       ,one_and_done
       ,product_category
     FROM Unified_Itemized_Transactions uit
     INNER JOIN new_in_21 ON new_in_21.amperity_id=uit.amperity_id
   )

   SELECT
     product_category
     ,COUNT(DISTINCT amperity_id) customer_count
     ,1.0000*SUM(CASE
       WHEN one_and_done
       THEN 1
       ELSE 0
     END) / COUNT(DISTINCT amperity_id) pct_one_done
   FROM product_categories
   GROUP BY 1
   ORDER BY 3 DESC

.. sql-presto-with-clause-example-multiple-ctes-end


.. _sql-presto-select-statement:

SELECT statement
==================================================

.. sql-presto-select-statement-start

The **SELECT** statement defines a set of data to be returned from a data table. The set of returned data is often referred to as the result-set. Use the **SELECT** statement to retrieve rows from any table in the customer 360 database.

.. sql-presto-select-statement-end

.. sql-presto-select-statement-about-start

A **SELECT** statement can be complex, depending on the type of query you need to make. For example, the following **SELECT** statement ranks transactions by Amperity ID and by largest dollar totals:

.. code-block:: sql
   :linenos:

   SELECT
     t.orderid
     ,t.amperity_id
     ,t.transactiontotal
     ,RANK() OVER (
       PARTITION BY t.amperity_id
       ORDER BY t.transactiontotal DESC
     ) AS rank
   FROM TransactionsEcomm t
   ORDER BY t.amperity_id, rank ASC 
   LIMIT 100

The rest of this topic describes the clauses, expressions, functions, and operators that are the most commonly used within the **SQL Segment Editor** in Amperity. More functionality than what is described in this topic is supported, as the segment editors use Presto SQL.

.. important:: Not all of the functionality described in the official documentation for `Presto SQL <https://prestodb.io/docs/current/index.html>`__ |ext_link| should be used in the **SQL Segment Editor**.

.. sql-presto-select-statement-about-end


.. _sql-presto-select-statement-subquery-predicates:

Subquery predicates
--------------------------------------------------

.. sql-presto-select-statement-subquery-predicates-start

A subquery is an expression which is composed of a query. The subquery is correlated when it refers to columns outside of the subquery. Logically, the subquery will be evaluated for each row in the surrounding query. The referenced columns will thus be constant during any single evaluation of the subquery.

.. note:: Support for correlated subqueries is limited. Not every standard form is supported.

.. sql-presto-select-statement-subquery-predicates-end


.. _sql-presto-select-statement-subquery-predicate-exists:

EXISTS predicate
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-select-statement-subquery-predicate-exists-start

The **EXISTS** predicate determines if a subquery returns any rows:

.. code-block:: sql
   :linenos:

   SELECT name
   FROM nation
   WHERE EXISTS (SELECT * FROM region WHERE region.regionkey = nation.regionkey)

.. sql-presto-select-statement-subquery-predicate-exists-end


.. _sql-presto-select-statement-subquery-predicate-in:

IN predicate
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-select-statement-subquery-predicate-in-start

The **IN** predicate determines if any values produced by the subquery are equal to the provided expression. The result of **IN** follows the standard rules for **NULL** values. The subquery must produce exactly one column:

.. code-block:: sql
   :linenos:

   SELECT name
   FROM nation
   WHERE regionkey IN (SELECT regionkey FROM region)

.. sql-presto-select-statement-subquery-predicate-in-end


.. _sql-presto-select-distinct-statement:

SELECT DISTINCT statement
==================================================

.. sql-presto-select-distinct-statement-start

Use the **SELECT DISTINCT** statement instead of **SELECT** to return only distinct rows of data.

For example:

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     amperity_id
     ,order_id
     ,order_quantity
     ,order_datetime
   FROM Unified_Transactions

.. sql-presto-select-distinct-statement-end


.. _sql-presto-from-clause:

FROM clause
==================================================

.. sql-presto-from-clause-start

The **FROM** clause specifies the name of the data table against which the SQL query will be run and is part of every **SELECT** statement.

.. sql-presto-from-clause-end


.. _sql-presto-tablesample-bernoulli:

TABLESAMPLE BERNOULLI clause
--------------------------------------------------

.. sql-presto-tablesample-bernoulli-clause-start

Use the **TABLESAMPLE BERNOULLI** clause to return a random sample of records. Specify the size of the random sample within parentheses. For example:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
   FROM Customer_360 TABLESAMPLE BERNOULLI (50)

will return a random sample of records from the **Customer 360** table at a 50% rate.

The following example shows a segment for use with campaigns that samples all customers with the surname "Smith" who do not have the given name "Joe" at a 30% rate:

.. code-block:: sql
   :linenos:

   SELECT
     "amperity_id"
   FROM "Customer_360" TABLESAMPLE BERNOULLI (30)
   WHERE
     (
       (
         "amperity_id" IN (
           SELECT DISTINCT "t0"."amperity_id"
           FROM "Customer_360" "t0"
           INNER JOIN "Customer_360" "t1" 
           ON "t0"."amperity_id" = "t1"."amperity_id"
           WHERE
             (
               LOWER("t0"."surname") = 'smith'
               AND LOWER("t1"."given_name") <> 'joe'
             )
         )
       )
       AND LOWER("surname") = 'smith'
       AND LOWER("given_name") <> 'joe'
     )

and returns a list of Amperity IDs ready for use with a campaign.

.. sql-presto-tablesample-bernoulli-clause-end


.. _sql-presto-left-join:

LEFT JOIN clause
==================================================

.. sql-presto-left-join-clause-start

The **LEFT JOIN** clause joins rows from two tables. For a **LEFT JOIN**, each row in the left table is joined with all matching rows from the right table. For rows with no match in the right table, the join is completed with **NULL** to represent column values.

For example:

.. code-block:: sql
   :linenos:

   SELECT * FROM (VALUES 1, 2) t("left") 
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

.. sql-presto-left-join-clause-end


.. _sql-presto-where:

WHERE clause
==================================================

.. sql-presto-where-clause-start

The **WHERE** clause filters records, and then returns only records that match the specified condition and value. The **WHERE** clause can be combined with **AND**, **OR**, and **NOT** operators.

.. sql-presto-where-clause-end

.. _sql-presto-where-parentheses:

.. sql-presto-where-clause-tip-parentheses-start

.. tip:: Use parentheses to group the contents of **AND**, **OR**, and **NOT** operators within complex SQL to ensure that each element within the **WHERE** clause runs in the correct order. For example:

   **Do**

   .. code-block:: sql
      :linenos:

      AND (c360.email IS NOT NULL OR c360.phone IS NOT NULL)
      AND (
          (is_cancellation IS NULL)
        OR (NOT is_cancellation)
      )
      AND (
        (is_return IS NULL)
        OR (NOT is_return)
      )

   **Avoid**

   .. code-block:: sql

      AND c360.email IS NOT NULL OR c360.phone IS NOT NULL
      AND is_cancellation IS NULL OR NOT is_cancellation
      AND is_return IS NULL OR NOT is_return

.. sql-presto-where-clause-tip-parentheses-end


.. _sql-presto-statement-operator-and:

AND operator
--------------------------------------------------

.. sql-presto-statement-operator-and-start

The **AND** operator is used to filter records based on more than one condition. The **AND** operator displays a record if all the conditions separated by **AND** are **TRUE**.

.. sql-presto-statement-operator-and-end


.. _sql-presto-statement-operator-or:

OR operator
--------------------------------------------------

.. sql-presto-statement-operator-or-start

The **AND** operator is used to filter records based on more than one condition. The **OR** operator displays a record if any of the conditions separated by **OR** is **TRUE**.

.. sql-presto-statement-operator-or-end


.. _sql-presto-statement-operator-not:

NOT operator
--------------------------------------------------

.. sql-presto-statement-operator-not-start

The **NOT** operator displays a record if the conditions is ``NOT TRUE``.

.. sql-presto-statement-operator-not-end


.. _sql-presto-case:

CASE expression
==================================================

.. sql-presto-case-expression-start

The standard SQL **CASE** expression has two forms: simple and searched.

.. note:: If a **CASE** expression is too long, add a new line between **WHEN** and **THEN** clauses to make the line more readable.

.. sql-presto-case-expression-end


.. _sql-presto-case-simple:

Simple form
--------------------------------------------------

.. sql-presto-case-simple-start

The simple form searches each value expression from left to right until it finds one that equals expression:

.. code-block:: sql
   :linenos:

   CASE expression
     WHEN value THEN result
     [ WHEN ... ]
     [ ELSE result ]
   END

The result for the matching value is returned.

If no match is found, the result from the **ELSE** clause is returned if it exists, otherwise **NULL** is returned:

.. code-block:: sql
   :linenos:

   SELECT a,
     CASE a
       WHEN 1 THEN 'one'
       WHEN 2 THEN 'two'
       ELSE 'many'
     END

.. sql-presto-case-simple-end


.. _sql-presto-case-searched:

Searched form
--------------------------------------------------

.. sql-presto-case-searched-start

The searched form evaluates each boolean condition from left to right until one is true and returns the matching result:

.. code-block:: sql
   :linenos:

   CASE
     WHEN condition THEN result
     [ WHEN ... ]
     [ ELSE result ]
   END

If no conditions are true, the result from the **ELSE** clause is returned if it exists, otherwise **NULL** is returned:

.. code-block:: sql
   :linenos:

   SELECT a, b,
     CASE
       WHEN a = 1 THEN 'aaa'
       WHEN b = 2 THEN 'bbb'
       ELSE 'ccc'
     END

.. sql-presto-case-searched-end


.. _sql-presto-case-searched-example-group-states-by-timezone:

Group states by time zones
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-case-searched-example-group-states-by-timezone-start

The following **CASE** expression groups states by North American time zone:

.. code-block:: sql
   :linenos:

   ,CASE
     WHEN state = 'HI' THEN 'Hawaii'
     WHEN state = 'AK' THEN 'Alaska'
     WHEN state IN ('WA','OR','CA','NV') THEN 'Pacific Time (US & Canada)'
     WHEN state IN ('MT','ID','WY','UT','CO','AZ','NM') THEN 'Mountain Time (US & Canada)'
     WHEN state IN ('ND','SD','NE','KS','OK','TX','MN','WI','IA','IL','MO','AR','TN','LA','MS','AL') THEN 'Central Time (US & Canada)'
     WHEN state IN ('MI','IN','OH','KY','FL','GA','SC','NC','WV','VA','MD','DE','DC','NJ','PA', 'NY','CT','RI','MA','VT','NH','ME') THEN 'Eastern Time (US & Canada)'
     WHEN state = 'PR' THEN 'Puerto Rico'
     WHEN state = 'GU' THEN 'Guam'
     WHEN state = 'VI' THEN 'US Virgin Islands'
     WHEN state = 'AS' THEN 'American Samoa'
   ELSE '' END AS time_zone

.. sql-presto-case-searched-example-group-states-by-timezone-end


.. _sql-presto-group-by:

GROUP BY clause
==================================================

.. sql-presto-group-by-clause-start

The **GROUP BY** clause divides the output of a **SELECT** statement into groups of rows containing matching values. A simple **GROUP BY** clause may contain any expression composed of input columns or it may be an ordinal number selecting an output column by position (starting at one).

The following queries are equivalent. They both group the output by the ``given_name`` input column with the first query using the ordinal position of the output column and the second query using the input column name:

.. code-block:: sql

   SELECT COUNT(*), given_name FROM Customer_360 GROUP BY 2

is equivalent to:

.. code-block:: sql

   SELECT COUNT(*), given_name FROM Customer_360 GROUP BY given_name

**GROUP BY** clauses can group output by input column names not appearing in the output of a select statement. For example, the following query generates row counts for the customer table using the input column ``surname``:

.. code-block:: sql

   SELECT COUNT(*) FROM Customer_360 GROUP BY surname

returns a table similar to:

.. code-block:: mysql

    _col0
   -------
    82
    468
    42
    9
    1
   (3984 rows)

When a **GROUP BY** clause is used in a **SELECT** statement all output expressions must be either aggregate functions or columns present in the **GROUP BY** clause.

.. sql-presto-group-by-clause-end


.. _sql-presto-group-by-cube:

CUBE operator
--------------------------------------------------

.. sql-presto-group-by-cube-start

The **CUBE** operator generates all possible groupings for the specified group of columns.

For example, the following query:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,purchase_brand
     ,SUM(order_revenue) AS total_order_revenue
   FROM Unified_Transactions
   --WHERE amperity_id = '12345-abcde'
   GROUP BY CUBE(amperity_id, purchase_brand)
   ORDER BY amperity_id, purchase_brand

will return a table similar to:

.. code-block:: mysql

   ------------- ---------------- ---------------------
    amperity_id   purchase_brand   total_order_revenue
   ------------- ---------------- ---------------------
                  FoxEssentials    3976068.32
                  FoxEssentials    3976068.32
                  GoldenSwan       1358357.54
                  GoldenSwan       1358357.54
                  TrendyBear       5703142.95
    ...
   ------------- ---------------- ---------------------

.. sql-presto-group-by-cube-end


.. _sql-presto-group-by-rollup:

ROLLUP operator
--------------------------------------------------

.. sql-presto-group-by-rollup-start

The **ROLLUP** operator generates all possible subtotals for the specified group of columns.

For example, the following query:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,purchase_brand
     ,SUM(order_revenue) AS total_order_revenue
   FROM Unified_Transactions
   --WHERE amperity_id = '12345-abcde'
   GROUP BY ROLLUP(amperity_id, purchase_brand)
   ORDER BY amperity_id, purchase_brand

will return a table similar to:

.. code-block:: mysql

   ------------- ---------------- ---------------------
    amperity_id   purchase_brand   total_order_revenue
   ------------- ---------------- ---------------------
                  FoxEssentials    3976068.32
                  GoldenSwan       1358357.54
                  TrendyBear       5703142.95
                                   11037568.81
    ...
   ------------- ---------------- ---------------------

.. sql-presto-group-by-rollup-end

.. _sql-presto-having:

HAVING clause
==================================================

.. sql-presto-having-clause-start

The **HAVING** clause sorts a result set by one or more output expressions. Use in conjunction with aggregate functions and the **GROUP BY** clause to control which groups are selected. A **HAVING** clause eliminates groups that do not satisfy the given conditions and filters groups after groups and aggregates are computed.

For example:

.. code-block:: sql
   :linenos:

   SELECT
     COUNT(*)
     ,purchase_brand
     ,payment_method
     ,CAST(SUM(order_quantity) AS bigint) AS quantity
   FROM Unified_Transactions
   GROUP BY purchase_brand, payment_method
   HAVING SUM(order_quantity) > 100
   ORDER BY quantity DESC

returns a table similar to:

.. code-block:: mysql

   ---------------- ---------------- ----------
    purchase_brand   payment_method   quantity
   ---------------- ---------------- ----------
    FoxEssentials    VISA             51753
    GoldenSwan       VISA             50933
    TrendyBear                        34329
    FoxEssentials    PayPal           33513
    GoldenSwan       MASTER           16651
    GoldenSwan       MASTER           6482
    FoxEssentials    DISCOVER         4673
    ...
   ---------------- ---------------- ----------

.. sql-presto-having-clause-end


.. _sql-presto-set-operations:

Set operations
==================================================

.. sql-presto-set-operations-start

Use one of the following set operation clauses to combine the results of more than one **SELECT** statement into a single result set:

* :ref:`sql-presto-except`
* :ref:`sql-presto-intersect`
* :ref:`sql-presto-union`

.. sql-presto-set-operations-end


.. _sql-presto-except:

EXCEPT clause
--------------------------------------------------

.. sql-presto-except-start

Use the **EXCEPT** clause to return the rows that are in the result set of the first query, but not the second.

For example, to compare two tables and find out which rows are in table B, but not in table A:

.. code-block:: sql

   SELECT table_b
   EXCEPT SELECT table_a

.. tip:: The **EXCEPT** clause deduplicates records. For example, if all of the rows in table A are present in table B, the results should be 0 rows.

   Use a query similar to the following to verify that 0 rows is accurate:

   .. code-block:: sql
      :linenos:

      SELECT COUNT(*)
      FROM (
        SELECT DISTINCT *
        FROM table_b
      )

.. sql-presto-except-end


.. _sql-presto-intersect:

INTERSECT clause
--------------------------------------------------

.. sql-presto-intersect-start

Use the **INTERSECT** clause to return only the rows that are in the result sets of both the first and the second queries.

For example, to find all rows in both tables A and B:

.. code-block:: sql

   SELECT table_b
   INTERSECT SELECT table_a

.. sql-presto-intersect-end


.. _sql-presto-union:

UNION clause
--------------------------------------------------

.. sql-presto-union-clause-start

The **UNION** clause combines the the unique results of one query with the unique results of a second. For example:

::

   SELECT shirts, pants
   UNION
   SELECT shoes

will return:

::

    _col0
   -------
    shirts
    pants
    shoes

The **UNION** clause supports two arguments: **ALL** and **DISTINCT**. Use **UNION ALL** to return all rows, even if they are identical. **UNION DISTINCT** is the default behavior of **UNION** (when an argument is not specified) and will return only unique rows.

.. sql-presto-union-clause-end

.. sql-presto-union-clause-tip-start

.. tip:: Use :ref:`GROUP BY CUBE <sql-presto-group-by-cube>` and/or :ref:`GROUP BY ROLLUP <sql-presto-group-by-rollup>` clauses for more efficient unions of records.

.. sql-presto-union-clause-tip-end

.. sql-presto-union-clause-example-start

For example, the following query:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,purchase_brand
     ,SUM(order_revenue) AS total_order_revenue
   FROM Unified_Transactions
   --WHERE amperity_id = '12345-abcde'
   GROUP BY amperity_id, purchase_brand

   UNION ALL

   SELECT
     amperity_id
     ,NULL
     ,SUM(order_revenue) AS total_order_revenue
   FROM Unified_Transactions
   --WHERE amperity_id = '12345-abcde'
   GROUP BY amperity_id

   ORDER BY purchase_brand NULLS LAST

will return a table similar to:

.. code-block:: mysql

   ------------- ---------------- ---------------------
    amperity_id   purchase_brand   total_order_revenue
   ------------- ---------------- ---------------------
                  FoxEssentials    3976068.32
                  GoldenSwan       1358357.54
                  TrendyBear       5703142.95
                                   11037568.81
    ...
   ------------- ---------------- ---------------------

.. sql-presto-union-clause-example-end


.. _sql-presto-unnest:

UNNEST clause
==================================================

.. sql-presto-unnest-clause-start

The **UNNEST** clause expands an **ARRAY** or **MAP** into a relation.

* Arrays are expanded into a single column.
* Maps are expanded into two columns (key, value).

**UNNEST** can also be used with multiple arguments, in which case they are expanded into multiple columns, with as many rows as the highest cardinality argument (the other columns are padded with **NULL** values).

**UNNEST** can optionally have a **WITH ORDINALITY** clause, in which case an additional ordinality column is added to the end. **UNNEST** is normally used with a **JOIN** and can reference columns from relations on the left side of the join.

.. sql-presto-unnest-clause-end

.. sql-presto-unnest-clause-example-expand-email-address-start

Use the UNNEST clause in the SQL segment to expand phone and/or email addresses so that the query looks at individual bad values. The following example shows using an **UNNEST** clause to expand email addresses that are part of a bad-values blocklist SQL query:

.. code-block:: sql
   :linenos:

   SELECT
     REGEXP_REPLACE(v.value,'\+.*@','@') AS value
     ,M.semantic
     ,M.datasource
     ,M.domain_table
     ,M.proxy
   FROM (
     SELECT DISTINCT  
       SPLIT(UPPER(email), ',') AS vs
       ,'email' AS semantic
       ,REGEXP_EXTRACT(datasource, '.+?(?=:)') AS datasource
       ,datasource AS domain_table
       ,UPPER(given_name) AS proxy
     FROM Unified_Coalesced AS UC
   ) AS M
   CROSS JOIN UNNEST(vs) AS v(value)
   WHERE value IS NOT NULL
   AND value <> ''),

.. sql-presto-unnest-clause-example-expand-email-address-end


.. _sql-presto-values:

VALUES clause
==================================================

.. sql-presto-values-clause-start

The **VALUES** clause can be used anywhere a query can be used, such as the **FROM** clause of a **SELECT** statement, an **INSERT**, or even at the top level. The **VALUES** clause creates an anonymous table without column names, but the table and columns can be named using an **AS** keyword with column aliases.

To return a table with one column and three rows:

.. code-block:: sql

   VALUES 1, 2, 3

To return a table with two columns and three rows:

.. code-block:: sql
   :linenos:

   VALUES
     (1, 'a'),
     (2, 'b'),
     (3, 'c')

To return table with column ID and name:

.. code-block:: sql
   :linenos:

   SELECT * FROM (
     VALUES
       (1, 'a'),
       (2, 'b'),
       (3, 'c')
   ) AS t (id, name)

To add a table with column ID and name:

.. code-block:: sql
   :linenos:

   CREATE TABLE example AS
   SELECT * FROM (
     VALUES
       (1, 'a'),
       (2, 'b'),
       (3, 'c')
   ) AS t (id, name)

.. sql-presto-values-clause-end


.. _sql-presto-window-functions:

Window functions
==================================================

.. https://prestodb.io/docs/current/functions/window.html

.. sql-presto-window-functions-start

A window function performs calculations across rows. A window function runs *after* the **HAVING** clause, but *before* the **ORDER BY** clause. A window function requires special syntax using the **OVER** clause to specify the window.

.. tip:: When a window function is too long, add a new code line to improve readability.

A window function has the following components:

#. A list of columns that act as inputs to the window function.
#. A window function that defines the operation to be performed by the window function. For example: **RANK()** or **SUM()**. This may be any of the ranking functions, value functions, or aggregate functions available in Presto SQL.
#. **OVER()** defines the window frame, which represents a sliding window.
#. **PARTITION BY** separates the input into different partitions; only rows in the specified partition will be considered by the window function
#. **ORDER BY** determines the order in which the input will be processed by the window function.

   .. tip:: Use **ROWS BETWEEN** to define any number of preceding and following rows, as related to the current row.
   
      For example:

      .. code-block:: sql

         ROWS BETWEEN 1 preceding AND 1 following

      .. code-block:: sql

         ROWS BETWEEN current row AND 1 following

      .. code-block:: sql

         ROWS BETWEEN 5 preceding AND 2 preceding

#. **DESC** sorts the output in descending order.

   .. tip:: Add ``_uuid_pk`` to window function ordering--``DESC, _uuid_pk``--to return deterministic results in case of ties.

For example:

.. code-block:: sql
   :linenos:

   SELECT input_1, input_2, input_3,
     window_function() OVER (
       PARTITION BY input_2
       ORDER BY input_3 DESC, _uuid_pk
     ) AS rnk
   FROM table_name
   ORDER BY input_2, rnk

.. sql-presto-window-functions-end


.. _sql-presto-window-function-example-rolling-seven-day-window:

Rolling 7-day window
--------------------------------------------------

.. sql-presto-window-function-example-rolling-seven-day-window-start

The following example shows a rolling seven day window for order revenue.

.. code-block:: sql
   :linenos:

   SELECT
     *
   FROM (
     SELECT
       purchase_channel
       ,order_day
       ,SUM(order_revenue) OVER (
         PARTITION BY purchase_channel
         ORDER BY order_day
         ROWS BETWEEN 6 preceding AND current row
       ) rolling_7_day_revenue
     FROM (
       SELECT
         purchase_channel
         ,DATE(order_datetime) order_day
         ,SUM(order_revenue) order_revenue
       FROM Unified_Transactions
       WHERE amperity_id IS NOT NULL
       AND order_datetime > (CURRENT_DATE - interval '36' day)
       GROUP BY 1,2
     )
   )
   WHERE order_day > (CURRENT_DATE - interval '30' day)
   ORDER BY 1,2

.. sql-presto-window-function-example-rolling-seven-day-window-end


.. _sql-presto-window-function-example-retention-rate-previous-year:

Retention rate, previous year
--------------------------------------------------

.. sql-presto-window-function-example-retention-rate-previous-year-start

The following example shows how to use a rolling 1-year window to return the values necessary for calculating retention rate during the previous year.

.. code-block:: sql
   :linenos:

   WITH customers AS (
     SELECT DISTINCT amperity_id AS amperity_id
     FROM Unified_Transactions
     WHERE order_datetime < CAST(CURRENT_DATE - interval '1' year AS date)
   )
   ,orders AS (
     SELECT DISTINCT amperity_id AS ordered_in_past_year
     FROM Unified_Transactions
     WHERE order_datetime >= CAST(CURRENT_DATE - interval '1' year AS date)
   )
   SELECT
     SUM(CAST(ordered_in_past_year IS NULL AS int)) AS not_retained
     ,SUM(CAST(ordered_in_past_year IS NOT NULL AS int)) AS retained
   FROM customers
   LEFT JOIN orders ON amperity_id = ordered_in_past_year

This query will return all customers who purchased more than 1 year ago, and then separates them into two groups: customers who did purchase within the previous year (``retained``) and customers who did not (``not_retained``).

Retention rate, in this example, is the number of customers who made a repeat purchase within the previous year represented as a percentage of all customers.

For example, if this query returned a table similar to:

.. code-block:: mysql

   -------------- ----------
    not_retained   retained
   -------------- ----------
    525217         87421
   -------------- ----------

this means there are 612,638 Amperity IDs (not_retained plus retained) and 87,421 Amperity IDs that made a repeat purchase (retained). Divide the retained amount by the total number of Amperity IDs to get the retention rate: 14.2%.

.. sql-presto-window-function-example-retention-rate-previous-year-end


.. _sql-presto-order-by:

ORDER BY clause
==================================================

.. sql-presto-order-by-clause-start

The **ORDER BY** clause sorts a result set by one or more output expressions.

.. code-block:: none

    ORDER BY expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...]

Each expression may be composed of output columns or it may be an ordinal number selecting an output column by position (starting at one). The **ORDER BY** clause is evaluated as the last step of a query after any **GROUP BY** or **HAVING** clause. The default null ordering is **NULLS LAST**, regardless of the ordering direction.

.. sql-presto-order-by-clause-end


.. _sql-presto-limit:

LIMIT clause
==================================================

.. sql-presto-limit-clause-start

The **LIMIT** clause restricts the number of rows in the result set. The following example queries a large table, but the limit clause restricts the output to only have five rows (because the query lacks an **ORDER BY**, exactly which rows are returned is arbitrary):

.. code-block:: sql

   SELECT orderdate FROM orders LIMIT 5;

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

.. sql-presto-limit-clause-end


.. _sql-presto-operators:

Operators
==================================================

.. sql-presto-operators-start

An operator compares two data items, and then returns a result.

.. sql-presto-operators-end

* :ref:`sql-presto-operators-between`
* :ref:`sql-presto-operators-comparison`
* :ref:`sql-presto-operators-is-null`
* :ref:`sql-presto-operators-is-not-null`


.. _sql-presto-operators-between:

BETWEEN
--------------------------------------------------

.. sql-presto-operators-comparison-start

Use the **BETWEEN** operator to test if a value falls within the specified range using the syntax **BETWEEN** [minimum value] **AND** [maximum value]:

.. code-block:: none

   SELECT 3 BETWEEN 2 AND 6;

The statement shown above is equivalent to the following statement:

.. code-block:: none

   SELECT 3 >= 2 AND 3 <= 6;

**Presence of NULL evaluates to NULL**

The presence of **NULL** will result in the statement evaluating to **NULL**:

.. code-block:: none

   SELECT NULL BETWEEN 2 AND 4;

and:

.. code-block:: none

   SELECT 2 BETWEEN NULL AND 6;

**String arguments must be of same type**

Use the **BETWEEN** operator to evaluate string arguments as long as the value, min, and max parameters are of the same type:

.. code-block:: none

   SELECT 'Paul' BETWEEN 'John' AND 'Ringo';

whereas this query will produce an error:

.. code-block:: none

   SELECT '2.3' BETWEEN 'John' AND '35.2';


**Within a CASE statement**

.. code-block:: none

   CASE
     WHEN field BETWEEN 20 AND 1 THEN 'match'
     ELSE 'noop'
   END

is equivalent to:

.. code-block:: none

   CASE
     WHEN field < 20 AND field > 1 THEN 'match'
     ELSE 'noop'
   END

.. sql-presto-operators-comparison-end


.. _sql-presto-operators-comparison:

Comparison operators
--------------------------------------------------

.. sql-presto-operators-comparison-start

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

Quantifiers--:ref:`sql-presto-operator-comparison-all`, :ref:`sql-presto-operator-comparison-any`, :ref:`sql-presto-operator-comparison-some`--may be used along with comparison operators to provide more specific comparisons.

.. sql-presto-operators-comparison-end


.. _sql-presto-operator-comparison-all:

ALL
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-operator-comparison-all-start

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
A <> ALL (subquery)     Evaluates to **TRUE** when A doesn't match any value.
A < ALL (subquery)      Evaluates to **TRUE** when A is smaller than the smallest value.
====================    ===========

.. sql-presto-operator-comparison-all-end


.. _sql-presto-operator-comparison-any:

ANY
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-operator-comparison-any-start

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
A <> ANY (subquery)     Evaluates to **TRUE** when A doesn't match one or more values.
A < ANY (subquery)      Evaluates to **TRUE** when A is smaller than the biggest value.
====================    ===========

.. sql-presto-operator-comparison-any-end


.. _sql-presto-operator-comparison-some:

SOME
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-operator-comparison-some-start

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

A <> SOME (subquery)    Evaluates to **TRUE** when A doesn't match one or more values.
A < SOME (subquery)     Evaluates to **TRUE** when A is smaller than the biggest value.
====================    ===========

.. sql-presto-operator-comparison-some-end


.. _sql-presto-operators-is-null:

IS NULL
--------------------------------------------------

.. sql-presto-operators-is-null-start

The **IS NULL** operator tests whether a value is **NULL**. This operator works for all data types.

Using **NULL** with **IS NULL** evaluates to **TRUE**:

.. code-block:: none

   select NULL IS NULL;

But any other constant does not evaluate to **FALSE**:

.. code-block:: none

   SELECT 3.0 IS NULL;

.. sql-presto-operators-is-null-end


.. _sql-presto-operators-is-not-null:

IS NOT NULL
--------------------------------------------------

.. sql-presto-operators-is-not-null-start

The **IS NULL** operator tests whether a value is not **NULL**. This operator works for all data types.

Using **NULL** with **IS NOT NULL** evaluates to **FALSE**:

.. code-block:: none

   select NULL IS NOT NULL;

But any other constant evaluates **TRUE**:

.. code-block:: none

   SELECT 3.0 IS NOT NULL;

.. sql-presto-operators-is-not-null-end


.. _sql-presto-operator-pivot:

PIVOT operator
==================================================

.. sql-presto-operator-pivot-start

.. warning:: Presto SQL does not support the use of a **PIVOT** operator.

.. sql-presto-operator-pivot-end


.. _sql-presto-functions:

Functions
==================================================

.. sql-presto-functions-start

A function is a SQL statement that accepts input parameters, performs actions, and then returns results. This section highlights some useful functions for use when building segments in Amperity.

.. sql-presto-functions-end

.. sql-presto-functions-note-start

.. note:: This section highlights a very small subset of `the complete list of functions available in Presto SQL <https://prestodb.io/docs/current/functions.html>`__ |ext_link|, many of which can be useful depending on the type of query.

.. sql-presto-functions-note-end

.. sql-presto-functions-list-start

The following list contains some of the most frequently used functions for building segments via the **SQL Segment Editor** (alphabetized):

* :ref:`sql-presto-function-array-agg`
* :ref:`sql-presto-function-array-join`
* :ref:`sql-presto-function-avg`
* :ref:`sql-presto-function-cast`
* :ref:`sql-presto-function-chr`
* :ref:`sql-presto-function-coalesce`
* :ref:`sql-presto-function-concat`
* :ref:`sql-presto-function-count`
* :ref:`sql-presto-function-current-date`
* :ref:`sql-presto-function-current-timestamp`
* :ref:`sql-presto-function-date-diff`
* :ref:`sql-presto-function-date-format`
* :ref:`sql-presto-function-date-trunc`
* :ref:`sql-presto-function-day-month-year`
* :ref:`sql-presto-function-dense-rank`
* :ref:`sql-presto-function-from-unixtime`
* :ref:`sql-presto-function-greatest`
* :ref:`sql-presto-function-if`
* :ref:`sql-presto-function-least`
* :ref:`sql-presto-function-length`
* :ref:`sql-presto-function-lower`
* :ref:`sql-presto-function-max`
* :ref:`sql-presto-function-median`
* :ref:`sql-presto-function-min`
* :ref:`sql-presto-function-now`
* :ref:`sql-presto-function-ntile`
* :ref:`sql-presto-function-percent-rank`
* :ref:`sql-presto-function-percentile`
* :ref:`sql-presto-function-rank`
* :ref:`sql-presto-function-regexp-extract`
* :ref:`sql-presto-function-regexp-like`
* :ref:`sql-presto-function-regexp-replace`
* :ref:`sql-presto-function-replace`
* :ref:`sql-presto-function-round`
* :ref:`sql-presto-function-split`
* :ref:`sql-presto-function-split-part`
* :ref:`sql-presto-function-substr`
* :ref:`sql-presto-function-sum`
* :ref:`sql-presto-function-to-hex`
* :ref:`sql-presto-function-to-unixtime`
* :ref:`sql-presto-function-trim`
* :ref:`sql-presto-function-try-cast`
* :ref:`sql-presto-function-upper`

.. sql-presto-functions-list-end


.. _sql-presto-function-array-agg:

ARRAY_AGG()
--------------------------------------------------

.. sql-presto-function-array-agg-start

Use the **ARRAY_AGG(x)** function to return an array created by ``x``.

.. sql-presto-function-array-agg-end


.. _sql-presto-function-array-agg-example-aggregate-order-ids:

Aggregate order IDs
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-array-agg-example-aggregate-order-ids-start

The following SQL query uses the **ARRAY_JOIN()** and **ARRAY_AGG()** functions to aggregate an array of order IDs using a comma as the delimiter:

.. code-block:: sql
   :linenos:
   :emphasize-lines: 3

   SELECT
     amperity_id
     ,ARRAY_JOIN(ARRAY_AGG(order_id), ', ') AS Orders
   FROM Transactions
   GROUP BY amperity_id
   LIMIT 1000

.. sql-presto-function-array-agg-example-aggregate-order-ids-end


.. _sql-presto-function-array-agg-example-chronological-order:

Sort in chronological order
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-array-agg-example-chronological-order-start

The following SQL query uses the **ARRAY_AGG()** function to sort a list of products in chronological order:

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     sub.amperity_id
     ,ARRAY_JOIN(ARRAY_AGG(sub.item_name) OVER(
       PARTITION BY sub.amperity_id
       ORDER BY sub.order_datetime DESC
       RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
     ), ', ') AS Products_Ordered
   FROM (
     SELECT DISTINCT
       amperity_id
       ,item_name
       ,order_datetime
     FROM DW_OrderDetail Z
     WHERE order_closed = true AND order_status <> 'Void'
   ) AS sub

.. warning:: This example only runs in tenants that are running on Microsoft Azure.

.. sql-presto-function-array-agg-example-chronological-order-end


.. _sql-presto-function-array-agg-example-separate-product-ids-with-pipe-symbol:

Separate product IDs with pipe symbol
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-array-agg-example-separate-product-ids-with-pipe-symbol-start

The following example joins product IDs and uses the pipe symbol (``|``) as a separator:

.. code-block:: sql

   ,ARRAY_JOIN(ARRAY_AGG(invoices), '|') AS product_ids

.. sql-presto-function-array-agg-example-separate-product-ids-with-pipe-symbol-end


.. _sql-presto-function-array-join:

ARRAY_JOIN()
--------------------------------------------------

.. sql-presto-function-array-join-start

Use the **ARRAY_JOIN(array, delimiter, string)** function to concatenate elements of a given ``array`` using a ``delimiter`` and an optional ``string`` to replace **NULL** values.

.. sql-presto-function-array-join-end


.. _sql-presto-function-array-join-example-join-order-ids:

Join order IDs
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-array-join-example-join-order-ids-start

The following SQL query uses the **ARRAY_JOIN()** and **ARRAY_AGG()** functions to aggregate an array of order IDs using a comma as the delimiter:

.. code-block:: sql
   :linenos:
   :emphasize-lines: 3

   SELECT
     amperity_id
     ,ARRAY_JOIN(ARRAY_AGG(order_id), ', ') AS Orders
   FROM Transactions
   GROUP BY amperity_id
   LIMIT 1000

.. sql-presto-function-array-join-example-join-order-ids-end


.. _sql-presto-function-avg:

AVG()
--------------------------------------------------

.. sql-presto-function-avg-start

Use the **AVG(x)** function to return the average of all input values.

.. sql-presto-function-avg-end


.. _sql-presto-function-cast-example-return-mean:

Return mean
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-cast-example-return-mean-start

The following example returns the mean.

.. code-block:: sql
   :linenos:

   SELECT
     product_category
     ,1.0*AVG(item_revenue) avg_item_revenue
   FROM Unified_Itemized_Transactions
   WHERE amperity_id IS NOT NULL
   GROUP BY 1
   ORDER BY 1 DESC

.. sql-presto-function-cast-example-return-mean-end


.. _sql-presto-function-cast:

CAST()
--------------------------------------------------

.. sql-presto-function-cast-start

Use the **CAST(value AS type)** function to cast the value of ``value`` as ``type``.

.. sql-presto-function-cast-end


.. _sql-presto-function-cast-example-cast-rfm-as-real:

Cast RFM as REAL data type
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-cast-example-cast-rfm-as-real-start

The following example shows using the **CAST()** function to cast the values of ``Recency``, ``Frequency``, and ``Monetary`` to the ``real`` data type, which is a floating-point, 32-bit inexact, variable-precision value.

.. code-block:: sql

   ,ROUND((CAST(Recency AS real) + CAST(Frequency AS real) + CAST(Monetary AS real)) / 3, 2) 

.. sql-presto-function-cast-example-cast-rfm-as-real-end


.. _sql-presto-function-cast-example-cast-as-uuid:

Cast as UUID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-cast-example-cast-as-uuid-start

The following example casts email addresses as a UUID:

.. code-block:: sql

   ,CAST(email AS UUID) AS "email_address"

.. sql-presto-function-cast-example-cast-as-uuid-end


.. _sql-presto-function-cast-example-cast-date-as-year:

Cast date as year
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-cast-example-cast-date-as-year-start

.. code-block:: sql

   ,CAST(YEAR(purchase_date) AS VARCHAR) AS purchase_year

.. sql-presto-function-cast-example-cast-date-as-year-end


.. _sql-presto-function-chr:

CHR()
--------------------------------------------------

.. sql-presto-function-chr-start

Use the **CHR(codepoint)** function to return the Unicode ``codepoint`` as a single-character string.

.. sql-presto-function-chr-end

.. sql-presto-function-chr-tip-start

.. tip:: Use the **CODEPOINT(string)** function to return the Unicode ``codepoint`` as the only character of ``string``. For example:

   .. code-block:: none

      CODEPOINT(')

   Returns:

   .. code-block:: none

      39

.. sql-presto-function-chr-tip-end


.. _sql-presto-function-chr-example-add-leading-apostrophe:

Add leading apostrophe
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-chr-example-add-leading-apostrophe-start

Some use cases for CSV files have a downstream dependency on Microsoft Excel. Excel automatically removes leading zeros and converts large numbers to scientific notation, such as 1.23E+15, to ensure that formulas and math operations work correctly.

Long strings are output from Amperity in the form of the Amperity ID, customer keys, loyalty program IDs, product codes, and so on. Add a leading apostrophe (**'**) to these strings within the Amperity segment to ensure these string values are interpreted as text by Excel.

Use the **CONCAT()** function to build a string with a leading character, and then use the **CHR()** function to apply Unicode codepoint ``39``, which is an apostrophe.

For example:

.. code-block:: sql

   CONCAT(CHR(39),customer_key)

.. sql-presto-function-chr-example-add-leading-apostrophe-end


.. _sql-presto-function-coalesce:

COALESCE()
--------------------------------------------------

.. sql-presto-function-coalesce-start

Use the **COALESCE(value1, value2)** function to return the first non-null value in the argument list. Arguments are only evaluated if necessary.

.. sql-presto-function-coalesce-end


.. _sql-presto-function-concat:

CONCAT()
--------------------------------------------------

.. sql-presto-function-concat-start

Use the **CONCAT(array1, array2)** function to concatenate a set of arrays into a single value that can be used elsewhere in a SQL query.

.. sql-presto-function-concat-end

.. sql-presto-function-concat-note-about-null-start

.. note:: The **CONCAT()** function will return **NULL** if the value of any field is **NULL**. Use the **COALESCE()** function to coalesce to a zero-length string prior to concatenation. For example, use:

   ::

      CONCAT(COALESCE(firstname, ""), " ", COALESE(lastname, ""))

   to concatenate a **FullName** field.

.. sql-presto-function-concat-note-about-null-end


.. _sql-presto-function-count:

COUNT()
--------------------------------------------------

.. sql-presto-function-count-start

Use the **COUNT(*)** function to return the number of input rows.

.. sql-presto-function-count-end


.. _sql-presto-function-count-example-customers-by-state:

Count customers by state
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-count-example-customers-by-state-start

The following example counts customers in the United States, and then also in California, Oregon, Washington, Alaska, and Hawaii who also belong to the loyalty program (which is indicated when ``loyalty_id`` is not **NULL**):

.. code-block:: sql
   :linenos:

   SELECT
     state
     ,COUNT(amperity_id) AS TotalCustomers
   FROM
     Customer360
   WHERE (UPPER("country") = 'US'
   AND UPPER("state") in ('AK', 'CA', 'HI', 'OR', 'WA')
   AND LOWER("loyalty_id") IS NOT NULL)
   GROUP BY state

.. sql-presto-function-count-example-customers-by-state-end


.. _sql-presto-function-current-date:

CURRENT_DATE
--------------------------------------------------

.. sql-presto-function-current-date-start

Use the **CURRENT_DATE** function to return the current date as of the start of the query. You may use an interval to offset the returned date by the value of the interval.

.. sql-presto-function-current-date-end


.. _sql-presto-function-current-date-example-birthdays-tomorrow:

Birthdays, tomorrow
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-current-date-example-birthdays-tomorrow-start

The following example returns all users who have a birthday tomorrow:

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     amperity_id
     ,email
     ,given_name
     ,birthdate
   FROM Customer360
   WHERE MONTH('birthdate') = MONTH(CURRENT_DATE + interval '1' day)
   AND DAY('birthdate') = DAY(CURRENT_DATE + interval '1' day)

.. sql-presto-function-current-date-example-birthdays-tomorrow-end


.. _sql-presto-function-current-timestamp:

CURRENT_TIMESTAMP
--------------------------------------------------

.. sql-presto-function-current-timestamp-start

Use the **CURRENT_TIMESTAMP** function to return the current timestamp for the time zone specified by the AT TIME ZONE operator:

.. code-block:: none

   CURRENT_TIMESTAMP AT TIME ZONE 'time/zone'+ interval '1' day

where ``time/zone`` is a valid `TZ database name <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__ |ext_link|, such as "America/Los_Angeles" or "America/New_York". 

.. sql-presto-function-current-timestamp-end

.. sql-presto-function-current-timestamp-important-start

.. important:: When the **Enable performance mode** option is enabled for queries, the **CURRENT_TIMESTAMP** function must be cast as a timestamp. For example:

   ::

      CAST(CURRENT_TIMESTAMP AS timestamp)

.. sql-presto-function-current-timestamp-important-end


.. _sql-presto-function-date-diff:

DATE_DIFF()
--------------------------------------------------

.. sql-presto-function-date-diff-start

Use the **DATE_DIFF(unit, timestamp1, timestamp2)** function as a way to return the difference between two columns that contain timestamp data, expressed in terms of an interval ``unit``.

Possible interval unit values:

* millisecond
* second
* minute
* hour
* day
* week
* month
* quarter
* year

.. sql-presto-function-date-diff-end


.. _sql-presto-function-date-diff-example-calculate-purchase-decay:

Calculate purchase day
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-date-diff-example-calculate-purchase-decay-start

.. code-block:: sql
   :linenos:

   SELECT
     ,t.amperity_id
     ,t.purchasedate
     ,firstpurchase.firstpurchasedate
     ,DATE_DIFF('day', firstpurchase.firstpurchasedate, t.purchasedate) AS PurchaseDecay
   FROM TransactionsEcomm t
   INNER JOIN
     (
     SELECT
       i.amperity_id
       ,MIN(i.purchasedate) AS firstpurchasedate
     FROM TransactionsEcomm i
     GROUP BY i.amperity_id
     LIMIT 1000
     ) firstpurchase
   ON t.amperity_id = firstpurchase.amperity_id
   LIMIT 1000

.. sql-presto-function-date-diff-example-calculate-purchase-decay-end


.. _sql-presto-function-date-format:

DATE_FORMAT()
--------------------------------------------------

.. sql-presto-function-date-format-start

Use the **DATE_FORMAT(timestamp, format)** function to format a ``timestamp`` as a string based on the ``format`` specifier.

===========   ===========================
Specifier     Description
===========   ===========================
%a            Abbreviated weekday name (Sun .. Sat)
%b            Abbreviated month name (Jan .. Dec)
%c            Month, numeric (1 .. 12); This specifier does not support 0 as a month or day.
%d            Day of the month, numeric (01 .. 31); This specifier does not support 0 as a month or day.
%e            Day of the month, numeric (1 .. 31); This specifier does not support 0 as a month or day.
%f            Fraction of second (6 digits for printing: 000000 .. 999000; 1 - 9 digits for parsing: 0 .. 999999999), truncated to milliseconds
%H            Hour (00 .. 23)
%h            Hour (01 .. 12)
%I            Hour (01 .. 12)
%i            Minutes, numeric (00 .. 59)
%j            Day of year (001 .. 366)
%k            Hour (0 .. 23)
%l            Hour (1 .. 12)
%M            Month name (January .. December)
%m            Month, numeric (01 .. 12); This specifier does not support 0 as a month or day.
%p            AM or PM
%r            Time, 12-hour (hh:mm:ss followed by AM or PM)
%S            Seconds (00 .. 59)
%s            Seconds (00 .. 59)
%T            Time, 24-hour (hh:mm:ss)
%v            Week (01 .. 53), where Monday is the first day of the week; used with %x
%W            Weekday name (Sunday .. Saturday)
%x            Year for the week, where Monday is the first day of the week, numeric, four digits; used with %v
%Y            Year, numeric, four digits
%y            Year, numeric (two digits); When parsing, two-digit year format assumes range 1970 to 2069, so "70" will result in year 1970 but "69" will produce 2069
%%            A literal % character
%x            x, for any x not listed above
===========   ===========================

.. sql-presto-function-date-format-end


.. _sql-presto-function-date-format-example-stitch-date:

Format as Stitch date
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-date-format-example-stitch-date-start

.. code-block:: sql

   ,DATE_FORMAT(CURRENT_DATE, '%Y-%m-%d 00:00:00') AS "amperity_stitch_date"

.. sql-presto-function-date-format-example-stitch-date-end


.. _sql-presto-function-date-trunc:

DATE_TRUNC()
--------------------------------------------------

.. sql-presto-function-date-trunc-start

Use the **DATE_TRUNC(unit, x)** function to return ``x`` truncated to one of the following ``unit`` values (shown in **bold**):

=========== ===========================
Unit        Example Truncated Value
=========== ===========================
**second**  2001-08-22 03:04:**05**.000
**minute**  2001-08-22 03:**04**:00.000
**hour**    2001-08-22 **03**:00:00.000
**day**     2001-08-**22** 00:00:00.000
**week**    2001-08-20 00:00:00.000
**month**   2001-**08**-01 00:00:00.000
**quarter** 2001-07-01 00:00:00.000
**year**    **2001**-01-01 00:00:00.000
=========== ===========================

.. sql-presto-function-date-trunc-end


.. _sql-presto-function-date-trunc-example-last-purchase-this-year:

Last purchase, this year
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-date-trunc-example-last-purchase-this-year-start

.. code-block:: sql

   WHERE DATE_TRUNC('year', LastPurchase) = DATE_TRUNC('year', Now())

.. sql-presto-function-date-trunc-example-last-purchase-this-year-end


.. _sql-presto-function-day-month-year:

DAY(), MONTH(), YEAR()
--------------------------------------------------

.. sql-presto-function-day-month-year-start

Identifying the day, month, and year from within a date can be helpful when building segments that use these values to improve the timing of communication:

* Use **DAY()** to return the day of the month from a date or timestamp.
* Use **MONTH()** to return the month of the year from a date or timestamp.
* Use **YEAR()** to return the year from a date or timestamp.

.. tip:: Functions also exist for **HOUR()**, **MINUTE()**, **QUARTER()**, and **WEEK()**. These functions are used in the same manner as **DAY()**, **MONTH()**, and **YEAR()**, but against different elements within a date or timestamp column value.

.. sql-presto-function-day-month-year-end


.. _sql-presto-function-day-month-year-example-one-and-dones-by-year:

One and dones, by year
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-day-month-year-example-find-guests-who-canceled-start

The following example shows using a common table expression to identify all one-and-done purchasers for a single calendar year:

.. code-block:: sql
   :linenos:

   WITH one_and_dones_2022 AS (
     SELECT
       amperity_id
     FROM Transaction_Attributes
     WHERE one_and_done AND YEAR(first_order_datetime) = 2022
   )

   SELECT
     COUNT(*) one_and_dones_2022
   FROM
     one_and_dones_2022

.. sql-presto-function-day-month-year-example-find-guests-who-canceled-end


.. _sql-presto-function-day-month-year-example-find-guests-who-canceled:

Find guests who canceled last month
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-day-month-year-example-find-guests-who-canceled-start

The following example uses member, consumer, and confirmation IDs, along with the reservation confirmation number and the checkin date to return all customers who canceled their stay one month ago:

.. code-block:: sql
   :linenos:

   SELECT
     g.amperity_id AS AMPERITY_ID
     ,g.member_id AS MEMBER_ID
     ,g.consumer_id AS CONSUMER_ID
     ,r.confirmation_id AS CONFIRMATION_ID
     ,r.booking_id AS CONFIRMATION_NUMBER
     ,r.stay_start AS CHECKIN_DATE
   FROM Reservation_Table r
   JOIN Guest_Table g ON r.amperity_id = g.amperity_id
   WHERE (
     r.stay_status = 'canceled'
     AND DAY(r.stay_start) = DAY(CURRENT_TIMESTAMP + INTERVAL '1' MONTH)
   )

.. sql-presto-function-day-month-year-example-find-guests-who-canceled-end


.. _sql-presto-function-day-month-year-example-find-birthdays-tomorrow:

Find tomorrow's birthdays
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-day-month-year-example-find-birthdays-tomorrow-start

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,email
     ,given_name
     ,birthdate
   FROM "Customer360"
   WHERE
     MONTH(birthdate) = MONTH(CURRENT_TIMESTAMP AT TIME ZONE 'America/Los_Angeles'+ INTERVAL '1' DAY)
   AND
     DAY(birthdate) = DAY(CURRENT_TIMESTAMP AT TIME ZONE 'America/Los_Angeles' + INTERVAL '1' DAY)

.. sql-presto-function-day-month-year-example-find-birthdays-tomorrow-end


.. _sql-presto-function-dense-rank:

DENSE_RANK()
--------------------------------------------------

.. sql-presto-function-dense-rank-start

Use the **DENSE_RANK()** function to compute the rank of a value in a group of values. **DENSE_RANK()** will assign the same rank to rows with the same value and will not create gaps in the ranked sequence.

.. note:: The **DENSE_RANK()** and **RANK()** functions both assign a rank to rows with the same value. The difference is that **RANK()** will create gaps in the sequence. The following example shows rows that are ranked in ascending order by column B:

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

.. sql-presto-function-dense-rank-end


.. _sql-presto-function-from-unixtime:

FROM_UNIXTIME()
--------------------------------------------------

.. sql-presto-function-from-unixtime-start

Use the **FROM_UNIXTIME(unixtime)** function to return ``unixtime`` (a UNIX timestamp) as a timestamp.

* Use **FROM_UNIXTIME(unixtime, string)** to return ``unixtime`` as a timestamp and ``string`` as a timezone.
* Use **FROM_UNIXTIME(unixtime, hours, minutes)** to return ``unixtime`` as a timestamp and ``hours`` and ``minutes`` as a timezone offset.

.. sql-presto-function-from-unixtime-end


.. _sql-presto-function-from-unixtime-example-convert-updated-to-date:

Convert _updated to a date
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feeds-set-last-updated-field-start
   :end-before: .. feeds-set-last-updated-field-end

.. sql-presto-function-from-unixtime-example-convert-updated-to-date-start

Use the **FROM_UNIXTIME(unixtime)** function to convert the values in the last updated column (``_updated``) into a date format.

.. code-block:: sql

   CAST(FROM_UNIXTIME(_updated / 1048576000) AS date) AS "Date"

.. sql-presto-function-from-unixtime-example-convert-updated-to-date-end


.. _sql-presto-function-greatest:

GREATEST()
--------------------------------------------------

.. sql-presto-function-greatest-start

Use the **GREATEST(column_name, column_name)** function to return the column with the greatest value among the values of all named columns.

.. sql-presto-function-greatest-end


.. _sql-presto-function-if:

IF()
--------------------------------------------------

.. sql-presto-function-if-start

Use the **IF(condition,x)** function to evaluate and return true, NULL, or false.

* Use **IF(condition,true_value)** to evaluate and return ``true_value`` when the ``condition`` is ``true``, otherwise return NULL.
* Use **IF(condition,true_value, false_value)** to return ``true_value`` when the ``condition`` is ``true`` or return ``false_value`` when the ``condition`` is ``false``.

.. sql-presto-function-if-end


.. _sql-presto-function-least:

LEAST()
--------------------------------------------------

.. sql-presto-function-least-start

Use the **LEAST(column_name, column_name)** function to return the column with the lowest value among the values of all named columns.

.. sql-presto-function-least-end


.. _sql-presto-function-least-example-find-earliest-dates:

Find earliest dates
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-least-example-find-earliest-dates-start

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,email
     ,given_name
     ,birthdate
   FROM "Customer360"
   WHERE
     LEAST(date_col1, date_col2, date_col3, date_col4)

.. sql-presto-function-least-example-find-earliest-dates-end


.. _sql-presto-function-length:

LENGTH()
--------------------------------------------------

.. sql-presto-function-length-start

Use the **LENGTH(string)** function to return the length of ``string`` in characters.

.. sql-presto-function-length-end


.. _sql-presto-function-lower:

LOWER()
--------------------------------------------------

.. sql-presto-function-lower-start

Use the **LOWER(string)** function to convert ``string`` to lowercase.

.. sql-presto-function-lower-end


.. _sql-presto-function-max:

MAX()
--------------------------------------------------

.. sql-presto-function-max-start

Use the **MAX()** function to return the maximum value of all input values.

.. sql-presto-function-max-end


.. _sql-presto-function-max-example-collapse-rows-by-amperity-id:

Collapse rows by Amperity ID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-max-example-collapse-rows-by-amperity-id-start

The following SQL will collapse all rows with Amperity IDs in the **Unified Coalesced** table into a single row per Amperity ID:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS amperity_id
     ,MAX(given_name) AS given_name
     ,MAX(surname) AS surname
     ,MAX(email) AS email
     ,MAX(phone) AS phone
     ,MAX(address) AS address
     ,MAX(city) AS city
     ,MAX(state) AS state
     ,MAX(postal) AS postal
     ,MAX(birthdate) AS birthdate
     ,MAX(gender) AS gender
   FROM Unified_Coalesced
   GROUP BY amperity_id

.. sql-presto-function-max-example-collapse-rows-by-amperity-id-end


.. _sql-presto-function-median:

MEDIAN()
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-median-start

.. warning:: The **MEDIAN()** function is not supported within Amperity. Use :ref:`NTILE() <sql-presto-function-ntile>` of 2 over the value, **GROUP BY** over the **NTILE()**, and then take the **MAX()** of the first value or the **MIN()** of the second value.

.. sql-presto-function-median-end


.. _sql-presto-function-min:

MIN()
--------------------------------------------------

.. sql-presto-function-min-start

Use the **MIN()** function to return the minimum value of all input values.

.. sql-presto-function-min-end


.. _sql-presto-function-min-example-replace-null-with-zero:

Replace NULL with 0
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-min-example-replace-null-with-zero-start

Wrap the **MIN()** function to replace **NULL** values with ``0``:

.. code-block:: sql
   :linenos:

   MIN(CASE 
     WHEN field IS NULL THEN 0
     ELSE field
   END)

or:

.. code-block:: sql

   MIN(COALESCE(field,0))

.. sql-presto-function-min-example-replace-null-with-zero-end


.. _sql-presto-function-now:

NOW()
--------------------------------------------------

.. sql-presto-function-now-start

Use the **NOW()** function to return the current timestamp (with time zone) as of the start of the query. This function is an alias for ``current_timestamp``.

.. sql-presto-function-now-end


.. _sql-presto-function-ntile:

NTILE()
--------------------------------------------------

.. sql-presto-function-ntile-start

Use the **NTILE(n)** window function to evenly distribute large numbers of rows across ``n`` buckets, ranging from 1 to n.

.. important:: Results can be unpredictable when the number of returned records is less than the ``(n)`` value of **NTILE()**.

.. tip:: Use the **PERCENT_RANK()** function when the expected number of returned rows is a small number.

.. sql-presto-function-ntile-end


.. _sql-presto-function-ntile-example-partition-pclv-by-brand:

Partition predicted CLV by brand
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-ntile-example-partition-pclv-by-brand-start

The following example shows how to separate values into brand tiers using predicted customer lifetime value.

.. code-block:: sql

   NTILE(100) OVER (PARTITION BY brand ORDER BY predicted_clv desc, _uuid_pk)

.. sql-presto-function-ntile-example-partition-pclv-by-brand-end


.. _sql-presto-function-ntile-example-percentiles:

Percentiles by 10
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-ntile-example-percentiles-start

The following example shows how to return 10th percentiles.

.. code-block:: sql
   :linenos:

   SELECT 
     tier*.1 AS tier
     ,MIN(lifetime_order_revenue) lifetime_revenue_amount
   FROM (
     SELECT
       amperity_id
       ,lifetime_order_revenue
       ,NTILE(10) OVER (ORDER BY lifetime_order_revenue) tier
     FROM Transaction_Attributes
   )
   GROUP BY 1
   ORDER BY 1

.. sql-presto-function-ntile-example-percentiles-end


.. _sql-presto-function-ntile-example-percentiles-25-median-75:

Percentiles by 4
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-ntile-example-percentiles-start

The following example shows how to return the 25th, median, and 75th percentiles.

.. code-block:: sql
   :linenos:

   SELECT 
     tier*.25 tier
     ,MIN(lifetime_order_revenue) lifetime_revenue_amount
   FROM (
     SELECT DISTINCT
       amperity_id
       ,lifetime_order_revenue
       ,NTILE(4) OVER (ORDER BY lifetime_order_revenue) tier
     FROM Transaction_Attributes
   )
   GROUP BY 1
   ORDER BY 1

.. sql-presto-function-ntile-example-percentiles-end


.. _sql-presto-function-nullif:

NULLIF()
--------------------------------------------------

.. sql-presto-function-nullif-start

Use the **NULLIF(expression1, expression2)** function to return **NULL** if ``expression1`` is equal to ``expression2``.

.. sql-presto-function-nullif-end


.. _sql-presto-function-percent-rank:

PERCENT_RANK()
--------------------------------------------------

.. sql-presto-function-percent-rank-start

Use the **PERCENT_RANK()** function to return the percentage ranking of a value in group of values. The result is ``(r - 1) / (n - 1)`` where ``r`` is the rank of the row and ``n`` is the total number of rows in the window partition.

.. sql-presto-function-percent-rank-end


.. _sql-presto-function-percent-rank-example-percent-rank-of-all-purchases:

Percent rank of all purchases
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-percent-rank-example-percent-rank-of-all-purchases-start

The following example shows how to return the percent rank of all purchases.

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     amperity_id
     ,order_revenue
     ,PERCENT_RANK() OVER (ORDER BY order_revenue) pct_rank
   FROM Unified_Transactions
   WHERE order_datetime > DATE('2023-03-01') AND amperity_id IS NOT NULL
   ORDER BY pct_rank DESC

.. sql-presto-function-percent-rank-example-percent-rank-of-all-purchases-end


.. _sql-presto-function-percentile:

PERCENTILE()
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-percentile-start

.. warning:: The **PERCENTILE()** function is not supported within Amperity.

.. sql-presto-function-percentile-end


.. _sql-presto-function-rank:

RANK()
--------------------------------------------------

.. sql-presto-function-rank-start

Use the **RANK()** function to return the rank of a value within a group of values. The rank is one plus the number of rows preceding the row that is not a peer to the ranked row. Tie values in the ordering will produce gaps in the sequence. The ranking is performed for each window partition.

.. sql-presto-function-rank-end


.. _sql-presto-function-rank-example-rank-by-amperity-id:

Rank by Amperity ID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-rank-example-rank-by-amperity-id-start

The following SQL query uses the **RANK()** function to find the largest transactions by Amperity ID, and then returns them in ascending order:

.. code-block:: sql
   :linenos:
   :emphasize-lines: 6,9,12

   WITH ranked_transactions AS (
   SELECT
     t.orderid
     ,t.amperity_id
     ,t.transactiontotal
     ,RANK() OVER (PARTITION BY t.amperity_id ORDER BY t.transactiontotal DESC) AS rank
   FROM
     TransactionsEcomm t
   ORDER BY t.amperity_id, rank ASC
   LIMIT 100
   )
   SELECT * FROM ranked_transactions WHERE rank = 1

.. sql-presto-function-rank-example-rank-by-amperity-id-end


.. _sql-presto-function-regexp-extract:

REGEXP_EXTRACT()
--------------------------------------------------

.. sql-presto-function-regexp-extract-start

Use the **REGEXP_EXTRACT(string, pattern)** function to replace every instance of the substring matched by the ``regex`` pattern from ``string``.

.. sql-presto-function-regexp-extract-end


.. _sql-presto-function-regexp-like:

REGEXP_LIKE()
--------------------------------------------------

.. sql-presto-function-regexp-like-start

Use the **REGEXP_LIKE(string, 'expression')** function to return true when ``string`` matches ``expression``.

.. sql-presto-function-regexp-like-end


.. _sql-presto-function-regexp-like-example-validate-email:

Validate email addresses
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-like-example-validate-email-start

The following example shows using the **REGEXP_LIKE()** function within a **CASE** statement to return valid email addresses:

.. code-block:: sql
   :linenos:

   CASE
     WHEN REGEXP_LIKE(email, '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')
     AND email_completion > 0 THEN true
     ELSE false
   END AS contactable_email

.. sql-presto-function-regexp-like-example-validate-email-end


.. _sql-presto-function-regexp-like-example-validate-phone:

Validate phone numbers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-like-example-validate-phone-start

The following example shows using the **REGEXP_LIKE()** function within a **CASE** statement to return valid phone numbers:

.. code-block:: sql
   :linenos:

   CASE
     WHEN REGEXP_LIKE(phone, '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
     AND phone_completion > 0 THEN true
     ELSE false
   END AS contactable_phone

.. sql-presto-function-regexp-like-example-validate-phone-end


.. _sql-presto-function-regexp-replace:

REGEXP_REPLACE()
--------------------------------------------------

.. sql-presto-function-regexp-replace-start

Use the **REGEXP_REPLACE(string, regex)** function to remove every instance of the substring matched by the ``regex`` pattern from ``string``.

Use the **REGEXP_REPLACE(string, regex, replace)** function to replace every instance of the substring.

.. sql-presto-function-regexp-replace-end


.. _sql-presto-function-regexp-replace-example-remove-whitespace:

Remove whitespace
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-remove-whitespace-start

.. code-block:: sql

   NULLIF(REGEXP_REPLACE(field, '^\\s*(\\S.*\\S)\\s*$', '\\1'), '')

.. sql-presto-function-regexp-replace-example-remove-whitespace-end


.. _sql-presto-function-regexp-replace-example-remove-spaces:

Remove spaces
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-remove-spaces-start

.. code-block:: sql
   :linenos:

   SELECT
     REGEXP_REPLACE(AddressLine1, '(\s*)([ ])', '')
     ,AddressLine1
   FROM Customer360
   LIMIT 100

.. sql-presto-function-regexp-replace-example-remove-spaces-end


.. _sql-presto-function-regexp-replace-example-keep-az09-from-string:

Keep A-z, 0-9 from string
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-keep-az09-from-string-start

.. code-block:: sql
   :linenos:

   SELECT
     REGEXP_REPLACE(AddressLine1, '(\s*)([^a-zA-Z0-9])', '')
     ,AddressLine1
   FROM Customer360
   LIMIT 100

.. sql-presto-function-regexp-replace-example-keep-az09-from-string-end


.. _sql-presto-function-regexp-replace-example-keep-alphabetical-characters:

Keep alphabetical characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-keep-alphabetical-characters-start

.. code-block:: sql
   :linenos:

   ,REGEXP_REPLACE(LOWER(given_name), '[^a-zA-Z]+', '') AS given_name
   ,REGEXP_REPLACE(LOWER(surname), '[^a-zA-Z]+', '') AS surname
   ,REGEXP_REPLACE(LOWER(full_name), '[^a-zA-Z ]+', '') AS full_name

.. sql-presto-function-regexp-replace-example-keep-alphabetical-characters-end


.. _sql-presto-function-regexp-replace-example-replace-characters-after-symbol:

Replace characters after + symbol
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-replace-characters-after-symbol-start

.. code-block:: sql

   ,REGEXP_REPLACE(LOWER(email), '\+(.*?)\@', '@') AS email

.. sql-presto-function-regexp-replace-example-replace-characters-after-symbol-end


.. _sql-presto-function-regexp-replace-example-keep-characters-before-symbol:

Keep characters before @ symbol
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-keep-characters-before-symbol-start

.. code-block:: sql

   ,SPLIT(REGEXP_REPLACE(LOWER(email), '\+(.*?)\@', '@'), '@')[1] AS email_username

.. sql-presto-function-regexp-replace-example-keep-characters-before-symbol-end


.. _sql-presto-function-regexp-replace-example-keep-characters-after-symbol:

Keep characters after @ symbol
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-keep-characters-after-symbol-start

.. code-block:: sql

   ,REPLACE(LOWER(email), SPLIT(REGEXP_REPLACE(LOWER(email), '\+(.*?)\@', '@'), '@')[1], '') AS email_domain

.. sql-presto-function-regexp-replace-example-keep-characters-after-symbol-end


.. _sql-presto-function-regexp-replace-example-clean-up-semantic-values:

Clean up semantic values
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-clean-up-semantic-values-start

.. code-block:: sql
   :linenos:

   ,REGEXP_REPLACE(LOWER(phone), '[^0-9]+', '') AS phone
   ,REGEXP_REPLACE(LOWER(address), '[.]+', '') AS address
   ,REGEXP_REPLACE(LOWER(address2), '[.]+', '') AS address2
   ,REGEXP_REPLACE(LOWER(city), '[^a-zA-Z]+', '') AS city
   ,REGEXP_REPLACE(LOWER(state), '[^a-zA-Z]+', '') AS state

.. sql-presto-function-regexp-replace-example-clean-up-semantic-values-end


.. _sql-presto-function-regexp-replace-example-formatting-for-facebook-ads:

Formatting for Facebook Ads
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-formatting-for-facebook-ads-start

.. note:: Facebook Ads has specific requirements for data formatting and naming of certain fields. Destinations and campaigns configured for Facebook Ads automatically apply the correct formatting to fields that are required by Facebook Ads. This example shows the regular expression formatting for those fields.

.. TODO: The following block should not be in a code-block.

::

   ,REGEXP_REPLACE(LOWER(given_name), '[.,\/#!$%\^&\*;:{}=\-_`~()@'\"+ ]', '') AS FN
   ,REGEXP_REPLACE(LOWER(surname), '[.,\/#!$%\^&\*;:{}=\-_`~()@'\"+ ]', '') AS LN
   ,REGEXP_REPLACE(LOWER(city), '[^a-z]', '') AS CT
   ,REGEXP_REPLACE(LOWER(state), '[^a-z]', '') AS ST
   ,REGEXP_REPLACE(LOWER(postal), ' " "', '') AS ZIP
   ,REGEXP_REPLACE(LOWER(email), '[^a-z]', '') AS EMAIL

.. sql-presto-function-regexp-replace-example-formatting-for-facebook-ads-end


.. _sql-presto-function-regexp-replace-example-capitalize-first-letter:

Capitalize the first character
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-regexp-replace-example-capitalize-first-letter-start

Presto SQL does not have a function that is equivalent to the **INITCAP** function in Spark SQL. To format the first character in a string as uppercase and the rest of the string as lowercase, use the **REGEXP_REPLACE()** function.

For example:

.. code-block:: sql

   REGEXP_REPLACE('new york', '(\p{L})(\p{L}*)', x -> UPPER(x[1]) || LOWER(x[2]))

.. note:: The ``\p{L}`` matches any character in any language, such as with accent characters found in non-English languages.

.. sql-presto-function-regexp-replace-example-capitalize-first-letter-end


.. _sql-presto-function-replace:

REPLACE()
--------------------------------------------------

.. sql-presto-function-replace-start

Use the **REPLACE()** function to remove and/or replace all instances of ``search`` from ``string``. There are two variants:

* Use **REPLACE(string, search)** to remove all instances of ``search`` from ``string``, i.e. "replace string with nothing".
* Use **REPLACE(string, search, replace)** to replace all instances of ``search`` from ``string`` with ``replace``.

.. sql-presto-function-replace-end


.. _sql-presto-function-round:

ROUND()
--------------------------------------------------

.. sql-presto-function-round-start

Use the **ROUND(x)** function to return ``x`` rounded to the nearest integer.

.. sql-presto-function-round-end


.. _sql-presto-function-split:

SPLIT()
--------------------------------------------------

.. sql-presto-function-split-start

Use the **SPLIT(string, regex, limit)** function to split a ``string`` at occurrences that match ``regex``, and then return the results. Add a positive integer to **LIMIT** the number of occurrences to that integer.

.. note:: In Presto SQL, the index starts at 1.

.. sql-presto-function-split-end


.. _sql-presto-function-split-example-return-username-from-email:

Return username from email
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-split-example-return-username-from-email-start

To return only the username from an email address (the characters before the @ symbol):

.. code-block:: sql

   SPLIT(REGEXP_REPLACE(LOWER(email), '[.]+', ''), '@')[1] AS email_username

.. sql-presto-function-split-example-return-username-from-email-end


.. _sql-presto-function-split-part:

SPLIT_PART()
--------------------------------------------------

.. sql-presto-function-split-part-start

Use the **SPLIT_PART(string, delimiter, index)** function to split a ``string`` at occurrences that match ``index``, and then return the results. If the index is larger than the number of available characters, or if the specified index position is out of range, the function will return **NULL**.

.. note:: In Presto SQL, the index starts at 1.

For example:

.. code-block:: sql

   TRIM(SPLIT_PART(GIFTCARDCODE, '-', 1))

.. sql-presto-function-split-part-end

.. sql-presto-function-split-part-example-index-position-compare-to-spark-start

.. tip:: Use the ``SPLIT()`` function in Spark SQL. For example:

   .. code-block:: sql

      SPLIT(GIFTCARDCODE,'-')[0]

   In Spark SQL, the index starts at 0.

.. sql-presto-function-split-part-example-index-position-compare-to-spark-end


.. _sql-presto-function-substr:

SUBSTR()
--------------------------------------------------

.. sql-presto-function-substr-start

Use the **SUBSTR()** function to return N characters in a string. There are two variants:

* Use **SUBSTR(string, start)** to return ``string`` from the ``start`` position that is equal to the value of ``start``. A positive starting position (``1``) is relative to the start of ``string``; a negative starting position (``-1``) is relative to the end of ``string``.
* Use **SUBSTR(string, start, length)** to return ``string`` from the ``start`` position that contains the number of characters specified by ``length``. A positive starting position (``1``) is relative to the start of ``string``; a negative starting position (``-1``) is relative to the end of ``string``.

.. sql-presto-function-substr-end


.. _sql-presto-function-substr-example-return-two-characters:

Return two characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-substr-example-return-two-characters-start

To return the last two characters of ``column_name``, use either of:

.. code-block:: sql

   SUBSTR(column_name, -2)

or

.. code-block:: sql

   SUBSTR(column_name, -1, 2)

.. sql-presto-function-substr-example-return-two-characters-end


.. _sql-presto-function-sum:

SUM()
--------------------------------------------------

.. sql-presto-function-sum-start

Use the **SUM(x)** function to return the sum of all input values.

.. sql-presto-function-sum-end

.. sql-presto-function-sum-note-about-null-start

.. note:: The **SUM()** function will return **NULL** if the value of any field is **NULL**. In some situations you must use the **COALESCE()** function to coalesce to a zero-length string prior to concatenation. For example:

   ::

      SUM(COALESCE(lifetimeValue,0))

.. sql-presto-function-sum-note-about-null-end


.. _sql-presto-function-sum-example-invoices-as-total-amount:

Sum invoices as total amount
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-sum-example-invoices-as-total-amount-start

.. code-block:: sql

   ,SUM(orders.invoice_amount) AS total_amount

.. sql-presto-function-sum-example-invoices-as-total-amount-end


.. _sql-presto-function-sum-example-revenue-descending-order:

Total revenue, descending order
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-sum-example-revenue-descending-order-start

The following example uses the **SUM()** function to return total revenue, returns, and quantity, groups them, and then arranges the results in descending order:

.. code-block:: sql
   :linenos:

   SELECT
     purchase_brand
     ,SUM(order_revenue) AS total_revenue
     ,SUM(order_returned_revenue) AS total_returns
     ,SUM(order_quantity) AS total_quantity
   FROM Unified_Transactions
   GROUP BY 1
   ORDER BY 1 DESC

.. sql-presto-function-sum-example-revenue-descending-order-end


.. _sql-presto-function-to-hex:

TO_HEX()
--------------------------------------------------

.. sql-presto-function-to-hex-start

Use the **TO_HEX(binary)** function to encode ``binary`` into a hex string representation.

.. sql-presto-function-to-hex-end


.. _sql-presto-function-to-hex-example-one-way-hash:

One-way SHA-256 hash
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sql-presto-function-to-hex-example-one-way-hash-start

The following example applies a one-way SHA-256 hash to email addresses:

.. code-block:: sql

   TO_HEX(SHA256(TO_UTF8(UPPER(TRIM(email)))))

.. sql-presto-function-to-hex-example-one-way-hash-end


.. _sql-presto-function-to-unixtime:

TO_UNIXTIME()
--------------------------------------------------

.. sql-presto-function-to-unixtime-start

Use the **TO_UNIXTIME(timestamp)** function to return ``timestamp`` as a UNIX timestamp.

.. sql-presto-function-to-unixtime-end


.. _sql-presto-function-trim:

TRIM()
--------------------------------------------------

.. sql-presto-function-trim-start

Use the **TRIM(string)** function to remove leading and trailing whitespace from ``string``.

.. tip:: To remove only leading whitespace use the **LTRIM(string)** function instead of **TRIM(string)**.

   To remove only trailing whitespace use the **RTRIM(string)** function instead of **TRIM(string)**.

.. sql-presto-function-trim-end


.. _sql-presto-function-try-cast:

TRY_CAST()
--------------------------------------------------

.. sql-presto-function-try-cast-start

Use the **TRY_CAST(value AS type)** function to cast a ``value`` as a ``type``, and then return **NULL** if the cast fails.

.. sql-presto-function-try-cast-end


.. _sql-presto-function-upper:

UPPER()
--------------------------------------------------

.. sql-presto-function-upper-start

Use the **UPPER(string)** function to convert ``string`` to uppercase.

.. sql-presto-function-upper-end
