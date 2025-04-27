.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: BI Connect
.. |what-send| replace:: databases, tables, and query results
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


.. meta::
    :description lang=en:
        Configure Amperity to send data to BI Connect.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to BI Connect.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to BI Connect

==================================================
Send data to BI Connect
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-business-intelligence-connect-start
   :end-before: .. term-business-intelligence-connect-end

.. destination-business-intelligence-connect-important-start

.. important:: |bic| is licensed for presentation of Amperity-sourced data within BI tools and contexts. It is not meant to be a general data warehouse solution.

   Loading data into the |bic| data warehouse from sources other than Amperity is considered out-of-license. Customers that wish to load data to the |bic| data warehouse from other data sources should contact their Amperity account team to discuss options.

.. destination-business-intelligence-connect-important-end


.. _destination-bic-request-to-enable:

Request to enable warehouse
==================================================

.. destination-bic-request-to-enable-start

|bic| is available upon request. After the data warehouse for |bic| is configured by Amperity for your tenant, you can send data from Amperity to the data warehouse, and then connect any of your BI tools to that data.

.. destination-bic-request-to-enable-end

.. destination-bic-request-to-enable-steps-start

Open a |ext_amperity_support_ticket| to make the request to enable |bic|. In the ticket list the specific user accounts in your tenant that should be granted read-only access to the |bic| data warehouse.

.. destination-bic-request-to-enable-steps-end


.. _destination-bic-request-to-enable-provision:

Provision the warehouse
--------------------------------------------------

.. destination-bic-request-to-enable-provision-start

Your Amperity support team will provision the following:

#. A dedicated data warehouse in Snowflake that is configured to run in the same cloud platform as your tenant.

   .. list-table::
      :widths: 250 250
      :header-rows: 1

      * - Cloud platform
        - Regions
      * - **Amazon AWS**
        - **us-west-2**

          **us-east-1**

          **ca-central-1**
      * - **Microsoft Azure**
        - **east-us-2.azure**

          **west-us-2.azure**

          **north-europe.azure**

          **west-europe.azure**

#. A default database and schema within the data warehouse. These are empty by default.

#. A data staging environment within the data warehouse location.

#. A role with read-only access to the schema.

   Individual user accounts in your tenant are granted read-only access to the data warehouse using the read-only role.

#. A role with read-write access to the database and schema.

#. A service account that is granted access to the database and schema using the read-write role.

.. destination-bic-request-to-enable-provision-end


.. _destination-bic-request-to-enable-connection-details:

Connection details
--------------------------------------------------

.. destination-bic-request-to-enable-connection-details-start

Allow the Amperity support team a few days to complete the provisioning process. When finished, the support team will share the following connection details with you via SnapPass:

#. The URL for the data warehouse.
#. The **Account Name**, **Region ID**, **Database name**, **Schema name**, and **Staging path**.
#. A JDBC connection string.
#. An ODBC connection string.
#. A service account username and password, which has been granted read-only access to the data warehouse. (A dedicated read-write account is used to exchange data between Amperity and the data warehouse.)

   Use the service account to connect BI tools, such as Tableau, to the data warehouse.

   .. important:: Store the service account username and password in a safe place.

.. destination-bic-request-to-enable-connection-details-end


.. _destination-bic-request-to-enable-service-hours:

Service hours
--------------------------------------------------

.. destination-bic-request-to-enable-service-hours-start

|bic| is available to licensed Amperity tenants. This license comes with 300 free annual hours of compute service time, enough to support light-to-moderate use of BI tools.

Customers can track their utilization against their free tier hours by requesting their usage hours from their Amperity account team.

.. note:: If additional compute service time hours are needed, customers can pre-purchase additional capacity or pay on demand when usage goes outside of free tier limits.

   Discuss plans for heavy use of BI tools with your Amperity account team.

   Compute service time is calculated in minute increments and is based on the running time of the customer's data warehouse. The warehouse is started when a query is first run. As queries are submitted, the data warehouse continues to run. Five minutes after all queries have completed, the data warehouse will stop running and service hours will stop accumulating.

.. destination-bic-request-to-enable-service-hours-end


.. _destination-bic-request-to-enable-data-sharing:

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


.. _destination-bic-send-to-data-warehouse-user-access:

