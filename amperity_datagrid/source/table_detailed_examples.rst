.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Configure and manage the Detailed Examples table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Detailed Examples table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Detailed Examples table

==================================================
Detailed Examples table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-detailed-examples-table-start
   :end-before: .. term-detailed-examples-table-end

.. table-detailed-examples-automatically-added-start

The **Detailed Examples** table is automatically added to the Stitch QA database as a SQL table when it is generated using the "Stitch QA" database template.

.. table-detailed-examples-automatically-added-end


.. _table-detailed-examples-use-with-stitch-qa:

Use with Stitch QA
==================================================

.. table-detailed-examples-use-with-stitch-qa-start

Use the **Detailed Examples** table as part of the Stitch QA process to return a detailed set of examples that show you what is in your customer 360 database. Use this data to identify which types of features lead to scores with the largest effect on overall Stitch results, including how those features are associated with various combinations of fields that contain profile (PII) data.

.. table-detailed-examples-use-with-stitch-qa-end


.. _table-detailed-examples-use-with-stitch-qa-configure:

Configure query
--------------------------------------------------

.. table-detailed-examples-use-with-stitch-qa-configure-start

The **Detailed Examples** query should be configured to match the fields that are in your tenant. Open this table in the **Database Editor** in edit mode and make the following updates:

#. Uncomment rows of matching a/b pairs or add new rows so that the uncommented rows match your tenant.
#. Adjust case count and score count limits, if necessary.
#. Add customer keys (`ck`) if they are available (and update this query if customer keys are added).
#. Uncomment rows for the bad-values blocklist after it is enabled for your tenant.

.. table-detailed-examples-use-with-stitch-qa-configure-end


.. _table-detailed-examples-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-detailed-examples-table-about-start
   :end-before: .. data-tables-detailed-examples-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-detailed-examples-table-start
   :end-before: .. data-tables-detailed-examples-table-end


.. _table-detailed-examples-sql:

SQL reference
==================================================

.. table-detailed-examples-sql-start

.. code-block:: sql

   WITH Filtered_Scores AS (
     SELECT
       score
       ,COUNT(1) AS c
       ,500/COUNT(1) AS p
     FROM Unified_Scores
     GROUP BY score HAVING COUNT(1) > 10000
   ),
   Sampled_Pairs AS (
     SELECT
       us.amperity_id
       ,us.match_category
       ,us.source1
       ,us.source2
       ,us.pk1
       ,us.pk2
       ,us.score
     FROM Filtered_Scores fs
     JOIN Unified_Scores us
     ON us.score = fs.score
     WHERE rand() < p
   )

   SELECT
     scores.match_category
     ,scores.score
     ,fs.c AS score_count
     ,scores.amperity_id
     ,t1.datasource AS datasource_a
     ,t2.datasource AS datasource_b
     ,t1.given_name AS given_name_a
     ,t2.given_name AS given_name_b
     ,t1.surname AS surname_a
     ,t2.surname AS surname_b
     -- UNCOMMENT BELOW IF full_name IS AVAILABLE
     -- ,t1.full_name AS full_name_a
     -- ,t2.full_name AS full_name_b
     -- UNCOMMENT BELOW IF generational_suffix IS AVAILABLE
     -- ,t1.generational_suffix AS generational_suffix_a
     -- ,t2.generational_suffix AS generational_suffix_b
     -- UNCOMMENT BELOW IF title IS AVAILABLE
     -- ,t1.title AS title_a
     -- ,t2.title AS title_b
     ,t1.email AS email_a
     ,t2.email AS email_b
     ,t1.phone AS phone_a
     ,t2.phone AS phone_b
     ,t1.address AS address_a
     ,t2.address AS address_b
     -- UNCOMMENT BELOW IF address2 IS AVAILABLE
     -- ,t1.address2 AS address2_a
     -- ,t2.address2 AS address2_b
     ,t1.birthdate AS birthdate_a
     ,t2.birthdate AS birthdate_b
     ,t1.city AS city_a
     ,t2.city AS city_b
     ,t1.state AS state_a
     ,t2.state AS state_b
     ,t1.country AS country_a
     ,t2.country AS country_b
     ,t1.postal AS postal_a
     ,t2.postal AS postal_b
     -- UNCOMMENT BELOW IF company IS AVAILABLE
     -- ,t1.company AS company_a
     -- ,t2.company AS company_b
     -- UNCOMMENT BELOW IF gender IS AVAILABLE
     -- ,t1.gender AS gender_a
     -- ,t2.gender AS gender_b
     ,t1.pk AS pk_a
     ,t2.pk AS pk_b
     -- UNCOMMENT BELOW IF ck IS AVAILABLE
     -- ,t1.ck AS ck_a
     -- ,t2.ck AS ck_b
     -- OPTIONAL: UNCOMMENT FOR BAD-VALUES BLACKLIST
     -- ,t1.has_blv AS has_blv_a
     -- ,t2.has_blv AS has_blv_b
     -- ,t1.blv_given_name AS blv_given_name_a
     -- ,t2.blv_given_name AS blv_given_name_b
     -- ,t1.blv_surname AS blv_surname_a
     -- ,t2.blv_surname AS blv_surname_b
     -- ,t1.blv_email AS blv_email_a
     -- ,t2.blv_email AS blv_email_b
     -- ,t1.blv_phone AS blv_phone_a
     -- ,t2.blv_phone AS blv_phone_b
     -- ,t1.blv_address AS blv_address_a
     -- ,t2.blv_address AS blv_address_b
     -- USE AS DESIRED FOR namespaced fks
     -- ,t1.fk_field_name AS fk_field_name_a
     -- ,t2.fk_field_name AS fk_field_name_b
     ,ROW_NUMBER() OVER (PARTITION BY scores.score
                         ORDER BY scores.amperity_id, scores.pk1, scores.pk2
                         ) AS case_count
     -- ,ROW_NUMBER() OVER (PARTITION BY scores.amperity_id
                            ORDER BY scores.amperity_id, scores.pk1, scores.pk2
                            ) AS amperity_id_count
   FROM Sampled_Pairs AS scores
   LEFT JOIN Filtered_Scores
     AS fs ON fs.score = scores.score
   LEFT JOIN Unified_Coalesced
     AS t1 ON scores.pk1 = t1.pk AND scores.source1 = t1.datasource
   LEFT JOIN Unified_Coalesced
     AS t2 ON scores.pk2 = t2.pk AND scores.source2 = t2.datasource
   -- OPTIONAL: UNCOMMENT FOR BAD-VALUES BLOCKLIST
   -- AND has_blv IS NULL
   -- AND blv_surname IS NULL
   -- AND blv_given_name IS NULL
   -- AND blv_email IS NULL
   -- AND blv_phone IS NULL
   -- AND blv_address IS NULL

.. table-detailed-examples-sql-end
