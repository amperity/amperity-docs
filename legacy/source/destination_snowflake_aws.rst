.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Snowflake
.. |plugin-name| replace:: Snowflake
.. |what-send| replace:: databases, tables, and query results
.. |filter-the-list| replace:: "snow"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by |destination-name| were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


==================================================
Send data to Snowflake on Amazon AWS
==================================================

.. vale off

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_snowflake_aws.html>`__ |ext_link|.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-snowflake-start
   :end-before: .. term-snowflake-end

.. destination-snowflake-aws-stages-vs-share-start

Amperity can send data to customer-managed instances of Snowflake that are located in the same cloud platform as Amperity in the following ways:

#. To stages that are configured in the customer-managed instance
#. Sharing directly between an Amperity-managed and a customer-managed instances

.. destination-snowflake-aws-stages-vs-share-end

.. destination-snowflake-aws-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-snowflake-aws-get-details>`
#. :ref:`Configure Snowflake objects <destination-snowflake-aws-configure-objects>`
#. :ref:`Configure Snowflake storage integration <destination-snowflake-aws-configure-storage-integration>`
#. :ref:`Configure Snowflake tables <destination-snowflake-aws-configure-tables>`
#. :ref:`Define a database export <destination-snowflake-aws-database-export>`
#. :ref:`Add an Amazon S3 destination <destination-snowflake-aws-add-destination>`
#. :ref:`Add data template <destination-snowflake-aws-add-data-template>`

.. destination-snowflake-aws-steps-to-send-end


.. _destination-snowflake-aws-get-details:

Get details
==================================================

.. destination-snowflake-aws-get-details-start

|destination-name| requires the following configuration details:

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
     - The stage name, along with credentials that allow Amperity to send data to a customer-managed Amazon S3 bucket, which is the :ref:`storage location <destination-snowflake-aws-configure-storage-integration>` to which Amperity stages data and from which Snowflake pulls data.

       Use `secrets and keys <https://docs.snowflake.com/en/user-guide/data-load-s3-config-aws-iam-user>`__ |ext_link| to send table output to the customer-managed Amazon S3 bucket.

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
     - A list of table names in the Snowflake database to be sent from Amperity.

.. destination-snowflake-aws-get-details-end


.. _destination-snowflake-aws-get-details-data-sharing:

Snowflake secure data sharing
--------------------------------------------------

.. destination-bic-request-to-enable-data-sharing-start

Snowflake `secure data sharing <https://docs.snowflake.com/en/user-guide/data-sharing-intro.html>`__ |ext_link| is not enabled by default. If your organization wants to use secure data sharing, your instance of Snowflake must be in the same region as the Amperity instance.

.. destination-bic-request-to-enable-data-sharing-end


.. _destination-snowflake-aws-configure-objects:

Configure objects
==================================================

.. destination-snowflake-aws-configure-objects-start

Amperity requires access to the customer's instance of Snowflake. This requires write permissions to a `warehouse object in Snowflake <https://docs.snowflake.net/manuals/user-guide/warehouses-overview.htm>`__ |ext_link| via a role and a user.

The following objects must be created in the customer's instance of Snowflake:

#. A role via `CREATE ROLE <https://docs.snowflake.net/manuals/sql-reference/sql/create-role.html>`__ |ext_link|.

   The role must be granted permission to the warehouse via `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__ |ext_link|. 

#. An external stage via `CREATE STAGE <https://docs.snowflake.com/en/sql-reference/sql/create-stage.html>`__ |ext_link|.

   .. note:: The external stage is used by the Amperity destination to stage data that is sent from Amperity in the Amazon S3 bucket. Snowflake picks data up from this location.

   The **CREATE STAGE** command defaults to CSV file types.

   When sending data from Amperity to Snowflake you must configure an external stage that points to the URL of the Amazon S3 bucket that is included with Amperity. (``URL = 's3://bucket[/path/]'``)

#. A warehouse via `CREATE WAREHOUSE <https://docs.snowflake.net/manuals/sql-reference/sql/create-warehouse.html>`__ |ext_link|.
#. A user via `CREATE USER <https://docs.snowflake.net/manuals/sql-reference/sql/create-user.html>`__ |ext_link|.

   The user must be added to the role via `GRANT ROLE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-role.html>`__ |ext_link|.

.. destination-snowflake-aws-configure-objects-end

**To configure Snowflake objects**

To configure Snowflake objects use a Data Definition Language (DDL) command similar to:

.. destination-snowflake-aws-configure-objects-steps-start

