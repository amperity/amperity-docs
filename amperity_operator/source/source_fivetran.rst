.. https://docs.amperity.com/operator/


.. |source-name| replace:: any Fivetran-enabled data source


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Fivetran-enabled data sources.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Fivetran-enabled data sources.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Fivetran-enabled data sources

==================================================
Fivetran-enabled data sources
==================================================

.. source-fivetran-start

Fivetran is a third-party application that collects data from a wide variety of sources, and then loads that data to Snowflake tables. This data can be made available to Amperity from those Snowflake tables.

.. source-fivetran-end

.. source-fivetran-why-start

.. admonition:: Why does Amperity use Fivetran?

   Amperity uses Fivetran to enable a wide variety of data sources. This is for many reasons.

   #. Customers may choose to centralize their data on Snowflake, regardless of the built-in sources that Amperity offers.
   #. Customers may require data sources that are not built-in to Amperity, but are availble from Fivetran.

.. source-fivetran-why-end


.. _source-fivetran-generic-howitworks:

How Fivetran-enabled sources work
==================================================

.. source-fivetran-generic-howitworks-start

Every Fivetran-enabled workflow is different. Some workflows require permission to intstall Fivetran into your application. Some workflows require an SSH tunnel during the configuration process to enable database interactions. Once configured in Fivetran, all Fivetran-enabled sources use an Amperity built-in Snowflake connector.

.. source-fivetran-generic-howitworks-end

.. image:: ../../images/source-fivetran-generic.png
   :width: 600 px
   :alt: Pull data to Amperity from Fivetran.
   :align: left
   :class: no-scaled-link

.. source-fivetran-generic-howitworks-callouts-start

A Fivetran-enabled data source works like this:

#. Fivetran is configured to pull data from a data source. This process requires allowing Fivetran the right level of access to pull that data from your data source to Fivetran.
#. Fivetran pulls that data into one or more Snowflake tables.

   .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-does-not-store-data-start
      :end-before: .. sources-get-details-fivetran-does-not-store-data-end

#. Amperity is configured to pull data to Amperity from those Snowflake tables.
#. Domain tables within Amperity are refreshed.
#. Customer profiles are made available to Stitch. All data is passed to your customer 360 database. The Amperity ID links records across data sources for each unique customer.

.. source-fivetran-generic-howitworks-callouts-end

.. source-fivetran-generic-documented-start

.. vale off

.. tip:: There are a number of Fivetran-enabled data sources that may be configured directly from the Amperity user interface. The following data sources do not require Snowflake *and* do not require using Fivetran:

   * :doc:`Adobe Analytics <source_adobe_analytics>` (pull directly using SFTP)
   * :doc:`Amazon S3 <source_amazon_s3>` (pull any file from cloud-based storage)
   * :doc:`Azure Blob Storage <source_azure_blob_storage>` (pull any file from cloud-based storage)
   * :doc:`Braze <source_braze>` (pull directly using an Amazon S3-based workflow)
   * :doc:`Cordial <source_cordial>` (pull directly using a REST API)
   * :doc:`Google Analytics <source_google_analytics>` (pull directly using a REST API)
   * :doc:`Google Cloud Storage <source_google_cloud_storage>` (pull any file from cloud-based storage)
   * :doc:`Heap <source_heap>` (pull directly using an Amazon S3-based workflow)
   * :doc:`Klaviyo <source_klaviyo>` (pull directly using a REST API)
   * :doc:`Optimizely <source_optimizely>` (pull directly using an Amazon S3-based workflow)
   * :doc:`Sailthru by Marigold <source_sailthru>` (pull directly using a REST API)
   * :doc:`Salesforce Marketing Cloud <source_salesforce_marketing_cloud>`
   * :doc:`SFTP <source_sftp>` (pull data from any SFTP site)

.. vale on

.. source-fivetran-generic-documented-start


.. _source-fivetran-sources:

Fivetran-enabled sources
==================================================

.. source-fivetran-sources-start

