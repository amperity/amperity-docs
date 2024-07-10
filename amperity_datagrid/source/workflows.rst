.. 
.. https://docs.amperity.com/datagrid/
..


.. meta::
    :description lang=en:
        Automate end-to-end workflows within Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Automate end-to-end workflows within Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Automate workflows

==================================================
Automate workflows
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-workflow-start
   :end-before: .. term-workflow-end

.. workflows-about-start

For example, many workflows are end-to-end process that:

#. Use a courier to pull data to Amperity.
#. Standardize data using semantic tags and feeds.
#. Add data to domain tables.
#. Build databases.
#. Run queries and segments to return results and audiences for use with downstream workflows.
#. Send results to destinations using orchestrations and campaigns.

An automated workflow is configured to run these steps automatically, and then send workflow alerts when warnings and errors within a workflow are detected.

.. workflows-about-end


.. _workflows-courier-groups:

Courier groups
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

.. note::

   .. include:: ../../amperity_reference/source/courier_groups.rst
      :start-after: .. courier-groups-context-start
      :end-before: .. courier-groups-context-end


.. _workflows-courier-group-duration-thresholds:

Duration thresholds
--------------------------------------------------

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-duration-alert-start
   :end-before: .. courier-groups-configure-duration-alert-end

**To configure a workflow alert for a courier group**

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-duration-alert-steps-start
   :end-before: .. courier-groups-configure-duration-alert-steps-end


.. _workflows-courier-group-missing-files:

Missing files
--------------------------------------------------

.. workflows-courier-group-missing-files-start

A courier group can be configured to send email and Slack alerts when files are missing, and then:

#. :ref:`Continue processing even if files are missing <workflows-courier-group-missing-files-notify-continue>`
#. :ref:`Stop processing <workflows-courier-group-missing-files-notify-stop>`

.. workflows-courier-group-missing-files-end


.. _workflows-courier-group-missing-files-notify-continue:

Notify and continue
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-missing-files-alert-notify-continue-start
   :end-before: .. courier-groups-configure-missing-files-alert-notify-continue-end

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-missing-files-alert-notify-continue-tip-start
   :end-before: .. courier-groups-configure-missing-files-alert-notify-continue-tip-end

**To send a workflow notification, and then continue the workflow**

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-missing-files-alert-notify-continue-steps-start
   :end-before: .. courier-groups-configure-missing-files-alert-notify-continue-steps-end


.. _workflows-courier-group-missing-files-notify-stop:

Notify and stop
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-missing-files-alert-notify-stop-start
   :end-before: .. courier-groups-configure-missing-files-alert-notify-stop-end

**To send a workflow notification, and then stop the workflow**

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-missing-files-alert-notify-stop-steps-start
   :end-before: .. courier-groups-configure-missing-files-alert-notify-stop-steps-end


.. _workflows-courier-group-missing-files-wait:

Wait for missing files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-missing-files-wait-start
   :end-before: .. courier-groups-configure-missing-files-wait-end

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-configure-missing-files-alert-important-start
   :end-before: .. courier-groups-configure-missing-files-alert-important-end


.. _workflows-orchestration-groups:

Orchestration groups
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-group-start
   :end-before: .. term-orchestration-group-end


.. _workflows-orchestration-group-run-after:

Run after courier group
--------------------------------------------------

.. include:: ../../amperity_reference/source/orchestration_groups.rst
   :start-after: .. orchestration-groups-courier-group-constraints-start
   :end-before: .. orchestration-groups-courier-group-constraints-end

**To configure an orchestration group to run after a courier group**

.. include:: ../../amperity_reference/source/orchestration_groups.rst
   :start-after: .. orchestration-groups-courier-group-constraints-steps-start
   :end-before: .. orchestration-groups-courier-group-constraints-steps-end


.. _workflows-orchestration-group-run-on-schedule:

Run on a schedule
--------------------------------------------------

.. include:: ../../amperity_reference/source/orchestration_groups.rst
   :start-after: .. orchestration-groups-run-on-a-schedule-start
   :end-before: .. orchestration-groups-run-on-a-schedule-end

**To configure an orchestration group to run on a schedule**

.. include:: ../../amperity_reference/source/orchestration_groups.rst
   :start-after: .. orchestration-groups-run-on-a-schedule-steps-start
   :end-before: .. orchestration-groups-run-on-a-schedule-steps-end

