.. https://docs.amperity.com/internal/



.. |destination-name| replace:: Snowflake (Azure)
.. |plugin-name| replace:: "Snowflake"
.. |credential-type| replace:: "snowflake"
.. |required-credentials| replace:: "username", "password", "account name", and "shared access signature"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "snow"


.. meta::
    :description lang=en:
        Configure Amperity to send data to Snowflake.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Snowflake.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Snowflake (Azure)

==================================================
Send data to Snowflake (Azure)
==================================================

.. note:: This topic contains information for configuring a destination for sending query results to |destination-name| using orchestrations. To configure a destination for sending audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_snowflake_azure.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-snowflake-start
   :end-before: .. term-snowflake-end

.. destination-snowflake-azure-stages-vs-share-start

Amperity can send data to customer-managed instances of Snowflake that are located in the same cloud platform as Amperity in the following ways:

#. To stages that are configured in the customer-managed instance
#. Sharing directly between an Amperity-managed and a customer-managed instances

.. destination-snowflake-azure-stages-vs-share-end


.. _destination-snowflake-azure-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-snowflake-azure-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **Username**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-username-start
             :end-before: .. credential-snowflake-username-end

       **Password**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-password-start
             :end-before: .. credential-snowflake-password-end

       **Account name**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-account-name-start
             :end-before: .. credential-snowflake-account-name-end

          .. important:: This role must be granted :ref:`write permission to Snowflake objects <destination-snowflake-azure-configure-objects>`, :ref:`permission to access each table <destination-snowflake-azure-configure-tables>`, and permission to :ref:`write table output to Azure Blob Storage <destination-snowflake-azure-configure-storage-integration>`.

       **Shared access signature**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-shared-access-signature-start
             :end-before: .. credential-snowflake-shared-access-signature-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Account name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-account-name-start
             :end-before: .. setting-snowflake-account-name-end

       **Region ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-region-id-start
             :end-before: .. setting-snowflake-region-id-end

       **Stage**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-stage-start
             :end-before: .. setting-snowflake-stage-end

       **Warehouse**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-warehouse-start
             :end-before: .. setting-snowflake-warehouse-end

       **Snowflake location**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-location-start
             :end-before: .. setting-snowflake-location-end

       **Create table?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-create-table-start
             :end-before: .. setting-snowflake-create-table-end

       **Truncate table?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-truncate-table-start
             :end-before: .. setting-snowflake-truncate-table-end

       **Drop table?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-drop-table-start
             :end-before: .. setting-snowflake-drop-table-end

.. destination-snowflake-azure-get-details-end


.. _destination-snowflake-azure-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Snowflake (Azure)**

.. destination-snowflake-azure-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Username**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-username-start
             :end-before: .. credential-snowflake-username-end

       **Password**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-password-start
             :end-before: .. credential-snowflake-password-end

       **Account name**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-account-name-start
             :end-before: .. credential-snowflake-account-name-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-account-name-required-permissions-start
             :end-before: .. credential-snowflake-account-name-required-permissions-end

       **Shared access signature**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-snowflake-shared-access-signature-start
             :end-before: .. credential-snowflake-shared-access-signature-end

.. destination-snowflake-azure-credentials-steps-end


.. _destination-snowflake-azure-get-details-data-sharing:

Snowflake secure data sharing
--------------------------------------------------

.. destination-snowflake-azure-get-details-data-sharing-start

Snowflake `secure data sharing <https://docs.snowflake.com/en/user-guide/data-sharing-intro.html>`__ |ext_link| is not enabled by default. If your organization wants to use secure data sharing, your instance of Snowflake must be in the same region as the Amperity instance and you must provide your Snowflake `account identifier <https://docs.snowflake.com/en/user-guide/admin-account-identifier.html>`__ |ext_link| to Amperity.

.. TODO: This is important and shared elsewhere so it's gotta be moved from the business intelligence connect topic to maybe here. Must be in a single location:

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

.. note:: If your region is not listed you may make a request through your Amperity representative for Amperity engineering to add support for that region.

.. destination-snowflake-azure-get-details-data-sharing-end


.. _destination-snowflake-azure-configure-objects:

Configure objects
==================================================

.. destination-snowflake-azure-configure-objects-start

Amperity requires access to the customer's instance of Snowflake. This requires write permissions to a `warehouse object in Snowflake <https://docs.snowflake.net/manuals/user-guide/warehouses-overview.htm>`__ |ext_link| via a role and a user.

The following objects must be created in the customer's instance of Snowflake:

#. A role via `CREATE ROLE <https://docs.snowflake.net/manuals/sql-reference/sql/create-role.html>`__ |ext_link|.

   The role must be granted permission to the warehouse via `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__ |ext_link|. 

#. A stage via `CREATE STAGE <https://docs.snowflake.com/en/sql-reference/sql/create-stage.html>`__ |ext_link|.

   .. note:: The external stage is used by the Amperity destination to stage data that is sent from Amperity in the Azure container. Snowflake picks data up from this location.

   The **CREATE STAGE** command defaults to CSV file types.

   When sending data from Amperity to Snowflake you must configure an external stage that points to the URL for the Azure container that is included with Amperity.  (``URL = 'azure://account.blob.core.windows.net/container[/path/]'``).

#. A warehouse via `CREATE WAREHOUSE <https://docs.snowflake.net/manuals/sql-reference/sql/create-warehouse.html>`__ |ext_link|.
#. A user via `CREATE USER <https://docs.snowflake.net/manuals/sql-reference/sql/create-user.html>`__ |ext_link|.

   The user must be added to the role via `GRANT ROLE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-role.html>`__ |ext_link|.

.. destination-snowflake-azure-configure-objects-end

**To configure Snowflake objects**

