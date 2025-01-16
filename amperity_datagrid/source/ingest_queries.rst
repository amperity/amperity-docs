.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Use ingest queries to shape data before it is pulled to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use ingest queries to shape data before it is pulled to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Ingest queries

==================================================
Ingest queries
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end


.. _ingest-queries-spark-sql:

Spark SQL
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-spark-sql-start
   :end-before: .. term-spark-sql-end

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-about-start
   :end-before: .. sql-spark-about-end

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-note-spark-vs-presto-start
   :end-before: .. sql-spark-note-spark-vs-presto-end


.. _ingest-queries-courier-load-operations:

Courier load operations
==================================================

.. ingest-queries-courier-load-operations-start

An ingest query can be used to transform data prior to loading it to Amperity. For example, to remove errant commas, removing extra line breaks, flattening hierarchical data structures, joining data, or resolving other formatting issues. An ingest query is written in Spark SQL and should be tested prior to running it in Amperity. An ingest query must be added to a courier as a load operation.

.. ingest-queries-courier-load-operations-end

.. ingest-queries-courier-load-operations-structure-block-start

The structure for an ingest query load operation is similar to:

.. code-block:: none

   {
     "FEED_ID": [
       {
         "type": "spark-sql",
         "spark-sql-files": [
         {
           "file": "FILE_NAME",
           "options": {
             "delimiter": "\,",
             "escape": "\\",
             "multiline": "true",
             "quote": "\""
           }
         }
       ],
       "spark-sql-query": "INGEST_QUERY_NAME"
       }
     ]
   }

where:

* **file** is set to the name of the file (**FILE_NAME**) against which the ingest query will run.
* **FEED_ID** is set to the ID for the feed for which the ingest query will run.
* **delimiter** specifies the delimiter to use with CSV, TSV, and PSV files. (These default to ",", "\t", and "|". respectively if not otherwise specified.)
* **escape** defines the character used for escaping quotes inside an already quoted value in the source file. The default escape character in Spark is the backslash ( ``\`` ).
* **multiline** is an optional parameter that indicates the presence of records that cross multiple lines. Use only for CSV, TSV, or PSV file types and set to "true" only if that file has fields with newline characters in them.

  .. caution:: **multiline** only supports files that contain Unix line endings (**\n**). When **multiline** is enabled for files that contain DOS line endings (**\r\n**) the trailing **\r** character remains in the file, which may cause an ingest failure.

  Use an ingest query to remove multiline elements, as necessary. For example:

     ::

        REGEXP_REPLACE(message_text,"\n","") AS message_text

        REGEXP_REPLACE(message_text,"\r\n","") AS message_text

        REGEXP_REPLACE(message_text,"\r","") AS message_text

