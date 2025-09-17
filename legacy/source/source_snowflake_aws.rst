.. https://docs.amperity.com/legacy/


.. |source-name| replace:: Snowflake
.. |plugin-name| replace:: Snowflake
.. |feed-name| replace:: Tablename
.. |example-filename| replace:: tablename.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: databases and tables
.. |credential-type| replace:: **aws-snowflake**


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Snowflake running on Amazon AWS.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Snowflake running on Amazon AWS.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Snowflake on Amazon AWS

==================================================
Pull from Snowflake on Amazon AWS
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-snowflake-start
   :end-before: .. term-snowflake-end

.. snowflake-send-from-warehouse-start

Snowflake can provide data to Amperity in the following ways:

#. Stages configured in Snowflake
#. Sharing directly with Amperity

.. snowflake-send-from-warehouse-end

.. source-snowflake-aws-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-snowflake-aws-get-details>`
#. :ref:`Configure Snowflake objects <source-snowflake-aws-configure-objects>`
#. :ref:`Configure Snowflake storage integration <source-snowflake-aws-configure-storage-integration>`
#. :ref:`Configure Snowflake tables <source-snowflake-aws-configure-tables>`
#. :ref:`Get sample CSV files <source-snowflake-aws-get-sample-csv-file>`
#. :ref:`Add feed <source-snowflake-aws-add-feed>`
#. Add courier using :ref:`table objects <source-snowflake-aws-add-courier-tables>` or using :ref:`Snowflake query syntax <source-snowflake-aws-add-courier-query>`
#. :ref:`Run courier <source-snowflake-aws-run-courier-manually>`
#. :ref:`Add to courier group <source-snowflake-aws-add-to-courier-group>`

.. source-snowflake-aws-steps-to-pull-end


.. _source-snowflake-aws-get-details:

Get details
==================================================

.. source-snowflake-aws-get-details-start

|source-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The username and password.

       .. tip:: Most users are configured with an initial password that must be changed. Create the user, manually change the password, and then use the updated password to configure this data source.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - The stage name, along with credentials that allow Amperity to pull data from a customer-managed Amazon S3 bucket, which is the :ref:`storage location <source-snowflake-aws-configure-storage-integration>` to which Snowflake stages data and from which Amperity pulls data.

       Use `secrets and keys <https://docs.snowflake.com/en/user-guide/data-load-s3-config-aws-iam-user>`__ |ext_link| to pull Snowflake table output from the customer-managed Amazon S3 bucket.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - The Snowflake account name.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail four.
          :align: left
          :class: no-scaled-link
     - The region in which Snowflake is located.

       .. note:: The Amperity instance of Snowflake should be located in the same region as the customer's instance of Snowflake.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail five.
          :align: left
          :class: no-scaled-link
     - A list of table names in the Snowflake database to be pulled to Amperity.

       .. tip:: :ref:`Download each table from Snowflake <source-snowflake-aws-get-sample-csv-file>` as a CSV file with UTF-8 encoding, and then use it as a sample file during feed creation.

.. source-snowflake-aws-get-details-end


.. _source-snowflake-aws-get-details-data-sharing:

Snowflake secure data sharing
--------------------------------------------------

.. destination-bic-request-to-enable-data-sharing-start

Snowflake `secure data sharing <https://docs.snowflake.com/en/user-guide/data-sharing-intro.html>`__ |ext_link| is not enabled by default. If your organization wants to use secure data sharing, your instance of Snowflake must be in the same region as the Amperity instance.

.. destination-bic-request-to-enable-data-sharing-end

.. destination-bic-request-to-enable-data-sharing-aws-start

Amperity supports the following regions for Amazon AWS:

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - US West
     - **us-west-2**
   * - US East
     - **us-east-1**
   * - Canada
     - **ca-central-1**

.. destination-bic-request-to-enable-data-sharing-aws-end

.. destination-bic-request-to-enable-data-sharing-azure-start

Amperity supports the following regions for Microsoft Azure:

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - US West
     - **west-us-2.azure**
   * - US East
     - **east-us-2.azure**
   * - North Europe
     - **north-europe.azure**

.. destination-bic-request-to-enable-data-sharing-azure-end

.. destination-bic-request-to-enable-data-sharing-note-start

.. note:: If your region is not listed you may make a request through your Amperity representative for Amperity engineering to add support for that region.

.. destination-bic-request-to-enable-data-sharing-note-end


.. _source-snowflake-aws-configure-objects:

Configure objects
==================================================

.. source-snowflake-aws-configure-objects-start

Amperity requires access to the customer's instance of Snowflake. This requires narrow read permissions to `a warehouse object in Snowflake <https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html>`__ via a role and a user.

The following objects must be created in the customer's instance of Snowflake:

