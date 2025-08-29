.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing a detailed set of examples that show what is in your customer 360 database.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing a detailed set of examples that show what is in your customer 360 database.

.. meta::
    :content class=swiftype name=title data-type=string:
        Detailed examples

==================================================
Detailed examples
==================================================

.. stitch-qa-query-detailed-examples-start

Use this query to return a detailed set of examples that show you what is in your customer 360 database. Use this data to identify which types of features lead to scores with the largest effect on overall Stitch results, including how those features are associated with various combinations of fields that contain PII data.

.. stitch-qa-query-detailed-examples-end


.. _stitch-qa-query-detailed-examples-use:

When to use
==================================================

.. stitch-qa-query-detailed-examples-use-start

#. Run this query on a regular basis.
#. Review the results of this query (typically ~30-60 minutes).
#. Look for clusters with anomalies above the threshold.
#. Investigate each individual cluster in which anomalies are discovered.

.. stitch-qa-query-detailed-examples-use-end


.. _stitch-qa-query-detailed-examples-steps:

Configure query
==================================================

.. stitch-qa-query-detailed-examples-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Update the list of matched records to reflect those used for your tenant. The list of matched records is an A/B pair of semantic fields. The default template includes **given-name**, **surname**, **email**, **phone**, **address**, **birthdate**, **city**, **state**, and **postal**. 

   Add matched records for one or more of the **full-name**, **generational-suffix**, **gender**, **address2**, **company**, and **title** semantic fields. For example:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 5,6,7,8,15,16,27,28,29,30

       ,t1.given_name AS given_name_a
       ,t2.given_name AS given_name_b
       ,t1.surname AS surname_a
       ,t2.surname AS surname_b
       ,t1.full_name AS full_name_a
       ,t2.full_name AS full_name_b
       ,t1.generational_suffix AS generational_suffix_a
       ,t2.generational_suffix AS generational_suffix_b
       ,t1.title AS title_a
       ,t2.title AS title_b
       ,t1.email AS email_a
       ,t2.email AS email_b
       ,t1.phone AS phone_a
       ,t2.phone AS phone_b
       ,t1.address AS address_a
       ,t2.address AS address_b
       ,t1.address2 AS address2_a
       ,t2.address2 AS address2_b
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
       ,t1.company AS company_a
       ,t2.company AS company_b
       ,t1.gender AS gender_a
       ,t2.gender AS gender_b

#. When customer keys are present, uncomment the matching records:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 3,4

      ,t1.pk AS pk_a
      ,t2.pk AS pk_b
      ,t1.ck AS ck_a
      ,t2.ck AS ck_b

#. Update the matching records for all foreign keys:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 1,2

      -- ,t1.fk_field_name AS fk_field_name_a
      -- ,t2.fk_field_name AS fk_field_name_b

   For example:

   .. code-block:: sql
      :linenos:

      t1.fk_customer_id AS fk_customer_id_a,
      t2.fk_customer_id AS fk_customer_id_b,
      t1.fk_campaign AS fk_campaign_a
      t2.fk_campaign AS fk_campaign_b

#. Rows may be numbered by case (default) or by Amperity ID.

   .. code-block:: sql
      :linenos:

      ROW_NUMBER() OVER (PARTITION BY scores.score
                         ORDER BY scores.amperity_id
                                  ,scores.pk1
                                  ,scores.pk2)
                         AS case_count
      -- ROW_NUMBER() OVER (PARTITION BY scores.amperity_id
      --                    ORDER BY scores.amperity_id,
      --                             scores.pk1,
      --                             scores.pk2)
      --                    AS amperity_id_count

#. Set the case count limit to be greater than "1" to return more examples of each feature:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 3

      Filtered_Examples AS (
        SELECT * FROM Detailed_Examples
        WHERE case_count <= 1
        AND score_count > 1000
      )

   .. important:: Set **case_count** to "1" when calculating coverage.

#. Set the score count limit:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 4

      Filtered_Examples AS (
        SELECT * FROM Detailed_Examples
        WHERE case_count <= 1
        AND score_count > 1000
      )

#. Update the list of fields for filtered examples for the list of semantic values you want included in the results.

   For example, to include **email**, **given_name**, **address**, and **phone**:
   
   .. code-block:: sql
      :linenos:
      :emphasize-lines: 3,4,5,6

      SELECT *
        FROM Filtered_Examples
        WHERE email_a <> email_b
        AND given_name_a <> given_name_b
        AND address_a <> address_b
        AND phone_a <> phone_b
      ORDER BY score DESC

   .. hint:: This should be the same list as specified for matched records.

#. To return coverage statistics, uncomment the **SELECT** statement under coverage stats:

   .. code-block:: sql
      :linenos:

      SELECT
        SUM(score_count) AS example_coverage
        ,(SELECT COUNT(1) FROM Unified_Scores) AS total_scores,
        ,CAST(SUM(score_count) as DECIMAL(12,3))
              / CAST((SELECT COUNT(1) FROM Unified_Scores) AS DECIMAL(12,3))
              * CAST(100 AS DECIMAL) AS coverage_percentage
      FROM Filtered_Examples

#. If using the :doc:`bad-values blocklist <blocklist_bad_values>` you may apply those blocklist values to the results of this query. This requires uncommenting two sections of this query. First, uncomment the matching records:

   .. code-block:: sql
      :linenos:

      ,t1.has_blv as has_blv_a
      ,t2.has_blv as has_blv_b
      ,t1.blv_given_name as blv_given_name_a
      ,t2.blv_given_name as blv_given_name_b
      ,t1.blv_surname as blv_surname_a
      ,t2.blv_surname as blv_surname_b
      ,t1.blv_email as blv_email_a
      ,t2.blv_email as blv_email_b
      ,t1.blv_phone as blv_phone_a
      ,t2.blv_phone as blv_phone_b
      ,t1.blv_address as blv_address_a
      ,t2.blv_address as blv_address_b

   and then enable them to be part of the **LEFT JOIN** operations for unified scores:
   
   .. code-block:: sql
      :linenos:

      AND has_blv IS null
      AND blv_surname IS null
      AND blv_given_name IS null
      AND blv_email IS null
      AND blv_phone IS null
      AND blv_address IS null

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-detailed-examples-steps-end
