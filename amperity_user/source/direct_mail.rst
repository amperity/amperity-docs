.. https://docs.amperity.com/user/


.. TODO: Q: What is a good timeline for measuring the conversion of a retail customer who has received a direct mail offer? A: 28 days, 30 days, 4 weeks, 1 month are all reasonable timelines.

.. TODO: Review usecases for usecase_send_flyer_to_at_risk_customers and usecase_send_weekly_flyer_grocery_store


.. meta::
    :description lang=en:
        Build direct mail campaigns in Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Build direct mail campaigns in Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Direct mail 

==================================================
Direct mail campaigns
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-direct-mail-start
   :end-before: .. term-direct-mail-end

.. direct-mail-context-start

Direct mail is an effective way to help your brand stand out in the age of digital ads and overflowing email inboxes. With the right audiences, direct mail gives your brand a physical touchpoint with which you can make a positive impression on your customers.

Many direct-to-consumer companies prefer using direct mail because they can show the brand and products using a tangible format that customers can hold in their hands.

The right mix of creative advertising, physical design of what is sent to the customer, offer, and frequency often leads to higher customer response rates when compared to digital and media advertising.

Use householding to support a wide variety of householding use cases, such as:

* Deduplicating physical addresses to ensure that only one catalog is sent to each address
* Sending high-value customers periodic direct mail offers that are different from the quarterly catalog
* Expanding digital marketing campaigns to include non-digital customers and customers who do not have an email address
* Aligning householding use cases to your larger marketing strategy

.. direct-mail-context-end


.. _direct-mail-householding-use-cases:

Householding table
==================================================

Use the |householding| table to build customer profiles by household, and then use segments and queries to build audiences by household using all of the attributes in your customer 360 database.


.. _direct-mail-build-audience:

Build an audience
==================================================

.. direct-mail-build-audience-start

A good approach to building audiences for your direct mail campaigns is to put them into categories by current lifecycle status and value tier:

.. list-table::
   :widths: 200 200 200
   :header-rows: 1

   * - Lifecycle status
     - High value
     - Low value
   * - Active
     - Use this group for most of your direct mail marketing campaigns.
     - Use this group as part of lookalike audience marketing campaigns.

       Use A/B testing to identify the most effective approaches for this group.
   * - Inactive
     - Use this group as part of retention or reactivation marketing campaigns.
     - Deprioritize this group.

Use the customer lifecycle status and customer value tier attributes to compare combinations, and then identify the right combination to use with your direct mail campaign.

.. direct-mail-build-audience-end


.. _direct-mail-build-audience-by-tier:

By value tier
--------------------------------------------------

.. direct-mail-build-audience-by-tier-start

To accurately budget for direct mail campaigns, marketers must determine the amount customers will spend. Use predicted CLV attributes to group customers into high-value and low-value categories based on their predicted spend in the coming year and then use these groupings to define effective segmentation strategies.

.. include:: ../../shared/terms.rst
   :start-after: .. term-pclv-start
   :end-before: .. term-pclv-end

.. include:: ../../amperity_reference/source/attribute_predicted_value_tier.rst
   :start-after: .. attribute-predicted-value-tier-start
   :end-before: .. attribute-predicted-value-tier-end

.. include:: ../../amperity_reference/source/attribute_predicted_value_tier.rst
   :start-after: .. attribute-predicted-value-tier-segment-start
   :end-before: .. attribute-predicted-value-tier-segment-end

.. direct-mail-build-audience-by-tier-end


.. _direct-mail-build-audience-by-status:

By lifecycle status
--------------------------------------------------

.. include:: ../../amperity_reference/source/attribute_predicted_lifecycle_status.rst
   :start-after: .. attribute-predicted-lifecycle-status-start
   :end-before: .. attribute-predicted-lifecycle-status-end

.. include:: ../../amperity_reference/source/attribute_predicted_lifecycle_status.rst
   :start-after: .. attribute-predicted-lifecycle-status-repeat-start
   :end-before: .. attribute-predicted-lifecycle-status-repeat-end

.. include:: ../../amperity_reference/source/attribute_predicted_lifecycle_status.rst
   :start-after: .. attribute-predicted-lifecycle-status-segment-start
   :end-before: .. attribute-predicted-lifecycle-status-segment-end

