.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building an audience of customers who have purchased across channels.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of customers who have purchased across channels.

.. meta::
    :content class=swiftype name=title data-type=string:
        High-value multichannel customers

==================================================
High-value multichannel customers
==================================================

.. usecase-customers-high-value-multi-channel-start

A multichannel marketing strategy often leads to higher revenue. Customers who respond to multiple channels are easier to reach and lead to more effective marketing campaigns. The first step to building an effective multichannel marketing strategy is to identify high-value customers whose purchases can be associated with multiple channels.

You can find high-value multichannel customers first by identifying which customers have spent an amount over a defined threshold, and then by identifying which of those customers have purchased across multiple channels.

.. usecase-customers-high-value-multi-channel-end

.. usecase-customers-high-value-multi-channel-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that finds customers with a high lifetime value who have purchased across multiple channels.

.. usecase-customers-high-value-multi-channel-howitworks-end

**High-value multichannel customers**

.. usecase-customers-high-value-multi-channel-howitworks-callouts-start

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
          :width: 340 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find customers with a lifetime order revenue greater than $500.
          :align: center
          :class: no-scaled-link

     - To identify which customers have spent at least $500, choose the **Lifetime Order Revenue** attribute from the **Transaction Attributes Extended** table, select the "is greater than" operator, and then enter "500":

       .. image:: ../../images/attribute-lifetime-order-revenue-greater-than-500.png
          :width: 540 px
          :alt: Find customers with a lifetime order revenue greater than $500.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them could belong to a future campaign.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Find customers who have purchased across multiple channels.
          :align: center
          :class: no-scaled-link

     - Add a second attribute to your segment.

       To identify customers who have purchased from multiple channels, choose the **Multi Purchase Channel** attribute from the **Transaction Attributes Extended** table, and then select the "is true" operator:

       .. image:: ../../images/usecase-high-value-multi-channel-combo.png
          :width: 540 px
          :alt: Find customers who have purchased across multiple channels.
          :align: left
          :class: no-scaled-link

       Keep the slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to refresh segment insights to view updated values for the combination of customers who have spent at least $500 *and* have purchased from more than one channel.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You are done. Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that describes the purpose and audience type for the segment. For example: "High Value Multichannel Purchases".

       .. image:: ../../images/usecases-dialog-save-new-high-value-multi-purchase.png
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

.. usecase-customers-high-value-multi-channel-callouts-end
