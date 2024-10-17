.. 
.. https://docs.amperity.com/datagrid/
.. 

.. meta::
    :description lang=en:
        An overview of sending data from Amperity to a variety of downstream destinations.

.. meta::
    :content class=swiftype name=body data-type=text:
        An overview of sending data from Amperity to a variety of downstream destinations.

.. meta::
    :content class=swiftype name=title data-type=string:
        General advice

==================================================
General advice
==================================================

.. send-data-to-amperity-start

This topic contains general advice and recommendations for sending data to Amperity.

Sending data to Amperity is the combination of:

#. Identifying a data source. It is important to define data sources to have predictable handoffs.
#. Determining the location from which that data source will be made available to Amperity, the file format to be provided, and the process that will be used (cloud-based storage, SFTP, FiveTran, REST API, or Snowflake) to make that available.

   .. important:: Even if you do not see a data source in various lists of data sources that are shown to be "available" (such as on the Amperity website or on various pages within the documentation site), this does not mean you cannot send data from that source. A significant percentage of data sources used by Amperity customers are enabled using cloud-based storage.

#. Configuring Amperity to process that data.

For a production environment, most data sources are configured to run once per 24-hour time period. This means that within that 24-hour time period, the data must be made available to Amperity for processing early enough within that 24-hour time period to allow Amperity to complete all downstream processing. Downstream processing includes:

* Running Stitch for identity resolution
* Refreshing all databases based on Stitch output
* Processing all queries and segments that have downstream dependencies
* Sending query results or audiences to all configured destinations and marketing channels

.. note:: Preprocessing or filtering data before sending it to Amperity is typically not required, but sometimes business and security concerns will require it.

.. send-data-to-amperity-end

.. send-data-to-amperity-sections-start

The following sections contain specific advice and/or recommendations:

* :ref:`Credentials and secrets <send-data-to-amperity-credentials-and-secrets>`
* :ref:`File formats <send-data-to-amperity-file-format>`
* :ref:`Pull data vs. push data <send-data-to-amperity-pull-vs-push>`
* :ref:`Optimize Apache Spark <send-data-to-amperity-apache-spark>`
* :ref:`Connection details <send-data-to-amperity-connection-details>`
* :ref:`Date formats <send-data-to-amperity-date-formats>`
* :ref:`IP allowlists <send-data-to-amperity-ip-allowlists>`
* :ref:`Large datasets <send-data-to-amperity-large-datasets>`

.. send-data-to-amperity-sections-end


.. _send-data-to-amperity-credentials-and-secrets:

Credentials and Secrets
==================================================

.. send-data-to-amperity-credentials-and-secrets-start

Amperity requires the ability to connect to, and then read data from the data source. The credentials that allow that connection and the ability to read that data are entered into the Amperity user interface while configuring a courier.

These credentials are created and managed by the owner of the data source, which is often external to Amperity (but is sometimes a system that is owned by Amperity, such as Amazon S3 or Azure Blob Storage). Credentials must be provided to Amperity using SnapPass to complete the configuration.

.. send-data-to-amperity-credentials-and-secrets-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-snappass-start
   :end-before: .. term-snappass-end


.. _send-data-to-amperity-file-format:

File Formats
==================================================

.. send-data-to-amperity-file-format-start

The following data formats are ranked in terms of preference:

#. :ref:`Apache Parquet files <send-data-to-amperity-file-format-parquet>`
#. :ref:`CSV files <send-data-to-amperity-file-format-csv>`
#. :ref:`JSON files with simple nested data only <send-data-to-amperity-file-format-json>`
#. :ref:`Other data formats <send-data-to-amperity-file-format-other>`

.. send-data-to-amperity-file-format-end


.. _send-data-to-amperity-file-format-parquet:

Apache Parquet
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-apache-parquet-start
   :end-before: .. term-apache-parquet-end


.. _send-data-to-amperity-file-format-csv:

CSV
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-csv-start
   :end-before: .. term-csv-end

