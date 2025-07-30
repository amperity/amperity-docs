.. https://docs.amperity.com/reference/

:orphan:

.. meta::
    :description lang=en:
        Use these how tos to help you build segments.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use these how tos to help you build segments. 

.. meta::
    :content class=swiftype name=title data-type=string:
        About building segments

==================================================
How-tos
==================================================

.. segments-how-tos-start

This section describes tasks related to building segments in Amperity:

.. segments-how-tos-end

.. segments-howtos-list-start

* :ref:`segments-add-attribute-from-table`
* :ref:`segments-add-conditions`
* :ref:`segments-add-exclusion`
* :ref:`segments-add-purchase-behaviors`
* :ref:`segments-add-section`
* :ref:`segments-baseline-chart-source`
* :ref:`segments-change-comparison-dates`
* :ref:`segments-segment-database-source`
* :ref:`segments-change-date`
* :ref:`segments-choose-activation-id`
* :ref:`segments-choose-andor`
* :ref:`segments-compare`
* :ref:`segments-select-segment-comparison-chart`
* :ref:`segments-copy-column`
* :ref:`segments-copy-segment-id`
* :ref:`segments-copy-sql-query`
* :ref:`segments-create-campaign`
* :ref:`segments-create-customer-list`
* :ref:`segments-create-sql-segment-in-folder`
* :ref:`segments-customize-charts`
* :ref:`segments-delete-segment`
* :ref:`segments-download-segment`
* :ref:`segments-duplicate-segment`
* :ref:`segments-edit-segment`
* :ref:`segments-edit-segment-editor`
* :ref:`segments-expand-graph`
* :ref:`segments-explore-copy`
* :ref:`segments-format-segment`
* :ref:`segments-create-new-segment-from-overlap`
* :ref:`segments-organize-segments`
* :ref:`segments-rename-segment`
* :ref:`segments-rerun-segment`
* :ref:`segments-search-segment`
* :ref:`segments-select-database`
* :ref:`segments-select-multi-values`
* :ref:`segments-set-default-charts`
* :ref:`segments-configure-segments`
* :ref:`segments-show-columns`
* :ref:`segments-switch-sql-segment`
* :ref:`segments-use-relative-dates`
* :ref:`segments-view-segment`
* :ref:`segments-view-edit-history`
* :ref:`segments-view-matching-records`
* :ref:`segments-view-segment-overlap`
* :ref:`segments-view-sql`

.. segments-howtos-list-end





.. _segments-add-attribute-from-table:

Add attribute from table
==================================================

.. segments-add-attribute-from-table-start

You can add attributes from a customer 360 database table to a segment on the **Segment Editor**.

.. segments-add-attribute-from-table-end

**To add an attribute from a table to a segment**

.. segments-add-attribute-from-table-steps-start

#. From the **Segment Editor**, click **Add condition**.
#. Choose **Attributes**, and then select a table.
#. Choose an attribute from the table, and then define the criteria for the attribute.

.. segments-add-attribute-from-table-steps-end


.. _segments-comment:

Add comment to SQL segment
==================================================

.. segments-comment-start

You can add comments to the query in a segment.

.. segments-comment-end

**To add comments to a query**

.. segments-comment-start

#. From the **Segment Editor**, click **View SQL**
#. On the **Visual SQL** window, click **Convert to SQL segment**.
#. On the **Segment Editor**, click **Comment**.
#. Move your cursor to where you want to add a comment. Enter your comments.
#. Click **Activate**.

.. segments-comment-end


.. _segments-add-conditions:

Add conditions
==================================================

.. segments-add-conditions-start

Conditions are the fields in your data tables that your brand uses to create segments, define audiences, and build campaigns.

.. segments-add-conditions-end


.. _segments-add-exclusion:

Add exclusions
==================================================

.. segments-add-exclusion-start

You can add a list of customers to exclude from your segment.

.. segments-add-exclusion-end

**To add an exclusion to a segment**

.. segments-add-exclusion-steps-start

#. From the **Segments** page, select **Create segment**. This opens the **Segment Editor**.
#. After you add conditions, click **Add exclusions**.
#. You can exclude customers by **Purchase behavior**, **Attributes**, or **Customer lists**.

.. segments-add-exclusion-steps-end


.. _segments-add-purchase-behaviors:

Add purchase behaviors
==================================================

.. segments-add-purchase-behavior-start

Purchase behaviors are a feature of Amperity that are built on top of standard output for transactions (orders and items). Purchase behaviors require standardized product catalog field names to be present in your standard output for transactions.