To configure Snowflake objects use a Data Definition Language (DDL) command similar to:

.. destination-snowflake-azure-configure-objects-steps-start

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

.. destination-snowflake-azure-configure-objects-steps-end

.. destination-snowflake-azure-configure-objects-note-start

.. note:: You must send a customer who will connect directly to the Snowflake data warehouse the following information using a SnapPass link:

   #. The URL for the Snowflake data warehouse.
   #. The Snowflake username.
   #. The password for that username.
   #. Snowflake data warehouse name.

.. destination-snowflake-azure-configure-objects-note-end


.. _destination-snowflake-azure-configure-user-access:

Configure user access
==================================================

.. destination-snowflake-azure-configure-user-access-start

Users that will connect to Snowflake to use data in external applications, such as Tableau, Microsoft Power BI, and Databricks, will need to be granted read-only access to the Snowflake data warehouse. 

.. destination-snowflake-azure-configure-user-access-end

**To configure user access to a Snowflake data warehouse**

.. destination-snowflake-azure-configure-user-access-steps-start

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

.. destination-snowflake-azure-configure-user-access-steps-end


.. _destination-snowflake-azure-configure-storage-integration:

Configure storage integration
==================================================

.. destination-snowflake-azure-configure-storage-integration-start

Amperity can send database table data to Snowflake. This output should be written to Azure Blob Storage via a storage integration configured in Snowflake. This requires the Azure tenant ID and the full path to each allowed storage location.

For each database and schema to be output to the Amazon S3 bucket, specify a database and schema via `USE <https://docs.snowflake.net/manuals/sql-reference/sql/use.html>`__ |ext_link|, create a stage via `CREATE <https://docs.snowflake.net/manuals/sql-reference/sql/create>`__ |ext_link|, and then `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__ |ext_link|.

.. destination-snowflake-azure-configure-storage-integration-end

**To configure Snowflake storage integration**

To configure Snowflake storage integration use a Data Definition Language (DDL) command similar to:

.. destination-snowflake-azure-configure-storage-integration-steps-start

.. code-block:: sql

   USE DATABASE <database-name>
   USE SCHEMA <schema-name>
   CREATE STORAGE INTEGRATION <storage-integration-name>
     TYPE = EXTERNAL_STAGE
     STORAGE_PROVIDER = AZURE
     ENABLED = TRUE
     AZURE_TENANT_ID = '<tenant-id>'
     STORAGE_ALLOWED_LOCATIONS = ('PATH', 'PATH', 'PATH')
   GRANT USAGE ON STAGE <storage-integration-name> TO ROLE AMPERITY;
   DESC STAGE <stage-name>;

.. destination-snowflake-azure-configure-storage-integration-steps-end

where each PATH is similar to ``azure://<account>.blob.core.windows.net/<container>/<path>/``.


.. _destination-snowflake-azure-configure-tables:

Configure tables
==================================================

.. destination-snowflake-azure-configure-tables-start

For each table to be sent from Amperity, the Amperity role in Snowflake must be given permission. This requires permissions on both the database and the schema that contain the table. Usage rights to the database and schema do not grant access to the entire database or schema. Additional table-specific grants are required via a combination of `GRANT USAGE <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html>`__ |ext_link|, `USE <https://docs.snowflake.net/manuals/sql-reference/sql/use.html>`__ |ext_link|, and `GRANT SELECT <https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege-share.html>`__ |ext_link|.  

.. destination-snowflake-azure-configure-tables-end

**To configure Snowflake tables**

To configure Snowflake tables use a Data Definition Language (DDL) command similar to:

.. destination-snowflake-azure-configure-tables-steps-start

.. code-block:: sql

   GRANT USAGE ON DATABASE <database-name> TO ROLE AMPERITY;
   USE DATABASE <database-name>
   GRANT USAGE ON SCHEMA <schema-name> TO ROLE AMPERITY;
   USE SCHEMA <schema-name>;
   GRANT SELECT ON TABLE <table-name> TO ROLE AMPERITY;

.. destination-snowflake-azure-configure-tables-steps-end


.. _destination-snowflake-azure-database-export:

Define a database export
==================================================

.. destination-snowflake-azure-database-export-start

Database tables (or even entire databases) can be sent from Amperity to Snowflake as a database export. A database export is configured from the **Customer 360** page, and then added to an orchestration from the **Destinations** page. A database export can be an ad hoc process or be scheduled as a regular drop to an external filedrop location or data warehouse.

.. destination-snowflake-azure-database-export-end

.. TODO: UNCOMMENT

.. 
.. **To add a database export for Snowflake**
.. 
.. .. include:: ../../amperity_reference/source/data_exports.rst
..    :start-after: .. data-exports-add-steps-start
..    :end-before: .. data-exports-add-steps-end
.. 


.. _destination-snowflake-azure-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Snowflake (Azure)**

.. destination-snowflake-azure-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Account name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-account-name-start
             :end-before: .. setting-snowflake-account-name-end

       **Region ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-region-id-start
             :end-before: .. setting-snowflake-region-id-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-region-id-location-start
             :end-before: .. setting-snowflake-region-id-location-end

       **Stage**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-stage-start
             :end-before: .. setting-snowflake-stage-end

       **Warehouse**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-warehouse-start
             :end-before: .. setting-snowflake-warehouse-end

       **Snowflake location**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-location-start
             :end-before: .. setting-snowflake-location-end

       **Create table?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-create-table-start
             :end-before: .. setting-snowflake-create-table-end

       **Truncate table?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-truncate-table-start
             :end-before: .. setting-snowflake-truncate-table-end

       **Drop table?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snowflake-drop-table-start
             :end-before: .. setting-snowflake-drop-table-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-snowflake-azure-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