.. send-data-to-amperity-file-format-csv-note-start

.. note:: Other delimited-file formats--TSV and PSV--are supported. They follow the same recommendations as CSV files and may be considered interchangeable.

.. send-data-to-amperity-file-format-csv-note-end


.. _send-data-to-amperity-file-format-json:

JSON
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-json-start
   :end-before: .. term-json-end


.. _send-data-to-amperity-file-format-other:

Other data formats
--------------------------------------------------

.. send-data-to-amperity-file-format-other-start

Amperity can ingest data from many types of data sources, such as:

* Output from relational database management systems
* |format_parquet| files along with non-Parquet files that are common to Apache Hadoop environments, such as |format_avro|
* Legacy data outputs, such as |format_dat|
* |format_psv| and |format_tsv| files
* |format_ndjson|
* |format_json| and |format_json_streaming|
* Many REST APIs
* Snowflake tables, including data sources that use FiveTran to send data
* |format_cbor|

.. send-data-to-amperity-file-format-other-end


.. _send-data-to-amperity-file-format-troubleshoot:

Troubleshoot file ingest errors
--------------------------------------------------

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feed-troubleshoot-ingest-errors-start
   :end-before: .. feed-troubleshoot-ingest-errors-end


.. _send-data-to-amperity-pull-vs-push:

Pull vs. Push
==================================================

.. send-data-to-amperity-pull-vs-push-start

Data may be provided to Amperity in the following ways:

#. Recommended. Amperity pulls data from a cloud-accessible storage location, such as |source_amazon_s3|, |source_azure_blob_storage|, |source_google_cloud_storage|, or any |source_sftp| site.

   This location may be customer-managed (recommended) or Amperity-managed. For Amazon AWS, it is recommended to use cross-account role assumption. For Microsoft Azure, it is recommended to use Azure Data Share.
   
   Some data sources provide a REST API that may be used to provide data to Amperity, such as |source_campaign_monitor|.

   Many data sources are eligible to use FiveTran as the interface that pulls data to Amperity, such as |source_hubspot| |source_klaviyo|, |source_kustomer|, |source_shopify|, |source_sailthru|, and |source_square|.
#. The customer pushes data to Amperity via the |api_streaming_ingest|.

   .. note:: This scenario should only be used for transactional or event-like data that would be streamed as it happens.

Amperity strongly recommends and prefers data exchange to use customer-managed cloud storage locations. This is because many REST APIs are designed for smaller volumes or have record limits. An additional challenge is that many REST APIs are record oriented rather than change oriented. This can result in scenarios like deleted records not showing up in incremental pulls or sources that are missing discrete data on upstream merges.

Systems that support change data capture (CDC) are often suitable, but those types of systems are uncommon. Even when systems do support all of these properties, upstream changes, such as normalizing a status column or changing a billing code, can cause updates to large percentages of records, which can be risky given the preference for 24-hour cadences for all workflows.

A hybrid path where a REST API is used for partial incremental changes, and then a separate file-based delivery path is used for catch-ups (either on regular intervals or on-demand) adds more surface area (i.e. risk) to the workflow.

Some REST APIs support bulk delivery, which can perform with the same type of reliability as cloud-accessible storage locations.

A complete file-based delivery using cloud-accessible storage locations is the most reliable way to get very large data volumes to Amperity.

.. send-data-to-amperity-pull-vs-push-end


.. _send-data-to-amperity-push-data-to-amperity:

Push Data to Amperity
--------------------------------------------------

.. send-data-to-amperity-push-data-to-amperity-start

To push data to Amperity you may use the |api_streaming_ingest|.

.. send-data-to-amperity-push-data-to-amperity-end


.. _send-data-to-amperity-apache-spark:

Apache Spark
==================================================

.. include:: ../../amperity_reference/source/sql_spark.rst
   :start-after: .. sql-spark-recommendation-load-sizes-start
   :end-before: .. sql-spark-recommendation-load-sizes-end


