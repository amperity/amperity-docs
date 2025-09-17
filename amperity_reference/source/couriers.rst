.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        A courier brings data from an external system to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        A courier brings data from an external system to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        About couriers

==================================================
About couriers
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. couriers-what-they-do-start

What a courier does:

#. Checks if data is available at the source location.
#. Collects data from the source location, and then pulls that data to Amperity.

What a courier needs:

#. Access to the source location. Most data sources--Amazon S3, Azure Blob Storage, Google Cloud Storage, or any SFTP site--allow the use of many file formats, while others may use Snowflake or REST APIs.
#. A location from which to copy data.
#. An associated feed.
#. A file format--CSV, TSV, Apache Parquet, etc., along with additional details for compression, archive, and encryption.
#. A combination of :ref:`load settings <couriers-files-load-settings>` and :ref:`load operations <couriers-load-operation-types>`. The exact combination of settings and operations depends on the data source and the types of files to be pulled to Amperity.

.. couriers-what-they-do-end


.. _couriers-files:

File couriers
==================================================

.. couriers-files-start

A file data source can provide files to Amperity in just about any file format, such as CSV, JSON, Apache Parquet, Apache AVRO, PSV, and TSV. Locations from which file data sources can be pulled include |source_amazon_s3|, |source_azure_blob_storage|, |source_google_cloud_storage|, and |source_sftp_any|.

.. couriers-files-end


.. _couriers-files-load-settings:

Load settings
--------------------------------------------------

.. couriers-files-load-settings-start

File data sources define load settings in two parts:

#. A list of files that should be pulled to Amperity.
#. A load operation.

The exact combination of files and load operations depends on the data source from which data is made available to Amperity.

.. couriers-files-load-settings-end


.. _couriers-files-patterns:

File patterns
--------------------------------------------------

.. couriers-files-patterns-start

A courier looks for objects using a combination of the path to a directory, the name of a file, and a date. A courier runs based on a date or a date range, and then looks for files in the source location for that date or date range.

.. couriers-files-patterns-end


.. _couriers-files-patterns-wildcards:

Wildcards
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-files-patterns-wildcards-start

A wildcard can match zero or more characters up until a forward-slash character.

.. note:: When a file pattern with a wildcard matches more than one file for a given date or date range, the matched files are loaded in such a way that guarantees per-day ordering. If your courier uses an ingest query, ascending lexicographical ordering by file is not guaranteed or preserved within a single day's files.

**Examples**

The following example shows using a wildcard at the end of a file pattern:

.. code-block:: none

   'files/'yyyy'/'MM'/'dd'/customers-*.csv'

will match any of these files:

* /customers-.csv
* /customers-1.csv
* /customers-hello-world.csv

and will not match any of these:

* /customers-.csv.0
* /customers-0.json
* /customers-0/1/file.csv
* /customers.csv

.. couriers-files-patterns-wildcards-end


.. _couriers-files-patterns-literal-strings:

Literal strings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-load-settings-file-pattern-literal-strings-start

A literal string must be an exact match to characters in the file path, with the exception of the presence of wildcard characters within literal strings. Wrap literal strings that match Joda-Time format in single quotes. For example:

* 'files/'
* '/'
* '/'
* 'MM-dd-YYYY'

.. couriers-files-patterns-literal-strings-end


.. _couriers-files-patterns-date-components:

Date components
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-files-patterns-date-components-start

Date components act as placeholders for months, days, and years. Real values are applied when the courier runs on a given date or date range. Date components must match `Joda-Time pattern-based formatting <https://www.joda.org/joda-time/key_format.html>`__ |ext_link|, but should generally be limited to the following patterns:

.. list-table::
   :widths: 200 200 200
   :header-rows: 1

   * - Pattern
     - Meaning
     - Examples
   * - **yyyy**
     - 4-digit year
     - 2020, 2021, 2022
   * - **MM**
     - 2-digit month
     - 01, 02, 03
   * - **dd**
     - 2-digit date
     - 01, 02, 03, 04

A courier that runs using this pattern:

.. code-block:: none

   'files/'yyyy'/'MM'/'dd'/customers-*.csv'

when run on April 10, 2020 will look for files at ``'files/2020/04/10/customers-*.csv'`` and will return any files that match.

.. couriers-files-patterns-date-components-end


.. _couriers-load-settings-input-examples:

Input examples
--------------------------------------------------

.. include:: ../../amperity_reference/source/format_common.rst
   :start-after: .. format-common-send-input-examples-start
   :end-before: .. format-common-send-input-examples-end


.. _couriers-load-settings-input-example-single:

for single files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/format_common.rst
   :start-after: .. format-common-send-input-examples-single-start
   :end-before: .. format-common-send-input-examples-single-end


.. _couriers-load-settings-input-example-multiple:

for multiple files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/format_common.rst
   :start-after: .. format-common-send-input-examples-multiple-start
   :end-before: .. format-common-send-input-examples-multiple-end


.. _couriers-api:

API couriers
==================================================

.. couriers-api-start

An API data source varies, depending on the file format and other configuration details. API data sources include |source_campaign_monitor|, |source_google_analytics|, |source_salesforce_sales_cloud|, and |source_zendesk|.

.. couriers-api-end


.. _couriers-snowflake:

Snowflake couriers
==================================================

.. couriers-snowflake-start

A Snowflake data source provides a list of tables that are consolidated into a fileset. Snowflake data sources include Snowflake itself, and then also any FiveTran data source, such as |source_klaviyo|, |source_shopify|, |source_kustomer|, and |source_hubspot|.

.. couriers-snowflake-end


.. _couriers-snowflake-table-list:

Table lists
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-table-list-start
   :end-before: .. sources-add-courier-fivetran-table-list-end

.. couriers-snowflake-table-list-example-start

::

   [
     "AMPERITY_A1BO987C.ACME.CAMPAIGN",
     "AMPERITY_A1BO987C.ACME.LIST",
     "AMPERITY_A1BO987C.ACME.CONTACT"
   ]

.. couriers-snowflake-table-list-example-end


.. _couriers-snowflake-stage-name:

Stage names
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-stage-name-start
   :end-before: .. sources-add-courier-fivetran-stage-name-end

.. couriers-snowflake-stage-name-example-start

::

   AMPERITY_A1BO987C.ACME.ACME_STAGE

.. couriers-snowflake-stage-name-example-end


.. _couriers-snowflake-load-operation:

Load operations
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-load-operation-start
   :end-before: .. sources-add-courier-fivetran-load-operation-end

.. couriers-snowflake-load-operation-start

::

   {
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.ACME.CAMPAIGN"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.ACME.LIST"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.ACME.CONTACT"
       }
     ]
   }

.. couriers-snowflake-load-operation-end


.. _couriers-load-operation-types:

Load types
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-fileset-start
   :end-before: .. term-courier-fileset-end

.. couriers-load-operation-types-start

.. couriers-load-operation-types-links-start

Each file in a fileset must be associated with one of the following load operation types:

* :ref:`couriers-load-operation-type-load-files`
* :ref:`couriers-load-operation-type-spark`
* :ref:`couriers-load-operation-type-truncate-then-load`

.. couriers-load-operation-types-links-end


.. _couriers-load-operation-type-load-files:

Load file
--------------------------------------------------

.. couriers-load-operation-type-load-files-start

You can load contents of a data file to a domain table as an ``UPSERT`` operation that is based off of the primary key in the table.

.. couriers-load-operation-type-load-files-end


.. _couriers-load-operation-type-spark:

Load file with complex data types
--------------------------------------------------

.. couriers-load-operation-type-spark-start

Use the **Spark** load type for files that have complex or nested data structures. Use when:

* :doc:`format_avro` files have **records**, **enums**, **arrays**, **maps**, **unions**, and **fixed** data types.
* :doc:`format_parquet` files have **struct**, **array**, and **map** data types.
* :doc:`format_json` files have nested objects and arrays.
* :doc:`format_xml` files have **complexType** elements.

.. couriers-load-operation-type-spark-end


.. _couriers-load-operation-type-truncate-then-load:

Truncate, then load file
--------------------------------------------------

.. couriers-load-operation-type-truncate-then-load-start

You can empty the contents of a table prior to loading a data file to a domain table as a load operation.

.. note:: A truncate operation is always run first, regardless of where it's specified within the load operation.

.. couriers-load-operation-type-truncate-then-load-end



.. _couriers-howtos:

How-tos
==================================================

.. couriers-howtos-list-start

Tasks related to managing couriers in Amperity:

* :ref:`couriers-add`
* :ref:`couriers-add-as-copy`
* :ref:`couriers-add-to-courier-group`
* :ref:`couriers-delete`
* :ref:`couriers-edit`
* :ref:`couriers-load-data-only`
* :ref:`Run and only load files <couriers-run-only-load-files>`
* :ref:`Run for a specific day <couriers-run-for-specific-day>`
* :ref:`Run for a time period <couriers-run-for-time-period>`
* :ref:`Run, but skip missing files <couriers-run-skip-missing-files>`
* :ref:`couriers-run-restart-job`
* :ref:`couriers-view`

