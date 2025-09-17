.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        A journey is an automated sequence that connects customers across channels and your brand's marketing campaigns.

.. meta::
    :content class=swiftype name=body data-type=text:
        A journey is an automated sequence that connects customers across channels and your brand's marketing campaigns.

.. meta::
    :content class=swiftype name=title data-type=string:
        About journeys

==================================================
About journeys
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-start
   :end-before: .. term-journey-end

.. journeys-about-context-start

By using **Journeys**, marketers can implement cross-channel strategies, improve targeting precision, and activate the right message at the right moment to drive better engagement and higher conversions.

.. journeys-about-context-end


.. _journeys-howitworks:

How journeys work
==================================================

.. journeys-howitworks-start

A journey starts with a defined audience that moves through a series of interactions based on criteria you specify, like customer behavior, attributes, or engagement history. The sequence can branch depending on what conditions you set, so that customers have a different experience depending on what actions they take.

.. journeys-howitworks-end

.. journeys-howitworks-context-start

Here's an example of a built-out journey:

.. image:: ../../images/mockup-journeys-overview-alt.png
   :width: 600 px
   :alt: Journey built out in the journeys canvas interface
   :align: left
   :class: no-scaled-link

In this case, the marketer is offering high-value customers early access to new products before general release in two weeks. They start by creating an audience segment made up of customers in the top 10% of customer lifetime value.

The first step divides this audience into three sub-audiences: those who purchased in the last 1-30 days, those whose purchased in the last 31-90 days, and those whose most recent purchase was more than 90 days ago.

Each different audience is sent down a different path toward activation in a marketing channel.

* The high-value customers who purchased most recently are contacted immediately, giving them exclusive early access.
* The high-value customers who purchased between 1 and 3 months ago are set for a delay followed by an activation, as a second wave of early access.
* Additionally, this audience is further split, so that 75% receive a special promotion and 25% do not, to see how important an added incentive is for getting customers to purchase again.
* Finally, the high-value customers who have not purchased in the last three months are contacted when the new products become generally available to make sure they are among the first to know.

The journey can be further built out beyond this, with further splits based on whether or not customers purchase or how they engage with the communications they receive.

.. journeys-howitworks-context-end


.. _journeys-setup:

Journey setup
==================================================

.. journeys-setup-start

**Journeys** require that segments are available and that at least one destination has been configured.

Access the **Journeys** canvas by selecting **Journeys** at the top of the **Activations** page, and then click **Create journey**.

.. journeys-setup-end


Name a journey
--------------------------------------------------

.. journeys-setup-name-start

Enter a name in the **Journey Name** field.

A journey should be assigned a name that makes it easy to find and for other Amperity users to understand.

.. journeys-setup-name-end

.. journeys-setup-name-tip-start

.. tip:: Use good naming patterns to ensure that you can always find your journeys in the various applications to which you sends them. The journey name will *always* appear in the filename that is sent to any destination.

   Avoid duplication between journey and treatment group names.

   Avoid using the names of destinations as journey names unless the journey is sent to *only* that destination.

   Use a naming pattern that ensures the journey name works across every treatment group that is configured within any sub-audience.

   If brand names and/or region names apply to all sub-audiences in the journey, consider using them within the journey name.

   Some examples:

   * "Birthdays_Under_40"
   * "Acme_Churn"
   * "Churn_HighValue_Early"
   * "Socktown_High_AOV"

.. journeys-setup-name-tip-end

.. _journeys-setup-who-enters:

Who enters?
--------------------------------------------------

.. journeys-setup-who-enters-start

Every journey starts with an audience defined by one or more segments that determine which users enter this journey.

Choose one or more segments from the **Select inclusion segments** dropdown list. The customers in that list will become the audience for this campaign.

.. image:: ../../images/mockup-journeys-canvas-inclusion.png
   :width: 380 px
   :alt: Include a segment
   :align: left
   :class: no-scaled-link

.. journeys-setup-who-enters-end

.. journeys-setup-who-enters-note-start

.. note:: When adding multiple inclusion segments, all segments are unioned, so a customer only needs to match one of the segments in the inclusion category in order to be considered part of it. 

.. journeys-setup-who-enters-note-end