.. _send-data-to-amperity-connection-details:

Connection Details
==================================================

.. send-data-to-amperity-connection-details-start

The following collection details are needed for customer-owned Amazon S3, Azure Blob Storage, and SFTP locations.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Location
     - Details
   * - Amazon S3
     - Access key, secret key, and bucket name.
   * - Azure Blob Storage
     - Using shared access credentials, the name of the container, the blob prefix, and credential details.
   * - SFTP
     - Host name, user name, public key (preferred).

       -or-

       Host name, user name, and passphrase.

.. send-data-to-amperity-connection-details-end


.. _send-data-to-amperity-date-formats:

Date Formats
==================================================

.. include:: ../../amperity_reference/source/format_common.rst
   :start-after: .. format-common-pull-date-formats-start
   :end-before: .. format-common-pull-date-formats-end


.. _send-data-to-amperity-ip-allowlists:

IP addresses for allowlists
==================================================

.. send-data-to-amperity-ip-allowlists-start

You can add Amperity services to allowlists that may be required by upstream systems. The IP address that should be added to the allowlist for the upstream system depends on the service to which that upstream system will connect.

.. send-data-to-amperity-ip-allowlists-end

.. send-data-to-amperity-ip-allowlists-important-start

.. important:: Amperity does not maintain allowlists for connections that are made to Amperity services from upstream systems.

.. send-data-to-amperity-ip-allowlists-important-end

.. send-data-to-amperity-ip-allowlists-warning-start

.. warning:: Using an IP allowlist is not recommended. Many issues can arise when an IP address is on an allowlist within Amazon AWS or Microsoft Azure because both services use their own internal networks for routing.

   * Amazon AWS recommends against using allowlists on the SourceIP condition because it |ext_aws_allowlist|
   * Microsoft Azure suggests that using IP allowlists for shared access signature (SAS) tokens is only recommended for use with IP addresses that are located outside of Microsoft Azure.

.. send-data-to-amperity-ip-allowlists-warning-end

**When connecting to your Amperity tenant**

.. send-data-to-amperity-ip-allowlists-amperity-start

Most connections are made directly to your Amperity tenant. Use one of the following Amperity IP addresses for an allowlist that is required by an upstream system. The specific IP address to use depends on the location in which your tenant is hosted:

* On Amazon AWS use "52.42.237.53"
* On Amazon AWS (Canada) use "3.98.199.97"
* On Microsoft Azure use "104.46.106.84" and "20.81.91.210"
* On Microsoft Azure (EU) use "20.123.127.54"

.. send-data-to-amperity-ip-allowlists-amperity-end

**When connecting to the attached SFTP site**

.. send-data-to-amperity-ip-allowlists-sftp-start

Some connections are made directly to the SFTP site that is included with your Amperity tenant. The specific IP address to use depends on the location in which your tenant is hosted:

* On Amazon AWS use "52.11.51.214"
* On Amazon AWS (Canada) use "52.60.229.171"
* On Microsoft Azure use "20.36.236.80"
* On Microsoft Azure (EU) use "51.104.139.110"

.. send-data-to-amperity-ip-allowlists-sftp-end

.. send-data-to-amperity-ip-allowlists-tip-start

.. tip:: Alternatives to using an allowlist include: 

   #. Cross-account roles within Amazon AWS, which requires using an Amazon Resource Name (ARN) for the role with cross-account access.
   #. Using Azure Data Share.

   Discuss these options with your Amperity representative prior to making a decision to allowlist IP addresses.

.. send-data-to-amperity-ip-allowlists-tip-end


.. _send-data-to-amperity-large-datasets:

Large Datasets
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-large-dataset-start
   :end-before: .. term-large-dataset-end

.. include:: ../../amperity_reference/source/format_common.rst
   :start-after: .. format-common-pull-file-compression-large-datasets-start
   :end-before: .. format-common-pull-file-compression-large-datasets-end
