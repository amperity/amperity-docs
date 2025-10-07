.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Export one or more tables or an entire database from Amperity to support any downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        Export one or more tables or an entire database from Amperity to support any downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        About data exports

==================================================
About data exports
==================================================

.. data-exports-start

A database may be configured to export one or more tables or an entire database from Amperity. Each data export must be assigned a unique name. A data export must be associated with a configured destination and must be added to an orchestration.

.. data-exports-end

.. data-exports-policy-start

.. admonition:: Policies required to run data exports from a sandbox

   A data export must be configured within a sandbox by a user who is assigned to the **DataGrid Administrator** policy, after which users assigned to the **DataGrid Operator** and **Amp360 User** policies may add the data export to orchestrations.

.. data-exports-policy-start


.. _data-exports-howtos:

How-tos
==================================================


.. _data-exports-add:

.. dropdown:: Add data export
   :icon: code

   Database tables and databases can be sent from Amperity as a data export. A data export is configured from the **Customer 360** page, and then added to an orchestration from the **Destinations** page.

   **To add a data export**

   #. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
   #. Click **Create New Export**. This opens the **Add Export** dialog box.
   #. Add the name of the data export, and then click **Add**. This adds a draft data export to the **Database Exports** page.
   #. Open the menu for the draft data export, and then select **Edit**.
   #. From the **Database** dropdown, select a database.
   #. From the **Entities** list, select one or more database tables to add to the data export.
   #. Click **Activate**.




.. _data-exports-add-tables:

.. dropdown:: Add table export
   :icon: code

   Tables may be added to an existing data export.

   **To add tables to a data export**

   #. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
   #. Open the menu for a data export, and then select **Edit**.
   #. From the **Entities** list, select one or more database tables to add to the data export.

      For a single table, click the table. For multiple tables, use click + command for each table to be selected. For all tables click the first table, hold shift, and then click the last table.

   #. Click **Activate**.




.. _data-exports-add-to-orchestration:

.. dropdown:: Add to orchestration
   :icon: code

   .. include:: ../../shared/terms.rst
      :start-after: .. term-orchestration-start
      :end-before: .. term-orchestration-end

   **To add a data export to an orchestration**

   #. From the **Destinations** page click **Add Orchestration**. This opens the **Add Orchestration** dialog box.
   #. From the **Object Type** dropdown, select **Database Export**.
   #. Select a destination and complete the rest of the orchestration settings.
   #. Click **Save**.




.. _data-exports-delete:

.. dropdown:: Delete data export
   :icon: code

   Use the **Delete** option to remove a data export from Amperity. Verify that both upstream and downstream processes no longer depend on this orchestration prior to deleting it. This action will *not* delete the data template or destination associated with the orchestration.

   **To delete a data export**

   #. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
   #. Open the menu for a data export, and then select **Delete**.
   #. Click **Delete** to confirm.




.. _data-exports-discard:

.. dropdown:: Discard data export
   :icon: code

   A draft data export may be discarded.

   **To discard a draft data export**

   #. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
   #. Open the menu for a draft data export, and then select **Discard**.




.. _data-exports-switch:

.. dropdown:: Switch database
   :icon: code

   The database associated with a data export may be switched to any other database that is available from the **Customer 360** page.

   **To switch databases**

   #. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
   #. Open the menu for a data export, and then select **Edit**.
   #. From the **Databases** dropdown menu, pick another database.
   #. From the **Entities** list, select one or more database tables to add to the data export.

      For a single table, click the table. For multiple tables, use click + command for each table to be selected. For all tables click the first table, hold shift, and then click the last table.

   #. Click **Activate**.




.. _data-exports-remove-table:

.. dropdown:: Remove table
   :icon: code

   A table may be removed from an existing data export.

   **To remove a table from a data export**

   #. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
   #. Open the menu for a data export, and then select **Edit**.
   #. From the **Entities** list, select one or more database tables to remove from the data export.

      For a single table, click the table. For multiple tables, use click + command for each table to be selected. For all tables click the first table, hold shift, and then click the last table.

   #. Click **Activate**.




.. _data-exports-view:

.. dropdown:: View data exports
   :icon: code

   The **Database Exports** page shows the status of every data export. This page is accessible from the **Configure Exports** link on the **Customer 360** page.

