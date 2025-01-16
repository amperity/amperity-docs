.. https://docs.amperity.com/ampiq/


.. meta::
    :description lang=en:
        A use case for building campaigns that help reduce paid media ad spend.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building campaigns that help reduce paid media ad spend.

.. meta::
    :content class=swiftype name=title data-type=string:
        Reduce paid media ad spend

==================================================
Reduce paid media ad spend
==================================================

.. usecase-reduce-paid-media-ad-spend-start

Your brand's spend on paid media is often the highest percentage of spend within your brand's total advertising budget. The best way to deliver greater ROI on the campaigns that your brand runs through paid media is to exclude your lowest value customers from those campaigns.

For example, a "lost" customer has stopped interacting with your brand, probably for years. They have opted out from receiving email and SMS communications and have not purchased from any of your brand's direct mail efforts. Are these customers worth marketing to? It depends on the campaign and the answer is not always "No." Should these customers be included in your most expensive paid media campaigns? That's easier and the answer is always "No."

You can exclude these customers from your paid media campaigns--and preserve a percentage of your total advertising budget--by building an audience of your brand's lowest value customers. Use this audience as an exclusion, which will prevent these customers from being part of your highest priority (and most expensive) paid media campaigns.

.. usecase-reduce-paid-media-ad-spend-end

.. usecase-reduce-paid-media-ad-spend-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that contains only your brand's lowest-value customers.

.. usecase-reduce-paid-media-ad-spend-howitworks-end

**REDUCE PAID MEDIA AD SPEND**

.. usecase-reduce-paid-media-ad-spend-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: left
          :class: no-scaled-link

     - Open the **Segment Editor**, look in the lower-right of the page and make sure your customer 360 database is selected.

       .. image:: ../../images/mockup-segments-tab-database-and-tables-small.png
          :width: 350 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find at risk customers.
          :align: left
          :class: no-scaled-link

     - The first step is to identify your lowest value customers. There are many ways you use Amperity to build this type of segment, including approximate RFM scores, historical purchaser lifecycle status, and predicted lifecycle status. The approach that you choose depends on how your brand defines your lowest value customers.

       * **Approximate RFM scores**

         You can filter customers into your brand's lowest 20% by using the monetary component of approximate RFM scores. This scores measures customer activity during the previous year.

         Choose the **L12M Monetary** attribute from the **Transaction Attributes Extended** table, select the "is in list" operator, and then choose the "1" and "2" values, which (when combined) represent the lowest 20%:

         .. image:: ../../images/attribute-rfm-monetary-bottom-20.png
            :width: 540 px
            :alt: Find your lowest value customers using the monetary component of RFM scores.
            :align: left
            :class: no-scaled-link

         You could apply a more strict score using lowest 20% of the combined RFM score by using the **L12M RFM Score** attribute, also from the **Transaction Attributes Table**, and then use "222" for the lowest 20% across all scores:

         .. image:: ../../images/attribute-rfm-combined-bottom-20.png
            :width: 540 px
            :alt: Find your lowest value customers using the monetary component of RFM scores.
            :align: left
            :class: no-scaled-link

       * **Historical purchaser lifecycle status**

         You can customize the historical purchaser lifecycle status tiers to align to the windows you use for your churn prevention campaigns. For this example, customers whose most recent purchase was more than 2 years ago are configured to belong to the "Dormant" tier.

         Choose the **Historical Purchaser Lifecycle Status** attribute from the **Customer Attributes** table, select the "is in list" operator, and then select "Lapsed" from the list, which filters for customers who purchased between 1 and 2 years ago:

         .. image:: ../../images/attribute-historical-purchaser-lifecycle-status-lapsed.png
            :width: 540 px
            :alt: Find customers with a historical value of lapsed.
            :align: left
            :class: no-scaled-link

       * **Predicted lifetime value tier**

         Tenants with Amperity predictive modeling can use predicted customer lifetime value (CLV) instead of **Historical Purchaser Lifecycle Status** attributes. Choose the **Predicted Lifetime Value Tier** attribute from the **Predicted CLV Attributes** table, set the operator to "is in list", and then choose "Low":

         .. image:: ../../images/attribute-predicted-lifecycle-status-low.png
            :width: 540 px
            :alt: Find customers whose predicted lifecycle status is "Low".
            :align: left
            :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Send customer list to your favorite paid media destination.
          :align: left
          :class: no-scaled-link

     - Send this list of customers to your favorite paid media destination (for example, Facebook Ads, Google Ads, etc.) on the **Campaigns** page.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: left
          :class: no-scaled-link
     - You're done building your audience! Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "Reduce Paid Media Ad Spend"

       .. image:: ../../images/usecases-dialog-reduce-paid-media-ad-spend.png 
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use this audience as an exclusion in your campaigns to filter out your lowest value from paid media campaigns.

          .. image:: ../../images/usecases-dialog-reduce-paid-media-ad-spend-exclusion-list.png 
             :width: 440 px
             :alt: Exclude this audience from your campaigns.
             :align: left
             :class: no-scaled-link

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Segment insights page
          :align: left
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-reduce-paid-media-ad-spend-callouts-end
