.. 
.. xxxxx
..



**TEMPLATE SECTIONS FOR CHANNELS**

.. channels-overview-list-intro-start

This topic describes the steps that are required to configure campaigns to send |what-send| to |destination-name|.

.. channels-overview-list-intro-end

.. channels-overview-note-start

.. note:: Ask your DataGrid Operator or your Amperity representative for help configuring |destination-name| as a destination to which you can send campaigns for customer activation.

.. channels-overview-note-end



**BUILD SEGMENT**

.. channels-build-segment-start

Use the **Segment Editor** to build any audience using a series of drop-downs and picklists.

As you define the attribute profile for an audience be sure to refresh segment insights to see how many customers match your audience and to see how much value they bring to your business.

When the segment is ready, activate it, and then use it use it in a campaign to send to your preferred destinations for customer activation.

.. channels-build-segment-end

.. channels-build-segment-context-start

You can use any attribute that is in your customer 360 database to define your audience.

When the list of customers who belong to this audience is sent to |destination-name| as part of a campaign you will be required to choose specific attributes to send.

|destination-name| supports the following attributes: |what-send|.

.. channels-build-segment-context-end


**To build a segment for use with campaigns**

.. TODO: This needs to be updated to reflect the new behaviors in the segment editor. Just moving this over for now.

.. channels-build-segment-steps-start

#. From the **Segments** tab, click **Create Segment**. This opens the **Segment Editor**.
#. Select a table that contains the attributes you want to use, and then use the drop-downs, picklists, conditions, and values to define the attribute profile.

   .. note:: The **Customer 360** table is the default. For many segments it's the only table you will need.
#. When more than one attribute is present within an attribute group use **AND** or **OR** to filter values on more than one condition.
#. Click **Add section** to add additional attribute groups.

   Each attribute group has the same requirement for using **AND** or **OR** to filter values. There is another **AND** versus **OR** choice that must be made in-between each each attribute group.

#. For each attribute group that is added to the segment, select the database table that contains the attributes, and then select attributes.

   .. tip:: Any table that is listed in the lower right may be used to build the attribute profile. Open the **Data Explorer** to learn more about the individual attributes within these tables.

#. To view updated segment insights based on the currently-defined attributes, click **REFRESH**. This will validate the segment, after which segment insights are updated to match the condition-value pairs associated to all of the attributes in the segment.
#. When the segment returns the parameters that meets the goals for your campaign, click **Save**, and then give your segment a name.

.. channels-build-segment-steps-end






**CONFIGURE DEFAULT ATTRIBUTES**


.. channels-configure-default-attributes-start

Each unique destination that is configured to send data to |destination-name| may be configured to have a set of default attributes that will sent to |destination-name| every time this destination is associated with a treatment group in an active campaign.

Default attributes may be configured for a destination by clicking the **Default attributes** link next to the **Create campaign** button on the **Campaigns** page.

The source table is set to **Merged Customers** for most attributes. Your brand may configure each attribute to be pulled from the source table that best represents how your brand wants to use the attribute in |destination-name|.

.. channels-configure-default-attributes-end






**BUILD CAMPAIGN**

.. channels-build-campaign-start

Use the campaign editor to build campaigns that send data to |destination-name|. Add a segment, define exclusions and sub-audiences, and then configure Amperity to send campaign data to |destination-name|.

.. channels-build-campaign-end


.. channels-build-campaign-important-email-or-phone-start

.. important:: |destination-name| supports using |what-send| to identify subscribers. However, a list sent to |destination-name| from Amperity cannot contain a mixture of the two, only one or the other. Verify which attribute you are using within |destination-name| to identify subscribers, and then ensure that only the matching attribute is selected.

.. channels-build-campaign-important-email-or-phone-end


.. channels-build-campaign-important-may-contain-mixed-start

.. important:: |destination-name| supports using |what-send| to identify subscribers. A list sent to |destination-name| from Amperity may contain a mixture of these attributes.

.. channels-build-campaign-important-may-contain-mixed-end


.. channels-build-campaign-important-filedrop-start

.. important:: Use the **Edit Attributes** feature to select the right set of attributes, such as |what-send|, to |destination-name| to support any downstream workflow.

.. channels-build-campaign-important-filedrop-end


**To build a campaign**

.. TODO: The following quote is the "boilerplate" for the "attributes-sent" variable used with all destinations that use file-based campaign sends, including SFTP, Amazon S3, Azure Blob Storage, Google Cloud Storage: "You must select the set of attributes that are sent to |destination-name|. Review your downstream requirements, open the **Edits attributes** page, and then select the attributes you want to send to |destination-name| for this campaign." If this gets updated, review all the campaigns to update the tokens to match this pattern.

.. TODO: The following blocks build out single-sourced "Build a campaign" content for destinations for /ampiq/. They are built into a list-table structure in each topic and the reason why the table is in the topic and the content is here is to allow for the possibility that some destinations may require a unique ordering and/or bespoke content. Work with the docs team first before using unique ordering and/or bespoke content.


