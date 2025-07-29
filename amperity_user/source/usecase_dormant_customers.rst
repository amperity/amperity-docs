.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building an audience of customers who haven't made a purchase within the previous 2 years.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of customers who haven't made a purchase within the previous 2 years.

.. meta::
    :content class=swiftype name=title data-type=string:
        Dormant customers

==================================================
Dormant customers
==================================================

.. usecase-dormant-customers-start

A dormant customer is a person who hasn't made a purchase with your brand within a defined time period. Amperity defines a dormant customer as a customer who hasn't made a purchase within the previous 730 days (2 years).

.. usecase-dormant-customers-end

.. usecase-dormant-customers-howitworks-start

The following sections describe using the the **Segment Editor** to build a segment that returns dormant customers.

.. usecase-dormant-customers-howitworks-end

**FIND DORMANT CUSTOMERS**

.. usecase-dormant-customers-howitworks-callouts-start

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
          :alt: Find dormant customers.
          :align: center
          :class: no-scaled-link

     - To identify dormant customers, choose the **Latest Order Datetime** attribute from the **Transaction Attributes Extended** table, select the "is after" operator, enable the **Use relative dates** checkbox, and then enter "today - 2 years" in the field:

       .. image:: ../../images/usecase-dormant-customers.png
          :width: 540 px
          :alt: Find customers who are going dormant.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them could belong to a future campaign.

       .. tip:: You may use the **Historical Purchaser Lifecycle Status** attribute in the **Customer Attributes** table to identify dormant customers. Set the operator to "is in list", and then choose "Dormant".

          .. image:: ../../images/attribute-historical-purchaser-lifecycle-status-dormant.png
             :width: 540 px
             :alt: Find customers whose last purchase was over 1 year ago.
             :align: left
             :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done! Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "Dormant Customers"

       .. image:: ../../images/usecases-dialog-save-dormant-customers.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions and want to build segments that are brand- and/or region-specific.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-dormant-customers-callouts-end
