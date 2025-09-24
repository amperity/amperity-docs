.. https://docs.amperity.com/reference/

:orphan:

.. meta::
    :description lang=en:
        What data types can be in structured data?

.. meta::
    :content class=swiftype name=body data-type=text:
        What data types can be in structured data?


.. meta::
    :content class=swiftype name=title data-type=string:
        About data types

==================================================
About data types
==================================================

.. data-types-amperity-start

Amperity supports the following data types when structured data is made available to Amperity. Complex types--arrays, maps, and structs--must be converted to individual fields prior to making them available to the Stitch process.

.. data-types-amperity-end


.. _data-types-amperity-array:

Array
==================================================

.. data-types-amperity-array-start

A composite fully-structred data type that stores a sequence of elements where each element is a set of fields and values.

.. important:: Amperity will load a data source with an array to a domain table.

   For data sources with an array, you must use a custom domain table to convert all elements in the array to individual fields in the table output.

   After all elements are converted to individual fields in the custom domain table output you assign semantic tags and keys to individual fields in the table.

   An array may be used as part of a common table expression (CTE) in Spark SQL and Presto SQL as long as output of the query does not have a field with an array data type.

.. admonition:: Compare to

   **Databricks:** `ARRAY <https://docs.databricks.com/aws/en/sql/language-manual/data-types/array-type>`__ |ext_link|

   **Google BigQuery:** `ARRAY <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_type>`__ |ext_link|

   **Snowflake:** `ARRAY <https://docs.snowflake.com/en/sql-reference/data-types-structured#specifying-a-structured-array-type>`__ |ext_link|

.. data-types-amperity-array-end


.. _data-types-amperity-boolean:

Boolean
==================================================

.. data-types-amperity-boolean-start

A value that is **TRUE**, **FALSE**, or **NULL**.

.. admonition:: Compare to

   **Databricks:** `BOOLEAN <https://docs.databricks.com/aws/en/sql/language-manual/data-types/boolean-type>`__ |ext_link|

   **Google BigQuery:** `BOOLEAN <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#boolean_type>`__ |ext_link|

   **Snowflake:** `BOOLEAN <https://docs.snowflake.com/en/sql-reference/data-types-logical#boolean>`__ |ext_link|

.. data-types-amperity-boolean-end


.. _data-types-amperity-date:

Date
==================================================

.. data-types-amperity-date-start

An ISO-8601 compliant date value.

.. admonition:: Compare to

   **Databricks:** `DATE <https://docs.databricks.com/aws/en/sql/language-manual/data-types/date-type>`__ |ext_link|

   **Google BigQuery:** `DATE <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#date_type>`__ |ext_link|

   **Snowflake:** `DATE <https://docs.snowflake.com/en/sql-reference/data-types-datetime#label-datatypes-date>`__ |ext_link|

.. data-types-amperity-date-end


.. _data-types-amperity-datetime:

Datetime
==================================================

.. data-types-amperity-datetime-start

An ISO-8601 compliant date and time value.

.. admonition:: Compare to

   **Databricks:** `INTERVAL <https://docs.databricks.com/aws/en/sql/language-manual/data-types/interval-type>`__ |ext_link| and `TIMESTAMP <https://docs.databricks.com/aws/en/sql/language-manual/data-types/timestamp-type>`__ |ext_link|

   **Google BigQuery:** `DATETIME <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#datetime_type>`__ |ext_link|, `TIME <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#time_type>`__ |ext_link|, and `TIMESTAMP <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type>`__ |ext_link|

   **Snowflake:** `DATETIME <https://docs.snowflake.com/en/sql-reference/data-types-datetime#datetime>`__ |ext_link|, `TIME <https://docs.snowflake.com/en/sql-reference/data-types-datetime#time>`__ |ext_link|, `TIMESTAMP <https://docs.snowflake.com/en/sql-reference/data-types-datetime#label-datatypes-timestamp-variations>`__ |ext_link|, `TIMESTAMP_LTZ <https://docs.snowflake.com/en/sql-reference/data-types-datetime#timestamp-ltz-timestamp-ntz-timestamp-tz>`__ |ext_link|, `TIMESTAMP_NTZ <https://docs.snowflake.com/en/sql-reference/data-types-datetime#timestamp-ltz-timestamp-ntz-timestamp-tz>`__ |ext_link|, and `TIMESTAMP_TZ <https://docs.snowflake.com/en/sql-reference/data-types-datetime#timestamp-ltz-timestamp-ntz-timestamp-tz>`__ |ext_link|