Use purchase behaviors in segments to return a list of customers, *and then* filter that list of customers by any combination of brand, channel, individual items in your product catalog, and store.

Purchase behaviors are available for :doc:`first purchase <attribute_purchase_behavior_first_purchase>`, :doc:`has not purchased <attribute_purchase_behavior_has_not_purchased>`, :doc:`has purchased <attribute_purchase_behavior_has_purchased>`, :doc:`most frequent order <attribute_purchase_behavior_most_frequent_order>`, :doc:`repeat purchase <attribute_purchase_behavior_repeat_purchase>`, and :doc:`total value of orders <attribute_purchase_behavior_total_value_of_orders>`.

You can add purchase behaviors to segments from the **Segment Editor**.

.. segments-add-purchase-behavior-end

**To add purchase behaviors to a segment**

.. segments-add-transactional-behavior-steps-start

#. From the **Segment Editor**, click **Add condition**.
#. Open **Purchase behaviors**, and then select a purchase behavior attribute.
#. Define the criteria for the attribute.

.. segments-add-transactional-behavior-steps-end


.. _segments-add-section:

Add sections
==================================================

.. segments-add-section-start

You can add sections to a segment on the **Segment Editor**

.. segments-add-section-end

**To add a section to a segment**

.. segments-add-section-steps-start

#. From the **Segment Editor**, click **Add section**.
#. Click **Add condition** to add a set of conditions to the section.

.. segments-add-section-steps-end


.. _segments-baseline-chart-source:

Change baseline comparison
==================================================

.. segments-change-baseline-chart-start

You can choose to compare additional segments to a segment of all customers or you can compare to the current segment.

.. segments-change-baseline-chart-end

**To change the baseline comparison chart**

.. segments-change-baseline-chart-steps-start

#. From the **Segments** page, select a segment then click the **Customers** tab.
#. In the **Comparing to** field, choose **All customers** or choose **This segment**.

.. segments-change-baseline-chart-steps-end


.. _segments-change-comparison-dates:

Change comparison date range
==================================================

.. segments-change-comparison-dates-start

You can change the comparison date range on the **Breakdown** tab.

.. segments-change-comparison-dates-end

**To change the date range of a comparison chart**

.. segments-change-comparison-dates-steps-start

#. From the **Segments** page, on the **Breakdown** tab, click the date range field.
#. Select a date range from the menu.

.. segments-change-comparison-dates-steps-end


.. _segments-segment-database-source:

Change database source
==================================================

.. segments-change-database-source-start

You can change the database that a segment retrieves data from.
 
.. note:: Changing the database for a segment will remove all the segment conditions and the resulting customer lists. It will also change any campaign that uses this segment.

.. segments-change-database-source-end

**To change the segment database source**

.. segments-change-database-source-steps-start

#. From the **Segments** page, open the menu for a segment.
#. Click **Edit**.
#. On the right side of the **Segment Editor** under **Database**, pick a database.
#. Choose **Clear segment**.

.. segments-change-database-source-steps-end


.. _segments-change-date:

Change insights date range
==================================================

.. segments-change-date-start

You can change the date range for all the insight details charts.

.. segments-change-date-end

**To change the date range for the insight details**

.. segments-change-date-steps-start

#. From the **Segments** page, select a segment and then click the **Breakdown** tab.
#. On the right side of the page, choose a date range from the dropdown with date ranges.
#. View the updated dates on the horizontal axis of each insight chart.

.. segments-change-date-steps-end


.. _segments-choose-activation-id:

Choose activation ID
==================================================

.. segments-choose-activation-id-start

You can configure a segment to use any activation ID that is configured in your tenant.

Tables and lists are limited to only those that contain a field that matches the selected activation ID.

For example, if the activation ID is "email_id" then only tables with a field named **email_id** will be available for use with segments or campaigns.

The language that is used within the **Segment Editor** is updated to match the friendly, singular, and plural names of the selected activation ID.

For example, the "Include customers with ALL of the following ..." statement is updated to "Include email addresses with ALL of the following ..." when the plural name is "email addresses".

Segment insights are updated to only show the count for records that match the selected activation ID and the language is updatedf.

.. segments-choose-activation-id-end

**To choose an activation ID**

.. segments-choose-activation-id-steps-start

#. Create a segment.
#. In the **Segment Editor** select an activation ID from the **Activation ID** dropdown. The language in the **Segment Editor** is updated to match the configured activation ID.
#. Build the rest of the segment as you would normally, and then click **Save**.

