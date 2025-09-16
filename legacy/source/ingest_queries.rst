.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Use ingest queries to shape data before ingest.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use ingest queries to shape data before ingest.

.. meta::
    :content class=swiftype name=title data-type=string:
        About ingest queries

==================================================
About ingest queries
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-ingest-query-start
   :end-before: .. term-ingest-query-end

.. ingest-queries-learning-lab-start

.. admonition:: Amperity Learning Lab

   Ingest queries are a powerful tool that flatten hierarchical, unstructured data like JSON and XML.

   Amperity can ingest data in most formats; however, to be stored in a source domain table and used in processes like Stitch, data must be in a format that fits neatly into rows and columns.

   Open **Learning Lab** for `ingest queries <https://learn.amperity.com/ingest-queries>`__ |ext_link|. Registration is required.

.. ingest-queries-learning-lab-end


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

An ingest query can be used to transform data prior to loading it to Amperity. For example, to remove errant commas, removing extra line breaks, flattening hierarchical data structures, joining data, or resolving other formatting issues. Write an ingest query in Spark SQL and test the query prior to running it in Amperity. An ingest query must be added to a courier as a load operation.

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

* ``file`` is set to the name of the file (``FILE_NAME``) against which the ingest query runs.
* ``FEED_ID`` is set to the ID for the feed for which the ingest query runs.
* ``delimiter`` specifies the delimiter to use with CSV, TSV, and PSV files. (These default to ``,``, ``\t``, and ``|`` respectively if not otherwise specified.)
* ``escape`` defines the character used for escaping quotes inside an already quoted value in the source file. The default escape character in Spark is the backslash (``\``).
* ``multiline`` indicates the presence of records that cross multiple lines. Use only for CSV, TSV, or PSV file types and set to ``true`` only if that file has fields with newline characters in them.

  .. note:: Use an ingest query to remove the multiline elements. For example:

     ::

        REGEXP_REPLACE(message_text,"\n","") AS message_text

