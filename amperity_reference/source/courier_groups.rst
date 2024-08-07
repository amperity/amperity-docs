..
.. https://docs.amperity.com/reference/
..


.. meta::
    :description lang=en:
        A courier group defines the frequency at which one (or more) couriers bring data from an external system to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        A courier group defines the frequency at which one (or more) couriers bring data from an external system to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        About courier groups

==================================================
About courier groups
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

.. courier-groups-context-start

A courier group is typically configured to run automatically on a recurring schedule. All couriers within a courier group run as a unit; couriers with required files must complete before any downstream processes, such as Stitch or database generation, can be started. For each courier with required files, Amperity determines if those files have updates, and then pulls updated files to Amperity.

.. courier-groups-context-end

.. image:: ../../images/mockups-workflow-courier-group-dialog.png
   :width: 400 px
   :alt: Enable duration alerts for workflows.
   :align: left
   :class: no-scaled-link

.. courier-groups-what-a-courier-group-does-start

What a courier group does:

#. Logically organizes a list of couriers into a group that shares the same schedule and workflow.
#. Allows for each courier to be assigned schedule variance via wait times and offsets.
#. Enables both automatic and ad hoc runs of couriers.
#. Polls each data source associated with a courier in the group to determine if data is ready to be pulled to Amperity.
#. Ensures that constraints for downstream processes are present in the workflow; all couriers in a courier group must complete their jobs.

What a courier group needs:

#. One (or more) couriers.
#. A schedule.
#. A run type.
#. Configuration for wait times and offsets to help ensure that all files assigned to the courier group have a time window that is large enough to complete data collection.

.. courier-groups-what-a-courier-group-does-start

.. courier-groups-view-start

The **Sources** page shows the status of all courier groups, including when they last ran or updated, and its current status.

.. courier-groups-view-end


.. _courier-groups-schedules:

Schedules
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-schedule-start
   :end-before: .. term-courier-group-schedule-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-cron-start
   :end-before: .. term-cron-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-crontab-syntax-start
   :end-before: .. term-crontab-syntax-end

.. courier-groups-schedules-start

Amperity uses cron syntax to schedule the time at which a courier group is available for transferring files from a customer data source location to Amperity. A courier group that is scheduled runs automatically. Schedules are in UTC.

.. courier-groups-schedules-end

.. courier-groups-schedules-note-start

.. note:: Scheduling a courier group is optional. When a courier group is not assigned a schedule, it may be run manually on an ad hoc basis.

.. courier-groups-schedules-note-end

.. courier-groups-schedules-context-start

A courier group that is scheduled to run on a daily basis will check for files on a daily basis.

A courier group that runs less frequently, such as weekly, bi-weekly, monthly, or quarterly, will (by default) look for files on each day that has passed since the last time the courier group ran.

When a courier group is configured to run less frequently, you can also configure that courier group to only look for files on a specific day.

To use this approach, it is recommended to configure your upstream systems to make their files available to the courier group on a schedule that ensures they will be available to the courier group within a 24-hour window. This window is based on the schedule that is defined for the courier group.

Configure the courier group to run at the end of that 24-hour window, and then enable the **Only retrieve files dropped in the past day?** option, which forces the courier group to only look for files that were made available within the previous 24 hours.

.. courier-groups-schedules-context-end

.. courier-groups-schedules-tip-start

.. tip:: Daylight savings time can affect a schedule. Be sure to set the schedule to be stable and not require changes over time. For example: if a schedule is set to 12:30 AM, and then you fall back, the schedule may become 11:30 PM (fall back) or 1:30 AM (spring forward).

.. courier-groups-schedules-tip-end


.. _courier-groups-schedule-run-types:

Run types
==================================================

.. courier-groups-run-types-start

A courier group can be configured for any of the following run types:

**Full workflow**
   A full workflow refreshes domain tables, runs Stitch, refreshes your customer 360 database, and then runs every scheduled orchestration group that is configured to run after this courier group.

