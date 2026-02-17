.. 
.. shared settings for destinations
.. 


.. vale off

**LOREM IPSUM**

.. TODO: Placeholder content for testing and validation.

.. setting-lorem-ipsum-long-start

Lorem ipsum dolor sit amet, duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. setting-lorem-ipsum-long-end

.. setting-lorem-ipsum-short-start

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. setting-lorem-ipsum-short-end

.. setting-lorem-ipsum-alt-start

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

.. setting-lorem-ipsum-alt-end

.. vale on



**Steps**

**Step 01a**

.. destinations-steps-add-destinations-start

Open the **Destinations** page, select the **New destinations** button, and then select **Orchestration**.

.. destinations-steps-add-destinations-end

.. campaigns-steps-add-destinations-start

Open the **Destinations** page, select the **New destinations** button, and then select **Campaign**.

.. campaigns-steps-add-destinations-end

**Step 01b**

.. destinations-steps-add-destinations-select-start

To configure a destination for |destination-name|, do one of the following:

#. Click the row in which |destination-name| is located. Destinations list alphabetically and you can scroll up and down the list.
#. Search for |destination-name|. Start typing |filter-the-list|. The list filters to show only matching destinations. Select |plugin-name|.

.. destinations-steps-add-destinations-select-end

.. campaigns-steps-add-destinations-select-start

To configure a campaign for |destination-name|, do one of the following:

#. Click the row in which |destination-name| is located. Destinations list alphabetically and you can scroll up and down the list.
#. Search for |destination-name|. Start typing |filter-the-list|. The list filters to show only matching destinations. Select |plugin-name|.

.. campaigns-steps-add-destinations-select-end

**Step 02a**

.. destinations-steps-select-credential-start

Select the credential for |destination-name| from the **Credential** dropdown, and then click **Continue**.

.. destinations-steps-select-credential-end

.. campaigns-steps-select-credential-start

Select the credential for |destination-name| from the **Credential** dropdown, and then click **Continue**.

.. campaigns-steps-select-credential-end

**Step 02b**

.. destinations-steps-test-connection-start

If there are any issues with destination connectivity, an error message will display in the destination setup dialog. If the destination saves successfully, the connection is ready for use. 

.. destinations-steps-test-connection-end

.. campaigns-steps-test-connection-start

If there are any issues with destination connectivity, an error message will display in the destination setup dialog. If the destination saves successfully, the connection is ready for use. 

.. campaigns-steps-test-connection-end

**Step 03**

.. destinations-steps-name-and-description-start

In the "Destination settings" dialog box, assign the destination a name and description that ensures other users of Amperity can recognize when to use this destination.

.. destinations-steps-name-and-description-end

.. campaigns-steps-name-and-description-start

In the "Destination settings" dialog box, assign the destination a name and description that ensures other users of Amperity can recognize when to use this destination.

.. campaigns-steps-name-and-description-end

**Step 04**

.. destinations-steps-settings-start

Configure the following settings, and then click "Save".

.. destinations-steps-settings-end

.. campaigns-steps-settings-start

Configure the following settings, and then click "Save".

.. campaigns-steps-settings-end

.. campaigns-steps-campaign-settings-start

Under **Campaign settings** select one of the following:

* **Send audience list as separate files**

  This option sends a standalone file for each treatment group sending an audience to |destination-name|.

* **Send audience lists as a single file**

  This option consolidates all treatment groups into a single file before sending the audience to |destination-name|.

.. campaigns-steps-campaign-settings-end

**Step 05**

.. destinations-steps-business-users-start

After configuring this destination users may use:

* Orchestrations to send query results
* Orchestrations and campaigns to send audiences
* Orchestrations and campaigns to send events

.. destinations-steps-business-users-end

.. destinations-steps-business-users-orchestration-only-start

After configuring this destination users may use orchestrations to send query results |destination-name|.

.. destinations-steps-business-users-orchestration-only-end

.. campaigns-steps-business-users-start

After configuring this destination users may send campaigns to |destination-name|.

.. campaigns-steps-business-users-end

.. campaigns-steps-business-users-orchestration-only-start

After configuring this destination users may send campaigns to |destination-name|.

.. campaigns-steps-business-users-orchestration-only-end


**Step 06**

.. destinations-steps-validate-audience-start

Test the connection with |destination-name| by using an audience with a very small membership. For example: 10 or 100 members or the minimum audience size recommended by |destination-name|. Send the test audience to |destination-name| and verify the audience is correct in |destination-name|. Make adjustments if necessary. Only send full audiences after validation is complete.

.. destinations-steps-validate-audience-end



.. vale off

**COMMON API**

.. vale on

Details common to API-based destinations.

**API allow-for note**

.. allow-for-start

Changes to |allow-for-what| are not immediately available in |destination-name|. Allow for |allow-for-duration| after the point at which Amperity has finished sending audience updates for them to be available.

.. allow-for-end



.. vale off

**COMMON**

.. vale on

Settings across more than one destination.

.. TODO: Compare Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP for common settings.

**Audience primary key**

Applies to: ActiveCampaign, Cordial, Criteo, HubSpot, Klaviyo, Listrak, Microsoft Ads, Oracle Eloqua, Pinterest, and Sailthru. Must set the ``|audience-primary-key|`` variable in the destination file.

.. setting-common-audience-primary-key-start

The primary key for the audience. Set to |audience-primary-key|.

.. setting-common-audience-primary-key-end

**Business user access**

Applies to: all destinations.

.. TODO: These two settings are in an admonition block in docs pages. Definition list in modals.

.. setting-common-business-user-access-allow-start

By default a destination is available to all users who have permission to view personally identifiable information (PII).

Enable the **Admin only** checkbox to restrict access to only users assigned to the **Datagrid Operator** and **Datagrid Administrator** policies.

Enable the **PII setting** checkbox to allow limited access to PII for this destination.

.. setting-common-business-user-access-allow-end

.. setting-common-business-user-access-restrict-pii-start

Use the **Restrict PII access** policy option to prevent users from viewing data marked as PII anywhere in Amperity and from sending data to downstream workflows.

.. setting-common-business-user-access-restrict-pii-end

**Compression**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-compression-start

The compression format to apply to the file. May be one of "GZIP", "None", "TAR", "TGZ", or "ZIP". 

.. setting-common-compression-end

**Configure** in intro

.. setting-common-file-configure-start

Configure Amperity to send |what-send| to |where-send|.

.. setting-common-file-configure-end

**Delimiter**

.. setting-common-delimiter-start

The custom character to use as a delimiter within the output file.

.. setting-common-delimiter-end

**Escape character**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-escape-character-start

The escape character to use in the file output. Applies to CSV, TSV, PSV, and custom delimiter file types.

.. setting-common-escape-character-end

.. vale off

.. setting-common-escape-character-unspecified-start

When an escape character is not specified *and* the quote mode is "None" files are sent with unescaped and unquoted data. When an escape character is not specified, you should select a non-"None" option as the quote mode.

.. setting-common-escape-character-unspecified-end

.. vale on


**File format**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-file-format-start

Configure Amperity to send |what-send| to |where-send|.

.. setting-common-file-format-end

.. setting-common-file-format-custom-delimiter-start

Some file formats allow a custom delimiter. Choose the "Custom delimiter" file format, and then add a single character to represent the custom delimiter.

.. setting-common-file-format-custom-delimiter-end

.. vale off

.. setting-common-file-format-apache-parquet-start

The extension for Apache Parquet files may be excluded from the directory name.

.. setting-common-file-format-apache-parquet-end

.. vale on


**Filename template**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. include:: ../../shared/terms.rst
   :start-after: .. term-filename-template-start
   :end-before: .. term-filename-template-end

**Get details** common intro

.. setting-common-get-details-start

Review the following details before configuring credentials for |destination-name| and before configuring Amperity to send |what-send| to |where-send|.

.. setting-common-get-details-end

.. setting-common-get-details-file-specific-start

Review file-specific details to ensure correct configuration for all files sent from Amperity to downstream workflows. For example, configure Apache Parquet to exclude the extension from the directory name. Some files require specific escape characters and others may have unique delimiters.

Each file sent from Amperity has its own unique requirements.

.. setting-common-get-details-file-specific-end

**Header**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-header-start

Enable to include header rows in output files.

.. setting-common-header-end

**Line ending**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-line-ending-start

The line ending to use in file output. May be one of "LF" or "CRLF".

.. setting-common-line-ending-end

**List name**

Applies to ActiveCampaign, Cordial, HubSpot, Klaviyo, Listrak and others. Try to come up with a template.

.. setting-common-list-name-start