.. code-block:: sql

   CREATE ROLE AMPERITY;

   CREATE DATABASE AMPERITY_DATABASE;

   CREATE SCHEMA AMPERITY_SCHEMA.CUSTOMER_360;

   CREATE STAGE AMPERITY_SCHEMA.CUSTOMER_360.AMPERITY_STAGE;

   CREATE WAREHOUSE AMPERITY_WAREHOUSE WITH
     WAREHOUSE_SIZE = 'XSMALL'
     WAREHOUSE_TYPE = 'STANDARD'
     AUTO_SUSPEND = 600
     AUTO_RESUME = TRUE
     MIN_CLUSTER_COUNT = 1
     MAX_CLUSTER_COUNT = 2
     SCALING_POLICY = 'ECONOMY';

   GRANT USAGE ON STAGE AMPERITY_STAGE TO ROLE AMPERITY;

   GRANT USAGE ON WAREHOUSE AMPERITY_WAREHOUSE TO ROLE AMPERITY;

   CREATE USER amperity
     PASSWORD = '********************'
     DEFAULT_WAREHOUSE = AMPERITY_WAREHOUSE
     DEFAULT_ROLE = AMPERITY;

   GRANT ROLE AMPERITY TO USER amperity;

.. destination-snowflake-aws-configure-objects-steps-end 

.. destination-snowflake-aws-configure-objects-note-start

.. note:: You must send a customer who connects directly to the Snowflake data warehouse the following information using a SnapPass link:

   #. The URL of the Snowflake data warehouse.
   #. The Snowflake username.
   #. The password for that username.
   #. Snowflake data warehouse name.

.. destination-snowflake-aws-configure-objects-note-end


.. _destination-snowflake-aws-configure-user-access:

Configure user access
==================================================

.. destination-snowflake-aws-configure-user-access-start

Users that connects to Snowflake to use data in external applications, such as from Tableau, from Microsoft Power BI, and from Databricks, need to be granted read-only access to the Snowflake data warehouse.

.. destination-snowflake-aws-configure-user-access-end

**To configure user access to a Snowflake data warehouse**

.. destination-snowflake-aws-configure-user-access-steps-start

.. code-block:: sql

   CREATE ROLE USER_READ;

   GRANT SELECT ON ALL TABLES IN SCHEMA AMPERITY_DATABASE.CUSTOMER_360 TO ROLE USER_READ;
   GRANT SELECT ON FUTURE TABLES IN SCHEMA AMPERITY_DATABASE.CUSTOMER_360 TO ROLE USER_READ;
   GRANT USAGE ON WAREHOUSE AMPERITY_WAREHOUSE ROLE USER_READ;
   GRANT USAGE ON DATABASE AMPERITY_DATABASE TO ROLE USER_READ;
   GRANT USAGE ON SCHEMA AMPERITY_DATABASE.CUSTOMER_360 TO ROLE USER_READ;

   CREATE USER USERNAME
     PASSWORD = 'PASSWORD'
     DEFAULT_WAREHOUSE = AMPERITY_WAREHOUSE
     DEFAULT_ROLE = USER_READ
     FIRST_NAME = 'USER_FIRST_NAME'
     LAST_NAME = 'USER_LAST_NAME'
     EMAIL = 'USER_EMAIL_ADDRESS';

   GRANT ROLE USER_READ TO USER USERNAME

.. destination-snowflake-aws-configure-user-access-steps-end


.. _destination-snowflake-aws-configure-storage-integration:

Configure storage integration
==================================================

.. destination-snowflake-aws-configure-storage-integration-start

Amperity can send database table data to Snowflake. This output is written by Amperity to a customer-managed Amazon S3 bucket, from which Snowflake pulls the data.

Use `secrets and keys <https://docs.snowflake.com/en/user-guide/data-load-s3-config-aws-iam-user>`__ |ext_link| to send table output to the customer-managed Amazon S3 bucket.

.. note:: You may need to mock the IAM role for the external ID and IAM user name. After the `named stage <https://docs.snowflake.net/manuals/user-guide/data-unload-s3.html>`__ |ext_link| is created in Snowflake, update the IAM role for the external ID and IAM user name.

   The IAM role is unique to the Snowflake account. The external ID is unique to the Snowflake stage.

For each database and schema to be output to the Amazon S3 bucket, specify a database and schema via `USE <https://docs.snowflake.net/manuals/sql-reference/sql/use.html>`__ |ext_link|, create a stage via `CREATE <https://docs.snowflake.net/manuals/sql-reference/sql/create>`__ |ext_link|, and then `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__ |ext_link|.

.. destination-snowflake-aws-configure-storage-integration-end

**To configure Snowflake storage integration**

To configure Snowflake storage integration use a Data Definition Language (DDL) command similar to:

.. destination-snowflake-aws-configure-storage-integration-steps-start

.. code-block:: sql

   USE DATABASE <database-name>
   USE SCHEMA <schema-name>
   CREATE STAGE <stage-name>
     URL = 's3://<bucket>/<tenant-specific-path>/'
     CREDENTIALS = (AWS_ROLE = 'AMPERITY')
     ENCRYPTION = (TYPE = 'AWS_SSE_S3');
   GRANT USAGE ON STAGE <stage-name> TO ROLE AMPERITY;
   DESC STAGE <stage-name>;

.. destination-snowflake-aws-configure-storage-integration-steps-end


.. _destination-snowflake-aws-configure-tables:

Configure tables
==================================================

.. destination-snowflake-aws-configure-tables-start

For each table to be sent from Amperity, the Amperity role in Snowflake must be given permission. This requires permissions on both the database and the schema that contain the table. Usage rights to the database and schema do not grant access to the entire database or schema. Additional table-specific grants are required via a combination of `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__ |ext_link|, `USE <https://docs.snowflake.net/manuals/sql-reference/sql/use.html>`__ |ext_link|, and `GRANT SELECT <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege-share.html>`__ |ext_link|. 

