.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing an overview that combines the number of records, accounts, Amperity IDs, singletons, clusters with more than one record, and deduplication rates.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing an overview that combines the number of records, accounts, Amperity IDs, singletons, clusters with more than one record, and deduplication rates.

.. meta::
    :content class=swiftype name=title data-type=string:
        Statistics -- combined

==================================================
Statistics -- combined
==================================================

.. stitch-qa-query-combined-statistics-start

Use this query to return an overview of Stitch statistics that contains the number of records, accounts, Amperity IDs, singletons, clusters with more than one record, overall deduplication rate, and the deduplication rate across all data sources.

.. stitch-qa-query-combined-statistics-end


.. _stitch-qa-query-combined-statistics-steps:

Configure query
==================================================

.. stitch-qa-query-combined-statistics-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. If customer keys are available, change the following line in the common table expression:

   .. code-block:: sql
      :emphasize-lines: 4

      WITH overall_dedupe_keys AS (
        SELECT DISTINCT
          amperity_id
          ,CONCAT(datasource, pk) AS dedupe_key
       FROM Unified_Coalesced

   to:

   .. code-block:: sql
      :emphasize-lines: 4

      WITH overall_dedupe_keys AS (
        SELECT DISTINCT
          amperity_id
          ,CONCAT(datasource, coalesce(ck, pk)) AS dedupe_key
       FROM Unified_Coalesced

   and then change the following line in the **table_dedupe_keys** **SELECT** statement:

   .. code-block:: sql
      :emphasize-lines: 5

      ,table_dedupe_keys AS (
        SELECT DISTINCT
          datasource
          ,amperity_id
          ,pk AS dedupe_key
        FROM Unified_Coalesced

   to:

   .. code-block:: sql
      :emphasize-lines: 5

      ,table_dedupe_keys AS (
        SELECT DISTINCT
          datasource
          ,amperity_id
          ,COALESCE(ck, pk) AS dedupe_key
        FROM Unified_Coalesced

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-combined-statistics-steps-end
