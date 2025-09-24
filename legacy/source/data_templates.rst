.. https://docs.amperity.com/legacy/


.. meta::
    :description lang=en:
        A data template defines how columns in Amperity data structures are sent to downstream workflows.

.. meta::
    :content class=swiftype name=body data-type=text:
        A data template defines how columns in Amperity data structures are sent to downstream workflows.

.. meta::
    :content class=swiftype name=title data-type=string:
        About data templates

==================================================
About data templates
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. TODO: Data templates will be removed from the product during an upcoming redesign for the destinations page. It's likely some of the descriptions/settings will persist in the new UX.


.. _data-templates-campaigns:

Campaign templates
==================================================

.. data-templates-campaigns-start

Data templates that are made available to campaigns may use variables to apply campaign names, group names, and send dates to the names of campaigns that are sent from Amperity.

.. note:: A date is automatically appended to the filename for one-time campaigns.

.. important:: Campaign templates use the same tokens and Joda-Time filters as file-based templates.

.. data-templates-campaigns-end


.. _data-templates-campaigns-recommended-pattern:

Recommended patterns
--------------------------------------------------

.. data-templates-campaigns-recommended-pattern-start

The recommended pattern for using campaign templates with one-time campaigns is to use the ``{{ campaign_name }}`` and ``{{ group_name }}`` variables, along with a timestamp:

::

   {{ campaign_name }} - {{ group_name }}_{{ now|format'yyyy-mm-dd' }}.csv

For recurring campaigns you should avoid using a timestamp:

::

   {{ campaign_name }} - {{ group_name }}.csv

.. data-templates-campaigns-recommended-pattern-end


.. _data-templates-campaigns-variables:

Campaign variables
--------------------------------------------------

.. data-templates-campaigns-variables-start

You may use any of the following campaign template variables:

* :ref:`data-templates-campaigns-campaign-name`
* :ref:`data-templates-campaigns-group-name`

.. * :ref:`data-templates-campaigns-list-name`

.. data-templates-campaigns-variables-end


.. _data-templates-campaigns-campaign-name:

Campaign names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-campaigns-campaign-name-start

Use the ``{{ campaign_name }}`` variable to define where the name of the campaign is added to the filename for a campaign, as it is received by the downstream system.

Use this variable by itself to use the campaign name as the filename. For example, when the filename template is set to ``{{ campaign_name }}`` and the name of the campaign is ``acme_subscriber_bogo_20220815_1`` the filename will be ``acme_subscriber_bogo_20220815_1``.

You may use this variable by itself or with ``{{ group_name }}`` in any order.

.. data-templates-campaigns-campaign-name-end


.. _data-templates-campaigns-group-name:

Treatment group names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-campaigns-group-name-start

Use the ``{{ group_name }}`` variable to define where the name of a treatment group is added to the filename for a campaign, as it is received by the downstream system.

Use this variable by itself to use the treatment group name as the filename. For example, when the filename template is set to ``{{ group_name }}`` and the name of the treatment group is ``Group1_bogo_20220815_1`` the filename will be ``Group1_bogo_20220815_1``.

You may use this variable by itself or with ``{{ campaign_name }}`` in any order.

.. data-templates-campaigns-group-name-end


.. _data-templates-campaigns-list-name:

List names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-campaigns-list-name-start

Use the ``{{ list_name }}`` variable to use the name of the campaign as the filename for a campaign, as it is received by the downstream system.

.. data-templates-campaigns-list-name-end

.. data-templates-campaigns-list-name-caution-start

.. caution:: You should avoid using this campaign template with one-time or recurring campaigns and instead use ``{{ campaign_name }}`` (with or without a timestamp).

.. data-templates-campaigns-list-name-caution-end


.. _data-templates-campaigns-examples:

Campaign examples
--------------------------------------------------

.. data-templates-campaigns-examples-start