**Partial workflow**
   A partial workflow refreshes domain tables, runs Stitch, refreshes your customer 360 database, but does not run any orchestrations.

   .. important:: Use partial workflows in sandboxes to ensure that data in your sandbox is not inadvertently sent to downstream workflows.

**Ingest only**
   An ingest-only workflow refreshes domain tables, but does not run Stitch.

.. courier-groups-run-types-end


.. _courier-groups-schedule-wait-times:

Wait times
==================================================

.. courier-groups-schedule-wait-time-start

A wait time is a constraint placed on a courier group that defines an extended time window for data to be made available at the source location.

A courier group typically runs on an automated schedule that expects customer data to be available at the source location within a defined time window. However, in some cases, the customer data may be delayed and isn't made available within that time window.

.. courier-groups-schedule-wait-time-end

.. courier-groups-schedule-wait-time-window-start

Use a wait time to extend the time window for data to be made available. This can help reduce the number of alerts that may be generated for data sources that cannot be picked up by a courier group.

.. courier-groups-schedule-wait-time-window-end

.. courier-groups-schedule-wait-time-note-start

.. note:: For couriers associated with a filedrop location the default wait time is 0. A polling operation only checks for a data source before declaring success or failure. For couriers associated with REST APIs and data warehouses, the polling operation is always considered to be successful.

.. courier-groups-schedule-wait-time-note-end

.. courier-groups-schedule-wait-time-downstream-start

A downstream process begins after each load operation is completed for each data source associated with each courier in the courier group and each domain table has been updated.

.. courier-groups-schedule-wait-time-downstream-end


.. _courier-groups-schedule-offsets:

Offsets
==================================================

.. courier-groups-schedule-offset-start

An offset is a constraint placed on a courier group that defines a range of time that is older than the scheduled time, within which a courier group will accept customer data as valid for the current job. Offset times are in Coordinated Universal Time (UTC), unless the "Use this time zone for file date ranges" checkbox is checked.

A courier group offset is typically set to be 24 hours. For example, it's possible for customer data to be generated with a correct file name and datestamp appended to it, but for that datestamp to represent the previous day because of the customer's own workflow. An offset ensures that the data at the source location is recognized by the courier as the correct data source.

.. warning:: An offset affects couriers in a courier group whether or not they run on a schedule. Manually run courier groups will not take their schedule into consideration when determining the date range; only the provided input day(s) to load data from are used as inputs.

.. courier-groups-schedule-offset-end

.. courier-groups-schedule-offset-callout-start

.. important:: The schedule defines the frequency at which the courier group will run.

   The timezone is the time at which the courier group will run. This may be set to your local time zone.

   Individual courier offsets are calculated using Coordinated Universal Time (UTC), even when a non-UTC time zone is specified for the courier group. This means that when a courier group runs, the current time in UTC is used to calculate the offset.

   When a courier group is set to your local time zone, you must consider the offset for your local time zone when defining the offset for each courier in the courier group.

.. courier-groups-schedule-offset-callout-end


.. _courier-groups-timezones:

Time zones
==================================================

.. courier-groups-timezones-start

A courier group schedule is associated with a time zone. The time zone determines the point at which a courier group's scheduled start time begins. A time zone should be aligned with the time zone of system from which the data is being pulled.

.. courier-groups-timezones-end

.. courier-groups-timezones-about-start

The time zones that are available for selection in Amperity are modeled after the Google Calendar and are similar to:

.. code-block:: none

   (GMT-08:00) Pacific Time
   (GMT-07:00) Mountain Time
   (GMT-08:00) Central Time
   (GMT-09:00) Eastern Time

.. courier-groups-timezones-about-end

.. courier-groups-timezones-downstream-start

The time zone that is chosen for an courier group schedule should consider every downstream business processes that requires the data and also the time zone(s) in which the consumers of that data will operate.

.. courier-groups-timezones-downstream-end

.. courier-groups-timezones-tip-start