.. couriers-howtos-list-end


.. _couriers-add:

Add courier
--------------------------------------------------

.. couriers-add-start

Use the **Add Courier** button to add a courier to Amperity. A courier should be created for each feed that exists in Amperity.

.. couriers-add-end

.. couriers-add-context-start

For smaller data sources, a courier may be associated with more than one feed. For larger data sources, a courier should be associated with a single feed. This is, in part, because couriers are run in parallel, but multiple feeds associated with a single courier are run sequentially.

For example: if Snowflake is configured to send six tables to Amperity via six feeds, but all running as part of the same courier, table one must finish before table two, which must finish before table three, and so on. Whereas if each table is configured with its own courier, all six tables could start processing at the same time.

A courier configured from the Amperity UI must be configured to use one of the existing plugins in Amperity, such as for Amazon S3, Azure Blob Storage, Azure Data Lake Storage, SFTP, or Snowflake.

Some of these plugins have more than one option for credentials.

Use SnapPass to securely share configuration data with your Amperity representative.

.. couriers-add-context-end

**To add a courier**

.. couriers-add-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Courier** page opens.
#. Enter the name of the courier.
#. From the **Plugin** dropdown, select a plugin.

   .. note:: The settings for a courier varies, depending on the courier selected from the **Plugin** dropdown.

#. Enter the credentials for the courier type.
#. Enter any courier-specific settings.
#. Under **<COURIER NAME> Settings** configure the file load settings. This is done in two parts: a list of files that should be available to Amperity, including how they are made available, and then a series of load operations that associates each file in the list to a feed.
#. Click **Save**.

.. couriers-add-steps-end


.. _couriers-add-as-copy:

Add courier as copy
--------------------------------------------------

.. couriers-add-as-copy-start

You may add a courier by copying an existing courier. This is useful when couriers share plugin, credential, and other common settings. A copied courier will retain all of the configured settings as the original, but will be assigned a unique name based on the name of the copied courier.

.. couriers-add-as-copy-end

**To add a courier as a copy**

.. couriers-add-as-copy-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Make a copy**. The **Add Courier** page opens.
#. Update the name of the courier.
#. Verify all other configuration settings. Edit them as necessary.
#. Under **<COURIER NAME> Settings** configure the file load settings. This is done in two parts: a list of files that should be available to Amperity, including how they are made available, and then a series of load operations that associates each file in the list to a feed.
#. Click **Save**.

.. couriers-add-as-copy-steps-end


.. _couriers-add-to-courier-group:

Add to courier group
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add a courier to a courier group**

.. couriers-add-to-courier-group-steps-start

#. From the **Sources** page, open the menu for a courier group, and then select **Edit**.
#. On the **Couriers** tab, click the **Add courier** link.
#. Select the name of a courier from the dropdown list, set the wait time and range for which data is loaded. Enable alerts for when files are missing.
#. Click **Save**.

.. couriers-add-to-courier-group-steps-end


.. _couriers-delete:

Delete courier
--------------------------------------------------

.. couriers-delete-start

Use the **Delete** option to remove a courier from Amperity. This should be done carefully. Verify that both upstream and downstream processes no longer depend on this courier before you delete it. This action will *not* delete the feeds associated with the courier.

.. couriers-delete-end

**To delete a courier**

.. couriers-delete-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Delete**. The **Delete Courier** dialog box opens.
#. Click **Delete**.

.. couriers-delete-steps-end


.. _couriers-edit:

Edit courier
--------------------------------------------------

.. couriers-edit-start

Use the **Edit** option in the row for a specific courier to make configuration changes. For example, a new file is added to an Amazon S3 filedrop location already configured to send data to Amperity. After the feed is created, it can be added to the existing courier objects and load operations.

In other cases, a courier may need editing because the credentials to the data source have changed. 

.. couriers-edit-end

**To edit a courier**

.. couriers-edit-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Edit**. The **Edit Courier** page opens.
#. Make your changes.
#. Click **Save**.

.. couriers-edit-steps-end


.. _couriers-load-data-only:

Load data only
--------------------------------------------------

.. couriers-load-data-only-start

A courier can be run to load data to a domain table and prevent downstream processes, such as Stitch, customer 360 database runs, queries, and orchestrations.

.. couriers-load-data-only-end

**To load data without downstream processing**

.. couriers-load-data-only-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific day** or **Load data from a specific time period**.
#. To prevent downstream processing, select **Ingest only**.
#. Click **Run**.

.. couriers-load-data-only-steps-end