The following examples show various campaign template configurations for a campaign named "ACME Churn" and three treatment groups named "Facebook", "Google", and "Bing" that are configured to send the campaign to Meta Ads Manager, Google Ads, and Microsoft Ads.

**campaign name, group name, datestamp**

::

   {{ campaign_name }} - {{ group_name }}_{{ now|format'yyyy-mm-dd' }}.csv

would send three campaigns with names similar to:

* ACME_Churn_Bing_2022-06-15.csv (sent to Microsoft Ads)
* ACME_Churn_Facebook_2022-06-15.csv (sent to Meta Ads Manager)
* ACME_Churn_Google_2022-06-15.csv (sent to Google Ads)


**group name, datestamp**

::

   {{ group_name }}_{{ now|format'yyyy-mm-dd' }}.csv

would send three campaigns with names similar to:

* Bing_2022-06-15.csv (sent to Microsoft Ads)
* Facebook_2022-06-15.csv (sent to Meta Ads Manager)
* Google_2022-06-15.csv (sent to Google Ads)


**campaign name, datestamp**

::

   {{ campaign_name }}_{{ now|format'yyyy-mm-dd' }}.csv

would send three campaigns with names similar to:

* ACME_Churn_2022-06-15.csv (sent to Microsoft Ads)
* ACME_Churn_2022-06-15.csv (sent to Meta Ads Manager)
* ACME_Churn_2022-06-15.csv (sent to Google Ads)


**campaign name, no datestamp**

::

   {{ campaign_name }}.csv

would send three campaigns with names similar to:

* ACME_Churn.csv (sent to Microsoft Ads)
* ACME_Churn.csv (sent to Meta Ads Manager)
* ACME_Churn.csv (sent to Google Ads)

.. data-templates-campaigns-examples-end


.. _data-templates-files:

File templates
==================================================

.. data-templates-files-start

Data templates for file-based destinations share a set of :ref:`common settings <data-templates-files-common>` and then have specific settings, depending on if you are sending those files to any |destination_sftp| site, |destination_amazon_s3|, |destination_azure_blob_storage|, or |destination_google_cloud_storage|.

.. data-templates-files-end


.. _data-templates-files-common:

Common settings
--------------------------------------------------

.. data-templates-files-common-start

Most file-based destinations share common settings:

* :ref:`data-templates-files-common-done`
* :ref:`data-templates-files-common-encoding-methods`
* :ref:`data-templates-files-common-escape-characters`
* :ref:`data-templates-files-common-formats`
* :ref:`data-templates-files-common-template`
* :ref:`data-templates-files-common-header-rows`
* :ref:`data-templates-files-common-line-endings`
* :ref:`data-templates-files-common-quote-mode`

.. data-templates-files-common-end


.. _data-templates-files-common-done:

.DONE files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-common-done-start

Amperity may be configured to include a "success file" to indicate when an orchestration has finished sending data. A success file has a ``.DONE`` file extension and is the last file added by Amperity.

.. data-templates-files-common-done-end

.. data-templates-files-common-done-tip-start

.. tip:: If a downstream sensor is listening for files sent from Amperity, configure that sensor to listen for the presence of the ``.DONE`` file.

.. data-templates-files-common-done-tip-end


.. _data-templates-files-common-encoding-methods:

Encoding methods
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-common-encoding-methods-start

Amperity supports the following encoding methods:

* GZIP
* TAR
* TGZ
* ZIP

.. data-templates-files-common-encoding-methods-end


.. _data-templates-files-common-escape-characters:

Escape characters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-escape-character-start
   :end-before: .. term-escape-character-end

.. data-templates-files-common-escape-character-start

If an escape character is not specified and quote mode is set to “None” this may result in unescaped, unquoted files. When an escape character is not specified, you should select a non-“None” option.

.. data-templates-files-common-escape-character-end


.. _data-templates-files-common-formats:

File formats
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-common-formats-start

You can send results from Amperity in the following file formats:

* `Apache Parquet <https://docs.amperity.com/reference/format_parquet.html>`__
* `CSV <https://docs.amperity.com/reference/format_csv.html>`__
* `JSON <https://docs.amperity.com/reference/format_json.html>`__
* `NDJSON <https://docs.amperity.com/reference/format_ndjson.html>`__
* `PSV <https://docs.amperity.com/reference/format_psv.html>`__
* `TSV <https://docs.amperity.com/reference/format_tsv.html>`__

.. data-templates-files-common-formats-end


.. _data-templates-files-common-formats-delimiters:

Custom delimiters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. data-templates-files-common-formats-delimiters-start

Some formats accepts a custom delimiter. From the **File format** dropdown, select "Custom delimiter" and then in the **Delimiter** box type a single character to use as a custom delimiter.

.. data-templates-files-common-formats-delimiters-end


.. _data-templates-files-common-template:

Filename templates
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-filename-template-start
   :end-before: .. term-filename-template-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-joda-time-start
   :end-before: .. term-joda-time-end


.. _data-templates-files-common-template-text:

Text variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. data-templates-files-common-template-text-start

Strings in a filename template are literal by default. Use the ``{{ text }}`` variable to apply special rendering to the ``text`` value. 

.. data-templates-files-common-template-text-end


.. _data-templates-files-common-template-filters:

Filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. data-templates-files-common-template-filters-start

Use a filter to shift a timezone, and then format it as a string. The following filters are available:

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Filter
     - Description
   * - **local**
     - Use the ``local`` filter to shift a datetime to a given timezone using a string in Joda-Time format. For example: ``local:'America/Los_Angeles'``.
   * - **format**
     - Use the ``format`` filter to format a datetime with a string in Joda-Time format. For example: ``format:'MM-dd-yyyy'``.
   * - **next day**
     - Use the ``next day`` filter to shift the datetime to the next day. For example: ``now|local:'America/Los_Angeles'|next_day``.

.. data-templates-files-common-template-filters-end


.. _data-templates-files-common-template-tokens:

Tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. vale off

.. data-templates-files-common-template-tokens-start

Use a token to specify how to apply a datetime to a file. The following tokens are available:

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Token
     - Description
   * - **now**
     - Use the ``now`` token to apply a datetime to a file that is current *at the time* a file is written.

.. data-templates-files-common-template-tokens-end

.. vale on


.. _data-templates-files-common-template-examples:

Template examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. data-templates-files-common-template-examples-start

To ensure an orchestration's datetime is applied to the Pacific Time Zone:

.. code-block:: none

   C360_incremental_{{now|local:'America/Los_Angeles'|format:'MM-dd-yyyy'}}.csv.gz

To shift the date for an orchestration to be the day after its run:

.. code-block:: none

   customer_360/{{now|local:'America/Los_Angeles'|next_day|format:'YYYY/MM/dd'}}/Customer_360.tsv.gz

.. data-templates-files-common-template-examples-end


.. _data-templates-files-common-header-rows:

Header rows
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-common-header-rows-start

Files, such as CSV, PSV, or TSV, may (or may not) require header rows, which define the headers for that data set. Configure the settings to match if header rows are required by the downstream workflow.

.. data-templates-files-common-header-rows-end


.. _data-templates-files-common-line-endings:

Line endings
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-common-line-endings-start

Some files require a specific line ending. Amperity supports ``LF`` and ``CRLF`` line endings. Configure the settings to match if specific line endings are required by the downstream workflow.

.. data-templates-files-common-line-endings-end


.. _data-templates-files-common-quote-mode:

Quote modes
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-common-quote-mode-start

Quote mode can be set to one of the following:

#. Quotes all fields
#. Quotes all non-null fields
#. Quotes fields with special characters only
#. Quotes all non-numeric fields
#. None

.. data-templates-files-common-quote-mode-end


.. _data-templates-files-specific:

Specific settings
--------------------------------------------------

.. data-templates-files-specific-start

File-based destinations have specific settings, depending on the type of location to which files are sent:

* :ref:`data-templates-files-specific-s3`
* :ref:`data-templates-files-specific-azure-blob-storage`
* :ref:`data-templates-files-specific-google-cloud-storage`
* :ref:`data-templates-files-specific-sftp`

.. data-templates-files-specific-end


.. _data-templates-files-specific-s3:

Amazon S3
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-specific-s3-start

Amazon S3 requires the name of the S3 bucket and the S3 prefix.

.. data-templates-files-specific-s3-end


.. _data-templates-files-specific-azure-blob-storage:

Azure Blob Storage
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-specific-azure-blob-storage-start

Azure Blob Storage requires the name of the container and the blob prefix.

.. data-templates-files-specific-azure-blob-storage-end


.. _data-templates-files-specific-google-cloud-storage:

Google Cloud Storage
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-specific-google-cloud-storage-start

Google Cloud Storage requires the object prefix.

.. data-templates-files-specific-google-cloud-storage-end


.. _data-templates-files-specific-sftp:

SFTP
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-files-specific-sftp-start

SFTP requires the path to the remote folder.

.. data-templates-files-specific-sftp-end


.. _data-templates-api:

API templates
==================================================

.. data-templates-api-start

A data template for a destination that uses an API varies, depending on the type of destination and other configuration details. Data templates that are associated with APIs include |destination_hubspot|, |destination_klaviyo|, |destination_sailthru|, |destination_zendesk|, |destination_meta_ads_manager|, |destination_google_ads|, |destination_campaign_monitor|, |destination_microsoft_dynamics|, and |destination_salesforce_marketing_cloud|.

.. data-templates-api-end


.. _data-templates-snowflake:

Snowflake templates
==================================================

.. data-templates-snowflake-start

A data template for a destination that uses Snowflake must specify the location of the tables to which Amperity writes data, and then the action that will be performed against those tables.

.. data-templates-snowflake-end


.. _data-templates-snowflake-location:

Location
--------------------------------------------------

.. data-templates-snowflake-location-start

A Snowflake location is a period-delimited list that specifies the Snowflake database name, the Snowflake schema name, and the Snowflake table name. For example:

::

   SNOWFLAKE_DATABASE_NAME.SNOWFLAKE_SCHEMA.TABLE_NAME

.. data-templates-snowflake-location-end


.. _data-templates-snowflake-table-actions:

Table actions
--------------------------------------------------

.. data-templates-snowflake-table-actions-start

Amperity can perform three actions against Snowflake tables: create, drop, and truncate.

* :ref:`data-templates-snowflake-table-action-create`
* :ref:`data-templates-snowflake-table-action-drop`
* :ref:`data-templates-snowflake-table-action-truncate`

.. data-templates-snowflake-table-actions-start


.. _data-templates-snowflake-table-action-create:

Create
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-snowflake-table-action-create-start

Use the **Create table** option to create the table in Snowflake when it is not already there.

.. data-templates-snowflake-table-action-create-end

.. data-templates-snowflake-table-action-create-caution-start

.. caution:: Only use this option when Snowflake is not managed by |bic| and when user roles in Snowflake have permissions set on a per-table basis.

.. data-templates-snowflake-table-action-create-caution-end


.. _data-templates-snowflake-table-action-drop:

Drop
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-snowflake-table-action-drop-start

Use the **Drop table** option to overwrite the table and apply an updated schema when the upstream segment or table changes.

.. data-templates-snowflake-table-action-drop-end

.. data-templates-snowflake-table-action-drop-important-start

.. important:: Always use this option when Snowflake is managed by |bic| or when user roles in Snowflake have permission to access all tables in the database.

.. data-templates-snowflake-table-action-drop-important-end


.. _data-templates-snowflake-table-action-truncate:

Truncate
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-templates-snowflake-table-action-truncate-start

Use the **Truncate table** option when the contents of the table should be emptied prior to loading data.

.. data-templates-snowflake-table-action-truncate-end

.. data-templates-snowflake-table-action-truncate-caution-start

.. caution:: Only use this option when Snowflake is not managed by |bic| and when user roles in Snowflake have permissions set on a per-table basis.

.. data-templates-snowflake-table-action-truncate-caution-start


.. _data-templates-howtos:

How-tos
==================================================

.. data-templates-howtos-start

Tasks related to managing data templates in Amperity:

* :ref:`data-templates-add`
* :ref:`data-templates-allow-to-send-queries`
* :ref:`data-templates-allow-to-send-pii`
* :ref:`data-templates-copy-id`
* :ref:`data-templates-delete`
* :ref:`data-templates-edit`
* :ref:`data-templates-enable-success-file`
* :ref:`data-templates-map-to-external-schemas`
* :ref:`data-templates-make-available-to-campaigns`

.. data-templates-howtos-end


.. _data-templates-add:

Add data template
--------------------------------------------------

.. data-templates-add-start

Use the **Add data template** button option in the row for an existing destination to add a data template. The data template inherits the credentials, visibility, PII, and template settings that were configured for the destination.

.. data-templates-add-end

**To add a data template**

.. data-templates-add-steps-start

#. From the **Destinations** page, open the menu for a destination, and then select **Add data template**.
#. In the **Add Data Template** dialog box, enter the name of the data template and add a description.

   .. note:: The data template inherits the credentials and template settings that are configured by the destination.

#. Select **Allow query authors to use this data template** to ensure use of this data template by query authors.
#. Select **Allow query authors with limited PII access to use with orchestrations** to enable the use of this data template by users with limited PII access.

   .. important:: This option must be enabled for the destination **and** the data template.
#. Review the data template settings.
#. Click **Save**.

.. data-templates-add-steps-end


.. _data-templates-allow-to-send-queries:

Allow to send queries
--------------------------------------------------

.. data-templates-allow-to-send-queries-start

Query authors must be allowed to send queries to a destination. This is enabled by the **Allow query authors to use this data template** option. When this option is enabled for a data template, it must also be enabled for the destination to which the query author wants to send a query.

.. data-templates-allow-to-send-queries-end

**To allow query authors to use a data template**

.. data-templates-allow-to-send-queries-steps-start

#. From the **Destinations** page, open the menu in the same row as the destination to be edited, and then select **Edit Settings**.
#. Select the **Allow query authors to use this data template** option.
#. Click **Save**.

.. data-templates-allow-to-send-queries-steps-end


.. _data-templates-allow-to-send-pii:

Allow to send PII
--------------------------------------------------

.. data-templates-allow-to-send-pii-start

Some users of Amperity are allowed only limited access to view PII data. Users with limited access must be allowed to send PII data. This is enabled by the **Allow query authors with limited PII access to use with orchestrations** option. When this option is enabled for a data template, it must also be enabled for the destination to which PII data is to be sent.

.. data-templates-allow-to-send-pii-end

**To allow users with limited access to PII data to send data**

.. data-templates-allow-to-send-pii-steps-start

#. From the **Destinations** page, open the menu in the same row as the destination to be edited, and then select **Edit Settings**.
#. Select the **Allow query authors with limited PII access to use with orchestrations** option.
#. Click **Save**.

.. data-templates-allow-to-send-pii-steps-end


.. _data-templates-copy-id:

Copy data template ID
--------------------------------------------------

.. data-templates-copy-id-start

You can copy a data template ID, and then use that ID within Amperity workflows, such as getting a list of campaigns associated with a specific data template when using the **Campaigns** endpoint in the Amperity API.

.. data-templates-copy-id-end

**To copy the ID for a data template**

.. data-templates-copy-id-steps-start