The name of the list managed by Amperity.

.. setting-common-list-name-end

**Membership duration**

Applies to Amazon Ads, Google Ads, Google Customer Match, The Trade Desk, Yahoo DSP.

.. vale off

.. setting-common-membership-duration-start

The length of time |duration|, after which a customer is removed from this audience. This value may be between |duration-value|. Set this value to "0" to remove all audience members.

.. setting-common-membership-duration-end

.. vale on


.. setting-common-membership-duration-frequency-start

To ensure customers stay in this audience ensure the frequency at which Amperity sends the audience to |destination-name| is less than the membership duration.

.. setting-common-membership-duration-frequency-end

**Name and description**

.. setting-common-name-and-description-start

The name and description for a destination.

.. setting-common-name-and-description-end

**Optional settings**

.. setting-common-optional-settings-start

All other Amperity file format settings for |destination-name| are optional.

.. setting-common-optional-settings-end

**Parquet extension**

Applies to: Apache Parquet files only.

.. setting-common-parquet-extension-start

Enable to remove the file extension from the directory name. Applies to Apache Parquet files only.

.. setting-common-parquet-extension-end

**PGP public key**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-pgp-public-key-start

The PGP public key that Amperity uses to encrypt files.

.. setting-common-pgp-public-key-end


**Quote mode**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-quote-mode-start

The quote mode to use within the file. May be one of "all fields", "all non-**NULL** fields", "fields with special characters only", "all non-numeric fields" or "None".

.. setting-common-quote-mode-end

.. setting-common-quote-mode-none-start

Unescaped, unquoted files may occur when quote mode is "None" and an escape character is not specified.

.. setting-common-quote-mode-none-end

**Remote folder**

Applies to: Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-remote-folder-start

The remote folder to which Amperity sends data.

.. setting-common-remote-folder-end

.. setting-common-remote-folder-forward-slash-start

Use a forward slash--"/"--as the first character for this value. For example: |remote-folder|.

.. setting-common-remote-folder-forward-slash-end

.. vale off
.. off because this sentence needs to show the escape character behavior and using a code block prevents that

.. setting-common-remote-folder-spaces-start

If the path to the remote folder has a space, use a backslash (\\) character to escape that space. For example, a folder named "From ACME" should be entered as "From\\ ACME".

.. setting-common-remote-folder-spaces-end

.. vale on

**Row Number**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP destinations.

.. setting-common-row-number-start

Select to include a row number column in the output file. Applies to CSV, TSV, PSV, and custom delimiter file types.

.. setting-common-row-number-end

.. setting-common-row-number-column-name-start

Use the **Column name** setting to specify the name of the row number column in the output file. The name of this column must have fewer than 1028 characters and may only contain numbers, letters, underscores, and hyphens. Default value: "row_number".

.. setting-common-row-number-column-name-end

**Sandbox**

.. setting-common-sandbox-recommendation-start

Use a sandbox to configure a destination for |destination-name|. Before promoting your changes, send a test audience, and then verify the results in |destination-name|. After verifying the end-to-end workflow, push the destination from the sandbox to production.

.. setting-common-sandbox-recommendation-end


**Split outputs**

.. setting-common-split-outputs-start

Split delimiter-separated output--CSV, PSV, TSV, or files with custom delimiters--into multiple files to ensure downstream file limits are not exceeded.

Choose "Rows" and set "Rows limit" to a value between "50000" and "10000000". This is the maximum number of rows for split output files.

Choose "Megabytes" and set "Megabytes limit" to a value between "1 MB" and "2000 MB". This is the maximum file size.

Additional configuration is required for filename templates.

Set the value of "Split filename template" to "{{file_number}}.csv" to apply a unique seven digit left-padded integer to the filename. For example: "0000001.csv", "0000002.csv", and "0000003.csv".

Use the "Split file directory template" to name the directory into which split files are added.

For example: if the value of "Split file directory template" is {{now|format:'YYYY'}}.tgz and the value of "Split filename template" is "{{file_number}}.csv" Amperity will output a gzipped tarball named "2025.tgz" with subfiles named "0000001.csv", "0000002.csv", and "0000003.csv".

.. setting-common-split-outputs-end


**Success file**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-success-file-start

Enable to send a ".DONE" file when Amperity has finished sending data.

.. setting-common-success-file-end

.. setting-common-success-file-downstream-start

If a downstream sensor is listening for files sent from Amperity, configure that sensor to listen for the presence of the ".DONE" file.

.. setting-common-success-file-downstream-end

**Use Zip64**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-use-zip64-start

Enable to apply Zip64 data compression to large files.

.. setting-common-use-zip64-end





.. vale off

**ACTIVECAMPAIGN**

.. vale on

Settings unique to ActiveCampaign.

**Audience primary key**

See common settings.

.. setting-active-campaign-email-required-start

A contact in |destination-name| is an email address. A contact may have more information, but cannot exist without an email address.

Use a query or a campaign to define the information in the email list managed by Amperity.

.. setting-active-campaign-email-required-end

**Group name**

.. setting-active-campaign-group-name-start

The name of the `user group <https://help.activecampaign.com/hc/en-us/articles/115000090164#setting-user-permissions-create-user-groups-0-0>`__ |ext_link| to which Amperity sends data. This group must exist in |destination-name| and must have permission to view and interact with the email list.

.. setting-active-campaign-group-name-end

.. setting-active-campaign-group-name-access-start

You must log into |destination-name| as a member of the specified user group to have access to the email list managed by Amperity.

.. setting-active-campaign-group-name-access-end

**List name**

.. setting-active-campaign-list-name-start

The name of an `email list <https://help.activecampaign.com/hc/en-us/articles/360000030559-How-to-create-a-list-in-ActiveCampaign>`__ |ext_link| in |destination-name| managed by Amperity.

.. setting-active-campaign-list-name-end

**Verbose logging**

.. setting-active-campaign-verbose-logging-start

Enable verbose logging to return log details when |destination-name| rejects adding contacts to the email list.

A list of rejected contacts returned by the response from ActiveCampaign lists each rejected contact with a contact identifier and a string that describes the rejection.

.. setting-active-campaign-verbose-logging-end





.. vale off

**ACXIOM**

.. vale on

See SFTP.





.. vale off

**ADOBE CAMPAIGN**

.. vale on

See SFTP.




.. vale off

**ADOBE COMMERCE**

.. vale on

Not a destination.





.. vale off

**ADOBE CUSTOMER ATTRIBUTES**

.. vale on

See SFTP.





.. vale off

**ADOBE EXPERIENCE CLOUD**

.. vale on

See SFTP.





.. vale off

**ADOBE MARKETO**

.. vale on

Settings unique to Adobe Marketo.

**Folder name**

.. setting-adobe-marketo-folder-name-start

Required. The name of the folder in |destination-name| in which a program that has the audience list is located.

.. setting-adobe-marketo-folder-name-end

**List name**

.. setting-adobe-marketo-list-name-start

Required. The name of the audience list managed by Amperity.

.. setting-adobe-marketo-list-name-end

.. setting-adobe-marketo-list-name-first-audience-start

It is possible for Adobe Marketo to contain many audience lists with the same name. If the Adobe Marketo API returns more than one audience list, Amperity updates the first audience in that list.

.. setting-adobe-marketo-list-name-first-audience-end

.. setting-adobe-marketo-list-name-membership-start

Amperity uses the |destination-name| API to update the membership of audience lists in |destination-name| to match the membership of audience lists sent from Amperity. The membership updates to match the membership of the audience list sent from Amperity. Amperity adds a user when they do not exist in |destination-name|.

Amperity does not keep smart lists and does not remove users from the |destination-name| database.

.. setting-adobe-marketo-list-name-membership-end

.. setting-adobe-marketo-list-name-limitations-start

|destination-name| API `has the following limitations <https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/marketo-integration-best-practices#>`__ |ext_link|:

* Subscriptions can make up to 50,000 API calls per day. This resets daily at 12:00 AM, Central Standard Time.
* API access is rate limited to 100 calls per 20 seconds, with up to 10 concurrent API calls.

You may experience these rate limits when sending large audience lists.

It is possible for |destination-name| to have many audience lists with duplicate names. If the |destination-name| API returns more than one audience list, Amperity updates the first audience list in that list.

.. setting-adobe-marketo-list-name-limitations-end

**Program name**

.. setting-adobe-marketo-program-name-start

The name of the program in which the audience list managed by Amperity is located.

.. setting-adobe-marketo-program-name-end




.. vale off

**ADOBE TARGET**

.. vale on

Settings unique to Adobe Target.