.. data-types-amperity-datetime-end


.. _data-types-amperity-decimal:

Decimal
==================================================

.. data-types-amperity-decimal-start

A fixed point number with a configurable number of characters before and after a decimal point.

.. admonition:: Compare to

   **Databricks:** `DECIMAL (p,s) <https://docs.databricks.com/aws/en/sql/language-manual/data-types/decimal-type>`__ |ext_link|

   **Google BigQuery:** `BIGNUMERIC <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|, `DECIMAL (p,s) <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|, and `NUMERIC (p,s) <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

   **Snowflake:** `NUMBER (p,s) <https://docs.snowflake.com/en/sql-reference/data-types-numeric#number>`__ |ext_link|

.. data-types-amperity-decimal-end


.. _data-types-amperity-float:

Float
==================================================

.. data-types-amperity-float-start

A floating point number with a configurable number of characters before and after a decimal point.

.. admonition:: Compare to

   **Databricks:** `DOUBLE <https://docs.databricks.com/aws/en/sql/language-manual/data-types/double-type>`__ |ext_link|, and `FLOAT <https://docs.databricks.com/aws/en/sql/language-manual/data-types/float-type>`__ |ext_link|

   **Google BigQuery:** `FLOAT64 <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

   **Snowflake:** `DOUBLE <https://docs.snowflake.com/en/sql-reference/data-types-numeric#double-double-precision-real>`__ |ext_link| and `FLOAT <https://docs.snowflake.com/en/sql-reference/data-types-numeric#float-float4-float8>`__ |ext_link|

.. data-types-amperity-float-end


.. _data-types-amperity-integer:

Integer
==================================================

.. data-types-amperity-integer-start

A numeric value of various lengths.

.. admonition:: Compare to

   **Databricks:** `BIGINT <https://docs.databricks.com/aws/en/sql/language-manual/data-types/bigint-type>`__ |ext_link|, `INT <https://docs.databricks.com/aws/en/sql/language-manual/data-types/int-type>`__ |ext_link|, `SMALLINT <https://docs.databricks.com/aws/en/sql/language-manual/data-types/smallint-type>`__ |ext_link|, and `TINYINT <https://docs.databricks.com/aws/en/sql/language-manual/data-types/tinyint-type>`__ |ext_link|

   **Google BigQuery:** `BIGINT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|, `BYTEINT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|, `INT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|, `INTEGER <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|, `INT64 <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|, `SMALLINT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|, and `TINYINT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

   **Snowflake:** `BIGINT <https://docs.snowflake.com/en/sql-reference/data-types-numeric#int-integer-bigint-smallint-tinyint-byteint>`__ |ext_link|, `INTEGER <https://docs.snowflake.com/en/sql-reference/data-types-numeric#int-integer-bigint-smallint-tinyint-byteint>`__ |ext_link|, `NUMBER <https://docs.snowflake.com/en/sql-reference/data-types-numeric#number>`__ |ext_link|, `SMALLINT <https://docs.snowflake.com/en/sql-reference/data-types-numeric#int-integer-bigint-smallint-tinyint-byteint>`__ |ext_link|, and `TINYINT <https://docs.snowflake.com/en/sql-reference/data-types-numeric#int-integer-bigint-smallint-tinyint-byteint>`__ |ext_link|

.. data-types-amperity-integer-end


.. _data-types-amperity-map:

Map
==================================================

.. data-types-amperity-map-start

A composite fully-structured data type that stores data as key-value pairs.