Amperity does not document every Fivetran-enabled data source workflow on its own page, with the following exceptions: :doc:`Adobe Commerce (Magento) <source_adobe_commerce>`, :doc:`HubSpot <source_hubspot>`, :doc:`Kustomer <source_kustomer>`, :doc:`Salesforce Pardot <source_salesforce_pardot>`, and :doc:`Square <source_square>`.

This group of topics describes the specific steps that are required for those data sources, including the steps you must do in Fivetran and the steps you must do in Amperity. This group of topics is represenatitive of the typical end-to-end configuration process that is required by many Fivetran-enabled data sources.

.. source-fivetran-sources-end

.. source-fivetran-sources-important-start

.. caution:: The documentation for how to configure each Fivetran-enabled data source is availble from Fivetran. Please use link in the "Fivetran Docs" column in the table below to open that page and to learn more about how to configure that data source for Fivetran.

   All of the configuration requirements and steps for each Fivetran-enabled data source are found on the page for that data source within Fivetran documentation. Use the link in the table below to open that data source's page within the |fivetran_documentation| site.

   All configuration requirements for connecting a data source to Fivetran are specified in Fivetran documentation. Be sure to review those requirements. In a scenario where your Amperity representative will configure Fivetran on your behalf, you need to provide to your Amperity representative those details.

   Amperity uses Snowflake to pull data from Fivetran for all Fivetran-enabled data sources.

.. source-fivetran-sources-important-end

.. source-fivetran-sources-start

The following table is a list of Fivetran-enabled data sources. You must first configure these data sources to make their data available to Fivetran and load it successfully, after which you can use a Snowflake connector in Amperity to pull that data to Amperity.

.. source-fivetran-sources-end

.. source-fivetran-sources-table-start