.. segments-choose-activation-id-steps-end


.. _segments-choose-andor:

Choose AND/OR from toggle
==================================================

.. segments-choose-andor

When you add a condition, select either **AND** or **OR**  on the toggle for the conditional operator.

.. segments-choose-andor-end


.. _segments-compare:

Compare segment insights
==================================================

.. segments-compare-start

You can compare segment by the following:

* Purchasers percentage 
* Revenue percentage
* Revenue/Purchaser

.. segments-compare-end

**To update compare segments**

.. segments-compare-add-steps-start

#. From the **Breakdown** tab click the down arrow in the **Compare by:** field.
#. Select one of the following options from the list:

   * **% of Purchasers**
   * **% of Revenue**
   * **Revenue/Purchaser**

.. segments-compare-add-steps-end


.. _segments-select-segment-comparison-chart:

Configure overlap chart
==================================================

.. segments-select-segment-comparison-chart-start

You can select one or more segments to compare in a chart. 

.. segments-select-segment-comparison-chart-end

**To select a segment for a comparison chart**

.. segments-select-segment-comparison-chart-steps-start

#. From the **Segments** page, select a segment and then click the **Compare** tab.
#. Under **Segments** click **Select segment**.
#. Choose one or more segments to compare and then click **Compare**.

.. segments-select-segment-comparison-chart-end


.. _segments-copy-column:

Copy a column to the clipboard
==================================================

.. segments-copy-column-start

You can copy a column of customer data to the clipboard so you can paste it in other applications.

.. segments-copy-column-end

**To copy a column of customer data to the clipboard**

.. segments-copy-column-steps-start

#. From the **Segments** page, select a segment and then click the **Customers** tab.
#. Open the menu for a column.
#. Click **Copy column to clipboard**.

.. segments-copy-column-steps-end


.. _segments-copy-segment-id:

Copy a segment ID
==================================================

.. segments-copy-segments-start

You can copy a segment ID on the **Segments** page.

.. segments-copy-segments-end

**To copy a segment ID**

.. segments-copy-segments-steps-start

#. From the **Segments** page, open the menu for a segment.
#. In the menu, click **Copy ID**.
#. Paste the segment ID in the appropriate location.

.. segments-copy-segments-steps-end


.. _segments-copy-sql-query:

Copy a SQL Query
==================================================

.. segments-copy-sql-start

You can copy a SQL query from the **Segment Editor**.

.. segments-copy-sql-end

**To copy a SQL Query**

.. segments-copy-sql-steps-start

#. From the **Segment Editor**, click **View SQL**
#. On the **View SQL** window, click **Convert to SQL Segment**.
#. On the **Segment Editor**, click **Copy as SQL Query**.
#. On the **Copy as SQL Query** window, click **Copy as SQL Query**.
#. When finished, click **Activate**.

   .. tip:: To include customer matches, you can select the **Include "Customer Matches" columns** option.

.. segments-copy-sql-steps-end


.. _segments-create-campaign:

Create a campaign
==================================================

.. segments-create-campaign-start

You can access the campaign editor from the **Segments** page.

.. segments-create-campaign-end

**To create a campaign**

.. segments-create-campaign-steps-start

#. From the **Segments** page, select a segment.
#. Click **Actions** (upper-right corner) and then click **Create campaign**.

The Segments editor opens.

.. segments-create-campaign-steps-end


.. _segments-create-customer-list:

Customer lists
==================================================

.. segments-create-customer-list-start

You can define a segment from customer lists in the **Segment Editor**:

* :ref:`Using a segment <segments-add-segments-segment>`
* :ref:`Using a query <segments-add-query-segment>`
* :ref:`Using an uploaded file <segments-add-files-segment>`

.. create-segment-customer-list-end

.. _segments-add-query-segment:

Use query
--------------------------------------------------

.. segments-add-query-start

You can add query results to a segment from the **Segment Editor**.

.. segments-add-query-end

**To add query results to a customer list**

.. segments-add-query-steps-start

#. From the **Segment Editor** window, click **Add condition**.
#. Select **Customer lists**, and then choose **Query**.
#. In the **Select query** dialog, choose a query, and then click **Confirm**.

.. segments-add-query-steps-end

.. _segments-add-segments-segment:

Use segment
--------------------------------------------------

.. segments-add-files-segment-start

You can add a segment to a segment from the **Segment Editor**.

.. segments-add-files-segment-end

**To add a segment to a customer list**