User access to warehouse
==================================================

.. destination-bic-send-to-data-warehouse-user-access-start

An Amperity user account is required to access the |bic| data warehouse. Two categories of user accounts are supported:

#. :ref:`Single sign-on (SSO) <destination-bic-send-to-data-warehouse-sso>` for individual user accounts
#. :ref:`Service accounts <destination-bic-send-to-data-warehouse-service-accounts>`

.. destination-bic-send-to-data-warehouse-user-access-end


.. _destination-bic-send-to-data-warehouse-sso:

Single sign-on (SSO)
--------------------------------------------------

.. destination-bic-send-to-data-warehouse-sso-start

|bic| supports using SSO to provide access to individual user accounts. Use the same credentials to access the data warehouse as those used to access Amperity.

.. destination-bic-send-to-data-warehouse-sso-end

.. destination-bic-send-to-data-warehouse-sso-note-start

.. note:: The |bic| data warehouse can only be accessed by users with Amperity credentials.

.. destination-bic-send-to-data-warehouse-sso-note-end

.. destination-bic-send-to-data-warehouse-sso-important-start

.. important:: It is recommended to use SSO to access the data warehouse. SSO accounts are automatically disabled when a user loses access to Amperity.

.. destination-bic-send-to-data-warehouse-sso-important-end


.. _destination-bic-send-to-data-warehouse-service-accounts:

Service accounts
--------------------------------------------------

.. destination-bic-send-to-data-warehouse-service-accounts-start

A service account is a static username and password that may be provisioned for use with |bic|. A service account enables non-SSO workflows during the login process, should they be necessary.

.. warning:: A service account requires explicit rotation and must be revoked during lifecycle events.

.. destination-bic-send-to-data-warehouse-service-accounts-end

.. destination-bic-send-to-data-warehouse-service-accounts-defined-start

A set of service accounts are defined for any tenant that chooses to enable |bic|. Your Amperity representative will send to you your service account username and password via SnapPass, along with the URL for your instance of |bic|. Credentials for a read-only service account and a read-write service account may be provided. You may use these service accounts to log into |bic|.

.. destination-bic-send-to-data-warehouse-service-accounts-defined-end

**To log into BI Connect using your service account**

.. destination-bic-send-to-data-warehouse-service-accounts-steps-start

#. Enter the URL for your instance of |bic| into your web browser.
#. On the login screen, enter the username and password for your service account. For example:

   .. image:: ../../images/bi-connect-login-screen.png
      :width: 340 px
      :alt: The login screen for BI Connect.
      :align: left
      :class: no-scaled-link

#. Click **Sign in**.

.. destination-bic-send-to-data-warehouse-service-accounts-steps-end


.. _destination-bic-send-to-data-warehouse:

Send data to warehouse
==================================================

.. destination-bic-send-to-data-warehouse-start

The |bic| data warehouse is empty by default. You must configure Amperity to send data to the data warehouse by using one of the following workflows:

#. :ref:`Export a database or table directly <destination-bic-send-to-data-warehouse-export>` to the |bic| data warehouse.
#. :ref:`Send the results of a query <destination-bic-send-to-data-warehouse-queries>` to the |bic| data warehouse.

   The steps are slightly different, depending on if your tenant runs on :ref:`Amazon AWS <destination-bic-send-to-data-warehouse-queries-aws>` or :ref:`Microsoft Azure <destination-bic-send-to-data-warehouse-queries-azure>`. Both approaches use a :ref:`data template <destination-bic-send-to-data-warehouse-queries-data-template>` and :ref:`orchestration <destination-bic-send-to-data-warehouse-queries-orchestration>`.

.. destination-bic-send-to-data-warehouse-end


.. _destination-bic-send-to-data-warehouse-export:

Export databases and tables
--------------------------------------------------

.. destination-snowflake-aws-database-export-start

Database tables (or even entire databases) can be sent from Amperity to Snowflake as a database export. A database export is configured from the **Customer 360** page, and then added to an orchestration from the **Destinations** page. A database export can be an ad hoc process or be scheduled as a regular drop to an external filedrop location or data warehouse.

.. destination-snowflake-aws-database-export-end

**To add a database export for Snowflake**

