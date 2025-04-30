.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing an overview of statistics for Stitch, separated by deduplication keys and tables.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing an overview of statistics for Stitch, separated by deduplication keys and tables.

.. meta::
    :content class=swiftype name=title data-type=string:
        General separated statistics

==================================================
General separated statistics
==================================================

.. stitch-qa-query-separated-statistics-start

Use this query to return an overview of Stitch statistics, separated by deduplication keys and tables. This query is split into two individual queries: OVERALL and TABLE.

.. warning:: Running both queries together may exhaust the resources in a large tenant. It is recommended to run just one query at a time.

.. stitch-qa-query-separated-statistics-end


.. _stitch-qa-query-separated-statistics-steps:

Configure query
==================================================

.. stitch-qa-query-separated-statistics-steps-start

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
          ,CONCAT(datasource, COALESCE(ck, pk)) AS dedupe_key
       FROM Unified_Coalesced

   and then change the following line in the **table_dedupe_keys** **SELECT** statement:

   .. code-block:: sql
      :emphasize-lines: 5

      WITH table_dedupe_keys AS (
        SELECT DISTINCT
          datasource
          ,amperity_id
          ,pk AS dedupe_key
        FROM Unified_Coalesced

   to:

   .. code-block:: sql
      :emphasize-lines: 5

      WITH table_dedupe_keys AS (
        SELECT DISTINCT
          datasource
          ,amperity_id
          ,COALESCE(ck, pk) AS dedupe_key
        FROM Unified_Coalesced

#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-separated-statistics-steps-end
