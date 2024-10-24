.. 
.. xxxxx
..


.. |sftp-type| replace:: ``passphrase``
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
   :start-after: .. sources-add-courier-steps-files-start
   :end-before: .. sources-add-courier-steps-files-end







**TEMPLATE SECTIONS FOR DESTINATIONS**

This topic contains the templated sections for all of the "Send to xxxxx" topics in /configure/. You must use these templated sections. Use the beginning of the topic to introduce anything that is destination-specific. You cannot add destination-specific content within the templated sections outside of providing the variables for "destination name", xxxxx, and xxxxx.

In certain cases, a destination topic will require *some* customization within the templated sections. See the xxxxx topic, **xxxxx** section for how to do this.

.. destinations-overview-list-intro-start

This topic describes the steps that are required to send |what-send| to |destination-name| from Amperity:

.. destinations-overview-list-intro-end





**Configure OAuth**

.. destinations-oauth-intro-start

Use OAuth to configure Amperity to send |what-send| to |destination-name|.

.. destinations-oauth-intro-end


.. destinations-oauth-configure-step-1-start

Open the **Destinations** tab and click **Add Destination**. The **Add Destination** dialog box opens.

Select |destination-name| from the **Plugin** drop-down, and then from the **Credential** drop-down, select **Create a new credential**.

This opens the **Create New Credential** dialog box.

.. destinations-oauth-configure-step-1-end

.. destinations-oauth-configure-step-2-start

In the **Create New Credential** dialog box, click "Generate authorization URL".

Copy the URL, and then provide the URL to a user who has credentials that allow access to |destination-name|. The user must log in and complete the steps required by the OAuth process for |destination-name|.

After this is completed, you will be redirected to the **Credentials** page in Amperity.

Verify the credential is on the page, and then return to the **Destinations** tab.

.. destinations-oauth-configure-step-2-end

.. destinations-oauth-configure-step-3-start

Open the **Destinations** tab and click **Add Destination**. The **Add Destination** dialog box opens.

Select |destination-name| from the **Plugin** drop-down, and then from the **Credential** drop-down, select the credential that is authorized to access |destination-name|.

.. note:: The value for the **Refresh Token** setting is updated automatically after you select the credential.

.. destinations-oauth-configure-step-3-end


.. destinations-oauth-reauthorize-start

You may need to reauthorize access to |destination-name|. This is necessary when an authorization token has expired or when it has been removed by someone with permission to manage access within |destination-name|. To reauthorize access to |destination-name|, follow the steps to configure OAuth and create a new credential.

.. destinations-oauth-reauthorize-end

.. destinations-oauth-warning-about-reauthorize-start

.. important:: Amperity requires access to |destination-name|. This access may expire or be removed periodically, depending on how OAuth is managed at |destination-name|. If Amperity is unable to send data to |destination-name| ask your DataGrid Operator to reauthorize access to |destination-name|.

.. destinations-oauth-warning-about-reauthorize-end






**Add destination**

.. destinations-add-destinations-intro-all-start

Configure Amperity to send |what-send| directly to |destination-name|.

.. destinations-add-destinations-intro-all-end

.. TODO: Deprecate all of these "tailored" intros. They aren't needed. Except for "webhook"

.. destinationsx-add-destinations-intro-sftp-only-start

Configure Amperity to send data to |destination-name| using SFTP.

.. destinations-add-destinations-intro-sftp-only-end





**API destinations**

.. TODO: These are generic. Some APIs may have specific sections and may require their own bespoke step-by-steps. In those instances, copy the section below and "override" the section in the destination topic and add the content you need.


.. destinations-add-destinations-intro-allow-for-start

Changes to |allow-for-what| are not immediately available in |destination-name|. Allow for |allow-for-duration| after the point at which Amperity has finished sending audience updates for them to be available.

.. destinations-add-destinations-intro-allow-for-end



.. destinationsx-add-destinations-intro-api-only-start

Configure Amperity to send data to |destination-name| using the |destination-api|.

.. destinations-add-destinations-intro-api-only-end

.. TODO: The following API-based destinations have bespoke settings: Campaign Monitor, Mailchimp. If the steps below change, they are mostly global to API-based destinations, but you will need to also update ones with bespoke settings to retain consistency.

.. TODO: Facebook, Google use Oauth, which has different steps.








