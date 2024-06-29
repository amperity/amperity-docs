.. 
.. xxxxx
..


.. |sftp-type| replace:: ``xxxxx``
.. |sftp-hostname| replace:: ``xxxxx``


.. tip::

   .. include:: ../../amperity_configure/source/couriers.rst
      :start-after: .. couriers-run-without-load-operations-start
      :end-before: .. couriers-run-without-load-operations-end

**Example entities list**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-entities-list-intro-start
   :end-before: .. sources-add-courier-entities-list-intro-end

.. source-xxxxx-add-courier-entities-list-start

For example:

::

   [
     {
       "object/type": "file",
       "object/file-pattern": "'/path/to/customer-record.csv'",
       "object/land-as": {
         "file/header-rows": 1,
         "file/tag": "customer-record-files",
         "file/content-type": "text/csv"
       }
     }
   ]

.. source-xxxxx-add-courier-entities-list-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-entities-list-note-start
   :end-before: .. sources-add-courier-entities-list-note-end

**To add a courier**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-sftp-start
   :end-before: .. sources-add-courier-sftp-end






ADD THIS TO END OF GET DETAILS FOR ALL SOURCES AND CLEAN UP GET DETAILS


.. tip:: Use SnapPass to securely share configuration details for |source-name| between your company and your Amperity representative.




**TEMPLATE SECTIONS FOR DATA SOURCES**

This topic contains the templated sections for all of the "Pull from xxxxx" topics in /configure/. You must use these templated sections. Use the beginning of the topic to introduce anything that is source-specific. You cannot add source-specific content within the templated sections outside of providing the variables for "source name", "feed name", and "example filename". The "domain table name" is a concatenation of "source name" + "feed name".

In certain cases, a source topic will require *some* customization within the templated sections. See the Salesforce Sales Cloud topic, **Run courier manually** section for how to do this.

.. sources-overview-list-intro-start

This topic describes the steps that are required to pull |what-pull| to Amperity from |source-name|:

.. sources-overview-list-intro-end




**Get details**


FIVETRAN COURIERS
FIVETRAN COURIERS
FIVETRAN COURIERS

Fivetran couriers share some common details: 1) request to enable, 2) access to Snowflake, 3) the introduction, 4) note about Fivetran, 5) important about not storing data with 3, 4, and 5 tucked into consistent locations. The steps in-between 1) and 2) are custom to each topic.

.. sources-get-details-fivetran-overview-start

Amperity can pull data from |source-name| by using Fivetran as the interface to |source-interface|. This requires the following configuration details:

.. sources-get-details-fivetran-overview-end

.. sources-get-details-fivetran-connect-start

.. note:: Amperity connects to |source-name| using Fivetran, which is an application that must be configured for your instance of |source-name|. Fivetran connects to |source-name|, and then pulls this data directly to a Snowflake instance that is managed by Amperity. Use a Snowflake data source to pull these tables from that Snowflake instance to Amperity.

.. sources-get-details-fivetran-connect-end

.. sources-get-details-fivetran-does-not-store-data-start

.. important:: Fivetran does not store any data that is pulled to Amperity from |source-name|.

.. sources-get-details-fivetran-does-not-store-data-end

.. sources-get-details-fivetran-request-to-enable-start

A request to Amperity support to enable |source-name| as a data source for your tenant.

.. important:: Please allow for up to 24 hours after making the request for the |source-name| connection to be enabled.

.. sources-get-details-fivetran-request-to-enable-end

.. sources-get-details-fivetran-access-to-snowflake-start

Access to the instance of Snowflake that stores the |source-name| data tables that were pulled by Fivetran.

.. important:: The amount of time required to complete the initial population of data from |source-name| to Snowflake can vary, depending on the amount of data. Please allow for up 72 hours for this process to complete as a general guideline.

.. sources-get-details-fivetran-access-to-snowflake-start


FIVETRAN COURIERS
FIVETRAN COURIERS
FIVETRAN COURIERS


**Configure OAuth**

USE THIS FOR ALL SOURCES THAT ALLOW OAUTH

.. sources-oauth-configure-start

#. Select the |fa-kebab| menu next to your tenant name in the top navigation, and then select **Credentials**.
#. On the **Credentials** page, click **Add credential**. This opens the **Create New Credential** page.
#. From the **Plugin** dropdown, select |plugin-name|, and then enter a name and description for this connector.
#. Generate an authorization link, and then visit the URL that was generated to complete the authorization process.