.. tip:: Do not create courier group schedules that may occur during a daylight savings time transition.

   For example, an courier group schedule with the cron string of ``30 2 * * *`` and the time zone of "(GMT-08:00) Pacific Time" will run once a day most at 2:30am, except for one day in the spring when it will not run at all and one day in the fall when it will run twice.

   This is because American daylight savings time transitions at 2:00 AM, meaning the 2:00 AM hour occurs twice when transitioning out of daylight savings time (Fall) and is skipped altogether when transitioning into daylight savings time (Spring).

.. courier-groups-timezones-tip-end


.. _courier-groups-howtos:

How-tos
==================================================

.. courier-groups-howtos-list-start

This section describes tasks related to managing courier groups in Amperity:

* :ref:`Add a courier group <courier-groups-add>`
* :ref:`Configure duration alerts for workflows <courier-groups-configure-duration-alert>`
* :ref:`Configure missing files alerts for workflows <courier-groups-configure-missing-files-alert>`
* :ref:`Copy a courier group <courier-groups-copy>`
* :ref:`Delete a courier group <courier-groups-delete>`
* :ref:`Load data only for past day <courier-groups-load-only-for-past-day>`
* :ref:`Run a courier group <courier-groups-run>`
* :ref:`Wait for missing files <courier-groups-configure-missing-files-wait>`

.. courier-groups-howtos-list-end


.. _courier-groups-add:

Add courier group
--------------------------------------------------

.. courier-groups-add-start

Use the **Add courier group** button to add a courier group to Amperity. A courier group should be created to consolidate individual couriers into a scheduled workflow.

.. courier-groups-add-end

.. courier-groups-add-context-start

For each courier added to a courier group, define a wait time and an offset. This is used to help determine how much time the courier group should wait for the files associated with a courier to be ready for processing.

In some cases, if the files are not ready, the courier (and courier group) will fail. But in other cases, if the files in the courier are not flagged as required, the courier group may continue processing the rest of the files.

.. courier-groups-add-context-end

**To add a courier group**

