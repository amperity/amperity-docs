.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Review the list of queries that are available when troubleshooting Stitch results.

.. meta::
    :content class=swiftype name=body data-type=text:
        Review the list of queries that are available when troubleshooting Stitch results.

.. meta::
    :content class=swiftype name=title data-type=string:
        Stitch QA queries

==================================================
Stitch QA queries
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sql-segment-editor-start
   :end-before: .. term-sql-segment-editor-end


.. _segment-editor-sql-stitch-qa-add-queries:

Add queries
==================================================

.. include:: ../../amperity_reference/source/queries.rst
   :start-after: .. queries-manage-add-start
   :end-before: .. queries-manage-add-end

**To add a SQL query**

.. include:: ../../amperity_reference/source/queries.rst
   :start-after: .. queries-add-via-sql-editor-steps-start
   :end-before: .. queries-add-via-sql-editor-steps-end


.. _stitch-qa-query-semantic-values:

Semantic values
--------------------------------------------------

.. stitch-qa-query-preprocessed-values-start

Use regular expressions to create additional fields based on semantic values and to clean up semantic values, as necessary.

.. stitch-qa-query-preprocessed-values-end

**To keep only alphabetical characters**

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-regexp-replace-example-keep-az09-from-string-start
   :end-before: .. sql-presto-function-regexp-replace-example-keep-az09-from-string-end

**To replace characters after + symbol**

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-regexp-replace-example-replace-characters-after-symbol-start
   :end-before: .. sql-presto-function-regexp-replace-example-replace-characters-after-symbol-end

**To keep characters before @ symbol**

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-regexp-replace-example-keep-characters-before-symbol-start
   :end-before: .. sql-presto-function-regexp-replace-example-keep-characters-before-symbol-end

**To keep characters after @ symbol**

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-regexp-replace-example-keep-characters-after-symbol-start
   :end-before: .. sql-presto-function-regexp-replace-example-keep-characters-after-symbol-end

**To clean up semantic values**

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-regexp-replace-example-clean-up-semantic-values-start
   :end-before: .. sql-presto-function-regexp-replace-example-clean-up-semantic-values-end


.. _segment-editor-sql-stitch-qa-queries:

Stitch QA queries
==================================================

.. segment-editor-sql-stitch-qa-queries-start

Use the following queries to build the initial Stitch QA database

* :doc:`Bad foreign keys <stitch_qa_bad_foreign_keys>`
* :doc:`Cluster scores <stitch_qa_cluster_scores>`
* :doc:`Cluster size distribution <stitch_qa_cluster_size_distribution>`
* :doc:`Common values <stitch_qa_common_values>`
* :doc:`Connections across sources <stitch_qa_connections_across_sources>`
* :doc:`Dedupe keys per Amperity ID <stitch_qa_dedupe_keys_per_amperity_id>`
* :doc:`Denormalized reports <stitch_qa_denormalized_records>`
* :doc:`Detailed examples <stitch_qa_detailed_examples>`
* :doc:`Foreign key validation <stitch_qa_fk_validation>`
* :doc:`Combined statistics <stitch_qa_combined_statistics>`
* :doc:`Separated statistics <stitch_qa_separated_statistics>`
* :doc:`Many Amperity IDs <stitch_qa_many_amperity_ids>`
* :doc:`Many semantic values <stitch_qa_many_semantic_values>`
* :doc:`NULL Amperity IDs <stitch_qa_null_amperity_ids>`
* :doc:`Source cluster distribution <stitch_qa_source_cluster_distribution>`
* :doc:`Split clusters <stitch_qa_split_clusters>`
* :doc:`Unmatched semantic values <stitch_qa_unmatched_semantic_values>`
* :doc:`Weakest match <stitch_qa_weakest_match>`

.. segment-editor-sql-stitch-qa-queries-end
