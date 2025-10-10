.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Use a sandbox to make configuration changes, and then validate them before promoting them to production.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use a sandbox to make configuration changes, and then validate them before promoting them to production.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure your tenant in a sandbox


==================================================
Configure your tenant
==================================================

.. sandbox-workflows-static-intro-start

Use a sandbox to safely make changes to your production tenant:

#. :doc:`Create a sandbox <sandbox_create>` before making configuration changes to your tenant.
#. Access the sandbox, and then make configuration changes to your tenant. Run the updated workflow from within the sandbox, run sandbox validations, and verify that your changes are ready for promotion.
#. :doc:`Promote configuration changes <sandbox_promote>` to your production tenant.

This is part two of a series of topics that describes how your brand can use sandboxes to safely make changes to your production tenant.

.. note:: Users who have been assigned the **DataGrid Operator** or **DataGrid Administrator** policies, and then assigned the **Allow sandbox administration** policy option, are allowed to create sandboxes and promote changes to production from a sandbox.

.. sandbox-workflows-static-intro-end

.. sandbox-promote-steps-start

The following sections describe the steps you will follow when working in a sandbox to make configuration state changes to production.

.. sandbox-promote-steps-end

.. sandbox-promote-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - To access a sandbox, from the list of sandboxes, select the |fa-kebab| icon, and then from the list of options select **Access sandbox**.

       .. image:: ../../images/mockups-sandbox-access.png
          :width: 600 px
          :alt: Access a sandbox from the Users and Activity page.
          :align: left
          :class: no-scaled-link

       .. important:: Data is not moved between production and a sandbox.

          Configuration state is copied from production, and then applied to the sandbox.

          Updates to configuration state in production are made available to the sandbox as updates.

          Configuration state changes in the sandbox are copied to production when they are promoted.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Sandbox configuration works the same way as it does in production with all of the same features and functionality. The main difference is that users in a sandbox are assigned the **DataGrid Administrator** policy, which gives them full access to the configuration state within the sandbox.

       When you access a sandbox, it will look much the same as production, but with a different color scheme.

       .. image:: ../../images/mockups-sandbox-generic-page.png
          :width: 600 px
          :alt: A sandbox has a slightly different color scheme and a unique banner.
          :align: left
          :class: no-scaled-link

       Amperity recommends to use a sandbox when making any configuration state change to your brand's production tenant, including:

       * Adding data sources
       * Building custom domain tables
       * Configuring courier groups
       * Adding tables to existing databases
       * Adding new databases
       * Testing out complex queries, and then optimizing those queries
       * Adding destinations or data templates to existing destinations
       * Validating end-to-end workflows
       * Adding new Profile API endpoints or updating existing endpoints


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Sandbox-specific notifications are built into the pages to help you identify the current configuration state of the sandbox as it relates to the configuration state in production. These appear near the top of each page. 

       A notification is shown when action is required to synchronize the configuration states between a sandbox and production. For example:

       .. image:: ../../images/mockups-sandbox-updates-available.png
          :width: 600 px
          :alt: You will be notified when updates are available for your sandbox.
          :align: left
          :class: no-scaled-link

       after which you can review the details for each update that may be available.

       .. image:: ../../images/mockups-sandbox-sync-with-production-pull.png
          :width: 600 px
          :alt: Review the details for each update.
          :align: left
          :class: no-scaled-link

       A list of changes appears under the **Added**, **Changed**, or **Removed** sections. Click the name of the update to learn more about the differences between the configuration states of your sandbox and production.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - A series of validations are run against updates. These validations will notify you within the sandbox when the configuration state of production and a sandbox conflict.

       Most of the time you should receive a validation report that does not contain a list of conflicts, similar to:

       .. image:: ../../images/mockups-sandbox-access-validations-pull.png
          :width: 600 px
          :alt: All validations passed.
          :align: left
          :class: no-scaled-link

       Occasionally, you will receive a validation report that shows one or more validation errors. For example, a schema mismatch between a custom domain table in production and a custom domain table in the sandbox:

       .. image:: ../../images/mockups-sandbox-access-validations-errors.png
          :width: 600 px
          :alt: Some validations passed. Schema error.
          :align: left
          :class: no-scaled-link

       If you receive a validation report with errors, investigate each error and work to resolve the underlying issue. It is possible that resolution must be done in production before pulling those updates to the sandbox. It is also possible that the resolution is done in the sandbox. It depends on the validation issue.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - When there are updates that can be pulled to your sandbox from production you will be notified, after which you can review the validations and each of the updates. Click the **Pull** button in the top-right of the page to pull the updates to your sandbox.

       .. image:: ../../images/mockups-sandbox-access-pull-updates.png
          :width: 600 px
          :alt: Pull updates from production to a sandbox.
          :align: left
          :class: no-scaled-link


.. sandbox-promote-callouts-end
