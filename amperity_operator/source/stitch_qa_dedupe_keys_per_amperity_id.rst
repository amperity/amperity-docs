.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Troubleshoot Stitch results by the presence of deduplication keys by Amperity ID.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by the presence of deduplication keys by Amperity ID.

.. meta::
    :content class=swiftype name=title data-type=string:
        Deduplication keys per Amperity ID

==================================================
Deduplication keys per Amperity ID
==================================================

.. stitch-qa-query-dedupe-keys-per-amperity-id-start

Use this query to return a rough distribution of deduplication keys to Amperity IDs. The deduplication key may be set to a foreign key, a customer key, or a concatenated value.

There are no obvious "good" or "bad" results, but it is useful to take a closer look at all clusters that return 2 or more deduplication keys, as this shows evidence of records that have been connected, but were previously independent, and may indicate overclustering.

* Foreign keys are interesting because Amperity deterministically matches on foreign keys in most situations. When there are 2 or more deduplication keys related to foreign keys, this is an indication of records that were connected beyond what the customer could have connected deterministically.
* Customer keys are interesting because they show the before and after of entity distribution.
* Concatenated values, such as **datasource + fk** can help focus the results on a per-source level.

.. stitch-qa-query-dedupe-keys-per-amperity-id-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-overcluster-start
   :end-before: .. term-overcluster-end

.. stitch-qa-query-dedupe-keys-per-amperity-id-note-start

.. note:: This query is two queries.

   * The first query returns the distribution of deduplication keys by Amperity ID with one row for the number of Amperity IDs that have 2 or more deduplication keys.
   * The second query returns a list of Amperity IDs along with the number of deduplication keys associated to each Amperity ID, sorted from most to least.

.. stitch-qa-query-dedupe-keys-per-amperity-id-note-end


.. _stitch-qa-query-dedupe-keys-per-amperity-id-use:

When to use
==================================================

.. stitch-qa-query-dedupe-keys-per-amperity-id-use-start

#. Run this query when foreign keys or customer keys are present in the data.
#. If customer keys are present, use **ck** as the deduplication key.
#. Run this query for each data source.
#. Investigate clusters with 2 or more deduplication keys.
#. Look for examples of overclustering.

.. stitch-qa-query-dedupe-keys-per-amperity-id-use-end


.. _stitch-qa-query-dedupe-keys-per-amperity-id-steps:

Configure query
==================================================

.. stitch-qa-query-dedupe-keys-per-amperity-id-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Specify the deduplication key to use for the query. The default deduplication key is a concatenation of data source and primary key:

   .. code-block:: sql

      COUNT(distinct CONCAT(datasource, pk)) AS dk_count

   The deduplication key can be updated to be any combination of foreign key, customer key, primary key, and data source. For example, for a foreign key named **fk-campaign** you could use:

   .. code-block:: sql

      COUNT(distinct fk_campaign) as dk_count

   or you could concatenate the foreign key and data source:

   .. code-block:: sql

      COUNT(distinct CONCAT(datasource, fk_campaign)) as dk_count

   If customer keys are present, you could concatenate the customer key to data sources and primary keys:

   .. code-block:: sql

      COUNT(distinct CONCAT(datasource, COALESCE(ck, pk))) AS dk_count

#. By default, the deduplication key count is 2 or more. You can adjust this value higher:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 4

      SELECT *
      FROM dk_distribution
      WHERE dk_count > 1
      ORDER BY dk_count DESC

   Update ``dk_count > 1`` to the desired threshold.

#. Click **Run Segment** to return a list of Amperity IDs, along with the number of deduplication keys associated to each Amperity ID.
#. To return the distribution of deduplication keys by Amperity ID, first use ``/*`` and ``*/`` to comment out the size investigation **SELECT** statement:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 1,5

      /*SELECT *
      FROM dk_distribution
      WHERE dk_count > 1
      ORDER BY dk_count DESC*/

   Update ``dk_count > 1`` to the desired threshold, and then remove the comments from the distribution **SELECT** statement, and then click **Run Segment**.
#. Click **Activate**.

.. stitch-qa-query-dedupe-keys-per-amperity-id-steps-end
