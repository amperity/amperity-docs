.. meta::
   :description lang=en:
      Package first-party data as a product to sell in third-party marketplaces.

.. meta::
   :content class=swiftype name=body data-type=text:
      Package first-party data as a product to sell in third-party marketplaces.

.. meta::
   :content class=swiftype name=title data-type=string:
      Audience monetization

==================================================
Audience monetization
==================================================

.. monetize-about-start

Package first-party data as audience products available in data marketplaces, where advertisers can pay to use these audiences in their campaigns.

.. monetize-about-end


.. _monetize-audience-types: 

Marketplace audience types
==================================================

.. monetize-audience-types-start

A data marketplace makes audiences available to buyers as :ref:`custom audiences <monetize-audience-type-custom>` or :ref:`syndicated audiences <monetize-audience-type-syndicated>`

.. monetize-audience-types-end


.. _monetize-audience-type-custom:

Custom audiences
--------------------------------------------------

.. monetize-audience-type-custom-start

A custom audience defines an advertiser- or partner-specific rate for a single purchaser and is purchased directly using a private deal.

.. monetize-audience-type-custom-end


.. _monetize-audience-type-syndicated:

Syndicated audiences
--------------------------------------------------

.. monetize-audience-type-syndicated-start

A syndicated audience defines a standard global rate for all purchasers and may be purchased by any verified buyer not on your blocklist.

.. monetize-audience-type-syndicated-end


.. monetize-audience-types-marketplaces-start

Use the **Monetization** page to send custom or syndicated audiences based on new or existing audience segments to the following marketplaces:

* The Trade Desk

.. monetize-audience-types-marketplaces-end


.. _monetize-data-marketplace-concepts: 

Data marketplace concepts
==================================================

.. monetize-data-marketplace-concepts-start

When monetizing audiences, it is important to understand the pricing models and structural requirements used by data marketplaces.

* :ref:`Buyable? <monetize-data-marketplace-concept-buyable>`
* :ref:`Cost per thousand (CPM) <monetize-data-marketplace-concept-cpm>`
* :ref:`Data rates <monetize-data-marketplace-concept-data-rates>`
* :ref:`Percentage of media costs <monetize-data-marketplace-concept-percentage>`
* :ref:`Rate caps <monetize-data-marketplace-concept-rate-caps>`
* :ref:`Rate levels <monetize-data-marketplace-concept-rate-levels>`
* :ref:`Rate types <monetize-data-marketplace-concept-rate-types>`
* :ref:`Taxonomy <monetize-data-marketplace-concept-taxonomy>`

.. monetize-data-marketplace-concepts-end


.. _monetize-data-marketplace-concept-buyable: 

Buyable?
--------------------------------------------------

.. monetize-data-marketplace-concept-buyable-start

All audiences are buyable by default when managed by Amperity.

A non-buyable audience cannot appear in the data marketplace. Any audience in Amperity can be made non-buyable. Open the segment in the **Audience monetization** page, and then click **Make not buyable**.

.. monetize-data-marketplace-concept-buyable-end

.. monetize-data-marketplace-concept-buyable-the-trade-desk-start

.. note:: A buyable audience without a rate or without assigned users is a non-buyable audience and cannot appear in The Trade Desk.

.. monetize-data-marketplace-concept-buyable-the-trade-desk-end


.. _monetize-data-marketplace-concept-cpm: 

Cost per thousand (CPM)
--------------------------------------------------

.. monetize-data-marketplace-concept-cpm-start

A cost per thousand (CPM) rate defines a maximum rate to prevent runaway costs for an audience. A CPM rate must be in United States dollars (USD) and must be an amount, such as $5.50 or $3.00.

.. monetize-data-marketplace-concept-cpm-end

.. monetize-data-marketplace-concept-cpm-the-trade-desk-start

.. note:: CPM rates lower than $5 require approval by The Trade Desk.

.. monetize-data-marketplace-concept-cpm-the-trade-desk-end


.. _monetize-data-marketplace-concept-data-rates: 

Data rates
--------------------------------------------------

.. monetize-data-marketplace-concept-data-rates-start

All buyable audiences `must have an approved rate <https://partner.thetradedesk.com/v3/portal/data/doc/ThirdPartyDataManagement#approval-criteria>`__ |ext_link|.

.. note:: The first syndicated rate submission for a brand requires approval.

.. tip:: Hybrid rates are recommended for all audiences.

An effective hybrid rate establishes a percent of media cost value that scales across media channels. As the value of an audience scales into premium high cost channels, audiences yield higher vaules.

.. monetize-data-marketplace-concept-buyable-end


.. _monetize-data-marketplace-concept-percentage: 

Percentage of media costs
--------------------------------------------------

.. monetize-data-marketplace-concept-percentage-start