.. include:: ../../amperity_reference/source/data_exports.rst
   :start-after: .. data-exports-add-steps-start
   :end-before: .. data-exports-add-steps-end


.. _destination-bic-send-to-data-warehouse-queries:

Send query results
--------------------------------------------------

.. destination-bic-send-to-data-warehouse-queries-start

You can send the results of any query from the **Queries** page to the |bic| data warehouse.

.. destination-bic-send-to-data-warehouse-queries-end


.. _destination-bic-send-to-data-warehouse-queries-aws:

Send to Amazon AWS
++++++++++++++++++++++++++++++++++++++++++++++++++

.. destination-snowflake-aws-add-destination-start

The following steps describe how to configure a destination for |bic| when it is running in Amazon AWS.

.. destination-snowflake-aws-add-destination-end

**To add a destination for BI Connect**

.. TODO: The following section is specific to BI connect

.. destination-bic-send-to-data-warehouse-queries-aws-steps-start

#. From the **Destinations** page, click **Add Destination**. This opens the **Add Destination** dialog box.
#. Enter the name of the destination and a description. For example: "BI Connect" and "This sends data to the BI Connect data warehouse".
#. From the **Plugin** dropdown, select **Snowflake**.
#. From the **Credential Type** dropdown, select a credential type: "aws-snowflake".
#. From the **Credential** dropdown, select **Create a new credential**. This opens the **Create New Credential** dialog box. 
#. Enter the username and password. This is the service account username and password.
#. Add the IAM Access Key and IAM Secret Key for the IAM role with permission to access the Amazon S3 bucket.
#. Under **Snowflake Settings**, enter the Snowflake account name, Amazon AWS region ID, Snowflake stage name, and Snowflake data warehouse name.

   The **Account Name** is contained within the URL for the Snowflake instance and is a character code located before ``snowflakecomputing.com``. For example: "ab12345".

   The **Region ID** is the region ID in Amazon AWS. For example: "us-west-2".

   The **Stage** is the Snowflake stage name.

   The **Warehouse** is the name of the Snowflake data warehouse.

#. Select **Allow customers to use this data template**.
#. Select **Allow orchestrations from users with limited PII access**.
#. Click **Save**.

.. destination-bic-send-to-data-warehouse-queries-aws-steps-end


.. _destination-bic-send-to-data-warehouse-queries-azure:

Send to Microsoft Azure
++++++++++++++++++++++++++++++++++++++++++++++++++

.. destination-snowflake-aws-add-destination-start

The following steps describe how to configure a destination for |bic| when it is running in Microsoft Azure.

.. destination-snowflake-aws-add-destination-end

**To add a destination for BI Connect**

.. destination-bic-send-to-data-warehouse-queries-azure-steps-start

#. From the **Destinations** page, click **Add Destination**. This opens the **Add Destination** dialog box.
#. Enter the name of the destination and a description. For example: "Snowflake" and "This sends data to Snowflake".
#. From the **Plugin** dropdown, select **Snowflake**.
#. From the **Credential Type** dropdown, select a credential type: "azure-snowflake".
#. From the **Credential** dropdown, select **Create a new credential**. This opens the **Create New Credential** dialog box. 
#. Enter the username and password. This is the service account username and password.
#. Add the Azure Blob Storage account name and shared access signature for the AZURE_ROLE with permission to access Azure Bob Storage.
#. Under **Snowflake Settings**, enter the Snowflake account name, the region identifier, Snowflake stage name, and Snowflake data warehouse name.

   The **Account Name** is contained within the URL for the Snowflake instance and is a character code located before ``snowflakecomputing.com``. For example: "ab12345".

   The **Region ID** is the region ID in Azure. For example: "west-us-2".

   The **Stage** is the Snowflake stage name.

   The **Warehouse** is the name of the Snowflake data warehouse.

#. Select **Allow customers to use this data template**.
#. Select **Allow orchestrations from users with limited PII access**.
#. Click **Save**.

.. destination-bic-send-to-data-warehouse-queries-azure-steps-end


.. _destination-bic-send-to-data-warehouse-queries-data-template:

Add data template
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-bic-send-to-data-warehouse-queries-data-template-steps-start

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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-allow-campaigns-start
          :end-before: .. destinations-data-template-business-users-allow-campaigns-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end


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

       Select **Drop table** to overwrite the table and apply an updated schema when the upstream segment or table changes..


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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-after-start
          :end-before: .. destinations-data-template-save-after-end

