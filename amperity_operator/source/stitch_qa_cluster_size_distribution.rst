.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing the distribution of clusters by size.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing the distribution of clusters by size.

.. meta::
    :content class=swiftype name=title data-type=string:
        Cluster size distribution

==================================================
Cluster size distribution
==================================================

.. stitch-qa-query-cluster-size-distribution-start

Use this query to understand the overall distribution of clusters. A good Stitch result have an overwhelming majority of small clusters. However, there can be a long-tail of supersized clusters. The query defaults to using primary keys, but should be configured to use customer keys when they are available.

.. stitch-qa-query-cluster-size-distribution-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-supersized-cluster-start
   :end-before: .. term-supersized-cluster-end

.. stitch-qa-query-cluster-size-distribution-note-start

.. note:: The presence of supersized clusters may indicate overclustering.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-overcluster-start
      :end-before: .. term-overcluster-end

.. stitch-qa-query-cluster-size-distribution-note-end


.. _stitch-qa-query-cluster-size-distribution-use:

When to use
==================================================

.. stitch-qa-query-cluster-size-distribution-use-start

#. Run this query to identify if distinct entities are clustered together.
#. Review the cluster size distribution value specified in the query, and then adjust this size limit as appropriate.
#. Look for supersize clusters or other indicators of overclustering.

   .. important:: The presence of clusters that exist outside the 1-20 range is an indicator of overclustering. If a lot of clusters are present at the high end of this range, it is important to investigate those cases to identify if distinct entities were clustered together.
#. If present, investigate each cluster individually.

.. stitch-qa-query-cluster-size-distribution-use-end


.. _stitch-qa-query-cluster-size-distribution-steps:

Configure query
==================================================

.. stitch-qa-query-cluster-size-distribution-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. When customer keys are available, update the common table expression to use both customer and primary keys, instead of just primary keys. Change the following:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 2

      SELECT DISTINCT amperity_id,
        pk
      FROM Unified_Coalesced) GROUP BY amperity_id

   to:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 2

       SELECT DISTINCT amperity_id,
         CONCAT(datasource, COALESCE(ck, pk)) AS pk
       FROM Unified_Coalesced) GROUP BY amperity_id

#. You may adjust the query to count clusters of any size. The default cluster sizes are:

   .. code-block:: sql
      :linenos:

      WHEN cluster_size = 1 THEN '1'
      WHEN cluster_size = 2 THEN '2'
      WHEN cluster_size = 3 THEN '3'
      WHEN cluster_size = 4 THEN '4'
      WHEN cluster_size = 5 THEN '5'
      WHEN cluster_size > 5 AND cluster_size <= 10 THEN '6-10'
      WHEN cluster_size > 10 AND cluster_size <= 20 THEN '11-20'
      WHEN cluster_size > 20 AND cluster_size <= 63 THEN '21-63'
      -- Supersized clusters
      WHEN cluster_size > 63 AND cluster_size <= 100 THEN '64-100'
      WHEN cluster_size > 100 AND cluster_size <= 1000 THEN '101-1000'
      WHEN cluster_size > 1000 AND cluster_size <= 10000 THEN '1001-10000'
      WHEN cluster_size > 10000 THEN '10001+'

   For example, to use cluster sizes of 6, 7, 8, 9, update to:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 6,7,8,9

      WHEN cluster_size = 1 THEN '1'
      WHEN cluster_size = 2 THEN '2'
      WHEN cluster_size = 3 THEN '3'
      WHEN cluster_size = 4 THEN '4'
      WHEN cluster_size = 5 THEN '5'
      WHEN cluster_size = 6 THEN '6'
      WHEN cluster_size = 7 THEN '7'
      WHEN cluster_size = 8 THEN '8'
      WHEN cluster_size = 9 THEN '9'
      WHEN cluster_size > 5 AND cluster_size <= 10 THEN '6-10'
      WHEN cluster_size > 10 AND cluster_size <= 20 THEN '11-20'
      WHEN cluster_size > 20 AND cluster_size <= 63 THEN '21-63'
      -- Supersized clusters
      WHEN cluster_size > 63 AND cluster_size <= 100 THEN '64-100'
      WHEN cluster_size > 100 AND cluster_size <= 1000 THEN '101-1000'
      WHEN cluster_size > 1000 AND cluster_size <= 10000 THEN '1001-10000'
      WHEN cluster_size > 10000 THEN '10001+'

   or to use a cluster size of 5000:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 12,13

      WHEN cluster_size = 1 THEN '1'
      WHEN cluster_size = 2 THEN '2'
      WHEN cluster_size = 3 THEN '3'
      WHEN cluster_size = 4 THEN '4'
      WHEN cluster_size = 5 THEN '5'
      WHEN cluster_size > 5 AND cluster_size <= 10 THEN '6-10'
      WHEN cluster_size > 10 AND cluster_size <= 20 THEN '11-20'
      WHEN cluster_size > 20 AND cluster_size <= 63 THEN '21-63'
      -- Supersized clusters
      WHEN cluster_size > 63 AND cluster_size <= 100 THEN '64-100'
      WHEN cluster_size > 100 AND cluster_size <= 1000 THEN '101-1000'
      WHEN cluster_size > 1000 AND cluster_size <= 5000 THEN '1001-5000'
      WHEN cluster_size > 5000 AND cluster_size <= 10000 THEN '5001-10000'
      WHEN cluster_size > 10000 THEN '10001+'

   .. note:: If you update the cluster sizes, make the same updates to the **CASE** statement below that is used for ordering rows correctly.

#. Run the query, and then review the cluster size distribution.
#. The threshold for supersized clusters is specified in the **CASE** statements to be greater than 63. Uncomment the following **SELECT** statement:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 1,2,3,4

      SELECT *
      FROM cluster_sizes
      WHERE cluster_size > 63
      ORDER BY cluster_size DESC

   and then rerun the query to return only supersized clusters.

   .. tip:: Depending on the type of investigation you want to perform, re-commenting this part of the query may be helpful.
#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-cluster-size-distribution-steps-end
