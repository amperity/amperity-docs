.. 
.. https://docs.amperity.com/
.. 


.. meta::
    :description lang=en:
        Use DataGrid to pull all of your customer data to Amperity, build databases to support your brands and use cases, and then send audiences and query results downstream to support any workflow.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use DataGrid to pull all of your customer data to Amperity, build databases to support your brands and use cases, and then send audiences and query results downstream to support any workflow.

.. meta::
    :content class=swiftype name=title data-type=string:
        About DataGrid

==================================================
About DataGrid
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-datagrid-start
   :end-before: .. term-datagrid-end

.. datagrid-important-start

.. important:: DataGrid is configured by users of Amperity with administrative privileges. These users may belong to your organization and manage Amperity directly or they may be representatives from Amperity who manage DataGrid for you on your behalf. This documentation is written for the administrative users who belong to your organization. Some steps, such as configuring Google Ads and Facebook Ads as destinations, or configuring the SFTP site that is included with Amperity, require additional steps to be done by Amperity representatives and should be initiated by filing a support ticket or by contacting your Amperity representative and asking them to start that process on your behalf.

.. datagrid-important-end

.. datagrid-about-start

DataGrid is the multi-patented infrastructure that powers Amperity. DataGrid handles your customer data with speed, scale, and accuracy and provides optimal performance and interoperability when using any combination of AmpID, Amp360, and AmpIQ.

DataGrid is a cloud-native high-performance infrastructure that runs at scale on your choice of Amazon AWS or Microsoft Azure.

* 100+ integration options to handle any type of data.
* Pull unlimited amounts of structured and semi-structured raw data to Amperity from any source without the need for schema planning or pre-shaping data.
* Use multiple databases, SQL database querying, and the Amperity data explorer to manage your workflows and data transformation options.
* Send data shaped for any destination in any format, such as sending full databases to analytics environments, segments to campaign tools, or attributes to personalization engines.
* Use the sandbox environment to safely make changes with zero downtime to the production environment, including data sources, data models, and workflows.
* Rely on security features, such as SOC2 certification, SSO integration, PII obfuscation, user actions auditing, and more, to keep your data safe.

.. datagrid-about-end


.. _datagrid-common-workflows:

Common workflows
==================================================

.. datagrid-common-workflows-start

The most common workflows for DataGrid involve pulling data to Amperity from a customer data source or sending data from Amperity to a downstream workflow. There are five main areas:

* Pulling data to Amperity
* Configuring and running Stitch
* Configuring the customer 360 database, along with any other custom databases and tables your data requires
* Defining queries that interact with databases and tables in the **Customer 360** page, some of which are used for QA purposes, others are used to generate results to be sent to downstream workflows outside of Amperity
* Sending data from Amperity

After configuring DataGrid to pull data to and send data from Amperity, use these components to configure more complex and more valuable use cases, such as:

* Consolidate data across brands
* Consolidate historical data
* Enterprise change management
* Manage customer data directly
* Reshape data for downstream workflows

.. datagrid-common-workflows-end


.. _datagrid-configure:

Configure DataGrid
==================================================

.. datagrid-configure-start

The following sections provide an overview of configuring DataGrid. The person who configures DataGrid depends on how you have chosen to run Amperity. This might be a member of your organization who has completed the DataGrid certification process or it might be a representative from Amperity who works closely with you during implementation to configure Amperity exactly as you require, but then over time as Amperity runs on a daily basis.

.. datagrid-configure-end

.. datagrid-configure-tip-start

.. tip:: Some information about your configuration must be shared with Amperity, such as a username and passcode required to authenticate and access to various cloud storage services or REST APIs. This information, when it must be shared with an Amperity representative, should be shared using SnapPass.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-snappass-start
      :end-before: .. term-snappass-end

   Open |ext_snappass| to send information to your Amperity representative.

.. datagrid-configure-tip-end


.. _datagrid-sandboxes:

Sandboxes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-sandbox-start
   :end-before: .. term-sandbox-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-sandbox-administrator-policy-start
   :end-before: .. term-sandbox-administrator-policy-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-sandbox-administrator-policy-assign-start
   :end-before: .. term-sandbox-administrator-policy-assign-end

.. include:: ../../amperity_reference/source/sandboxes.rst
   :start-after: .. sandboxes-policy-allow-sandbox-administration-important-start
   :end-before: .. sandboxes-policy-allow-sandbox-administration-important-end

.. include:: ../../amperity_reference/source/sandboxes.rst
   :start-after: .. sandboxes-best-practice-start
   :end-before: .. sandboxes-best-practice-end


.. _datagrid-pull-data-to-amperity:

Pull data to Amperity
--------------------------------------------------

.. datagrid-pull-data-to-amperity-start

Pulling data to Amperity falls into four broad categories:

* Pull data from cloud storage
* Pull data from file transfer
* Pull data from REST API
* Pull data from warehouse

Another option for specific use cases is to use the Streaming Ingest API to pull data to Amperity.

The process of pulling data to Amperity is managed from the **Sources** page in the Amperity user interface.

