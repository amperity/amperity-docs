.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Export one (or more) tables or an entire database from Amperity to support any downstream workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        Export one (or more) tables or an entire database from Amperity to support any downstream workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        About data exports

==================================================
About data exports
==================================================

.. data-exports-start

A database may be configured to export one (or more) tables or an entire database from Amperity. Each data export must be assigned a unique name. A data export must be associated with a configured destination and must be added to an orchestration.

.. data-exports-end

.. data-exports-policy-start

.. admonition:: Policies required to run data exports from a sandbox

   A data export must be configured within a sandbox by a user who is assigned to the **DataGrid Administrator** policy, after which users assigned to the **DataGrid Operator** and **Amp360 User** policies may add the data export to orchestrations.

.. data-exports-policy-start

.. data-exports-policy-links-start

This topic describes tasks related to managing data exports in Amperity:

#. :ref:`data-exports-add`
#. :ref:`data-exports-add-tables`
#. :ref:`data-exports-add-to-orchestration`
#. :ref:`data-exports-delete`
#. :ref:`data-exports-discard`
#. :ref:`data-exports-switch`
#. :ref:`data-exports-remove-table`
#. :ref:`data-exports-view`

.. data-exports-policy-links-end


.. _data-exports-add:

Add data export
==================================================

.. data-exports-add-start

Database tables and databases can be sent from Amperity as a data export. A data export is configured from the **Customer 360** page, and then added to an orchestration from the **Destinations** page.

.. data-exports-add-end

**To add a data export**

.. data-exports-add-steps-start

#. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
#. Click **Create New Export**. This opens the **Add Export** dialog box.
#. Add the name of the data export, and then click **Add**. This will add a draft data export to the **Database Exports** page.
#. Open the menu for the draft data export, and then select **Edit**.
#. From the **Database** dropdown, select a database.
#. From the **Entities** list, select one (or more) database tables to add to the data export.
#. Click **Activate**.

.. data-exports-add-steps-end


.. _data-exports-add-tables:

Add table export
==================================================

.. data-exports-add-tables-start

Tables may be added to an existing data export.

.. data-exports-add-tables-end

**To add tables to a data export**

.. data-exports-add-tables-steps-start

#. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
#. Open the menu for a data export, and then select **Edit**.
#. From the **Entities** list, select one (or more) database tables to add to the data export.

   For a single table, click the table. For multiple tables, use click + command for each table to be selected. For all tables click the first table, hold shift, and then click the last table.

#. Click **Activate**.

.. data-exports-add-tables-steps-end


.. _data-exports-add-to-orchestration:

Add to orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add a data export to an orchestration**

.. data-exports-add-to-orchestration-steps-start

#. From the **Destinations** page click **Add Orchestration**. This opens the **Add Orchestration** dialog box.
#. From the **Object Type** dropdown, select **Database Export**.
#. Select a destination and complete the rest of the orchestration settings.
#. Click **Save**.

.. data-exports-add-to-orchestration-steps-end


.. _data-exports-delete:

Delete data export
==================================================

.. data-exports-delete-start

Use the **Delete** option to remove a data export from Amperity. This should be done carefully. Verify that both upstream and downstream processes no longer depend on this orchestration prior to deleting it. This action will *not* delete the data template or destination associated with the orchestration.

.. data-exports-delete-end

**To delete a data export**

.. data-exports-delete-steps-start

#. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
#. Open the menu for a data export, and then select **Delete**.
#. Click **Delete** to confirm.

.. data-exports-delete-steps-end


.. _data-exports-discard:

Discard data export
==================================================

.. data-exports-discard-start

A draft data export may be discarded.

.. data-exports-discard-end

**To discard a draft data export**

.. data-exports-discard-steps-start

#. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
#. Open the menu for a draft data export, and then select **Discard**.

.. data-exports-discard-steps-end


.. _data-exports-switch:

Switch database
==================================================

.. data-exports-switch-start

The database associated with a data export may be switched to any other database that is available from the **Customer 360** page.

.. data-exports-switch-end

**To switch databases**

.. data-exports-edit-steps-start

#. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
#. Open the menu for a data export, and then select **Edit**.
#. From the **Databases** dropdown menu, pick another database.
#. From the **Entities** list, select one (or more) database tables to add to the data export.

   For a single table, click the table. For multiple tables, use click + command for each table to be selected. For all tables click the first table, hold shift, and then click the last table.

#. Click **Activate**.

.. data-exports-edit-steps-end


.. _data-exports-remove-table:

Remove table
==================================================

.. data-exports-remove-tables-start

A table may be removed from an existing data export.

.. data-exports-remove-tables-end

**To remove a table from a data export**

.. data-exports-remove-tables-steps-start

#. From the **Customer 360** page click **Configure Exports**. This opens the **Database Exports** page.
#. Open the menu for a data export, and then select **Edit**.
#. From the **Entities** list, select one (or more) database tables to remove from the data export.

   For a single table, click the table. For multiple tables, use click + command for each table to be selected. For all tables click the first table, hold shift, and then click the last table.

#. Click **Activate**.

.. data-exports-remove-tables-steps-end


.. _data-exports-view:

View data exports
==================================================

.. destinations-orchestration-manage-view-start

The **Database Exports** page shows the status of every data export. This page is accessible from the **Configure Exports** link on the **Customer 360** page.

.. destinations-orchestration-manage-view-end
