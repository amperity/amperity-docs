.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by validating foreign key distribution.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by validating foreign key distribution.

.. meta::
    :content class=swiftype name=title data-type=string:
        Foreign key validation

==================================================
Foreign key validation
==================================================

.. stitch-qa-query-fk-validation-start

Use this query to compare two versions of a data source or two distinct data sources and return coverage and distribution data for foreign keys across multiple data sources.

.. note:: This query should not be used to compare distinct foreign keys across data sources, such as **fk-name-id** and **fk-customer-id**.

.. stitch-qa-query-fk-validation-end


.. _stitch-qa-query-fk-validation-use:

When to use
==================================================

.. stitch-qa-query-fk-validation-use-start

#. :ref:`Looking for name IDs with multiple Amperity IDs <stitch-qa-query-fk-validation-name-ids-with-multiple-amperity-ids>`.
#. :ref:`Looking for name IDs with different Amperity IDs <stitch-qa-query-fk-validation-name-ids-with-different-amperity-ids>`.
#. :ref:`Inspecting name IDs between tables <stitch-qa-query-fk-validation-inspect-name-ids>`.
#. :ref:`Checking for foreign keys with multiple Amperity IDs between tables <stitch-qa-query-fk-validation-multiple-amperity-ids>`.
#. :ref:`Checking for foreign keys with different Amperity IDs between tables <stitch-qa-query-fk-validation-different-amperity-ids>`.
#. :ref:`Inspecting foreign keys between tables <stitch-qa-query-fk-validation-inspect-between-tables>`.

.. stitch-qa-query-fk-validation-use-end


.. _stitch-qa-query-fk-validation-steps:

Configure query
==================================================

.. stitch-qa-query-fk-validation-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Uncomment the specific **SELECT** statement to run, and then update that statement for the foreign key names and table names.
#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-fk-validation-steps-end


.. _stitch-qa-query-fk-validation-name-ids-with-multiple-amperity-ids:

Names, multiple IDs
--------------------------------------------------

.. stitch-qa-query-fk-validation-name-ids-with-multiple-amperity-ids-start

Use any of the following **SELECT** statements to look for name IDs with multiple Amperity IDs. Update **name_id** to the name ID, and **data_source** and/or **data_source_v2** to the name of the table and/or table version:

.. code-block:: sql

   SELECT
     name_id
     ,COUNT(DISTINCT amperity_id)
   FROM
     data_source
   GROUP BY 1
   HAVING COUNT(DISTINCT amperity_id) > 1

   SELECT
     name_id
     ,COUNT(DISTINCT amperity_id)
   FROM
     data_source_v2
   GROUP BY 1
   HAVING COUNT(DISTINCT amperity_id) > 1

.. stitch-qa-query-fk-validation-name-ids-with-multiple-amperity-ids-end


.. _stitch-qa-query-fk-validation-name-ids-with-different-amperity-ids:

Names, different IDs
--------------------------------------------------

.. stitch-qa-query-fk-validation-name-ids-with-different-amperity-ids-start

Use any of the following **SELECT** statements to look for name IDs with different Amperity IDs. Update **name_id** to the name ID, and **data_source** and/or **data_source_v2** to the name of the table and/or table version:

.. code-block:: sql

   SELECT
     v1.name_id
     ,v1.amperity_id
     ,v2.amperity_id
   FROM (
     SELECT DISTINCT
       name_id
       ,amperity_id
     FROM
       data_source_v2)
     AS v1
   FULL OUTER JOIN (
     SELECT DISTINCT
       name_id
       ,amperity_id
     FROM
       data_source)
     AS v2
   ON v1.name_id = v2.name_id
   WHERE v1.amperity_id <> v2.amperity_id
   LIMIT 100

.. stitch-qa-query-fk-validation-name-ids-with-different-amperity-ids-end


.. _stitch-qa-query-fk-validation-inspect-name-ids:

Inspect Names
--------------------------------------------------

.. stitch-qa-query-fk-validation-inspect-name-ids-start