.. important:: **Segment filtering by database**

   Each journey is associated with a specific database. This database is set automatically when you select your first inclusion segment.
   
   Once that first inclusion segment is selected:
   
   * The journey is tied to the same database as that segment
   * Viability of the journey depends on the database functioning with no errors.
   * All other segments--whether inclusion, exlcusion, or exit--are filtered to only show segments from that database.
   * Similarly, the activation ID associated with the initial segment determines the activation ID for all other segments to ensure consistency across the journey. For example, if the initial segment activates based on email, then other segments will only include customers with valid email addresses. 
   
   To change the database associated with a journey, you must first remove all inclusion segments. Then, when you select a new first inclusion segment from a different database, the journey's database updates accordingly.

.. _journeys-setup-who-is-excluded:

Who is excluded?
--------------------------------------------------

.. journeys-setup-who-is-excluded-start

Sometimes a journey needs to exclude certain members of your audience. For example, a journey aimed at churn prevention often excludes customers who have opted-out of SMS messaging and/or who have unsubscribed from an email list.

When you need to exclude audience members, choose one or more segments from the **Select exclusion segments** dropdown list. The customers in an exclusion list will be removed from the audience for this journey.

.. image:: ../../images/mockup-journeys-canvas-exclusion.png
   :width: 380 px
   :alt: Exclude a segment
   :align: left
   :class: no-scaled-link

.. journeys-setup-who-is-excluded-end

.. journeys-setup-who-is-excluded-note-start

.. note:: When adding multiple exclusion segments, all segments are unioned, so a customer only needs to match one of the segments in the exclusion category in order to be considered part of it. 

.. journeys-setup-who-is-excluded-note-end

.. _journeys-exit-conditions:

Exit conditions
--------------------------------------------------

.. journeys-exit-conditions-start

Some customers should exit a journey when a particular criterion has been fulfilled. For example:

* The goal of a churn prevention campaign is to convince a customer to make a purchase. If a customer who is part of a churn prevention campaign makes a purchase they should be removed from the campaign.

* An audience starts with customers who have opted in to receiving marketing messages from your brand. If a customer who is part of that journey later opts out they should be removed from the campaign.

Exit conditions are defined using a segment. One or more segments that define exit conditions may be added to a journey using the **Select exit segments** dropdown.

.. image:: ../../images/mockup-journeys-canvas-exit-conditions.png
   :width: 380 px
   :alt: Choose exit conditions
   :align: left
   :class: no-scaled-link

.. journeys-setup-who-is-excluded-note-start

.. note:: When adding multiple exit condition segments, all segments are unioned, so a customer only needs to match one of the segments in the exit conditions category in order to be considered part of it. 

.. journeys-setup-who-is-excluded-note-end

.. journeys-exit-conditions-end


.. _journeys-canvas:

Journeys canvas
==================================================

.. journeys-canvas-start

After establishing the audience and starting conditions of the journey, you will be taken to the **Journeys** canvas. This is the interface where you determine the steps of the journey and define how your brand will interact with customers at each step.

.. journeys-canvas-end

.. journeys-node-types-start

The following building blocks are available to users for creating journeys:

* :ref:`journeys-node-start`
* :ref:`journeys-node-activate`
* :ref:`journeys-node-delay`
* :ref:`journeys-node-split-conditional`
* :ref:`journeys-node-split-percent`
* :ref:`journeys-node-split-individual`

.. journeys-node-types-end


.. _journeys-node-start:

Journey start
--------------------------------------------------

.. journeys-node-start-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-start-start
   :end-before: .. term-journey-node-start-end

.. image:: ../../images/mockup-journeys-canvas-start.png
   :width: 280 px
   :alt: Start node
   :align: left
   :class: no-scaled-link

To edit inclusions, exclusions, or exit conditions, click on the **Journey setup** sidebar. Click the plus button underneath to add nodes to the journey.

.. journeys-node-start-end


.. _journeys-node-activate:

Activate
--------------------------------------------------

.. journeys-node-activate-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-activate-start
   :end-before: .. term-journey-node-activate-end

.. image:: ../../images/mockup-journeys-canvas-activate.png
   :width: 280 px
   :alt: Activate node
   :align: left
   :class: no-scaled-link

You can rename the activate node.

You can configure a single activation node to send to multiple destinations at once, and this is generally recommended for simplicity and efficiency.

