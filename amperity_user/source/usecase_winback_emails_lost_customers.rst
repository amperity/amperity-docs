.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building win-back campaigns for lost customers.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building win-back campaigns for lost customers.

.. meta::
    :content class=swiftype name=title data-type=string:
        Win-back campaigns for lost customers

==================================================
Win-back campaigns for lost customers
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-win-back-campaign-start
   :end-before: .. term-win-back-campaign-end

.. usecase-winback-emails-lost-customers-start

An email-based win-back campaign should be built around a series of personalized messages that encourage lost customers to re-engage with your brand.

A win-back campaign for lost customers will typically include:

* Incentives and offers, such as a percentage discount or "buy one, get one"
* Product announcements and updates
* Product suggestions that are based on previous purchases
* Other types of messaging, such as surveys and customer reviews

.. usecase-winback-emails-lost-customers-end

.. usecase-winback-emails-lost-customers-tip-start

.. admonition:: Track the win-back percentage for your win-back campaigns.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-win-back-percentage-start
      :end-before: .. term-win-back-percentage-end

.. usecase-winback-emails-lost-customers-tip-end

.. usecase-winback-emails-lost-customers-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that returns a list of customers who have a contactable email address and whose most recent order was more than two years ago.

.. usecase-winback-emails-lost-customers-howitworks-end

**Use email to win back lost customers**

.. usecase-winback-emails-lost-customers-howitworks-callouts-start

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
          :alt: Return a list of customers for whom your brand has contactable email addresses.
          :align: center
          :class: no-scaled-link

     - To identify customers for whom your brand has complete and contactable email addresses in their customer profiles. Choose the **Contactable Email** attribute from the **Customer Attributes** table, and then select the "is true" operator:

       .. image:: ../../images/attribute-contactable-email-true.png
          :width: 540 px
          :alt: Find customers for whom your brand has email addresses.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them should belong to a future campaign.

       .. tip:: Use the **Is Opted Into Email** attribute from the **Customer Attributes** table to include only customers who are opted into receiving email messages from your brand.

          .. image:: ../../images/usecase-generic-email-optin.png
             :width: 540 px
             :alt: Find customers for whom your brand has an opted-in email address.
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Find customers whose last purchase was over 2 years ago.
          :align: center
          :class: no-scaled-link

     - The next step is to identify customers whose most recent order was at least 2 years ago. Choose the **Days Since Latest Order** attribute from the **Transaction Attributes Extended** table, select the "is greater than or equal to" operator, and then configure the dates to be "730":

       .. image:: ../../images/attribute-days-since-latest-order-greater-than-730.png
          :width: 540 px
          :alt: Find customers whose last purchase was over 2 years ago.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to view updated values for the combination of customers who have a contactable email address *and* whose most recent order was more than two years ago.

       .. tip:: You can also use the **Historical Purchaser Lifecycle Status** attribute in the **Customer Attributes** table to identify dormant, or "lost", customers. Set the operator to "is in list", and then choose "Dormant":

          .. image:: ../../images/attribute-historical-purchaser-lifecycle-status-dormant.png
             :width: 540 px
             :alt: Find customers whose last purchase was over 2 years ago.
             :align: left
             :class: no-scaled-link

       .. admonition:: What about predicted customer lifetime value?

          Tenants with Amperity predictive modeling can use predicted customer lifetime value (CLV) instead of the **Days Since Latest Order** attribute. Choose the **Predicted Customer Lifecycle Status** attribute from the **Predicted CLV Attributes** table, set the operator to "is in list", and then choose "Lost":

          .. image:: ../../images/attribute-predicted-clv-lost.png
             :width: 540 px
             :alt: Find customers whose predicted CLV is "Lost".
             :align: left
             :class: no-scaled-link

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You are done. Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that describes the purpose and audience type for the segment. For example: "Win-back: Lost Customers".

       .. image:: ../../images/usecases-dialog-save-winback-emails-lost-customers.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use good naming patterns to ensure that you can always find your segments when you need them. Be sure to include the brand name or the region name if you have multiple brands or have multiple regions and want to build segments that are brand and region specific.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-winback-emails-lost-customers-callouts-end
