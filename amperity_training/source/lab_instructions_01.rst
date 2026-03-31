.. https://docs.amperity.com/reference/


==================================================
Lab 01: Creating sandboxes
==================================================

Sandboxes are short-lived and deleted when changes are promoted. Before you can make any changes in the sandbox, you must pull these changes from the production environment into the sandbox so that you can fully test the changes you are about to make.

.. admonition:: Reference Materials

   * `About Sandboxes <../reference/sandboxes.html>`__ |ext_link|


Objective
==================================================

Sandbox tenants are used to safely make configuration changes, test those changes, and then promote the changes back to a production tenant. Acting as the tenant sandbox administrator, in this exercise you will create a sandbox and in the next section you will use the sandbox to make changes to the production tenant.


Create a new sandbox
==================================================

#. Log in to your production training tenant at https://app.amperity.com
#. Navigate to the **Settings** page and locate the **Sandboxes** subtab on this page.
#. Create a new sandbox using the following information:

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - Amperity field name
        - Value to enter
      * - **Sandbox Name**
        - TET-YourName-Lab2-SB
      * - **Sandbox Description**
        - A sandbox to enhance customer PII data

#. Use the tenant drop-down or the actions menu or the **Go to sandbox** button to switch to the sandbox you just created.

#. Ensure you are in the Sandbox training tenant. Sandbox tenants utilize the teal blue navigation color scheme. Sandboxes also display the sandbox status banner. You can quickly switch between tenants by clicking on the tenant selection menu in the top-right corner of the screen.

   .. image:: /_images/ex01_create_sandbox_button.png
      :width: 300 px
      :alt: Create sandbox button
      :align: left
      :class: no-scaled-link
