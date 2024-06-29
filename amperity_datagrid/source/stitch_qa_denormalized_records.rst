.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Troubleshoot Stitch results by reviewing denormalized records.

.. meta::
    :content class=swiftype name=body data-type=text:
        Troubleshoot Stitch results by reviewing denormalized records.

.. meta::
    :content class=swiftype name=title data-type=string:
        Denormalized records

==================================================
Denormalized records
==================================================

.. stitch-qa-query-denormalized-records-start

Use this query to look for foreign key clusters with large row expansions for denormalized records. This query performs 3x3x3 or 5x5x5 denormalization with a maximum of five rows that contain columns for email, phone, and address values and provides a condensed option for examining PII values.

.. stitch-qa-query-denormalized-records-end


.. _stitch-qa-query-denormalized-records-steps:

Configure query
==================================================

.. stitch-qa-query-denormalized-records-steps-start

#. From the **Queries** page, open the **Stitch QA** folder, and then select this query.

   .. tip:: :ref:`Add the Stitch QA queries template folder <qa-stitch-enable-steps-add-queries>` if it does not already exist.

#. Update the **uc_filter_query** to the desired threshold, which is currently set to "50".
#. Click **Run Query** and debug any issues that may arise.
#. Click **Activate**.

.. stitch-qa-query-denormalized-records-steps-end