A percentage of media costs rate defines a percentage applied to impressions that scales with the cost of media across channels. A percent of media cost is a decimal, such as 0.12 or 0.25, which represents 12% or 25%.

.. tip:: Apply a rate cap in conjunction with a percent of media cost to prevent runaway costs. 

.. monetize-data-marketplace-concept-percentage-end

.. monetize-data-marketplace-concept-percentage-the-trade-desk-start

.. note:: Percentages of media cost below 0.10 require approval by The Trade Desk.

.. monetize-data-marketplace-concept-percentage-the-trade-desk-end


.. _monetize-data-marketplace-concept-rate-caps: 

Rate caps
--------------------------------------------------

.. monetize-data-marketplace-concept-rate-caps-start

A rate cap protects against excessive costs, especially on premium channels. An effective rate cap exceeds the desired average cost per thousand, should be seen more often in high cost environments, and should be met about twenty percent of the time, where percent of media costs are the other eighty percent.

.. monetize-data-marketplace-concept-rate-caps-end


.. _monetize-data-marketplace-concept-rate-levels: 

Rate levels
--------------------------------------------------

.. monetize-data-marketplace-concept-rate-levels-start

Amperity assigns rate levels automatically depending on the type of audience sent to The Trade Desk.

.. monetize-data-marketplace-concept-rate-levels-end

* :ref:`Advertiser <monetize-data-marketplace-concept-rate-level-advertiser>`
* :ref:`Partner <monetize-data-marketplace-concept-rate-level-partner>`
* :ref:`System <monetize-data-marketplace-concept-rate-level-system>`


.. _monetize-data-marketplace-concept-rate-level-advertiser: 

Advertiser
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-data-marketplace-concept-rate-level-advertiser-start

An advertiser rate level is assigned to custom audiences intended for specific advertisers. An advertiser rate level is assigned to a specific **Advertiser ID**, which allows an advertiser to access the audience at the configured data rate.

.. monetize-data-marketplace-concept-rate-level-advertiser-end

.. monetize-data-marketplace-concept-rate-level-advertiser-the-trade-desk-start

.. note:: Use The Trade Desk **Platform ID** for an advertiser to configure the value of **Advertiser ID** in this destination.

   The value of **Advertiser ID** may not be empty for advertiser rate levels.

.. monetize-data-marketplace-concept-rate-level-advertiser-the-trade-desk-end


.. _monetize-data-marketplace-concept-rate-level-partner: 

Partner
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-data-marketplace-concept-rate-level-partner-start

A partner rate level is assigned to custom audiences intended for specific partners and their advertisers. A partner rate level is assigned to a specific **Partner ID**, which allows that partner to access the audience at the configured data rate.

.. monetize-data-marketplace-concept-rate-level-partner-end

.. monetize-data-marketplace-concept-rate-level-partner-the-trade-desk-start

.. note:: Use The Trade Desk **Platform ID** for a partner to configure the value of **Partner ID** in this destination.

   The value of **Partner ID** may not be empty for partner rate levels.

.. monetize-data-marketplace-concept-rate-level-partner-the-trade-desk-end


.. _monetize-data-marketplace-concept-rate-level-system: 

System
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-data-marketplace-concept-rate-level-system-start

A system rate level is assigned automatically to a syndicated audience.

.. monetize-data-marketplace-concept-rate-level-system-end


.. _monetize-data-marketplace-concept-rate-types: 

Rate types
--------------------------------------------------

.. monetize-data-marketplace-concept-rate-types-start

A rate type defines the pricing model for an audience and establishes a consistent relative value for advertising impressions while keeping audience pricing scalable across channels.

.. monetize-data-marketplace-concept-rate-types-end

* :ref:`CPM <monetize-data-marketplace-concept-rate-type-cpm>`
* :ref:`Hybrid <monetize-data-marketplace-concept-rate-type-hybrid>`
* :ref:`Percent of media cost <monetize-data-marketplace-concept-rate-type-percent>`


.. _monetize-data-marketplace-concept-rate-type-cpm: 

CPM
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-data-marketplace-concept-rate-type-cpm-start

A cost per thousand (CPM) rate defines a maximum rate to prevent runaway costs for an audience.

.. monetize-data-marketplace-concept-rate-type-cpm-end


.. _monetize-data-marketplace-concept-rate-type-hybrid: 

Hybrid
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-data-marketplace-concept-rate-type-hybrid-start

A hybrid rate blends a rate that scales with the cost of media across ad environments with a maximum rate that prevents runaway costs. All audiences sent from Amperity should be configured with a hybrid data rate.

.. note:: All syndicated audiences are assigned a hybrid rate type. A cost per thousand (CPM) rate *and* a percent of media cost rate must be provided.

.. monetize-data-marketplace-concept-rate-type-hybrid-end


