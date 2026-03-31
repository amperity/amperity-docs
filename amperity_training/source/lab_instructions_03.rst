.. https://docs.amperity.com/reference/


==================================================
Lab 03: Using sandboxes
==================================================

Operators should validate the changes made in a sandbox before the changes are promoted to production. The specific steps needed to validate any set of changes will vary based on the nature of the changes that have been made. In the previous labs you have added a new datasource. Use the following steps to validate the changes you have made before promoting the changes to production.

.. note:: The ingest workflow initiated in previous steps needs to be completed before continuing. If the workflows are still running, wait for them to complete before proceeding.


Objective
==================================================

Now that you have updated the configuration in the sandbox it is time to validate the impact of those changes and promote the sandbox.


Validate and promote sandbox
==================================================

#. In the sandbox, Use the Stitch tab to Navigate to Stitch page. The Summary subtab should now show two sources, and an increased deduplication rate.

   .. image:: /_images/ex03_stitch_summary.png
      :width: 400 px
      :alt: Stitch summary
      :align: left
      :class: no-scaled-link

#. Open the Benchmarking subtab and select Grade and calibrate under Amperity IDs with many postal codes. Grade and calibrate some tests and select Save and close.

   .. image:: /_images/ex03_benchmarking.png
      :width: 400 px
      :alt: Benchmarking
      :align: left
      :class: no-scaled-link

#. Click Review changes in the sandbox promote notification.

   .. image:: /_images/ex03_review_changes_notification.png
      :width: 400 px
      :alt: Review changes notification
      :align: left
      :class: no-scaled-link

#. Select Yes, continue and update all necessary tables. Amperity requires a Merge message for promotion. Provide a descriptive Merge message such as: This merge introduces a new table, pos_customers_out with POS data to improve the customer 360 view. Click on Promote.

   .. image:: /_images/ex03_promote_changes_dialog.png
      :width: 400 px
      :alt: Promote changes dialog
      :align: left
      :class: no-scaled-link

#. In the Promote changes modal, select the default Promote and delete sandbox and click Promote.

   .. image:: /_images/ex03_promote_and_delete_sandbox.png
      :width: 400 px
      :alt: Promote and delete sandbox
      :align: left
      :class: no-scaled-link

   A sandbox should be short-lived and should be used to make small, iterative changes within a tenant. After these changes are safely promoted to production, sandboxes should be deleted. Use a sandbox for each iterative change to ensure that you are never making large changes to production. You can automatically delete a sandbox using the Promote and delete sandbox option when promoting changes from a sandbox to production. You can verify that you have returned to your production tenant when the side bar returns to black.

#. After you are returned to your production tenant select the Sources tab and take note of the number source records and pos_customers_out records.

   .. image:: /_images/ex03_sources_tab_records.png
      :width: 400 px
      :alt: Sources tab records
      :align: left
      :class: no-scaled-link

#. Click on the Actions kebab menu |fa-kebab| to the right of the Courier group Daily and select Run.

   .. image:: /_images/ex03_run_courier_groups.png
      :width: 400 px
      :alt: Run Courier group
      :align: left
      :class: no-scaled-link

#. Select Partial workflow and click on Run.

   .. image:: /_images/ex03_partial_workflow.png
      :width: 400 px
      :alt: Partial workflow
      :align: left
      :class: no-scaled-link

#. Check that the Daily workflow under the Workflows tab has started. Then return to the Sources tab and note the number of source records and pos_customers_out records. What changed?

   .. image:: /_images/ex03_workflow_started.png
      :width: 400 px
      :alt: Workflow started
      :align: left
      :class: no-scaled-link

   When promoting changes from a sandbox to a production tenant, the object configuration is copied, but not the data. After completing the last section, the POS dataset configuration has been promoted, but the data has not. It is necessary to run the Courier group to ensure the data is available in the production tenant.