**Identifier type**

.. setting-adobe-target-identifier-start

The identifier type for individual profiles in the |destination-name| profile store. The first column in the dataset sent to |destination-name| must have a header that matches the name of the selected identifier type.

.. setting-adobe-target-identifier-end

**thirdPartyId** (identifier type)

.. setting-adobe-target-identifier-thirdpartyid-start

The **thirdPartyId** is a persistent identifier that uniquely identifies visitors to a website, mobile app, social media platform, and other cross-channel locations to which your customers log in. For example, a loyalty ID, a membership number, a web account ID, or some other identifier that is not personally identifiable information (PII) or sensitive information. Every call made to the |destination-name| profile store must use the **thirdPartyId**.

.. setting-adobe-target-identifier-thirdpartyid-end

**pcId** (identifier type)

.. setting-adobe-target-identifier-pcid-start

The **pcId** is an internal identifier generated automatically by |destination-name|. It is tied to the visitor's browser **mboxPC** cookie and is the source of truth for profile storage on a single device, single browser, or other cookie location. A single visitor can have many **pcId** identifiers.

.. setting-adobe-target-identifier-pcid-end


.. vale off

**AIRSHIP**

.. vale on

See SFTP.





.. vale off

**AMAZON ADS**

.. vale on

Settings unique to Amazon Ads.

**AMC instance**

.. setting-amazon-ads-amc-instance-start

The `instance within Amazon Marketing Cloud <https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/how-amc-works>`__ |ext_link| to which your brand sends audiences.

.. setting-amazon-ads-amc-instance-end

**Audience description**

.. setting-amazon-ads-audience-description-start

A description of the audience managed by Amperity.

.. setting-amazon-ads-audience-description-end

**Audience name**

.. setting-amazon-ads-audience-description-start

The name of the audience managed by Amperity. Amperity creates a new audience if an audience in |destination-name| does not match exactly the name of the one sent from Amperity.

.. setting-amazon-ads-audience-description-end

**DSP advertiser**

.. setting-amazon-ads-dsp-advertiser-start

The name of the DSP advertiser within |destination-name|.

.. setting-amazon-ads-dsp-advertiser-end

**Membership duration**

.. setting-amazon-ads-membership-duration-start

The length of time |duration|, after which a customer is removed from this audience. This value may be between |duration-value|.

.. setting-amazon-ads-membership-duration-end






.. vale off

**AMAZON S3**

.. vale on

Settings unique to Amazon S3.

Applies to: Amazon S3, Cheetah Digital, Domo, Optimizely.

.. setting-amazon-s3-about-start

Amazon Simple Storage Service--|destination-name|--can store data files of any size for any file format supported by Amperity.

.. setting-amazon-s3-about-end

**Compression**

See Common.

**Delimiter**

See Delimiter.

**Escape character**

See Common.

**File format**

See Common. Including Parquet extension.

**Filename template**

See Common.

**Header?**

See Common.

**PGP public key**

See Common.

**Quote mode**

See Common.

**S3 prefix**

.. setting-amazon-s3-prefix-start

Required. The S3 prefix is a string used to filter results to include only objects whose names begin with this prefix. When set, this value returns a list of object names relative to the root of the bucket.

.. setting-amazon-s3-prefix-end

**Success file**

See Common.

**Use Zip64?**

See Common.





.. vale off

**ATTENTIVE** (API + SFTP)

.. vale on

Settings unique to Attentive (API).

See SFTP for any common file settings.

**Client domain** (SFTP)

.. setting-attentive-client-domain-start

The client domain for your brand's instance of |destination-name|.

.. setting-attentive-client-domain-end

**Primary Identifier** (API)

.. setting-attentive-primary-identifier-start

The primary identifier used within your |destination-name| account. May be one of the following: "email" or "phone".

.. setting-attentive-primary-identifier-end

.. setting-attentive-primary-identifier-context-start

|destination-name| accepts email addresses *or* phone numbers as the primary identifier. The set of data sent from Amperity **must** contain the primary identifier. For example, if your primary identifier is phone numbers, than include the **phone** field.

You may send the non-primary email address or phone number as a custom attribute.

.. setting-attentive-primary-identifier-context-end

**Segment name** (SFTP)

.. setting-attentive-segment-name-start

The name of the segment in |destination-name| managed by Amperity.

.. setting-attentive-segment-name-end





.. vale off

**AZURE BLOB STORAGE**

.. vale on

Settings unique to Azure Blob Storage.

Applies to: Azure Blob Storage.

.. setting-azure-blob-storage-about-start

Microsoft |destination-name| can store data files of any size for any file format supported by Amperity.

.. setting-azure-blob-storage-about-end

**Blob prefix**

.. setting-azure-blob-storage-blob-prefix-start

A prefix filters the list of `blob storage objects <https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-list#filter-results-with-a-prefix>`__ |ext_link| to only blob names that match the prefix value within your instance of |destination-name|. A prefix may be a character or a string.

.. setting-azure-blob-storage-blob-prefix-end

**Compression**

See Common.

**Delimiter**

See Delimiter.

**Escape character**

See Common.

**File format**

See Common. Including Parquet extension.

**Filename template**

See Common.

**Header?**

See Common.

**PGP public key**

See Common.

**Quote mode**

See Common.

**Success file**

See Common.

**Use Zip64?**

See Common.





.. vale off

**BAZAARVOICE**

.. vale on

See SFTP.





.. vale off

**BLUECORE**

.. vale on

See SFTP.

**Header**

.. setting-bluecore-header-start

|destination-name| requires a header row to be present in |what-send|. The header row cannot start with a number or contain any special characters other than underscores ``_`` and must be less than 30 characters in length.

|destination-name| recommends the following file naming convention: "<company_name>_<data_type>_<date>.csv".

Consider naming queries sent to the |destination-name| platform in a way that satisfies the "<company_name>_<data_type>" part of the recommended naming pattern.

.. setting-bluecore-header-end




.. vale off

**BRAZE**

.. vale on

Settings unique to Braze.

**Instance**

.. setting-braze-instance-start

Required. Select the `Braze instance <https://www.braze.com/docs/user_guide/administrative/access_braze/braze_instances>`__ |ext_link| for your account. May be one of "US-01", "US-02", "US-03", "US-04", "US-05", "US-06", "US-07", "US-08", "EU-01", or "EU-02".

.. setting-braze-instance-end

.. setting-braze-instance-example-start

For example, if your URL of |destination-name| is ``https://dashboard-03.braze.com``, the REST API endpoint is ``https://rest.iad-03.braze.com``, and the instance is "US-03".

.. setting-braze-instance-example-end

**User identifier**

.. setting-braze-user-identifier-start

The identifier to use for matching users in |destination-name|. May be "external_id" or "braze_id".

.. setting-braze-user-identifier-end

.. setting-braze-user-identifier-about-start

The `external_id <https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import/#importing-with-external-id>`__ |ext_link| is a unique identifier for your customers, such as the Amperity ID. The `braze_id <https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import/#importing-with-braze-id>`__ |ext_link| is a unique identifier for existing |destination-name| customers.

.. setting-braze-user-identifier-about-end

**Update existing profiles**

.. setting-braze-update-existing-profiles-start

Use the **Update existing profiles only?** option to `update only existing user profiles in Braze <https://www.braze.com/docs/api/objects_filters/user_attributes_object#update-existing-profiles-only>`__ |ext_link|. When this setting is not enabled a new user profile is created when a profile with a matching ``external_id`` value does not already exist.

.. setting-braze-update-existing-profiles-end





.. vale off

**CAMELOT SMM**

.. vale on

See SFTP.





.. vale off

**CORDIAL**

.. vale on

Settings unique to Cordial.

**Audience primary key**

See common.

**List name**

.. setting-cordial-list-name-start

The name of the list in |destination-name| managed by Amperity. Amperity creates the list when it does not exist.

.. setting-cordial-list-name-end

**Subscription status**

.. setting-cordial-subscription-status-start

Enable "Do not set subscription status automatically" to prevent subscriptions when "channels.email.subscribeStatus" is not set.

.. setting-cordial-subscription-status-end





.. vale off

**CRITEO**

.. vale on

Settings unique to Criteo.

**Advertiser ID**

.. setting-criteo-advertiser-id-start

The unique ID for the advertiser account in |destination-name| to which Amperity sends audiences.

.. setting-criteo-advertiser-id-end

**Audience name**

.. setting-criteo-audience-name-start

The name of the audience sent to |destination-name|.

.. setting-criteo-audience-name-end

**Audience primary key**

See common settings.




.. vale off

