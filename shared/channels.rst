.. 
.. xxxxx
..


.. vale off

**TEMPLATE SECTIONS FOR CHANNELS**

.. vale on

.. vale off

.. channels-overview-list-intro-start

The steps required to configure campaigns to send |what-send| to |destination-name|.

.. channels-overview-list-intro-end

.. vale on

.. vale off

.. channels-overview-note-start

.. note:: Ask your DataGrid Operator or your Amperity representative for help configuring |destination-name| as a destination to which you can send campaigns for customer activation.

.. channels-overview-note-end

.. vale on


.. vale off

**BUILD SEGMENT**

.. vale on

.. channels-build-segment-start

Use the **Segment Editor** to build any audience using a series of drop-downs and picklists.

As you define the attribute profile for an audience be sure to refresh segment insights to view audience size and to see the value it brings to your business.

When the segment is ready, activate it, and then use it use it in a campaign to send to your preferred destinations for customer activation.

.. channels-build-segment-end

.. channels-build-segment-context-start

You can use any attribute that is in your customer 360 database to define your audience.

When sending the list of customers who belong to this audience to |destination-name| as part of a campaign you must choose specific attributes to send.

|destination-name| supports the following attributes: |what-send|.

.. channels-build-segment-context-end


**To build a segment for use with campaigns**

.. TODO: This needs to be updated to reflect the new behaviors in the segment editor. Just moving this over for now.

.. channels-build-segment-steps-start

#. From the **Segments** tab, click **Create Segment**. This opens the **Segment Editor**.

#. Select a table that has the attributes you want to use, and then use the drop-downs, picklists, conditions, and values to define the attribute profile.

   .. note:: The **Customer 360** table is the default.

#. When more than one attribute is present within an attribute group use **AND** or **OR** to filter values on more than one condition.

#. Click **Add section** to add more attribute groups.

   Each attribute group has the same ability to use **AND** or **OR** to filter values for attributes within the attribute group and between each attribute group.

#. For each attribute group added to the segment, select the database table that has the attributes, and then select attributes.

   .. tip:: Use any table shown in the lower right to build the attribute profile. Open the **Data Explorer** to learn more about the individual attributes within these tables.

#. To view updated segment insights, click **REFRESH**. This validates the segment, after which segment insights update to match the condition-value pairs for the attributes in the segment.

#. When the segment returns the parameters that meets the goals for your campaign, click **Save**, and then give your segment a name.

.. channels-build-segment-steps-end






**CONFIGURE DEFAULT ATTRIBUTES**


.. channels-configure-default-attributes-start

Each unique destination configured to send treatment group audiences to |destination-name| has a set of default attributes.

Configure default attributes by clicking the **Default attributes** link next to the **Create campaign** button on the **Campaigns** page.

The source table defaults to the **Merged Customers** table for most attributes. This is configurable.

.. channels-configure-default-attributes-end




.. vale off

**BUILD CAMPAIGN**

.. vale on

.. channels-build-campaign-start

Use the campaign editor to configure Amperity to send data to |destination-name|. Add a segment, define exclusions and sub-audiences, and then define each audience sent to |destination-name|.

.. channels-build-campaign-end


.. channels-build-campaign-important-email-or-phone-start

.. important:: |destination-name| supports using |what-send| to identify subscribers. A list sent to |destination-name| from Amperity cannot contain a mixture of the two, only one or the other. Verify which attribute you are using within |destination-name| to identify subscribers, and then ensure to select only the matching attribute.

.. channels-build-campaign-important-email-or-phone-end


.. channels-build-campaign-important-may-contain-mixed-start

.. important:: |destination-name| supports using |what-send| to identify subscribers. A list sent to |destination-name| from Amperity may contain a mixture of these attributes.

.. channels-build-campaign-important-may-contain-mixed-end


.. channels-build-campaign-important-filedrop-start

.. important:: Use the **Edit Attributes** feature to select the right set of attributes, such as |what-send|, to |destination-name| to support any downstream workflow.

.. channels-build-campaign-important-filedrop-end


**To build a campaign**

.. TODO: The following quote is the "boilerplate" for the "attributes-sent" variable used with all destinations that use file-based campaign sends, including SFTP, Amazon S3, Azure Blob Storage, Google Cloud Storage: "You must select the set of attributes that are sent to |destination-name|. Review your downstream requirements, open the **Edits attributes** page, and then select the attributes you want to send to |destination-name| for this campaign." If this gets updated, review all the campaigns to update the tokens to match this pattern.

.. TODO: The following blocks build out single-sourced "Build a campaign" content for destinations for /ampiq/. They are built into a list-table structure in each topic and the reason why the table is in the topic and the content is here is to allow for the possibility that some destinations may require a unique ordering or bespoke content. Work with the docs team first before using unique ordering or bespoke content.


.. channels-build-campaign-steps-open-page-start

Open the **Campaign Editor**. This is available from the **Campaigns** page. Click the **Create campaign** button in the top right corner of the page.

.. channels-build-campaign-steps-open-page-end

.. channels-build-campaign-steps-destinations-start

Assign |destination-name| as a destination for at least one treatment group.

.. channels-build-campaign-steps-destinations-end

.. channels-build-campaign-steps-destinations-note-start

.. note:: You may need to edit the attributes for the sub-audience to ensure Amperity is sending the right data to |destination-name|.

.. channels-build-campaign-steps-destinations-note-end

.. channels-build-campaign-steps-edit-attributes-start

Click **Edit attributes** to review the attributes that Amperity sends to |destination-name|.

|attributes-sent|

Amperity pre-selects the list of attributes sent to |destination-name|. The **Edit attributes** page for |destination-name| is similar to:

.. channels-build-campaign-steps-edit-attributes-end

.. TODO: There is an image here that is often unique by destination. There are some generic mockups for "email only", "email + phone", "all attributes" and there is a bigger collection of destination-specific ones. Please pay attention to this spot and request a destination-specific mockup if you need one.

.. channels-build-campaign-steps-edit-attributes-note-start

.. note:: The **Merged Customers** table is the default table for sending data to |destination-name|, even though segments are often built against the **Customer 360** table. This is by design. The **Merged Customers** table is the underlying table for customer profile data and is the source for all customer profile data that exists within the **Customer 360** table.

.. channels-build-campaign-steps-edit-attributes-note-end






