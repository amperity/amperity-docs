.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing the scores that were assigned to individual clusters.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing the scores that were assigned to individual clusters.

.. meta::
    :content class=swiftype name=title data-type=string:
        Cluster scores

==================================================
Cluster scores
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pairwise-connection-start
   :end-before: .. term-pairwise-connection-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-pairwise-connection-score-start
   :end-before: .. term-pairwise-connection-score-end

.. stitch-qa-query-cluster-scores-start

Use this query to investigate pairwise comparison scores for an individual cluster or for a set of clusters.

.. stitch-qa-query-cluster-scores-end


.. _stitch-qa-query-cluster-scores-use:

When to use
==================================================

.. stitch-qa-query-cluster-scores-use-start

#. Run this query to investigate pairwise scores.
#. Identify the Amperity IDs each cluster to be investigated and update the query with those IDs.

.. stitch-qa-query-cluster-scores-use-end


.. _stitch-qa-query-cluster-scores-steps:

Configure query
==================================================

.. stitch-qa-query-cluster-scores-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. The query selects a subset of the fields in the **Unified Coalesced** table by default. You may adjust this list up to (and including) selecting all fields.
#. The query is configured for a single Amperity ID. Replace **amp_id** with an Amperity ID:

   .. code-block:: sql
      :emphasize-lines: 4

      FROM Unified_Coalesced uc1
      JOIN unified_coalesced uc2
      ON uc1.amperity_id = uc2.amperity_id
      AND uc1.amperity_id = amp_id
      JOIN Unified_Scores us
      ON uc1.amperity_id = us.amperity_id
      AND uc1.pk = us.pk1
      AND uc2.pk = us.pk2

#. To run the query for multiple Amperity IDs, update the query to input a list of IDs, and then replace each **amp_id** with an Amperity ID:

   .. code-block:: sql
      :emphasize-lines: 4

      FROM Unified_Coalesced uc1
      JOIN unified_coalesced uc2
      ON uc1.amperity_id = uc2.amperity_id
      AND uc1.amperity_id IN (amp_id, amp_id, amp_id, ...)
      JOIN Unified_Scores us
      ON uc1.amperity_id = us.amperity_id
      AND uc1.pk = us.pk1
      AND uc2.pk = us.pk2

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-cluster-scores-steps-end
