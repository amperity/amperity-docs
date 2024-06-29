.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by finding records with NULL Amperity IDs.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by finding records with NULL Amperity IDs.

.. meta::
    :content class=swiftype name=title data-type=string:
        Null Amperity IDs

==================================================
NULL Amperity IDs
==================================================

.. stitch-qa-query-null-amperity-ids-start

Use this query to discover if **NULL** Amperity IDs are present in your customer 360 database.

.. important:: The number of **NULL** Amperity IDs that should be present is zero.
 
.. stitch-qa-query-null-amperity-ids-end


.. _stitch-qa-query-null-amperity-ids-use:

When to use
==================================================

.. stitch-qa-query-null-amperity-ids-use-start

#. Run this query on a regular basis.
#. If any records are returned, investigate why those records returned with **NULL** Amperity IDs.

.. stitch-qa-query-null-amperity-ids-use-end


.. _stitch-qa-query-null-amperity-ids-steps:

Configure query
==================================================

.. stitch-qa-query-null-amperity-ids-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Click **Run Query** and debug any issues that may arise. This query should return 0.
#. Click **Activate**.

.. stitch-qa-query-null-amperity-ids-steps-end