**CRITEO RETAIL MEDIA**

.. vale on

Settings unique to Criteo Retail Media.

**Account ID**

.. setting-criteo-account-id-start

The account ID for the account in |destination-name| to which Amperity sends audience segments.

.. setting-criteo-account-id-end

**Audience segment description**

.. setting-criteo-audience-segment-description-start

Optional. A description for the audience segment.

.. setting-criteo-audience-segment-description-end

**Retailer ID**

.. setting-criteo-retailer-id-start

The retailer ID associated with the account in |destination-name| to which Amperity sends audience segments.

.. setting-criteo-retailer-id-end

**Identifier type**

.. setting-criteo-identifier-type-start

The identifier type. The correct value depends on the campaign.

For offsite campaigns must be one of the following identifiers:

* Use "Email" to build audience segments using email addresses.
* Use "IdentityLink" to build audience segments using LiveRamp identity graph data.
* Use "UserIdentifier" to build audience segments using a unique identifier provided by your brand. The user identifier may be one of the following: "IDFA", "AAID", "LiveRamp ID", or "Criteo Cookie ID".

For onsite display campaigns choose the "CustomerID" identifier.

.. setting-criteo-identifier-type-end




.. vale off

**CROSS COUNTRY COMPUTER**

.. vale on

See SFTP.




.. vale off

**DATABRICKS**

.. vale on

Settings unique to Databricks.

**Catalog name**

.. setting-databricks-catalog-name-start

The catalog name to use for Databricks.

.. setting-databricks-catalog-name-end

**Schema name**

.. setting-databricks-schema-name-start

The schema name to use for Databricks.

.. setting-databricks-schema-name-end

**Table name**

.. setting-databricks-table-name-start

The table name to use for Databricks.

.. setting-databricks-table-name-end





.. vale off

**DOTDIGITAL**

.. vale on

Settings unique to Dotdigital.

**List name**

See common list name.

**Contact identifier type**

.. setting-dotdigital-contact-identifier-type-start

The primary identifier for matching contacts in |destination-name|. Use "email" for email campaigns. Use "mobile_number" for SMS campaigns.

.. setting-dotdigital-contact-identifier-type-end





.. vale off

**EPSILON ABACUS**

.. vale on

See SFTP.





.. vale off

**EPSILON CONVERSANT**

.. vale on

See SFTP.





.. vale off

**EPSILON TARGETING**

.. vale on

See SFTP.





.. vale off

**EXPERIAN**

.. vale on

See SFTP.





.. vale off

**GOOGLE ADS**

.. vale on

Settings unique to Google Ads.

**Audience description**

.. setting-google-ads-audience-description-start

A description of the audience managed by Amperity.

.. setting-google-ads-audience-description-end

**Audience name**

.. setting-google-ads-audience-name-start

The name of the audience in |destination-name| managed by Amperity. Amperity creates the audience if it does not exist.

.. setting-google-ads-audience-name-end

**Customer ID**

.. setting-google-ads-customer-id-start

The customer ID for your brand's |destination-name| account. This value must be 10 digits and may not contain dashes.

.. setting-google-ads-customer-id-end

**Membership duration**

See common.

.. setting-google-ads-membership-duration-start

Set this value to "10000" for unlimited audience membership.

.. setting-google-ads-membership-duration-end

**Mobile app ID**

.. setting-google-ads-mobile-app-id-start

When the value of "Upload key type" is "Mobile ID", the mobile ID for the iOS or Android app.

.. setting-google-ads-mobile-app-id-end

**Upload key type**

.. setting-google-ads-upload-key-type-start

The key to use for audience matching in |destination-name|. May be one of "Contact Info", "Mobile ID", or "User Id".

.. setting-google-ads-upload-key-type-end



.. vale off

**GOOGLE ANALYTICS 4 (GA4)** (destination)

.. vale on

Settings unique to Google Analytics 4 (GA4).

.. setting-google-analytics-xxxxx-start

.. TODO: Currently: None.

.. setting-google-analytics-xxxxx-end




.. vale off

**GOOGLE CLOUD STORAGE**

.. vale on

Settings unique to Google Cloud Storage.

Applies to: Google Cloud Storage.

.. setting-google-cloud-storage-about-start

|destination-name| can store data files of any size for any file format supported by Amperity.

.. setting-google-cloud-storage-about-end

**Compression**

See Common.

**Delimiter**

See Delimiter.

**Escape character**

See Common.

**File format**

See Common. Including Parquet extension.

**Filename template**

See Common.

**Header?**

See Common.

**Object prefix**

.. setting-google-cloud-storage-object-prefix-start

Required. The prefix for the name of the `cloud storage object <https://cloud.google.com/storage/docs/objects>`__ |ext_link| for your instance of |destination-name|.

.. setting-google-cloud-storage-object-prefix-end

**PGP public key**

See Common.

**Quote mode**

See Common.

**Remote folder**

See Common.

**Success file**

See Common.

**Use Zip64?**

See Common.





.. vale off

**GOOGLE CUSTOMER MATCH**

.. vale on

Settings unique to Google Customer Match.

**Audience description**

See Google Ads.

**Audience name**

See Google Ads.

**Customer ID**

See Google Ads.

**Customer product**

.. setting-google-customer-match-customer-product-start

The Google advertising product to which Amperity sends audiences. May be one of "Google Ads", "Display Video Advertiser", or "Display Video Partner".

.. setting-google-customer-match-customer-product-end

**Membership duration**

See common.

**Mobile app ID**

See Google Ads.

**Upload key type**

See Google Ads.





.. vale off

**GOOGLE ENHANCED CONVERSIONS**

.. vale on

Settings unique to Google Enhanced Conversions.

**Conversion action name**

.. setting-google-enhanced-conversions-action-name-start

The name of the conversion action.

.. setting-google-enhanced-conversions-action-name-end

**Customer ID**

.. setting-google-enhanced-conversions-customer-id-start

The Customer ID of the Google Enhanced Conversions account.

.. setting-google-enhanced-conversions-customer-id-end





.. vale off

**HUBSPOT**

.. vale on

Settings unique to HubSpot.

**Audience primary key**

See common settings.

**Dates / datetimes**

.. setting-hubspot-dates-and-datetimes-start

Attributes sent to |destination-name| with values for a specific day, month, and year `must be in UTC and formatted as ISO 8601 strings or as EPOCH-timestamps in milliseconds <https://developers.hubspot.com/docs/guides/api/crm/properties>`__ |ext_link|.

.. setting-hubspot-dates-and-datetimes-end


**Create contacts?**

.. setting-hubspot-create-contacts-start

Select **Create contacts** to create contacts in |destination-name| when they do not already exist. Existing contacts are updated when this setting is unselected.

.. setting-hubspot-create-contacts-end


**List name**

.. setting-hubspot-list-name-start

The list name to which Amperity sends contacts. This can be the name of an existing list or a new list.

.. setting-hubspot-list-name-end





.. vale off

**INFUTOR**

.. vale on

See SFTP.

**Escape character**

.. vale off

.. setting-infutor-escape-character-start

An escape character must be specified because |destination-name| requires removing quotations from files.

.. setting-infutor-escape-character-end

.. vale on


**Quote mode**

.. setting-infutor-quote-mode-start

Remove quotations from files. If an escape character is not specified and quote mode is "None", as required by |destination-name|, this may result in unescaped, unquoted files.

.. setting-infutor-quote-mode-end

**Public key**

.. setting-infutor-public-key-start

Use public key encryption to encrypt data that has PII before using SFTP to send it to |destination-name|.

.. setting-infutor-public-key-end





.. vale off

**KIBO**

.. vale on

See SFTP.





.. vale off

**KLAVIYO**

.. vale on

Settings unique to Klaviyo.

**Audience primary key**

See common settings.

**List name**

.. setting-klaviyo-list-name-start

The list name to which Amperity writes the audience list. This can be the name of an existing list or a new list.

.. setting-klaviyo-list-name-end

.. setting-klaviyo-list-name-note-start

|destination-name| supports up to 1000 lists and segments in your account at any given time.

.. setting-klaviyo-list-name-note-end

**Update contacts?**

.. setting-klaviyo-update-contacts-start

Send customer profile fields with an audience list, These fields are visible in |destination-name| from the "Customer Properties" section within individual profiles for members of that audience list.

.. setting-klaviyo-update-contacts-end





.. vale off

**KOUPON MEDIA**

.. vale on

See SFTP.





.. vale off

**LINKEDIN DMP**

.. vale on

Settings unique to LinkedIn DMP.

**Account ID**

.. setting-linkedin-dmp-account-id-start