.. sources-oauth-configure-end



**Filedrop requirements**

TODO: Consolidate the "requirements" into the Get Details sections, as much as possible.

.. sources-filedrop-requirements-start

Amperity must connect to, and then pull data from |source-name|. Configure the courier that will pull data to Amperity with credentials--username and passphrase--that have permission to read data from |source-name|.

.. sources-filedrop-requirements-end

.. sources-filedrop-requirements-use-snappass-start

.. tip:: Use SnapPass to share credentials between individuals who are responsible for configuring this courier.

.. sources-filedrop-requirements-use-snappass-end




**Add courier**



THERE ARE STEPS FOR SFTP ... maybe can consolidate for SFTP/Azure/S3/GCP
THERE ARE STEPS FOR APIs << these might be unique or at least have unique settings
THERE ARE STEPS FOR SNOWFLAKE << these are repetitive except potentially the S3 vs. Azure
THERE ARE STEPS FOR FIVETRAN? << these should be repetitive? "To add a courier for table objects" << these are Snowflakey, but should be their own pattern
THERE ARE SNOWFLAKES? << Many :(
THERE IS AN OAUTH vs. NOT-OAUTH STEPS ALSO variance with specific credentials steps, already created









SFTP COURIERS
SFTP COURIERS
SFTP COURIERS

This section applies ONLY to data sources that use SFTP.

.. sources-add-courier-entities-list-intro-sftp-only-start

An entites list defines the list of files to be pulled to Amperity, along with any file-specific details (such as file name, file type, if header rows are required, and so on).

.. sources-add-courier-entities-list-intro-sftp-only-end

.. sources-add-courier-entities-list-note-sftp-only-start

.. note:: You may configure files as required (``"object/optional": false``) or optional (``"object/optional": true``.) A courier will fail if a required file is not available or, if all files in the fileset are optional, at least one of those files is not available.

.. sources-add-courier-entities-list-note-sftp-only-end

This section has an introduction to entities lists and a note about required/optional file behaviors. In-between you show an example of an entities list that is appropriate for each SFTP data source. All data sources share the same add couriers steps. This section applies to SFTP connectors only.

.. sources-add-courier-sftp-only-start

#. From the **Sources** tab, click **Add Courier**. The **Select integration** page opens.
#. Find, and then click the row that contains |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**. Add the hostname for the location from which data is pulled. For example: |sftp-hostname|.
#. Enter the name of the courier. For example: "|source-name|".
#. From the **Credential** drop-down, select **Create a new credential**. This opens the **Create New Credential** page.
#. From the **Credential** drop-down, select **Create a new credential**. This opens the **Create New Credential** dialog box. Enter a name for the credential (typically "|source-name|"), and then enter the username and password required to access this location.
#. Under **Settings** configure the list of files to pull to Amperity. Configure the **Entities List** for each file to be loaded to Amperity.

   .. note:: If the file is contained within a ZIP archive, you may need to specify the fully qualified filename within the ZIP archive. For example, to import a file named "items.csv" you may need to specify "export\items.csv".
#. Under **Settings** set the load operations to a string that is obviously incorrect, such as ``df-xxxxxx``. (You may also set the load operation to empty: ``{}``.)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the feed is configured and activated you can edit the courier, and then update the feed ID with the correct identifier.

   .. caution:: If load operations are not set to ``{}`` the validation test for the courier configuration settings will fail.
#. Click **Save**.

.. sources-add-courier-sftp-only-end

SFTP COURIERS
SFTP COURIERS
SFTP COURIERS



FIVETRAN COURIERS
FIVETRAN COURIERS
FIVETRAN COURIERS

This section applies ONLY to data sources that use Fivetran.

.. sources-add-courier-fivetran-consolidate-start

Consolidate all tables from |source-name| to a single courier as a fileset.

.. important:: The courier itself is added by Amperity support. You must to complete the configuration to specify which |source-name| tables should be pulled from the Snowflake instance to Amperity.

.. sources-add-courier-fivetran-consolidate-end

.. sources-add-courier-fivetran-table-list-start

A table list defines the list of tables to be pulled to Amperity from Snowflake.

.. sources-add-courier-fivetran-table-list-end

.. sources-add-courier-fivetran-stage-name-start

A stage defines the location of objects that are available within Snowflake.

.. sources-add-courier-fivetran-stage-name-end

.. sources-add-courier-fivetran-load-operation-start

Load operations associate each table in the list of tables to a feed. (The initial setup for this courier will use an incorrect feed ID -- ``df-xxxxxx``.)

.. sources-add-courier-fivetran-load-operation-end

.. sources-add-courier-fivetran-start

#. From the **Sources** tab, select the courier added for |source-name|, and then click **Edit Courier**.
#. Add a name for the courier. For example: "|source-name| (Snowflake)".
#. Select the "Snowflake" plugin, and then select the credential type.
#. Enter the username and password. This should be the Amperity username and password created in Snowflake that allows Amperity to access the instance of Snowflake that stores |source-name| data tables for your tenant.
#. Complete the credentials, account name, and region ID settings.
#. Define the list of tables to pull to Amperity:

   ::

      [
        "table.name.one",
        "table.name.two"
        "table.name.etc"
      ]

#. Enter the name of the Snowflake stage.
#. Optional. Use a query to select specific columns from a Snowflake table prior to pulling those results to Amperity. Click "Add Snowflake query". In the expanded box, provide a unique query name. A query name may contain alphanumeric characters (A-Z, a-z), underscores, hyphens, and/or periods. For example: "Query_name.12-345a".

   Use |ext_snowflake_query_syntax| to build a query to run against a table that is to be pulled to Amperity.

   .. important:: The name of the query must be added to the **file** parameter within the load operations. For example:

      ::

         "FEED_ID": [
           {
             "type": "load",
             "file": "Query_name.12-345a"
           }
#. For each table to be sent to Amperity, define the load operations using the feed ID for the feed that is associated with that table.

   Set the load operations to a string that is obviously incorrect, such as ``df-xxxxxx``. (You may also set the load operation to empty: ``{}``.)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to ``{}`` or are not set to an obviously incorrect string the validation test for the courier configuration settings will fail.

#. Click **Save**.

.. sources-add-courier-fivetran-end

FIVETRAN COURIERS
FIVETRAN COURIERS
FIVETRAN COURIERS



AMAZON S3 COURIERS
AMAZON S3 COURIERS
AMAZON S3 COURIERS

This section applies ONLY to data sources that use AMAZON S3.

.. TODO: Sync the example entities list intros to be generic for all file-based couriers.

.. sources-add-courier-entities-list-intro-s3-generic-start

An entites list defines the list of files to be pulled to Amperity, along with any file-specific details (such as file name, file type, if header rows are required, and so on).

.. sources-add-courier-entities-list-intro-s3-generic-end

.. sources-add-courier-amazon-s3-cross-account-start

.. note:: Amperity supports using cross-account role assumption with Amazon S3 buckets when |source-name| supports the use of cross-account roles and your tenant uses the |source_amazon_s3| data source.

.. sources-add-courier-amazon-s3-cross-account-end

.. sources-add-courier-entities-list-note-s3-generic-start

.. note:: You may configure files as required (``"object/optional": false``) or optional (``"object/optional": true``.) A courier will fail if a required file is not available or, if all files in the fileset are optional, at least one of those files is not available.

.. sources-add-courier-entities-list-note-s3-generic-end

This section has an introduction to entities lists and a note about required/optional file behaviors. In-between you show an example of an entities list that is appropriate for each SFTP data source. All data sources share the same add couriers steps. This section applies to SFTP connectors only.

.. sources-add-courier-s3-generic-start

#. From the **Sources** tab, click **Add Courier**. The **Select integration** page opens.
#. Find, and then click the row that contains |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the name of the courier. For example: "|source-name|".
#. From the **Credential** drop-down, select **Create a new credential**. This opens the **Create New Credential** page.
#. Enter a name for the credential and add the configuration settings. Click **Save**.
#. Under **Amazon S3 Settings**, add the name of the Amazon S3 bucket and prefix.
#. Under **Amazon S3 Settings** configure the list of files to pull to Amperity. Configure the **Entities List** for each file to be loaded to Amperity.
#. Under **Amazon S3 Settings** set the load operations to a string that is obviously incorrect, such as ``df-xxxxxx``. (You may also set the load operation to empty: ``{}``.)

   .. tip:: If you use an obviously incorrect string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to ``{}`` the validation test for the courier configuration settings will fail.
#. Click **Save**.

.. sources-add-courier-s3-generic-end

AMAZON S3 COURIERS
AMAZON S3 COURIERS
AMAZON S3 COURIERS




API COURIERS THAT AUTOMATICALLY BUILD FEEDS
API COURIERS THAT AUTOMATICALLY BUILD FEEDS
API COURIERS THAT AUTOMATICALLY BUILD FEEDS

This section applies ONLY to data sources that use APIs and automatically handle the feed creation.

.. TODO: Currently hooked into Zendesk, Sailthru, and Listrak. Not hooked into Google Analytics. Requires the credential-fields, settings-details, and box-names replacements.

.. sources-add-courier-api-automatic-start

#. From the **Sources** tab, click **Add Courier**. The **Select integration** page opens.
#. Find, and then click the row that contains |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the name of the courier. For example: "|source-name|".
#. From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.
   
#. Under **Settings** enter the |settings-details|.
#. Under **Select Data**, enable |box-names|.
#. Click **Create**.

.. sources-add-courier-api-automatic-end

.. sources-add-courier-review-feed-and-domain-table-start

After running the |source-name| courier a feed is created automatically with a pre-defined list of fields. You may apply semantic tags to these fields and you may make the domain table available to Stitch, depending on your use cases. A domain table named |domain-table-name| will be added.

.. sources-add-courier-review-feed-and-domain-table-end

API COURIERS THAT AUTOMATICALLY BUILD FEEDS
API COURIERS THAT AUTOMATICALLY BUILD FEEDS
API COURIERS THAT AUTOMATICALLY BUILD FEEDS






**Get sample files**

This section has three possible introductions: one for files, another for Snowflake, and another for Fivetran. Fivetran does not have a howto.

.. sources-get-sample-files-start

Every |source-name| file that is pulled to Amperity must be configured as a feed. Before you can configure each feed you need to know the schema of that file. Run the courier without load operations to bring sample files from |source-name| to Amperity, and then use each of those files to configure a feed.

.. sources-get-sample-files-end

.. sources-get-sample-files-fivetran-start

Run the |source-name| courier to pull sample files to Amperity for each of the tables configured in the load operation. Use these sample files to configure a feed for each |source-name| table to be loaded to Amperity.

.. important:: The courier run will fail, but this process will successfully return a list of files, one for each table that was defined in the courier load operation. Use these files to define the feed schema.

.. sources-get-sample-files-fivetran-end

.. sources-get-sample-files-snowflake-start

A sample CSV file may be output from Snowflake, and then uploaded to Amperity while adding a feed.

.. sources-get-sample-files-snowflake-end

.. sources-get-sample-files-steps-start

#. From the **Sources** tab, open the menu for a courier configured for |source-name| with empty load operations, and then select **Run**. The **Run Courier** dialog box opens.
#. Select **Load data from a specific day**, and then select today's date.
#. Click **Run**.

   .. important:: The courier run will fail, but this process will successfully return a list of files from |source-name|.

   These files will be available for selection as an existing source from the **Add Feed** dialog box.
#. Wait for the notification for this courier run to return an error similar to:

   ::

      Error running load-operations task
      Cannot find required feeds: "df-xxxxxx"

.. sources-get-sample-files-steps-end

.. sources-get-sample-files-steps-snowflake-start

#. Open the Snowflake web UI.
#. Select the **Worksheets** tab.
#. From the object browser, select a table that is to be sent to Amperity.
#. In the SQL editor, run the following query:

   .. code-block:: sql

      SELECT * FROM <table-name> LIMIT 1000

#. Click the **Download Results** button.
#. In the **Export Results** dialog box, click the **Export** button.

.. sources-get-sample-files-steps-snowflake-end




**Add feeds**

This section starts with the glossary term for feeds, then has a note. There are three styles for notes: one for files, one for Fivetran, and one for Snowflake. Slighly different. Then there are two styles for steps: one for Snowflake and another for everything else.

.. sources-add-feed-note-file-start

.. note:: A feed must be added for *each* file that is pulled from |source-name|, including all files that contain customer records and interaction records, along with any other files that will be used to support downstream workflows.

.. sources-add-feed-note-file-end

.. 
.. For Hubspot, Klaviyo, Shopify, Zendesk, and all other Fivetran-based sources.
.. 

.. sources-add-feed-note-fivetran-start

.. note:: A feed must be added for *each* table that is pulled from |source-name|, including all tables that contain customer records and interaction records, along with any other tables that will be used to support downstream workflows. Use the CSV files that were pulled to Amperity to define the schema for each feed.

.. sources-add-feed-note-fivetran-end

.. 
.. For Snowflake itself running on either Amazon AWS or Azure.
.. 

.. sources-add-feed-note-snowflake-start

.. note:: A feed must be added for *each* table that is pulled from |source-name|, including all tables that contain customer records and interaction records, along with any other tables that will be used to support downstream workflows. Use the CSV files that were pulled to Amperity to define the schema for each feed.

.. sources-add-feed-note-snowflake-end

**To add a feed (non-Snowflake)**

.. sources-add-feed-steps-start

#. From the **Sources** tab, click **Add Feed**. This opens the **Add Feed** dialog box.
#. Under **Data Source**, select **Create new source**, and then enter "|source-name|".
#. Enter the name of the feed in **Feed Name**. For example: "|feed-name|".

   .. tip:: The name of the domain table will be "<data-source-name>:<feed-name>". For example: "|domain-table-name|".

#. Under **Sample File**, select **Select existing file**, and then choose from the list of files. For example: "|example-filename|".

   .. tip:: The list of files that is available from this drop-down menu is sorted from newest to oldest.
#. Select **Load sample file on feed activation**.
#. Click **Continue**. This opens the **Feed Editor** page.
#. Select the primary key.
#. Apply semantic tags to customer records and interaction records, as appropriate.
#. Under **Last updated field**, specify which field best describes when records in the table were last updated.

   .. tip:: Choose **Generate an "updated" field** to have Amperity generate this field. This is the recommended option unless there is a field already in the table that reliably provides this data.

#. For feeds with customer records (PII data), select **Make available to Stitch**.
#. Click **Activate**. Wait for the feed to finish loading data to the domain table, and then review the sample data for that domain table from the **Data Explorer**.

.. sources-add-feed-steps-end

**To add a feed (Snowflake)**

.. sources-add-feed-steps-snowflake-start

#. From the **Sources** tab, click **Add Feed**.
#. Add a data source named Snowflake.

   .. tip:: Use the same data source for all Snowflake table objects that are to be sent to Amperity.
#. Enter the name of the Snowflake table object as the name of the feed.
#. Upload a CSV file.
#. Click **Continue**.
#. Choose the primary key, apply semantics, adjust field types, verify any fields that are marked required, and then click **Activate**.

.. sources-add-feed-steps-snowflake-end




**Add load operations**

The introduction to this section is literally the same for all data sources and uses the "source name" variable. This section has a custom section that shows an example load operation, which is positioned after the introduction and before the how-to.

.. sources-add-load-operation-start

After the feeds are activated and domain tables are available, add the load operations to the courier used for |source-name|.

.. sources-add-load-operation-end

**Example for example load operations**

There are two example intros, one for files and one for Fivetran.

.. sources-add-load-operation-example-intro-start

Load operations must specify each file that will be pulled to Amperity from |source-name|.

.. sources-add-load-operation-example-intro-end

.. sources-add-load-operation-example-intro-fivetran-start

Load operations must specify each table that will be pulled to Amperity from |source-name|.

.. sources-add-load-operation-example-intro-fivetran-end

.. 
.. each source has its own example operation that should go in this spot
.. do not pull this section to the file; each of these is unique
.. 

.. source-xxxxx-add-load-operations-example-start

Load operations must specify each file that will be pulled to Amperity from |source-name|. For example:

::

   {
     "CUSTOMER-RECORDS-FEED-ID": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "customer-records"
       }
     ],
     "TRANSACTION-RECORDS-FEED-ID": [
       {
         "type": "load",
         "file": "transaction-records"
       }
     ]
   }