.. destination-bic-send-to-data-warehouse-queries-data-template-steps-end


.. _destination-bic-send-to-data-warehouse-queries-orchestration:

Add orchestration
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-snowflake-start
   :end-before: .. sendtos-add-orchestration-snowflake-end


.. _destination-bic-send-to-data-warehouse-queries-run:

Run orchestration
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _destination-bic-connect-to-bi-tools:

Connect BI tools
==================================================

.. destination-bic-connect-to-bi-tools-start

|bic| supports all of the leading BI tools, including Tableau, Looker, Domo, Qlik, Microsoft PowerBI, Amazon QuickSight, Oracle Business Analytics, and SAP Business Objects, along with any BI tool that can connect to a data warehouse using the Open Database Connectivity (ODBC) or Java Database Connectivity (JDBC) standards.

.. destination-bic-connect-to-bi-tools-end

.. destination-bic-connect-to-bi-tools-important-start

.. important:: Please refer to the documentation for individual BI tools for troubleshooting connectivity issues with |bic| and to Snowflake documentation for troubleshooting connectivity issues related to the Snowflake ODBC or JDBC drivers.

.. destination-bic-connect-to-bi-tools-important-end


.. _destination-bic-connect-to-amazon-quicksight:

Amazon QuickSight
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-quicksight-start
   :end-before: .. term-amazon-quicksight-end

.. destination-bic-connect-to-amazon-quicksight-start

Configure Amazon QuickSight to connect to the |bic| data warehouse as a `VPC data source <https://docs.aws.amazon.com/quicksight/latest/user/vpc-connection-supported-data-sources.html>`__ |ext_link|.

.. destination-bic-connect-to-amazon-quicksight-end


.. _destination-bic-connect-to-domo:

Domo
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-domo-start
   :end-before: .. term-domo-end

.. destination-bic-connect-to-domo-start

Configure Domo to connect to the |bic| data warehouse using the `Snowflake connector <https://domohelp.domo.com/hc/en-us/articles/360042931814-Snowflake-Connector>`__ |ext_link| or the `Snowflake connector <https://domohelp.domo.com/hc/en-us/articles/360061552054-Snowflake-OAuth-Connector>`__ |ext_link|.

.. destination-bic-connect-to-domo-end


.. _destination-bic-connect-other-jdbc:

JDBC driver
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-jdbc-start
   :end-before: .. term-jdbc-end

.. destination-bic-connect-other-jdbc-start

Download the |ext_snowflake_jdbc| to connect BI tools such as Databricks, SAP Business Objects, `SQL Workbench <https://www.sql-workbench.eu/>`__ |ext_link|, or `Sisense <https://documentation.sisense.com/latest/managing-data/connectors/snowflake-online.htm>`__ |ext_link| to the |bic| data warehouse.

.. destination-bic-connect-other-jdbc-end

.. destination-bic-connect-other-jdbc-externalbrowser-start

.. important:: BI tools that use the JDBC driver must set the **Authenticator** setting to **externalbrowser** as `a requirement for browser-based SSO <https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-use.html#setting-up-browser-based-sso>`__ |ext_link|. The location in which this setting is configured varies, depending on the BI tool. For example, SQL Workbench appends this setting to the URL for the |bic| data warehouse:

   ::

      URL/?authenticator=externalbrowser

.. destination-bic-connect-other-jdbc-externalbrowser-end


.. _destination-bic-connect-other-jdbc-databricks:

Databricks
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-databricks-start
   :end-before: .. term-databricks-end

.. destination-bic-connect-other-jdbc-databricks-important-start

.. important:: Use your :ref:`SSO credentials <destination-bic-send-to-data-warehouse-sso>` to connect Databricks to |bic|.

.. destination-bic-connect-other-jdbc-databricks-important-end

**To connect Databricks to BI Connect**

.. destination-bic-connect-other-jdbc-databricks-steps-start

