.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Configure and manage the Stitch Scores table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Stitch Scores table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Stitch Scores table

==================================================
Stitch Scores table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-stitch-scores-table-start
   :end-before: .. term-stitch-scores-table-end


.. _table-stitch-scores-use-with-stitch-qa:

Use with Stitch QA
==================================================

.. table-stitch-scores-use-with-stitch-qa-start

Use the **Stitch Scores** table to understand why blocking used (or did not use) a foreign key or separation key to block (or unblock) two records.

.. table-stitch-scores-use-with-stitch-qa-end


.. _table-stitch-scores-use-with-stitch-qa-compare-records:

Compare records
--------------------------------------------------

.. table-stitch-scores-use-with-stitch-qa-compare-records-start

Use a query similar to the following to compare scores for two records:

.. code-block:: sql

   SELECT * FROM Stitch_Scores
   WHERE source1 = 'Table_Name' AND pk1 = '123abc456def'
   AND source2 = 'Table_Name' AND pk1 = '789ghi012jkl'

where the values of **pk1** and **pk2** are for the records you want to compare.

.. table-stitch-scores-use-with-stitch-qa-compare-records-end


.. _table-stitch-scores-add-table:

Add table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-passthrough-360-table-start
   :end-before: .. term-passthrough-360-table-end

**To add the Stitch Scores table**

.. table-stitch-scores-add-steps-start

#. From the **Database Editor**, click **Add Table**.
#. Name the table "Stitch_Scores".
#. Set the build mode to **Passthrough**, and then select **Stitch Scores**.
#. Hide the table from the **Segment Editor** by verifying that **Show in VSE?** is unselected.
#. Click **Activate** to update the customer 360 database with your changes.

.. table-stitch-scores-add-steps-end


.. _table-stitch-scores-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-stitch-scores-table-about-start
   :end-before: .. data-tables-stitch-scores-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-stitch-scores-table-start
   :end-before: .. data-tables-stitch-scores-table-end