.. source-xxxxx-add-load-operations-example-end

**To add load operations**

.. sources-add-load-operation-steps-start

#. From the **Sources** tab, open the menu for the courier that was configured for |source-name|, and then select **Edit**. The **Edit Courier** dialog box opens.
#. Edit the load operations for each of the feeds that were configured for |source-name| so they have the correct feed ID.
#. Click **Save**.

.. sources-add-load-operation-steps-end




**Run courier manually**

This section is literally the same for all data sources.

.. sources-run-courier-start

Run the courier again. This time, because the load operations are present and the feeds are configured, the courier will pull data from |source-name|.

.. sources-run-courier-end

**To run the courier manually**

.. sources-run-courier-steps-start

#. From the **Sources** tab, open the |fa-kebab| menu for the courier with updated load operations that is configured for |source-name|, and then select **Run**. The **Run Courier** dialog box opens.
#. Select the load option, either for a specific time period or all available data. Actual data will be loaded to a domain table because the feed is configured.
#. Click **Run**.

   This time the notification will return a message similar to:

   ::

      Completed in 5 minutes 12 seconds

.. sources-run-courier-steps-end





**Add to courier group**

.. sources-add-to-courier-group-steps-start

#. From the **Sources** tab, click **Add Courier Group**. This opens the **Create Courier Group** dialog box.
#. Enter the name of the courier. For example: "|source-name|".
#. Add a cron string to the **Schedule** field to define a schedule for the orchestration group.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-courier-group-schedule-start
      :end-before: .. term-courier-group-schedule-end

   .. include:: ../../shared/terms.rst
      :start-after: .. term-crontab-syntax-start
      :end-before: .. term-crontab-syntax-end