#. Download and install the |ext_snowflake_jdbc|.
#. Configure Databricks to |ext_databricks_from_jdbc| to |bic|.
#. Enter the following information:

   .. list-table::
      :widths: 250 250
      :header-rows: 1

      * - Setting
        - Description
      * - **Driver**
        - The Snowflake JDBC driver.
      * - **URL**
        - The URL for the |bic| data warehouse.

          This must start with ``jdbc:snowflake://``, be followed by the URL for the data warehouse, and then appended with ``?authenticator=externalbrowser``.

          For example: 

          ::

             jdbc:snowflake://ab12345.snowflakecomputing.com/?authenticator=externalbrowser

      * - **Username**
        - The string token for |bic|.
      * - **Password**
        - The personal access token for |bic|.

#. After the JDBC driver is configured to use SSO you may begin authoring and running queries from Databricks against data in the |bic| data warehouse.

.. destination-bic-connect-other-jdbc-databricks-steps-end


.. _destination-bic-connect-other-jdbc-sql-workbench:

SQL Workbench
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-sql-workbench-start
   :end-before: .. term-sql-workbench-end

**To connect SQL Workbench to BI Connect**

.. destination-bic-connect-other-jdbc-sql-workbench-steps-start

#. Download and install the |ext_snowflake_jdbc|.
#. In SQL Workbench, choose **File**, **Connect Window**, and then **Create a New Connection Profile**. This opens the **Connection Profile** pane.
#. Enter the following information:

   .. list-table::
      :widths: 250 250
      :header-rows: 1

      * - Setting
        - Description
      * - **Driver**
        - The Snowflake JDBC driver.
      * - **URL**
        - The URL for the |bic| data warehouse.

          This must start with ``jdbc:snowflake://``, be followed by the URL for the data warehouse, and then appended with ``?authenticator=externalbrowser``.

          For example: 

          ::

             jdbc:snowflake://ab12345.snowflakecomputing.com/?authenticator=externalbrowser

      * - **Username**
        - Your Amperity username. For example: ``justin.currie@acme.com``.
      * - **Password**
        - The password for your Amperity username. Leave this blank.

#. Click **OK**. Your browser will open.

   If you are already logged into Amperity, you will see a message in your browser that confirms you are authenticated to the |bic| data warehouse. Navigate back to SQL Workbench.

   If you are not logged into Amperity, you will be prompted for your username and password. Complete the login process, and then nagivate back to SQL Workbench.

#. You may begin authoring and running queries from SQL Workbench against data in the |bic| data warehouse.

.. destination-bic-connect-other-jdbc-sql-workbench-steps-end


.. _destination-bic-connect-to-looker:

Looker
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-looker-start
   :end-before: .. term-google-looker-end

.. destination-bic-connect-to-looker-start

Configure `Looker to connect directly <https://docs.looker.com/setup-and-management/connecting-to-db>`__ |ext_link| to the |bic| data warehouse.

.. destination-bic-connect-to-looker-end


.. _destination-bic-connect-to-microsoft-powerbi:

Microsoft PowerBI
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-powerbi-start
   :end-before: .. term-microsoft-powerbi-end

.. destination-bic-connect-to-microsoft-powerbi-start

Download the |ext_snowflake_odbc|, and then connect Microsoft |ext_microsoft_power_bi_desktop_to_snowflake| to the |bic| data warehouse.

.. destination-bic-connect-to-microsoft-powerbi-end


.. _destination-bic-connect-other-odbc:

ODBC driver
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-odbc-start
   :end-before: .. term-odbc-end

.. destination-bic-connect-other-odbc-start

Download the |ext_snowflake_odbc| to connect BI tools such as `Adobe Campaign <https://experienceleague.adobe.com/docs/campaign-classic/using/installing-campaign-classic/accessing-external-database/configure-fda/config-databases/configure-fda-snowflake.html?lang=en>`__ |ext_link|, Microsoft PowerBI, SAP Business Objects, Tableau, or `TIBCO Spotfire <https://docs.tibco.com/pub/sfire-analyst/11.3.0/doc/html/en-US/TIB_sfire-analyst_UsersGuide/connectors/snowflake/snowflake_accessing_data_from_snowflake.htm>`__ |ext_link| to the |bic| data warehouse.

.. destination-bic-connect-other-odbc-end

.. destination-bic-connect-other-odbc-externalbrowser-start