.. courier-groups-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link

     - From the **Sources** page, click **Add courier group**. This opens the **Edit courier group** dialog box. Add a name for the courier group.

       .. image:: ../../images/mockups-workflow-courier-group-name.png
          :width: 400 px
          :alt: Enable duration alerts for workflows.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

     - .. include:: ../../shared/terms.rst
          :start-after: .. term-courier-group-schedule-start
          :end-before: .. term-courier-group-schedule-end

       .. image:: ../../images/mockups-workflow-courier-group-schedule.png
          :width: 400 px
          :alt: Enable duration alerts for workflows.
          :align: left
          :class: no-scaled-link

       Use a cron string to define a schedule for the courier group.

       .. include:: ../../amperity_reference/source/courier_groups.rst
          :start-after: .. courier-groups-schedules-tip-start
          :end-before: .. courier-groups-schedules-tip-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link

     - Select a time zone.

       .. image:: ../../images/mockups-workflow-courier-group-timezone.png
          :width: 400 px
          :alt: Select a time zone.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link

     - Optional. Enable duration alerts. Enable the **Warn if runtime exceeds** checkbox, and then set the number of hours (or minutes) at which, when the configured amount of time is exceeded, a workflow alert will be sent.

       .. image:: ../../images/mockups-workflow-courier-group-duration-alerts.png
          :width: 400 px
          :alt: Enable duration alerts for workflows.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link

     - Define how the courier group workflow will run: a **Full workflow**, a **Partial workflow**, or an **Ingest only** workflow.

       .. image:: ../../images/mockups-workflow-courier-group-run-types.png
          :width: 400 px
          :alt: A courier group has three run types.
          :align: left
          :class: no-scaled-link

       A full workflow refreshes domain tables, runs Stitch, refreshes your customer 360 database, and then runs every scheduled orchestration group that is configured to run after this courier group.

       A partial workflow refreshes domain tables, runs Stitch, refreshes your customer 360 database, but does not run any orchestrations.

       An ingest-only workflow refreshes domain tables, but does not run Stitch.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link

     - To enable the courier group and have it run on the configured schedule, set **Courier group status?** to **Enabled**. (If this setting is set to **Disabled** the courier group will not run on a schedule, but may be run manually.)

       Many courier groups are scheduled to run on a daily basis. Some courier groups are scheduled to run less frequently, such as bi-weekly, monthly, or even quarterly. Use the **Only retrieve files dropped in the past day?** setting to configure a courier group that runs less frequently to only look for files dropped yesterday.

       .. image:: ../../images/mockups-workflow-courier-group-settings.png
          :width: 400 px
          :alt: Enable duration alerts for workflows.
          :align: left
          :class: no-scaled-link

       .. tip:: A courier group that runs less frequently, such as weekly, bi-weekly, monthly, or quarterly, will (by default) look for files on each day that has passed since the last time the courier group ran.

          When a courier group is configured to run less frequently, you can also configure that courier group to only look for files on a specific day.

          To use this approach, it is recommended to configure your upstream systems to make their files available to the courier group on a schedule that ensures they will be available to the courier group within a 24-hour window. This window is based on the schedule that is defined for the courier group.

          Configure the courier group to run at the end of that 24-hour window, and then enable the **Only retrieve files dropped in the past day?** option, which forces the courier group to only look for files that were made available within the previous 24 hours.


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link

     - Add one (or more) couriers to the courier group.

       For each courier in the courier group, select a courier, configure the wait time and offset, and then enable workflow alerts.

       .. image:: ../../images/mockups-workflow-courier-group-add-couriers.png
          :width: 400 px
          :alt: Enable duration alerts for workflows.
          :align: left
          :class: no-scaled-link

       **About wait times**

       .. include:: ../../amperity_reference/source/courier_groups.rst
          :start-after: .. courier-groups-schedule-wait-time-start
          :end-before: .. courier-groups-schedule-wait-time-end

       Use a wait time to extend the time window for data to be made available. This can help reduce the number of alerts that may be generated for data sources that cannot be picked up by a courier group.

       **About offsets for loading data**

       .. include:: ../../amperity_reference/source/courier_groups.rst
          :start-after: .. courier-groups-schedule-offset-start
          :end-before: .. courier-groups-schedule-offset-end


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step 8.
          :align: left
          :class: no-scaled-link

     - Click **Save** to save the courier group.

.. courier-groups-add-steps-end


.. _courier-groups-configure-duration-alert:

Configure duration alerts
--------------------------------------------------

.. courier-groups-configure-duration-alert-start

A duration alert is a type of workflow alert that is sent when a courier group has run longer than a configured amount of time. A duration alert is sent to any email address or Slack channel that is configured for the **Courier group** workflow type.

.. courier-groups-configure-duration-alert-end

**To configure a duration alert for a courier group**

.. courier-groups-configure-duration-alert-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Edit**.
#. Enable the **Warn if runtime exceeds** checkbox, and then set the number of hours (or minutes) at which, when this amount of time is exceeded, a workflow alert will be sent.

   .. image:: ../../images/mockups-workflow-courier-group-duration-alerts.png
      :width: 400 px
      :alt: Enable duration alerts for workflows.
      :align: left
      :class: no-scaled-link

#. Click **Save**.

.. courier-groups-configure-duration-alert-steps-end


.. _courier-groups-configure-missing-files-alert:

Configure missing files alerts
--------------------------------------------------

.. courier-groups-configure-missing-files-alert-start

A courier group can be configured to workflow alerts when files are missing, and then:

#. :ref:`Continue processing even if files are missing <courier-groups-configure-missing-files-alert-notify-continue>`
#. :ref:`Stop processing <courier-groups-configure-missing-files-alert-notify-stop>`

.. courier-groups-configure-missing-files-alert-end

.. courier-groups-configure-missing-files-alert-important-start

.. important:: Files can be missing for any number of reasons, including by delays that may have occurred in upstream workflows that exist outside of Amperity. And in many situations a file is late, not missing.