.. segments-add-files-segment-steps-start

#. From the **Segment Editor** window, click **Add condition**.
#. Select **Customer lists**, and then choose **Segment**.
#. In the **Select segment** dialog, choose a query, and then click **Confirm**.

.. segments-add-files-segment-steps-end


.. _segments-add-files-segment:

Use uploaded file
--------------------------------------------------

.. segments-add-files-segment-start

You can add data in uploaded files to a segment from the **Segment Editor**.

.. segments-add-files-segment-end

**To add uploaded files to a customer list**

.. segments-add-files-segment-steps-start

#. From the **Segment Editor** window, click **Add condition**.
#. Select **Customer lists**, and then choose **File upload**.
#. In the **Select file upload** dialog, choose a query, and then click **Confirm**.

.. segments-add-files-segment-steps-end


.. _segments-create-sql-segment-in-folder:

Create SQL segment in a folder
==================================================

.. segments-create-sql-segment-in-folder-start

You can create a SQL segment from a folder on the Segments page. 

.. segments-create-sql-segment-in-folder-end

**To create a SQL segment in a folder**

.. segments-create-sql-segment-in-folder-steps-start

#. From the **Segments** page, open the menu for a folder.
#. Click **Create SQL segment**.

The SQL **Segment Editor** appears.

.. segments-create-sql-segment-in-folder-steps-end

.. _segments-visual-segment-in-folder:

Create segment in a folder
==================================================

.. segments-create-visual-segment-in-folder-start

You can create a visual segment from a folder on the Segments page. 

.. segments-create-visual-segment-in-folder-end

**To create a visual segment in a folder**

.. segments-create-visual-segment-in-folder-steps-start

#. From the **Segments** page, open the menu for a folder.
#. Click **Create visual segment**.

The visual **Segment Editor** appears.

.. segments-create-visual-segment-in-folder-steps-end


.. _segments-customize-charts:

Customize comparison charts
==================================================

.. segments-customize-charts-start

You can customize insights charts on the **Breakdown** tab.

.. segments-customize-charts-end

**To customize insights charts**

.. segments-customize-charts-start

#. From the **Breakdown** tab, in the **Attributes breakdown** section, click **Customize**.
#. On the **Customize breakdown charts** window, you can select up to 6 customer attributes, behavioral attributes, and default attributes. You can also uncheck default attributes that you don't want to use.
#. Once done updating the insights charts, click **Apply**.

The default charts are available to all users of the **Breakdown** tab.

   .. note:: To reset the insight charts to the default charts, click **Reset** at the bottom of the **Customize Insights Charts** window.


.. segments-customize-charts-end


.. _segments-delete-segment:

Delete a segment
==================================================

.. segments-delete-segments-start

You can delete a segment from the **Segments** page.

.. segments-delete-segments-end

**To delete a segment**

.. segments-delete-segments-steps-start

#. From the **Segments** page, open the menu for a segment.
#. In the menu, click **Delete**.
#. On the **Delete Segment** window, click **Confirm**.

.. segments-delete-segments-steps-end


.. _segments-download-segment:

Download segment
==================================================

.. segments-download-start

You can download segment results as a CSV file. The CSV format is supported by many applications, which makes the format a great way to test the potential of orchestrating segments for downstream applications and workflows.

.. note:: You cannot download the results of any segment that returns an error.

.. segments-download-end

**To download a segment as a CSV file**

.. segments-download-steps-start

#. From the **Segments** page, open the menu for a segment, and then select a segment.
#. Click the **Customers** page.
#. Click **Download**.
#. A CSV file with a filename that is identical to the segment name is downloaded to your local machine.

.. segments-download-steps-end


.. _segments-duplicate-segment:

Duplicate segment
==================================================

.. segments-duplicate-segments-start

You can duplicate a segment from the **Segments** page.

.. segments-duplicate-segments-end

**To duplicate a segment**

.. segments-duplicate-segments-steps-start

#. From the **Segments** page, open the menu for a segment.
#. Click **Duplicate**.
#. On the **Segment Editor**, make your changes, and then click **Save As**. Add a name and choose where to save the segment.
#. Click **Save**.

.. segments-duplicate-segments-steps-end


.. _segments-edit-segment:

Edit segment from Segments page
==================================================

.. segments-edit-segments-start

You can edit a segment from the **Segments** page.

.. segments-edit-segments-end

**To edit a segment**

.. segments-edit-segments-steps-start

#. From the **Segments** page, open the menu for a segment.
#. Click **Edit**.
#. On the **Segment Editor**, make your changes, and then click **Save**.

