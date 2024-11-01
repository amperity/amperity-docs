.. 
.. https://docs.amperity.com/amp360/
.. 


.. meta::
    :description lang=en:
        Send query results to a variety of analytics and BI tools.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send query results to a variety of analytics and BI tools.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to analytics and BI tools

==================================================
Send data to analytics and BI tools
==================================================

.. sendto-analytics-bi-start

Amperity supports making data available to all of the leading analytics and business intelligence (BI) tools.

Send your data from Amperity to any of these tools, and then use that data to build dashboards along with anything else that is enabled by your favorite analytics and BI tools.

This topic consolidates the discussion of how to get data from Amperity to your favorite analytics and/or BI tools into a single topic, along with providing links to the documentation for each of the analytics and BI tools.

.. sendto-analytics-bi-end


.. _sendto-analytics-bi-howitworks:

How analytics workflows work
==================================================

.. sendto-analytics-bi-howitworks-start

Workflows that make data available to analytics and BI tools are done in two broad steps.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Send data from Amperity.
          :align: left
          :class: no-scaled-link
     - Use any of the following options:

       #. Send data from Amperity to cloud storage -- one of :doc:`Amazon S3 <destination_amazon_s3>`, :doc:`Azure Blob Storage <destination_azure_blob_storage>`, or :doc:`Google Cloud Storage <destination_google_cloud_storage>`.
       #. Send data to Snowflake.
       #. Send data to a cloud database -- :doc:`Amazon Redshift <destination_amazon_redshift>`, Azure Synapse Analytics, or Google BigQuery.
       #. Send to a location from which you can use Open Database Connectivity (ODBC) or Java Database Connectivity (JDBC) to connect to the data.

       The option that you choose for this step depend on which analytics and/or BI tools you use and/or what type of cloud infrastructure is available to your organization. Many analytics and BI tools support using any of these options. Cloud-based workflows are the most common.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Load data to your favorite analytics or BI tool.
          :align: left
          :class: no-scaled-link
     - Load the data to the analytics and BI tools using the processes and steps that are described in each tool's documentation.

.. sendto-analytics-bi-howitworks-end


.. _sendto-analytics-bi-tools:

Analytics and BI tools
==================================================

The following sections lists some popular analytics and business intelligence tools alphabetically, and then each section describes the options that are available.

* :ref:`Amazon QuickSight <sendto-analytics-bi-tool-amazon-quicksight>`
* :ref:`Domo <sendto-analytics-bi-tool-domo>`
* :ref:`Google BigQuery <sendto-analytics-bi-tool-google-bigquery>`
* :ref:`Looker <sendto-analytics-bi-tool-looker>`
* :ref:`Microsoft Power BI <sendto-analytics-bi-tool-power-bi>`
* :ref:`Pyramid Analytics <sendto-analytics-bi-tool-pyramid-analytics>`
* :ref:`Sisense <sendto-analytics-bi-tool-sisense>`
* :ref:`Tableau <sendto-analytics-bi-tool-tableau>`
* :ref:`Tellius <sendto-analytics-bi-tool-tellius>`
* :ref:`ThoughtSpot <sendto-analytics-bi-tool-thoughtspot>`
* :ref:`Yellowfin <sendto-analytics-bi-tool-yellowfin>`
* :ref:`Zoho Analytics <sendto-analytics-bi-tool-zoho>`


.. _sendto-analytics-bi-tool-amazon-quicksight:

Amazon QuickSight
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-quicksight-start
   :end-before: .. term-amazon-quicksight-end

.. sendto-analytics-bi-tool-amazon-quicksight-start

#. Send CSV or TSV files from Amperity to :doc:`Amazon S3 <destination_amazon_s3>`.
#. Configure Amazon AWS to create a |ext_aws_quicksight_s3|.

.. sendto-analytics-bi-tool-amazon-quicksight-end


.. _sendto-analytics-bi-tool-domo:

Domo
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-domo-start
   :end-before: .. term-domo-end

.. sendto-analytics-bi-tool-domo-start

You can use a variety of |ext_domo_business_intelligence| to analyze data in Domo. Send query results from Amperity to a customer-managed Amazon S3 bucket, and then load that data to Domo as a |ext_domo_dataset|.

.. sendto-analytics-bi-tool-domo-end


.. _sendto-analytics-bi-tool-google-bigquery:

Google BigQuery
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-bigquery-start
   :end-before: .. term-google-bigquery-end

.. sendto-analytics-bi-tool-google-bigquery-start

#. Send CSV or Parquet files from Amperity to :doc:`Amazon S3 <destination_amazon_s3>` or :doc:`Google Cloud Storage <destination_google_cloud_storage>`.
#. Load |ext_google_bigquery_load_parquet| or |ext_google_bigquery_load_csv| from cloud storage or transfer Parquet and CSV |ext_google_bigquery_load_from_amazon_s3|.
#. Enable downstream workflows in analytics and BI tools like :ref:`Microsoft Power BI <sendto-analytics-bi-tool-power-bi>`, or :ref:`Tableau <sendto-analytics-bi-tool-tableau>`. Support or enable real-time downstream workflows with |ext_google_pubsub_overview|.

.. sendto-analytics-bi-tool-google-bigquery-end


.. _sendto-analytics-bi-tool-looker:

Looker
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-looker-start
   :end-before: .. term-google-looker-end

You can connect Looker to cloud databases, including |ext_google_looker_bi_amazon_redshift|, |ext_google_looker_bi_azure_synapse_analytics|, |ext_google_looker_bi_google_bigquery|, and |ext_google_looker_bi_snowflake|.

.. sendto-analytics-bi-tool-looker-end


.. _sendto-analytics-bi-tool-power-bi:

Microsoft Power BI
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-powerbi-start
   :end-before: .. term-microsoft-powerbi-end

.. sendto-power-bi-important-start

Data is not sent from Amperity directly to Microsoft Power BI. Microsoft Power BI must connect to a location that supports queries to that data; Microsoft Power BI cannot connect directly to a static file. Amperity must send data to Microsoft Power BI indirectly by configuring a destination to:

#. Send a CSV file to an Azure container, after which it is :ref:`picked up by Azure Synapse Analytics <sendto-powerbi-connect-to-azure>`.
#. Send a CSV file to Google Cloud Storage, after which it is :ref:`transferred to Google BigQuery <sendto-powerbi-connect-to-google-bigquery>`
#. Send data to |ext_google_bigquery_supported_connectors|.

Microsoft Power BI may be configured to connect directly to Snowflake, Google BigQuery, or Azure Synapse Analytics. The destination workflow in Amperity may be configured to send data on a regular basis to ensure that the data available to the Microsoft Power BI user is up to date.

.. sendto-power-bi-important-end


.. _sendto-analytics-bi-tool-pyramid-analytics:

Pyramid Analytics
--------------------------------------------------

.. sendto-analytics-bi-tool-pyramid-analytics-start

Pyramid Analytics supports using |ext_pyramid_analytics_sources| to pull data from :doc:`Amazon S3 <destination_amazon_s3>` and :doc:`Azure Blob Storage <destination_azure_blob_storage>`.

.. sendto-analytics-bi-tool-pyramid-analytics-end


.. _sendto-analytics-bi-tool-sisense:

Sisense
--------------------------------------------------

.. sendto-analytics-bi-tool-sisense-start

Review the Sisense |ext_sisense_connector_list| and choose the option that works best for you. A variety of options are supported, including :doc:`Amazon Redshift <destination_amazon_redshift>`, :doc:`Amazon S3 <destination_amazon_s3>`, :doc:`Azure Blob Storage <destination_azure_blob_storage>`, :ref:`Google BigQuery <sendto-analytics-bi-tool-google-bigquery>`, :doc:`Google Cloud Storage <destination_google_cloud_storage>`, and Snowflake.

.. sendto-analytics-bi-tool-sisense-end


.. _sendto-analytics-bi-tool-tableau:

Tableau
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-tableau-start
   :end-before: .. term-tableau-end

.. sendto-tableau-important-start

Data is not sent from Amperity directly to Tableau. Tableau must connect to a location that supports queries to that data; Tableau cannot connect directly to a static file. Amperity must send data to Tableau indirectly by configuring a destination to:

#. Send a CSV file to an Amazon S3 bucket, after which it is :ref:`picked up by Amazon Redshift <sendto-tableau-connect-to-amazon-redshift>`.
#. Send a CSV file to an Azure container, after which it is :ref:`picked up by Azure Synapse Analytics <sendto-tableau-connect-to-azure>`.
#. Send a CSV file to Google Cloud Storage, after which :ref:`data is transferred to Google BigQuery <sendto-tableau-connect-to-google-bigquery>`.
#. Send Apache Parquet, Apache Avro, CSV, or JSON files to Snowflake, after which you then :ref:`connect to that data from Tableau <sendto-tableau-connect-to-snowflake>`.

Tableau may be configured to connect directly to Snowflake, Amazon Redshift, or Azure Synapse Analytics. The destination workflow in Amperity may be configured to send data on a regular basis to ensure that the data available to the Tableau user is up to date.

.. sendto-tableau-important-end


.. _sendto-analytics-bi-tool-tellius:

Tellius
--------------------------------------------------

.. sendto-analytics-bi-tool-tellius-start

Tellius is a platform for analytics and BI that unifies visual data intelligence, actionable insights, machine learning capabilities, and custom predictive models.

You can send data to cloud storage and then move that data into a cloud database using any |ext_tellius_connectors|.

.. sendto-analytics-bi-tool-tellius-end


.. _sendto-analytics-bi-tool-thoughtspot:

ThoughtSpot
--------------------------------------------------

.. sendto-analytics-bi-tool-thoughtspot-start

Use |ext_thoughtspot_dataflow| connections to make data available to ThoughtSpot. A variety of options are supported, including :doc:`Amazon Redshift <destination_amazon_redshift>`, :doc:`Amazon S3 <destination_amazon_s3>`, :doc:`Azure Blob Storage <destination_azure_blob_storage>`, :ref:`Google BigQuery <sendto-analytics-bi-tool-google-bigquery>`, :doc:`Google Cloud Storage <destination_google_cloud_storage>`, and Snowflake.

.. sendto-analytics-bi-tool-thoughtspot-end


.. _sendto-analytics-bi-tool-yellowfin:

Yellowfin
--------------------------------------------------

.. sendto-analytics-bi-tool-yellowfin-start

Download |ext_yellowfin| for :doc:`Amazon Redshift <destination_amazon_redshift>`, :doc:`Amazon S3 <destination_amazon_s3>`, :ref:`Google BigQuery <sendto-analytics-bi-tool-google-bigquery>`, :doc:`Google Cloud Storage <destination_google_cloud_storage>`, and Snowflake. Send data to any of these cloud storage locations, connect the JDBC driver to that source, and then open the data in Yellowfin.

.. sendto-analytics-bi-tool-yellowfin-end


.. _sendto-analytics-bi-tool-zoho:

Zoho Analytics
--------------------------------------------------

.. sendto-analytics-bi-tool-zoho-start

You can |ext_zoho_data_feeds| or import data from an |ext_zoho_amazon_s3_bucket|.

.. sendto-analytics-bi-tool-zoho-end
