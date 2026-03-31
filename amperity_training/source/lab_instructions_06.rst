.. https://docs.amperity.com/reference/


==================================================
Lab 06: Using workflows
==================================================

A workflow is the series of steps that your data follows as it moves through Amperity. Information about a workflow, including details and individual tasks, is available from the Workflows page. In this lab, you will see workflows in action.

.. admonition:: Reference Materials

   * `About scheduled workflows <../operator/workflows.html>`__ |ext_link|
   * `About Workflows page <../reference/workflows.html>`__ |ext_link|


Objective
==================================================

In this lab you will set up a workflow to gain a deeper understanding of the parts of workflows work in Amperity.


Configure a workflow
==================================================

#. Log into your production training tenant at https://app.amperity.com

#. Navigate to the Settings page and locate the Sandboxes subtab on this page.

#. Create a new sandbox using the following information:

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - Amperity field name
        - Value to enter
      * - **Sandbox Name**
        - TET-YourName-Lab4-SB
      * - **Sandbox Description**
        - A sandbox to create workflows

#. Use the tenant drop-down or the actions menu or the go to sandbox button to switch to the sandbox you just created.

#. Ensure you are in the Sandbox training tenant. Sandbox tenants utilize the teal blue navigation color scheme. Sandboxes also display the sandbox status banner. You can quickly switch between tenants by clicking on the tenant selection menu in the top-right corner of the screen.

   .. image:: /_images/ex06_switch_to_sandbox.png
      :width: 400 px
      :alt: Switch to sandbox
      :align: left
      :class: no-scaled-link

#. Navigate to the **Destinations** page, select the **Destinations** subtab, and click on **New destination** and select **For orchestrations**.

   .. image:: /_images/ex06_new_destination.png
      :width: 500 px
      :alt: New destination
      :align: left
      :class: no-scaled-link

#. Select **SFTP** plugin.

   .. image:: /_images/ex06_select_sftp.png
      :width: 380 px
      :alt: SFTP plugin
      :align: left
      :class: no-scaled-link

#. In the **Credential** dropdown, select **Create new credential**.

   .. image:: /_images/ex06_create_credential.png
      :width: 400 px
      :alt: Create new credential
      :align: left
      :class: no-scaled-link

#. In the form that appears fill in the following fields and click **Continue**.

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - Amperity field name
        - Value to enter
      * - **Name**
        - Amperity SFTP
      * - **Hostname**
        - sftp.amperity.com
      * - **Username**
        - training
      * - **Passphrase**
        - Bootcamp4all

   .. image:: /_images/ex06_sftp_credential.png
      :width: 400 px
      :alt: SFTP credential form
      :align: left
      :class: no-scaled-link

#. In the **Configure destination** dialog that comes up, fill in the following fields and click **Save**.

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - Amperity field name
        - Value to enter
      * - **Name**
        - Analytics SFTP
      * - **Remote folder**
        - /training/destination_output
      * - **File format**
        - CSV

   .. image:: /_images/ex06_sftp_destination_settings.png
      :width: 400 px
      :alt: Configure destination
      :align: left
      :class: no-scaled-link

#. Navigate to the **Activations** page, select the **Orchestrations** subtab, and click on **Add orchestration**.

   .. image:: /_images/ex06_add_orchestration.png
      :width: 400 px
      :alt: Add orchestration
      :align: left
      :class: no-scaled-link

#. In the **Add orchestration** dialog that comes up fill in the following fields and click **Save**.

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - Amperity field name
        - Value to enter
      * - **Object type**
        - Query
      * - **Object**
        - Most popular product
      * - **Destination**
        - Analytics SFTP
      * - **Filename template**
        - <Student_Name>_Most_popular_product_({now|format:'yyyy-MM-dd)).csv
      * - **Workflow option**
        - Manual

   .. image:: /_images/ex06_add_orchestration_dialog.png
      :width: 400 px
      :alt: Add orchestration dialog
      :align: left
      :class: no-scaled-link

#. Navigate to the **Sources** page and click on the **Actions** kebab menu |fa-kebab| to the right of the **Courier group Daily** and select **Edit**.

   .. image:: /_images/ex06_edit_courier_group.png
      :width: 500 px
      :alt: Edit Courier group
      :align: left
      :class: no-scaled-link

#. Set the **Schedule** cron for 8 am daily Pacific time and set the courier group to **Active** and then click **Save**.

   .. image:: /_images/ex06_schedule_cron.png
      :width: 400 px
      :alt: Schedule Courier group
      :align: left
      :class: no-scaled-link

#. Navigate to the **Activations** page, select the **Orchestrations** subtab, and click on **Add orchestration group**.

   .. image:: /_images/ex06_add_orchestration_group.png
      :width: 500 px
      :alt: Add orchestration group
      :align: left
      :class: no-scaled-link

#. In the **Add orchestration group** dialog that comes up set the **Name** to "Daily". Select **Run options** to **Run after courier group Daily** and click **Save**.

   .. image:: /_images/ex06_run_after_courier_group.png
      :width: 400 px
      :alt: Add orchestration group dialog
      :align: left
      :class: no-scaled-link

#. Click on the **Actions** kebab menu |fa-kebab| to the right of the **Orchestration** named "Most popular product" and select **Edit**.

   .. image:: /_images/ex06_edit_orchestration.png
      :width: 500 px
      :alt: Edit orchestration>
      :align: left
      :class: no-scaled-link

#. Set the Workflow options to **Automatic**, select the **Daily Orchestration** group, and then click **Save**.

   .. image:: /_images/ex06_set_workflow_options.png
      :width: 400 px
      :alt: Set workflow options
      :align: left
      :class: no-scaled-link


This completes Exercise #6: Using Workflows in Amperity. In a live production tenant, the next step is to verify the workflow and promote it to the production tenant.