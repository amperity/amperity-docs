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

.. TODO: update image

.. .. image:: ../../images/mockup-monetization-page.png
   :width: 600 px
   :alt: Monetization page
   :align: left
   :class: no-scaled-link

You can choose between creating a **Custom audience** and a **Syndicated audience**.

**Custom audiences** have advertiser or partner-specific rates. Each custom audience is for purchase by a single buyer via a private deal on the data marketplace.

**Syndicated audiences** have a standard global rate. They may be purchased on the data marketplace by any verified buyers not on your blocklist.

Use the **Monetization** page to send custom or syndicated audiences based on new or existing audience segments to the following marketplaces:

* The Trade Desk

.. monetize-about-end


.. _monetize-data-marketplace-concepts: 

Data marketplace concepts
==================================================

.. monetize-data-marketplace-concepts-start

When monetizing audiences, it is important to understand the pricing models and structural requirements used by data marketplaces.


Data rates
--------------------------------------------------
All buyable audiences `must have an approved rate <https://partner.thetradedesk.com/v3/portal/data/doc/ThirdPartyDataManagement#approval-criteria>`__ |ext_link|.

.. note:: The first syndicated rate submission for a brand requires approval.

.. tip:: Hybrid rates are recommended for all audiences.

An effective hybrid rate establishes a percent of media cost value that scales across media channels. As the value of an audience scales into premium high-cost channels, audiences yield higher vaules.

A rate cap protects against excessive costs, especially on premium channels. An effective cap exceeds the desired average cost per thousand, should be seen more often in high cost environments, and should be met about twenty percent of the time, where percent of media costs are the other eighty percent.




Cost per thousand (CPM)
--------------------------------------------------
A cost per thousand (CPM) rate defines a maximum rate to prevent runaway costs for an audience. A CPM rate must be in United States dollars (USD) and must be an amount, such as $5.50 or $3.00.

.. note:: CPM rates lower than $5 require approval by The Trade Desk.


Percent of media cost
--------------------------------------------------
A percent of media cost rate defines a percentage applied to impressions that scales with the cost of media across channels. Apply a **CPM cap** in conjunction with a percent of media cost rate to prevent runaway costs. A percent of media cost rate must be a decimal, such as 0.12 or 0.25, which represents 12% or 25%.

.. note:: Percentages of media cost below 0.10 require approval by The Trade Desk.


Rate level
--------------------------------------------------
Amperity assigns rate levels automatically depending on the type of audience sent to The Trade Desk:

**System**
A system rate level is assigned automatically to a syndicated audience.

**Partner**
A partner rate level is assigned to custom audiences intended for specific partners and their advertisers. A partner rate level is assigned to a specific **Partner ID**, which allows that partner to access the audience at the configured data rate.

.. note:: Use The Trade Desk **Platform ID** for a partner to configure the value of **Partner ID** in this destination.

   The value of **Partner ID** may not be empty for partner rate levels.

**Advertiser**
An advertiser rate level is assigned to custom audiences intended for specific advertisers. An advertiser rate level is assigned to a specific **Advertiser ID**, which allows an advertiser to access the audience at the configured data rate.

.. note:: Use The Trade Desk **Platform ID** for an advertiser to configure the value of **Advertiser ID** in this destination.

   The value of **Advertiser ID** may not be empty for advertiser rate levels.


Rate type
--------------------------------------------------
          The rate type defines the pricing model for an audience and establishes a consistent relative value for advertising impressions while keeping audience pricing scalable across channels.

          **CPM**
             A cost per thousand (CPM) rate defines a maximum rate to prevent runaway costs for an audience.

          **Hybrid**
             A hybrid rate blends a rate that scales with the cost of media across ad environments with a maximum rate that prevents runaway costs. All audiences sent from Amperity should be configured with a hybrid data rate.

             .. note:: All syndicated audiences are assigned a hybrid rate type. A cost per thousand (CPM) rate *and* a percent of media cost rate must be provided.

          **Percent of media cost**
             A percent of media cost rate defines a percentage applied to impressions that scales with the cost of media across channels. Apply a **CPM cap** in conjunction with a percent of media cost rate to prevent runaway costs.

             .. note:: The value for percent of media costs may be $0.00.



















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