.. channels-build-campaign-steps-open-page-start

The campaign builder is available from the **Campaigns** page. The **Create Campaign** button in the top right corner of the page opens the campaign builder.

After the campaign builder opens, give your campaign a name.

.. channels-build-campaign-steps-open-page-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

.. channels-build-campaign-steps-good-names-start

.. tip:: The campaign name will *always* appear in the filename that is sent to any destination.

   Use good naming patterns for the campaigns you will send to |destination-name|. Good naming patterns help ensure that you can easily find your campaigns within Amperity *and* that the campaign is discoverable in |destination-name| by users who may not be the same users who built the campaign in Amperity.

   Avoid duplication between campaign and treatment group names.

   Avoid using |destination-name| in the name *unless* the campaign is sent *only* to |destination-name|.

   Use a naming pattern that ensures the campaign name works across every treatment group that is configured within any sub-audience.

   If brand names and/or region names apply to all sub-audiences in the campaign, consider using them within the campaign name.

.. channels-build-campaign-steps-good-names-end

.. channels-build-campaign-steps-audience-start

All campaigns start with an audience. Choose a segment from the **Include** drop-down list. The customers in that list will become the audience for this campaign.

.. channels-build-campaign-steps-audience-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

.. channels-build-campaign-steps-audience-tip-start

.. tip:: When a campaign starts with an audience that is defined by a single segment, you can use the segment insights for that segment as a way to measure the performance of that audience over time.

.. channels-build-campaign-steps-audience-tip-end

.. channels-build-campaign-steps-exclusions-start

Sometimes campaigns need to exclude certain members of your audience. For example, a churn prevention campaign is often configured to exclude customers who have opted-out of SMS messaging and/or who have unsubscribed from an email list.

When you need to exclude audience members, choose one (or more) segments from the **Exclude** drop-down list. The customers in an exclusion list will be removed from the audience for this campaign.

.. channels-build-campaign-steps-exclusions-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

.. channels-build-campaign-steps-subaudiences-start

Some campaigns have just one audience, while others have many and require sub-audiences.

Sub-audiences can be many things. How you choose to configure them depends on your audience, marketing strategy and goals, and the type of campaign you will run in |destination-name|.

Click **Add treatment** to add another treatment group to a sub-audience. The total percentages for all treatment groups (and the control group, if present) **must** be 100%.

Click **Add Sub-audience** to add more sub-audiences to this campaign, and then use the **Audience Builder** to define the criteria for that sub-audience.

.. channels-build-campaign-steps-subaudiences-end

.. channels-build-campaign-steps-destinations-start

Assign |destination-name| as a destination for at least one treatment group, and then edit the attributes for the sub-audience to ensure Amperity is sending the right data to |destination-name|.

.. channels-build-campaign-steps-destinations-end

.. channels-build-campaign-steps-edit-attributes-start

Click **Edit attributes** to review the attributes that Amperity will send to |destination-name|.

|attributes-sent|

Amperity pre-selects the list of attributes that may be sent to |destination-name|. The **Edit attributes** page for |destination-name| is similar to:

.. channels-build-campaign-steps-edit-attributes-end

.. TODO: There is an image here that is often unique by destination. There are some generic mockups for "email only", "email + phone", "all attributes" and there is a bigger collection of destination-specific ones. Please pay attention to this spot closely and request a destination-specific mockup if you need one.

.. channels-build-campaign-steps-edit-attributes-note-start

.. note:: The **Merged Customers** table is the default table from which data is sent to |destination-name|, even though segments are often built against the **Customer 360** table. This is by design. The **Merged Customers** table is the underlying table for customer profile data and is the source for all customer profile data that exists within the **Customer 360** table.

.. channels-build-campaign-steps-edit-attributes-note-end

.. channels-build-campaign-steps-timing-start

A campaign can be configured to be sent once or on a recurring basis. A campaign can also be scheduled (i.e. "to be sent at the time you choose in the future") or to be sent as soon as possible.

.. image:: ../../images/mockup-campaigns-timing.png
   :width: 650 px
   :alt: Give your campaign a name.
   :align: left
   :class: no-scaled-link

.. channels-build-campaign-steps-timing-end

.. channels-build-campaign-steps-launch-date-start

Enter the date on which you plan to launch your campaign in |destination-name|. This date helps Amperity improve results tracking and campaign results measurement.

.. image:: ../../images/mockup-campaigns-launch.png
   :width: 650 px
   :alt: Configure the schedule and timing for your campaign.
   :align: left
   :class: no-scaled-link

.. channels-build-campaign-steps-launch-date-end

.. channels-build-campaign-steps-schedule-start

When your campaign is ready, click the **Schedule** button in the top right corner of the **Campaigns** page.

.. note:: Amperity will begin processing the segments that define audiences, exclusions, and sub-audiences, and will then send the results to |destination-name|.

Please allow for enough time for Amperity to complete this process before starting a campaign in |destination-name|.

.. channels-build-campaign-steps-schedule-end