.. journeys-node-activate-note-start

.. note:: If you are activating to several destinations and each one uses different custom attributes, you'll need to create a separate activation node for each destination to assign those attributes correctly.

.. journeys-node-activate-note-end

.. journeys-node-activate-filename-conflict-tip-start

.. tip:: **Avoid activation file naming conflicts**

   Running a journey generates a file for every activation node. The filename is constructed using:
   
   * the **journey name**
   * the **activation node name**
   
   If multiple activation nodes have the same filename, it will cause an error. 
   
   To avoid this error, make sure each activation node within a journey has a unique name. Renaming the node will automatically update the generated filename.
   
   You can check an activation node's path and file name in the **Node configuration** panel on the righthand side of the **Journeys** canvas, under "Destination Summary". 

.. journeys-node-activate-filename-conflict-tip-end 

.. TODO: add screenshot

.. journeys-node-activate-end


.. _journeys-node-delay:

Delay
--------------------------------------------------

.. journeys-node-delay-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-delay-start
   :end-before: .. term-journey-node-delay-end

.. image:: ../../images/mockup-journeys-canvas-delay.png
   :width: 280 px
   :alt: Delay node
   :align: left
   :class: no-scaled-link

Choose a combination of an integer plus "days", "weeks", or "months" to designate how long to wait before the next step in the journey begins.

.. image:: ../../images/mockup-journeys-canvas-delay-options.png
   :width: 500 px
   :alt: Delay node
   :align: left
   :class: no-scaled-link

A delay is applied to a single parent node.

You can rename the delay node.

.. important:: Customers do not automatically move forward after the wait period ends. Progression only occurs the next time the journey runs. 
   
   For example, if a delay node is set to 3 days but the journey is scheduled to run weekly, customers will remain at the delay node until the next scheduled run, potentially waiting up to 7 days. 
   
   If a journey is set to run only once, customers will not move beyond the delay node after it executes. 

.. journeys-node-delay-end


.. _journeys-node-split-conditional:

Conditional split
--------------------------------------------------

.. journeys-node-split-conditional-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-conditional-split-start
   :end-before: .. term-journey-node-conditional-split-end

.. image:: ../../images/mockup-journeys-canvas-conditional-split.png
   :width: 440 px
   :alt: Conditional split node
   :align: left
   :class: no-scaled-link

These segments may already exist or may be defined within this journey using custom criteria.

You can rename the individual conditional split node and rename the "Everyone else" sub-audience.

.. journeys-node-split-conditional-end


.. _journeys-node-split-percent:

Percent split
--------------------------------------------------

.. journeys-node-split-percent-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-percent-split-start
   :end-before: .. term-journey-node-percent-split-end

.. image:: ../../images/mockup-journeys-canvas-percent-split.png
   :width: 440 px
   :alt: Percent split node
   :align: left
   :class: no-scaled-link

The percentage of all individual nodes under a percent split must add up to 100% of the audience, including the control group.

You can rename the percent split node and rename the individual paths.

.. journeys-node-split-percent-end


.. _journeys-node-split-individual:

Individual split
--------------------------------------------------

.. journeys-node-split-individual-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-individual-split-start
   :end-before: .. term-journey-node-individual-split-end

.. image:: ../../images/mockup-journeys-canvas-individual-split-examples.png
   :width: 440 px
   :alt: Individual split nodes
   :align: left
   :class: no-scaled-link

.. note:: To edit sub-audiences conditions and naming, click into the parent node.

.. journeys-node-split-individual-end


Add a node
--------------------------------------------------

.. journeys-node-add-start

Click the plus button to add a node to the journey. May be one of "Activate", "Delay", "Conditional Split", or "Percent Split."

.. image:: ../../images/mockup-journeys-canvas-plus.png
   :width: 280 px
   :alt: Delay node
   :align: left
   :class: no-scaled-link

.. journeys-node-add-end


.. _journeys-howtos:

How-tos
==================================================

.. journeys-howtos-start

Tasks related to building journeys in Amperity:

.. journeys-howtos-end

.. journeys-howtos-list-start

