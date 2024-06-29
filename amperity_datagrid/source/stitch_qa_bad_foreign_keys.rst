.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing bad foreign key matches.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing bad foreign key matches.

.. meta::
    :content class=swiftype name=title data-type=string:
        Bad foreign key matches

==================================================
Bad foreign key matches
==================================================

.. stitch-qa-query-bad-foreign-key-matches-start

Use this query to return records where the Amperity ID and the foreign key are equal, but one (or more) values associated with the **email**, **given-name**, and **surname** semantics are not equal. Records with incorrect matches may be an indicator of overclustering.

.. stitch-qa-query-bad-foreign-key-matches-end

.. stitch-qa-query-bad-foreign-key-matches-tip-start

.. tip:: Foreign keys are matched deterministically which can lead to incorrect matches or overclustering.

.. stitch-qa-query-bad-foreign-key-matches-tip-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-overcluster-start
   :end-before: .. term-overcluster-end


.. _stitch-qa-query-bad-foreign-key-matches-use:

When to use
==================================================

.. stitch-qa-query-bad-foreign-key-matches-use-start

#. Run this query when foreign keys exist.
#. Review the results of this query (typically ~30 minutes).
#. Look for potentially inaccurate foreign keys.
#. Look for indicators of overclustering.

.. stitch-qa-query-bad-foreign-key-matches-use-end


.. _stitch-qa-query-bad-foreign-key-matches-steps:

Configure query
==================================================

.. stitch-qa-query-bad-foreign-key-matches-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Update the query for unique foreign keys, customer keys, or concatenated values against which comparisons will be made. 

   Uncomment the following lines and replace them with the names of unique foreign keys, one pair of lines per unique foreign key or customer key:

   .. code-block:: sql
      :emphasize-lines: 3,4

      t1.amperity_id AS amp_id_a,
      t2.amperity_id AS amp_id_b,
      -- t1.fk AS fk_a,
      -- t2.fk AS fk_b,
      t1.email AS email_a,
      t2.email AS email_b,

   Use the following pattern to make comparisons against a foreign key or customer key:

   ::

      fk_name_id, CONCAT(datasource, fk)

   For example, for foreign keys named **fk-customer-id** and **fk-campaign**, with the latter concatenated against the **EmailList** data source:

   .. code-block:: sql

      t1.amperity_id AS amp_id_a,
      t2.amperity_id AS amp_id_b,
      t1.fk_customer_id AS fk_customer_id_a,
      t2.fk_customer_id AS fk_customer_id_b,
      t1.fk_campaign AS fk_campaign_a, CONCAT(email_list, fk_campaign)
      t2.fk_campaign AS fk_campaign_b, CONCAT(email_list, fk_campaign)
      t1.email AS email_a,
      t2.email AS email_b,

#. Update the INNER JOIN for the same set of foreign keys:
   
   .. code-block:: sql
      :emphasize-lines: 3

      INNER JOIN Unified_Coalesced AS t2
        ON  t1.amperity_id = t2.amperity_id
        -- AND t1.fk = t2.fk
        AND hf.high_freq_email IS NULL

   For example:

   .. code-block:: sql

      INNER JOIN Unified_Coalesced AS t2
        ON  t1.amperity_id = t2.amperity_id
        AND fk_customer_id.fk = fk_customer_id.fk
        AND fk_campaign.fk = fk_campaign.fk
        AND hf.high_freq_email IS NULL

#. Update for other semantic values against which comparisons will be made. 

   Add the following pair of lines for each added semantic value:

   .. code-block:: sql
      :emphasize-lines: 3,4

      t1.email AS email_a,
      t2.email AS email_b,
      t1.semantic AS semantic_a,
      t2.semantic AS semantic_b,

   For example, to add **address** and **loyalty** (a custom semantic typically associated with loyalty programs):

   .. code-block:: sql

      t1.email AS email_a,
      t2.email AS email_b,
      t1.address AS address_a,
      t2.address AS address_b,
      t1.loyalty AS loyalty_a,
      t2.loyalty AS loyalty_b,

#. Replace **100** with the value that best represents the definition of high-frequency email:

   .. code-block:: sql
      :emphasize-lines: 3

      LEFT JOIN (
        SELECT email, TRUE AS high_freq_email FROM Unified_Coalesced GROUP BY email
        HAVING COUNT(email) > 100
      ) AS hf ON LOWER(t1.email) = LOWER(hf.email)

   and then set the value for **high_freq_email** to NULL or TRUE:

   .. code-block:: sql
      :emphasize-lines: 3

      INNER JOIN Unified_Coalesced AS t2
        ON  t1.amperity_id = t2.amperity_id
        AND hf.high_freq_email IS NULL

#. Update the INNER JOIN for all foreign keys:
   
   .. code-block:: sql
      :emphasize-lines: 3

      INNER JOIN Unified_Coalesced AS t2
        ON  t1.amperity_id = t2.amperity_id
        -- AND t1.fk = t2.fk
        AND hf.high_freq_email IS NULL

   For example:

   .. code-block:: sql

      INNER JOIN Unified_Coalesced AS t2
        ON  t1.amperity_id = t2.amperity_id
        AND fk_customer_id.fk = fk_customer_id.fk
        AND fk_campaign.fk = fk_campaign.fk
        AND hf.high_freq_email IS NULL

#. Update the INNER JOIN for any conditions for which you want to explore unmatched values. These conditions typically are done for semantic fields that should not match. Use the following pattern:

   ::

      AND TRIM(LOWER(t1.unmatched_field)) <> TRIM(LOWER(t2.unmatched_field))

   Uncomment the following line and replace **unmatched_field** with the names of the field for which you want to explore unmatched values. Add a line for each field:

   .. code-block:: sql
      :emphasize-lines: 7

      INNER JOIN Unified_Coalesced AS t2
        ON  t1.amperity_id = t2.amperity_id
        AND hf.high_freq_email IS NULL
        AND TRIM(LOWER(t1.email)) <> TRIM(LOWER(t2.email))
        AND TRIM(LOWER(t1.given_name)) <> TRIM(LOWER(t2.given_name))
        AND TRIM(LOWER(t1.surname)) <> TRIM(LOWER(t2.surname))
        --AND LOWER(t1.unmatched_field) <> LOWER(t2.unmatched_field)

   For example, to add **address** and **loyalty** to the list of conditions:

   .. code-block:: sql

      INNER JOIN Unified_Coalesced AS t2
        ON  t1.amperity_id = t2.amperity_id
        AND hf.high_freq_email IS NULL
        AND TRIM(LOWER(t1.email)) <> TRIM(LOWER(t2.email))
        AND TRIM(LOWER(t1.given_name)) <> TRIM(LOWER(t2.given_name))
        AND TRIM(LOWER(t1.surname)) <> TRIM(LOWER(t2.surname))
        AND TRIM(LOWER(t1.address)) <> TRIM(LOWER(t2.address))
        AND TRIM(LOWER(t1.loyalty)) <> TRIM(LOWER(t2.loyalty))

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-bad-foreign-key-matches-steps-end
