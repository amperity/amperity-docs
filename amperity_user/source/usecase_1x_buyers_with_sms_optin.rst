.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building an audience of first-time buyers who have opted in to SMS messaging from your brand.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of first-time buyers who have opted in to SMS messaging from your brand.

.. meta::
    :content class=swiftype name=title data-type=string:
        First-time buyers with SMS opt-in

==================================================
First-time buyers with SMS opt-in
==================================================

.. usecase-engage-first-time-buyers-with-sms-start

Customer retention is critical for the long-term growth of your brand. It is not enough to acquire a customer who makes a single purchase. It is essential to find ways to convince your first-time buyers to become long-term, repeat customers.

If your brand uses SMS messaging as part of your one-time buyer or winback campaigns, a good early step is getting first-time buyers to opt-in to receiving SMS messages from your brand. Use incentives -- free shipping, a percentage discount, etc. -- to help convince first-time buyers to sign up to receive messages from your brand. This step works best when it's a part of the purchasing process.

The next step is to include first-time buyers who have opted-in as part of your one-time buyer or winback campaign strategies.

.. usecase-engage-first-time-buyers-with-sms-end

.. usecase-engage-first-time-buyers-with-sms-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that returns a list of customers who have made their first purchase within the previous 30 days *and* have opted-in to receiving SMS messages from your brand.

.. usecase-engage-first-time-buyers-with-sms-howitworks-end

.. usecase-engage-first-time-buyers-with-sms-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link

     - Open the **Segment Editor**, look in the lower-right of the page and make sure your customer 360 database is selected.

       .. image:: ../../images/mockup-segments-tab-database-and-tables-small.png
          :width: 350 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find newly acquired customers who made their first purchase during the holiday season.
          :align: center
          :class: no-scaled-link

     - To find customers who have made their first purchase within the previous 30 days, choose the **First Order Datetime** attribute from the **Transaction Attributes Extended** table, select the "is after" operator, enable the **Use relative dates** option, and then enter "today - 1 month":

       .. image:: ../../images/usecase-engage-sms-first-time-buyers.png
          :width: 540 px
          :alt: Find customers who made their first purchase within the previous month.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in their first purchase, how many are active, and how many of them should belong to a future campaign.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Find new customers who have opted-in to receive text messages.
          :align: center
          :class: no-scaled-link

     - Add an attribute that filters the first-time buyers audience to only include customers who want to receiving SMS messages.

       Click **+Add section**, choose the **Is SMS Opted In** attribute from the **SMS Opt Status** table, and then select the "is true" operator:

       .. image:: ../../images/usecase-generic-sms-optin.png
          :width: 540 px
          :alt: Find customers who have opted-in to receive text messages.
          :align: left
          :class: no-scaled-link

       Keep the slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to refresh segment insights to view updated values for the combination of customers who made their first purchase within the previous 30 days *and* who have opted in to SMS.

       .. tip:: For companies with multiple brands or are in multiple regions, you may use the **Brand** and **Region** attributes in the **SMS Opt Status** table to identify customer opt-in status by brand or by region.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done. Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "First-time Buyers with SMS Opt-in":

       .. image:: ../../images/usecases-dialog-engage-sms.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Be sure to include the brand name and the region name if you have multiple brands or have multiple regions and want to build segments that are brand- or region-specific.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-engage-first-time-buyers-with-sms-callouts-end