.. destination-snowflake-aws-configure-tables-end

**To configure Snowflake tables**

To configure Snowflake tables use a Data Definition Language (DDL) command similar to:

.. destination-snowflake-aws-configure-tables-steps-start

.. code-block:: sql

   GRANT USAGE ON DATABASE <database-name> TO ROLE AMPERITY;
   USE DATABASE <database-name>
   GRANT USAGE ON SCHEMA <schema-name> TO ROLE AMPERITY;
   USE SCHEMA <schema-name>;
   GRANT SELECT ON TABLE <table-name> TO ROLE AMPERITY;

.. destination-snowflake-aws-configure-tables-steps-end


.. _destination-snowflake-aws-database-export:

Define a database export
==================================================

.. destination-snowflake-aws-database-export-start

Database tables (or even entire databases) can be sent from Amperity to Snowflake as a database export. A database export is configured from the **Customer 360** page, and then added to an orchestration from the **Destinations** page. A database export can be an ad hoc process or be scheduled as a regular drop to an external filedrop location or data warehouse.

.. destination-snowflake-aws-database-export-end


.. _destination-snowflake-aws-add-destination:

Add a Snowflake destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a Snowflake destination**

.. destination-snowflake-aws-add-destination-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-name-and-description-start
          :end-before: .. destinations-add-name-and-description-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-01-select.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       The username and password should be the Amperity username and password created in Snowflake for the :ref:`user security object <destination-snowflake-aws-configure-storage-integration>`.

       Add the IAM Access Key and IAM Secret Key for the IAM role with permission to access the Amazon S3 bucket used for :ref:`Snowflake stages <destination-snowflake-aws-configure-tables>`.

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings.png
          :width: 500 px
          :alt: Settings for Snowflake (AWS).
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Account Name**
            - The account name is contained within the URL of the Snowflake instance and is a character code located before ``snowflakecomputing.com``. For example: "ab12345".

          * - **Region ID**
            - The region ID in Amazon AWS. For example: "us-west-2".

          * - **Stage**
            - The Snowflake stage name, which is created by the :ref:`CREATE STAGE <destination-snowflake-aws-configure-objects>` command. For example: ``AMPERITY_ABCDEF.CUSTOMER_360.AMP_PROD_STAGE``.

          * - **Warehouse**
            - The name of the Snowflake data warehouse. This is created by the :ref:`CREATE WAREHOUSE <destination-snowflake-aws-configure-objects>` command. For example: ``AMPERITY_WH``.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-snowflake-aws-add-destination-steps-end


.. _destination-snowflake-aws-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-snowflake-aws-add-data-template-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-start
          :end-before: .. destinations-data-template-open-template-end

       .. image:: ../../images/mockup-data-template-tab-add-01-details.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-name-start
          :end-before: .. destinations-data-template-open-template-name-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       .. image:: ../../images/mockup-data-template-tab-add-03-settings.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-note-start
          :end-before: .. destinations-data-template-verify-config-settings-note-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Under **Template Settings**, specify the **Snowflake Location**. This is a period-delimited list of the Snowflake database name, the Snowflake schema name, and the Snowflake table name:

       ::

          SNOWFLAKE_DATABASE_NAME.SNOWFLAKE_SCHEMA.TABLE_NAME

       .. note:: Be sure that the table name is appended.

       For example:

       ::

          AMPERITY.CUSTOMER_360.TABLE_NAME

       Specify the option to use for managing the table in Snowflake: create, drop, or truncate.

       .. list-table::
          :widths: 200 400
          :header-rows: 1

          * - Option
            - Description
          * - **Create table**
            - Use the **Create table** option when the table should be created in Snowflake if it is not already there.

              .. caution:: Only use this option when Snowflake is not managed by |bic| and when user roles in Snowflake have permissions set on a per-table basis.
          * - **Drop table**
            - Use the **Drop table** option to overwrite the table and apply an updated schema when the upstream segment or table changes.

              .. important:: Always use this option when Snowflake is managed by |bic| or when user roles in Snowflake have permission to access all tables in the database.
          * - **Truncate table**
            - Use the **Truncate table** option when the contents of the table should be emptied prior to loading data.

              .. caution:: Only use this option when Snowflake is not managed by |bic| and when user roles in Snowflake have permissions set on a per-table basis..


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-start
          :end-before: .. destinations-data-template-save-end

       .. image:: ../../images/mockup-destinations-tab-add-05-save.png
          :width: 500 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

.. destination-snowflake-aws-add-data-template-steps-end