.. important:: BI tools that use the ODBC driver must set the **Authenticator** setting to **externalbrowser** as `a requirement for browser-based SSO <https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-use.html#setting-up-browser-based-sso>`__ |ext_link|. The location in which this setting is configured varies, depending on the BI tool. For example, Tableau configures this setting from the **Advanced** tab as part of the workflow within Tableau that configures the connection to the |bic| data warehouse.

.. destination-bic-connect-other-odbc-externalbrowser-end


.. _destination-bic-connect-to-oracle-business-analytics:

Oracle Business Analytics
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-oracle-business-analytics-start
   :end-before: .. term-oracle-business-analytics-end

.. destination-bic-connect-to-oracle-business-analytics-start

Use |ext_oracle_analytics_desktop_snowflake| to connect directly to the |bic| data warehouse.

.. destination-bic-connect-to-oracle-business-analytics-end


.. _destination-bic-connect-to-qlik:

Qlik Sense
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-qlik-sense-start
   :end-before: .. term-qlik-sense-end

.. destination-bic-connect-to-qlik-start

Configure `Qlik to connect directly <https://help.qlik.com/en-US/connectors/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Snowflake/Snowflake-connector.htm>`__ |ext_link| to the |bic| data warehouse.

.. destination-bic-connect-to-qlik-end


.. _destination-bic-connect-to-sap-business-objects:

SAP Business Objects
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-sap-business-objects-start
   :end-before: .. term-sap-business-objects-end

.. destination-bic-connect-to-sap-business-objects-start

Download the |ext_snowflake_jdbc|, and then configure `SAP Business Objects <https://blogs.sap.com/2018/11/20/how-to-set-up-sap-businessobjects-with-snowflake-using-jdbc/>`__ |ext_link| to connect to the |bic| data warehouse.

.. destination-bic-connect-to-sap-business-objects-end


.. _destination-bic-connect-to-sas:

SAS Cloud Analytic Services
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-sas-cas-start
   :end-before: .. term-sas-cas-end

.. destination-bic-connect-to-sas-start

Download the |ext_snowflake_jdbc|, and then configure `SAS Cloud Analytics Services <https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/casref/n1ldk5vubre9oen10bdqoqkfc1y7.htm>`__ |ext_link| to connect to the |bic| data warehouse.

.. destination-bic-connect-to-sas-end


.. _destination-bic-connect-to-tableau:

Tableau Desktop
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-tableau-start
   :end-before: .. term-tableau-end

.. destination-bic-connect-to-tableau-important-bridge-server-start

.. important:: You may connect Tableau Bridge or Tableau Server to |bic| using :ref:`your Amperity service account <destination-bic-send-to-data-warehouse-service-accounts>`.

.. destination-bic-connect-to-tableau-important-bridge-server-end

**To connect Tableau Desktop to BI Connect**

.. destination-bic-connect-other-odbc-tableau-steps-start

#. Download and install the |ext_snowflake_odbc|, and then `connect Tableau <https://help.tableau.com/current/pro/desktop/en-us/examples_snowflake.htm>`__ |ext_link| to the |bic| data warehouse.
#. Log in to Tableau. Select the **Connect** menu option, then **To A Server**, then **More..**, and then **Snowflake**. This opens the **Snowflake** configuration page.
#. Select the **General** tab, and then enter the following information:

   .. list-table::
      :widths: 250 250
      :header-rows: 1

      * - Setting
        - Description
      * - **Server**
        - The URL for the |bic| data warehouse.
      * - **Role**
        - The role that is assigned to this user. Leave this blank.
      * - **Authentication**
        - Set this to "Username and Password".
      * - **Username**
        - Your Amperity username. For example: ``justin.currie@acme.com``.
      * - **Password**
        - The password for your Amperity username. Leave this blank.

#. Select the **Advanced** tab, and then set **Custom Driver Parameters** to "authenticator=externalbrowser".
#. Click **Sign In**. Your browser will open.

   If you are already logged into Amperity, you will see a message in your browser that confirms you are authenticated to the |bic| data warehouse. Navigate back to Tableau.

   If you are not logged into Amperity, you will be prompted for your username and password. Complete the login process, and then nagivate back to Tableau.

#. You may begin authoring and running queries from Tableau against data in the |bic| data warehouse.

.. destination-bic-connect-other-odbc-tableau-steps-end