* :ref:`journeys-howtos-add`
* :ref:`journeys-howtos-node-activate`
* :ref:`journeys-howtos-node-conditional-split`
* :ref:`journeys-howtos-node-delay`
* :ref:`journeys-howtos-node-percent-split`
* :ref:`journeys-howtos-allow-reentry`
* :ref:`journeys-howtos-delete`
* :ref:`journeys-howtos-edit`
* :ref:`journeys-howtos-edit-destination-attributes`
* :ref:`journeys-howtos-edit-starting-audience`
* :ref:`journeys-howtos-edit-exit-conditions`
* :ref:`journeys-howtos-interact`
* :ref:`journeys-howtos-monitor-resolve`
* :ref:`journeys-howtos-rename`
* :ref:`journeys-howtos-save-a-journey`
* :ref:`journeys-howtos-schedule-a-journey`
* :ref:`journeys-howtos-view-journey-participant-numbers`
* :ref:`journeys-howtos-view-node-configuration`

.. journeys-howtos-list-start


.. _journeys-howtos-add:

Add a journey
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-about-start
   :end-before: .. journeys-about-end

.. journeys-howitworks-steps-start

Follow this sequence when building a journey:

.. journeys-howitworks-steps-end

.. include:: ../../amperity_user/source/journeys.rst
   :start-after: .. journeys-howitworks-callouts-start
   :end-before: .. journeys-howitworks-callouts-end


.. _journeys-howtos-node-activate:

Add activate nodes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-activate-start
   :end-before: .. term-journey-node-activate-end

**To add an Activate node to a journey** 

.. journeys-howtos-node-activate-steps-start

#. From the **Journeys** canvas, select the plus symbol, and then choose **Activate**.

   .. image:: ../../images/mockup-journeys-canvas-plus-activate.png
      :width: 280 px
      :alt: Activate node
      :align: left
      :class: no-scaled-link

#. Configure the following settings:

   **Name** Give the node a custom name or keep the "Activate" default name.

   **Destination** Choose one or more destinations from the dropdown menu.

   A summary of details is shown. Click the **Attributes** tab to review the list of attributes that are sent.

   **Add another destination** Click the "Add another destination" link to add more destinations to the activation node.

#. Continue building the journey or, if finished, click **Save**.

.. journeys-howtos-node-activate-steps-end

.. tip:: You can add multiple destinations to a single activation node. However, if your destinations require different custom attributes, use separate activation nodes for each destination.

.. _journeys-howtos-node-conditional-split:

Add conditional split nodes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-conditional-split-start
   :end-before: .. term-journey-node-conditional-split-end

**To add a Conditional Split node to a journey**

.. journeys-howtos-node-conditional-split-steps-start

#. From the **Journeys** canvas, select the plus symbol, and then choose **Conditional split**.

   .. image:: ../../images/mockup-journeys-canvas-plus-conditional-split.png
      :width: 280 px
      :alt: Conditional split node
      :align: left
      :class: no-scaled-link

#. Configure the following settings:

   **Name** Give the node a custom name or keep the "Conditional Split" default name.

   **Add new path** Click the "Add new path" link to add paths for this split. Each path requires a sub-audience, which may be defined by a segment or by custom criteria.

   **Name of remaining audience** Amperity uses "Everyone else" to name the audience for customers who do not belong to the segment or custom criteria for a path in this conditional split. You may keep the "Everyone else" default or may add a custom name.

#. Continue building the journey or, if finished, click **Save**.

.. journeys-howtos-node-conditional-split-steps-end


.. _journeys-howtos-node-delay:

Add delay nodes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-delay-start
   :end-before: .. term-journey-node-delay-end

**To add a Delay node to a journey**

.. journeys-howtos-node-delay-steps-start

#. From the **Journeys** canvas, select the plus symbol, and then choose **Delay**.

   .. image:: ../../images/mockup-journeys-canvas-plus-delay.png
      :width: 280 px
      :alt: Delay node
      :align: left
      :class: no-scaled-link

#. Configure the following settings:

   **Name** Give the node a custom name or keep the "Delay" default name.

   **Set delay time** Enter an integer and a unit of time to define length of time to wait before the next step in a journey begins

#. Continue building the journey or, if finished, click **Save**.

.. journeys-howtos-node-delay-steps-end