.. TODO: Amazon S3, Optimizely, Throtle

.. TODO: Common intro for non-Amazon S3 destinations

.. destinationsx-add-destinations-amazon-s3-common-start

|destination-name| is a destination that may be configured directly from Amperity. This destination uses a customer-managed |plugin-name| bucket. Use the customer's credentials to this |plugin-name| bucket when configuring this location.

.. destinations-add-destinations-amazon-s3-common-end


.. destinations-add-destinations-amazon-s3-cross-account-start

.. note:: Amperity supports using cross-account role assumption with Amazon S3 buckets when |destination-name| supports the use of cross-account roles and your tenant uses the |destination_amazon_s3| destination.

.. destinations-add-destinations-amazon-s3-cross-account-end





**OAuth Destinations**

.. TODO: Applies to Criteo, Facebook Ads, Google Ads, Microsoft Ads, Snapchat, and TikTok destinations.

.. destinations-add-destinations-api-oauth-reminder-start

.. warning:: Amperity must be authorized to send data to your |destination-name| account prior to configuring the destination.

.. destinations-add-destinations-api-oauth-reminder-end



**Webhook destinations**

.. destinations-add-destinations-webhook-intro-start

Use a webhook destination to send query results from Amperity to a Lambda function running in AWS Lambda in your instance of Amazon AWS.

.. destinations-add-destinations-webhook-intro-end


.. destinations-add-destinations-webhook-start

#. From the **Destinations** tab, click **Add Destination**. This opens the **Add Destination** dialog box.
#. Enter the name of the destination and a description. For example, "|destination-name|" and "Send |what-send| in |destination-name|".
#. From the **Plugin** drop-down, select "Webhook".
#. The "webhook" credential type is selected automatically.
#. From the **Credential** drop-down, select a credential that has already been configured for this destination *or* click **Create a new credential**, which opens the **Create New Credential** dialog box. For new credentials, enter a name for the credential, the API key, and the webhook URL. (The webhook URL is the endpoint for the API gateway.) Click **Save**.

   .. tip:: The API key and webhook URL settings are available from your AWS Lambda console. Log in to your AWS Lambda console, and then click **Configuration**. The API key is in the **Details** section and the webhook URL is in the **Triggers** section.

      For example:

      **API key** AB1c2D3eFGH4j5KL6

      **Webhook URL** https://acme.execute-api.us-east-123.amazonaws.com/Prod/run/

#. Select **Allow business users to use this destination**.

   This allows users who have been assigned to the **Amp360 User** and/or **AmpIQ User** policies to use this destination with orchestrations and/or campaigns.
#. Select **Allow business users with limited PII access to send data**.

   This allows users who have been assigned to the **Restrict PII access** policy option to use this destination with orchestrations and/or campaigns.
#. Click **Save**.

.. destinations-add-destinations-webhook-end


**Add data template**


.. Use the following intro for configuring data templates for any email service provider (ESP) or any other destination that supports only email address lists.

.. destinations-add-data-template-overview-campaigns-email-only-start

You can configure Amperity to send campaign results. These results are sent from the **Campaigns** tab and may only contain a list of email addresses.

.. destinations-add-data-template-overview-campaigns-email-only-end


.. Use the following intro for configuring data templates for all Amazon S3, Microsoft Azure, Google Cloud Storage, and SFTP destinations THAT ARE USED WITH CAMPAIGNS. You can pick additional attributes for any campaign that sends to those types of destinations.

.. destinations-add-data-template-overview-campaigns-email-plus-start

You can configure Amperity to |channel-link|. These results are sent from the **Campaigns** tab. Results default to a list of email addresses, but you may configure a campaign to send |email-plus-send| to |destination-name|.

.. destinations-add-data-template-overview-campaigns-email-plus-end


.. Use the following intro for configuring data templates for all Amazon S3, Microsoft Azure, Google Cloud Storage, and SFTP destinations THAT ARE USED WITH ORCHESTRATIONS. You specify the fields in the query, and then send all query results.

.. destinations-add-data-template-overview-file-orchestrations-start

You can configure Amperity to |sendto-link|. These results are sent using an orchestration and will include all columns that were specified in the query.

.. destinations-add-data-template-overview-file-orchestrations-end

.. destinations-add-data-template-overview-webhook-orchestrations-start

