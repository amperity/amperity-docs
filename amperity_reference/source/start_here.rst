.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        A landing page for the Amperity A-Z reference.

.. meta::
    :content class=swiftype name=body data-type=text:
        A landing page for the Amperity A-Z reference.

.. meta::
    :content class=swiftype name=title data-type=string:
        Start here

==================================================
Start here
==================================================

.. start-here-start

Welcome to Amperity reference documentation! This collection of topics is about Amperity, ordered from A to Z.

.. start-here-end


.. _start-here-topics:

Topics
==================================================

.. start-here-topics-start

This set of topics covers the following components of Amperity and is organized alphabetically:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Topic
     - Description

   * - **Amperity APIs**
     - Amperity provides APIs for :ref:`interacting with your Amperity tenant <api-amperity>`, :ref:`streaming data to your tenant <api-streaming-ingest>`, and :ref:`building endpoints that are unique to your brand's customer data <api-profile>`.

   * - **Bridge**
     - Use a :doc:`bridge <bridge>` to share data between Amperity and a data lakehouse using industry-standard data formats.

   * - **Campaigns**
     - Use the :doc:`Campaigns page <campaigns>` to configure :ref:`one-time or recurring campaigns <campaigns-types>`. Use a combination of audiences, exclusion lists, control and treatment groups, and sub-audiences to build any type of campaign.

   * - **Courier groups**
     - A :doc:`courier group <courier_groups>` is a list of one (or more) couriers that are run as a group. Use courier groups to define ad hoc and automatic schedules that bring data to Amperity.

   * - **Couriers**
     - A :doc:`courier <couriers>` brings data from external system to Amperity. A courier relies on a :doc:`feed <feeds>` to know which fileset to bring to Amperity for processing.

   * - **Credentials**
     - The **Credentials** page provides a consolidated view for all credentials used to provide access to sources and destinations in your tenant.

   * - **Data exports**
     - A database may be configured to :doc:`export one (or more) tables or an entire database <data_exports>` from Amperity.

   * - **Data tables**
     - A customer 360 database is built using :doc:`standard outputs of the Stitch process <data_tables>`.

   * - **Data templates**
     - A :doc:`data template <data_templates>` defines how columns in Amperity data structures are sent to downstream workflows.

   * - **Databases**
     - The :doc:`Customer 360 page <databases>` enables the use of :doc:`Spark SQL <sql_spark>` to build any database or table based on your raw data combined with the standard outputs of the Stitch process, which provide the stable linking key known as the Amperity ID.

   * - **Domain tables**
     - :doc:`Domain tables <domain_tables>` that contain :ref:`customer records <domain-tables-record-type-customer>` are made available to the Stitch process to identify unique individuals and assign them Amperity IDs.
 
       Domain tables that contain :ref:`interaction records <domain-tables-record-type-interaction>` are used to create attributes that are associated with the unique individuals who have been assigned Amperity IDs.

   * - **Feeds**
     - A feed defines how data should be loaded to Amperity. Use the :ref:`Feed Editor <feed-editor>` to :ref:`standardize field types <feed-field-types>` and :ref:`apply semantic tags <feeds-semantic-tags>` to all of the incoming fields that contain customer and/or interaction records.

   * - **File formats**
     - Amperity supports :doc:`Apache Avro <format_avro>`, :doc:`Apache Parquet <format_parquet>`, :doc:`CBOR <format_cbor>`, :doc:`CSV <format_csv>`, :doc:`JSON <format_json>`, :doc:`NDJSON <format_ndjson>`, :doc:`PSV <format_psv>`, :doc:`streaming JSON <format_json_streaming>`, :doc:`TSV <format_tsv>`, and :doc:`XML <format_xml>` file formats.

   * - **Ingest queries**
     - An :doc:`ingest query <ingest_queries>` is a SQL statement that may be applied to data prior to loading it to Amperity.

   * - **Orchestration groups**
     - An :doc:`orchestration group <orchestration_groups>` defines the schedule that is used to send data from Amperity.

   * - **Orchestrations**
     - An :doc:`orchestration <orchestrations>` defines the relationship between query results and a destination.

   * - **Policies**
     - A :doc:`policy <policies>` represents a set of actions that are available to a user when that policy is assigned to them. All actions within Amperity are controlled by a policy.

   * - **Predictive models**
     - Amperity provides predictive models for :doc:`product affinity <model_product_affinity>`, :doc:`churn propensity <model_churn_propensity>`, and :doc:`predicted customer lifetime value <model_predicted_clv>`.

   * - **Queries**
     - Build :doc:`queries <queries>` against your databases using :doc:`Presto SQL <sql_presto>`, and then :doc:`use orchestrations <orchestrations>` to send those results to any downstream system or workflow.

   * - **Recent activity**
     - Use :doc:`recent activity <notifications>` to learn more about the state of workflows that are currently running in your tenant.

   * - **Sandboxes**
     - Use :doc:`sandboxes <sandboxes>` to safely make configuration changes to your production tenant.

   * - **Segments**
     - Use :doc:`segments <segments>` and segment insights to build audiences, and then :doc:`assign those audiences to campaigns <campaigns>`.

   * - **Semantic tags**
     - A :doc:`semantic tag <semantics>` standardizes profile (PII), transaction, and other important customer details across all columns in all data tables.

   * - **Settings**
     - The :doc:`Settings page <settings>` lets you manage users, configure SSO, define resource groups, and monitor user activity. 

   * - **Single sign-on (SSO)**
     - Amperity supports the use of :doc:`single sign-on (SSO) <sso>` to manage the users who can access your tenant. Learn more about :ref:`how it works with Amperity <sso-howitworks>`, and then request to :ref:`enable SSO for your tenant <sso-use-cases>`.

   * - **SQL -- Presto SQL**
     - Presto is a distributed SQL query engine that is designed to efficiently query vast amounts of data using distributed queries. Presto is used by the Amperity SQL segment editors to define segments, which are SQL queries that return data from stitched data tables.

       Use the :doc:`Amperity Presto SQL reference <sql_presto>` to learn more about how you can use Presto SQL to build queries and segments that return data from your customer 360 database.

   * - **SQL -- Spark SQL**
     - Spark SQL is a high performance SQL query engine that is used by Amperity to ingest data, create domain tables, and extend the outcome of the Stitch process in your customer 360 database.

       Use the :doc:`Amperity Spark SQL reference <sql_spark>` to learn more about how you can use Spark SQL to build ingest queries, custom domain tables, and database tables. You may also refer to the official |ext_sparksql_version_current| documentation for more information about functions that are not covered by the Amperity Spark SQL reference.

   * - **Stitch**
     - :doc:`Stitch <stitch>` uses patented algorithms to evaluate massive volumes of data to discover the hidden connections in your customer records that identify unique individuals. Stitch outputs a unified collection of data that assigns a unique identifier to each unique individual that is discovered within your customer records.

   * - **Workflows**
     - The :doc:`Workflow page <workflows>` provides a view of all of your tenant workflows.

.. start-here-topics-end