* A role via `CREATE ROLE <https://docs.snowflake.net/manuals/sql-reference/sql/create-role.html>`__
* A warehouse via `CREATE WAREHOUSE <https://docs.snowflake.net/manuals/sql-reference/sql/create-warehouse.html>`__ 
* A user via `CREATE USER <https://docs.snowflake.net/manuals/sql-reference/sql/create-user.html>`__

The role must be granted permission to the warehouse via `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__ and the user must be added to the role via `GRANT ROLE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-role.html>`__.

.. source-snowflake-aws-configure-objects-end

**To configure Snowflake objects**

To configure Snowflake objects use a Data Definition Language (DDL) command similar to:

.. source-snowflake-aws-configure-objects-steps-start

.. code-block:: sql

   CREATE ROLE AMPERITY;
   
   CREATE WAREHOUSE AMPERITY_WH WITH
     WAREHOUSE_SIZE = 'XSMALL'
     WAREHOUSE_TYPE = 'STANDARD'
     AUTO_SUSPEND = 600
     AUTO_RESUME = TRUE
     MIN_CLUSTER_COUNT = 1
     MAX_CLUSTER_COUNT = 2
     SCALING_POLICY = 'ECONOMY';

   GRANT USAGE ON WAREHOUSE AMPERITY_WH TO ROLE AMPERITY;

   CREATE USER amperity
     PASSWORD = '********************'
     DEFAULT_WAREHOUSE = AMPERITY_WH
     DEFAULT_ROLE = AMPERITY;

   GRANT ROLE AMPERITY TO USER amperity;

.. source-snowflake-aws-configure-objects-steps-end


.. _source-snowflake-aws-configure-storage-integration:

Configure storage integration
==================================================

.. source-snowflake-aws-configure-storage-integration-start

Amperity can ingest any type of data structure or data format that can be output from Snowflake. This output is written by Snowflake to a customer-managed Amazon S3 bucket, from which Amperity pulls the data.

Use `secrets and keys <https://docs.snowflake.com/en/user-guide/data-load-s3-config-aws-iam-user>`__ |ext_link| to pull Snowflake table output from the customer-managed Amazon S3 bucket.

.. note:: You may need to mock the IAM role for the external ID and IAM user name. After the `named stage is created <https://docs.snowflake.net/manuals/user-guide/data-unload-s3.html>`__ in Snowflake, update the IAM role for the external ID and IAM user name.

   The IAM role is unique to the Snowflake account. The external ID is unique to the Snowflake stage.

For each database and schema to be output to the Amazon S3 bucket, specify a database and schema via `USE <https://docs.snowflake.net/manuals/sql-reference/sql/use.html>`__ |ext_link|, create a stage via `CREATE <https://docs.snowflake.net/manuals/sql-reference/sql/create>`__ |ext_link|, and then `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__ |ext_link|.

.. source-snowflake-aws-configure-storage-integration-end

**To configure Snowflake storage integration**

To configure Snowflake storage integration use a Data Definition Language (DDL) command similar to:

.. source-snowflake-aws-configure-storage-integration-steps-start

.. code-block:: sql

   USE DATABASE <database-name>;
   USE SCHEMA <schema-name>;
   CREATE STAGE <stage-name>
     URL = 's3://<bucket>/<tenant-specific-path>/'
     CREDENTIALS = (AWS_ROLE = 'AMPERITY')
     ENCRYPTION = (TYPE = 'AWS_SSE_S3');
   GRANT USAGE ON STAGE <stage-name> TO ROLE AMPERITY;
   DESC STAGE <stage-name>;

.. source-snowflake-aws-configure-storage-integration-steps-end


.. _source-snowflake-aws-configure-tables:

Configure tables
==================================================

.. source-snowflake-aws-configure-tables-start

For each table to be sent to Amperity, the Amperity role in Snowflake must be given permission. This requires permissions on both the database and the schema that contain the table. Usage rights to the database and schema do not grant access to the entire database or schema. Additional table-specific grants are required via a combination of `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__, `USE <https://docs.snowflake.net/manuals/sql-reference/sql/use.html>`__, and `GRANT SELECT <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege-share.html>`__. 

.. source-snowflake-aws-configure-tables-end

**To configure Snowflake tables**

To configure Snowflake tables use a Data Definition Language (DDL) command similar to:

.. source-snowflake-aws-configure-tables-steps-start

.. code-block:: sql

   GRANT USAGE ON DATABASE <database-name> TO ROLE AMPERITY;
   USE DATABASE <database-name>;
   GRANT USAGE ON SCHEMA <schema-name> TO ROLE AMPERITY;
   USE SCHEMA <schema-name>;
   GRANT SELECT ON TABLE <table-name> TO ROLE AMPERITY;

.. source-snowflake-aws-configure-tables-steps-end


.. _source-snowflake-aws-get-sample-csv-file:

Get sample CSV file
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-snowflake-start
   :end-before: .. sources-get-sample-files-snowflake-end

**Get a sample CSV file from Snowflake**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-snowflake-start
   :end-before: .. sources-get-sample-files-steps-snowflake-end