The account ID for your |destination-name| account.

.. setting-linkedin-dmp-account-id-end

**Identifier type**

.. setting-linkedin-dmp-identifier-type-start

The name of the identifier type must be one of the following: 1) **email** 2) **firstname** and **lastname**. Including any other fields will return an error. Map the output of query results and segments before sending to LinkedIn.

.. setting-linkedin-dmp-identifier-type-end

**Segment description**

.. setting-linkedin-dmp-segment-description-start

A description of the audience segment.

.. setting-linkedin-dmp-segment-description-end

**Segment name**

.. setting-linkedin-dmp-segment-name-start

The name of segment in |destination-name|.

.. setting-linkedin-dmp-segment-name-end





.. vale off

**LISTRAK** (email)

.. vale on

Settings unique to Listrak.

**Audience primary key**

See common settings.

**Field group**

.. setting-listrak-field-group-start

The name of a profile field group in |destination-name|, from which the collection of audience and attribute fields sent from Amperity is available.

.. setting-listrak-field-group-end

**List name**

.. setting-listrak-list-name-start

The name of the email list in |destination-name| and managed by Amperity.

.. setting-listrak-list-name-end

**Segment name**

.. setting-listrak-segment-name-start

The name of a segment in |destination-name| managed by Amperity.

.. setting-listrak-segment-name-end

**Listrak default list name** (applies to SMS also)

.. vale off

.. setting-listrak-default-list-name-start

|destination-name| uses a list named "Master List" by default, but allows custom lists to be created. Verify the name of the list in |destination-name| before configuring this destination in Amperity.

If you are not sure which lists should be managed by Amperity, work with your Listrak representative to determine the best approach for list management.

.. setting-listrak-default-list-name-end

.. vale on






.. vale off

**LISTRAK** (SMS)

.. vale on

Settings unique to Listrak.

**Audience primary key**

See common settings. This one defaults to "phone".

**Opted-in?**

.. setting-listrak-sms-optin-start

.. caution:: Audience members sent to |destination-name| from Amperity are automatically subscribed to a list and can receive SMS messages as the default behavior in |destination-name|. Audience members who did not already exist in |destination-name| are created and subscribed by default.

   To avoid sending unsubscribed customers, apply filters to remove any customers who have unsubscribed from receiving SMS messages before sending audiences to |destination-name| using campaigns, journeys, or orchestrations.

   Amperity updates the contact attributes of SMS audiences in Listrak, including **phone** (required), **email**, **first name**, **last name**, **birthdate**, and **postal code**. Additional attributes may be sent when a matching custom segmentation field exists in |destination-name|.

   Talk with your Amperity representative about the |destination-name| connector before configuring it in your tenant.

.. setting-listrak-sms-optin-end

**Sender code ID**

.. setting-listrak-sms-sender-code-id-start

A sender code associates your brand's |destination-name| account with SMS campaigns, such as broadcast, split tests, keyword, and subscription.

The sender code ID is provided by |destination-name|. Ask your |destination-name| representative for the sender code if necessary.

.. setting-listrak-sms-sender-code-id-end

**SMS list ID**

.. setting-listrak-sms-phone-list-id-start

The SMS list ID for a list in |destination-name|.

The SMS list ID is available from the |destination-name| user interface. Open the **Contacts** menu, and then choose **SMS Lists**. Open a list. The SMS list ID is available in the URL of the list after the equals symbol.

.. setting-listrak-sms-phone-list-id-end

**Include attributes that match custom profile fields**

.. setting-listrak-sms-enable-segmentation-start

Select **Include attributes that match custom profile fields** to have Amperity synchronize all profile attributes in Amperity that match custom profile fields defined in |destination-name|. Custom attributes must match the name of the custom profile field in Listrak and must be a supported Listrak data.

.. setting-listrak-sms-enable-segmentation-end

.. setting-listrak-sms-enable-segmentation-caveat-start

.. important:: Custom attributes must be `configured as custom profile fields <https://help.listrak.com/en/articles/1852936-sms-profile-fields-and-personalization-guide>`__ |ext_link| in Listrak before Amperity can send custom attributes with |destination-name| profiles.

   The attribute name in Amperity **must** match the profile field name in |destination-name|. Attribute names are not case-sensitive.

   All custom attributes sent by Amperity **must** match a custom profile field that exists in |destination-name|.

.. setting-listrak-sms-enable-segmentation-caveat-end






.. vale off

**LIVERAMP**

.. vale on

See SFTP.





.. vale off

**MAILCHIMP**

.. vale on

Settings unique to Mailchimp.

**Data center**

.. setting-mailchimp-data-center-start

The data center ID appends to the API key after the hyphen.

.. setting-mailchimp-data-center-end

**List ID**

.. setting-mailchimp-list-id-start

The audience ID to which Amperity writes data. This is sometimes referred to as the list ID.

.. setting-mailchimp-list-id-end

**List name**

.. setting-mailchimp-list-name-start

The name of the list that by Amperity in |destination-name|.

.. setting-mailchimp-list-name-end

**Tag name**

.. setting-mailchimp-tag-name-start

A `Mailchimp tag <https://mailchimp.com/help/getting-started-tags/>`__ |ext_link| to apply to all audience list members. For example: "Added by Amperity". If this tag does not exist in Mailchimp, it applies to all audience members added by Amperity.

.. setting-mailchimp-tag-name-end




.. vale off

**META ADS MANAGER**

.. vale on

Settings unique to Meta Ads Manager.

**Account ID**

.. setting-meta-ads-manager-account-id-start

The account ID for your |destination-name| account.

.. setting-meta-ads-manager-account-id-end

**Custom audience name**

.. setting-meta-ads-manager-custom-audience-name-start

The name of the custom audience in |destination-name|. The name of a custom audience should not include the word "treatment".

.. setting-meta-ads-manager-custom-audience-name-end

**Customer file source**

.. setting-meta-ads-manager-customer-file-source-start

A setting that describes how to collect custom audience information. Select one of the following settings:

* USER_PROVIDED_ONLY
* PARTNER_PROVIDED_ONLY
* BOTH_USER_AND_PARTNER_PROVIDED

.. setting-meta-ads-manager-customer-file-source-end





.. vale off

**META ADS MANAGER: EVENTS**

.. vale on

Settings unique to Meta Ads Manager: Events.

**Dataset ID**

.. setting-meta-ads-manager-dataset-id-start

`Datasets connect and manage event data <https://www.facebook.com/business/help/750785952855662?id=490360542427371>`__ |ext_link| from different sources--such as from websites, mobile apps, physical store locations or business chats--from one location.

A `dataset ID configured <https://www.facebook.com/business/help/5818684664831465?id=490360542427371>`__ |ext_link| in |destination-name| supports sending send events from Amperity.

.. setting-meta-ads-manager-dataset-id-end





.. vale off

**MICROSOFT ADVERTISING**

.. vale on

Settings unique to Microsoft Advertising.

**Account and customer IDs**

.. vale off

.. setting-microsoft-advertising-account-and-customer-ids-start

To get your customer and account IDs, sign into the Microsoft Advertising web application, and then click on the Campaigns page. The URL of the Campaigns page has two key-value pairs, one for the customer ID and the other for the account ID.

The URL is similar to:

::

   https://ui.ads.microsoft.com/campaign
   /Campaigns.m?cid=12345678&aid=9876543
   21#/customer/...

The customer ID is the number in the URL that follows the "cid" parameter. For example: "12345678".

The account ID is the number in the URL that follows the "aid" parameter. For example: "987654321".

.. setting-microsoft-advertising-account-and-customer-ids-end

.. vale on


**Audience primary key**

See common settings.

**List name**

.. setting-microsoft-advertising-list-name-start

The name of the list in Microsoft Advertising.

.. setting-microsoft-advertising-list-name-end




.. vale off

**MICROSOFT DATAVERSE**

.. vale on

Settings unique to Microsoft Dataverse.

**Dataverse table logical name**

.. setting-microsoft-dataverse-table-logical-name-start

The table name in |destination-name|. This is the table to which the connector writes data. For example: "abc123_customers".

.. setting-microsoft-dataverse-table-logical-name-end

**Power Apps environment name**

.. setting-microsoft-dataverse-powerapps-name-start

The environment name for your Power Apps application. For example: "socktown".

.. setting-microsoft-dataverse-powerapps-name-end

**Power Apps environment region**

.. vale off

.. setting-microsoft-dataverse-powerapps-region-start

The environment region for your Power Apps application. For example: "crm".

.. setting-microsoft-dataverse-powerapps-region-end

.. vale on

