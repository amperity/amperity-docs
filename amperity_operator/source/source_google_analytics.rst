.. https://docs.amperity.com/operator/


.. |source-name| replace:: Google Analytics
.. |plugin-name| replace:: Google Analytics 4
.. |feed-name| replace:: Transactional Analytics
.. |example-filenamex| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **google-analytics-4**
.. |what-pull| replace:: data from websites and apps


.. meta::
    :description lang=en:
        Configure Amperity to pull GA4 property reports from Google Analytics.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull GA4 property reports from Google Analytics.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull GA4 property reports from Google Analytics

==================================================
Pull from Google Analytics
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-analytics-start
   :end-before: .. term-google-analytics-end

.. source-google-analytics-start

Amperity can be configured to pull Google Analytics 4 (GA4) property reports using the `batchRunReports <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/batchRunReports>`__ |ext_link| endpoint.

.. source-google-analytics-end

.. source-google-analytics-tip-start

.. tip:: Use this data source to |source_google_analytics_build_reports|.

.. source-google-analytics-tip-end

.. source-google-analytics-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-google-analytics-get-details>`
#. :ref:`Configure OAuth for Google Analytics <source-google-analytics-configure-oauth>`
#. :ref:`Add courier <source-google-analytics-add-courier>`
#. :ref:`Review feed and domain table <source-google-analytics-review-data>`
#. :ref:`Run courier <source-google-analytics-run-courier>`
#. :ref:`Add to courier group <source-google-analytics-add-to-courier-group>`

.. source-google-analytics-steps-to-pull-end


.. _source-google-analytics-get-details:

Get details
==================================================

.. source-google-analytics-get-details-start

#. An account with permission to log in to |source-name| as a standard administrator. This step is :ref:`required to configure OAuth <source-google-analytics-configure-oauth>`.
#. Your |source-name| **Account ID** and **Property ID**.

   .. note:: These ID values are available from a dropdown menu in the configuration for this data source after it has been :ref:`configured to use OAuth <source-google-analytics-configure-oauth>`.

.. source-google-analytics-get-details-end


.. _source-google-analytics-configure-oauth:

Configure OAuth
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oauth-start
   :end-before: .. term-oauth-end

**To configure OAuth**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-oauth-configure-start
   :end-before: .. sources-oauth-configure-end


.. _source-google-analytics-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-google-analytics-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   Select |credential-type| as the **Credential Type**.

#. Select the user account you added when :ref:`configuring OAuth <source-google-analytics-configure-oauth>`. The **Refresh token** should populate automatically.
#. Click **Continue**.
#. Under **Google Analytics 4 Settings**, select the **Account ID**, and then the **Property ID**.
#. Under **Select Data to Ingest** select **Transactional Analytics 4**.
#. Click **Create**.

.. source-google-analytics-add-courier-steps-end


.. _source-google-analytics-review-data:

Review feed and domain table
==================================================

.. source-google-analytics-review-data-start

After creating the |source-name| courier it will create a source named |source-name| and a feed named |feed-name| that contains the fields that Amperity pulls from the configured Google Analytics 4 property.

.. source-google-analytics-review-data-end

.. source-google-analytics-review-data-table-start

The following fields will be available:

* **itemRevenue**
* **transactionId** (assigned the **pk** semantic tag)
* **browser**
* **sessionCampaignName**
* **sessionSource**
* **sessionGoogleAdsAdGroupName**
* **date**
* **deviceCategory**
* **operatingSystem**
* **operatingSystemVersion**
* **sessionMedium**
* **sessionGoogleAdsAdGroupId**

.. source-google-analytics-review-data-table-end

.. source-google-analytics-review-data-important-start

.. important:: The |feed-name| feed for |source-name| cannot be edited and should not be made available to Stitch.

.. source-google-analytics-review-data-important-end


.. _source-google-analytics-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-google-analytics-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
