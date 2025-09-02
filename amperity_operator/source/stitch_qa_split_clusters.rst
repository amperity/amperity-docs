.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Troubleshoot Stitch results by finding split clusters.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by finding split clusters.

.. meta::
    :content class=swiftype name=title data-type=string:
        Split clusters

==================================================
Split clusters
==================================================

.. stitch-qa-query-split-clusters-start

Use this query to investigate patterns in split clusters that lack transitive matching for names, email addresses, and/or post office boxes, and for semantic tagging issues that may arise when using multiple, ordinal, or namespaced semantics.

.. stitch-qa-query-split-clusters-end


.. _stitch-qa-query-split-clusters-use:

When to use
==================================================

.. stitch-qa-query-split-clusters-use-start

#. Run this query to identify split clusters.
#. Test various column selections and/or versions of columns from the **Unified Coalesced** table.
#. Add/update **WHERE** conditions to filter the initial results.
#. Spend 30-60 minutes examining various **CASE** statements and filters.
#. Adjust selection columns from the **Unified Coalesced** table to inspect various cases of matching PII.
#. Look for examples of missed nicknames.
#. Look for examples of new address keywords or formats.

.. stitch-qa-query-split-clusters-use-end


.. _stitch-qa-query-split-clusters-steps:

Configure query
==================================================

.. stitch-qa-query-split-clusters-steps-start

.. vale off

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Update the common table expression for any calculated fields required by your tenant:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 6

      SELECT DISTINCT
        amperity_id
        ,regexp_replace(LOWER(given_name), '[^a-zA-Z]+', '') AS given_name
        ,regexp_replace(LOWER(surname), '[^a-zA-Z]+', '') AS surname
        ,split(regexp_replace(LOWER(email), '[.]+', ''), '@')[1] AS email_username
        -- regex_replace(LOWER(field_name), expression, '') AS calculated_field
        ,LOWER(email) AS email
        ,regexp_replace(LOWER(address), '[.]+', '') AS address
        ,postal
        ,city
        ,state
      FROM Unified_Coalesced

   For example, to add **email_domain** as a calculated field:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 6

      SELECT DISTINCT
        amperity_id
        ,regexp_replace(LOWER(given_name), '[^a-zA-Z]+', '') AS given_name
        ,regexp_replace(LOWER(surname), '[^a-zA-Z]+', '') AS surname
        ,split(regexp_replace(LOWER(email), '[.]+', ''), '@')[1] AS email_username
        ,replace(lower(email), split(regexp_replace(lower(email), '\+(.*?)\@', '@'), '@')[1], '') AS email_domain
        ,LOWER(email) AS email
        ,regexp_replace(LOWER(address), '[.]+', '') AS address
        ,postal
        ,city
        ,state
      FROM Unified_Coalesced

#. Extend the **WHERE** clause in the common table expression as necessary. For example:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 4

      WHERE
        length(regexp_replace(LOWER(given_name), '[^a-zA-Z]+', '')) > 0
        AND length(regexp_replace(LOWER(surname), '[^a-zA-Z]+', '')) > 0        
        AND email IS NOT NULL
        AND email NOT LIKE '%+%'

#. Update the list of fields to contain any additional semantic or custom fields required by your tenant:
   
   .. code-block:: sql
      :linenos:
      :emphasize-lines: 20

      SELECT
        uc1.amperity_id AS amp_1
        ,uc2.amperity_id AS amp_2
        ,uc1.given_name AS given_1
        ,uc2.given_name AS given_2
        ,uc1.surname AS sur_1
        ,uc2.surname AS sur_2
        ,uc1.email AS email_1
        ,uc2.email AS email_2
        ,uc1.email_username AS email_username_1
        ,uc2.email_username AS email_username_2
        ,uc1.address AS adr_1
        ,uc2.address AS adr_2
        ,uc1.postal AS pos_1
        ,uc2.postal AS pos_2
        ,uc1.city AS city_1
        ,uc2.city AS city_2
        ,uc1.state AS state_1
        ,uc2.state AS state_2
        -- ADD MATCHING PAIRS FOR SEMANTICS

   For example, to add **postal** and **gender**:

   .. code-block:: sql
      :linenos:

      SELECT
        uc1.amperity_id AS amp_1
        ,uc2.amperity_id AS amp_2
        ,uc1.given_name AS given_1
        ,uc2.given_name AS given_2
        ,uc1.surname AS sur_1
        ,uc2.surname AS sur_2
        ,uc1.email AS email_1
        ,uc2.email AS email_2
        ,uc1.email_username AS email_username_1
        ,uc2.email_username AS email_username_2
        ,uc1.address AS adr_1
        ,uc2.address AS adr_2
        ,uc1.postal AS pos_1
        ,uc2.postal AS pos_2
        ,uc1.city AS city_1
        ,uc2.city AS city_2
        ,uc1.state AS state_1
        ,uc2.state AS state_2
        ,uc1.postal AS postal_1
        ,uc2.postal AS postal_2
        ,uc1.gender AS gender_1
        ,uc2.gender AS gender_2

#. Update the list of fields for all foreign keys:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 1,2

       -- ADD MATCHING PAIRS FOR FOREIGN KEYS
       -- ,t1.fk_field_name AS fk_field_name_1
       -- ,t2.fk_field_name AS fk_field_name_2

   For example:

   .. code-block:: sql
      :linenos:

      ,t1.fk_customer_id AS fk_customer_id_1
      ,t2.fk_customer_id AS fk_customer_id_2
      ,t1.fk_campaign AS fk_campaign_1
      ,t2.fk_campaign AS fk_campaign_2

#. If using the :doc:`bad-values blocklist <blocklist_bad_values>` you may apply those blocklist values to the results of this query. Uncomment the following rows:

   .. code-block:: sql
      :linenos:

      -- AND blv_surname IS NULL
      -- AND blv_given_name IS NULL
      -- AND blv_email IS NULL
      -- AND blv_phone IS NULL
      -- AND blv_address IS NULL

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. vale on

.. stitch-qa-query-split-clusters-steps-end