#. On the **Audience monetization** page, click **Create audience**.
#. Select **Custom**.
#. Select **Create from existing segments** and use the checkboxes to pick one or more segments, or select **Create a new segment** and use the **Visual segment editor** to define a new segment.
#. When you have selected or created segments, click **Next** to proceed to the **Select marketplace seat** page.
#. Select an existing markletplace seat or create a new connection
#. If creating a new connection, select an existing credential or ask your data grid operator to create a new one.

.. TODO: link to operator's guide for credential creation

#. If creating a new connection, select **Rate level** and designate a **Partner name** and **Partner ID**.
#. Select **Rate type**.
#. Set a cadence and delivery start date.
#. If creating a new connection, click **Connect**, and then select your new connection and fill any remaining fields, then click **Save**. 
#. Once your selected connection is highlighted, click **Next** to proceed to the **Prepare data products** page.
#. You may rename the audience and add a description.
#. You must set the percent of media and the cost per thousand (CPM) cap. 
#. Click **Save and send**. 

.. tip:: On the **Prepare data products** page, your selected segment will default display with whatever internal title it may have. Renaming it and/or adding a description may help advertisers better understand what kind of audience it is.

.. note:: If you select multiple segments when defining the audience, each of these will be sent to the data marketplace as a separate audience product. Selecting multiple segments does not combine them into one audience product.

.. note:: New segments you create will populate an Audience Monetization folder on the **Segments** page. 

.. caution:: Segments you send to data marketplaces cannot be edited while in use for an advertiser's campaign.

.. TODO: Is that true, what i wrote in the caution? It seems to be, but not certain.  Also, too many admonitions in a row?

.. monetize-howtos-create-custom-audience-steps-end

.. _monetize-howtos-create-syndicated-audience:

Create syndicated audience
--------------------------------------------------

.. monetize-howtos-create-syndicated-audience-start

Syndicated audiences have a standard global rate. They may be purchased on the data marketplace by any verified buyers not on your blocklist.

.. monetize-howtos-create-syndicated-audience-end

**To create a syndicated audience**

.. monetize-howtos-create-syndicated-audience-steps-start

#. On the **Audience monetization** page, click **Create audience**.
#. Select **Syndicated**.
#. Select **Create from existing segments** and use the checkboxes to pick one or more segments, or select **Create a new segment** and use the **Visual segment editor** to define a new segment.
#. When you have selected or created segments, click **Next** to proceed to the **Select marketplace seat** page.
#. Select an existing markletplace seat or create a new connection
#. If creating a new connection, select an existing credential or ask your data grid operator to create a new one.

.. TODO: link to operator's guide for credential creation

#. Set a cadence and delivery start date.
#. If creating a new connection, click **Connect**, and then select your new connection and fill any remaining fields, then click **Save**. 
#. Once your selected connection is highlighted, click **Next** to proceed to the **Prepare data products** page.
#. You may rename the audience and add a description.
#. You must set the percent of media and the cost per thousand (CPM) cap. 
#. Click **Save and send**. 

.. tip:: On the **Prepare data products** page, your selected segment will default to whatever internal title it may have. Renaming it and/or adding a description may help advertisers better understand what kind of audience it is.

.. note:: If you select multiple segments when defining the audience, each of these will be sent to the data marketplace as a separate audience product. Selecting multiple segments does not combine them into one audience product.

.. note:: New segments you create will populate an Audience Monetization folder on the **Segments** page. 

.. caution:: Segments you send to data marketplaces cannot be edited while in use for an advertiser's campaign.

.. TODO: Is that true, what i wrote in the caution? It seems to be, but not certain.  Also, too many admonitions in a row?

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
