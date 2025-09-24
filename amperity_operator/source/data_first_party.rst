.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use first-party data sources with Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use first-party data sources with Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        First-party data sources

==================================================
First-party data sources
==================================================

.. backstory-start

Third-party data, such as from cookies that track a product or brand on someone else's website, are no longer supported by the Firefox and Safari web browsers, and support for third-party cookies will be removed from Chrome. This means that more than 75% of a user's browsing activity cannot be tracked via third-party data. This percentage does not include user activity that occurs on mobile applications, which are typically tracked in ways that do not use cookies.

This is due to a combination of emerging trends around data transparency that give users more control over their data along with new government policies that mandate this transparency, such as General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA).

With the value of using third-party data rapidly degrading, it's time to shift focus to first-party data.

.. backstory-end

.. first-party-data-start

First-party data, such as from cookies that directly track a product or brand on a customer's own website and clickstream events that captures a user's activity from within a mobile application, has become an essential part of any strategy that markets to customers based on their shopping preferences.

Capturing reliable first-party data is a very important part of understanding how your customers interact with your products and your brand. First-party data can be sent to Amperity as part of a broad strategy to build a complete data foundation that can then be associated with important profile attributes.

.. first-party-data-end


.. _data-source-first-party-clickstream-vs-cookies:

Clickstream vs. cookies
==================================================

.. why-amperity-start

First-party data captures how your customers interact with your brand. Applying this data toward a unified understanding of a customer's interaction with your products and brands can be prohibitive.

* Clickstream events for mobile applications are very granular and complex, are difficult to use as a singular source of data, and are often stored separately from first-party cookie data.
* First-party cookies can help identify customer behavior and connect website activity to other interaction records, such as loyalty programs, points of sale, and other channels. This data is usable even when a customer does not log in.

Amperity is built to handle this complexity. Billions of PII-based customer records from legacy and modern marketing systems, as well as hundreds of billions of interaction records that describe how individuals interact with products and brands are analyzed by Amperity on a daily basis.

Amperity can analyze first-party cookies and clickstream events to associate those interaction records to a unique customer. For example. clickstream events identify a product was browsed via a mobile application, first-party cookies identify that product was purchased online, and the Amperity ID associates a unique individual to both clickstream and first-party cookie interaction records. All of these results are available in the customer 360 database Use these results to create more useful marketing and analytics use cases.

In addition to using first-party data as a fundamental part of your marketing strategy, understanding that first-party data, along knowing to which individual its associated, will help you be ready for future best practices around information security and knowing who's who in your data set.

.. why-amperity-end


.. _data-source-first-party-use-cases:

Use cases
--------------------------------------------------

.. data-source-first-party-use-cases-start

Using first-party data as part of the effort to understand your customer helps with questions like:

* What products are my customers viewing?
* What products are my customers viewing the most?
* Do these views correspond to purchase events?
* What is the customer's purchase history?
* What devices are associated with this customer?
* Does this customer have a preferred device?
* What interactions did a customer have with a product prior to a login or identification event?
* Based on online and offline purchase history, is this customer's lifetime value high, medium, or low?
* What is this customer's preferred channel? A retail store? A website? A mobile application?
* Did the customer add items to their cart, but not purchase the items?
* Did the customer eventually purchase those items via a different channel?
* Are there other products to recommend?

These questions and answers are an important part of identifying downstream marketing efforts.

.. data-source-first-party-use-cases-end


.. _data-source-first-party-raw-clickstream:

Raw clickstream data
==================================================

.. data-source-first-party-raw-clickstream-start

Raw clickstream data should be provided to Amperity as a targeted subset of operational data points. This filtering can be done in two ways:

#. Recommended. Configure the application that is sending clickstream data to send files that contain only a useful subset of fields. Configure these files as feeds and run the files that contain useful clickstream data on a daily basis.
#. Use a saved query to filter the fields into a useful subset prior to loading the data to Amperity, and then use two domain tables: one for all of the raw data and the other for the subset of useful data.

   The domain table with all of the raw data should never be made available to Stitch and never added to the customer 360 database.

   The domain table with the useful subset of data should be processed on a regular basis and may be made available to Stitch if it contains meaningful profile (PII) data, and then added to the customer 360 database as a passthrough table.

   This dual-domain table approach ensures that Amperity has direct access to a filtered subset of operational clickstream data and that the superset of data does not require daily processing. Updates to that filtered subset can be done quickly by updating the saved query instead of creating a new feed.

.. data-source-first-party-raw-clickstream-end


.. _data-source-first-party-raw-clickstream-adobe-analytics:

Adobe Analytics
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-adobe-analytics-start
   :end-before: .. term-adobe-analytics-end

.. data-source-first-party-raw-clickstream-adobe-analytics-start

.. vale off

Clickstream data from Adobe Analytics `contains standard fields <https://experienceleague.adobe.com/docs/analytics/export/analytics-data-feed/data-feed-contents/datafeeds-reference.html>`__ |ext_link|, and then `up to 250 conversion variables (evar1-evar250) <https://docs.adobe.com/help/en/analytics/admin/admin-tools/conversion-variables/conversion-var-admin.html>` |ext_link|.

.. vale on

Conversion variables are customer-specific and represent events that identify:

* The customer, such as IDs or PII
* Customer interactions
* Purchases, transactions, and prices
* Marketing campaign IDs that tie the customer to marketing efforts
* Behaviors that may be useful to better understand the customer

.. data-source-first-party-raw-clickstream-adobe-analytics-end

.. data-source-first-party-raw-clickstream-adobe-analytics-steps-start

Adobe Analytics can :doc:`send clickstream data to the SFTP site built into Amperity <source_adobe_analytics>` as a data feed.

.. data-source-first-party-raw-clickstream-adobe-analytics-steps-end


.. _data-source-first-party-raw-clickstream-google-analytics:

Google Analytics
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-analytics-start
   :end-before: .. term-google-analytics-end

.. data-source-first-party-raw-clickstream-google-analytics-start

Clickstream data from Google Analytics `contains a predefined series of fields <https://support.google.com/analytics/answer/3437719?hl=en>`__ |ext_link|, with sets of fields available for:

* Identifiers, such as client ID, user ID, visit ID, along with dates and times
* Totals, such as hits, page views, bounces, time on screen
* Traffic sources, such as campaign IDs, customer IDs, Google AdWords
* Devices, such as device type, operating system, screen resolution
* Geographic data, such as state, city, latitude, longitude
* Hits, including web and app, and then actions based on hits
* User-defined custom dimensions

.. data-source-first-party-raw-clickstream-google-analytics-end

.. data-source-first-party-raw-clickstream-google-analytics-example-start

Use a Spark SQL query similar to:

.. code-block:: sql
   :linenos:

   SELECT
     _c1 AS clientId,
     _c2 AS visitorId,
     _c3 AS userId,
     _c4 AS visitNumber,
     _c5 AS visitId,
     _c6 AS visitStartTime,
     _c7 AS date,
     _c8 AS totals.hits,
     _c9 AS totals.pageviews,
     _c10 AS totals.timeOnScreen,
     _c11 AS totals.timeOnSite,
     _c12 AS totals.transactions,
     _c13 AS trafficSource.adwordsClickInfo.campaignId,
     _c14 AS trafficSource.adwordsClickInfo.customerId,
     _c15 AS trafficSource.keyword,
     _c16 AS device.browser,
     _c17 AS device.operatingSystem,
     _c18 AS geoNetwork.city,
     _c19 AS hits.dataSource,
     _c20 AS hits.eCommerceAction,
     _c21 AS customDimensions,
     _c22 AS customDimensions.index,
     _c23 AS customDimensions.value,
   FROM appdata

.. data-source-first-party-raw-clickstream-google-analytics-example-end