.. direct-mail-build-audience-by-status-start

Set your list to the following values: "Cooling down" and "At risk".

.. direct-mail-build-audience-by-status-end


.. _direct-mail-align-to-objectives:

Align to campaign objectives
==================================================

.. direct-mail-align-to-objectives-start

After you have associated your customers to their lifecycle status and value tier, align the audience to your overall marketing objectives for your direct mail campaign, such as what types of discount preferences, promo codes, or offers you want to use.

After determining which customer groups to market to, apply additional segments to align campaigns with your overall marketing goals. For example, you may want to focus on customers who opted in to receive emails. With the ability to add multiple segments, you can determine which groups are more inclined to make a purchase.

.. direct-mail-align-to-objectives-end


.. _direct-mail-track-campaign-performance:

Track campaign performance
==================================================

.. direct-mail-track-campaign-performance-start

To understand how direct mail attribution impacts a multichannel marketing campaign, marketers need to clarify the difference between the direct mail campaign performance and return on investment. Marketers can track this performance by utilizing the following processes:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-matchback-start
     :end-before: .. term-matchback-end

* .. include:: ../../shared/terms.rst
     :start-after: .. term-control-group-start
     :end-before: .. term-control-group-end

  .. tip:: Control groups are sometimes referred to as holdout groups.

* .. include:: ../../shared/terms.rst
     :start-after: .. term-single-touch-attribution-start
     :end-before: .. term-single-touch-attribution-end

* .. include:: ../../shared/terms.rst
     :start-after: .. term-multi-touch-attribution-start
     :end-before: .. term-multi-touch-attribution-end
	 
.. direct-mail-track-campaign-performance-end
	 

.. _direct-mail-sendto-channels:

Send to direct mail channels
==================================================

.. direct-mail-sendto-channels-start

Marketers can send audience lists from Amperity to a variety of channels that support direct mail campaigns.

.. direct-mail-sendto-channels-end


.. _direct-mail-sendto-channel-cross-country-computer:

Cross Country Computer
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ccc-start
   :end-before: .. term-ccc-end


.. _direct-mail-sendto-channel-pebblepost:

PebblePost
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pebblepost-start
   :end-before: .. term-pebblepost-end

.. direct-mail-sendto-channel-pebblepost-start

Use direct mail campaigns with PebblePost as part of marketing strategies to acquire and retain customers. Use direct mail campaigns to:

*  Discover, engage, and convert new customers.
*  Upsell, cross-sell, and win back existing customers.

PebblePost has built-in reporting and measurement that can track the outcomes of your direct mail campaigns across points of sale, whether online, in-store, or over the phone.

.. direct-mail-sendto-channel-pebblepost-end


.. _direct-mail-sendto-channel-other:

Other channels
--------------------------------------------------

.. direct-mail-sendto-channel-other-start

Other direct mail channels are available as plugins through popular marketing automation platforms like Adobe Marketo, HubSpot, and Salesforce Marketing Cloud. Send audience lists to the marketing automation platform, and then use a plugin to manage the direct mail campaign.

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Plugin
     - Description
   * - **Alyce**
     - `Alyce <https://www.alyce.com/>`__ |ext_link| is a personal experience platform that enables marketers to reach customers using an AI-powered one-on-one gifting approach. Send query results or audience lists to Adobe Marketo, HubSpot, or Salesforce Marketing Cloud, and then use Alyce to manage your direct mail campaign.
   * - **Postal.io**
     - `Postal.io <https://www.postal.io/>`__ |ext_link| allows you to manage direct mail campaigns using customizable workflows and automated sends. Send query results or audience lists to Adobe Marketo, HubSpot, or Salesforce Marketing Cloud, and then use Postal.io to manage your direct mail campaign. 

   * - **Sendoso**
     - `Sendoso <https://sendoso.com/>`__ |ext_link| is a send management platform that uses automated and scaled solutions to help marketers manage effective direct mail campaigns. Send query results or audience lists to Adobe Marketo, HubSpot, or Salesforce Marketing Cloud, and then use Sendoso to manage your direct mail campaign. 

.. direct-mail-sendto-channel-other-end