.. segments-edit-segments-steps-end


.. _segments-edit-segment-editor:

Edit segment from Segment Editor
==================================================

.. segments-edit-segments-editor-start

You can edit a segment from the **Segment Editor**.

.. segments-edit-segments-editor-end

**To edit a segment from the Segment Editor**

.. segments-edit-segments-editor-steps-start

#. From the **Segment Editor**, click **Actions** (upper-right corner).
#. Click **Edit**.
#. Make your changes and then click **Save**.

.. segments-edit-segments-editor-steps-end


.. _segments-expand-graph:

Expand a graph
==================================================

.. segments-expand-graph-start

You can expand graphs on the **Breakdown** tab.

.. segments-expand-graph-end

**To expand a graph**

.. segments-expand-graph-steps-start

#. From the **Breakdown** tab, open the menu for a graph.
#. Click **Expand**.

   The graph opens up in a window with more details.

.. segments-expand-graph-steps-end

.. _segments-explore-copy:

Explore a segment copy
==================================================

.. segments-explore-copy-start

You can explore a copy of a saved segment on the **Summary** tab.

.. segments-explore-copy-end

**To explore a copy of a saved segment**

.. segments-explore-copy-steps-start

#. From the **Summary** tab, click **Explore a Copy**.
#. From the **Segments Editor**, you can do one of the following:

   Explore the saved segment attribute details

   Add new attributes, conditions, and filters to the segment copy
#. When done, either click **Save As** to copy the saved segment, *or* click **View** to view the segment insights on the **Summary** tab, *or* click **Cancel**.

.. segments-explore-copy-steps-end


.. _segments-format-segment:

Format a SQL segment
==================================================

.. segments-edit-segments-start

You can format a segment from the **Segments** page.

.. segments-edit-segments-end

**To format a segment**

.. segments-edit-segments-steps-start

#. From the **Segments** page, open the menu for a segment.
#. Click **Edit**.
#. Click the **Format** button.

.. segments-edit-segments-steps-end


.. _segments-create-new-segment-from-overlap:

New segment from intersection
==================================================

.. segments-create-new-segment-from-overlap-start

You can create a new segment from the intersections of overlapping segments. 

.. segments-create-new-segment-from-overlap-end

**To create a new segment from intersections**

.. segments-create-new-segment-from-overlap-steps-start

#. From the **Segments** page, select a segment and then click the **Compare** tab.
#. Under **Segments**, choose **Select segment** to add more segments to compare.
#. In the **Overlap** tab, under **Overlapping customers**, choose **New segment from intersection**.

The visual **Segment Editor** appears.

.. note:: You can change the baseline comparison segment on the **Metrics** tab in the **Comparing to** field.

.. segments-create-new-segment-from-overlap-steps-end


.. _segments-organize-segments:
 
Organize segments
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-segment-folder-start
   :end-before: .. term-segment-folder-end

You can organize the segments shown in the **Segments** page:

* :ref:`Add a folder <segments-add-folders>`
* :ref:`Add a subfolder <segments-add-subfolders>`
* :ref:`Move a segment to another folder <segments-move-segment>`
* :ref:`Save segment to a folder <segments-save-segments-to-folder>`
* :ref:`Bulk delete segments <segments-bulk-delete-segments>`
* :ref:`Bulk move segments <segments-bulk-move-segment>`


.. _segments-add-folders:

Add folders
--------------------------------------------------

.. segments-add-folder-start

Folders may be expanded (or collapsed) to view (and hide) the list of segments and subfolders contained within.

.. segments-add-folder-end

**To add a folder**

.. segments-add-folder-steps-start

#. From the **Segments** page click **Create folder**, and then select **Add Folder**. This opens the **Create Folder** dialog box.
#. Enter the name for the folder.
#. Click **Create**.

.. segments-add-folder-steps-end

.. _segments-add-subfolders:

Add subfolders
--------------------------------------------------

.. segments-list-organize-subfolder-start

Use the **Create folder** option in the menu to add up to three levels of subfolders. All folder names must be unique.

.. segments-list-organize-subfolder-end

**To add a subfolder**

.. segments-add-subfolder-steps-start

#. From the **Segments** page, open the menu for a folder, and then select **Create folder**. This opens the **Create Folder** window.
#. Enter the name for the folder.
#. Click **Save**.

.. segments-add-a-subfolder-steps-end


.. _segments-move-segment:

Move segment
--------------------------------------------------

