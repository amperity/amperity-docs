.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        An activation ID is a unique identifier that is used for precise segmentation and campaign targeting.

.. meta::
    :content class=swiftype name=body data-type=text:
        An activation ID is a unique identifier that is used for precise segmentation and campaign targeting.

.. meta::
    :content class=swiftype name=title data-type=string:
        Activation IDs


==================================================
About activation IDs
==================================================

.. TODO: Keep this as an "all-up" tutorial.

.. activation-ids-intro-start

An activation ID is a unique identifier that your brand can use for precise segmentation and campaign targeting for specific types of marketing activity, such as personalized experiences, tracking customer journeys, and more effective campaign measurement, along with improved return on advertising spend.

The default activation ID within Amperity is the **Amperity ID**. Your brand can configure additional identifiers as activation IDs, such as email addresses, loyalty account IDs, mobile advertising IDs, customer account IDs, or any other unique identifier, to support using segments to build audiences for those activation IDs, and then make those audiences availble for use in campaigns.

.. activation-ids-intro-end


.. _activation-ids-configure:

Configure activation IDs
==================================================

.. TODO: This needs to also be added to the database reference page.

.. activation-ids-configure-start

Additional activation IDs may be configured.

.. activation-ids-configure-end

**To configure activation IDs**

.. activation-ids-configure-steps-start

#. From the **Customer 360** page, open the **Databases** tab.
#. Open a database in **Edit** mode.
#. In the right-side navigation pane, under **Activation IDs**, click **Add activation ID**. This opens the **Activation ID** dialog.
#. Open the **Base table** dropdown.

   Choose a table, and then choose a field in that table that will be used as an activation ID.

#. Required. Assign the activation ID a friendly name, along with a singular and a plural version of the friendly name.

   These terms will be used within the Amperity user interface.

   For example: "Email ID" is the friendly name, "email address" is the singular version, and "email addresses" is the plural version.

   .. important:: Type the friendly name and the singular and plural versions of the friendly name exactly as you want them to appear in the Amperity user interface. These are case-sensitive and are required. For example: "customer_id", "Customer_ID", "Customer ID", or "CustomerID" for the friendly name, "customer ID" for the singular, and "customer IDs" for the plural.

#. Optional. Add a description of the activation ID.
#. Click **Save**, and then **Activate**.

   Activation IDs are available immediately after the database is activated and do not require the database to be run.

.. activation-ids-configure-steps-end


.. _activation-ids-use-in-segments:

Use activation IDs in segments
==================================================

.. TODO: This needs to also be added to the segments reference page.

.. activation-ids-use-in-segments-start

.. TODO: Need an intro here.

#. Create a segment.
#. In the **Segment Editor** select the activation ID from the **Activation ID** dropdown.

   .. important:: Tables and lists are limited to only those that contain a field that matches the selected activation ID.

      For example, if the activation ID is "email_id" then only tables with a field named **email_id** will be available for use with segments or campaigns.

#. The language that is used within the **Segment Editor** is updated to match the friendly, singular, and plural names of the selected activation ID.

   For example, the "Include customers with ALL of the following ..." statement is updated to "Include email addresses with ALL of the following ..." when the plural name is "email addresses".

#. Segment insights are updated to only show the count for records that match the selected activation ID.

   The language that is used to describe segment insights is updated to match the friendly, singular, and plural names of the activation ID.

#. Build the rest of the segment as you would normally, and then click **Save**.

.. activation-ids-use-in-segments-end


.. _activation-ids-use-in-campaigns:

Use activation IDs in campaigns
==================================================

.. TODO: This needs to also be added to the campaigns reference page and maybe to the campaigns topic in user guides.

.. activation-ids-use-in-campaigns-start

The activation ID that is used within a campaign is determined by the activation ID that is present in the segment that is used to define the starting audience for the campaign.

Additional segments that are used for inclusions and exclusions must have a matching activation ID.

Campaign audience counts are updated to reflect the count for records that match the activation ID.

The language that is used within the **Campaign Editor** is updated to match the friendly, singular, and plural names of the activation ID.

For example, the "Customers" column that is associated with audiences (and sub-audiences) is updated to "Email addresses" when the plural name is "email addresses" and the count of customers at the top of the **Campaign Editor** is updated to show "Total email addresses".

Attributes that are useable within campaigns are limited to only attributes that are available from tables that match the activation ID.

.. activation-ids-use-in-campaigns-end


.. _activation-ids-test-campaigns:

Test the campaign
==================================================

.. TODO: This needs to be moved to the /reference/campaigns.rst topic as an alphabetical how-to titled "Test campaigns" along with a "View history of campaign tests" topic. And maybe to the campaigns topic in user guides.

.. activation-ids-test-campaigns-start

Click the **Campaign test** link in the top of the **Campaign Editor** to open the **Campaign tests** dialog box. Configure the number of records to use with the test, and then click **Run test**.

This runs the campaign exactly the same as if it were run in a production workflow. A sample file is output that shows what the results of this campaign will look like downstream.

A history of campaign tests is also available.

.. activation-ids-test-campaigns-end
