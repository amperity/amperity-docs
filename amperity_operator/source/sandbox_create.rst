.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Create a sandbox, and then safely make configuration changes to your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Create a sandbox, and then safely make configuration changes to your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        Create a sandbox

==================================================
Create a sandbox
==================================================

.. sandbox-workflows-static-intro-start

Use a sandbox to safely make changes to your production tenant:

#. Create a sandbox before making configuration changes to your tenant.
#. :doc:`Access the sandbox <sandbox_open>`, and then make configuration changes to your tenant. Run the updated workflow from within the sandbox, run sandbox validations, and verify that your changes are ready for promotion.
#. :doc:`Promote configuration changes <sandbox_promote>` to your production tenant.

This is part one of a series of topics that describes how your brand can use sandboxes to safely make changes to your production tenant.

.. note:: Users who have been assigned the **DataGrid Operator** or **DataGrid Administrator** policies, and then assigned the **Allow sandbox administration** policy option, are allowed to create sandboxes and promote changes to production from a sandbox.

.. sandbox-workflows-static-intro-end

.. sandbox-promote-steps-start

The following sections describe the steps you will follow when creating a sandbox to make configuration state changes to production.

.. sandbox-promote-steps-end

.. sandbox-promote-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Sandboxes are created from the **Settings** page. Open the **Sandboxes** tab, and then click **Create sandbox**.

       .. image:: ../../images/mockups-sandbox-create.png
          :width: 600 px
          :alt: Create a sandbox for your tenant.
          :align: left
          :class: no-scaled-link

       .. tip:: Use a sandbox to make specific configuration state changes to production.

          Validate these changes within the sandbox, including running the full end-to-end workflow to validate any dependencies or requirements that exist upstream or downstream of Amperity. When these changes are ready, promote them to production.

          Use a dedicated sandbox for each type iterative change. For example:

          * A new data source in sandbox A
          * A new destination in sandbox B
          * Changes to a profile API endpoint in sandbox C
          * A set of custom database tables in sandbox D

          Each sandbox should exist only to support a specific set of planned configuration state changes. After these changes are promoted to production, the sandbox should be deleted.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Each sandbox should be given a name that identifies the type of configuration state change that will be made in that sandbox, along with an expanded description of those changes. Click **Create** to generate the sandbox for your tenant.

       .. image:: ../../images/mockups-sandbox-create-dialog.png
          :width: 450 px
          :alt: Add a name and description for your sandbox.
          :align: left
          :class: no-scaled-link

       .. note:: The name of a sandbox may have up to 64 characters. The description for a sandbox may have up to 512 characters.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - You can view details about this sandbox. From the list of sandboxes, select the |fa-kebab| icon, and then from the list of options select **Details**.

       .. image:: ../../images/mockups-sandbox-details.png
          :width: 600 px
          :alt: View sandbox details
          :align: left
          :class: no-scaled-link

       This opens a dialog box that shows details for the sandbox, including:

       * The date and time at which it was created
       * The URL of the sandbox
       * The last time a workflow ran in this sandbox
       * What configuration state changes are ready for promotion to production
       * What updates are ready to be pulled from production to the sandbox

       .. tip:: A sandbox that has not run recently--for example, within the previous two weeks--should be accessed and then evaluated. If the changes in the sandbox are not candidates for promotion your brand should consider deleting the sandbox.


.. sandbox-promote-callouts-end