.. _source-snowflake-aws-add-feed:

Add feed
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-note-snowflake-start
   :end-before: .. sources-add-feed-note-snowflake-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-snowflake-start
   :end-before: .. sources-add-feed-steps-snowflake-end


.. _source-snowflake-aws-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. source-snowflake-aws-add-courier-start

.. important:: Consolidate all Snowflake feeds to a single courier as a fileset.

.. source-snowflake-aws-add-courier-end

.. source-snowflake-aws-add-courier-options-start

You have two options for how to pull data from Snowflake:

* :ref:`Pull Snowflake table objects <source-snowflake-aws-add-courier-tables>`
* :ref:`Pull specific columns from a table object using Snowflake query syntax <source-snowflake-aws-add-courier-query>`

.. source-snowflake-aws-add-courier-options-end


.. _source-snowflake-aws-add-courier-tables:

Pull table objects
--------------------------------------------------

.. source-snowflake-aws-add-courier-start

You can pull entire tables from |source-name| to Amperity.

.. source-snowflake-aws-add-courier-end

**To pull Snowflake table objects**

.. source-snowflake-aws-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the username and password. This should be the Amperity username and password created in Snowflake for the :ref:`user security object <source-snowflake-aws-configure-storage-integration>`.
#. Add the IAM Access Key and IAM Secret Key for the IAM role with permission to access the Amazon S3 bucket used for :ref:`Snowflake stages <source-snowflake-aws-configure-storage-integration>`. Add the Amazon Resource Name (ARN) if the IAM role is provisioned for cross-account access.
#. Add Snowflake settings for the account name, the region identifier, and a square-bracketed list of :ref:`Snowflake tables <source-snowflake-aws-configure-tables>` to be sent to Amperity:

   ::

      [
        "table.name.one",
        "table.name.two"
        "table.name.etc"
      ]

#. Enter :ref:`the name of the Snowflake stage <source-snowflake-aws-configure-storage-integration>`.
#. For each table to be sent to Amperity, define the load operations using the feed ID for the feed that is associated with that table.
#. Click **Save**.

.. source-snowflake-aws-add-courier-steps-end


.. _source-snowflake-aws-add-courier-query:

Pull columns using Snowflake query syntax
--------------------------------------------------

.. source-snowflake-aws-add-courier-query-start

You can use `Snowflake query syntax <https://docs.snowflake.com/en/sql-reference/constructs.html>`__ |ext_link| to build a query that runs against one or more Snowflake tables.

.. important:: A Snowflake query name must be unique. The name may contain alphanumeric characters (A-Z, a-z), underscores, hyphens, and/or periods. For example: "Query_name.12-345a".

.. source-snowflake-aws-add-courier-query-end

**To pull columns using Snowflake query syntax**

.. source-snowflake-aws-add-courier-query-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the username and password. This should be the Amperity username and password created in Snowflake for the :ref:`user security object <source-snowflake-aws-configure-storage-integration>`.
#. Add the IAM Access Key and IAM Secret Key for the IAM role with permission to access the Amazon S3 bucket used for :ref:`Snowflake stages <source-snowflake-aws-configure-storage-integration>`. Add the Amazon Resource Name (ARN) if the IAM role is provisioned for cross-account access.
#. Add Snowflake settings for the account name, the region identifier, and a square-bracketed list of :ref:`one or more Snowflake tables against which a query that uses Snowflake query syntax is run <source-snowflake-aws-configure-tables>` to be sent to Amperity:

   ::

      [
        "table.name.one",
        "table.name.two",
        "table.name.etc"
      ]

   .. caution:: The courier downloads both query results **AND** all listed tables.

#. Enter :ref:`the name of the Snowflake stage <source-snowflake-aws-configure-storage-integration>`.
#. Click "Add Snowflake query". In the expanded box, provide a unique query name. A query name may contain alphanumeric characters (A-Z, a-z), underscores, hyphens, and/or periods. For example: "Query_name.12-345a".

   .. caution:: You must add a blank line to the end of the |source-name| query.

   Use `Snowflake query syntax <https://docs.snowflake.com/en/sql-reference/constructs.html>`__ |ext_link| to build a query to run against a table that is to be pulled to Amperity.

   .. important:: The name of the query must be added to the **file** parameter within the load operations. For example:

      ::

         "FEED_ID": [
           {
             "type": "load",
             "file": "Query_name.12-345a"
           }

#. For each table to be sent to Amperity, define the load operations using the feed ID for the feed that is associated with that table.
#. Click **Save**.

.. source-snowflake-aws-add-courier-query-steps-end


.. _source-snowflake-aws-run-courier-manually:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-snowflake-aws-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

.. source-snowflake-aws-add-to-courier-group-start

After the Snowflake courier is configured correctly and you have verified that all tables are being collected successfully, you can add the courier to a courier group and automate it.

.. source-snowflake-aws-add-to-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
