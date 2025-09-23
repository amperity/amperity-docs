.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Troubleshoot Stitch results by finding records that are associated with many different semantic values.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by finding records that are associated with many different semantic values.

.. meta::
    :content class=swiftype name=title data-type=string:
        Many semantic values

==================================================
Many semantic values
==================================================

.. stitch-qa-query-many-semantic-values-start

Use this query to explore cases where a single Amperity ID is associated with many different semantic values or associated with combinations of semantic values that are generally good identifiers. 

For example, **email**, **given-name**, and **surname**. Use this query to determine if Amperity has incorrectly clustered different entities together into supersized clusters or by overclustering.

.. stitch-qa-query-many-semantic-values-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-supersized-cluster-start
   :end-before: .. term-supersized-cluster-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-overcluster-start
   :end-before: .. term-overcluster-end


.. _stitch-qa-query-many-semantic-values-use:

When to use
==================================================

.. stitch-qa-query-many-semantic-values-use-start

#. Run this query to identify cases where a single Amperity ID is associated with many semantic values.
#. Run with **email** as the semantic.
#. Run with **phone** as the semantic.
#. Run with **given-name** and **surname** as the semantic.
#. Run with other semantics, as necessary.
#. Examine the results. Look for examples of supersized clusters or for examples of overclustering.

.. stitch-qa-query-many-semantic-values-use-end


.. _stitch-qa-query-many-semantic-values-steps:

Configure query
==================================================

.. stitch-qa-query-many-semantic-values-steps-start

.. vale off

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. You can run this query against multiple semantics. For example, **email**:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 2,7

      SELECT
        LOWER(email),
        COUNT(DISTINCT (amperity_id)) num_amperity_ids
      FROM Unified_Coalesced
      WHERE email IS NOT NULL
      GROUP BY 1
      ORDER BY 2 DESC
      LIMIT 100

   Run for other semantics, as necessary.

#. You can run this query against multiple semantics, comment out the **SELECT** statement used for single semantics and then uncomment the following **SELECT** statement:

   .. code-block:: sql
      :linenos:

      /*
      SELECT
        amperity_id
        -- UPDATE FOR SEMANTICS YOU WANT TO USE
        ,COUNT(DISTINCT LOWER(semantic)) num_semantic
        ,COUNT(DISTINCT LOWER(semantic)) num_semantic
      FROM Unified_Coalesced
      GROUP BY 1
      ORDER BY 2,3 DESC
      LIMIT 100
      */

   For example, to run this statement for **given-name** and **surname**:

   .. code-block:: sql
      :linenos:

      SELECT
        amperity_id
        ,COUNT(DISTINCT LOWER(given_name)) num_given_name
        ,COUNT(DISTINCT LOWER(surname)) num_surname
      FROM Unified_Coalesced
      GROUP BY 1
      ORDER BY 2,3 DESC
      LIMIT 100

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. vale on

.. stitch-qa-query-many-semantic-values-steps-end