.. _couriers-run:

Run couriers
--------------------------------------------------

.. couriers-run-start

Use the **Run** option to run the courier manually.

.. couriers-run-end

A courier can be run in the following ways:

* :ref:`Only load files <couriers-run-only-load-files>`
* :ref:`Run for a specific day <couriers-run-for-specific-day>`
* :ref:`Run for a time period <couriers-run-for-time-period>`
* :ref:`Skip missing files <couriers-run-skip-missing-files>`


.. _couriers-run-only-load-files:

Only load files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-run-only-load-files-start

A courier can be configured to load data, but not start any downstream processing, including Stitch, database generation, or queries.

.. warning:: Stitch must be run for data to be available in databases. Jobs that are run as load only do not automatically run Stitch.

.. couriers-run-only-load-files-end

**To run a courier without downstream processing**

.. couriers-run-without-downstream-processing-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific day** or **Load data from a specific time period**.
#. Under **Load options**, select **Ingest only**.
#. Click **Run**.

.. couriers-run-without-downstream-processing-steps-end


.. _couriers-run-for-specific-day:

Run for a specific day
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-run-for-specific-day-start

A courier can be configured to load data from a specific day.

.. couriers-run-for-specific-day-end

**To run a courier and load data from a specific day**

.. couriers-run-for-specific-day-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific day**.
#. Select a calendar date.
#. To prevent downstream processing, select **Ingest only**.

   .. warning:: When a data source is changed, and then loaded using the **Ingest only** option, downstream processes are not started automatically. Data that contains PII must be stitched. Databases that contain interaction records must be regenerated so that attributes and predictions are recalculated.
#. Click **Run**.

.. couriers-run-for-specific-day-steps-end


.. _couriers-run-for-time-period:

Run for a time period
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-run-for-time-period-start

A courier can be configured to load all data from a specified time period.

.. couriers-run-for-time-period-end

**To run a courier to load all data from a specific time period**

.. couriers-run-for-time-period-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific time period**.
#. Select a start date and an end date.

   .. important:: The start of the selected date range is inclusive, whereas the end of the selected date range is exclusive.
#. To prevent downstream processing, select **Ingest only**.

   .. warning:: When a data source is changed, and then loaded using the **Ingest only** option, downstream processes are not started automatically. Data that contains PII must be stitched. Databases that contain interaction records must be regenerated so that attributes and predictions are recalculated.
#. Click **Run**.

.. couriers-run-for-time-period-steps-end


.. _couriers-run-skip-missing-files:

Skip missing files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-run-skip-missing-files-start

A courier can be configured to skip sources files that are missing and continue running.

.. couriers-run-skip-missing-files-end

**To skip missing files**

.. couriers-run-skip-missing-files-steps-start

#. From the **Sources** page, open the menu for a courier, and then select **Run**. The **Run Courier** page opens.
#. Select **Load data from a specific day** or **Load data from a specific time period**.
#. Under **Load options**, select **Skip missing files**.
#. Click **Run**.

.. couriers-run-skip-missing-files-steps-end


.. _couriers-view-errors:

View error log
--------------------------------------------------

.. couriers-view-errors-start

If a courier runs and returns an error, you may view the errors from that feed.

.. couriers-view-errors-end

**To view errors**

.. couriers-view-errors-steps-start

#. From the **Notifications** pane, for the stage error, open the **View Load Details** link.
#. From the **View Load Details** pane, select **View Error Log** for the feed with errors.
#. Investigate the errors reported.

.. couriers-view-errors-steps-end


.. _couriers-run-restart-job:

Restart job
++++++++++++++++++++++++++++++++++++++++++++++++++

.. couriers-run-restart-job-start

If a courier runs and returns an error, you may view the error, resolve that error by updating the feed configuration or Spark SQL query, and then restart it without having to reload the data associated with the job.

.. couriers-run-restart-job-end

**To restart a job**

.. couriers-run-restart-job-steps-start

#. From the **Notifications** pane, for the stage error, open the **View Load Details** link and investigate why the job failed.
#. Edit the feed configuration or Spark SQL query to address the reasons for the error.
#. From the **Notifications** pane, click **Restart Ingest Job**.

.. couriers-run-restart-job-steps-end


.. _couriers-view:

View courier
--------------------------------------------------

.. couriers-view-start

The **Sources** page shows the status of every courier, including when it last ran or updated, and its current status.

.. couriers-view-end

**To view a courier**

.. couriers-view-steps-start

From the **Sources** page, open the menu for a courier, and then select **View**. The **View Courier** page opens.

.. couriers-view-steps-end