#. Set **Status** to **Enabled**.
#. Specify a time zone.

   .. include:: ../../amperity_reference/source/courier_groups.rst
      :start-after: .. courier-groups-timezones-start
      :end-before: .. courier-groups-timezones-end

   .. note::

      .. include:: ../../amperity_reference/source/courier_groups.rst
         :start-after: .. courier-groups-timezones-downstream-start
         :end-before: .. courier-groups-timezones-downstream-end

#. Add at least one courier to the courier group. Select the name of the courier from the **Courier** drop-down. Click **+ Add Courier** to add more couriers.
#. Click **Add a courier group constraint**, and then select a courier group from the drop-down list.

   .. include:: ../../amperity_reference/source/courier_groups.rst
      :start-after: .. courier-groups-schedule-wait-time-start
      :end-before: .. courier-groups-schedule-wait-time-end

#. For each courier group constraint, apply any offsets.

   .. include:: ../../amperity_reference/source/courier_groups.rst
      :start-after: .. courier-groups-schedule-offset-start
      :end-before: .. courier-groups-schedule-offset-end
#. Click **Save**.

.. sources-add-to-courier-group-steps-end







SOURCES
SOURCES
SOURCES

.. TODO: This is the sections for the templated content for adding sources in /datagrid/. These sections allow for bespoke steps, usually as Step 3, but may have more if they are more complicated. Try to keep the bespoke content within Step 3 as much as possible for consistency.