.. segments-list-move-segment-start

Use the **Move** option to move around and organize the list of folders and segments. Folders may be expanded (or collapsed) to view (and hide) the list of segments and subfolders contained within.

.. segments-list-move-segment-end

**To move a segment**

.. segments-move-steps-start

#. From the **Segments** page, open the menu for a segment, and then select **Move**. This opens the **Move Segment** dialog box.
#. Select the name of an existing folder to which a segment will be moved, and then click **Move**.

.. segments-move-steps-end

.. segments-move-hint-start

.. hint:: If the folder to which a segment will be moved is not present in the list of folders, you can add it directly from the **Move Segment** dialog box. Click the **+ New folder** link, type a name for the folder, and then select it.

.. segments-move-hint-end

.. _segments-save-segments-to-folder:

Save segment to a folder
--------------------------------------------------

.. segments-save-segments-to-folder-start

You can save a segment into a folder from the **Segment Editor**.

.. segments-save-segments-to-folder-end

**To save a segment to a folder from the Segment Editor**

.. segments-save-segments-to-folder-steps-start

#. From the **Segment Editor**, click **Save as**. 
#. From the **Save as a new segment** window, enter the name in the **Name** field.
#. In the **Location** section, select the folder or subfolder.
#. Click **Save**.

.. segments-save-segments-to-folder-steps-end


.. _segments-bulk-delete-segments:

Bulk delete segments
--------------------------------------------------

.. segments-bulk-delete-segments-start

You can delete multiple segments from the **Segments** page.

.. segments-bulk-delete-segments-end

**To delete multiple segments**

.. segments-bulk-delete-segments-steps-start

#. From the **Segments** page, select multiple segments.
#. On the bottom of the **Segments** page, click **Delete**.
#. On the **Bulk Delete** window, click **Delete <#> Items**.

.. segments-bulk-delete-segments-steps-end


.. _segments-bulk-move-segment:

Bulk move segments
--------------------------------------------------

.. segments-bulk-move-segments-start

You can move multiple segments to a folder from the **Segments** page.

.. segments-bulk-move-segments-end

**To move multiple segments to a folder**

.. segments-bulk-move-segments-steps-start

#. From the **Segments** page, select multiple segments.
#. On the bottom of the **Segments** page, click **Move**.
#. On the **Bulk Move** window, select a folder.
#. Click **Move**.

.. segments-bulk-move-segments-end


.. _segments-rename-segment:

Rename a segment
==================================================

.. segments-rename-segments-start

You can rename a segment from the **Segments** page.

.. segments-rename-segments-end

**To rename a segment**

.. segments-rename-segments-steps-start

#. From the **Segments** page, open the menu for a segment.
#. Click **Rename**.
#. On the **Rename segment** window, enter a name.
#. Click **Save**.


#. From the **Segment** page, click **Actions** (upper-right corner).
#. Click **Rename**.
#. Enter a name and then click **Save**.

.. segments-rename-segments-steps-end


.. _segments-rerun-segment:

Rerun a segment
==================================================

.. segments-rerun-segments-start

You can rerun a segment from the **Segments** page.

.. segments-rerun-segments-steps-end

**To rerun a segment**

.. segments-rerun-segments-steps-start

#. From the **Segments** page, on the **Customers** page, click **Rerun**.
#. The system reruns the segment the customer data on the **Customers** page is updated.

.. segments-rerun-segments-steps-end


.. _segments-search-segment:

Search segments
==================================================

.. segments-search-segment-start

You can search for segments on the **Segments** page.

.. segments-search-segment-end

**To search for a segment**

.. segments-search-segment-steps-start

#. On the top of the **Segments** page, enter the name of the segment into the search field.

   .. tip:: Select the **Also search segment content** option to search segment content.

.. segments-search-segment-steps-end


.. _segments-select-database:

Select database
==================================================

.. segments-select-database-start

You can build a segment against any database that is visible from the **Customer 360** page.

.. segments-select-database-end

**To select a database**

.. segments-select-database-steps-start

#. From the **Segments** page, click **Create segment**, and then select **Visual Segment**. This opens the **Segment Editor**.
#. Under **Database**, select a database. The **Customer 360** database is selected by default.
#. Build your segment against the list of tables that are available in that database.

.. segments-select-database-steps-end


.. _segments-select-multi-values:

Select multiple values
==================================================

.. segments-select-multiple-values-start

You can select multiple values from the **Segment Editor**.

.. segments-select-multiple-values-end

**To add attribute groups to a segment**