.. important:: Customers do not automatically move forward after the wait period ends. Progression only occurs the next time the journey runs. 
   
   For example, if a delay node is set to 3 days but the journey is scheduled to run weekly, customers will remain at the delay node until the next scheduled run, potentially waiting up to 7 days. 
   
   If a journey is set to run only once, customers will not move beyond the delay node after it executes.

.. _journeys-howtos-node-percent-split:

Add percent split nodes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-percent-split-start
   :end-before: .. term-journey-node-percent-split-end

**To add a Percent Split node to a journey**

.. journeys-howtos-node-percent-split-steps-start

#. From the **Journeys** canvas, select the plus symbol, and then choose **Percent split**.

   .. image:: ../../images/mockup-journeys-canvas-plus-percent-split.png
      :width: 280 px
      :alt: Percent split node
      :align: left
      :class: no-scaled-link

#. Configure the following settings:

   **Name** Give the node a custom name or keep the "Percent Split" default name.

   **Configure paths** Choose a name and percentage for the treatment path, or keep the default name of "Main Group" and the value of 90%.

   Click the "Add path" link to add more treatments. Each treatment should have a unique name and a percentage value.

   .. important:: The percentages for all paths and the control group must add up to 100%.

   **Configure control group** Choose a name and percentage for the control group, or keep the default name of "Control Group" and the value of 10%.
   
   .. tip:: Uncheck "Include control" to disable the control group.

#. Continue building the journey or, if finished, click **Save**.

.. journeys-howtos-node-percent-split-steps-end

.. _journeys-howtos-allow-reentry:

Allow re-entry
--------------------------------------------------

.. journeys-howtos-allow-reentry-start

If a journey is set to recur, you can allow the same customer to re-enter the journey on its next run if the customer has both previously exited the journey and once again qualifies for the inclusion segment.

.. journeys-howtos-allow-reentry-end

**To allow re-entry into a journey**

.. journeys-howtos-allow-reentry-start

#. From the **Journeys** canvas, open the **Journey setup** sidebar.
#. Click the box on the lower left for **Allow re-entry**.

.. journeys-howtos-allow-reentry-end

.. journeys-howtos-allow-reentry-note-start

.. note:: When a journey is set to run on a recurring schedule, only customers who have newly qualified for the **inclusion** segment since the last run will enter the journey.

   For example, if the segment had 1,500 members at launch, all 1,500 would enter the journey.

   On the next run, if the segment has grown to 1,700, only the 200 new members--those who joined the segment after the previous run--are guaranteed to be included.

   If you have selected **Allow re-entry** customers who have previously exited the journey must re-qualify for the inclusion segment. For example, if the segment is based on a time window, such as "purchased in the last 7 days", and they meet the criteria again, they can re-enter.

   To prevent this, use an **exclusion** segment to filter out users who have already participated, or who meet other disqualifying conditions.

.. journeys-howtos-allow-reentry-note-end


.. _journeys-howtos-delete:

Delete node
--------------------------------------------------

.. journeys-howtos-delete-start

Any node on the **Journeys** canvas can be deleted. This action only deletes the node. All child nodes remain in the journey.

.. journeys-howtos-delete-end

**To delete a node from a journey**

.. journeys-howtos-delete-steps-start

#. From the **Journeys** canvas, select a node the |fa-kebab| menu on the node you wish to delete, then select **Delete**.
#. Continue building the journey or, if finished, click **Save**.

.. journeys-howtos-delete-steps-ende


.. _journeys-howtos-edit:

Edit existing node
--------------------------------------------------

.. journeys-howtos-edit-start

The settings for nodes in a journey can be edited.

.. journeys-howtos-edit-end

**To edit node configuration**

.. journeys-howtos-edit-steps-start

#. From the **Journeys** canvas, select a node.
#. Open **Node Configuration** sidebar, and then make your changes.
#. Continue building the journey or, if finished, click **Save**.

   Alternatively, clicking the **Node configuration** sidebar opens the configuration pane for the most recently edited node.

.. journeys-howtos-edit-steps-end


.. _journeys-howtos-edit-destination-attributes:

Edit destination attributes
--------------------------------------------------

.. journeys-howtos-edit-destination-attributes-start

The attributes that are sent to each destination that are configured for activation in a journey can be edited.

.. journeys-howtos-edit-destination-attributes-end

**To edit destination attributes**

