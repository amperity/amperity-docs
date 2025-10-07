.. https://docs.amperity.com/operator/


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
About scheduled workflows
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


.. _workflows-configure-automation-settings:

Automation settings
==================================================

.. workflows-configure-automation-settings-start

A workflow can be configured to run at defined intervals, such as daily or weekly, and then can be configured to run specific couriers, bridges, and activations.

.. workflows-configure-automation-settings-end


.. _workflows-configure-activate:

Set to active
--------------------------------------------------

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-setting-activate-start
   :end-before: .. courier-groups-setting-activate-end


.. _workflows-configure-name:

Name
--------------------------------------------------

.. workflows-configure-name-start

Give the workflow a clear and succinct name that is meaningful. This name appears in various locations, including other locations within the Amperity user interface, error messages related to the workflow, and in downstream applications and workflows.

.. workflows-configure-name-end


.. _workflows-configure-schedule:

Define schedule
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-schedule-start
   :end-before: .. term-courier-group-schedule-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-cron-start
   :end-before: .. term-cron-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-crontab-syntax-start
   :end-before: .. term-crontab-syntax-end

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-schedules-start
   :end-before: .. courier-groups-schedules-end

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-schedules-note-start
   :end-before: .. courier-groups-schedules-note-end

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-schedules-context-start
   :end-before: .. courier-groups-schedules-context-end

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-schedules-tip-start
   :end-before: .. courier-groups-schedules-tip-end


.. _workflows-configure-alerts:

Configure alerts
--------------------------------------------------

.. workflows-configure-alerts-start

The following alerts can be configured:

#. A workflow succeeds.
#. A workflow's runtime has exceeded a configurable number of hours.

.. workflows-configure-alerts-end


.. _workflows-configure-run-type:

Set the run type
--------------------------------------------------

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-run-types-start
   :end-before: .. courier-groups-run-types-end


.. _workflows-couriers:

Couriers
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
   :start-after: .. courier-groups-howto-notify-slow-start
   :end-before: .. courier-groups-howto-notify-slow-end

**To configure a workflow alert for a courier group**

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-howto-notify-slow-steps-start
   :end-before: .. courier-groups-howto-notify-slow-steps-end


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
   :start-after: .. courier-groups-howto-add-courier-alert-start
   :end-before: .. courier-groups-howto-add-courier-alert-end

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-howto-add-courier-alert-tip-start
   :end-before: .. courier-groups-howto-add-courier-alert-tip-end

**To send a workflow notification, and then continue the workflow**

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-howto-add-courier-alert-steps-start
   :end-before: .. courier-groups-howto-add-courier-alert-steps-end


.. _workflows-courier-group-missing-files-notify-stop:

Notify and stop
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-howto-add-courier-stop-start
   :end-before: .. courier-groups-howto-add-courier-stop-end

**To send a workflow notification, and then stop the workflow**

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-howto-add-courier-stop-steps-start
   :end-before: .. courier-groups-howto-add-courier-stop-steps-end


.. _workflows-courier-group-missing-files-wait:

Wait for missing files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-wait-for-missing-files-start
   :end-before: .. courier-groups-wait-for-missing-files-end

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-source-courier-alerts-start
   :end-before: .. courier-groups-source-courier-alerts-end


.. _workflows-bridges:

Bridges
==================================================

.. workflows-bridges-start

A bridge may be configured to run as part of a scheduled workflow. Use the **Bridges** tab in the **Scheduled workflows** dialog to add one or more bridges.

.. workflows-bridges-end


.. _workflows-activations:

Activations
==================================================

Activations are orchestrations, campaigns, and Profile API indexes that are configured to be run as part of a scheduled workflow.


.. _workflows-orchestrations:

Orchestrations
--------------------------------------------------

.. include:: ../../amperity_reference/source/orchestrations.rst
   :start-after: .. orchestrations-run-automatic-start
   :end-before: .. orchestrations-run-automatic-start


.. _workflows-profile-api:

Profile API indexes
--------------------------------------------------

.. include:: ../../amperity_operator/source/api_profile.rst
   :start-after: .. profile-api-enable-run-as-workflow-start
   :end-before: .. profile-api-enable-run-as-workflow-end


.. _workflows-campaigns:

Recurring campaigns
--------------------------------------------------

.. include:: ../../amperity_reference/source/campaigns.rst
   :start-after: .. campaigns-run-as-part-of-workflow-start
   :end-before: .. campaigns-run-as-part-of-workflow-end
