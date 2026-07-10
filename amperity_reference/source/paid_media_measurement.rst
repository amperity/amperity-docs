.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Set up a measurement courier to bring Meta and Google paid media performance data into Amperity, and then use AmpAI to analyze it.

.. meta::
    :content class=swiftype name=body data-type=text:
        Set up a measurement courier to bring Meta and Google paid media performance data into Amperity, and then use AmpAI to analyze it.

.. meta::
    :content class=swiftype name=title data-type=string:
        Paid Media Measurement & Optimization

==================================================
Paid Media Measurement & Optimization
==================================================

.. paid-media-measurement-overview-start

Paid Media Measurement & Optimization brings your paid media performance data from Meta and Google into Amperity where it is available to AmpAI for analysis alongside your customer data.

There are two parts to it:

#. **Set up a measurement courier** for Meta and/or Google. The courier pulls paid media performance data into your tenant on a daily schedule and adds it to the Customer 360 database.
#. **Ask AmpAI about paid media performance** using natural language. AmpAI answers questions about your paid media data without requiring you to write SQL.

.. paid-media-measurement-overview-end


.. _paid-media-measurement-how-it-works:

How it works
==================================================

.. paid-media-measurement-how-it-works-start

A measurement courier connects to Meta or Google using an authorized credential, and then pulls paid media performance data for a selected ad account into Amperity. The data lands in the Customer 360 database under a dedicated namespace for each platform, one for Meta and one for Google.

After the courier is set up, a courier group runs every day to keep the data current. Because the performance data lands in the Customer 360 database, it is available to AmpAI, which can use it to answer questions about paid media performance.

.. paid-media-measurement-how-it-works-end


.. _paid-media-measurement-requirements:

Requirements
==================================================

.. paid-media-measurement-requirements-start

Before you set up a measurement courier, make sure you have:

* An authorized credential for the platform you want to measure--Meta or Google. Add and authorize credentials from the **Credentials** page. See :doc:`Credentials <credentials>`.
* Access to the ad account whose performance data you want to bring into Amperity.
* AmpAI enabled for your tenant, so that you can ask questions about paid media performance. See :doc:`AmpAI <ampai>`.

.. paid-media-measurement-requirements-end


.. _paid-media-measurement-setup:

Set up a measurement courier
==================================================

.. paid-media-measurement-setup-start

Set up one measurement courier for each platform and ad account you want to measure. Add a measurement courier the same way you add any other courier, from the **Sources** page.

#. From **Sources**, open the **Couriers** tab, and then click **Add courier**.
#. For the plugin, select **Facebook Ads Measurements** or **Google Ads Measurements**.
#. Enter a **Name** for the courier.
#. Select the **Credential type**, and then select an authorized **Credential**.
#. Select the ad account to measure:

   * For **Facebook Ads Measurements**, select an **Account ID**.
   * For **Google Ads Measurements**, select a **Customer ID**.

#. Save the courier.

.. note::

   When you save the courier, Amperity sets up everything needed to keep the data current. It creates a courier group that runs once a day, creates the domain tables that the performance data lands in, and starts a first run that backfills approximately the previous twelve months of data. The first run can take longer than later daily runs.

.. paid-media-measurement-setup-end

To learn more about couriers and courier groups, see :doc:`Couriers <couriers>`.


.. _paid-media-measurement-data:

What data lands and how it refreshes
==================================================

.. paid-media-measurement-what-lands-start

Paid media performance data lands in the Customer 360 database as domain tables, organized under a separate namespace for each platform, one for Meta and one for Google. Within each namespace, tables are grouped by the type of data they hold, including delivery data (such as spend, impressions, and clicks), conversion actions, and metadata. Tables are provided at campaign, ad set or ad group, and ad grain, along with breakdowns by dimensions such as age, gender, device, and placement.

The measurement courier keeps this data current:

* The first run backfills approximately the previous twelve months of performance data.
* After that, the courier group runs once a day to bring in new data and to refresh recent data as the platforms restate conversions.

Because these tables are part of the Customer 360 database, you can browse them alongside your other domain tables. See :doc:`Custom domain tables <domain_tables>`.

.. paid-media-measurement-what-lands-end


.. _paid-media-measurement-ampai:

Query paid media performance with AmpAI
==================================================

.. paid-media-measurement-ampai-start

After paid media performance data lands in the Customer 360 database, you can use AmpAI to analyze it with natural language---no SQL required. AmpAI recognizes the paid media tables and can answer questions about performance across Meta and Google.

Ask AmpAI questions such as:

* "Compare the performance of Facebook and Instagram last month."
* "Rank my campaigns by return on ad spend."
* "Which campaigns show a declining click-through rate week over week?"
* "Show me reach by campaign."

AmpAI uses a set of standard paid media metrics as context when it answers, including return on ad spend (ROAS), cost per acquisition (CPA), click-through rate (CTR), cost per mille (CPM), cost per click (CPC), data freshness, and attribution status.

For how to ask questions, view the generated SQL, and work with results, see :doc:`AmpAI <ampai>` and :doc:`Customer Data Assistant <customer_data_assistant>`.

.. paid-media-measurement-ampai-end
