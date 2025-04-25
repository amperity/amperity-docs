.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use custom domain tables to shape data after it has been pulled to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use custom domain tables to shape data after it has been pulled to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        About custom domain tables

==================================================
About custom domain tables
==================================================

.. include:: ../../amperity_reference/source/domain_tables.rst
   :start-after: .. domain-tables-custom-intro-start
   :end-before: .. domain-tables-custom-intro-end

.. domain-tables-custom-links-start

These semantic tags generate the :doc:`Unified Itemized Transactions <table_unified_itemized_transactions>` table, which is then used as the underlying reference for the :doc:`Unified Transactions <table_unified_transactions>` and :doc:`Transaction Attributes Extended <table_transaction_attributes_extended>` tables.

.. domain-tables-custom-links-end

.. include:: ../../amperity_reference/source/domain_tables.rst
   :start-after: .. domain-tables-custom-may-reference-start
   :end-before: .. domain-tables-custom-may-reference-end

.. include:: ../../amperity_reference/source/domain_tables.rst
   :start-after: .. domain-tables-custom-note-start
   :end-before: .. domain-tables-custom-note-end


.. _custom-domain-tables-custom-domain-sql:

Domain SQL
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-domain-sql-start
   :end-before: .. term-domain-sql-end


.. _custom-domain-tables-run-history:

Custom Domain Table Run History
--------------------------------------------------

.. custom-domain-tables-run-history-start

Within the custom domain table run history allows you to see timeline information about custom domain tables that have been run, as well s the outcome of each table (whether it was succeeded, reused, or failed). 

You can view the run history for custom domain tables by clicking on **View run history** from the |fa-kebab| menu from any custom domain table or from the **View run history** link for any custom domain table cards within **Recent Activity**.

.. custom-domain-tables-run-history-end


.. _custom-domain-tables-custom-sql-use-cases:

Use cases
--------------------------------------------------

.. custom-domain-tables-custom-sql-use-cases-start

The following examples describe some of the more common uses cases for domain SQL:

* :ref:`custom-domain-tables-combine-birthdate`
* :ref:`custom-domain-tables-combine-postal`
* :ref:`custom-domain-tables-extract-names`
* :ref:`custom-domain-tables-rehash-data`
* :ref:`custom-domain-tables-parse-fields-with-multiple-separators`
* :ref:`custom-domain-tables-set-email-to-null`
* :ref:`custom-domain-tables-standardize-values-for-usa-states`
* :ref:`custom-domain-tables-update-blocklists`

.. note:: These examples are not meant to be copied and pasted, but they should work for most tenants as a good starting point.

.. custom-domain-tables-custom-sql-use-cases-end


.. _custom-domain-tables-combine-birthdate:

Combine day, month, year as birthdate
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/domain_tables.rst
   :start-after: .. domain-tables-custom-sql-use-case-combine-birthdate-start
   :end-before: .. domain-tables-custom-sql-use-case-combine-birthdate-end


.. _custom-domain-tables-combine-postal:

Combine five- and four-digit postal codes
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-concat-ws-example-combine-postal-codes-start
   :end-before: .. sql-spark-function-concat-ws-example-combine-postal-codes-end


.. _custom-domain-tables-extract-names:

Extract first and last names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-regexp-extract-example-names-start
   :end-before: .. sql-spark-function-regexp-extract-example-names-end


.. _custom-domain-tables-rehash-data:

Hash PII data that has been resent to Amperity
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-sha2-example-rehash-data-start
   :end-before: .. sql-spark-function-sha2-example-rehash-data-end


.. _custom-domain-tables-parse-fields-with-multiple-separators:

Parse fields with multiple separators
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-split-example-parse-fields-with-multiple-separators-start
   :end-before: .. sql-spark-function-split-example-parse-fields-with-multiple-separators-end


.. _custom-domain-tables-reference-custom:

Reference custom domain tables
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/domain_tables.rst
   :start-after: .. domain-tables-custom-sql-use-reference-custom-domain-table-start
   :end-before: .. domain-tables-custom-sql-use-reference-custom-domain-table-end


.. _custom-domain-tables-set-email-to-null:

Set non-US-ASCII email addresses to NULL
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-decode-example-identify-non-us-ascii-email-start
   :end-before: .. sql-spark-function-decode-example-identify-non-us-ascii-email-end


.. _custom-domain-tables-standardize-values-for-usa-states:

Standardize values for USA states
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-function-coalesce-example-standardize-values-for-usa-states-start
   :end-before: .. sql-spark-function-coalesce-example-standardize-values-for-usa-states-end


.. _custom-domain-tables-update-blocklists:

Update blocklists
--------------------------------------------------

.. include:: ../../amperity_operator/source/blocklist_bad_values.rst
   :start-after: .. bad-values-blocklist-advanced-custom-domain-tables-start
   :end-before: .. bad-values-blocklist-advanced-custom-domain-tables-end
