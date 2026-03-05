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

Use the **Segment Editor** to define audiences, and then use the **Monetization** page to send custom or syndicated audiences to the following marketplaces:

* The Trade Desk

.. monetize-about-end


.. _monetize-data-marketplace-concepts: 

Data marketplace concepts
==================================================


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

* :ref:`monetize-howtos-public`
* :ref:`monetize-howtos-private`
* :ref:`monetize-howtos-global-optout`

.. monetize-howtos-list-end


.. _monetize-howtos-public: 

Public marketplaces
--------------------------------------------------

.. monetize-howtos-public-start

A public marketplace has a standard rate for audiences. Audiences in a public marketplace may be purchased by an unlimited number of advertisers.

* :ref:`monetize-howtos-public-custom`
* :ref:`monetize-howtos-public-existing`

.. monetize-howtos-public-end


.. _monetize-howtos-public-custom: 

Custom audience
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-howtos-public-custom-start

Use the visual **Segment Editor** accessible through the **Audience Monetization** page to define a new audience that is available to all advertisers in a public marketplace.

.. monetize-howtos-public-custom-end

**To build a custom audience for a public marketplace**

.. monetize-howtos-public-custom-steps-start

#. Open the **Audience Monetization** page.
#. Click **Create syndicated audience**.
#. Select **Create custom segment**, and then define the custom audience. When finished, click **Next**.

   .. image:: ../../images/howto-monetize-segment-custom.png
      :width: 600 px
      :alt: Monetization page
      :align: left
      :class: no-scaled-link

#. Choose the destination to which this audience is sent, and then configure any destination-specific settings, including the frequency at which this audience is sent. Click **Save**.
#. Verify the audience name and description, and then define the values for **% of Media** and **CPM cap**.

   **% of Media** is the percentage of media cost. For example: "0.12".

   **CPM cap** is the maximum cap for advertising costs--cost per thousand (CPM)--in United States dollars.

   The percentage of media cost and cost per thousand (CPM) rate cap determine the hybrid data rate for audience monetization.

#. When finished click **Save and send**.

.. monetize-howtos-public-custom-steps-end


.. _monetize-howtos-public-existing: 

Existing audience
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-howtos-public-existing-start

Select an audience that has already been defined in Amperity to make it available to all advertisers in a public marketplace.

.. monetize-howtos-public-existing-end

**To use an existing audience for a public marketplace**

.. monetize-howtos-public-existing-steps-start

#. Open the **Audience Monetization** page.
#. Click **Create syndicated audience**.
#. Select **Create from existing segments**.

   .. image:: ../../images/howto-monetize-segment-existing.png
      :width: 600 px
      :alt: Monetization page
      :align: left
      :class: no-scaled-link

   Select one or more segments by clicking the checkbox next to the name of the segment, and then click **Next**.

#. Choose the destination to which this audience is sent, and then configure any destination-specific settings, including the frequency at which this audience is sent. Click **Save**.
#. Verify the audience name and description, and then define the values for **% of Media** and **CPM cap**.

   **% of Media** is the percentage of media cost. For example: "0.12".

   **CPM cap** is the maximum cap for advertising costs--cost per thousand (CPM)--in United States dollars.

   The percentage of media cost and cost per thousand (CPM) rate cap determine the hybrid data rate for audience monetization.

#. When finished click **Save and send**.

.. monetize-howtos-public-existing-steps-end


.. _monetize-howtos-private:

Private marketplace
--------------------------------------------------

.. monetize-howtos-private-start

A private marketplace has an advertiser-specific rate. An audience in a private marketplace is purchased by a single advertiser.

* :ref:`monetize-howtos-private-custom`
* :ref:`monetize-howtos-private-existing`

.. monetize-howtos-private-end


.. _monetize-howtos-private-custom: 

Custom audience
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-howtos-private-custom-start

Use the visual **Segment Editor** accessible through the **Audience Monetization** page to define a new audience for a specific deal with a single buyer.
.. monetize-howtos-private-custom-end

**To build a custom audience for a private marketplace**

.. monetize-howtos-private-custom-steps-start

#. Open the **Audience Monetization** page.
#. Click **Create custom audience**.
#. Select **Create custom segment**, and then define the custom audience. When finished, click **Next**.

   .. image:: ../../images/howto-monetize-segment-custom.png
      :width: 600 px
      :alt: Monetization page
      :align: left
      :class: no-scaled-link

#. Choose the destination to which this audience is sent, and then configure any destination-specific settings, including the frequency at which this audience is sent. Click **Save**.
#. Verify the audience name and description, and then define the values for **% of Media** and **CPM cap**.

   **% of Media** is the percentage of media cost. For example: "0.12".

   **CPM cap** is the maximum cap for advertising costs--cost per thousand (CPM)--in United States dollars.

   The percentage of media cost and cost per thousand (CPM) rate cap determine the hybrid data rate for audience monetization.

#. When finished click **Save and send**.

.. monetize-howtos-private-custom-steps-end


.. _monetize-howtos-private-existing: 

Existing audience
++++++++++++++++++++++++++++++++++++++++++++++++++

.. monetize-howtos-private-existing-start

Select an audience that has already been defined in Amperity to fulfill a specific deal with a single buyer.

.. monetize-howtos-private-existing-end

**To use an existing audience for a private marketplace**

.. monetize-howtos-private-existing-steps-start

#. Open the **Audience Monetization** page.
#. Click **Create custom audience**.
#. Select **Create from existing segments**.

   .. image:: ../../images/howto-monetize-segment-existing.png
      :width: 600 px
      :alt: Monetization page
      :align: left
      :class: no-scaled-link

   Select one or more segments by clicking the checkbox next to the name of the segment, and then click **Next**.
#. Choose the destination to which this audience is sent, and then configure any destination-specific settings, including the frequency at which this audience is sent. Click **Save**.
#. Verify the audience name and description, and then define the values for **% of Media** and **CPM cap**.

   **% of Media** is the percentage of media cost. For example: "0.12".

   **CPM cap** is the maximum cap for advertising costs--cost per thousand (CPM)--in United States dollars.

   The percentage of media cost and cost per thousand (CPM) rate cap determine the hybrid data rate for audience monetization.

#. When finished click **Save and send**.

.. monetize-howtos-private-existing-steps-end


.. _monetize-howtos-global-optout:

Opt audiences out of third-party marketplaces
--------------------------------------------------

.. monetize-howtos-global-optout-start

Audiences can be excluded from availability for third-party marketplaces.

.. monetize-howtos-global-optout-end

**To opt audiences out of third-party marketplaces**

.. monetize-howtos-global-optout-steps-start

#. Open the **Audience Monetization** page.
#. Click **Set global opt-out**.
#. Use the drop-down menu to select one or more segments
#. Click **Save**.

.. monetize-howtos-global-optout-steps-end
