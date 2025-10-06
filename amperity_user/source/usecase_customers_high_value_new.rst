.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building an audience of new customers who have the potential to become high-value repeat customers.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of new customers who have the potential to become high-value repeat customers.

.. meta::
    :content class=swiftype name=title data-type=string:
        New high-value customers

==================================================
New high-value customers
==================================================

.. usecase-customers-high-value-new-start

Repeat customers generate more revenue than one-time customers. In fact, it's not unusual in retail for ~20% of your customers to be ~80% of your revenue. Therefore, it's important to your business that you can identify new customers that also have the potential to become high-value repeat customers.

You can find new high value customers first by identifying which customers have made their first purchase, and then by identifying which of those customers are predicted to become high-value repeat customers.

.. usecase-customers-high-value-new-end

.. usecase-customers-high-value-new-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that finds new high-value customers.

.. usecase-customers-high-value-new-howitworks-end

**FIND NEW HIGH-VALUE CUSTOMERS**

.. usecase-customers-high-value-new-howitworks-callouts-start

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
          :alt: Find customers whose first purchase was during the previous 3 months.
          :align: center
          :class: no-scaled-link

     - To identify customers who have recently made their first purchase, choose the **First Order Datetime** attribute from the **Transaction Attributes Extended** table, select the "is between" operator, enable the **Use relative dates** option, and then configure the dates to be between "now" and "now - 3 months":

       .. image:: ../../images/attribute-first-order-datetime-example.png
          :width: 540 px
          :alt: Find customers whose first purchase was during the previous 3 months.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them could belong to a future campaign.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Find customers predicted to belong to platinum and gold value tiers.
          :align: center
          :class: no-scaled-link

     - Add a second attribute to your segment.

       To identify which customers are predicted to belong to a high value tier, choose the **Predicted Customer Lifetime Value Tier** attribute from the **Predicted CLV Attributes** table, select the "is in list" operator, and then select "Platinum", "Gold", and "Silver":

       .. image:: ../../images/usecase-high-value-new-combo.png
          :width: 540 px
          :alt: Find customers predicted to belong to platinum and gold value tiers.
          :align: left
          :class: no-scaled-link

       Keep the slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to refresh segment insights to view updated values for the combination of customers who purchased recently *and* are predicted to be high value customers.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done. Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "New High Value Customers".

       .. image:: ../../images/usecases-dialog-save-new-high-value-customers.png
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

.. usecase-customers-high-value-new-callouts-end