You can configure Amperity to |sendto-link|. These results are sent using an orchestration and will include all columns that were specified in the query.

.. destinations-add-data-template-overview-webhook-orchestrations-end

.. destinations-add-data-template-overview-api-orchestrations-start

You can configure Amperity to |sendto-link|. These results are sent using an orchestration.

.. destinations-add-data-template-overview-api-orchestrations-end



























DESTINATIONS
DESTINATIONS
DESTINATIONS

.. TODO: This is the sections for the templated content for adding destinations in /datagrid/. These sections allow for bespoke steps, usually as Step 4, but may have more if they are more complicated. Try to keep the bespoke content within Step xxxxxx as much as possible for consistency.

.. TODO: This is Step 1. Contains variable for image, in case it is necessary to customize.

.. destinations-add-destination-start

Open the **Destinations** tab to configure a destination for |destination-name|. Click the **Add Destination** button to open the **Destination** dialog box.

.. destinations-add-destination-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

.. destinations-add-name-and-description-start

Enter a name for the destination and provide a description. For example: "|destination-name|" and "This sends |what-send| to |destination-name|".

From the **Plugin** drop-down, start typing |filter-the-list| to filter the list, and then select |destination-name|.

.. destinations-add-name-and-description-end


.. TODO: This is Step 2; add credentials or use existing

.. destinations-add-credentials-start

Credentials allow Amperity to connect to |destination-name|.

The credential type is set automatically. You may use an existing credential or you may add a new one.

.. destinations-add-credentials-end

.. destinations-add-credentials-sftp-start

Credentials allow Amperity to connect to |destination-name|.

The credential type is set automatically to |sftp-type|. You may use an existing credential or you may add a new one.

.. destinations-add-credentials-sftp-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

.. destinations-add-new-or-select-existing-start

Select an existing credential from the **Credential** drop-down.

-- or -- 

Select **Create a new credential** from the **Credential** drop-down. This opens the **Credential** dialog box.

.. destinations-add-new-or-select-existing-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

.. destinations-intro-for-additional-settings-start

Enter the name for the credential, and then add a description.

.. destinations-intro-for-additional-settings-end

.. destinations-intro-for-additional-settings-oauth-start

.. admonition:: Steps to configure OAuth

   #. Generate an authorization link, and then visit the URL that was generated to complete the authorization process.
   #. Log in to |destination-name| at the generated URL using credentials that allow access to your instance of |destination-name|.

      .. note:: Send the URL to an individual who can provide these credentials, and then ask them to log into |destination-name| on your behalf.

   #. When complete, you will be redirected to the **Credentials** page in Amperity.
   #. Verify the credential is on the page, and then return to the **Destinations** tab. From the **Plugin** drop-down, select the |destination-name|, and then use the credential that was just created.

.. destinations-intro-for-additional-settings-oauth-end


.. destinations-intro-for-additional-settings-oauth-refresh-token-start

.. admonition:: Steps to configure OAuth

   #. Generate an authorization link, and then visit the URL that was generated to complete the authorization process.
   #. Log in to |destination-name| at the generated URL using credentials that allow access to your instance of |destination-name|.

      .. note:: Send the URL to an individual who can provide these credentials, and then ask them to log into |destination-name| on your behalf.

   #. When complete, you will be redirected to the **Credentials** page in Amperity.
   #. Verify the credential is on the page, and then return to the **Destinations** tab. From the **Plugin** drop-down, select the |destination-name|, and then use the credential that was just created.

      .. note:: The value for the **Refresh Token** setting will be updated automatically after you select the credential.

.. destinations-intro-for-additional-settings-oauth-refresh-token-end


.. destinations-intro-for-additional-settings-sftp-start

Enter the name for the credential, and then add a description. Select |sftp-hostname| from the **HOSTNAME** drop-down list. Enter the username and passphrase.

.. destinations-intro-for-additional-settings-sftp-end

.. TODO: For some connectors, we'll use "After the credential is saved you will need to provide additional settings for this destination." but only if there are additional settings.

.. TODO: What follows here is bespoke for most destinations, except for the "When finished, click save" bit.

.. destinations-save-settings-start

When finished, click **Save**.

.. destinations-save-settings-end


.. TODO: This is Step 3; add credentials or use existing

.. destinations-destination-settings-start