* **quote** defines the character used for escaping quoted values where the separator can be part of the value in the source file. The default character is the double quote ( " ).
* **INGEST_QUERY_NAME** is set to the name of the ingest query.

.. ingest-queries-courier-load-operations-structure-block-end


.. _ingest-queries-examples:

Examples
--------------------------------------------------

.. ingest-queries-examples-start

The following file formats can be loaded to Amperity using ingest queries:

* :ref:`ingest-queries-example-apache-avro`
* :ref:`ingest-queries-example-apache-parquet`
* :ref:`ingest-queries-example-cbor`
* :ref:`ingest-queries-example-csv`
* :ref:`ingest-queries-example-json`
* :ref:`ingest-queries-example-ndjson`
* :ref:`ingest-queries-example-psv`
* :ref:`ingest-queries-example-json-streaming`
* :ref:`ingest-queries-example-tsv`
* :ref:`ingest-queries-example-xml`

.. ingest-queries-examples-end


.. _ingest-queries-example-apache-avro:

Apache Avro
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-apache-avro-start
   :end-before: .. term-apache-avro-end

.. ingest-queries-example-apache-avro-start

Use |sql_spark| to define an ingest query for the |format_avro| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-apache-avro-end

.. include:: ../../amperity_reference/source/format_avro.rst
   :start-after: .. format-avro-pull-couriers-load-operations-ingest-query-start
   :end-before: .. format-avro-pull-couriers-load-operations-ingest-query-end


.. _ingest-queries-example-apache-parquet:

Apache Parquet
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-apache-parquet-start
   :end-before: .. term-apache-parquet-end

.. ingest-queries-example-apache-parquet-start

Use |sql_spark| to define an ingest query for the |format_parquet| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-apache-parquet-end

.. include:: ../../amperity_reference/source/format_parquet.rst
   :start-after: .. format-parquet-pull-couriers-load-operations-ingest-query-start
   :end-before: .. format-parquet-pull-couriers-load-operations-ingest-query-end


.. _ingest-queries-example-cbor:

CBOR
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-cbor-start
   :end-before: .. term-cbor-end

.. ingest-queries-example-cbor-start

Use |sql_spark| to define an ingest query for the |format_cbor| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-cbor-end

.. include:: ../../amperity_reference/source/format_cbor.rst
   :start-after: .. format-cbor-pull-couriers-load-operations-block-start
   :end-before: .. format-cbor-pull-couriers-load-operations-block-end


.. _ingest-queries-example-csv:

CSV
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-csv-start
   :end-before: .. term-csv-end

.. ingest-queries-example-csv-start

Use |sql_spark| to define an ingest query for the |format_csv| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-csv-end

.. include:: ../../amperity_reference/source/format_csv.rst
   :start-after: .. format-csv-pull-couriers-load-operations-ingest-query-start
   :end-before: .. format-csv-pull-couriers-load-operations-ingest-query-end

.. include:: ../../amperity_reference/source/format_csv.rst
   :start-after: .. format-csv-pull-couriers-load-operations-ingest-query-caution-start
   :end-before: .. format-csv-pull-couriers-load-operations-ingest-query-caution-end


.. _ingest-queries-example-json:

JSON
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-json-start
   :end-before: .. term-json-end

.. ingest-queries-example-json-start

Use |sql_spark| to define an ingest query for the |format_json| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-json-end

.. include:: ../../amperity_reference/source/format_json.rst
   :start-after: .. format-json-pull-couriers-load-operations-block-start
   :end-before: .. format-json-pull-couriers-load-operations-block-end


.. _ingest-queries-example-ndjson:

NDJSON
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-ndjson-start
   :end-before: .. term-ndjson-end

.. ingest-queries-example-ndjson-start

Use |sql_spark| to define an ingest query for the |format_ndjson| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-ndjson-end

.. include:: ../../amperity_reference/source/format_ndjson.rst
   :start-after: .. format-ndjson-pull-couriers-load-operations-block-start
   :end-before: .. format-ndjson-pull-couriers-load-operations-block-end


.. _ingest-queries-example-psv:

PSV
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-psv-start
   :end-before: .. term-psv-end

.. ingest-queries-example-psv-start

Use |sql_spark| to define an ingest query for the |format_psv| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-psv-end

.. include:: ../../amperity_reference/source/format_psv.rst
   :start-after: .. format-psv-pull-couriers-load-operations-ingest-query-start
   :end-before: .. format-psv-pull-couriers-load-operations-ingest-query-end


.. _ingest-queries-example-json-streaming:

Streaming JSON
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-streaming-json-start
   :end-before: .. term-streaming-json-end

.. ingest-queries-example-json-streaming-start

Use |sql_spark| to define an ingest query for the |format_json_streaming| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-json-streaming-end

.. include:: ../../amperity_reference/source/format_json_streaming.rst
   :start-after: .. format-json-streaming-pull-couriers-load-operations-block-start
   :end-before: .. format-json-streaming-pull-couriers-load-operations-block-end


.. _ingest-queries-example-tsv:

TSV
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-tsv-start
   :end-before: .. term-tsv-end

.. ingest-queries-example-tsv-start

Use |sql_spark| to define an ingest query for the |format_tsv| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-tsv-end

.. include:: ../../amperity_reference/source/format_tsv.rst
   :start-after: .. format-tsv-pull-couriers-load-operations-ingest-query-start
   :end-before: .. format-tsv-pull-couriers-load-operations-ingest-query-end


.. _ingest-queries-example-xml:

XML
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-xml-start
   :end-before: .. term-xml-end

.. ingest-queries-example-xml-start

Use |sql_spark| to define an ingest query for the |format_xml| file. Use a **SELECT** statement to specify which fields should be pulled to Amperity. Apply transforms to those fields as necessary.

.. ingest-queries-example-xml-end

.. include:: ../../amperity_reference/source/format_xml.rst
   :start-after: .. format-xml-pull-couriers-load-operations-block-start
   :end-before: .. format-xml-pull-couriers-load-operations-block-end


.. _ingest-queries-howtos:

How-tos
==================================================

.. ingest-queries-howtos-start

This section describes tasks related to managing ingest queries in Amperity:

* :ref:`ingest-queries-add`
* :ref:`ingest-queries-add-to-courier-as-load-operation`
* :ref:`ingest-queries-delete`
* :ref:`ingest-queries-edit`

.. ingest-queries-howtos-end


.. _ingest-queries-add:

Add ingest query
--------------------------------------------------

.. ingest-queries-add-start

An ingest query allows transformations to be done against customer data prior to adding it to a domain table, such as field-level cleaning, row-level filtering, and joins between files. An ingest query is authored directly from the **Sources** page using an editor that supports Spark SQL syntax.

.. ingest-queries-add-end

**To add an ingest query**

.. ingest-queries-add-steps-start

#. From the **Sources** page, click **Add SQL Query**. This opens the **Add SQL Query** dialog box.
#. Enter the name of the SQL query. This name must be unique.
#. Enter a description for the SQL query.
#. Under **SQL Query** define a SQL query using Spark SQL syntax. For example:

   .. include:: ../../amperity_reference/source/ingest_queries.rst
      :start-after: .. ingest-queries-examples-concatenate-columns-example-start
      :end-before: .. ingest-queries-examples-concatenate-columns-example-end

#. Click **Save**.

.. ingest-queries-add-steps-end


.. _ingest-queries-add-to-courier-as-load-operation:

Add to courier as load operation
--------------------------------------------------

.. include:: ../../amperity_reference/source/ingest_queries.rst
   :start-after: .. ingest-queries-courier-load-operations-start
   :end-before: .. ingest-queries-courier-load-operations-end

**To add an ingest query to courier load operations**

.. ingest-queries-add-to-courier-as-load-operation-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Courier** dialog box opens.
#. Complete the steps for naming the courier, choosing a plugin, and applying all necessary credentials and configuration settings.
#. Under **Settings**, under **Load Operations**, add a load operation:

   .. include:: ../../amperity_reference/source/ingest_queries.rst
      :start-after: .. ingest-queries-courier-load-operations-structure-block-start
      :end-before: .. ingest-queries-courier-load-operations-structure-block-end

#. Click **Save**.

.. ingest-queries-add-to-courier-as-load-operation-steps-end


.. _ingest-queries-delete:

Delete ingest query
--------------------------------------------------

.. ingest-queries-delete-start

You can delete an ingest query. Verify that both upstream and downstream processes no longer depend on this ingest query prior to deleting it.

.. ingest-queries-delete-end

**To delete an ingest query**

.. ingest-queries-delete-steps-start

#. From the **Sources** page, open the menu for an ingest query, and then select **Delete**. The **Delete Query** dialog box opens.
#. Click **Delete**.

.. ingest-queries-delete-steps-end


.. _ingest-queries-edit:

Edit ingest query
--------------------------------------------------

.. ingest-queries-edit-start

You can edit an ingest query.

.. ingest-queries-edit-end

**To edit an ingest query**

.. ingest-queries-edit-steps-start

#. From the **Sources** page, open the menu for an ingest query, and then select **Edit**. The **Edit SQL Query** dialog box opens.
#. Make your changes.
#. Click **Save**.

.. ingest-queries-edit-steps-end


.. _ingest-queries-example-queries:

Example ingest queries
==================================================

.. ingest-queries-examples-start

The following sections show examples of ingest queries:

* :ref:`ingest-queries-example-build-birthdate`
* :ref:`ingest-queries-example-concatenate-columns`
* :ref:`ingest-queries-example-explode-transactions`
* :ref:`ingest-queries-example-find-records`
* :ref:`ingest-queries-example-flatten-with-identifiers`
* :ref:`ingest-queries-example-import-billing-as-address`
* :ref:`ingest-queries-example-join-datasets`
* :ref:`ingest-queries-example-load-xml-data`
* :ref:`ingest-queries-example-parse-nested-records`
* :ref:`ingest-queries-example-remove-field`
* :ref:`ingest-queries-example-select-fields`

.. ingest-queries-examples-end


.. _ingest-queries-example-build-birthdate:

Build birthdate
--------------------------------------------------

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-if-example-build-birthdate-start
   :end-before: .. sql-spark-function-if-example-build-birthdate-end


.. _ingest-queries-example-concatenate-columns:

Concatenate columns
--------------------------------------------------

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-concat-ws-example-build-single-field-start
   :end-before: .. sql-spark-function-concat-ws-example-build-single-field-end


.. _ingest-queries-example-explode-transactions:

Explode transactions
--------------------------------------------------

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-explode-example-load-xml-as-ingest-query-start
   :end-before: .. sql-spark-function-explode-example-load-xml-as-ingest-query-end


.. _ingest-queries-example-find-records:

Find records
--------------------------------------------------

.. ingest-queries-examples-find-records-start

The following example finds records in an incoming table that have been marked as "DELETE", and then creates a table to stores a list of records to be deleted.

.. ingest-queries-examples-find-records-end

.. ingest-queries-examples-find-records-sql-start

.. code-block:: sql

   SELECT
     event.uniquesourceid AS uniqueSourceID
     ,current_date AS deleted_date
   FROM icon
   WHERE event.type='DELETE'

.. ingest-queries-examples-find-records-sql-end


.. _ingest-queries-example-flatten-with-identifiers:

Flatten with identifiers
--------------------------------------------------

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-recommendation-identifiers-example-ingest-query-start
   :end-before: .. sql-spark-recommendation-identifiers-example-ingest-query-end


.. _ingest-queries-example-import-billing-as-address:

Import billing as address
--------------------------------------------------

.. ingest-queries-example-import-billing-as-address-start

The following query imports billing addresses into the address table.

.. ingest-queries-example-import-billing-as-address-end

.. ingest-queries-example-import-billing-as-address-sql-start

.. code-block:: sql

   SELECT *
   FROM Customer_AcmeAddress
   WHERE isBilling = 'true'
   CLUSTER BY address_id

.. ingest-queries-example-import-billing-as-address-sql-end


.. _ingest-queries-example-join-datasets:

JOIN datasets
--------------------------------------------------

.. ingest-queries-example-join-datasets-start

.. note:: This example uses an |ext_download_sales_transactions| as the data source for sales transactions.

.. ingest-queries-example-join-datasets-end

.. ingest-queries-example-join-datasets-sql-start

Use a JOIN operation to join two datasets into a rectangular dataset, similar to:

.. code-block:: sql

   SELECT
     M.*
     ,L.status
   FROM main M
   JOIN lookup L ON M.statusId=L.statusId

.. ingest-queries-example-join-datasets-sql-end


.. _ingest-queries-example-load-xml-data:

Load XML data
--------------------------------------------------

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-explode-example-load-xml-as-ingest-query-start
   :end-before: .. sql-spark-function-explode-example-load-xml-as-ingest-query-end


.. _ingest-queries-example-parse-fields-from-files:

Parse fields from files
--------------------------------------------------

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-substr-example-parse-fields-from-dat-file-start
   :end-before: .. sql-spark-function-substr-example-parse-fields-from-dat-file-end


.. _ingest-queries-example-parse-nested-records:

Parse nested records
--------------------------------------------------

.. include:: ../../amperity_reference/source/format_csv.rst
   :start-after: .. format-csv-pull-ingest-queries-nested-records-start
   :end-before: .. format-csv-pull-ingest-queries-nested-records-end


.. _ingest-queries-example-remove-field:

Remove field
--------------------------------------------------

.. ingest-queries-example-remove-field-start

Some data sources contain fields that should not be loaded to Amperity. The following table contains a field named **_update** that you want to remove before loading the table to Amperity:

.. code-block:: mysql

   ----- ------ ---------------------- ---------
    id    type   datetime               _update
   ----- ------ ---------------------- ---------
    ABC   Add    2020-11-15T04:54:34Z   1
    DEF   Add    2020-11-15T04:55:25Z   0
    GHI   Add    2020-11-15T04:57:12Z   0
   ----- ------ ---------------------- ---------

To remove the **_update** field, use an ingest query similar to:

.. code-block:: sql

   SELECT
     id
     ,type
     ,datetime
   FROM
     table

.. ingest-queries-example-remove-field-end


.. _ingest-queries-example-select-fields:

Select all fields
--------------------------------------------------

.. ingest-queries-example-select-fields-start

In rare cases a file cannot be loaded using a feed and also requires no transforms. Use an ingest query to **SELECT** all of the fields:

.. code-block:: sql

   SELECT
     *
   FROM
     table

.. ingest-queries-example-select-fields-end
