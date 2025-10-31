.. 
.. xxxxx
..



.. vale off

**TEMPLATE SECTIONS FOR DATABASE TABLES**

.. vale on






.. vale off

**PASSTHROUGH TABLES**

.. vale on



**To add [table-name] as a passthrough table**

.. tables-add-passthrough-steps-start

#. From the **Campaigns** tab, click **Create Campaign**. This opens the **New Campaign** page.
#. Give your segment a name.
#. Select a table that contains the attributes you want to use, and then use the dropdowns, picklists, conditions, and values to define the attribute profile.

   .. note:: The **Customer 360** table is the default. For many segments it is the only table you need.
#. When more than one attribute is present within an attribute group use **AND** or **OR** to filter values on more than one condition.
#. Click **Add section** to add additional attribute groups.

   Each attribute group has the same requirement for using **AND** or **OR** to filter values. There is another **AND** versus **OR** choice that must be made in-between each attribute group.

#. For each attribute group that is added to the segment, select the database table that contains the attributes, and then select attributes.

   .. tip:: Any table that is listed in the lower right may be used to build the attribute profile. Open the **Data Explorer** to learn more about the individual attributes within these tables.

#. To view updated segment insights based on the defined attributes, click **REFRESH**. This will validate the segment, after which segment insights are updated to match the condition-value pairs associated to all of the attributes in the segment.
#. When the segment returns the parameters that meets the goals for your campaign, click **ACTIVATE**.

.. tables-add-passthrough-steps-end
