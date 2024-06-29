.. databases-validation-alerts-start

The SQL editor shows a validation alert when syntax is detected in your query that has the potential to cause performance issues with database generation, the length of time it may take to complete running a query, or situations where you can improve the quality of your SQL syntax.

.. admonition:: What should I do if my query has a validation alert?

   A validation alert does not mean your SQL is invalid. If your query has a validation alert, review the alert, review your SQL, and consider alternates that can help you avoid potential performance issues or avoid the situation the alert describes. There are situations where the SQL you need is the SQL that is causing the validation warning. You may activate a query even when it contains a validation alert.


**Implicit CROSS JOIN**

.. databases-validation-alert-implicit-cross-join-start




An implicit ``CROSS JOIN`` occurs when a query unintentionally returns a Cartesian product. A Cartesian product combines every item in the first table with every item in the second. For example, if table A has three items and table B has three items, the Cartesian product is 9 pairs.

A Cartesian product in Amperity between any two tables is often a very, very large number of pairs and, as a result, is an expensive operation. It is recommended to optimize your Spark SQL queries to avoid an implicit ``CROSS JOIN``.

The database editor will show a validation alert for an implicit ``CROSS JOIN`` in situations like:

#. A join statement does not use an ``ON()`` or ``USING()`` clause to specify one (or more) column names as the join criteria.

#. A ``SELECT`` statement returns too many columns from two tables. For example, using ``SELECT * FROM Table_A, Table_B`` can behave like a ``CROSS JOIN``. In this situation you should first filter out ``NULL`` values to avoid performance issues, or refactor your query to be more specific about which columns from which tables are to be joined.

.. databases-validation-alert-implicit-cross-join-end


**OVER without PARTITION BY**


.. databases-validation-alert-over-without-partition-by-start

.. TODO: Single-source this as a "caution" or something in the sql-spark-with-clause section of the Spark SQL reference.

A window function with an ``OVER`` statement that does not include a ``PARTITION BY`` clause often leads to performance issues when the ``OVER`` statement is asked to run across a large number of rows.

If you see this alert, add the ``PARTITION BY`` clause to your window function.

.. databases-validation-alert-over-without-partition-by-end


**Unescaped backslashes in regular expressions**

.. databases-validation-alert-unescaped-backslashes-start

Unescaped backslashes can cause errors with functions that use regular expressions, such as ``RLIKE()``, that are difficult to diagnose.

.. databases-validation-alert-unescaped-backslashes-end

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-rlike-caution-start
   :end-before: .. sql-spark-function-rlike-caution-end


**Unintentional broadcast joins**

.. databases-validation-alert-unintentional-broadcast-joins-start

A broadcast join sends the smaller table in a join operation to all Spark executors, and then evaluates the larger table across each executor's partitions. When a broadcast join is small, it's fast. Above a certain threshold they can performance issues.

A broadcast join often looks like:

::

   WHERE column_name NOT IN values

When ``values`` is not a small list of constants a broadcast join may occur.

.. TODO: Sync this note with sql-spark-left-join-clause, and then single-source it.


.. note:: In some situations you may want to use a ``LEFT ANTI JOIN``, which returns values from the left-side table when they do not have matches on the right-side table. Use a ``LEFT ANTI JOIN`` to avoid performance issues that may be caused by a broadcast join.

.. databases-validation-alert-unintentional-broadcast-joins-end
