.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Choose one or more destinations to use with your campaigns.

.. meta::
    :content class=swiftype name=body data-type=text:
        Choose one or more destinations to use with your campaigns.

.. meta::
    :content class=swiftype name=title data-type=string:
        Choose destinations

==================================================
Choose destinations
==================================================

.. destinations-static-intro-start

Sending campaigns from Amperity to downstream marketing workflows is a combination of:

* A :doc:`segment <segments>` that defines the audience that you will use with your campaign.
* A :doc:`campaign <campaigns>` that breaks that audience down into sub-audiences that align to your marketing strategies and goals.
* A set of destinations that specify the locations and channels to which you will send each sub-audience.

This is part three of a series of topics that describes how this works.

.. destinations-static-intro-end

.. destinations-howitworks-start

Destinations are the locations to which you will send the lists of customers that are associated with each treatment group within a sub-audience. You may send these lists to any destination that is configured for your tenant. You may send the same list to multiple destinations.

.. destinations-howitworks-end

.. destinations-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - This topic describes adding destinations to your :doc:`campaign <campaigns>`. This is done from within the campaign builder for each treatment group that is part of a sub-audience. You can assign more than one destination to each treatment group.

       The following sections show adding destinations for each of the "active", "cooling down", and "at risk" :doc:`sub-audiences within the campaign <campaigns>`.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - A specific set of journeys and messaging creatives are built out and are tailored for customers who fall into the "active" lifecycle status. "Active" customers will be sent to the following channels:

       * Klaviyo, for email campaigns
       * Attentive, for mobile messaging campaigns
       * Criteo, for online display advertising

       Click the **Destinations** column, and then select a destination from the list.

       .. image:: ../../images/mockup-campaigns-select-destinations-active-list.png
          :width: 650 px
          :alt: Select one or more destinations for each treatment group.
          :align: left
          :class: no-scaled-link

       Do this for each destination to which you want to send this treatment group.

       .. image:: ../../images/mockup-campaigns-select-destinations-active.png
          :width: 650 px
          :alt: Destinations for customers with an active lifecycle status.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - "Cooling down" customers are sent to the same channels as "active" customers, but journeys and messaging creatives will be tailored to the "cooling down" lifecycle status.

       Click the **Destinations** column, and then select a destination from the list. Do this for each destination to which you want to send this treatment group.

       .. image:: ../../images/mockup-campaigns-select-destinations-cooling-down.png
          :width: 650 px
          :alt: Destinations for customers with a cooling down lifecycle status.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - "At risk" high-value customers are sent to the same channels as "active" and "cooling down" customers and also to TikTok and Facebook. Journeys and messaging creatives will be tailored to the "at risk" lifecycle status, along with new channels for display advertising creatives that are tailored to customers who fall into the "at risk" lifecycle status.

       Click the **Destinations** column, and then select a destination from the list. Do this for each destination to which you want to send this treatment group.

       .. image:: ../../images/mockup-campaigns-select-destinations-at-risk.png
          :width: 650 px
          :alt: Destinations for customers with an at risk lifecycle status.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - Each sub-audience that is configured for your campaign will have at least one destination associated with it. For each destination that is configured you must specify the set of attributes that will be sent from Amperity to that destination.

       Click the **Edit Attributes** link to open the attributes editor. From the dropdown select each of the destinations that has been configured for this sub-audience, and then select which attributes will be sent to that destination.

       For example, if you are sending a treatment group to Attentive to support an SMS-based marketing campaign, you will need to send a list of phone numbers from Amperity to Attentive.

       .. image:: ../../images/mockup-campaigns-edit-attributes-attentive.png
          :width: 740 px
          :alt: Send a phone number OR an email address to Attentive, but not both.
          :align: left
          :class: no-scaled-link

       Enable the checkbox next to the **phone** attribute, and then leave the rest of the settings as they are. Why are both **email** and **phone** optional? Attentive requires that you send only one of those values and the value that you should select is the one that your organization is using within Attentive to build customer journeys and support your marketing campaigns.

       .. tip:: You should use the **Merged Customers** table for sending customer PII data from Amperity. The **Merged Customers** table is your best source table and contains the most accurate set of customer PII. Your **Customer 360** table is built from the **Merged Customers** table.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: center
          :class: no-scaled-link
     - The attributes that are available from the **Edit Attributes** window will vary, depending on the destination. Some destinations have strict naming requirements. Some destinations only allow specific fields to be sent. Some destinations allow only one or two attributes, whereas others have few restrictions.

       For example:

       * Attentive Mobile requires a phone number *or* an email address. The one you choose should match how you have configured your instance of Attentive.
       * Klaviyo requires an email address, but can be configured to allow additional customer profile data, such as birthdays, favorite colors, and so on.
       * Criteo requires an email address and does not accept any other attributes.
       * TikTok Ads requires an email address **and** a phone number and will accept advertising IDs for Apple and Android.
       * Facebook Ads requires mapping fields in your customer 360 database to field in Facebook and applying a strict naming convention.
       * Cloud-based storage -- Amazon S3, Google Cloud Storage, or Microsoft Azure -- and/or SFTP often have no restrictions.

         .. note:: Workflows often use cloud-based storage and/or SFTP as a staging location before uploading that data to another application. That application may have specific requirements for which attributes are required. You will need to ensure that the list of attributes for those use cases are configured correctly within the campaigns builder.

.. destinations-howitworks-callouts-end