.. segments-select-multiple-values-steps-start

#. From the **Segment Editor**, click **Add condition**.
#. Select a table or search for an attribute in the search field.
#. Select a condition.
#. In the field, search for or select values.

   .. tip:: You can search for a value and then easily select all options in the list of values that appears by selecting the **Select all** checkbox.

#. Click **Save**.
#. When done adding criteria and sections, click **Save** to update the segment.

.. segments-select-multiple-values-steps-end


.. _segments-set-default-charts:

Set default charts
==================================================

.. segments-set-default-charts-start

You can set and default charts from the **Segment Editor**.

.. segments-set-default-charts-end

**To set default charts**

.. segments-set-default-charts-steps-start

#. From the **Segment Editor**, click **Actions**.
#. In the list that appears, click **Set default charts**.
#. On the **Set default breakdown charts** window, you can either select up to 6 customer attributes *or* select up to 6 behavioral attributes.
#. Once done updating the default charts, click **Save**.

   The default charts are available to all users of the **Segments** page.

.. segments-set-default-charts-end


.. _segments-configure-segments:

Set recommended segments
==================================================

.. segments-configure-segments-start

Up to five segments may be configured to show in the list of recommended segments. (Ask your Amperity representative to configure the list of recommended segments for your tenant.)

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - From the **Segments** page, under **Recommended segments**, click **Configure**.

       .. image:: ../../images/mockup-segments-recommended-configure-click.png
          :width: 420 px
          :alt: Click the "Configure" link to configure recommended segments
          :align: left
          :class: no-scaled-link

       This opens the **Configure recommended segments** dialog box.

       For each recommended segment, use the dropdown list to choose a segment

       .. image:: ../../images/mockup-segments-recommended-select.png
          :width: 380 px
          :alt: Select a segment to be a recommended segment.
          :align: left
          :class: no-scaled-link

       and then choose an icon.

       .. image:: ../../images/mockup-segments-recommended-configure-icons.png
          :width: 280 px
          :alt: Select an icon to associate with each recommended segment.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Up to five recommended segments may be configured.

       .. image:: ../../images/mockup-segments-recommended-configure.png
          :width: 380 px
          :alt: Configure recommended segments.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - When your tenant has more than one database, you can select the list of recommended segments for *each database*.

       .. image:: ../../images/mockup-segments-recommended-configure-multibrand.png
          :width: 380 px
          :alt: Select an icon to associate with each recommended segment.
          :align: left
          :class: no-scaled-link

       From the **Segments** page, you can switch between the lists of recommended segments by choosing a database from the "Showing segments for ..." dropdown.

       .. image:: ../../images/mockup-segments-recommended-choose-database.png
          :width: 420 px
          :alt: Select a database.
          :align: left
          :class: no-scaled-link

.. segments-configure-segments-end


.. _segments-show-columns:

Show columns
==================================================

.. segments-show-columns-start

You can view columns that are in the segment results from the **Customers** page in the segment viewer. This can be configured to show all columns from all tables or only columns from a specific table.

.. segments-show-columns-end

**To show columns**

.. segments-show-columns-steps-start

#. From the **Segments** page, open the menu for a segment, and then select **Edit**. This opens the **Segment Editor**.
#. Click the **Customers** page.
#. Expand the **Show [x] columns from [table]** link.
#. Use the **Show all columns** and **Show only the columns I choose** options to configure which columns are shown.
#. Click **Refresh** to update the segment results to show the configured set of columns.

.. segments-show-columns-steps-end


.. _segments-switch-sql-segment:

Switch to SQL segment
==================================================

.. segments-switch-to-sql-start

You can switch a visual segment to a SQL segment.

.. segments-switch-to-sql-end

**To switch to a SQL segment**

.. segments-switch-to-sql-steps-start

#. From the **Segment Editor**, open a segment.
#. In the **Segment Editor**, in the top right, click **View SQL**.
#. Click **Convert to SQL Segment**.

.. segments-switch-to-sql-steps-end


.. _segments-use-relative-dates:

Use relative dates
==================================================

.. segments-use-relative-dates-start

A relative date is determined at the time a segment is run, where **today** is the day on which the segment is run. For example: **yesterday**, **30 days ago**, **14 days ago**, or **1 year ago**.

.. segments-use-relative-dates-end

**To use relative dates for a segment**

.. segments-use-relative-dates-steps-start

