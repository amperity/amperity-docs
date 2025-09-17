.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building an audience of active customers who prefer to shop at your store.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of active customers who prefer to shop at your store.

.. meta::
    :content class=swiftype name=title data-type=string:
        Active store shoppers

==================================================
Active store shoppers
==================================================

.. usecase-active-store-shoppers-start

An active store shopper is a customer who prefers to make their purchases at stores. You can build a list of active customers who prefer to shop at your stores and who have also made at least five purchases within the past year using a combination of attributes from the **Transaction Attributes Extended** table.

.. usecase-active-store-shoppers-end

.. usecase-active-store-shoppers-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that finds customers who have frequently shopped at a brick and mortar store.

.. usecase-active-store-shoppers-howitworks-end

**ACTIVE STORE SHOPPERS**

.. usecase-active-store-shoppers-howitworks-callouts-start

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
          :alt: Find customers who have ordered within the past year.
          :align: center
          :class: no-scaled-link

     - To identify customers have purchased from your brand within the past year, choose the **Latest Order Datetime** attribute from the **Transaction Attributes Extended** table, select the "is on or after" operator, enable the **Use relative dates** checkbox, and then enter "today - 1 year":

       .. image:: ../../images/usecase-active-store-shopper-order-datetime.png
          :width: 540 px
          :alt: Find customers who frequently shop at a store.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them could belong to a future campaign.

       .. tip:: You may use the **Historical Purchaser Lifecycle Status** attribute in the **Customer Attributes** table to identify active customers. The historical purchaser lifecycle status defines active as "someone who made a purchase within the previous year." Set the operator to "is in list", and then choose "Active".

          .. image:: ../../images/attribute-historical-purchaser-lifecycle-status-active.png
             :width: 540 px
             :alt: Find customers whose active.
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Find customers .
          :align: center
          :class: no-scaled-link

     - Add a second attribute to your segment.

       To identify customers who have purchased from a store and not your website, choose the **Purchase Channel** attribute from the **Transaction Attributes Extended** table, select the "is" operator, and then select "store":

       .. image:: ../../images/usecase-active-store-shopper-purchase-channel.png
          :width: 540 px
          :alt: Find customers who purchased from a store.
          :align: left
          :class: no-scaled-link

       Keep the slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to refresh segment insights to view updated values for the combination of customers who have purchased from a store within the previous year.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Find customers who purchased from a store.
          :align: center
          :class: no-scaled-link

     - Add a third attribute to your segment.

       To find customers who have made multiple purchases within the past year, choose the **L12M Order Frequency** attribute from the **Transaction Attributes Extended** table, select the "is greater than or equal to" operator, and then set the minimum number of orders. For example, for at least five orders in the past year enter "5":

       .. image:: ../../images/usecase-active-store-shopper-at-least-five-orders.png
          :width: 540 px
          :alt: Find customers who have made at least five purchases.
          :align: left
          :class: no-scaled-link

       Keep the slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to refresh segment insights to view updated values for the combination of customers who have purchased from a store within the previous year *and* have purchased at least five times.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done! Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "Active Store Multi-purchase Customers"

       .. image:: ../../images/usecases-dialog-active-store-multi-purchase-customers.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Be sure to include the brand name and the region name if you have multiple brands or have multiple regions and want to build segments that are brand- or region-specific.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-active-store-shoppers-callouts-end