.. journeys-howtos-edit-destination-attributes-steps-start

#. From the **Journeys** canvas, select an activation node.
#. Open the **Node configuration** sidebar. For each configuration destination, a list of attributes may be edited.
#. Select a destination from the **Destination** dropdown.
#. Open the **Attributes** panel. A list of attributes is shown with the field in Amperity on the left and the field that is sent to the destination on the right.
#. Click the **Edit** button to update the list of attributes that are sent to this destination.
#. When finished, click **Save**.

.. journeys-howtos-edit-destination-attributes-steps-end

.. journeys-howtos-edit-destination-attributes-note-start

.. note:: If you have multiple destinations in a single activation node and your destinations require different custom attributes, use separate activation nodes for each destination.

.. journeys-howtos-edit-destination-attributes-note-end


.. _journeys-howtos-edit-starting-audience:

Edit starting audience 
--------------------------------------------------

.. journeys-howtos-edit-starting-audience-start

The starting audience for a journey can be edited.

.. journeys-howtos-edit-starting-audience-end

**To edit the starting audience** 

.. journeys-howtos-edit-starting-audience-steps-start

#. From the **Journeys** canvas, open the **Journey setup** sidebar.
#. Under **Journey entry** use the dropdown menus to edit the included and excluded segments.

   .. image:: ../../images/mockup-journeys-canvas-inclusion-exclusion.png
      :width: 380 px
      :alt: Edit starting audience
      :align: left
      :class: no-scaled-link

.. journeys-howtos-edit-starting-audience-steps-end


.. _journeys-howtos-edit-exit-conditions:

Edit exit conditions
--------------------------------------------------

.. journeys-howtos-edit-exit-conditions-start

The exit criteria for a journey can be edited.

.. journeys-howtos-edit-exit-conditions-end

**To edit exit conditions**

.. journeys-howtos-edit-exit-conditions-steps-start

#. From the **Journeys** canvas, open the **Journey setup** sidebar.
#. Under **Exit conditions** use the dropdown menus to edit the segments that should exit the journey.

   .. image:: ../../images/mockup-journeys-canvas-exit-conditions.png
      :width: 380 px
      :alt: Choose exit conditions
      :align: left
      :class: no-scaled-link

.. journeys-howtos-edit-exit-conditions-steps-end


.. _journeys-howtos-interact:

Interact with Journeys canvas
--------------------------------------------------

.. journeys-howtos-interact-start

The **Journeys** canvas supports the following user interactions:

* Drag the journey using a mouse or a trackpad. You may do this directly on the canvas or on the minimap in the lower right.
* Zoom by using the **+** / **-** buttons in the bottom left or pinching/expanding on a trackpad.
* Center the canvas by clicking the square icon in the bottom left.
 
.. journeys-howtos-interact-end


.. _journeys-howtos-monitor-resolve:

Monitor status & resolve errors
--------------------------------------------------

.. journeys-howtos-monitor-resolve-start

You can monitor journey status and determine how to resolve errors on the `Workflows page <https://docs.amperity.com/reference/workflows.html>`__.

.. journeys-howtos-monitor-resolve-end

.. journeys-howtos-monitor-resolve-steps-start

#. Go to the **Workflows** page at the top level of your Amperity tenant. If you are starting from within the **Journeys** canvas you'll need to exit by clicking the X on the upper left.
#. Locate the name of your journey and click in to monitor status and get guidance on resolving errors.

.. journeys-howtos-monitor-resolve-steps-end

.. journeys-howtos-monitor-resolve-workflow-alerts-start

You may receive workflow alerts related to your journeys.

.. include:: ../../amperity_reference/source/workflows.rst
   :start-after: .. journeys-automated-alert-details-start
   :end-before: .. journeys-automated-alert-details-end

.. journeys-howtos-monitor-resolve-workflow-alerts-end


.. _journeys-howtos-rename:

Rename a journey
--------------------------------------------------

.. journeys-howtos-rename-start

A journey should be assigned a name that makes it easy to find and for other users of Amperity to understand.

.. journeys-howtos-rename-end

**To rename a journey**

.. journeys-howtos-rename-steps-start

#. From the **Journeys** canvas, click into the text of the current journey name at the top.
#. Enter a new name.

.. journeys-howtos-rename-steps-end


