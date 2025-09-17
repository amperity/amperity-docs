.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Promote configuration changes made in a sandbox to production.

.. meta::
    :content class=swiftype name=body data-type=text:
        Promote configuration changes made in a sandbox to production.

.. meta::
    :content class=swiftype name=title data-type=string:
        Promote configuration changes to production


==================================================
Promote sandbox updates
==================================================

.. sandbox-workflows-static-intro-start

Use a sandbox to safely make changes to your production tenant:

#. :doc:`Create a sandbox <sandbox_create>` before making configuration changes to your tenant.
#. :doc:`Access the sandbox <sandbox_open>`, and then make configuration changes to your tenant. Run the updated workflow from within the sandbox, run sandbox validations, and verify that your changes are ready for promotion.
#. Promote configuration changes to your production tenant.

   .. tip::

      .. include:: ../../amperity_reference/source/sandboxes.rst
         :start-after: .. sandboxes-best-practice-delete-on-promote-start
         :end-before: .. sandboxes-best-practice-delete-on-promote-end

This is part three of a series of topics that describes how your brand can use sandboxes to safely make changes to your production tenant.

.. note:: Users who have been assigned the **DataGrid Operator** or **DataGrid Administrator** policies, and then assigned the **Allow sandbox administration** policy option, are allowed to create sandboxes and promote changes to production from a sandbox.

.. sandbox-workflows-static-intro-end

.. sandbox-promote-steps-start

The following sections describe the steps you'll follow when promoting changes in a sandbox to production.

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
     - Open the sandbox from which you want to promote configuration state changes.

       .. image:: ../../images/mockups-sandbox-access.png
          :width: 600 px
          :alt: Access a sandbox that is ready to promote changes.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - A series of validations are run against updates. These validations will notify you within the sandbox when the configuration states of production and sandbox conflict.

       Most of the time you should receive a validation report that does not contain a list of conflicts, similar to:

       .. image:: ../../images/mockups-sandbox-access-validations-pull.png
          :width: 380 px
          :alt: All validations passed.
          :align: left
          :class: no-scaled-link

       Occasionally, you will receive a validation report that shows one or more validation errors. For example, a schema mismatch between a custom domain table in production and a custom domain table in the sandbox:

       .. image:: ../../images/mockups-sandbox-access-validations-errors.png
          :width: 380 px
          :alt: Some validations passed, but there is a schema error.
          :align: left
          :class: no-scaled-link

       If you receive a validation report with errors, investigate each error and work to resolve the underlying issue. It is possible that resolution must be done in the production tenant before pulling updates to the sandbox. It is also possible that the resolution is done in the sandbox. It depends on the error.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - When configuration state changes in a sandbox are ready for promotion to production, the sandbox-specific notifications provides a link named "Ready to promote".

       .. image:: ../../images/mockups-sandbox-sync-with-production-promote.png
          :width: 600 px
          :alt: Review the details for each update.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Review the list of **Added**, **Changed**, or **Removed** configuration state changes. Click the name of the added, changed, or removed object to review the details for the configuration state change.

       Resolve validation issues, as necessary.

       .. image:: ../../images/mockups-sandbox-access-validations-promote.png
          :width: 600 px
          :alt: Review the details for each update.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - Enter a merge message for this set of configuration state changes.

       .. image:: ../../images/mockups-sandbox-access-validations-merge-message.png
          :width: 600 px
          :alt: Review the details for each update.
          :align: left
          :class: no-scaled-link

       When the sandbox is ready to be promoted, click **Promote**.

       .. tip::

          .. include:: ../../amperity_reference/source/sandboxes.rst
             :start-after: .. sandboxes-best-practice-delete-on-promote-start
             :end-before: .. sandboxes-best-practice-delete-on-promote-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link
     - After the updates are safely running in production, you should delete the sandbox.

       .. image:: ../../images/mockups-sandbox-delete.png
          :width: 600 px
          :alt: Delete a sandbox after configuration state changes are promoted.
          :align: left
          :class: no-scaled-link


.. sandboxes-about-workflows-sandbox-admin-start
