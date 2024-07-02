.. 
.. https://docs.amperity.com/ampiq/
.. 


.. meta::
    :description lang=en:
        Use segments to build audiences, and then use those audiences within campaigns.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments to build audiences, and then use those audiences within campaigns.

.. meta::
    :content class=swiftype name=title data-type=string:
        Build segments

==================================================
Build segments
==================================================

.. segments-static-intro-start

Sending campaigns from Amperity to downstream marketing workflows is a combination of:

* A segment (this topic) that defines the audience that you will use with your campaign.
* A :doc:`campaign <campaigns>` that breaks that audience down into sub-audiences that align to your marketing strategies and goals.
* A set of :doc:`destinations <destinations>` that specify the locations and channels to which you will send each sub-audience.

This is part one of a series of topics that describes how this works.

.. segments-static-intro-end

.. segments-howitworks-start

You can use the **Segment Editor** to build a segment using the attributes that are available to your tenant. Use a segment as the starting audience for any campaign.

.. note:: A version of this editor---called **Audience Builder**---is also available from within the **Campaigns** page and is used to define sub-audiences for a campaign. The **Audience Builder** does not provide segment insights and you must use the same database and tables that were used to build the initial audience.

The following sections describe the individual elements within the **Segment Editor**.

.. segments-howitworks-end

.. segments-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link

     - The **Segment Editor** is available from two locations within Amperity:

       * When adding an audience from the **Segments** page. The **Create Segment** button in the top right corner of the page opens the **Segment Editor**.
       * When adding a sub-audience from within the campaigns editor. The **Add sub-audience** link opens a version of this editor---called **Audience Builder**---that does not contain segment insights.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

     - You may use any table in your customer 360 database to build an audience or sub-audience.

       Your customer 360 database should already be selected for you (by default), though it is possible to have more than one 360 database that is available to your **Segment Editor**. Expand each of the table rows to see the attributes that are available from that table. Open the **Data Explorer** to view detailed information about every table (including tables not made available to the **Segment Editor**) and every attribute, including examples of the values they contain.

       .. image:: ../../images/mockup-segments-tab-database-and-tables.png
          :width: 340 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link

       .. admonition:: What are the standard tables for building an audience?

          Amperity provides the following tables as standard output:

          * The **Customer 360** table contains customer profile data---names, addresses, email addresses, phone numbers, and so on---summarized by unique customer.
          * The **Unified Transactions** table contains order-level details for a transaction.
          * The **Unified Itemized Transactions** table contains line-item and product catalog details for a transaction.
          * The **Transaction Attributes Extended** table contains calculated attributes that are built from order- and item-level details in transaction tables.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link

     - Start building your segment by choosing an attribute. The attributes that you choose to add to your segment will depend on the goals for your marketing use case.

       For example, maybe you want to start building out a churn prevention campaign that uses predicted lifecycle status as your starting point. The **Predicted Lifecycle Status** attribute helps you identify the individual stages within a churn prevention campaign to which your customers are predicted to belong.

       Click **Add attribute** to open the attributes menu, find the **Predicted CLV Attributes** table, and then choose the **Predicted Lifecycle Status** attribute.

       There are six possible stages for predicted lifecycle status, so choose the "is in list" operator, and then select "Active", "Cooling down", and "At risk":

       .. image:: ../../images/mockup-segments-tab-lifecycle-status-active-coolingdown-atrisk.png
          :width: 540 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       After you add an attribute to your segment, click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them should belong to a future campaign.

       .. admonition:: What types of attributes can you choose?

          You can choose attributes the following categories:

          #. Tables in your customer 360 database. These include all standard output tables and may include custom tables you have added to Amperity. Standard output tables are always available.

          #. Purchase behaviors that combine your customer's interaction histories with your brand with your brand's product catalog. Purchase behavior attributes are always available.

          #. Custom tables built in the **Queries** page that are made available to the **Segment Editor**. 

          #. Files that have been uploaded by you directly to the **Segment Editor**. These attributes are only available when files have been uploaded.

          Add attributes to your segment by clicking **Add attribute**, choosing a source (table, purchase behavior, custom table, or uploaded file), and then selecting an attribute.

          Some attributes, such as those that have "true" or "false" values will ask you to pick a value right away. Most attributes, such as those with string values, dates and times, amounts, and quantities, have additional fields that are available after the attribute is added to your segment.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../amperity_ampiq/source/segments_reference.rst
          :start-after: .. segments-reference-segment-insights-start
          :end-before: .. segments-reference-segment-insights-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - Add as many attributes to your segment as you need.

       For example, to continue building out a churn prevention campaign, in addition to knowing if your customers are "active", "cooling down", and "at risk", maybe you want to know which of those customers have made a purchase during the previous 3 months.

       Use the **Has Purchased** purchase behavior attribute to filter the "active", "cooling down", and "at risk" customers to those who purchased only 1 pair of socks within the previous 3 months:

       .. image:: ../../images/mockup-segments-tab-purchase-behavior-has-purchased-3-months.png
          :width: 600 px
          :alt: Add another attribute to fine-tune your segment.
          :align: left
          :class: no-scaled-link

       and then refresh segment insights.

       .. image:: ../../images/mockup-segments-tab-segment-insights-3-months.png
          :width: 360 px
          :alt: Refresh segment insights after you add an attribute to your segment.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link
     - When you are done building your segment, click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment.

       .. image:: ../../images/mockup-segments-tab-dialog-save.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Add details like "historical", "daily", or "test" as appropriate. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions.

          Some examples:

          * "Birthdays_Under_40_CA"
          * "Birthdays_Under_40_NY"
          * "High_AOV_Active_Loyal"
          * "High_CLV_Historical"
          * "Acme_Daily_Churn"

          Prefix a segment that is located in a folder with that folder name as often as possible. For example, if you have a folders named "Braze" and "TikTok" use segment names like "Braze_Birthdays_Under_40_CA" and "TikTok_Birthdays_Under_40" for all segments that exist within those folders.

   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

       .. image:: ../../images/mockup-segments-tab-segment-insights-socktown.png
          :width: 800 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

.. segments-howitworks-callouts-end
