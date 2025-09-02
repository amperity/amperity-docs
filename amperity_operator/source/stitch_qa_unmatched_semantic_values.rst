.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Troubleshoot Stitch results by finding unmatched semantic values.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by finding unmatched semantic values.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unmatched semantic values

==================================================
Unmatched semantic values
==================================================

.. stitch-qa-query-unmatched-semantic-values-start

Use this query to investigate situations where unique semantic values are equal, but Amperity IDs are not.

.. stitch-qa-query-unmatched-semantic-values-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-undercluster-start
   :end-before: .. term-undercluster-end

.. _stitch-qa-query-unmatched-semantic-values-use:

When to use
==================================================

.. stitch-qa-query-unmatched-semantic-values-use-start

#. Run this query to discover pairs of records that contain matching semantic values, but with different assigned Amperity IDs. For example: the same email address, but two different Amperity IDs. This query helps verify that Stitch correctly split records, and then also helps to discover underclustering.
#. Run with email as the semantic value.
#. Run with phone as the semantic value.
#. Run with address as the semantic value.
#. If other individual semantic values are useful for your tenant, run with those semantic values.
#. Run for each semantic value with various **JOIN** conditions, such as given names matching or given names plus surnames matching.
#. Run for each semantic with varying semantic frequency limit values.
#. Look for examples of underclustering.
#. Look for values that should be added to the :doc:`bad-values blocklist <blocklist_bad_values>`.
#. Look for examples of records that were missed during blocking.
#. Look for values that may have been cleared during preprocessing.

.. stitch-qa-query-unmatched-semantic-values-use-end


.. _stitch-qa-query-unmatched-semantic-values-steps:

Configure query
==================================================

.. stitch-qa-query-unmatched-semantic-values-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

   .. note:: These steps describe how to complete this template to find unmatched semantic values for email addresses only. You may modify this template in the **SQL Query Editor** directly prior to running it to support other semantics, such as changing email to phone everywhere, *or* you could create additional queries, one per semantic, so that each query may remain fully customized and tuned for that use case.

#. Update the list of matching fields to contain any additional semantic or custom fields required by your tenant:
   
   .. code-block:: sql
      :linenos:
      :emphasize-lines: 10

      SELECT DISTINCT
        ,t1.amperity_id AS amp_id_a
        ,t2.amperity_id AS amp_id_b
        ,t1.email AS email_a
        ,t2.email AS email_b
        ,t1.given_name AS given_name_a
        ,t2.given_name AS given_name_b
        ,t1.surname AS surname_a
        ,t2.surname AS surname_b
        -- ADD MATCHING PAIRS FOR SEMANTICS

   For example, to add **address**:

   .. code-block:: sql
      :linenos:

      SELECT DISTINCT
        ,t1.amperity_id AS amp_id_a
        ,t2.amperity_id AS amp_id_b
        ,t1.email AS email_a
        ,t2.email AS email_b
        ,t1.given_name AS given_name_a
        ,t2.given_name AS given_name_b
        ,t1.surname AS surname_a
        ,t2.surname AS surname_b
        ,t1.address AS address_a
        ,t2.address AS address_b

#. Update the matching records for all foreign keys:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 1,2

      -- ,t1.fk_field_name AS fk_field_name_a
      -- ,t2.fk_field_name AS fk_field_name_b

   For example:

   .. code-block:: sql
      :linenos:

      ,t1.fk_customer_id AS fk_customer_id_a
      ,t2.fk_customer_id AS fk_customer_id_b
      ,t1.fk_campaign AS fk_campaign_a
      ,t2.fk_campaign AS fk_campaign_b

#. Update the high-frequency value--"100"--for this semantic:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 7

      FROM
        Unified_Coalesced AS t1
        LEFT JOIN (
          SELECT email, TRUE AS high_freq_email
          FROM Unified_Coalesced
          GROUP BY email             
          HAVING COUNT(email) > 100 ) AS hf
          ON LOWER(t1.email) = LOWER(hf.email)
        INNER JOIN

#. Update the **INNER JOIN** for any required additional filtering to be done prior to returning matching conditions:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 6,7

      INNER JOIN
        Unified_Coalesced AS t2
        ON t1.amperity_id <> t2.amperity_id
        AND LOWER(t1.email) = LOWER(t2.email)      
        AND hf.high_freq_email IS NULL
        -- MORE JOIN CONDITIONS MAY BE ADDED
        -- AND LOWER(t1.matching_field) = LOWER(t2.matching_field)

   For example, to require given name and surname to match when email addresses do not match:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 6,7

      INNER JOIN
        Unified_Coalesced AS t2
        ON t1.amperity_id <> t2.amperity_id
        AND LOWER(t1.email) = LOWER(t2.email)      
        AND hf.high_freq_email IS NULL
        AND LOWER(t1.given_name) = LOWER(t2.given_name)
        AND LOWER(t1.surname) = LOWER(t2.surname)

#. If using the :doc:`bad-values blocklist <blocklist_bad_values>` you may apply those blocklist values to the results of this query:

   .. code-block:: sql
      :linenos:

      -- EXCLUDE ENTIRE ROW
      -- AND t1.has_blv IS NULL
      -- EXCLUDE BY FIELD
      -- AND t1.blv_surname IS NULL
      -- AND t1.blv_given_name IS NULL
      -- AND t1.blv_email IS NULL
      -- AND t1.blv_phone IS NULL
      -- AND t1.blv_address IS NULL

   Uncomment the following line to exclude on the entire row:
   
   .. code-block:: sql
      :linenos:
      :emphasize-lines: 2

      -- EXCLUDE ENTIRE ROW
      AND t1.has_blv IS NULL
      -- EXCLUDE BY FIELD
      -- AND t1.blv_surname IS NULL
      -- AND t1.blv_given_name IS NULL
      -- AND t1.blv_email IS NULL
      -- AND t1.blv_phone IS NULL
      -- AND t1.blv_address IS NULL

   Uncomment the following line to exclude on email addresses only:
   
   .. code-block:: sql
      :linenos:
      :emphasize-lines: 6

      -- EXCLUDE ENTIRE ROW
      -- AND t1.has_blv IS NULL
      -- EXCLUDE BY FIELD
      -- AND t1.blv_surname IS NULL
      -- AND t1.blv_given_name IS NULL
      AND t1.blv_email IS NULL
      -- AND t1.blv_phone IS NULL
      -- AND t1.blv_address IS NULL

   Uncomment the appropriate row or rows for this query's use case.

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-unmatched-semantic-values-steps-end