.. datagrid-pull-data-to-amperity-end

.. image:: ../../images/mockup-sources-tab.png
   :width: 600 px
   :alt: The Sources page.
   :align: left
   :class: no-scaled-link

.. datagrid-pull-data-to-amperity-components-start

The **Sources** page contains the following components:

* Saved queries reshape data after pulling it to Amperity and before making it available to a feed.
* Feeds define the schema for each individual data source.
* Domain tables represent each data source after it has been processed against a feed.
* Domain transforms use existing domain tables and Spark SQL to add a custom domain table.
* Couriers define how data is pulled to Amperity, along with specifying the location from which it is pulled.
* Courier groups define schedules for pulling data to Amperity.

.. datagrid-pull-data-to-amperity-components-end


.. _datagrid-configure-and-run-stitch:

Configure and run Stitch
--------------------------------------------------

.. datagrid-configure-and-run-stitch-start

Stitch must be configured to run in a way that ensures that all data sources that contain customer records (names, email addresses, physical addresses, and other PII data) are made available to the Stitch process. The outcome of the Stitch process generates an Amperity ID for each unique customer record across all of your data.

Stitch is largely a transparent process, but there are ways to tune how it understands your data. And you can explore the results of the Stitch process against your data directly from the **Stitch** page.

.. datagrid-configure-and-run-stitch-end

.. image:: ../../images/mockup-stitch-tab.png
   :width: 600 px
   :alt: The Stitch page.
   :align: left
   :class: no-scaled-link


.. _datagrid-build-databases:

Build databases
--------------------------------------------------

.. datagrid-build-databases-start

The customer 360 database starts with the output of the Stitch process, which is a collection of database tables from which you can build *your* customer 360.

The tables that the Stitch process outputs include:

* **Transaction Attributes**
* **Unified Transactions**
* **Unified Itemized Transactions**
* **Unified Profiles**
* **Unified Scores**
* **Unified Customer**

In addition to these tables, you must build a **Merged Customers** table that defines certain rollup behaviors for profile data and, if using AmpIQ, transactions, itemized transactions, and customer profile data.

The databases and tables that may be present in the **Customer 360** page are not limited to only those output by the Stitch process. You can configure domain tables to be directly passed through to the customer 360 database and, using Spark SQL, you can build any custom database or table that you require.

All databases are managed from the **Customer 360** page.

.. datagrid-build-databases-end

.. image:: ../../images/mockup-customer360-tab.png
   :width: 600 px
   :alt: The Customer 360 page.
   :align: left
   :class: no-scaled-link

.. datagrid-build-databases-components-start

After you have build your customer 360 database and it is running against a representative collection of your data sources, you can start to look at extending the database for additional workflows and use cases, such as:

#. Blocklisting values from Stitch or from customer 360 data
#. Applying specific labels to data 
#. Adding calculations
#. Extending data to focus on address-based householding, first-party, third-party data
#. Adding CCPA or GDPR privacy rights workflows
#. Extending for customer interactions, such as order-level and item-level transactions data and product catalogs
#. Workflow-specific databases or tables to support PII consolidation or master data management (MDM) use cases
#. Adding support to enable additional Amperity features

.. datagrid-build-databases-components-end


.. _datagrid-run-queries:

Run queries
--------------------------------------------------

.. datagrid-run-queries-start

The **Queries** page uses Presto SQL to interact with any database and table that is present in the **Customer 360** database. You can use a visual SQL editor for simple queries and a SQL editor for more complex queries. Amperity supports nearly all of the functionality of Presto SQL that you would use when building a **SELECT** statement. See the Amperity Presto SQL reference for specific reference, but you may also refer to the Presto SQL documentation for anything not covered in the Amperity reference.

Use the **Queries** page to review the quality of Stitch output, the quality of transactions and itemized transactions data, and to build queries, the results of which can be sent from Amperity any downstream workflow.

.. datagrid-run-queries-end

.. image:: ../../images/mockup-queries-tab.png
   :width: 600 px
   :alt: The Queries page.
   :align: left
   :class: no-scaled-link


.. _datagrid-send-data-from-amperity:

Send data from Amperity
--------------------------------------------------

.. datagrid-send-data-from-amperity-start

Sending data from Amperity falls into similar categories:

* Send data to cloud storage
* Send data to file transfer
* Send data to REST API
* Send data to warehouse

The process of sending data from Amperity is managed from the **Destinations** page in the Amperity user interface.

.. datagrid-send-data-from-amperity-end

.. image:: ../../images/mockup-destinations-tab.png
   :width: 600 px
   :alt: The Destinations page.
   :align: left
   :class: no-scaled-link

.. datagrid-send-data-from-amperity-components-start

The **Destinations** page contains the following components:

* Destinations, which define how data is sent from Amperity and the location to which it is sent
* Data templates, which map fields in the customer 360 database to the fields that are required by the downstream workflow
* Orchestrations, which define schedules for sending data from Amperity

.. datagrid-send-data-from-amperity-components-end