.. _monetize-data-marketplace-concept-rate-type-percent: 

Percent of media cost
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-data-marketplace-concept-rate-type-percent-start

A percent of media cost rate defines a percentage applied to impressions that scales with the cost of media across channels. Apply a **CPM cap** in conjunction with a percent of media cost rate to prevent runaway costs.

.. note:: The value for percent of media costs may be $0.00.

.. monetize-data-marketplace-concept-rate-type-percent-end


.. _monetize-data-marketplace-concept-taxonomy: 

Taxonomy
--------------------------------------------------

.. monetize-data-marketplace-concept-taxonomy-start

The Trade Desk recommends `designing and building a flat taxonomy <https://partner.thetradedesk.com/v3/portal/data/doc/DataTaxonomyDesign>`__ |ext_link|, where all segments exist as children under the **ROOT** node, with segment names representing the full path.

* The display name of each segment defines the path hierarchy and taxonomy structure.
* The location of a segment in a taxonomy defines its full path, which always starts at the root level.
* The taxonomy hierarchy always starts with the **ROOT** element.
* The **ROOT** element is created for you and does appear in The Trade Desk for advertisers in the platform. For example, "Interest > Technology > Computers" appears as "Computers".

.. monetize-data-marketplace-concept-taxonomy-end


.. _monetize-howtos:

How-tos
==================================================

.. monetize-howtos-start

Tasks related to audience monetization in Amperity:

.. monetize-howtos-end

.. monetize-howtos-list-start

* :ref:`monetize-howtos-create-custom-audience`
* :ref:`monetize-howtos-create-syndicated-audience`
* :ref:`monetize-howtos-delete-audience`
* :ref:`monetize-howtos-edit-refresh-cadence`
* :ref:`monetize-howtos-global-optout`
* :ref:`monetize-howtos-make-not-buyable`
* :ref:`monetize-howtos-view-audience-details`

.. monetize-howtos-list-end


.. _monetize-howtos-create-custom-audience: 

Create custom audience
--------------------------------------------------

.. monetize-howtos-create-custom-audience-start

Custom audiences have advertiser or partner-specific rates. Each custom audience is for purchase by a single buyer via a private deal on the data marketplace.

.. monetize-howtos-create-custom-audience-end

**To create a custom audience**

.. monetize-howtos-create-custom-audience-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link
     - **Create audience**

       #. Open the **Audience monetization** page.
       #. Click **Create**, and then choose **Custom**


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link
     - **Choose segments**

       Do one of the following:

       #. Select **Create from existing segments**. This opens a list of segments. Use the checkboxes to pick one or more segments.

          .. note:: Each selected segment is sent to the data marketplace as a standalone audience. Selecting multiple segments does not combine them into a single audience.

       #. Select **Create a new segment**. This opens the visual **Segment Editor**. Define a new segment only for audience monetization.

       When finished, click **Next**.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link
     - **Select a marketplace**

       Do one of the following:

       #. Select an existing marketplace connection.
       #. Create a new connection to a marketplace.

          .. note:: Ask your **Datagrid Operator** for help configuring credentials for a marketplace connection.

          Click **Connect**, select a new connection, configure the credential settings and marketplace settings:

          * Set **Rate level** to **Partner** or **Advertiser**
          * Enter the **Partner name** and **Partner ID** *or* enter the **Audience name** and **Audience ID**.
          * Set **Rate type** to **Hybrid** or **Flat CPM**

       Set a cadence and choose the date on which Amperity will start delivering audiences to the marketplace.

       When finished, click **Next**.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link
     - **Prepare data products**

       #. Rename the audience, align the audience name with the taxonomy defined in The Trade Desk, and add a description.

          .. tip:: On the **Prepare data products** page, each segment name defaults to the Amperity-defined title. Renaming the segments or adding a description helps advertisers better understand what kind of audience is in the segment.

       #. Set the percent of media value and the cost per thousand (CPM) rate cap.

       When finished, click **Save and send**.

       .. note:: Audiences are added to the **Audience Monetization** folder on the **Segments** page. 

       .. caution:: Segments sent to data marketplaces cannot be edited while in use by an advertiser's campaign.

.. monetize-howtos-create-custom-audience-steps-end


.. _monetize-howtos-create-syndicated-audience:

Create syndicated audience
--------------------------------------------------

.. monetize-howtos-create-syndicated-audience-start

Syndicated audiences have a standard global rate. They may be purchased on the data marketplace by any verified buyers not on your blocklist.

.. monetize-howtos-create-syndicated-audience-end

**To create a syndicated audience**