#. From the **Segment Editor**, click **Add condition**, and then choose an attribute with a date or datetime value.
#. Select the **Use relative dates** option, and then specify the relative date (or dates) that match the condition you selected. For example: “30 days ago”.
#. Click **Refresh** to validate the segment.
#. Click **Save As**.

.. tip:: To build a segment using relative dates, Amperity turns datetime fields into dates.

.. segments-use-relative-dates-steps-end


.. _segments-view-segment:

View a segment
==================================================

.. segments-view-segment-start

You can view a segment on the **Segments** page.

.. segments-view-segment-end

**To view a segment**

.. segments-view-segment-steps-start

#. From the **Segments** page, click on a segment.
#. The segment appears displaying a summary page with insight details.

.. segments-view-segment-steps-end


.. _segments-view-edit-history:

View edit history
==================================================

.. segments-view-edit-history-start

You can view information on the edit history for a segment from the **Segments** page.

.. segments-view-edit-history-end

**To view the edit history for a segment**

.. segments-view-edit-history-steps-start

#. From the **Segments** page, open the menu for a segment.
#. Click **Version History**.

The **Segment history** window appears with informations about who edited the segment, the date(s) when the segment was edited, and the description(s) of what was edited.

.. segments-view-edit-history-steps-end


.. _segments-view-matching-records:

View matching records
==================================================

.. segments-view-matching-records-start

You can view matching records from a table from the **Customers** page on the **Segments** page.

.. segments-view-matching-records-end

**To view matching records from a table**

.. segments-view-matching-records-steps-start

#. From the **Segments** page, on the **Customers** page, expand the **Show [x] columns from [table]** link.
#. Click in the **Show matching records from:** field.
#. In the list that appears, select a table.

.. segments-view-matching-records-steps-end


.. _segments-view-segment-overlap:

View overlap between segments
==================================================

.. segments-view-segment-overlap-start

You can view and compare the overlap between segments.

.. segments-view-segment-overlap-end

**To view the overlap between segments**

.. segments-view-segment-overlap-steps-start

#. From the **Segments** page, select a segment and then click the **Compare** tab.
#. The overlapping segments appear as a graph under the **Overlap** tab.

.. segments-view-segment-overlap-steps-end


.. _segments-view-sql:

View SQL
==================================================

.. segments-view-sql-start

Many sections of the **Segments** page use SQL queries to return the data that is shown for the segment. You can view the SQL for the following areas:

* :ref:`segments-view-SQL-attribute-charts`
* :ref:`segments-view-SQL-revenue-tree`
* :ref:`segments-view-segment-stats-SQL`

.. segments-view-sql-end


.. _segments-view-SQL-attribute-charts:

For attribute charts 
--------------------------------------------------

.. segments-view-SQL-attribute-charts-start

You can view the SQL query that calculates the statistics in the segment attribute charts.

.. note:: You can't edit the query.

.. segments-view-SQL-attribute-charts-end

**To view the SQL for segment attribute charts**

.. segments-view-SQL-attribute-charts-steps-start

#. From the **Segments** page, select a segment and then click the **Breakdown** tab.
#. Open the menu for a customer or behavioral attributes chart. 
#. Select **View SQL**. The query that calculates the values in the tree is shown.

.. segments-view-SQL-attribute-charts-steps-end


.. _segments-view-SQL-revenue-tree:

For revenue tree
--------------------------------------------------

.. segments-view-SQL-revenue-tree-start

You can view the SQL query that calculates the statistics in the segment revenue tree.

.. note:: You can't edit the query.

.. segments-view-SQL-revenue-tree-end

**To view the SQL for segment revenue tree**

.. segments-view-SQL-revenue-tree-steps-start

#. From the **Segments** page, select a segment.
#. Under **Revenue and Reachability**, open the menu for the revenue tree.
#. Select **View SQL**. The query that calculates the values in the tree is shown.

.. segments-view-SQL-revenue-tree-steps-end


.. _segments-view-segment-stats-SQL:

For statistics 
--------------------------------------------------

.. segments-view-segment-stats-SQL-start

You can view the SQL for segment statistics on the **Segments** page in the **Summary** and **Breakdown** tabs. 

.. segments-view-segment-stats-SQL-end

**To view the SQL for segment statistics on the Segments page**

.. segments-view-segment-stats-SQL-steps-start

#. From the **Segments** page, on the either the **Summary** tab or the **Breakdown** tab, click the options icon on a segment data card.
#. Click **View SQL**.

The **View SQL** window appears with the query that calculates statistics for the segment.

.. segments-view-segment-stats-SQL-steps-end
