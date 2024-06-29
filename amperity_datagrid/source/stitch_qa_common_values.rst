.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing common values across semantics.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing common values across semantics.

.. meta::
    :content class=swiftype name=title data-type=string:
        Common values

==================================================
Common values
==================================================

.. stitch-qa-query-common-values-start

Use this query to return common values across semantics in a single view that shows cardinality for semantic values and shows the context for values that occur across multiple records and clusters.

.. stitch-qa-query-common-values-end


.. _stitch-qa-query-common-values-use:

When to use
==================================================

.. stitch-qa-query-common-values-use-start

#. Run this query to display common values.
#. Review the top results and investigate records to identify trends (~30 minutes).
#. For each common value, attempt to identify why it has so many records associated with it. For example, is it a company email address? A business address?
#. Review all associated records to ensure that records associated with it are clustered or split appropriately.
#. Identify if any values should be added to the :doc:`bad-values blocklist <blocklist_bad_values>`.
#. If anomalies are present, investigate each cluster individually.

.. stitch-qa-query-common-values-use-end