* ``quote`` defines the character used for escaping quoted values where the separator can be part of the value in the source file. The default character is the double quote (``"``).
* ``INGEST_QUERY_NAME`` is set to the name of the ingest query.

.. ingest-queries-courier-load-operations-structure-block-end


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
#. Under **SQL Query** define a SQL query using Spark SQL syntax.
#. Click **Save**.

.. ingest-queries-add-steps-end


.. _ingest-queries-add-to-courier-as-load-operation:

Add to courier as load operation
--------------------------------------------------
.. ingest-queries-add-to-courier-as-load-operation-steps-start

#. From the **Sources**, click **Add Courier**. The **Add Courier** dialog box opens.
#. Complete the steps for naming the courier, choosing a plugin, and applying all necessary credentials and configuration settings.
#. Under **Settings**, under **Load Operations**, add a load operation.
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

* :ref:`ingest-queries-example-explode-transactions`
* :ref:`ingest-queries-example-find-records`
* :ref:`ingest-queries-example-flatten-with-identifiers`
* :ref:`ingest-queries-example-import-billing-as-address`
* :ref:`ingest-queries-example-join-datasets`
* :ref:`ingest-queries-example-parse-nested-records`
* :ref:`ingest-queries-example-remove-characters`
* :ref:`ingest-queries-example-remove-field`
* :ref:`ingest-queries-example-select-fields`

.. ingest-queries-examples-end


.. _ingest-queries-example-explode-transactions:

Explode transactions
--------------------------------------------------

.. sql-spark-function-explode-example-load-xml-as-ingest-query-start

.. note:: This example uses an |ext_download_sales_transactions| as the data source for sales transactions.

Use the **EXPLODE()** function to process sales transaction data into a table using an ingest query similar to:

.. code-block:: sql

   WITH explodedData AS (
     SELECT
       salesTransactionId
       ,EXPLODE(salesOrder.tenders.tender) AS tender FROM PosXml
   )

   SELECT
     salesTransactionId
     ,tender.type AS type
     ,tender.amount AS amount
   FROM
     explodedData

.. sql-spark-function-explode-example-load-xml-as-ingest-query-end


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

.. sql-spark-function-nullif-example-ingest-query-start

The following **SELECT** statement is an ingest query that returns **NULL** if the field is empty after trimming whitespace from before and after the initial value:

.. code-block:: sql

   SELECT
     NULLIF(TRIM(BrandName),'') AS BrandName
     ,NULLIF(TRIM(AttributeName),'') AS AttributeName
     ,NULLIF(TRIM(Priority),'') AS Priority
   FROM
     Customer_Table

.. sql-spark-function-nullif-example-ingest-query-end


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


.. _ingest-queries-example-parse-nested-records:

Parse nested records
--------------------------------------------------

.. format-csv-pull-ingest-queries-nested-records-start

Occasionally, a CSV file contains nested records. For example, a field within the CSV file contains JSON data similar to:

.. code-block:: none

   [{"street": "123 Main Street", "apt": "101", "city": "Seattle", "state": "WA", "zip": "98101"}]

which is JSON data in a nested format:

.. code-block:: none

   [
     {
       "street": "123 Main Street",
       "apt": "101",
       "city": "Seattle",
       "state": "WA",
       "zip": "98101"
     }
   ]

There are two general approaches to take when a CSV file contains nested records:

#. Recommended. The customer should update the process for how the data is provided to Amperity to ensure the file does not contain nested records.
#. If the file cannot be provided without nested records, use an ingest query to flatten the data in these fields prior to loading it to Amperity.

   .. note:: This increases the preprocessing effort required by Amperity. Large datasets takes more time and this approach should be avoided with very large datasets and should be used carefully with datasets that is processed on a daily basis.

For example:

.. code-block:: sql

   WITH explodedData AS (
     SELECT
       table_id
       ,EXPLODE(combined_address) AS address FROM Source
   )

   SELECT
     table_id
     ,address.street AS address
     ,address.apt AS address2
     ,address.city AS city
     ,address.state AS state
     ,address.zip AS postal
   FROM Source

.. format-csv-pull-ingest-queries-nested-records-end


.. _ingest-queries-example-remove-characters:

Remove characters with regular expression
--------------------------------------------------

.. ingest-queries-example-remove-characters-start

You can use a regular expression to remove characters. For example, removing double quotes (") *and* backslash (\) characters from an email address from a record similar to:

::

   12345,abcde,"email@gmail.com\",2025-01-30

so that it 

::

   12345,abcde,email@gmail.com,2025-01-30

A regular expression similar to the following removes the double quotes (") *and* backslash (\) characters: 

.. code-block:: sql

   WITH test AS (
     SELECT '12345,abcde,"foobar@gmail.com\",2025-01-30' AS test
   )

   SELECT
     test
     ,REGEXP_REPLACE(test, '[\"\\\\]', '') AS updated_test
   FROM test

.. important:: Be sure to carefully test regular expressions to ensure the result matches your use case.

.. ingest-queries-example-remove-characters-end


.. _ingest-queries-example-remove-field:

Remove field
--------------------------------------------------

.. ingest-queries-example-remove-field-start

Some data sources contain fields that should not be loaded to Amperity. The following table contains a field named ``_update`` that you want to remove before loading the table to Amperity:

.. code-block:: mysql

   ----- ------ ---------------------- ---------
    id    type   datetime               _update
   ----- ------ ---------------------- ---------
    ABC   Add    2020-11-15T04:54:34Z   1
    DEF   Add    2020-11-15T04:55:25Z   0
    GHI   Add    2020-11-15T04:57:12Z   0
   ----- ------ ---------------------- ---------

To remove the ``_update`` field, use an ingest query similar to:

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

In rare cases a file cannot be loaded using a feed and also requires no transforms. Use an ingest query to ``SELECT`` all of the fields:

.. code-block:: sql

   SELECT
     *
   FROM
     table

.. ingest-queries-example-select-fields-end
