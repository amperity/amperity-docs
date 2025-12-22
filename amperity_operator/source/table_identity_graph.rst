.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Identity Graph table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Identity Graph table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Identity Graph table

==================================================
Identity Graph table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-identity-graph-start
   :end-before: .. term-identity-graph-end

.. table-identity-graph-about-start

The **Identity Graph** table compiles rows in the **Unified Coalesced** table into a graph that maps each data source, along with the primary key for that data source and any customer keys, to the Amperity ID.

.. table-identity-graph-about-end


.. _table-identity-graph-add:

Add table
==================================================

.. table-fiscal-calendar-add-start

The **Identity Graph** table is generated as stitched output when your tenant starts with `Guided setup <../guided/index.html>` and is an optional SQL table for all other customer 360 databases.

.. table-fiscal-calendar-add-end

**To add the Identity Graph table**

.. table-fiscal-calendar-add-steps-start

#. From the **Customer 360** page, select the **Databases** tab, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Identity_Graph".
#. Set the build mode to **SQL**.
#. Add the following SQL:

   .. code-block:: sql

      SELECT
        amperity_id
        ,datasource
        ,COALESCE(ck,pk) AS customer_key
      FROM Unified_Coalesced

#. Click **Validate**, and then click **Next**.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Do not make the table available to the visual **Segment Editor**.
#. From the **Table Semantics** dropdown, select **Identity Graph**.
#. Under **Version History**, select **Enable table version history**.
#. Click **Save**.

.. table-identity-graph-add-steps-end


.. _table-identity-graph-reference:

Column reference
==================================================

.. table-identity-graph-reference-start

The **Identity Graph** table contains the following columns.

.. table-identity-graph-reference-end

.. table-identity-graph-reference-columns-start

.. list-table::
   :widths: 200 100 300
   :header-rows: 1

   * - Column Name
     - Data type
     - Description
   * - **Amperity ID**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amperity-id-column-start
          :end-before: .. term-amperity-id-column-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-amperity-id-format-start
          :end-before: .. term-amperity-id-format-end

   * - **Datasource**
     - String
     - The name of the source data table.

   * - **Customer Key**
     - String
     - The primary key and all customer keys from a data source coalesced into a single value.

.. table-identity-graph-reference-columns-end