#. From the **Destinations** page, open the menu in the same row as the data template for which the ID is to be copied, and then select **Copy ID**.

.. data-templates-copy-id-steps-end


.. _data-templates-delete:

Delete data template
--------------------------------------------------

.. data-templates-delete-start

Use the **Delete Settings** option to remove a data template from Amperity. This should be done carefully. Verify that both upstream and downstream processes no longer depend on this data template prior to deleting it.

.. data-templates-delete-end

**To delete a data template**

.. data-templates-delete-steps-start

#. From the **Destinations** page, open the menu in the same row as the data template to be deleted, and then select **Delete**.
#. Click **Confirm**.

.. data-templates-delete-steps-end


.. _data-templates-edit:

Edit data template
--------------------------------------------------

.. data-templates-edit-start

Use the **Edit Settings** option in the row for a specific data template to make changes, including to credentials, visibility, PII, and template settings. Verify that both upstream and downstream processes are not affected by these changes.

.. data-templates-edit-end

**To edit a data template**

.. data-templates-edit-steps-start

#. From the **Destinations** page, open the menu in the same row as the data template to be edited, and then select **Edit Settings**.
#. Make changes to the data template.
#. Click **Save**.

.. data-templates-edit-steps-end


.. _data-templates-enable-success-file:

Enable success file
--------------------------------------------------

.. data-templates-enable-success-file-start

Amperity may be configured to include a "success file" to indicate when an orchestration has finished sending data. A success file has a ``.DONE`` file extension and is the last file added by Amperity.

.. data-templates-enable-success-file-end

.. data-templates-enable-success-file-tip-start

.. tip:: If a downstream sensor is listening for files sent from Amperity, configure that sensor to listen for the presence of the ``.DONE`` file.

.. data-templates-enable-success-file-tip-end

**To enable a success file**

.. data-templates-enable-success-file-steps-start

#. From the **Destinations** page, open the menu in the same row as the data template to be deleted, and then select **Edit**.
#. Under **Template Settings**, select the **Include success file upon completion** option.
#. Click **Save**.

.. data-templates-enable-success-file-steps-end


.. _data-templates-map-to-external-schemas:

Map to external schemas
--------------------------------------------------

.. warning:: Applies **ONLY** to the |destination_meta_ads_manager| and |destination_google_ads| destinations.

.. data-templates-map-to-external-schemas-start

Data mappings support two options:

* Use **Visual and SQL queries** to allow mapping for this template to apply to queries created by the visual **Query Editor** or the **SQL Query Editor**.
* Use **SQL queries only** to limit mapping for this template to apply only queries created by the **SQL Query Editor**.

If the destination does not require Amperity fields to be mapped, leave the value **NULL**. Otherwise, replace with a data mapping structure that maps fields to the required naming pattern.

.. data-templates-map-to-external-schemas-end

**To define a data mapping**

.. data-templates-map-to-external-schemas-steps-start

#. From the **Destinations** page, open the menu in the same row as the data template to be edited, and then select **Edit Settings**.
#. Identify the external schema to which Amperity data will be mapped.
#. As part of adding or editing a data template from within the **Data Template** dialog box, under **Data Mappings**, define the data mappings that are required to map Amperity fields with fields in the external schema.
#. Click **Save**.

.. data-templates-map-to-external-schemas-steps-end


.. _data-templates-make-available-to-campaigns:

Make available to campaigns
--------------------------------------------------

.. data-templates-make-available-to-campaigns-start

A destination may be used with campaigns only after it is enabled for those workflows.

.. data-templates-make-available-to-campaigns-end

**To make a data template available to campaigns**

.. data-templates-make-available-to-campaigns-steps-start

#. From the **Destinations** page, open the menu in the same row as the destination to be edited, and then select **Edit Settings**.
#. Enable the **Available to campaigns** option.
#. Click **Save**.

.. data-templates-make-available-to-campaigns-steps-end
