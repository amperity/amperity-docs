.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Configure and manage the Stitch BlocklistValues table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Stitch BlocklistValues table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Stitch BlocklistValues table

==================================================
Stitch BlocklistValues table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-stitch-blocklistvalues-table-start
   :end-before: .. term-stitch-blocklistvalues-table-end


.. _table-stitch-blocklistvalues-add:

Add table
==================================================

.. table-stitch-blocklistvalues-add-start

.. important:: This table cannot be added to the Stitch QA database until after the :doc:`bad-values blocklist has been configured <blocklist_bad_values>`.

.. table-stitch-blocklistvalues-add-end

**To add the Stitch BlocklistValues table**

.. table-stitch-blocklistvalues-add-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the Stitch QA database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Stitch_BlocklistValues".
#. Set the build mode to **Passthrough**.
#. From the **Source Table** drop-down, select the table associated with the bad-values blocklist.
#. Click **Next**.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Leave everything else unchanged.
#. Click **Save**.
#. Activate, and then run the Stitch QA database.

.. table-stitch-blocklistvalues-add-steps-end


.. _table-stitch-blocklistvalues-reference:

Column reference
==================================================

.. table-stitch-blocklistvalues-reference-start

.. list-table::
   :widths: 150 50 400
   :header-rows: 1

   * - Column Name
     - Data type
     - Description
   * - **datasource**
     - String
     - The data source in which the value was blocklisted.
   * - **semantic**
     - String
     - The semantic tag associated with the blocklisted value.
   * - **value**
     - String
     - The value that was blocklisted.

.. table-stitch-blocklistvalues-reference-end
