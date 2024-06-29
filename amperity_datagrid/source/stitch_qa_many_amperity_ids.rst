.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by finding records that are associated with many different Amperity IDs.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by finding records that are associated with many different Amperity IDs.

.. meta::
    :content class=swiftype name=title data-type=string:
        Many Amperity IDs

==================================================
Many Amperity IDs
==================================================

.. stitch-qa-query-many-amperity-ids-start

Use this query to explore cases where semantic values are associated with many different Amperity IDs, which may result in underclustering.

The results of this query will help:

* Determine whether Amperity has incorrectly split entities.
* Understand the cardinality of semantic values.
* Identify values to add to the :doc:`bad-values blocklist <blocklist_bad_values>`.

.. stitch-qa-query-many-amperity-ids-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-undercluster-start
   :end-before: .. term-undercluster-end


.. _stitch-qa-query-many-amperity-ids-use:

When to use
==================================================

.. stitch-qa-query-many-amperity-ids-use-start

#. Run this query to identify cases where semantic values are associated with many Amperity IDs.
#. Run with **email** as the semantic.
#. Run with **phone** as the semantic.
#. Run with **address** as the semantic.
#. Run with other semantics, as necessary.
#. Examine the results (~30 minutes). Look for examples of underclustering and for values that can be added to the :doc:`bad-values blocklist <blocklist_bad_values>`.

.. stitch-qa-query-many-amperity-ids-use-end


.. _stitch-qa-query-many-amperity-ids-steps:

Configure query
==================================================

.. stitch-qa-query-many-amperity-ids-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Run the query three times, once each for the following semantics: **email**, **phone**, and **address**. Update the highlighted lines prior to running the query.

   For **email**:

   .. code-block:: sql
      :emphasize-lines: 2,7

      SELECT
        LOWER(email),
        COUNT(DISTINCT (amperity_id)) num_amperity_ids
      FROM
        Unified_Coalesced
      WHERE
        email IS NOT NULL
      GROUP BY 1
      ORDER BY 2 DESC
      LIMIT 100

   For **phone**:

   .. code-block:: sql
      :emphasize-lines: 2,7

      SELECT
        LOWER(phone),
        COUNT(DISTINCT (amperity_id)) num_amperity_ids
      FROM
        Unified_Coalesced
      WHERE
        phone IS NOT NULL
      GROUP BY 1
      ORDER BY 2 DESC
      LIMIT 100

   For **address**:

   .. code-block:: sql
      :emphasize-lines: 2,7

      SELECT
        LOWER(address),
        COUNT(DISTINCT (amperity_id)) num_amperity_ids
      FROM
        Unified_Coalesced
      WHERE
        address IS NOT NULL
      GROUP BY 1
      ORDER BY 2 DESC
      LIMIT 100

   Run for other semantics, as necessary.

#. If you need to run the query against multiple semantics, comment out the **SELECT** statement used for single semantics and then uncomment the following **SELECT** statement:

   .. code-block:: sql

      /*
      SELECT
        -- UPDATE FOR SEMANTICS YOU WANT TO USE
        LOWER(semantic)
        ,LOWER(semantic)
        ,COUNT(DISTINCT (amperity_id)) num_amperity_ids
      FROM
        Unified_Coalesced
      WHERE
        -- UPDATE FOR SEMANTICS YOU WANT TO USE
        semantic IS NOT NULL
        AND semantic IS NOT NULL
      GROUP BY 1
      -- UPDATE ORDERING FOR NUMBER OF COMBINED SEMANTICS
      ORDER BY 2,3 DESC
      LIMIT 100
      */

   Update the list of **semantic** values in both the **SELECT** statement and the **WHERE** clause, and then specify the ordering for combined semantics.

   For example, to run this statement for **email**, **phone**, and **address**:

   .. code-block:: sql

      SELECT
        LOWER(email)
        ,LOWER(phone)
        ,LOWER(address)
        ,COUNT(DISTINCT (amperity_id)) num_amperity_ids
      FROM
        Unified_Coalesced
      WHERE
        -- UPDATE FOR SEMANTICS YOU WANT TO USE
        email IS NOT NULL
        AND phone IS NOT NULL
        AND address IS NOT NULL
      GROUP BY 1
      -- UPDATE ORDERING FOR NUMBER OF COMBINED SEMANTICS
      ORDER BY 2,3 DESC
      LIMIT 100

#. Keep track of values that indicate underclustering and values that should be added to the bad-values blocklist.

#. Use the following query to use those values to find the related Amperity IDs: 

   .. code-block:: sql
      :emphasize-lines: 4

      SELECT
        *
      FROM Unified_Coalesced
      WHERE lower(email) = 'value'

   Replace **email** with the correct semantic and **value** with one of the values retured by the other **SELECT** statements in this query.

   .. tip:: You can create a separate query that contains only this **SELECT** statement instead of commenting out the **SELECT** statements in this query that find a single semantic or a combination of semantics.
#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-many-amperity-ids-steps-end