.. TODO: add: Set journey description

.. _journeys-howtos-save-a-journey:

Save a journey
--------------------------------------------------

.. journeys-howtos-save-a-journey-start

Saving a journey initiates the workflow, allowing you to view results and return later to make additional edits.

.. journeys-howtos-save-a-journey-end

**To save a journey**

.. journeys-howtos-save-a-journey-steps-start

#. From the **Journeys** canvas, click the **Save** button in the top right.
#. Use the caret button to **Save as**.

.. journeys-howtos-save-a-journey-steps-end

.. journeys-howtos-save-a-journey-tip-start

.. tip:: Saving a journey takes you from **Edit** to **View** mode. In **View** mode, click **Edit** in the upper right to make further changes. Saving again takes you back to **View** mode.

.. journeys-howtos-save-a-journey-tip-end

.. journeys-howtos-save-a-journey-note-start

.. note:: You can save a journey with validation errors as long as it is not scheduled to run. However, if saving the journey would result in it being scheduled, and validation errors are still present, you won't be able to save it until those errors are resolved.

.. journeys-howtos-save-a-journey-note-end


.. _journeys-howtos-schedule-a-journey:

Schedule a journey
--------------------------------------------------

.. journeys-howtos-schedule-a-journey-start

A journey may be configured to run once, daily, weekly, monthly, or quarterly.

.. journeys-howtos-schedule-a-journey-end

**To schedule a journey**

.. journeys-howtos-schedule-a-journey-steps-start

#. From the **Journeys** canvas, click **Edit schedule** in the top navigation.
#. From the **Recurrence** dropdown menu choose one of the options: "once", "every 3 hours", "every 6 hours", "twice daily", "daily", "weekly", "monthly", or "quarterly".

.. journeys-howtos-schedule-a-journey-steps-end

.. journeys-howtos-schedule-a-journey-important-admonition-start

.. important:: Delay nodes require the journey to run again in order to progress. For journeys set to run only once, customers will not move beyond delay nodes. Use recurring schedules to ensure customers continue through the journey after delay node wait periods.

.. journeys-howtos-schedule-a-journey-important-admonition-end

.. journeys-howtos-schedule-a-journey-note-start

.. note:: Once you have saved a journey, the **Edit schedule** option becomes **View schedule**. To make changes to the schedule, click **Edit** on the top right of the **Journeys** canvas.

.. journeys-howtos-schedule-a-journey-note-end


.. _journeys-howtos-view-journey-participant-numbers:

View journey participant numbers
--------------------------------------------------

.. journeys-howtos-view-journey-participant-numbers-start

In **View** mode on the **Journeys** canvas you can see  how many total people have moved through any journey that has run at least once and how many have moved through each node in the current run.

Nodes have icons and numbers, representing journey participants.

   .. image:: ../../images/mockup-journeys-view-participant-numbers.png
      :width: 280 px
      :alt: View journey participant numbers
      :align: left
      :class: no-scaled-link
	  
* The people icon on the left displays how many total participants have moved through the journey across all runs to date.
* The circular arrow on the right displays how many partipants have moved through that node on the current run, as of last evaluation.

A delay node have an additional icon.

   .. image:: ../../images/mockup-journeys-view-participant-numbers-delay.png
      :width: 280 px
      :alt: View journey participant numbers on delay node
      :align: left
      :class: no-scaled-link
	  
* The clock icon displays the number of journey participants currently waiting at that node. 

.. journeys-howtos-view-journey-participant-numbers-end

.. journeys-howtos-view-participant-numbers-tip-start

.. tip:: Once you have saved a journey, it defaults to **View** mode. To exit **View** mode and make changes, click **Edit** on the top right of the **Journeys** canvas.

.. journeys-howtos-view-participant-numbers-tip-end


.. _journeys-howtos-view-node-configuration:

View node configuration
--------------------------------------------------

.. journeys-howtos-view-node-configuration-start

Open a node to view its configuration.

.. journeys-howtos-view-node-configuration-end

**To view the configuration for a node**

.. journeys-howtos-view-node-configuration-steps-start

#. From the **Journeys** canvas, select a node.
#. The current settings for a node are in the **Node configuration** sidebar.

.. journeys-howtos-view-node-configuration-steps-end
