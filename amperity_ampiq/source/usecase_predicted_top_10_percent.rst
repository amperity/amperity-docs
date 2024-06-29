.. 
.. https://docs.amperity.com/ampiq/
.. 


.. meta::
    :description lang=en:
        A use case for building an audience of customers who are predicted to be in your highest value customers.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of customers who are predicted to be in your highest value customers.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predicted top 10% high-value customerss

==================================================
Predicted top 10% high-value customers
==================================================

.. usecase-predicted-top-10-percent-start

When predictive modeling is enabled for your tenant you can use output from the |predicted customer lifetime value (CLV) model|, which helps you identify your highest value customers by value tier. Each tier represents a percentile grouping of customers by predicted value:

* Platinum represents the top 1%
* Gold represents customers who fall between 1% and 5%
* Silver represents customers who fall between 5% and 10%

Select all three of these predicted value tiers to build an audience that contains customers who are predicted to be in your top 10% (inclusive) high value customers.

.. usecase-predicted-top-10-percent-end

.. usecase-predicted-top-10-percent-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that returns customers who are predicted to be your top 10% highest value customers.

.. usecase-predicted-top-10-percent-howitworks-end

**WHICH CUSTOMERS ARE PREDICTED TO BE YOUR TOP 10%?**

.. usecase-predicted-top-10-percent-howitworks-callouts-start

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
          :alt:   Return a list of the customers with a predicted platinum, gold, or silver value.
          :align: left
          :class: no-scaled-link

     - The first step is to identify customers whose predicted customer lifetime value is platinum, gold, or silver. Choose the **Predicted Customer Lifetime Value Tier** attribute from the **Predicted CLV Attributes** table, select the "is in list" operator, and then select "Platinum", "Gold", *and* "Silver" from the list:

       .. image:: ../../images/usecases-predicted-value-tier-is-in-list.png
          :width: 540 px
          :alt: Find customers with a predicted platinum, gold, or silver value.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them should belong to a future campaign.
	   
   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Return a list of customers for whom your brand has email addresses.
          :align: left
          :class: no-scaled-link

     - The next step is to identify customers with contactable email address in their customer profiles. Choose the **Contactable Email** attribute from the **Customer Attributes** table, and then select the "is true" operator:

       .. image:: ../../images/attribute-contactable-email-true.png
          :width: 540 px
          :alt: Find customers for whom your brand has email addresses.
          :align: left
          :class: no-scaled-link

       Keep the and/or slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to view updated values for the combination of customers who have a predicted platinum, gold, or silver *and* a contactable email address.

       .. tip:: Use the **Is Opted Into Email** attribute from the **Customer Attributes** table to include only customers who are opted into receiving email messages from your brand.

          .. image:: ../../images/usecase-generic-email-optin.png
             :width: 540 px
             :alt: Find customers for whom your brand has an opted-in email address.
             :align: left
             :class: no-scaled-link

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Send customer list to your favorite email marketing tool.
          :align: left
          :class: no-scaled-link

     - Send this list of customers to your favorite email marketing tool (i.e. Attentive) on the **Campaigns** page.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Save your segment.
          :align: left
          :class: no-scaled-link
     - You're done building your audience! Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "Predicted Top 10% High Value Customers"

       .. image:: ../../images/usecases-dialog-save-top-10-high-value-customers.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions and want to build segments that are brand- and/or region-specific.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Segment insights page
          :align: left
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-predicted-top-10-percent-howitworks-callouts-end