.. TODO: This is Step 1. Contains variable for image, in case it is necessary to customize.

STEP 1
STEP 1
STEP 1

.. sources-add-source-start

Open the **Sources** page to configure a destination for |source-name|. Click the **Add courier** button to open the **Add courier** dialog box.

.. sources-add-source-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

IMPORTANT: The next paragraph after the image is located in the /shared/credentials.rst topic because they are IDENTICAL.


STEP 2 is also sourced from /shared/credentials.rst.

STEP 3 is unique to most sources.

STEP 4
STEP 4
STEP 4

.. sources-run-the-courier-start

From the **Sources** tab, open the |fa-kebab| menu for the courier, and then select **Run**. The **Run Courier** dialog box opens.

Select a time period to be run, and then click **Run**.

.. sources-run-the-courier-end

STEP 5
STEP 5
STEP 5

.. TODO: The following is for couriers that use a checkbox to select one (or more) tables to bring to Amperity, such as Adobe Commerce, Shopify, et al.

.. sources-verify-feeds-and-domain-tables-start

After running the |source-name| courier it will create a series of feeds and domain tables. Review the records for each domain table to ensure the right data was loaded from |source-name| and that any semantic tags for customer profiles and transactions are applied correctly for your tenant.

Select a time period to be run, and then click **Run**.

.. sources-verify-feeds-and-domain-tables-end