**Truncate table?**

.. setting-microsoft-dataverse-truncate-table-start

Select **Truncate?** to truncate the table before loading data.

.. setting-microsoft-dataverse-truncate-table-end





.. vale off

**MICROSOFT DYNAMICS 365 MARKETING**

.. vale on

Settings unique to Microsoft Dynamics 365 Marketing.

**Dynamics 365 marketing segment name**

.. setting-microsoft-dynamics-365-segment-name-start

The name of the segment in |destination-name| managed by Amperity.

.. setting-microsoft-dynamics-365-segment-name-end

**Power Apps environment name**

.. setting-microsoft-dynamics-365-environment-name-start

The environment name for your Power Apps application. For example: "socktown".

.. setting-microsoft-dynamics-365-environment-name-end

**Power Apps environment region**

.. vale off

.. setting-microsoft-dynamics-365-environment-region-start

The environment region for your Power Apps application. For example: "crm".

.. setting-microsoft-dynamics-365-environment-region-end

.. vale on




.. vale off

**MICROSOFT DYNAMICS**

.. vale on

Settings unique to Microsoft Dynamics.

**Azure Active Directory ID**

.. setting-microsoft-dynamics-azure-ad-id-start

The Active Directory tenant ID associated with your Microsoft Azure subscription.

.. setting-microsoft-dynamics-azure-ad-id-end

**Dynamics entity**

.. setting-microsoft-dynamics-entity-start

The `entity type <https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/entitytypes?view=dataverse-latest&viewFallbackFrom=dynamics-ce-odata-9>`__ |ext_link| that defines the schema for data.

.. setting-microsoft-dynamics-entity-end

**Dynamics URL**

.. setting-microsoft-dynamics-url-start

The URL of your instance of |destination-name|. The URL must be the full URL, including ``https://``. For example:

``https://<tenant-name>.crm.dynamics.com``

.. setting-microsoft-dynamics-url-end

**Operation**

.. setting-microsoft-dynamics-operation-start

The operation to perform. Use "Upsert" to create or update records. Use "Delete" to remove all records.

.. setting-microsoft-dynamics-operation-end

**ID field**

.. setting-microsoft-dynamics-id-field-start

The field to use for upsert or delete operations.

.. setting-microsoft-dynamics-id-field-end





.. vale off

**MONETATE**

.. vale on

See SFTP.





.. vale off

**NEUSTAR**

.. vale on

See SFTP.





.. vale off

**ORACLE DATA CLOUD**

.. vale on

See SFTP.





.. vale off

**ORACLE ELOQUA**

.. vale on

Settings unique to Oracle Eloqua.

**Audience primary key**

.. setting-oracle-eloqua-audience-primary-key-start

The primary key for the shared list: **C_EmailAddress**.

Map email address values to the database type **C_EmailAddress** before sending shared list audiences to |destination-name|.

You may send audience attributes. Some attributes must map to `default attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/ContactFieldsDefinitions.htm>`__ |ext_link|. You may define `custom attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/Tasks/CreatingContactFields.htm>`__ |ext_link|.

.. setting-oracle-eloqua-audience-primary-key-end

**Shared list name**

.. setting-oracle-eloqua-shared-list-name-start

The name of the shared list.

Use filename templates to configure Amperity to support managing more than one shared list. For example:

1. A timestamp at the end of a filename template--**Early_Purchasers_{{format:'MM-dd-yyyy'}}.csv**--creates a new shared list each time Amperity sends an audience. The filename always has "Early Purchasers", but each send has a unique datestamp.

2. A campaign configured only for campaign name and group name--**{{ campaign_name }} - {{ group_name }}**--updates the same shared list each time Amperity sends the audience.

.. setting-oracle-eloqua-shared-list-name-end

.. vale off

.. setting-oracle-eloqua-shared-list-name-caution-start

You may add custom attributes to the shared list as long as each custom attribute maps to the database name assigned to the custom contact field by |destination-name|.

This approach requires adding an empty shared list to |destination-name|, and then adding any custom contact fields to that shared list. This generates the database name, which is typically, but not always, prefixed with **C_**.

.. setting-oracle-eloqua-shared-list-name-caution-end

.. vale on




.. vale off

**PANDA PRINTING**

.. vale on

See SFTP.





.. vale off

**PEBBLEPOST**

.. vale on

See SFTP.





.. vale off

**PERSADO**

.. vale on

See SFTP.





.. vale off

**PINTEREST**

.. vale on

Settings unique to Pinterest.

**Ad account ID**

.. setting-pinterest-ad-account-id-start

Your brand's |destination-name| advertising account ID.

.. setting-pinterest-ad-account-id-end

**Audience primary key**

See common settings.

**List name**

.. setting-pinterest-list-name-start

The list name to which Amperity sends a list of SHA-256 hashed email addresses. This can be the name of an existing list or a new list.

.. setting-pinterest-list-name-end






.. vale off

**POWERREVIEWS**

.. vale on

See SFTP.





.. vale off

**QUAD**

.. vale on

See SFTP.





.. vale off

**RR DONNELLY**

.. vale on

See SFTP.





.. vale off

**SAILTHRU**

.. vale on

Settings unique to Sailthru by Zeta Engage.

**Audience primary key**

See common settings.

**List name**

.. setting-sailthru-list-name-start

The name of the list in |destination-name| managed by Amperity. Amperity creates the list if it does not exist.

.. setting-sailthru-list-name-end





.. vale off

**SALESFORCE MARKETING CLOUD**

.. vale on

Settings unique to Salesforce Marketing Cloud.

Note: There is an SFTP-based connector also.

**Account ID**

.. setting-salesforce-marketing-cloud-account-id-start

The account ID for the business unit in |destination-name|.

.. setting-salesforce-marketing-cloud-account-id-end

**Append data**

.. vale off

.. setting-salesforce-marketing-cloud-append-data-start

Enable this option to upsert new rows to the data extension and update existing rows.

When disabled, data in the data extension is deleted, and then updated to match the rows sent from Amperity.

.. setting-salesforce-marketing-cloud-append-data-end

.. vale on


**Data extension name**

.. setting-salesforce-marketing-cloud-data-extension-name-start

The name of the data extension in |destination-name| managed by Amperity.

.. setting-salesforce-marketing-cloud-data-extension-name-end

.. setting-salesforce-marketing-cloud-data-extension-name-context-campaigns-start

For campaigns, use the **{campaign_name}** and **{group_name}** campaign template variables and assign campaign and treatment group names to your data extension.

.. important:: The name of a data extension must be unique within |destination-name|.

.. setting-salesforce-marketing-cloud-data-extension-name-context-campaigns-end

.. setting-salesforce-marketing-cloud-data-extension-name-context-orchestrations-start

For orchestrations, assign a name to the data extension.

.. important:: The name of a data extension must be unique within |destination-name|, should use underscores--``_``--instead of spaces, and may not contain *any* of the following characters:

::

   ! @ # $ % ^ * ( ) = { } [ ] \ . < > / " : ? | , &

.. setting-salesforce-marketing-cloud-data-extension-name-context-orchestrations-end

**Folder name**

.. setting-salesforce-marketing-cloud-folder-name-start

The directory within the |destination-name| SFTP site from which the Marketing Cloud SOAP API finds CSV files.

.. setting-salesforce-marketing-cloud-folder-name-end

**Primary key**

.. setting-salesforce-marketing-cloud-primary-key-start

Set to one of the following: "subscriber_key" or "email".

Use "subscriber_key" when a field maps directly to the subscriber key in |destination-name|, otherwise use "email".

.. setting-salesforce-marketing-cloud-primary-key-end

**Subscriber field**

.. setting-salesforce-marketing-cloud-subscriber-field-start

Recommended. The subscriber key for |destination-name|.

.. setting-salesforce-marketing-cloud-subscriber-field-end

.. setting-salesforce-marketing-cloud-subscriber-field-important-start

A subscriber key is the "primary key" for the destination. Choose the |destination-name| subscriber key or choose email.

.. setting-salesforce-marketing-cloud-subscriber-field-important-end





.. vale off

**SALESFORCE SALES CLOUD**

.. vale on

Settings unique to Salesforce Sales Cloud.

**Connect to sandbox instance?**

.. setting-salesforce-sales-cloud-connect-to-sandbox-start

Optional. Select this option if the destination is a sandbox instance and not a production instance.

.. setting-salesforce-sales-cloud-connect-to-sandbox-end

.. setting-salesforce-sales-cloud-connect-to-sandbox-ignored-start

Ignore a sandbox instance when using a custom URL of Salesforce Sales Cloud logins.

