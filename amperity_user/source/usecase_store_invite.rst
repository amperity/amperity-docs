.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building campaigns that use store invites.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building campaigns that use store invites.

.. meta::
    :content class=swiftype name=title data-type=string:
        Store invites

==================================================
Store invites
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-omni-channel-marketing-start
   :end-before: .. term-omni-channel-marketing-end

.. usecase-store-invite-start

SMS messaging should be an important part of your brand's larger omnnichannel marketing strategy. For example, you can use SMS messaging to:

* Incentivize customers to visit your brand's physical store locations
* To purchase online and pick up in store
* Promote a limited-time in-store offer
* Announce an upcoming flash sale event
* Showcase new products that have arrived in your stores

An in-store focused campaign requires knowing which customers are close enough to your stores for them to be able to take advantage of your personalized offers. Build a list of customers who have opted in to receiving SMS messages from your brand, and then filter those customers by physical location.

.. usecase-store-invite-end

.. usecase-store-invite-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that finds customers have contactable phone numbers and who are in a specific postal code area.

.. usecase-store-invite-howitworks-end

**Invite customers to your stores using SMS**

.. usecase-store-invite-howitworks-callouts-start

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
          :alt: Return a list of customers for whom your brand has phone numbers.
          :align: center
          :class: no-scaled-link

     - The first step is to identify customers for whom your brand has complete and contactable phone numbers in their customer profiles. Choose the **Contactable Phone** attribute from the **Customer Attributes** table, and then select the "is true" operator:

       .. image:: ../../images/attribute-contactable-phone-true.png
          :width: 540 px
          :alt: Find customers for whom your brand has phone numbers.
          :align: left
          :class: no-scaled-link

       Set the slider set to **AND**.

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them should belong to a future campaign.

       .. tip:: Use the **Is Opted Into SMS** attribute from the **Customer Attributes** table to include only customers who are opted into receiving SMS messages from your brand.

          .. image:: ../../images/usecase-generic-sms-optin.png
             :width: 540 px
             :alt: Find customers for whom your brand has an opted-in SMS phone number.
             :align: left
             :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link

     - The next step is to filter your audience by proximity to your stores, such as by region, by state or province, by store ID, or by postal code.

       Choose the **Postal** attribute from the **Customer 360** table to build a list of postal codes for each city.

       .. image:: ../../images/usecase-store-invite-group-by-postal-code.png
          :width: 540 px
          :alt: Find customers in near a store.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to view updated values for the combination of customers with contactable phone number *and* who are located within a specific postal code area.

       .. tip:: You can use sub-audiences in your campaign to split those audiences by region. Your approach depends on how your brand groups physical stores and in the data that is provided to Amperity.

          For example, ZIP codes can be used to separate customers by cities, such as Portland, OR and in Seattle, WA.

          .. image:: ../../images/usecase-store-invite-subaudience-by-postal-code.png
             :width: 540 px
             :alt: Find customers to use with your store invite campaign.
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Send customer list to favorite email destination.
          :align: center
          :class: no-scaled-link

     - Configure Amperity to send these audiences downstream to the marketing application from which you manage your SMS campaigns. For example, Attentive.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You are done building your audience. Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that describes the purpose and audience type for the segment. For example: "In-store Customers"

       .. image:: ../../images/usecases-dialog-save-in-store-customers.png
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

.. usecase-store-invite-callouts-end
