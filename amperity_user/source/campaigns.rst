.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Create campaigns, add audiences, and then send those audiences to many destinations.

.. meta::
    :content class=swiftype name=body data-type=text:
        Create campaigns, add audiences, and then send those audiences to many destinations.

.. meta::
    :content class=swiftype name=title data-type=string:
        Create campaigns

==================================================
Create campaigns
==================================================

.. campaigns-static-intro-start

Sending campaigns from Amperity to downstream marketing workflows is a combination of:

* A :doc:`segment <segments>` that defines the audience that you will use with your campaign.
* A campaign (this topic) that breaks that audience down into sub-audiences that align to your marketing strategies and goals.
* A set of :doc:`destinations <destinations>` that specify the locations and channels to which you will send each sub-audience.

This is part two of a series of topics that describes how this works.

.. campaigns-static-intro-end

.. include:: ../../amperity_reference/source/campaigns.rst
   :start-after: .. campaigns-howitworks-start
   :end-before: .. campaigns-howitworks-end

.. campaigns-howitworks-steps-start

The following sections describe the steps you'll follow to set up and configure a campaign.

.. campaigns-howitworks-steps-end

.. campaigns-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0


   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - The campaign builder is available from the **Campaigns** page. The **Create Campaign** button in the top right corner of the page opens the campaign builder.

       .. image:: ../../images/mockup-campaigns-name.png
          :width: 320 px
          :alt: Give your campaign a name.
          :align: left
          :class: no-scaled-link

       After the campaign builder opens, give your campaign a name.

       .. tip:: Use good naming patterns to ensure that you can always find your campaigns in the various applications to which you will send them. The campaign name will *always* appear in the filename that is sent to any destination.

          Avoid duplication between campaign and treatment group names.

          Avoid using the names of destinations as campaign names unless the campaign is sent to *only* that destination.

          Use a naming pattern that ensures the campaign name works across every treatment group that is configured within any sub-audience.

          If brand names and/or region names apply to all sub-audiences in the campaign, consider using them within the campaign name.

          Some examples:

          * "Birthdays_Under_40"
          * "Acme_Churn"
          * "Churn_HighValue_Early"
          * "Socktown_High_AOV"


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - All campaigns start with an audience. Choose a segment from the **Include** dropdown list. The customers in that list will become the audience for this campaign.

       .. image:: ../../images/mockup-campaigns-select-audience-from-segment.png
          :width: 650 px
          :alt: Choose one (or more) segments to form the audience for this campaign.
          :align: left
          :class: no-scaled-link

       .. tip:: When a campaign starts with an audience that is defined by a single segment, you can use the segment insights for that segment as a way to measure the performance of that audience over time.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - Sometimes campaigns need to exclude certain members of your audience. For example, a churn prevention campaign is often configured to exclude customers who have opted-out of SMS messaging and/or who have unsubscribed from an email list.

       When you need to exclude audience members, choose one (or more) segments from the **Exclude** dropdown list. The customers in an exclusion list will be removed from the audience for this campaign.

       .. image:: ../../images/mockup-campaigns-select-exclusions-from-segment.png
          :width: 650 px
          :alt: Choose one (or more) segments to exclude customers from this campaign.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - Some campaigns have just one audience, while others require sub-audiences.

       Sub-audiences can be many things. How you choose to configure them is dependent on your audience, marketing strategy and goals, and the type of campaign you will run.

       This topic uses sub-audiences to split the combined high-value audience into more specific audiences by lifecycle status.

       Click **Add sub-audience** to open the **Audience Builder**, find the **Predicted CLV Attributes** table, choose the **Predicted Lifecycle Status** attribute, and then select "Active".

       .. image:: ../../images/mockup-segments-tab-lifecycle-status-active.png
          :width: 540 px
          :alt: Choose the "Active" lifecycle status.
          :align: left
          :class: no-scaled-link

       Then update the name of the treatment group. In this example, it's "Active_Socks". This is part of the filename that you will see in the application to which you send this sub-audience. For example: "Churn_HighValue_Early_Active_Socks".

       .. image:: ../../images/mockup-campaigns-select-sub-audience-active.png
          :width: 650 px
          :alt: A sub-audience for customers with an active lifecycle status.
          :align: left
          :class: no-scaled-link

       Assign one (or more) destinations to this treatment group, and then edit the attributes to ensure Amperity is sending the right data.

       .. tip:: Use good naming patterns to ensure that you can always find your campaigns in the various applications to which you will send them. The campaign name will *always* appear in the filename that is sent to any destination and the treatment group name is often appended. Use a naming pattern that allows the treatment group name to build on the campaign name.

          Avoid duplication between campaign and treatment group names.

          Avoid using the names of destinations as treatment group names unless the treatment group is sent to *only* that destination.

          If brand names and/or region names are specific to sub-audiences, consider using the brand names within the treatment group names.

          Add details like "historical", "daily", or "test" as appropriate. Be sure to include the region name if you have multiple regions.

          Some examples:

          * "CA", "NY", "WA"
          * "Region_Daily"
          * "Active", "CoolingDown", or "AtRisk"
          * "90D_Loyalty"

          The campaign and treatment group names are concatenated, typically as **{{ campaign_name }}_{{ recipient_group_name }}**. The campaign and treatment group names become part of the filename that will be visible to users in the application to which you send this treatment group.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - The second sub-audience is similar to the first one, but instead choose the "Cooling down" value from **Predicted Lifecycle Status**.

       .. image:: ../../images/mockup-segments-tab-lifecycle-status-coolingdown.png
          :width: 540 px
          :alt: Choose the "cooling down" lifecycle status.
          :align: left
          :class: no-scaled-link

       Then update the name of the treatment group. In this example, it's "CoolingDown_Socks". This is part of the filename that you will see in the application to which you send this sub-audience. For example: "Churn_HighValue_Early_CoolingDown_Socks".

       .. image:: ../../images/mockup-campaigns-select-sub-audience-cooling-down.png
          :width: 650 px
          :alt: A sub-audience for customers with a cooling down lifecycle status.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: center
          :class: no-scaled-link
     - The third sub-audience is similar to the previous two, but instead choose the "At risk" value from **Predicted Lifecycle Status**.

       .. image:: ../../images/mockup-segments-tab-lifecycle-status-atrisk.png
          :width: 540 px
          :alt: Choose the "At risk" lifecycle status.
          :align: left
          :class: no-scaled-link

       Then update the name of the treatment group. In this example, it's "AtRisk_Socks". This is part of the filename that you will see in the application to which you send this sub-audience. For example: "Churn_HighValue_Early_AtRisk_Socks".

       .. image:: ../../images/mockup-campaigns-select-sub-audience-at-risk.png
          :width: 650 px
          :alt: A sub-audience for customers with an at risk lifecycle status.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: center
          :class: no-scaled-link
     - A campaign can be configured to be sent once or on a recurring basis. A campaign can also be scheduled (i.e. "to be sent at the time you choose in the future") or to be sent as soon as possible.

       .. image:: ../../images/mockup-campaigns-timing.png
          :width: 650 px
          :alt: Give your campaign a name.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step 8.
          :align: center
          :class: no-scaled-link
     - Enter the date on which you plan to launch your campaign. This date helps Amperity improve results tracking and campaign results measurement.

       .. image:: ../../images/mockup-campaigns-launch.png
          :width: 650 px
          :alt: Configure the schedule and timing for your campaign.
          :align: left
          :class: no-scaled-link

       .. include:: ../../amperity_reference/source/campaigns.rst
          :start-after: .. campaigns-timing-and-launch-dates-admonition-start
          :end-before: .. campaigns-timing-and-launch-dates-admonition-end


   * - .. image:: ../../images/steps-09.png
          :width: 60 px
          :alt: Step 9.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../amperity_reference/source/campaigns.rst
          :start-after: .. campaigns-test-campaign-start
          :end-before: .. campaigns-test-campaign-end

       When your campaign is ready, click the **Schedule** button in the top right corner of the **Campaigns** page.

.. campaigns-howitworks-callouts-end