.. setting-salesforce-sales-cloud-connect-to-sandbox-ignored-end

**Custom Salesforce login URL**

.. setting-salesforce-sales-cloud-custom-login-url-start

Optional. The custom URL of |destination-name| logins requires only the scheme (``http://`` or ``https://``) and hostname parts of the URL. For example: ``http://<hostname>`` or ``https://<hostname>``. Amperity automatically adds the rest of the path.

.. setting-salesforce-sales-cloud-custom-login-url-end

**External ID field**

.. vale off

.. setting-salesforce-sales-cloud-external-id-field-start

Configure the external ID as "Amperity_ID__c". The "__c" identifies the field as a custom field in the Salesforce object.

.. setting-salesforce-sales-cloud-external-id-field-end

.. vale on


**Load data in parallel?**

.. setting-salesforce-sales-cloud-load-data-in-parallel-start

When enabled, "Upsert" operations ignore **NULL** values in data sent from Amperity. If a field has a **NULL** value and there is a value in the corresponding Salesforce object, the operation keeps the value in the Salesforce object.

.. setting-salesforce-sales-cloud-load-data-in-parallel-end

.. setting-salesforce-sales-cloud-load-data-in-parallel-caution-start

Enabling parallelism may cause Salesforce to process batches in parallel. This may improve performance, but comes with the risk of introducing failures due to locking. It is possible for more than one batch to try to get a lock on the same row, causing one or both batches to fail.

.. setting-salesforce-sales-cloud-load-data-in-parallel-caution-end

**Operation**

.. setting-salesforce-sales-cloud-operation-start

The operation may be one of the following: "Insert", "Upsert" (recommended), "Update", or "Delete". Upsert operations insert a new record or update an existing record, whereas insert and update operations insert or update, but not both.

.. setting-salesforce-sales-cloud-operation-end

**Salesforce object**

.. setting-salesforce-sales-cloud-salesforce-object-start

The name of the object, or audience list, in Salesforce Sales Cloud to which Amperity sends data. For example: "Contact", "Customers", or "Amperity_List__c".

.. setting-salesforce-sales-cloud-salesforce-object-end

**Use NULL for empty fields?**

.. setting-salesforce-sales-cloud-use-null-for-empty-fields-start

Enable to use **NULL** values when fields are empty.

.. setting-salesforce-sales-cloud-use-null-for-empty-fields-end




.. vale off

**SAP EMARSYS**

.. vale on

Settings unique to SAP Emarsys.

**Contact identifier**

.. setting-sap-emarsys-contact-identifier-start

The contact identifier for contact lists managed by this destination. Possible values: "email" or "phone".

.. setting-sap-emarsys-contact-identifier-end

**Create new contact**

.. setting-sap-emarsys-create-contact-start

Enable to create contacts when they do not exist in |destination-name|. Disable to prevent creating new contacts.

.. setting-sap-emarsys-create-contact-end


**Does the list exist?**

.. setting-sap-emarsys-list-exists-start

If Amperity is managing a list that already exists in |destination-name| configure the **Contact identifier** to match the one used by the list and ensure the name of the audience sent from Amperity matches the name of the contact list in |destination-name|.

If the contact list name doesn't exist Amperity will create it. If it exists, Amperity will update membership.

.. setting-sap-emarsys-list-exists-end

**Profile attributes and custom fields**

.. setting-sap-emarsys-attributes-and-fields-start

Profile attributes sent to |destination-name| must match any of the `SAP Emarsys system fields <https://help.sap.com/docs/SAP_EMARSYS/5d44574160f44536b0130abf58cb87cc/fdf56fb974c110149470d0c1a7fb5ee9.html>`__ |ext_link| or any `custom fields <https://help.sap.com/docs/SAP_EMARSYS/f8e2fafeea804018a954a8857d9dfff3/bea073ce154d4839b41ae26b5e451624.html>`__ |ext_link| that you have defined.

The name of the system or custom field sent from Amperity must match the name of the system attribute or custom field in |destination-name|.

Amperity will automatically pass the Amperity ID to the contact list when a custom field named **external_id** exists in the contact list.

.. important:: Log in to |destination-name| to find the correct string value for the system or custom field. Choose **Management** and open the **Field Editor**.

   Use the **Field String ID** column to indentify the correct system or custom field name. System fields are available from the **System fields** tab and custom fields are available from the **Custom fields** tab.

.. setting-sap-emarsys-attributes-and-fields-end




.. vale off

**SFTP**

.. vale on

Settings unique to SFTP.

.. vale off

Applies to: Acxiom, Adobe AEP, Adobe Campaign, Adobe Customer Attributes, Airship, BazaarVoice, Bluecore, Evocalize, Experian, Infutor, Kibo, Koupon Media, Neustar, Oracle Data Cloud, Oracle DMP, Oracle Responsys, PebblePost, Persado, PowerReviews, Quad, RR Donnelly, Salesforce Marketing Cloud, SMG, SoundCommerce, SFTP, Vibes.

.. vale on

**About**

.. setting-sftp-about-start

Secure File Transfer Protocol (SFTP) is a network protocol that provides file access, file transfer, and file management over any reliable data stream.

.. setting-sftp-about-end

**Compression**

See Common.

**Delimiter**

See Delimiter.

**Escape character**

See Common.

**File format**

See Common. Including Parquet extension.

**Filename template**

See Common.

**Header?**

See Common.

**Line ending**

See Common.

**PGP public key**

See Common.

**Quote mode**

See Common.

**Remote folder**

See Common.

**Success file**

See Common.

**Use Zip64?**

See Common.





.. vale off

**SMG**

.. vale on

See SFTP.





.. vale off

**SNAPCHAT**

.. vale on

Settings unique to Snapchat.

**Ad account ID**

.. setting-snapchat-ad-account-id-start

The ID for the |destination-name| advertising account. This ID is available from the top-left menu in |destination-name|. Open that menu, choose "Add Accounts", and then copy the ID for the account to which Amperity sends audiences.

.. setting-snapchat-ad-account-id-end

**Segment name**

.. setting-snapchat-segment-name-start

The name of the audience in |destination-name| managed by Amperity. Amperity creates the audience if it does not exist. The audience is available from the |destination-name| "Audiences" page.

.. setting-snapchat-segment-name-end







.. vale off

**SNOWFLAKE**

.. vale on

Settings unique to Snowflake.

**Account name**

.. vale off

.. setting-snowflake-account-name-start

The account name is found within the URL of the Snowflake instance and is a character string before ``snowflakecomputing.com``. For example: "ab12345".

.. setting-snowflake-account-name-end

.. vale on

**Create table?**

.. setting-snowflake-create-table-start

Use the **Create table** option to create the table in Snowflake if it is not already there.

.. setting-snowflake-create-table-end

**Drop table?**

.. setting-snowflake-drop-table-start

Use the **Drop table** option to overwrite the table and apply an updated schema when the upstream segment or table changes.

.. setting-snowflake-drop-table-end

**Region ID**

.. vale off

.. setting-snowflake-region-id-start

The ID for the region in which the Snowflake account name is located. For example: "us-west-2".

.. setting-snowflake-region-id-end

.. vale on


.. vale off

.. setting-snowflake-region-id-location-start

.. note:: The Amperity instance of Snowflake should be located in the same region as the customer's instance of Snowflake.

.. setting-snowflake-region-id-location-end

.. vale on


**Snowflake location**

.. setting-snowflake-location-start

The table to which Amperity loads data. Define this location using a period-delimited list of Snowflake database name, Snowflake schema name, and Snowflake table name. For example:

::

   SNOWFLAKE_DATABASE_NAME.SNOWFLAKE_SCHEMA.TABLE_NAME

.. setting-snowflake-location-end

**Stage**

.. setting-snowflake-stage-start

The Snowflake stage name created by the `CREATE STAGE <https://docs.snowflake.com/en/sql-reference/sql/create-stage>`__ |ext_link| command.

.. setting-snowflake-stage-end

**Truncate table?**

.. setting-snowflake-truncate-table-start

Use the **Truncate table** option to empty the contents of the table before loading data.

.. setting-snowflake-truncate-table-end

**Warehouse**

.. setting-snowflake-warehouse-start

The name of the Snowflake data warehouse created by the `CREATE WAREHOUSE <https://docs.snowflake.com/en/sql-reference/sql/create-warehouse>`__ |ext_link| command. For example:

``AMPERITY_WH``

.. setting-snowflake-warehouse-end





.. vale off

**SOUND COMMERCE**

.. vale on

See SFTP.





.. vale off

**THE TRADE DESK**

.. vale on

Settings unique to The Trade Desk.

**Membership duration**

See common.

.. vale off

.. setting-the-trade-desk-membership-duration-minmax-start

The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the default duration. The maximum value is "180".

.. setting-the-trade-desk-membership-duration-minmax-end

.. vale on


.. setting-the-trade-desk-membership-duration-example-start

The membership duration is in days. Adjust the membership duration value to be greater than or equal to than the frequency at which your brand sends campaigns or orchestrations from Amperity.

For example: if your brand sends a campaign to |destination-name| every 30 days, then set membership duration to "30". If your brand sends a campaign every 14 days, then set membership duration to "14".

If your brand sends a campaign every 30 days, but the membership duration is 14, then the audience size for the last 16 days of the duration window is "0".

.. setting-the-trade-desk-membership-duration-example-end

**Segment name**

.. setting-the-trade-desk-segment-name-start

The name of a segment in |destination-name|.

.. setting-the-trade-desk-segment-name-end

**UID 2.0 agreement**

.. setting-the-trade-desk-uid2-agreement-start

|destination-name| supports using `UID 2.0 <https://unifiedid.com/docs/intro>`__ |ext_link| to help establish your customers' identifies without using third-party data. UID 2.0 enables publisher websites, mobile apps, and Connected TV (CTV) apps to monetize through programmatic workflows, while offering user transparency and privacy controls that meet local market requirements.

Your brand must have a UID 2.0 agreement in-place with The Trade Desk before configuring Amperity to send events to |destination-name|.

.. setting-the-trade-desk-uid2-agreement-end




.. vale off

**THE TRADE DESK: 3P MARKETPLACE**

.. vale on

Settings unique to The Trade Desk: 3P Marketplace.

**Membership duration**

See common.

**Segment taxonomy ID**

.. setting-the-trade-desk-3p-segment-taxonomy-id-start

The taxonomy ID for a monetized segment in The Trade Desk.

.. setting-the-trade-desk-3p-segment-taxonomy-id-end





.. vale off

**THE TRADE DESK: EVENTS**

.. vale on

Settings unique to The Trade Desk: Events.

**Merchant ID**

.. setting-the-trade-desk-offline-merchant-id-start

Required if |destination-name| has assigned one to your brand. The merchant ID is a numeric platform identifier assigned to retailers who are onboarded to |destination-name| as a **Merchant**. For example: "11001".

.. setting-the-trade-desk-offline-merchant-id-end

.. setting-the-trade-desk-offline-merchant-versus-offline-start

Brands onboarded to The Trade Desk as a **Merchant** have access to **Product Catalog** and event tracking features in The Trade Desk user interface.

Brands not onboarded to The Trade Desk as a **Merchant** can:

#. Monetize conversation data for measurement and targeting using the **Offline Provider ID**.
#. Request to be onboarded as a **Merchant**, after which a merchant identifier is assigned.
#. Send conversion data to the advertiser seat at The Trade Desk for measurement within their own campaigns. Use "amperity" as the value for the **Offline Provider ID** setting for this use case.

.. setting-the-trade-desk-offline-merchant-versus-offline-end

**Offline Data Provider ID**

.. vale off

.. setting-the-trade-desk-offline-data-provider-id-start

Required. The offline data provider ID assigned to your |destination-name| account. Default value: "amperity". Use the default value if your brand only sends data for first-party measurement.

.. setting-the-trade-desk-offline-data-provider-id-end

.. vale on

**Tracking tag name**

.. setting-the-trade-desk-offline-tracking-tag-name-start

Required. The name of the tracking tag for events. The name is a string, may have up to 256 characters, must be unique, and may not duplicate any previous advertiser name or offline data provider ID. The tracking tag name appears in the UI for |destination-name| exactly as it is in Amperity.

.. setting-the-trade-desk-offline-tracking-tag-name-end

.. setting-the-trade-desk-offline-tracking-tag-name-context-start

|destination-name| uses a combination of the tracking tag name, your brand's advertiser ID, and offline data provider ID to build a unique offline tracking tag ID. Use the offline tracking ID to help measure the success of your brand's marketing campaigns.

.. setting-the-trade-desk-offline-tracking-tag-name-context-end





.. vale off

**TIKTOK ADS MANAGER**

.. vale on

Settings unique to TikTok Ads Manager.

**Advertiser ID**

.. setting-tiktok-ads-manager-advertiser-id-start

The advertiser ID for your |destination-name| account. This is a nineteen character string similar to "7654321098765432109" that you can find from the dropdown menu in the top right of TikTok Ads Manager.

.. setting-tiktok-ads-manager-advertiser-id-end

**Custom audience name**

.. setting-tiktok-ads-manager-custom-audience-name-start

The name of the audience in |destination-name| managed by Amperity. Amperity creates the audience if it does not exist.

.. setting-tiktok-ads-manager-custom-audience-name-end

**User ID type**

.. setting-tiktok-ads-manager-user-id-type-start

The user ID type. This value must be one of the following: "AAID" (Google), "EMAIL" (email addresses), "IDFA" (Apple), or "PHONE" (phone numbers). "EMAIL" and "PHONE" are the default values for campaigns.

.. setting-tiktok-ads-manager-user-id-type-end




.. vale off

**TIKTOK ADS MANAGER: EVENTS**

.. vale on

Settings unique to TikTok Ads Manager: Events.

**Advertiser ID**

.. setting-tiktok-ads-manager-offline-advertiser-id-start

The advertiser ID for the TikTok Ads account.

.. setting-tiktok-ads-manager-offline-advertiser-id-end

**Auto tracking?**

.. setting-tiktok-ads-manager-offline-auto-tracking-start

Select **Auto tracking** to use this event set for add tracking and attribution.

.. setting-tiktok-ads-manager-offline-auto-tracking-end

**Event set ID**

.. setting-tiktok-ads-manager-offline-event-set-id-start

The event set ID is a nineteen character string similar to "7654321098765432109".

.. setting-tiktok-ads-manager-offline-event-set-id-end

.. setting-tiktok-ads-manager-offline-event-set-id-context-start

The event set must exist before you can send data to it from Amperity. You can `create an event set ID <https://business-api.tiktok.com/portal/docs?id=1771101027431425>`__ |ext_link| from the |destination-name| user interface.

Add an event set ID if it does not exist.

Open the TikTok Ads Manager user interface. Choose **Assets**, then **Events**, and then from the **Offline** box select **Manage**.

Each event set has its own card. The event set ID is located under the name of the event set.

.. setting-tiktok-ads-manager-offline-event-set-id-context-end

**Event set name**

.. setting-tiktok-ads-manager-offline-event-set-name-start

The name of the events set in TikTok Ads Manager.

.. setting-tiktok-ads-manager-offline-event-set-name-end

**Event source**

.. setting-tiktok-ads-manager-offline-event-source-start

The event uploaded to TikTok Ads Manager. May be one of "web" or "offline". Use "web" for events that took place on your website and collected using the `payload helper <https://business-api.tiktok.com/portal/docs?id=1807346079965186>`__ |ext_link|. Use "offline" for events that took place in a physical store and measured by an offline event set ID.

.. setting-tiktok-ads-manager-offline-event-source-end





.. vale off

**VIBES**

.. vale on

See SFTP.

**Filename template**

.. setting-vibes-filename-template-pattern-start

A |destination-name| `recipient list <https://developer-platform.vibes.com/docs/recipient-list-import>`__ |ext_link| must have a name similar to "<filename>.recipient_list".

.. setting-vibes-filename-template-pattern-end




.. vale off

**WEBHOOK**

.. vale on

**Label name**

**Settings**




.. vale off

**YAHOO DSP**

.. vale on

**Short intro**

.. setting-yahoo-dsp-intro-start

Yahoo DSP is a demand-side platform (DSP) to which you can send audiences, and then advertise across the Yahoo brand ecosystem.

.. setting-yahoo-dsp-intro-end

**Membership duration**

Days. See common.

**Segment name**

.. setting-yahoo-dsp-segment-name-start

The name of the segment in |destination-name|. This can be the name of an existing segment or a new segment within the |destination-name| taxonomy. Segments are available in |destination-name| from "Audiences". Open the "Partner" audiences, and then choose "Amperity".

.. setting-yahoo-dsp-segment-name-end




.. vale off

**ZENDESK**

.. vale on

Settings unique to Zendesk.

**Subdomain**

.. setting-zendesk-subdomain-start

Required. The subdomain for your brand's Zendesk account. For example: "socktown" is the subdomain for "socktown.zendesk.com".

.. setting-zendesk-subdomain-end
