.. 
.. https://docs.amperity.com/ampiq/
.. 


.. meta::
    :description lang=en:
        A use case for building an audience of customers who made their first purchase from your brand's website.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of customers who made their first purchase from your brand's website.

.. meta::
    :content class=swiftype name=title data-type=string:
        New website customers

==================================================
New website customers
==================================================

.. usecase-customers-new-website-customers-start

Which customers made their first order from your website within the last 30 days?

You can find customers who made their first purchase from your website within the last 30 days first by identifying customers who have made their first purchase within the last 30 days, and then by identifying customers whose purchase channel is your website.

.. usecase-customers-new-website-customers-end

.. usecase-customers-new-website-customers-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that finds customers with a high lifetime value who have purchased across multiple channels.

.. usecase-customers-new-website-customers-howitworks-end

**NEW WEBSITE CUSTOMERS**

.. usecase-customers-new-website-customers-howitworks-callouts-start

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
          :width: 340 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find customers whose first purchase was within the last 30 days.
          :align: left
          :class: no-scaled-link

     - To identify which customers have made their first purchase within the previous 30 days, choose the **First Order Datetime** attribute from the **Transaction Attributes Extended** table, select the "is after" operator, enable the **Use relative dates** option, and then configure the dates to be between "now - 30 days":

       .. image:: ../../images/attribute-first-order-datetime-last-30-days.png
          :width: 540 px
          :alt: Find customers whose first purchase was within the last 30 days.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them could belong to a future campaign.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Find customers who have purchased from your website.
          :align: left
          :class: no-scaled-link

     - Add a second attribute to your segment.

       To identify customers who have purchased from your website, choose the **First Order Purchase Channel** attribute from the **Transaction Attributes Extended** table, select the "is" operator, and then select "web":

       .. image:: ../../images/usecase-new-website-customers-combo.png
          :width: 540 px
          :alt: Find customers who have purchased from your website.
          :align: left
          :class: no-scaled-link

       Keep the and/or slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to refresh segment insights to view updated values for the combination of customers who have made their first purchase within the last 30 days *and* made that purchase on your website.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: left
          :class: no-scaled-link
     - You're done! Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "New Customers L30D Website".

       .. image:: ../../images/usecases-dialog-save-new-customers-l30d-website.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions and want to build segments that are brand- and/or region-specific.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Segment insights page
          :align: left
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-customers-new-website-customers-callouts-end