.. courier-groups-configure-missing-files-alert-important-end


.. _courier-groups-configure-missing-files-alert-notify-continue:

Notify, continue workflow
++++++++++++++++++++++++++++++++++++++++++++++++++

.. courier-groups-configure-missing-files-alert-notify-continue-start

A courier group can be configured to send workflow alerts when one (or more) files are missing, and then continue processing if files are missing.

.. courier-groups-configure-missing-files-alert-notify-continue-end

.. courier-groups-configure-missing-files-alert-notify-continue-tip-start

.. tip:: Some files are not considered essential to the daily Amperity run. The reasons why a particular file may be considered non-essential will vary from tenant to tenant, but they may include situations like:

   * A data source is mostly static
   * A data source does not contain PII that will affect the quality of the Amperity ID.
   * A data source is associated with a workflow that often misses the configured Amperity wait time period.

.. courier-groups-configure-missing-files-alert-notify-continue-tip-end

**To send a workflow notification, and then continue the workflow**
.. courier-groups-configure-missing-files-alert-notify-continue-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Edit**.
#. Under the name of a courier group, set **Notify when missing?** to enabled, and then set **Stop when missing?** to disabled.
#. Click **Save**.

.. courier-groups-configure-missing-files-alert-notify-continue-steps-end


.. _courier-groups-configure-missing-files-alert-notify-stop:

Notify, stop workflow
++++++++++++++++++++++++++++++++++++++++++++++++++

.. courier-groups-configure-missing-files-alert-notify-stop-start

A courier group can be configured to send workflow alerts when one (or more) files are missing, and then stop processing if files are missing.

.. courier-groups-configure-missing-files-alert-notify-stop-end

**To send a workflow notification, and then stop the workflow**

.. courier-groups-configure-missing-files-alert-notify-stop-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Edit**.
#. Under the name of a courier group, set **Notify when missing?** to enabled, and then set **Stop when missing?** to enabled.
#. Click **Save**.

.. courier-groups-configure-missing-files-alert-notify-stop-steps-end


.. _courier-groups-copy:

Copy courier group
--------------------------------------------------

.. courier-groups-copy-start

Use the **Copy** option to copy a courier group to Amperity.

.. courier-groups-copy-end

**To delete a courier group**

.. courier-groups-copy-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Make a copy**.
#. On the **Copy courier group** window, enter the courier group name into the **Courier group name** field.
#. Click **Save**.

The copied courier group appears in the **Courier groups** section of the **Sources** page.

.. courier-groups-copy-steps-end


.. _courier-groups-delete:

Delete courier group
--------------------------------------------------

.. courier-groups-delete-start

Use the **Delete** option to remove a courier group from Amperity. This should be done carefully. Verify that both upstream and downstream processes no longer depend on this courier group prior to deleting it.

.. important:: This action will *not* delete couriers that are associated with the courier group.

.. courier-groups-delete-end

**To delete a courier group**

.. courier-groups-delete-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Delete**.
#. Click **Delete** to confirm.

.. courier-groups-delete-steps-end


.. _courier-groups-load-only-for-past-day:

Load data only for past day
--------------------------------------------------

.. courier-groups-load-only-for-past-day-start

.. TODO: If this section is edited, keep in sync with the tip callout in the add courier group how-to.

A courier group that runs less frequently, such as weekly, bi-weekly, monthly, or quarterly, will (by default) look for files on each day that has passed since the last time the courier group ran.

When a courier group is configured to run less frequently, you can also configure that courier group to only look for files on a specific day.

To use this approach, it is recommended to configure your upstream systems to make their files available to the courier group on a schedule that ensures they will be available to the courier group within a 24-hour window. This window is based on the schedule that is defined for the courier group.

Configure the courier group to run at the end of that 24-hour window, and then enable the **Only retrieve files dropped in the past day?** option, which forces the courier group to only look for files that were made available within the previous 24 hours.

.. courier-groups-load-only-for-past-day-end

**To load data only for the past day**