.. list-table::
   :widths: 140 220 240
   :header-rows: 1

   * - 
     - Fivetran docs
     - Description
	 
   * - .. figure:: ../../amperity_base/source/_static/connector-adjust.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-adjust-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_adjust|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-adjust-start
          :end-before: .. term-adjust-end

   * - .. figure:: ../../amperity_base/source/_static/connector-adobe-aec.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-adobe-aec.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_adobe|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-adobe-analytics-start
          :end-before: .. term-adobe-analytics-end

   * - .. figure:: ../../amperity_base/source/_static/connector-adroll.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-adroll-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_adroll|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-adroll-start
          :end-before: .. term-adroll-end

   * - .. figure:: ../../amperity_base/source/_static/connector-airtable.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-airtable-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_airtable|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-airtable-start
          :end-before: .. term-airtable-end

   * - .. figure:: ../../amperity_base/source/_static/connector-amazon-aws.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-amazon-aws-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_amazon_ads|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amazon-ads-start
          :end-before: .. term-amazon-ads-end

   * - .. figure:: ../../amperity_base/source/_static/connector-amazon-aurora.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-amazon-aurora.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_amazon_aurora_mysql|

       |fivetran_amazon_aurora_postgresql|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amazon-aurora-start
          :end-before: .. term-amazon-aurora-end

   * - .. figure:: ../../amperity_base/source/_static/connector-amazon-cloudfront.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-amazon-cloudfront.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_amazon_cloudfront|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amazon-cloudfront-start
          :end-before: .. term-amazon-cloudfront-end

   * - .. figure:: ../../amperity_base/source/_static/connector-amazon-dynamodb.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-amazon-dynamodb.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_amazon_dynamodb|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amazon-dynamodb-start
          :end-before: .. term-amazon-dynamodb-end

   * - .. figure:: ../../amperity_base/source/_static/connector-amazon-s3.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-amazon-s3.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_amazon_s3|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amazon-s3-start
          :end-before: .. term-amazon-s3-end

   * - .. figure:: ../../amperity_base/source/_static/connector-amplitude.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-amplitude.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_amplitude|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amplitude-start
          :end-before: .. term-amplitude-end

   * - .. figure:: ../../amperity_base/source/_static/connector-apache-kafka.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-apache-kafka.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_apache_kafka|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-apache-kafka-start
          :end-before: .. term-apache-kafka-end

   * - .. figure:: ../../amperity_base/source/_static/connector-apple.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-apple-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_apple_search_ads|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-apple-search-ads-start
          :end-before: .. term-apple-search-ads-end

   * - .. figure:: ../../amperity_base/source/_static/connector-appsflyer.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-appsflyer.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_appsflyer|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-appsflyer-start
          :end-before: .. term-appsflyer-end

   * - .. figure:: ../../amperity_base/source/_static/connector-jira.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-jira-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_atlassian_jira|
     - Atlassian Jira is an application designed for issues tracking, project management, and follow-through.

   * - .. figure:: ../../amperity_base/source/_static/connector-aws-kinesis.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-aws-kinesis.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_aws_kinesis|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amazon-kinesis-data-firehose-start
          :end-before: .. term-amazon-kinesis-data-firehose-end

   * - .. figure:: ../../amperity_base/source/_static/connector-aws-lambda.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-aws-lambda.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_aws_lambda|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-aws-lambda-start
          :end-before: .. term-aws-lambda-end

   * - .. figure:: ../../amperity_base/source/_static/connector-microsoft-azure.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-microsoft-azure.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_azure_cloud_functions|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-azure-cloud-functions-start
          :end-before: .. term-azure-cloud-functions-end

   * - .. figure:: ../../amperity_base/source/_static/connector-bigcommerce.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-bigcommerce-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_bigcommerce|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-bigcommerce-start
          :end-before: .. term-bigcommerce-end

   * - .. figure:: ../../amperity_base/source/_static/connector-box.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-box.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_box|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-box-start
          :end-before: .. term-box-end

   * - .. figure:: ../../amperity_base/source/_static/connector-branch.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-branch-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_branch|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-branch-start
          :end-before: .. term-branch-end

   * - .. figure:: ../../amperity_base/source/_static/connector-braze.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-braze-dark.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_braze|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-braze-start
          :end-before: .. term-braze-end

   * - .. figure:: ../../amperity_base/source/_static/connector-campaign-manager.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-campaign-manager.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_campaign_manager|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-google-campaign-manager-start
          :end-before: .. term-google-campaign-manager-end

   * - .. figure:: ../../amperity_base/source/_static/connector-coupa.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-coupa.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_coupa|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-coupa-start
          :end-before: .. term-coupa-end

   * - .. figure:: ../../amperity_base/source/_static/connector-cr1t30.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-cr1t30.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_criteo|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-criteo-start
          :end-before: .. term-criteo-end

   * - .. figure:: ../../amperity_base/source/_static/connector-delighted.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-delighted.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_delighted|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-delighted-start
          :end-before: .. term-delighted-end

   * - .. figure:: ../../amperity_base/source/_static/connector-dropbox.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-dropbox.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_dropbox|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-dropbox-start
          :end-before: .. term-dropbox-end

   * - .. figure:: ../../amperity_base/source/_static/connector-facebook-ads.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-facebook-ads.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_facebook|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-facebook-ads-start
          :end-before: .. term-facebook-ads-end

   * - .. figure:: ../../amperity_base/source/_static/connector-financial-force.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-financial-force.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_financial_force|
     - FinancialForce is a Salesforce-native cloud ERP application that gives you a complete, customer-centric view of your business.

   * - .. figure:: ../../amperity_base/source/_static/connector-github.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-github-dark.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_github|
     - GitHub is a platform for developers to build personal projects, support their businesses, and work together on open source technologies.

   * - .. figure:: ../../amperity_base/source/_static/connector-gladly.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-gladly.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_gladly|
     - Gladly is a customer service platform that is people-centric, not case-centric. Instead of tickets, Gladly manages a single, lifelong conversation with each of your customers.

   * - .. figure:: ../../amperity_base/source/_static/connector-google-ads.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-google-ads.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_google_ads|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-google-ads-start
          :end-before: .. term-google-ads-end

   * - .. figure:: ../../amperity_base/source/_static/connector-google-analytics.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-google-analytics.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_google_analytics|

       |fivetran_google_analytics_360|

       |fivetran_google_analytics_4|

       |fivetran_google_analytics_4_export|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-google-analytics-start
          :end-before: .. term-google-analytics-end

   * - .. figure:: ../../amperity_base/source/_static/connector-google-cloud.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-google-cloud.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_google_cloud_functions|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-google-cloud-functions-start
          :end-before: .. term-google-cloud-functions-end
 
   * - .. figure:: ../../amperity_base/source/_static/connector-google-cloud.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-google-cloud.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_google_cloud_storage|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-google-cloud-storage-start
          :end-before: .. term-google-cloud-storage-end

   * - .. figure:: ../../amperity_base/source/_static/connector-google-play.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-google-play.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_google_play|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-google-play-start
          :end-before: .. term-google-play-end

   * - .. figure:: ../../amperity_base/source/_static/connector-google.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-google.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_google_search_console|
     - Google Search Console helps you monitor and maintain your site's presence in Google Search results.

   * - .. figure:: ../../amperity_base/source/_static/connector-google-sheets.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-google-sheets.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_google_sheets|
     - Google Sheets is a spreadsheet application that can be shared with others at the same time from your computer, phone or tablet.

   * - .. figure:: ../../amperity_base/source/_static/connector-heap.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-heap.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_heap|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-heap-start
          :end-before: .. term-heap-end


   * - .. figure:: ../../amperity_base/source/_static/connector-helpscout.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-helpscout-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_help_scout|
     - Help Scout is an all-in-one customer service platform that helps you balance everything your customer needs.

   * - .. figure:: ../../amperity_base/source/_static/connector-hubspot.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-hubspot-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_hubspot|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-hubspot-start
          :end-before: .. term-hubspot-end

   * - .. figure:: ../../amperity_base/source/_static/connector-instagram.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-instagram.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_instagram_business|
     - Instagram Business enables creators and companies to connect with a variety of audiences at scale, and track their social media engagement metrics.

   * - .. figure:: ../../amperity_base/source/_static/connector-intercom.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-intercom-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_intercom|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-intercom-start
          :end-before: .. term-intercom-end

   * - .. figure:: ../../amperity_base/source/_static/connector-iterable.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-iterable-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_iterable|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-iterable-start
          :end-before: .. term-iterable-end

   * - .. figure:: ../../amperity_base/source/_static/connector-klaviyo.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-klaviyo-dark.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_klaviyo|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-klaviyo-start
          :end-before: .. term-klaviyo-end

   * - .. figure:: ../../amperity_base/source/_static/connector-kustomer.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-kustomer-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_kustomer|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-kustomer-start
          :end-before: .. term-kustomer-end

   * - .. figure:: ../../amperity_base/source/_static/connector-lightspeed.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-lightspeed-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_lightspeed|
     - Lightspeed Retail is a cloud-based point of sale (POS) solution that is suitable for retailers.

   * - .. figure:: ../../amperity_base/source/_static/connector-linkedin.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-linkedin.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_linkedin_ads|

       |fivetran_linkedin_company_pages|
     - LinkedIn is a social media network focused on professional relationship, business listings, and employment opportunities.

   * - .. figure:: ../../amperity_base/source/_static/connector-magento.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-magento.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_magento_mysql|

       |fivetran_magento_mysql_amazon_rds|
     - Magento is an ecommerce platform which provides online merchants with a flexible shopping cart system, and customization of their online store. Magento is also known as Adobe Commerce.

   * - .. figure:: ../../amperity_base/source/_static/connector-mailchimp.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-mailchimp.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_mailchimp|

       |fivetran_mandrill|
     - Mailchimp provides marketing automation and email marketing services for e-commerce businesses.

   * - .. figure:: ../../amperity_base/source/_static/connector-mariadb.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-mariadb.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_mariadb|

       |fivetran_mariadb_amazon_rds|

       |fivetran_mariadb_azure_database|
     - MariaDB offers open source database and database as a service (DBaaS) solutions to support scalability, mission-critical deployments, and more.


   * - .. figure:: ../../amperity_base/source/_static/connector-adobe-aec.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-adobe-aec.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_marketo|
     - Marketo provides inbound marketing, social marketing, CRM, and other related services.

   * - .. figure:: ../../amperity_base/source/_static/connector-mavenlink.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-mavenlink-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_mavenlink|
     - Mavenlink offers online project management with time tracking, resource planning, collaboration, finance etc. functions.

   * - .. figure:: ../../amperity_base/source/_static/connector-medallia.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-medallia.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_medallia|
     - Medallia is a customer feedback management software platform that enables organizations to collect customer feedback and improve the customer experience.

   * - .. figure:: ../../amperity_base/source/_static/connector-microsoft.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-microsoft.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_microsoft_advertising|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-microsoft-ads-start
          :end-before: .. term-microsoft-ads-end

   * - .. figure:: ../../amperity_base/source/_static/connector-microsoft-azure.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-microsoft-azure.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_microsoft_azure_blob_storage|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-azure-blob-storage-start
          :end-before: .. term-azure-blob-storage-end

   * - .. figure:: ../../amperity_base/source/_static/connector-microsoft-azure.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-microsoft-azure.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_microsoft_azure_sql_database|
     - Microsoft Azure SQL Database is the intelligent, fully managed relational cloud database service built for developers.

   * - .. figure:: ../../amperity_base/source/_static/connector-microsoft-dynamics.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-microsoft-dynamics.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_microsoft_dynamics_365|

       |fivetran_microsoft_dynamics_ax|

       |fivetran_microsoft_dynamics_crm|

       |fivetran_microsoft_dynamics_gp|

       |fivetran_microsoft_dynamics_nav|
     - Microsoft Dynamics 365 is a suite of products that connects people, products, and data and helps transform the way your company does business. 

   * - .. figure:: ../../amperity_base/source/_static/connector-mixpanel.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-mixpanel.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_mixpanel|
     - Mixpanel provides an advanced analytics platform for tracking user actions on web and mobile.

   * - .. figure:: ../../amperity_base/source/_static/connector-mongodb.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-mongodb-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_mongodb|

       |fivetran_mongodb_sharded|
     - MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemas.

   * - .. figure:: ../../amperity_base/source/_static/connector-mysql.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-mysql.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_mysql_database|

       |fivetran_mysql_azure_database|

       |fivetran_mysql_google_cloud_sql|

       |fivetran_mysql_rds|
     - MySQL is an open-source relational database management system. Its name is a combination of "My", the name of co-founder Michael Widenius's daughter My, and "SQL", the abbreviation for Structured Query Language.

   * - .. figure:: ../../amperity_base/source/_static/connector-optimizely.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-optimizely-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_optimizely|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-optimizely-start
          :end-before: .. term-optimizely-end

   * - .. figure:: ../../amperity_base/source/_static/connector-oracle.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-oracle.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_oracle|

       |fivetran_oracle_amazon_rds|

       |fivetran_oracle_ebs|

       |fivetran_oracle_eloqua|

       |fivetran_oracle_fusion_cloud_cx|

       |fivetran_oracle_fusion_cloud_erp|

       |fivetran_oracle_fusion_cloud_hcm|

       |fivetran_oracle_fusion_cloud_scm|

       |fivetran_oracle_peoplesoft|

       |fivetran_oracle_rac|

       |fivetran_oracle_siebel_crm|
     - Oracle is an enterprise-scale and priced relational database with a wide variety of business applications and services.

   * - .. figure:: ../../amperity_base/source/_static/connector-oracle.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-oracle.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_netsuite_suiteanalytics|
     - Oracle Netsuite offers built-in real-time dashboards, reporting, and analysis all integrated right into the ERP, CRM or e-commerce application that you use every day. Previously called Netsuite SuiteAnalytics.

   * - .. figure:: ../../amperity_base/source/_static/connector-outbrain.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-outbrain.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_outbrain|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-outbrain-start
          :end-before: .. term-outbrain-end

   * - .. figure:: ../../amperity_base/source/_static/connector-pendo.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-pendo-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_pendo|
     - Pendo helps product teams understand and guide users to create product experiences.

   * - .. figure:: ../../amperity_base/source/_static/connector-pipedrive.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-pipedrive.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_pipedrive|
     - Pipedrive is a sales CRM and pipeline management solution that enables businesses to plan their sales activities and monitor deals.

   * - .. figure:: ../../amperity_base/source/_static/connector-pinterest.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-pinterest.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_pinterest_ads|
     - Pinterest Ads helps businesses increase brand's visibility and drive conversions.

   * - .. figure:: ../../amperity_base/source/_static/connector-postgresql.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-postgresql.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_postgresql_database|

       |fivetran_postgresql_azure_database|

       |fivetran_postgresql_google_cloud|

       |fivetran_postgresql_rds|
     - PostgreSQL is one of the world's most popular open source relational databases.

   * - .. figure:: ../../amperity_base/source/_static/connector-qualtrics.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-qualtrics-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_qualtrics|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-qualtrics-start
          :end-before: .. term-qualtrics-end

   * - .. figure:: ../../amperity_base/source/_static/connector-recharge.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-recharge-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_recharge|
     - Recharge is a recurring billing and subscriptions service for ecommerce stores that use Shopify.

   * - .. figure:: ../../amperity_base/source/_static/connector-recurly.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-recurly.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_recurly|
     - Recurly provides a recurring billing and subscriptions solution for e-commerce.

   * - .. figure:: ../../amperity_base/source/_static/connector-reddit-ads.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-reddit-ads.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_reddit_ads|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-reddit-ads-start
          :end-before: .. term-reddit-ads-end

   * - .. figure:: ../../amperity_base/source/_static/connector-sage-intacct.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-sage-intacct.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_sage_intacct|
     - Sage Intacct provides real-time financial and operational insights, as well as the ability to automate critical processes.

   * - .. figure:: ../../amperity_base/source/_static/connector-sailthru.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-sailthru-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_sailthru|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-sailthru-start
          :end-before: .. term-sailthru-end

   * - .. figure:: ../../amperity_base/source/_static/connector-salesforce.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-salesforce.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_salesforce|

       |fivetran_salesforce_commerce_cloud|

       |fivetran_salesforce_marketing_cloud|

       |fivetran_salesforce_pardot|
     - Salesforce is a platform that is focused on customer success. Social and mobile cloud technologies--including flagship sales and CRM applications--help companies connect with customers in new ways.

   * - .. figure:: ../../amperity_base/source/_static/connector-sap.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-sap.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_sap_business_bydesign|

       |fivetran_sap_concur|

       |fivetran_sap_erp_hana|
     - SAP stands for System Applications and Products in Data Processing. SAP is a market leader in ERP software and helps companies of all sizes.

   * - .. figure:: ../../amperity_base/source/_static/connector-segment.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-segment.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_segment|
     - Segment is a platform that collects customer data across devices and channels, sends it to third-party tools, internal systems, or SQL databases.

   * - .. figure:: ../../amperity_base/source/_static/connector-sendgrid.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-sendgrid.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_sendgrid|
     - SendGrid is a customer communication platform for transaction-focused and marketing-focused emails.

   * - .. figure:: ../../amperity_base/source/_static/connector-servicenow.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-servicenow-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_servicenow|
     - ServiceNow is a cloud platform that provides service management software as a service.

   * - .. figure:: ../../amperity_base/source/_static/connector-fivetran-sftp.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-fivetran-sftp.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_sftp|
     - Secure File Transfer Protocol (SFTP) is a network protocol that provides file access, file transfer, and file management over a reliable data stream. Also available: |fivetran_ftp|, |fivetran_ftps|, |fivetran_csv_browser_upload|, and |fivetran_email_ingestor|.

   * - .. figure:: ../../amperity_base/source/_static/connector-shopify.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-shopify-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_shopify|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-shopify-start
          :end-before: .. term-shopify-end

   * - .. figure:: ../../amperity_base/source/_static/connector-snapchat.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-snapchat-dark.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_snapchat_ads|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-snapchat-start
          :end-before: .. term-snapchat-end

   * - .. figure:: ../../amperity_base/source/_static/connector-snowplow-analytics.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-snowplow-analytics.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_snowplow_analytics|
     - Snowplow Analytics provides enterprise-level event analytics that is powered by the open source Snowplow platform.

   * - .. figure:: ../../amperity_base/source/_static/connector-spree.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-spree.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_spree_commerce_mysql|
     - Spree Commerce is an API-driven ecommerce framework.

   * - .. figure:: ../../amperity_base/source/_static/connector-sql-server.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-sql-server.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_sql_server|

       |fivetran_sql_server_rds|
     - Microsoft's SQL Server is a powerful enterprise relational database.

   * - .. figure:: ../../amperity_base/source/_static/connector-square.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-square-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_square|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-square-start
          :end-before: .. term-square-end

   * - .. figure:: ../../amperity_base/source/_static/connector-stripe.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-stripe-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_stripe|
     - Stripe is a software platform for businesses of all sizes. Stripe provides transaction histories for all of your online payments.

   * - .. figure:: ../../amperity_base/source/_static/connector-taboola.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-taboola-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_taboola|
     - Taboola helps people find relevant content online, matching them with news stories, articles, blogs, videos, apps, products and other content they are likely to want to explore.

   * - .. figure:: ../../amperity_base/source/_static/connector-tiktok.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-tiktok-dark.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_tiktok_ads|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-tiktok-ads-start
          :end-before: .. term-tiktok-ads-end


   * - .. figure:: ../../amperity_base/source/_static/connector-toast.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-toast.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_toast|
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-toast-start
          :end-before: .. term-toast-end


   * - .. figure:: ../../amperity_base/source/_static/connector-twilio.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-twilio.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_twilio|
     - Twilio powers the future of business communications. Enabling phones, VoIP, and messaging to be embedded into web, desktop, and mobile software.

   * - .. figure:: ../../amperity_base/source/_static/connector-twitter.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-twitter.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_twitter_ads|

       |fivetran_twitter_analytics|
     - Twitter is a social media and online news website that allows marketers and brands to advertise on its platform. Capture data about popular content, retweets, social shares and more for advanced analytics.

   * - .. figure:: ../../amperity_base/source/_static/connector-typeform.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-typeform-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_typeform|
     - Typeform is an online survey management solution for creating forms, surveys, and quizzes that your customers will enjoy answering.

   * - .. figure:: ../../amperity_base/source/_static/connector-uservoice.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-uservoice-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_uservoice|
     - UserVoice gathers and analyzes customer feedback, and then helps you prioritize feature requests that drive product improvements.

   * - .. figure:: ../../amperity_base/source/_static/connector-webhook.png
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-webhook-dark.png
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_webhooks|
     - A webhook is a user-defined HTTP callback that is activated by an event that occurred on your website or within your application.

   * - .. figure:: ../../amperity_base/source/_static/connector-woo-commerce.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-woo-commerce.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_woocommerce|

       |fivetran_woocommerce_mysql|
     - WooCommerce is a customizable, open-source e-commerce platform that turns your WordPress into an online store.

   * - .. figure:: ../../amperity_base/source/_static/connector-workday.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-workday.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_workday|

       |fivetran_workday_hcm|
     - Workday offers enterprise-level software solutions for financial management, human resources, and planning.

   * - .. figure:: ../../amperity_base/source/_static/connector-xero.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-xero.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_xero|
     - Xero accounting software helps to manage invoicing, bank reconciliation, bookkeeping, and more.

   * - .. figure:: ../../amperity_base/source/_static/connector-yahoo.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-yahoo.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_yahoo_gemini|
     - Yahoo Gemini drives traffic to your website, raise brand awareness, promote your app, and increase your online sales.

   * - .. figure:: ../../amperity_base/source/_static/connector-youtube.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-youtube-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_youtube_analytics|
     - YouTube Analytics helps you better understand your video and channel performance by channel or by content owner.

   * - .. figure:: ../../amperity_base/source/_static/connector-zendesk.svg
          :figclass: light-only
          :width: 140 px
          :align: left

       .. figure:: ../../amperity_base/source/_static/connector-zendesk-dark.svg
          :figclass: dark-only
          :width: 140 px
          :align: left
     - |fivetran_zendesk|

       |fivetran_zendesk_chat|

       |fivetran_zendesk_gather|

       |fivetran_zendesk_guide|

       |fivetran_zendesk_sell|

       |fivetran_zendesk_sunshine|

       |fivetran_zendesk_talk|
     - Zendesk Support is a cloud-based customer support platform.

.. source-fivetran-sources-table-end