Each destination has settings that define how Amperity will deliver data to |destination-name|. These settings are listed under the **Settings** section of the **Destination** dialog box.

.. destinations-destination-settings-end

.. TODO: There is an image here that ideally is bespoke.

.. TODO: The following section is used *only* with SFTP connectors. It consolidates all of the common settings. If there is a unique setting for a specific connector, just add it to the topic LAST in the list so we can continue to reuse the common settings.


SETTINGS FOR SFTP DESTINATIONS ONLY

.. destinations-destination-settings-sftp-start

Complete the following **SFTP Settings**:

* The path to the **Remote folder**.

   .. tip:: If the path to the remote folder contains a space, use a backslash (\) character to escape that space. For example, a folder named "From ACME" should be entered as "From\\ ACME".

* The **File format**. Select the file format -- |file-format| -- from the drop-down list.

* Optional. The **Escape character** that is required by |destination-name|.

  .. note:: If an escape character is not specified *and* quote mode is set to "None" this may result in unescaped, unquoted files. When an escape character is not specified, you should select a non-"None" option from the **Quote Mode** setting.

* Optional. The **Compression** format. |encoding-method|

* Optional. The **PGP public key** that is used to encrypt files that are sent to |destination-name|.

* Optional. The **Quote mode** that should be used within the file. From the drop-down, select one of "all fields", "all non-NULL fields", "fields with special characters only", "all non-numeric fields" or "None".

  .. note:: If the quote mode is set to "None" *and* the **Escape Character** setting is empty this may result in unescaped, unquoted files. When quote mode is not set to "None", you should specify an escape character.

* Optional. Select **Include success file upon completion** to add a .DONE file that indicates when an orchestration has finished sending data.

   .. tip:: If a downstream sensor is listening for files sent from Amperity, configure that sensor to listen for the presence of the .DONE file.

* Optional. Select **Include header row in output files** if headers should be included in the output.

* Optional. Select **Row number** to include a row number column in the output file. Applies to CSV, TSV, PSV, and custom delimiter file types.

  When enabled, you may specify the name of the row number column in the output file.

* Optional. Select **Exclude Parquet extension from the directory name** for managing how |format_parquet_directories| are added to directories.

.. destinations-destination-settings-sftp-end


SETTINGS FOR GOOGLE CLOUD STORAGE DESTINATIONS ONLY

.. destinations-destination-settings-google-cloud-storage-start

Complete the following **SFTP Settings**:

* The **Object prefix**.

   The object prefix is a string that is used to filter results to include only objects whose names begin with this prefix. When this value is set, the names of objects that may be returned in the response are relative to the root of the bucket.

* The **File format**. Select the file format -- |file-format| -- from the drop-down list.

* Optional. The **Escape character** that is required by |destination-name|.

  .. note:: If an escape character is not specified *and* quote mode is set to "None" this may result in unescaped, unquoted files. When an escape character is not specified, you should select a non-"None" option from the **Quote Mode** setting.

* Optional. The **Compression** format. |encoding-method|

* Optional. The **PGP public key** that is used to encrypt files that are sent to |destination-name|.

* Optional. The **Quote mode** that should be used within the file. From the drop-down, select one of "all fields", "all non-NULL fields", "fields with special characters only", "all non-numeric fields" or "None".

  .. note:: If the quote mode is set to "None" *and* the **Escape Character** setting is empty this may result in unescaped, unquoted files. When quote mode is not set to "None", you should specify an escape character.

* Optional. Select **Include success file upon completion** to add a .DONE file that indicates when an orchestration has finished sending data.

   .. tip:: If a downstream sensor is listening for files sent from Amperity, configure that sensor to listen for the presence of the .DONE file.

* Optional. Select **Include header row in output files** if headers should be included in the output.

* Optional. Select **Row number** to include a row number column in the output file. Applies to CSV, TSV, PSV, and custom delimiter file types.

  When enabled, you may specify the name of the row number column in the output file.

* Optional. Select **Exclude Parquet extension from the directory name** for managing how |format_parquet_directories| are added to directories.

.. destinations-destination-settings-google-cloud-storage-end


SETTINGS FOR AMAZON S3 DESTINATIONS ONLY

.. destinations-destination-settings-amazon-s3-start

Complete the following **Amazon S3 Settings**:

* The **S3 prefix**.

   The S3 prefix is a string that is used to filter results to include only objects whose names begin with this prefix. When this value is set, the names of objects that may be returned in the response are relative to the root of the bucket.

* The **File format**. Select the file format -- |file-format| -- from the drop-down list.

* Optional. The **Escape character** that is required by |destination-name|.

  .. note:: If an escape character is not specified *and* quote mode is set to "None" this may result in unescaped, unquoted files. When an escape character is not specified, you should select a non-"None" option from the **Quote Mode** setting.

* Optional. The **Compression** format. |encoding-method|

* Optional. The **PGP public key** that is used to encrypt files that are sent to |destination-name|.

* Optional. The **Quote mode** that should be used within the file. From the drop-down, select one of "all fields", "all non-NULL fields", "fields with special characters only", "all non-numeric fields" or "None".

  .. note:: If the quote mode is set to "None" *and* the **Escape Character** setting is empty this may result in unescaped, unquoted files. When quote mode is not set to "None", you should specify an escape character.

* Optional. Select **Include success file upon completion** to add a .DONE file that indicates when an orchestration has finished sending data.

   .. tip:: If a downstream sensor is listening for files sent from Amperity, configure that sensor to listen for the presence of the .DONE file.

* Optional. Select **Include header row in output files** if headers should be included in the output.

* Optional. Select **Row number** to include a row number column in the output file. Applies to CSV, TSV, PSV, and custom delimiter file types.

  When enabled, you may specify the name of the row number column in the output file.

* Optional. Select **Exclude Parquet extension from the directory name** for managing how |format_parquet_directories| are added to directories.

.. destinations-destination-settings-amazon-s3-end



SETTINGS FOR AZURE BLOB STORAGE DESTINATIONS ONLY

.. destinations-destination-settings-azure-blob-storage-start

Complete the following **Azure Blob Storage Settings**:

* The **Container** and **Blob prefix**.

   The name of the container and blob prefix. For example: |azure-container-name| and |azure-blob-prefix|.

* The **File format**. Select the file format -- |file-format| -- from the drop-down list.

* Optional. The **Escape character** that is required by |destination-name|.

  .. note:: If an escape character is not specified *and* quote mode is set to "None" this may result in unescaped, unquoted files. When an escape character is not specified, you should select a non-"None" option from the **Quote Mode** setting.

* Optional. The **Compression** format. |encoding-method|

* Optional. The **PGP public key** that is used to encrypt files that are sent to |destination-name|.

* Optional. The **Quote mode** that should be used within the file. From the drop-down, select one of "all fields", "all non-NULL fields", "fields with special characters only", "all non-numeric fields" or "None".

  .. note:: If the quote mode is set to "None" *and* the **Escape Character** setting is empty this may result in unescaped, unquoted files. When quote mode is not set to "None", you should specify an escape character.

* Optional. Select **Include success file upon completion** to add a .DONE file that indicates when an orchestration has finished sending data.

   .. tip:: If a downstream sensor is listening for files sent from Amperity, configure that sensor to listen for the presence of the .DONE file.

* Optional. Select **Include header row in output files** if headers should be included in the output.

* Optional. Select **Row number** to include a row number column in the output file. Applies to CSV, TSV, PSV, and custom delimiter file types.

  When enabled, you may specify the name of the row number column in the output file.

* Optional. Select **Exclude Parquet extension from the directory name** for managing how |format_parquet_directories| are added to directories.

.. destinations-destination-settings-azure-blob-storage-end




.. TODO: This is Step "Business Users"; these are the same everywhere.

.. destinations-business-users-start

Business users are assigned to the **Amp360 User** and/or **AmpIQ User** policies. (**Amp360 User** allows access to queries and orchestrations and **AmpIQ User** allows access to segments and campaigns.) A business user cannot select a destination that is not visible to them.

Business users -- including users assigned to the **DataGrid Operator** policy -- may have restricted access to PII.

.. destinations-business-users-end

.. destinations-business-users-admonition-start

.. admonition:: What is restricted access to PII?

   Restricted PII access is enabled when the **Restrict PII access** policy option that prevents users who are assigned to that option from viewing data that is marked as PII anywhere in Amperity and from sending that data to any downstream workflow.

.. destinations-business-users-admonition-end

.. destinations-business-users-enable-start