.. monetize-howtos-create-syndicated-audience-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link
     - **Create audience**

       #. Open the **Audience monetization** page.
       #. Click **Create**, and then choose **Syndicated**


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link
     - **Choose segments**

       Do one of the following:

       #. Select **Create from existing segments**. This opens a list of segments. Use the checkboxes to pick one or more segments.

          .. note:: Each selected segment is sent to the data marketplace as a standalone audience. Selecting multiple segments does not combine them into a single audience.

       #. Select **Create a new segment**. This opens the visual **Segment Editor**. Define a new segment only for audience monetization.

       When finished, click **Next**.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link
     - **Select a marketplace**

       Do one of the following:

       #. Select an existing marketplace connection.
       #. Create a new connection to a marketplace.

          .. note:: Ask your **Datagrid Operator** for help configuring the credentials for a marketplace connection.

          Click **Connect**, select a new connection, configure the credential settings and marketplace settings, and then click **Save**

       Set a cadence and choose the date on which Amperity will start delivering audiences to the marketplace.

       When finished, click **Next**.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link
     - **Prepare data products**

       #. Rename the audience, align the audience name with the taxonomy defined in The Trade Desk, and add a description.

          .. tip:: On the **Prepare data products** page, the selected segment names default to their Amperity-defined titles. Renaming the segments or adding a description helps advertisers better understand what kind of audience is in the segment.

       #. Set the percent of media value and the cost per thousand (CPM) rate cap.

       When finished, click **Save and send**.

       .. note:: Audiences are added to the **Audience Monetization** folder on the **Segments** page. 

       .. caution:: Segments sent to data marketplaces cannot be edited while in use by an advertiser's campaign.

.. monetize-howtos-create-syndicated-audience-steps-end


.. _monetize-howtos-delete-audience:

Delete audience
--------------------------------------------------

.. monetize-howtos-delete-audience-start

You can delete an audience and remove it from the date markteplace.

.. monetize-howtos-delete-audience-end

**To delete an audience**

.. monetize-howtos-delete-audience-steps-start

#. On the **Audience monetization** page, use the search bar or scan the list to find the audience you wish to delete.
#. Click the |fa-kebab| icon and select **Delete**.

.. monetize-howtos-delete-audience-steps-end


.. _monetize-howtos-edit-refresh-cadence:

Edit refresh cadence
--------------------------------------------------

.. monetize-howtos-edit-refresh-cadence-start

You can edit how often audience product data is refreshed to reflect any updates to the segments you used to define the audience.

.. monetize-howtos-edit-refresh-cadence-end

**To edit refresh cadence**

.. monetize-howtos-edit-refresh-cadence-steps-start

#. On the **Audience monetization** page, use the search bar or scan the list to find the audience with the refresh cadence you want to edit.
#. Click the audience name.
#. On the **Data refresh** panel, locate **Refresh cadence** and click **Edit**.
#. Edit the cadence and start timing, and then click **Save**.

.. monetize-howtos-edit-refresh-cadence-steps-end


.. _monetize-howtos-global-optout:

Opt customers out
--------------------------------------------------

.. monetize-howtos-global-optout-start

Customers who have not given consent to use their data for advertising purposes can be excluded from availability across all audience products.

.. note:: Any incremental changes to the global opt-out group are sent to data marketplaces on a daily basis to account for timely removal of customers who have newly opted-out.

.. monetize-howtos-global-optout-end

**To opt customers out of audience products**

.. monetize-howtos-global-optout-steps-start

#. Open the **Audience monetization** page.
#. Click **Set global opt-out**.
#. Use the drop-down menu to select one or more segments
#. Click **Save**.

.. monetize-howtos-global-optout-steps-end


.. _monetize-howtos-make-not-buyable:

Make audience not buyable
--------------------------------------------------

.. monetize-howtos-make-not-buyable-start

You can make an audience no longer available for new purchases. Active campaigns currently using the audience may still use it.

.. caution:: This action cannot be undone.

.. monetize-howtos-make-not-buyable-end

**To make an audience not buyable**

.. monetize-howtos-make-not-buyable-steps-start

#. On the **Audience monetization** page, use the search bar or scan the list to find the audience you wish to delete.
#. Click the |fa-kebab| icon and select **Make not buyable**.
#. A warning dialog will appear. Click **Confirm** or **Cancel**. 
#. You may also make an audience not buyable by clicking into the audience and clicking **Make not buyable**. 

.. monetize-howtos-make-not-buyable-steps-end


.. _monetize-howtos-view-audience-details:

View audience details
--------------------------------------------------

.. monetize-howtos-view-audience-details-start

You can view audience details, including marketplace configuration, refresh timing, and action log.

.. monetize-howtos-view-audience-details-end

**To view audience details**

.. monetize-howtos-view-audience-details-steps-start

#. On the **Audience monetization** page, use the search bar or scan the list to find the audience you want to view.
#. Click the audience name.

.. monetize-howtos-view-audience-details-steps-end