Use any of the following **SELECT** statements to inspect name IDs. Update **name_id** to the name ID, and **data_source** and/or **data_source_v2** to the name of the table and/or table version:

.. code-block:: sql

   SELECT COUNT(DISTINCT name_id)
   FROM data_source

.. code-block:: sql

   SELECT COUNT(DISTINCT name_id)
   FROM data_source_v2

.. code-block:: sql

   SELECT COUNT(DISTINCT name_id)
   FROM data_source
   WHERE name_id IN (
     SELECT name_id
     FROM data_source_v2
   )

.. code-block:: sql

   SELECT COUNT(DISTINCT name_id)
   FROM data_source_v2
   WHERE name_id NOT IN (
     SELECT name_id
     FROM data_source
   )

.. stitch-qa-query-fk-validation-inspect-name-ids-end


.. _stitch-qa-query-fk-validation-multiple-amperity-ids:

Multiple Amperity IDs
--------------------------------------------------

.. stitch-qa-query-fk-validation-multiple-amperity-ids-start

Use any of the following **SELECT** statements to look for foreign keys that have multiple Amperity IDs. Update **fk_field_name** to the name of a foreign key, and **data_source**, **data_source_1** and/or **data_source_2** to the name of the table:

.. code-block:: sql

   SELECT
    fk_field_name
    ,COUNT(DISTINCT amperity_id)
   FROM
     data_source_1
   GROUP BY 1
   HAVING COUNT(DISTINCT amperity_id) > 1
   
   SELECT
     fk_field_name
     ,COUNT(DISTINCT amperity_id)
   FROM
     data_source_2
   GROUP BY 1
   HAVING COUNT(DISTINCT amperity_id) > 1

.. stitch-qa-query-fk-validation-multiple-amperity-ids-end


.. _stitch-qa-query-fk-validation-different-amperity-ids:

Different Amperity IDs
--------------------------------------------------

.. stitch-qa-query-fk-validation-different-amperity-ids-start

Use any of the following **SELECT** statements to look for foreign keys that have different Amperity IDs. Update **fk_field_name** to the name of a foreign key, and **data_source**, **data_source_1** and/or **data_source_2** to the name of the table:

.. code-block:: sql

   SELECT
     v1.fk_field_name
     ,v1.amperity_id
     ,v2.amperity_id
   FROM (
     SELECT DISTINCT
       fk_field_name
       ,amperity_id 
     FROM
       data_source_2
     ) 
   AS v1 FULL OUTER JOIN (
     SELECT DISTINCT
       fk_field_name
       ,amperity_id
     FROM
       data_source_1
     )
   AS v2 ON v1.fk_field_name = v2.fk_field_name
   WHERE v1.amperity_id <> v2.amperity_id 
   LIMIT 100

.. stitch-qa-query-fk-validation-different-amperity-ids-end


.. _stitch-qa-query-fk-validation-inspect-between-tables:

Inspect keys between tables
--------------------------------------------------

.. stitch-qa-query-fk-validation-inspect-between-tables-start

Use any of the following **SELECT** statements to inspect foreign keys between tables. Update **fk_field_name** to the name of a foreign key, and **data_source**, **data_source_1** and/or **data_source_2** to the name of the table:

.. code-block:: sql

   SELECT
     COUNT(DISTINCT fk_field_name)
   FROM
     data_source

.. code-block:: sql

   SELECT
     COUNT(DISTINCT fk_field_name)
   FROM
     data_source_1
   WHERE fk_field_name IN (
     SELECT fk_field_name
     FROM data_source_2
   )

.. code-block:: sql

   SELECT
     COUNT(DISTINCT fk_field_name)
   FROM data_source_1
   WHERE fk_field_name NOT IN (
     SELECT fk_field_name
     FROM data_source_2
   )

.. code-block:: sql

   SELECT
     COUNT(DISTINCT fk_field_name)
   FROM data_source_2
   WHERE fk_field_name NOT IN (
     SELECT fk_field_name
     FROM data_source_1
   )

.. stitch-qa-query-fk-validation-inspect-between-tables-end