You can make this destination visible to orchestrations *and* allow users with restricted access to PII to use this destination by enabling one (or both) of the following options:

.. image:: ../../images/mockup-destinations-tab-add-04-allow-access.png
   :width: 500 px
   :alt: Allow business users access to this destination.
   :align: left
   :class: no-scaled-link

.. destinations-business-users-enable-end

.. destinations-business-users-allow-start

.. note:: To allow business users to use this destination with campaigns, you must enable the **Available to campaigns** option within the data template. This allows users to send campaign results from Amperity to |destination-name|.

   The other two settings may be configured within the data template instead of the destination.

.. destinations-business-users-allow-end


.. TODO: This is Step "Save"; these are the same everywhere.

.. destinations-save-start

Review all settings, and then click **Save**.

.. image:: ../../images/mockup-destinations-tab-add-05-save.png
   :width: 500 px
   :alt: Save the destination.
   :align: left
   :class: no-scaled-link

.. important:: You must configure a data template for this destination before you can send data to |destination-name|.

.. destinations-save-end








DATA TEMPLATES
DATA TEMPLATES
DATA TEMPLATES

.. TODO: This is the sections for the templated content for adding data templates to destinations in /datagrid/. These sections allow for bespoke steps, usually as Step 4, but may have more if they are more complicated. Try to keep the bespoke content within Step 4 as much as possible for consistency.


.. TODO: This is Step 1. Contains variable for image, in case it is necessary to customize.

.. destinations-data-template-open-template-start

From the **Destinations** tab, open the menu for a destination that is configured for |destination-name|, and then select **Add data template**.

This opens the **Add Data Template** dialog box.

.. destinations-data-template-open-template-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

.. destinations-data-template-open-template-name-start

Enter the name of the data template and a description. For example: "|data-template-name|" and "|data-template-description|".

.. destinations-data-template-open-template-name-end


.. TODO: This is Step 2; the 2nd section can be removed for destinations that are not usable with campaigns.

.. destinations-data-template-business-users-start

Verify business user access to queries and orchestrations and access to segments and campaigns.

A business user may also have restricted access to PII, which prevents them from viewing and sending customer profile data.

.. destinations-data-template-business-users-end

.. TODO: There is an image here that should mostly be static across destination topics, but it's customizable if necessary.

.. destinations-data-template-business-users-access-not-configured-start

If business user access was not configured as part of the destination, you may configure access from the data template.

.. destinations-data-template-business-users-access-not-configured-end

.. destinations-data-template-business-users-allow-campaigns-start

.. important:: To allow business users to use this destination with campaigns, you must enable the **Available to campaigns** option. This allows users to send campaign results from Amperity to |destination-name|.

   If you enable this option, the data extension settings require using campaign name and group name template variables to associate the name of the data extension to your campaign.

.. destinations-data-template-business-users-allow-campaigns-end


.. TODO: This is Step 3. Contains variable for image, in case it is necessary to customize.

.. destinations-data-template-verify-config-settings-start

Verify all configuration settings.

.. destinations-data-template-verify-config-settings-end

.. TODO: There is an image here that SHOULD BE CUSTOMIZED

.. TODO: The following block has a WERE / IS and IT / THEY configuration requirement. Be watchful.

.. destinations-data-template-verify-config-settings-note-start

.. note:: When the |data-template-config-settings-list| are not configured as part of the destination, you must configure |data-template-config-settings-list-them-vs-it| as part of the data template before making this destination available to campaigns.

.. destinations-data-template-verify-config-settings-note-end


.. TODO: This is Step 4. Note that there is no templated Step 4 because these are often very specific.

.. TODO: In some cases, the data templates are sparse enough to also skip step 3 (review settings) and just jump straight to the below section. Zendesk, for example.

.. destinations-data-template-save-start

Review all settings, and then click **Save**.

.. destinations-data-template-save-end

.. TODO: There is an image here that should probably be the same everywhere.

.. destinations-data-template-save-after-start

After you have saved the data template, and depending on how you configured it, business users can |sendto-link| and/or |channel-link| to |destination-name|.

.. destinations-data-template-save-after-end

.. destinations-data-template-save-after-queries-only-start

After you have saved the data template, and depending on how you configured it, business users can |sendto-link| to |destination-name|.

.. destinations-data-template-save-after-queries-only-end
