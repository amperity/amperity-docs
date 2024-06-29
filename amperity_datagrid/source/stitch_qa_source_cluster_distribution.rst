.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing record-to-cluster size distributions by data source.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing record-to-cluster size distributions by data source.

.. meta::
    :content class=swiftype name=title data-type=string:
        Source cluster distribution

==================================================
Source cluster distribution
==================================================

.. stitch-qa-query-source-cluster-distribution-start

Use this query to return a breakdown of record-to-cluster size distribution by data source.

.. stitch-qa-query-source-cluster-distribution-end


.. _stitch-qa-query-source-cluster-distribution-steps:

Configure query
==================================================

.. stitch-qa-query-source-cluster-distribution-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. If customer keys are available, uncomment the following line:

   .. code-block:: sql

      CONCAT(datasource, COALESCE(ck, pk)) AS dedupe_key

#. You may adjust the query to count clusters of any size. The default cluster sizes are:

   .. code-block:: sql

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
#. Run the query, and then review the source cluster distribution.
#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-source-cluster-distribution-steps-end
