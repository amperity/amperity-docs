.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Troubleshoot Stitch results by identifying the lowest-scoring record pair.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by identifying the lowest-scoring record pair.

.. meta::
    :content class=swiftype name=title data-type=string:
        Weakest match

==================================================
Weakest match
==================================================

.. stitch-qa-query-weakest-match-start

Use this query to identify the lowest-scoring record pair, also referred to as the weakest match, within every Amperity ID cluster to improve the overall quality of Stitch results.

.. stitch-qa-query-weakest-match-end

.. stitch-qa-query-weakest-match-note-start

.. note:: There should be a notable decline over time for the number of clusters in which the weakest match is below the Stitch threshold. These clusters are required to have transitive connections to other high-quality pairs. If records are matched in clusters that do not have transitive connections to other high-quality pairs, it's important to investigate those clusters to confirm if they were accurately clustered together and do have transitive connections to other high-quality pairs.

.. stitch-qa-query-weakest-match-note-end


.. _stitch-qa-query-weakest-match-use:

When to use
==================================================

.. stitch-qa-query-weakest-match-use-start

#. Run this query periodically.
#. Review the results of this query.
#. Look for lowest scoring record pairs, and then investigate them.

.. stitch-qa-query-weakest-match-use-end


.. _stitch-qa-query-weakest-match-steps:

Configure query
==================================================

.. stitch-qa-query-weakest-match-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-weakest-match-steps-end