.. important:: Amperity will load a data source with a map to a domain table.

   For data sources with a map, you must use a custom domain table to convert all elements in the map to individual fields in the table output.

   After all elements are converted to individual fields in the custom domain table output you assign semantic tags and keys to individual fields in the table.

   A map may be used as part of a common table expression (CTE) in Spark SQL and Presto SQL as long as output of the query does not have a field with a map data type.

.. admonition:: Compare to

   **Databricks:** `MAP <https://docs.databricks.com/aws/en/sql/language-manual/data-types/map-type>`__ |ext_link|

   **Google BigQuery:** `JSON <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#json_type>`__ |ext_link| and `STRUCT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type>`__ |ext_link|

   **Snowflake:** `MAP <https://docs.snowflake.com/en/sql-reference/data-types-structured#label-structured-types-specifying-map>`__ |ext_link|

.. data-types-amperity-map-end


.. _data-types-amperity-string:

String
==================================================

.. data-types-amperity-string-start

A sequence of characters.

.. admonition:: Compare to

   **Databricks:** `STRING <https://docs.databricks.com/aws/en/sql/language-manual/data-types/string-type>`__ |ext_link|

   **Google BigQuery:** `JSON <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#json_type>`__ |ext_link| and `STRING <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type>`__ |ext_link|

   **Snowflake:** `CHAR <https://docs.snowflake.com/en/sql-reference/data-types-text#char-character-nchar>`__ |ext_link|, `CHARACTER <https://docs.snowflake.com/en/sql-reference/data-types-text#char-character-nchar>`__ |ext_link|, `STRING <https://docs.snowflake.com/en/sql-reference/data-types-text#string-text-nvarchar-nvarchar2-char-varying-nchar-varying>`__ |ext_link|, and `VARCHAR <https://docs.snowflake.com/en/sql-reference/data-types-text#varchar>`__ |ext_link|

.. data-types-amperity-string-end


.. _data-types-amperity-struct:

Struct
==================================================

.. data-types-amperity-struct-start

A composite fully-structured data type that groups data as a sequence of fields within the structure.

.. important:: Amperity will load a data source with a struct to a domain table.

   For data sources with a struct, you must use a custom domain table to convert all elements in the struct to individual fields in the table output.

   After all elements are converted to individual fields in the custom domain table output you assign semantic tags and keys to individual fields in the table.

   A struct may be used as part of a common table expression (CTE) in Spark SQL and Presto SQL as long as output of the query does not have a field with a struct data type.

.. admonition:: Compare to

   **Databricks:** `STRUCT <https://docs.databricks.com/aws/en/sql/language-manual/data-types/struct-type>`__ |ext_link|

   **Google BigQuery:** `STRUCT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type>`__ |ext_link|

   **Snowflake:** `OBJECT <https://docs.snowflake.com/en/sql-reference/data-types-structured#label-structured-types-specifying-object>`__ |ext_link|

.. data-types-amperity-struct-end


.. _data-types-amperity-unsupported:

Unsupported
==================================================

.. data-types-amperity-unsupported-start

Semi-structured data types are unsupported and must be converted to a fully-structured data type.

.. admonition:: Unsupported data types

   **Databricks:** `BINARY <https://docs.databricks.com/aws/en/sql/language-manual/data-types/binary-type>`__ |ext_link|

   **Google BigQuery:** `BYTES <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#bytes_type>`__ |ext_link| and `RANGE <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#range_type>`__ |ext_link|

   **Snowflake:** `BINARY <https://docs.snowflake.com/en/sql-reference/data-types-text#binary>`__ |ext_link|, `FILE <https://docs.snowflake.com/en/sql-reference/data-types-unstructured#file-data-type>`__ |ext_link|, `Semi-structured data types <https://docs.snowflake.com/en/sql-reference/data-types-semistructured>`__ |ext_link|, `VARBINARY <https://docs.snowflake.com/en/sql-reference/data-types-text#varbinary>`__ |ext_link|, `VARIANT <https://docs.snowflake.com/en/sql-reference/data-types-semistructured#variant>`__ |ext_link|, and `VECTOR <https://docs.snowflake.com/en/sql-reference/data-types-vector>`__ |ext_link|

.. data-types-amperity-unsupported-end