.. courier-groups-load-only-for-past-day-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Edit**. The **Edit courier group** page opens.
#. Enable the **Only retrieve files dropped in the past day?** option.

   .. image:: ../../images/mockups-workflow-courier-group-settings.png
      :width: 400 px
      :alt: Enable duration alerts for workflows.
      :align: left
      :class: no-scaled-link

#. Click **Save**.

.. courier-groups-load-only-for-past-day-steps-end


.. _courier-groups-run:

Run courier groups
--------------------------------------------------

.. courier-groups-run-start

A courier group may be run in the following ways:

* :ref:`courier-groups-run-automatically`
* :ref:`courier-groups-run-for-date-range`
* :ref:`courier-groups-run-for-specific-day`
* :ref:`courier-groups-run-for-all-data`
* :ref:`courier-groups-run-manually`

.. courier-groups-run-end


.. _courier-groups-run-automatically:

Automatically
++++++++++++++++++++++++++++++++++++++++++++++++++

.. courier-groups-run-automatically-start

A courier group with a schedule (including time zones, wait times, and offsets) will run automatically when the **Courier group status?** is set to **Enabled**.

.. courier-groups-run-automatically-end


.. _courier-groups-run-for-date-range:

For a date range
++++++++++++++++++++++++++++++++++++++++++++++++++

.. courier-groups-run-for-date-range-start

A courier group can be configured to load all data for a specific date range.

.. courier-groups-run-for-date-range-end

**To run a courier group for a date range**

.. courier-groups-run-for-date-range-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Run**. The **Run courier group** page opens.
#. Select **Load data from a specific time period**.
#. Select a start date and an end date.
#. To prevent downstream processing, select **Load only**.
#. Click **Run**.

.. courier-groups-run-for-date-range-steps-end


.. _courier-groups-run-for-specific-day:

For a specific day
++++++++++++++++++++++++++++++++++++++++++++++++++

.. courier-groups-run-for-specific-day-start

A courier group can be configured to load all data for a single day.

.. courier-groups-run-for-specific-day-end

**To run a courier group for a specific day**

.. courier-groups-run-for-specific-day-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Run**. The **Run courier group** page opens.
#. Select **Load data from a specific day**, and then select a day.
#. To prevent downstream processing, select **Load only**.
#. Click **Run**.

.. courier-groups-run-for-specific-day-steps-end


.. _courier-groups-run-for-all-data:

For all data
++++++++++++++++++++++++++++++++++++++++++++++++++

.. courier-groups-run-for-all-data-start

A courier group can be configured to load all data that is available. This can be a large amount of data if the courier group is running for the first time.

.. courier-groups-run-for-all-data-end

**To run a courier group for-all-data**

.. courier-groups-run-for-all-data-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Run**. The **Run courier group** page opens.
#. Select **Load all data**.
#. To prevent downstream processing, select **Load only**.
#. Click **Run**.

.. courier-groups-run-for-all-data-steps-end


.. _courier-groups-run-manually:

Manually
++++++++++++++++++++++++++++++++++++++++++++++++++

.. courier-groups-run-manually-start

Use the **Run** option to run the courier group manually.

.. courier-groups-run-manually-end

**To run a courier group manually**

.. courier-groups-run-manually-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Run**. The **Run courier group** page opens.
#. Select the time period for which data is loaded and indicate if downstream processes should be started automatically.
#. Click **Run**.

.. courier-groups-run-manually-steps-end


.. _courier-groups-configure-missing-files-wait:

Wait for missing files
--------------------------------------------------

.. courier-groups-configure-missing-files-wait-start

When files are missing or late, in addition to sending an email alert and either continuing or stopping the workflow, Amperity will continue to attempt to find the these files. Use the **Wait** setting to configure amount of time Amperity should wait:

.. image:: ../../images/mockups-workflow-courier-group-settings-wait.png
   :width: 400 px
   :alt: Enable duration alerts for workflows.
   :align: left
   :class: no-scaled-link

.. courier-groups-configure-missing-files-wait-end
