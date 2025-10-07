**Query performance mode (CTAS)**

.. queries-enable-performance-mode-start

You may enable performance mode for any query that returns large result sets. Performance mode wraps a ``CREATE TABLE`` operation around the ``SELECT`` statement in the query, writes the results to an Apache Parquet file, and then makes that file available to Amperity as a table.

.. queries-enable-performance-mode-end

.. queries-enable-performance-mode-important-start

Performance mode is faster than running a query in non-performance mode, but has the following limitations:

* Sort order is not guaranteed because results are written in parallel to many files.
* The ``UNION`` clause requires data types to match exactly.
* Column names cannot contain spaces.
* Column names are output in lowercase.
* Small queries may take longer.

.. queries-enable-performance--mode-important-end