.. 
.. shared settings for destinations
.. 



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


**STEPS**

**Step 01a**

.. destinations-steps-add-destinations-start

Open the **Destinations** page, and then click the **Add destination** button.

.. destinations-steps-add-destinations-end

**Step 01b**

.. destinations-steps-add-destinations-select-start

To configure a destination for |destination-name|, do one of the following:

#. Click the row in which |destination-name| is located. Destinations are listed alphabetically and you can scroll up and down the list.
#. Search for |destination-name|. Start typing |filter-the-list|. The list will filter to show only matching destinations.

.. destinations-steps-add-destinations-select-end

**Step 02a**

.. destinations-steps-select-credential-start

Select the credential for |destination-name| from the **Credential** drop-down, and then click **Continue**.

.. destinations-steps-select-credential-end

**Step 02b**

.. destinations-steps-test-connection-start

Click the "Test connection" link on the "Configure destination" page to verify that Amperity can connect to |destination-name|.

.. destinations-steps-test-connection-end

**Step 03**

.. destinations-steps-name-and-description-start

In the "Destination settings" dialog box, assign the destination a name and description that ensures other users of Amperity can recognize when to use this destination.

.. destinations-steps-name-and-description-end

**Step 04**

.. destinations-steps-settings-start

Configure the following settings, and then click "Save".

.. destinations-steps-settings-end

**Step 05**

.. destinations-steps-business-users-start

After this destination is configured, business users may configure Amperity to:

* Use orchestrations to send query results
* Use orchestrations and campaigns to send audiences
* Use orchestrations and campaigns to send offline events

to |destination-name|.

.. destinations-steps-business-users-end

.. destinations-steps-business-users-orchestration-only-start

After this destination is configured, business users may configure Amperity to use orchestrations to send query results |destination-name|.

.. destinations-steps-business-users-orchestration-only-end




**COMMON API**

This section contains details that are common to API-based destinations.

**API allow-for note**

.. allow-for-start

Changes to |allow-for-what| are not immediately available in |destination-name|. Allow for |allow-for-duration| after the point at which Amperity has finished sending audience updates for them to be available.

.. allow-for-end



**COMMON**

This section contains settings that are identical across more than one destination.

.. TODO: Compare Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP for common settings.

**Audience primary key**

Applies to: ActiveCampaign, Cordial, Criteo, HubSpot, Klaviyo, Listrak, Microsoft Ads, Oracle Eloqua, Pinterest, and Sailthru. Must set the ``|audience-primary-key|`` variable in the destination file.

.. setting-common-audience-primary-key-start

The primary key for the audience. Set to |audience-primary-key|.

.. setting-common-audience-primary-key-end

**Business user access**

Applies to: all destinations.

.. TODO: These two settings are in an admonition block in docs pages; definition list in modals.

.. setting-common-business-user-access-allow-start

Select the "Allow business users" option to allow access to |destination-name| for users who are assigned the "Amp360 User" and/or "AmpIQ User" policies.

.. setting-common-business-user-access-allow-end

.. setting-common-business-user-access-restrict-pii-start

Some business users may have restricted access to PII, which will prevent them from sending data to |destination-name|. Select the "Allow limited PII access" option to allow access to |destination-name| for users who are assigned the "Restrict PII access" policy option.

.. setting-common-business-user-access-restrict-pii-end

**Compression**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-compression-start

The compression format to apply to the file. May be one of "GZIP", "None", "TAR", "TGZ", or "ZIP". 

.. setting-common-compression-end

**Configure** (in intro)

.. setting-common-file-configure-start

Amperity can be configured to send |what-send| to |where-send|.

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

.. setting-common-escape-character-unspecified-start

When an escape character is not specified *and* the quote mode is "None" files may be sent with unescaped and unquoted data. When an escape character is not specified, you should select a non-"None" option as the quote mode.

.. setting-common-escape-character-unspecified-end

**File format**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-file-format-start

Configure Amperity to send |what-send| to |where-send|.

.. setting-common-file-format-end

.. setting-common-file-format-custom-delimiter-start

Some file formats allow a custom delimiter. Choose the "Custom delimiter" file format, and then add a single character to represent the custom delimiter.

.. setting-common-file-format-custom-delimiter-end

.. setting-common-file-format-apache-parquet-start

The extension for Apache Parquet files may be excluded from the directory name.

.. setting-common-file-format-apache-parquet-end

**Filename template**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. include:: ../../shared/terms.rst
   :start-after: .. term-filename-template-start
   :end-before: .. term-filename-template-end

**Get details** (common intro)

.. setting-common-get-details-start

Review the following details before configuring credentials for |destination-name| and before configuring Amperity to send |what-send| to |where-send|.

.. setting-common-get-details-end

.. setting-common-get-details-file-specific-start

File-specific details to ensure that all files that are sent from Amperity are configured correctly for downstream workflows.

For example, Apache Parquet can be configured to exclude the extension from the directory name, some files require specific escape characters, and others may have unique delimiters.

Each file that is sent from Amperity may be configured for its own unique requirements.

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

Applies to ActiveCampaign, Cordial, HubSpot, Klaviyo, Listrak and others. Try to come up with some type of template.

.. setting-common-list-name-start

The primary key for the audience. Set to |audience-primary-key|.

.. setting-common-list-name-end

**Membership duration**

Applies to Amazon Ads, Google Ads, Google Customer Match, The Trade Desk, Yahoo DSP.

.. setting-common-membership-duration-start

The length of time |duration|, after which a customer will be removed from this audience. This value may be between |duration-value|. Set this value to "0" to remove audience member.

.. setting-common-membership-duration-end

.. setting-common-membership-duration-frequency-start

To ensure customers stay in this audience ensure the frequency at which the audience is sent to |destination-name| is less than the membership duration.

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

The PGP public key that Amperity will use to encrypt files.

.. setting-common-pgp-public-key-end

**Quote mode**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-quote-mode-start

The quote mode to use within the file. May be one of "all fields", "all non-NULL fields", "fields with special characters only", "all non-numeric fields" or "None".

.. setting-common-quote-mode-end

.. setting-common-quote-mode-none-start

Unescaped, unquoted files may occur when quote mode is set to "None" and an escape character is not specified.

.. setting-common-quote-mode-none-end

**Remote folder**

Applies to: Azure Blob Storage, Google Cloud Storage, and SFTP.

.. setting-common-remote-folder-start

The remote folder to which Amperity will send data.

.. setting-common-remote-folder-end

.. setting-common-remote-folder-forward-slash-start

A "/" (forward slash) must be used as the first character for this value. For example: |remote-folder|. For example: |remote-folder|.

.. setting-common-remote-folder-forward-slash-end

.. setting-common-remote-folder-spaces-start

If the path to the remote folder contains a space, use a backslash (\\) character to escape that space. For example, a folder named "From ACME" should be entered as "From\\ ACME".

.. setting-common-remote-folder-spaces-end

**Row Number**

Applies to: Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP destinations.

.. setting-common-row-number-start

Select to include a row number column in the output file. Applies to CSV, TSV, PSV, and custom delimiter file types.

.. setting-common-row-number-end

.. setting-common-row-number-column-name-start

If **Row Number** is enabled you may use the **Column name** setting to specify the name of the row number column in the output file. The name of this column must be less than 1028 characters and may only contain numbers, letters, underscores, and hyphens. Default value: "row_number".

.. setting-common-row-number-column-name-end

**Sandbox**

.. setting-common-sandbox-recommendation-start

Use a sandbox to configure a destination for |destination-name|. Before promoting your changes, send a test audience, and then verify the the results in |destination-name|. After the end-to-end workflow has been verified, push the destination from the sandbox to production.

.. setting-common-sandbox-recommendation-end

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

Enable to apply Zip64 data compression to very large files.

.. setting-common-use-zip64-end





**ACTIVECAMPAIGN**

This section contains settings that are unique to ActiveCampaign.

**Audience primary key**

See common settings.

.. setting-active-campaign-email-required-start

A contact in |destination-name| is defined by an email address. A contact may have additional information, but cannot exist without an email address.

Use a query or a campaign to define the information in the email list that will be managed by Amperity.

.. setting-active-campaign-email-required-end

**Group name**

.. setting-active-campaign-group-name-start

The name of the `user group <https://help.activecampaign.com/hc/en-us/articles/115000090164#setting-user-permissions-create-user-groups-0-0>`__ |ext_link| to which Amperity will send data. This group must exist in |destination-name| and must have permission to view and interact with the email list.

.. setting-active-campaign-group-name-end

.. setting-active-campaign-group-name-access-start

You must log into |destination-name| as a member of the specified user group to have access to the email list that is managed by Amperity.

.. setting-active-campaign-group-name-access-end

**List name**

.. setting-active-campaign-list-name-start

The name of an `email list <https://help.activecampaign.com/hc/en-us/articles/360000030559-How-to-create-a-list-in-ActiveCampaign>`__ |ext_link| in |destination-name| that will be managed by Amperity.

.. setting-active-campaign-list-name-end

**Verbose logging**

.. setting-active-campaign-verbose-logging-start

Enable verbose logging to return log details when |destination-name| rejects adding contacts to the email list.

When verbose logging setting is enabled, a list of rejected contacts is returned by the response from ActiveCampaign. For each rejected contact, a contact identifier is provided along with a string that describes the reason why the contact was rejected.

.. setting-active-campaign-verbose-logging-end





**ACXIOM**

See SFTP.





**ADOBE CAMPAIGN**

See SFTP.




**ADOBE COMMERCE**

(Not a destination.)





**ADOBE CUSTOMER ATTRIBUTES**

See SFTP.





**ADOBE EXPERIENCE CLOUD**

See SFTP.





**ADOBE MARKETO**

This section contains settings that are unique to Adobe Marketo.

**Folder name**

.. setting-adobe-marketo-folder-name-start

Required. The name of the folder in |destination-name| in which a program that contains the audience list is located.

.. setting-adobe-marketo-folder-name-end

**List name**

.. setting-adobe-marketo-list-name-start

Required. The name of the audience list that is managed by Amperity.

.. setting-adobe-marketo-list-name-end

.. setting-adobe-marketo-list-name-first-audience-start

It is possible for Adobe Marketo to contain multiple audience lists with identical names. If the Adobe Marketo API returns more than one audience list, Amperity will update the first audience in that list.

.. setting-adobe-marketo-list-name-first-audience-end

.. setting-adobe-marketo-list-name-membership-start

Amperity uses the |destination-name| API to update the membership of audience lists in |destination-name| to match the membership of audience lists that are sent from Amperity. The membership of the list in |destination-name| will be updated to match the membership of the audience list that is sent from Amperity. Amperity will add a user when they do not exist in |destination-name|.

Amperity does not maintain smart lists and does not remove users from the |destination-name| database.

.. setting-adobe-marketo-list-name-membership-end

.. setting-adobe-marketo-list-name-limitations-start

|destination-name| API has the following limitations:

* Subscriptions are allocated 50,000 API calls per day. This resets daily at 12:00 AM, Central Standard Time.
* API access is rate limited to 100 calls per 20 seconds, with up to 10 concurrent API calls.

You may experience these rate limits when sending very large audience lists.

It is possible for |destination-name| to have multiple audience lists with duplicate names. If the |destination-name| API returns more than one audience list, Amperity will update the first audience list in that list.

.. setting-adobe-marketo-list-name-limitations-start

**Program name**

.. setting-adobe-marketo-program-name-start

The name of the program in which the audience list that is managed by Amperity is located.

.. setting-adobe-marketo-program-name-end





**AIRSHIP**

See SFTP.





**AMAZON ADS**

This section contains settings that are unique to Amazon Ads.

**AMC instance**

.. setting-amazon-ads-amc-instance-start

The `instance within Amazon Marketing Cloud <https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/how-amc-works>`__ |ext_link| to which your brand will send audiences.

.. setting-amazon-ads-amc-instance-end

**Audience description**

.. setting-amazon-ads-audience-description-start

A description of the audience that is managed by Amperity.

.. setting-amazon-ads-audience-description-end

**Audience name**

.. setting-amazon-ads-audience-description-start

The name of the audience that is managed by Amperity. Amperity will create a new audience if an audience in |destination-name| does not match exactly the name of the one sent from Amperity.

.. setting-amazon-ads-audience-description-end

**DSP advertiser**

.. setting-amazon-ads-dsp-advertiser-start

The name of the DSP advertiser within |destination-name|.

.. setting-amazon-ads-dsp-advertiser-end

**Membership duration**

Days. See common.






**AMAZON S3**

This section contains settings that are unique to Amazon S3.

Applies to: Amazon S3, Cheetah Digital, Domo, Optimizely.

.. setting-amazon-s3-about-start

Amazon Simple Storage Service (|destination-name|) can store data files of any size for any file format that is supported by Amperity.

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

Required. The S3 prefix is a string that is used to filter results to include only objects whose names begin with this prefix. When this value is set, the names of objects that may be returned in the response are relative to the root of the bucket.

.. setting-amazon-s3-prefix-end

**Success file**

See Common.

**Use Zip64?**

See Common.





**ATTENTIVE** (API + SFTP)

This section contains settings that are unique to Attentive (API).

See SFTP for any common file settings.

**Client domain** (SFTP)

.. setting-attentive-client-domain-start

The client domain for your brand's instance of |destination-name|.

.. setting-attentive-client-domain-end

**Primary Identifier** (API)

.. setting-attentive-primary-identifier-start

The primary identifier that is used within your |destination-name| account. May be one of the following: "email" or "phone".

.. setting-attentive-primary-identifier-end

.. setting-attentive-primary-identifier-context-start

|destination-name| accepts email addresses *or* phone numbers as the primary identifier. The set of data that is sent from Amperity **must** contain the primary identifier. For example, if your primary identifier is phone numbers, than the **phone** field must be included.

You may send the non-primary email address or phone number as a custom attribute.

.. setting-attentive-primary-identifier-context-end

**Segment name** (SFTP)

.. setting-attentive-segment-name-start

The name of the segment in |destination-name| that is managed by Amperity.

.. setting-attentive-segment-name-end





**AZURE BLOB STORAGE**

This section contains settings that are unique to Azure Blob Storage.

Applies to: Azure Blob Storage.

.. setting-azure-blob-storage-about-start

Microsoft |destination-name| can store data files of any size for any file format that is supported by Amperity.

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





**BAZAARVOICE**

See SFTP.





**BLUECORE**

See SFTP.

**Header**

.. setting-bluecore-header-start

|destination-name| requires a header row to be present in |what-send|. The header row cannot start with a number or contain any special characters other than underscores ( _ ) and must be less than 30 characters in length.

|destination-name| recommends the following file naming convention: "<company_name>_<data_type>_<date>.csv".

Consider naming queries that are sent to the |destination-name| platform in a way that satisfies the "<company_name>_<data_type>" component of the recommended naming pattern.

.. setting-bluecore-header-end




**BRAZE**

This section contains settings that are unique to Braze.

**Instance**

.. setting-braze-instance-start

Required. Select the `Braze instance <https://www.braze.com/docs/user_guide/administrative/access_braze/braze_instances>`__ |ext_link| in which your account was provisioned. May be one of "US-01", "US-02", "US-03", "US-04", "US-05", "US-06", "US-07", "US-08", "EU-01", or "EU-02".

.. setting-braze-instance-end

.. setting-braze-instance-example-start

For example, if your URL for |destination-name| is ``https://dashboard-03.braze.com``, the REST API endpoint is ``https://rest.iad-03.braze.com``, and the instance is "US-03".

.. setting-braze-instance-example-end

**Profile updates?**

.. setting-braze-profile-updates-start

To update audience profiles only when one (or more) values change, enable the **Only send updated audience profiles** option.

.. setting-braze-profile-updates-end

.. setting-braze-profile-updates-usewhen-start

Use the **Only send updated audience profiles** option to configure Amperity to update audience profiles only when one (or more) values within a profile have changed. An update to an individual value in an audience profile requires updating the entire audience profile.

For use cases that require sending attributes that have values that are expected to change frequently, consider using additional queries to orchestrate specific sets of attributes at defined intervals so that your brand can maintain these values independently of your customer profiles.

.. setting-braze-profile-updates-usewhen-end

**User identifier**

.. setting-braze-user-identifier-start

The indentifier to use for matching users in |destination-name|. May be "external_id" or "braze_id".

.. setting-braze-user-identifier-end

.. setting-braze-user-identifier-about-start

The `external_id <https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import/#importing-with-external-id>`__ |ext_link| is a unique identifier for your customers, such as the Amperity ID. The `braze_id <https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import/#importing-with-braze-id>`__ |ext_link| is a unique identifier for existing |destination-name| customers.

.. setting-braze-user-identifier-about-end





**CAMELOT SMM**

See SFTP.





**CORDIAL**

This section contains settings that are unique to Cordial.

**Audience primary key**

See common.

**List name**

.. setting-cordial-list-name-start

The name of the list in |destination-name| that is managed by Amperity. This list will be created by Amperity if it does not exist.

.. setting-cordial-list-name-end

**Subscription status**

.. setting-cordial-subscription-status-start

Enable "Do not set subscription status automatically" to prevent updates without "channels.email.subscribeStatus" from being automatically subscribed in |destination-name|.

.. setting-cordial-subscription-status-end





**CRITEO**

This section contains settings that are unique to Criteo.

**Advertiser ID**

.. setting-criteo-advertiser-id-start

The unique ID for the advertiser account in |destination-name| to which Amperity will send audiences.

.. setting-criteo-advertiser-id-end

**Audience name**

.. setting-criteo-audience-name-start

The name of the audience that will be sent to |destination-name|.

.. setting-criteo-audience-name-end

**Audience primary key**

See common settings.




**CRITEO RETAIL MEDIA**

This section contains settings that are unique to Criteo Retail Media.

**Account ID**

.. setting-criteo-account-id-start

The account ID for the account in |destination-name| to which Amperity will send audience segments.

.. setting-criteo-account-id-end

**Audience segment description**

.. setting-criteo-audience-segment-description-start

Optional. A description for the audience segment.

.. setting-criteo-audience-segment-description-end

**Retailer ID**

.. setting-criteo-retailer-id-start

The retailer ID that is associated with the account in |destination-name| to which Amperity will send audience segments.

.. setting-criteo-retailer-id-end

**Identifier type**

.. setting-criteo-identifier-type-start

The identifier type. May be set to "Email", "UserIdentifier", "IdentityLink", or "CustomerID".

* Use "Email" to build audience segments using email addresses.
* Use "UserIdentifier" to build audience segments using a unique identifier provided by your brand.
* Use "IdentityLink" to build audience segments using LiveRamp identity graph data.
* Use "CustomerID" to build audience segments using Criteo Retail Media-managed customer lists.

.. setting-criteo-identifier-type-end




**CROSS COUNTRY COMPUTER**

See SFTP.




**DATABRICKS**

This section contains settings that are unique to Databricks.

**Catalog name**

.. setting-databricks-catalog-name-start

TEMP: "The catalog name to use for Databricks"

.. setting-databricks-catalog-name-end

**Schema name**

.. setting-databricks-schema-name-start

TEMP: "The schema name to use for Databricks"

.. setting-databricks-schema-name-end

**Table name**

.. setting-databricks-table-name-start

TEMP: "The table name to create/use for Databricks"

.. setting-databricks-table-name-end




**EPSILON ABACUS**

See SFTP.





**EPSILON CONVERSANT**

See SFTP.





**EPSILON TARGETING**

See SFTP.





**EXPERIAN**

See SFTP.





**GOOGLE ADS**

This section contains settings that are unique to Google Ads.

**Audience description**

.. setting-google-ads-audience-description-start

A description of the audience that is managed by Amperity.

.. setting-google-ads-audience-description-end

**Audience name**

.. setting-google-ads-audience-name-start

The name of the audience in |destination-name| that is managed by Amperity. This audience will be created by Amperity if it does not exist.

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

When "Upload key type" is set to "Mobile ID", the ID for the iOS or Android app from which the mobile ID was collected.

.. setting-google-ads-mobile-app-id-end

**Upload key type**

.. setting-google-ads-upload-key-type-start

The type of key to use for audience matching in |destination-name|. May be one of "Contact Info" or "Mobile ID".

.. setting-google-ads-upload-key-type-end





**GOOGLE CLOUD STORAGE**

This section contains settings that are unique to Google Cloud Storage.

Applies to: Google Cloud Storage.

.. setting-google-cloud-storage-about-start

|destination-name| can store data files of any size for any file format that is supported by Amperity.

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





**GOOGLE CUSTOMER MATCH**

This section contains settings that are unique to Google Customer Match.

**Audience description**

See Google Ads.

**Audience name**

See Google Ads.

**Customer ID**

See Google Ads.

**Customer product**

.. setting-google-customer-match-customer-product-start

The Google advertising product to which audiences will be sent. May be one of "Google Ads", "Display Video Advertiser", or "Display Video Partner".

.. setting-google-customer-match-customer-product-end

**Membership duration**

See common.

**Mobile app ID**

See Google Ads.

**Upload key type**

See Google Ads.





**GOOGLE ENHANCED CONVERSIONS**

This section contains settings that are unique to Google Enhanced Conversions.

**Conversion action name**

.. setting-google-enhanced-conversions-action-name-start

TEMP: "Name of the Conversion Action. Will be created if it doesn't exist."

.. setting-google-enhanced-conversions-action-name-end

**Customer ID**

.. setting-google-enhanced-conversions-customer-id-start

TEMP: "Customer ID of the Google Enhanced Conversions account; might just be Google Ads account"

.. setting-google-enhanced-conversions-customer-id-end





**HUBSPOT**

This section contains settings that are unique to HubSpot.

**Audience primary key**

See common settings.

**List name**

.. setting-hubspot-list-name-start

The list name to which Amperity will send contacts. This can be the name of an existing list or a new list.

.. setting-hubspot-list-name-end





**INFUTOR**

See SFTP.

**Escape character**

.. setting-infutor-escape-character-start

An escape character must be specified because |destination-name| requires that quotations be removed from files.

.. setting-infutor-escape-character-end

**Quote mode**

.. setting-infutor-quote-mode-start

Quotations must be removed from files. If an escape character is not specified and quote mode is set to “None” (as required by |destination-name|) this may result in unescaped, unquoted files.

.. setting-infutor-quote-mode-end

**Public key**

.. setting-infutor-public-key-start

Data that contains PII must be encrypted using public key encryption before it is transmitted to |destination-name| using SFTP.

.. setting-infutor-public-key-end





**KIBO**

See SFTP.





**KLAVIYO**

This section contains settings that are unique to Klaviyo.

**Audience primary key**

See common settings.

**List name**

.. setting-klaviyo-list-name-start

The list name to which Amperity will write the audience list. This can be the name of an existing list or a new list.

.. setting-klaviyo-list-name-end

.. setting-klaviyo-list-name-note-start

|destination-name| supports up to 1000 lists and/or segments in your account at any given time.

.. setting-klaviyo-list-name-note-end

**Update contacts?**

.. setting-klaviyo-update-contacts-start

Send additional customer profile fields with an audience list, These fields are visible in |destination-name| from the "Customer Properties" section within individual profiles for members of that audience list.

.. setting-klaviyo-update-contacts-end





**KOUPON MEDIA**

See SFTP.





**LISTRAK**

This section contains settings that are unique to Listrak.

**Audience primary key**

See common settings.

**Field group**

.. setting-listrak-field-group-start

The name of a profile field group in |destination-name|, from which the collection of audience and attribute fields sent from Amperity will be available.

.. setting-listrak-field-group-end

**List name**

.. setting-listrak-list-name-start

The name of the list that will be managed in |destination-name|. This is often, but not always, named "Master List".

.. setting-listrak-list-name-end

**Segment name**

.. setting-listrak-segment-name-start

The name of segment in |destination-name| that is managed by Amperity.

.. setting-listrak-segment-name-end





**LIVERAMP**

See SFTP.





**MAILCHIMP**

This section contains settings that are unique to Mailchimp.

**Data center**

.. setting-mailchimp-data-center-start

The data center ID. This is appended to the API key after the hyphen.

.. setting-mailchimp-data-center-end

**List ID**

.. setting-mailchimp-list-id-start

The audience ID to which Amperity will write. (This is sometimes referred to as the list ID.)

.. setting-mailchimp-list-id-end

**List name**

.. setting-mailchimp-list-name-start

The name of the list that will be managed by Amperity in |destination-name|.

.. setting-mailchimp-list-name-end

**Tag name**

.. setting-mailchimp-tag-name-start

A `Mailchimp tag <https://mailchimp.com/help/getting-started-tags/>`__ |ext_link| to be applied to all audience list members. For example: "Added by Amperity". If this tag does not exist in Mailchimp, it will be associated to all audience members added by Amperity.

.. setting-mailchimp-tag-name-end




**META ADS MANAGER**

This section contains settings that are unique to Meta Ads Manager.

**Account ID**

.. setting-meta-ads-manager-account-id-start

The account ID for your |destination-name| account.

.. setting-meta-ads-manager-account-id-end

**Custom audience name**

.. setting-meta-ads-manager-custom-audience-name-start

The name of the custom audience in |destination-name|.

.. setting-meta-ads-manager-custom-audience-name-end

**Customer file source**

.. setting-meta-ads-manager-customer-file-source-start

A setting that describes how the information in the custom audience was originally collected. Select one of the following settings:

* USER_PROVIDED_ONLY
* PARTNER_PROVIDED_ONLY
* BOTH_USER_AND_PARTNER_PROVIDED

.. setting-meta-ads-manager-customer-file-source-end





**META ADS MANAGER: OFFLINE EVENTS**

This section contains settings that are unique to Meta Ads Manager: Offline Events.

**Dataset ID**

.. setting-meta-ads-manager-dataset-id-start

`Datasets allow you to connect and manage event data <https://www.facebook.com/business/help/750785952855662?id=490360542427371>`__ |ext_link| from different sources---such as from websites, mobile apps, physical store locations or business chats--–from one location.

A `dataset ID must be configured <https://www.facebook.com/business/help/5818684664831465?id=490360542427371>`__ |ext_link| in |destination-name| to support sending send offline events from Amperity.

.. setting-meta-ads-manager-dataset-id-end





**MICROSOFT ADVERTISING**

This section contains settings that are unique to Microsoft Advertising.

**Account and customer IDs**

.. setting-microsoft-advertising-account-and-customer-ids-start

To get your customer and account IDs, sign into the Microsoft Advertising web application, and then click on the Campaigns page. The URL for the Campaigns page will contain two key-value pairs, one for the customer ID and the other for the account ID.

The URL is similar to:

https://ui.ads.microsoft.com/campaign
/Campaigns.m?cid=12345678&aid=9876543
21#/customer/...

The customer ID is the number in the URL that follows the cid parameter. For example: "12345678".

The account ID is the number in the URL that follows the aid parameter. For example: "987654321".

.. setting-microsoft-advertising-account-and-customer-ids-end

**Audience primary key**

See common settings.

**List name**

.. setting-microsoft-advertising-list-name-start

The name of the list to be managed in Microsoft Advertising.

.. setting-microsoft-advertising-list-name-end




**MICROSOFT DATAVERSE**

This section contains settings that are unique to Microsoft Dataverse.

**Dataverse table logical name**

.. setting-microsoft-dataverse-table-logical-name-start

The table name in |destination-name|. This is the table to which the connector will write data. For example: "abc123_customers".

.. setting-microsoft-dataverse-table-logical-name-end

**Power Apps environment name**

.. setting-microsoft-dataverse-powerapps-name-start

The environment name for your Power Apps application. For example: "socktown".

.. setting-microsoft-dataverse-powerapps-name-end

**Power Apps environment region**

.. setting-microsoft-dataverse-powerapps-region-start

The environment region for your Power Apps application. For example: "crm".

.. setting-microsoft-dataverse-powerapps-region-end

**Truncate table?**

.. setting-microsoft-dataverse-truncate-table-start

Select **Truncate?** to truncate the table before loading data.

.. setting-microsoft-dataverse-truncate-table-end





**MICROSOFT DYNAMICS 365 MARKETING**

This section contains settings that are unique to Microsoft Dynamics 365 Marketing.

**Dynamics 365 marketing segment name**

.. setting-microsoft-dynamics-365-segment-name-start

The name of the segment in |destination-name| that is managed by Amperity.

.. setting-microsoft-dynamics-365-segment-name-end

**Power Apps environment name**

.. setting-microsoft-dynamics-365-environment-name-start

The environment name for your Power Apps application. For example: "socktown".

.. setting-microsoft-dynamics-365-environment-name-end

**Power Apps environment region**

.. setting-microsoft-dynamics-365-environment-region-start

The environment region for your Power Apps application. For example: "crm".

.. setting-microsoft-dynamics-365-environment-region-end





**MICROSOFT DYNAMICS**

This section contains settings that are unique to Microsoft Dynamics.

**Azure Active Directory ID**

.. setting-microsoft-dynamics-azure-ad-id-start

The Active Directory tenant ID that is associated with your Microsoft Azure subscription.

.. setting-microsoft-dynamics-azure-ad-id-end

**Dynamics entity**

.. setting-microsoft-dynamics-entity-start

The `entity type <https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/entitytypes?view=dataverse-latest&viewFallbackFrom=dynamics-ce-odata-9>`__ |ext_link| that defines the schema for data that is sent from Amperity.

.. setting-microsoft-dynamics-entity-end

**Dynamics URL**

.. setting-microsoft-dynamics-url-start

The URL for your instance of |destination-name|. The URL must be the full URL, including ``https://``. For example:

``https://<tenant-name>.crm.dynamics.com``

.. setting-microsoft-dynamics-url-end





**MONETATE**

See SFTP.





**NEUSTAR**

See SFTP.





**ORACLE DATA CLOUD**

See SFTP.





**ORACLE ELOQUA**

This section contains settings that are unique to Oracle Eloqua.

**Audience primary key**

.. setting-oracle-eloqua-audience-primary-key-start

The primary key for the shared list: **C_EmailAddress**.

An email address (mapped to the database type **C_EmailAddress**) is the only requirement for sending audiences to |destination-name| for use as a shared list.

Additional attributes may be sent. Some must be mapped to the `default attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/ContactFieldsDefinitions.htm>`__ |ext_link|; `custom attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/Tasks/CreatingContactFields.htm>`__ |ext_link| may be defined.

.. setting-oracle-eloqua-audience-primary-key-end

**Shared list name**

.. setting-oracle-eloqua-shared-list-name-start

The name of the shared list to be managed by Amperity.

Use filename templates to configure Amperity to support managing more than one shared list. For example:

1. A timestamp at the end of a filename template---**Early_Purchasers_{{format:'MM-dd-yyyy'}}.csv**---will create a new shared list each time an audience is sent from Amperity. The shared list will always be titled "Early Purchasers", but will have a unique datestamp.

2. A campaign that is configured only for campaign name and group name---**{{ campaign_name }} - {{ group_name }}**---will update the same shared list each time the audience is sent from Amperity.

.. setting-oracle-eloqua-shared-list-name-end

.. setting-oracle-eloqua-shared-list-name-caution-start

You may add custom attributes to the shared list as long as each custom attribute is mapped to the database name that was assigned to the custom contact field by |destination-name|.

This approach requires adding an empty shared list to |destination-name|, and then adding any custom contact fields to that shared list. This will generate the database name, which is typically (but not always) prefixed with **C_**.

.. setting-oracle-eloqua-shared-list-name-caution-end






**PANDA PRINTING**

See SFTP.





**PEBBLEPOST**

See SFTP.





**PERSADO**

See SFTP.





**PINTEREST**

This section contains settings that are unique to Pinterest.

**Ad account ID**

.. setting-pinterest-ad-account-id-start

Your brand's |destination-name| advertising account ID.

.. setting-pinterest-ad-account-id-end

**Audience primary key**

See common settings.

**List name**

.. setting-pinterest-list-name-start

The list name to which Amperity will send a list of SHA-256 hashed email addresses. This can be the name of an existing list or a new list.

.. setting-pinterest-list-name-end






**POWERREVIEWS**

See SFTP.





**QUAD**

See SFTP.





**RR DONNELLY**

See SFTP.





**SAILTHRU**

This section contains settings that are unique to Sailthru.

Now called Marigold Engage.

**Audience primary key**

See common settings.

**List name**

.. setting-sailthru-list-name-start

The name of the list in |destination-name| that is managed by Amperity. This list will be created by Amperity if it does not exist.

.. setting-sailthru-list-name-end





**SALESFORCE MARKETING CLOUD**

This section contains settings that are unique to Salesforce Marketing Cloud.

Note: There is an SFTP-based connector also.

**Account ID**

.. setting-salesforce-marketing-cloud-account-id-start

The account ID for the business unit in |destination-name|.

.. setting-salesforce-marketing-cloud-account-id-end

**Append data**

.. setting-salesforce-marketing-cloud-append-data-start

Enable this option to upsert new rows to the data extension and update existing rows.

When not selected, data in the data extension is deleted, and then is updated to match the rows sent from Amperity.

.. setting-salesforce-marketing-cloud-append-data-end

**Data extension name**

.. setting-salesforce-marketing-cloud-data-extension-name-start

The name of the data extension in |destination-name| that is managed by Amperity.

.. setting-salesforce-marketing-cloud-data-extension-name-end

.. setting-salesforce-marketing-cloud-data-extension-name-context-campaigns-start

For campaigns, use the **{campaign_name}** and **{group_name}** campaign template variables to assign campaign and treatment group names to your data extension.

.. important:: The name of a data extension must be unique within |destination-name|.

.. setting-salesforce-marketing-cloud-data-extension-name-context-campaigns-end

.. setting-salesforce-marketing-cloud-data-extension-name-context-orchestrations-start

For orchestrations, assign a name to the data extension that will be added (or updated) by Amperity.

.. important:: The name of a data extension must be unique within |destination-name|, should use underscores ( _ ) instead of spaces, and may not contain *any* of the following characters:

::

   ! @ # $ % ^ * ( ) = { } [ ] \ . < > / " : ? | , &

.. setting-salesforce-marketing-cloud-data-extension-name-context-orchestrations-end

**Folder name**

.. setting-salesforce-marketing-cloud-folder-name-start

The directory within the |destination-name| SFTP site from which the Marketing Cloud SOAP API will get CSV files.

.. setting-salesforce-marketing-cloud-folder-name-end

**Import location**

.. setting-salesforce-marketing-cloud-import-location-start

The directory within the |destination-name| SFTP server into which data should be added. This is also the location from which the Marketing Cloud SOAP API will get the CSV files.

.. setting-salesforce-marketing-cloud-import-location-end

**Primary key**

.. setting-salesforce-marketing-cloud-primary-key-start

Set to one of the following: "subscriber_key" or "email".

Use "subscriber_key" when a field can be mapped directly to the subscriber key in |destination-name|, or else use "email".

.. setting-salesforce-marketing-cloud-primary-key-end

**Subscriber field**

.. setting-salesforce-marketing-cloud-subscriber-field-start

Recommended. The subscriber key for |destination-name|.

.. setting-salesforce-marketing-cloud-subscriber-field-end

.. setting-salesforce-marketing-cloud-subscriber-field-important-start

A subscriber key is configured as the “primary key” for the destination. There are two options: using the |destination-name| subscriber key or using email. One of these options must be specified before the destination can send data to |destination-name|.

.. setting-salesforce-marketing-cloud-subscriber-field-important-end





**SALESFORCE SALES CLOUD**

This section contains settings that are unique to Salesforce Sales Cloud.

**Connect to sandbox instance?**

.. setting-salesforce-sales-cloud-connect-to-sandbox-start

Optional. Select this option if the destination is a sandbox instance (and not a production instance).

.. setting-salesforce-sales-cloud-connect-to-sandbox-end

.. setting-salesforce-sales-cloud-connect-to-sandbox-ignored-start

A sandbox instance is ignored when a custom URL for Salesforce Sales Cloud logins is used.

.. setting-salesforce-sales-cloud-connect-to-sandbox-ignored-end

**Custom Salesforce login URL**

.. setting-salesforce-sales-cloud-custom-login-url-start

Optional. The custom URL for |destination-name| logins requires only the scheme (``http://`` or ``https://``) and hostname parts of the URL. For example: ``http://<hostname>`` or ``https://<hostname>``. The rest of the path is added automatically by Amperity.

.. setting-salesforce-sales-cloud-custom-login-url-end

**External ID field**

.. setting-salesforce-sales-cloud-external-id-field-start

The external ID should be set to "Amperity_ID__c". (The "__c" identifies the field as a custom field in the Salesforce object.)

.. setting-salesforce-sales-cloud-external-id-field-end

**Load data in parallel?**

.. setting-salesforce-sales-cloud-load-data-in-parallel-start

When enabled, NULL values in data sent from Amperity will be ignored during "Upsert" operations. If a field from Amperity is NULL and there is a value in the corresponding Salesforce object, the value in the Salesforce object will be preserved.

.. setting-salesforce-sales-cloud-load-data-in-parallel-end

.. setting-salesforce-sales-cloud-load-data-in-parallel-caution-start

Enabling parallelism may cause Salesforce to process batches in parallel. This may improve performance, but comes with the risk of introducing failures due to locking. It is possible for more than one batch to attempt to obtain a lock on the same row, causing one (or both) batches to fail.

.. setting-salesforce-sales-cloud-load-data-in-parallel-caution-end

**Operation**

.. setting-salesforce-sales-cloud-operation-start

The operation may be one of the following: "Insert", "Upsert" (recommended), "Update", or "Delete". Upsert operations will insert a new record or update an existing record, whereas insert and update operations insert or update (but not both).

.. setting-salesforce-sales-cloud-operation-end

**Salesforce object**

.. setting-salesforce-sales-cloud-salesforce-object-start

The name of the object in Salesforce Sales Cloud to which Amperity will send data.

.. setting-salesforce-sales-cloud-salesforce-object-end

**Use NULL for empty fields?**

.. setting-salesforce-sales-cloud-use-null-for-empty-fields-start

Enable to use NULL values when fields are empty.

.. setting-salesforce-sales-cloud-use-null-for-empty-fields-end





**SFTP**

This section contains settings that are unique to SFTP.

Applies to: Acxiom, Adobe AEP, Adobe Campaign, Adobe Customer Attributes, Airship, BazaarVoice, Bluecore, Evocalize, Experian, Infutor, Kibo (Monetate), Koupon Media, Neustar, Oracle Data Cloud, Oracle DMP, Oracle Responsys, PebblePost, Persado, PowerReviews, Quad, RR Donnelly, Salesforce Marketing Cloud, SMG, SoundCommerce, SFTP, Vibes.

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





**SMG**

See SFTP.





**SNAPCHAT**

This section contains settings that are unique to Snapchat.

**Ad account ID**

.. setting-snapchat-ad-account-id-start

The ID for the |destination-name| advertising account. This ID is available from the top-left menu in |destination-name|. Open that menu, choose "Add Accounts", and then copy the ID for the account to which Amperity will send audiences.

.. setting-snapchat-ad-account-id-end

**Segment name**

.. setting-snapchat-segment-name-start

The name of the audience in |destination-name| that is managed by Amperity. This audience will be created by Amperity if it does not exist. The audience will be available from the |destination-name| "Audiences" page.

.. setting-snapchat-segment-name-end







**SNOWFLAKE**

This section contains settings that are unique to Snowflake.

**Account name**

.. setting-snowflake-account-name-start

The account name is contained within the URL for the Snowflake instance and is a character code located before ``snowflakecomputing.com``. For example: "ab12345".

.. setting-snowflake-account-name-end

**Create table?**

.. setting-snowflake-create-table-start

Use the Create table option when the table should be created in Snowflake if it is not already there.

.. setting-snowflake-create-table-end

**Drop table?**

.. setting-snowflake-drop-table-start

Use the Drop table option to overwrite the table and apply an updated schema when the upstream segment or table changes.

.. setting-snowflake-drop-table-end

**Region ID**

.. setting-snowflake-region-id-start

The ID for the region in which the Snowflake account name is located. For example: "us-west-2".

.. setting-snowflake-region-id-end

.. setting-snowflake-region-id-location-start

.. note:: The Amperity instance of Snowflake should be located in the same region as the customer's instance of Snowflake.

.. setting-snowflake-region-id-location-end

**Snowflake location**

.. setting-snowflake-location-start

The table to which data will be loaded. This location is defined using a period-delimited list of Snowflake database name, Snowflake schema name, and Snowflake table name. For example:

::

   SNOWFLAKE_DATABASE_NAME.SNOWFLAKE_SCHEMA.TABLE_NAME

.. setting-snowflake-location-end

**Stage**

.. setting-snowflake-stage-start

The Snowflake stage name, which is created by the `CREATE STAGE <https://docs.snowflake.com/en/sql-reference/sql/create-stage>`__ |ext_link| command. For example:

``AMPERITY_ABCDEF.CUSTOMER_360.AMP_PROD_STAGE``

.. setting-snowflake-stage-end

**Truncate table?**

.. setting-snowflake-truncate-table-start

Use the Truncate table option when the contents of the table should be emptied prior to loading data.

.. setting-snowflake-truncate-table-end

**Warehouse**

.. setting-snowflake-warehouse-start

The name of the Snowflake data warehouse. This is created by the `CREATE WAREHOUSE <https://docs.snowflake.com/en/sql-reference/sql/create-warehouse>`__ |ext_link| command. For example:

``AMPERITY_WH``

.. setting-snowflake-warehouse-end





**SOUND COMMERCE**

See SFTP.





**THE TRADE DESK**

This section contains settings that are unique to The Trade Desk.

**Membership duration**

See common.

.. setting-the-trade-desk-membership-duration-minmax-start

The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the default duration. The maximum value is "180".

.. setting-the-trade-desk-membership-duration-minmax-end

.. setting-the-trade-desk-membership-duration-example-start

The membership duration is measured in days. Adjust the membership duration value to be greater than (or equal to) than the frequency at which your brand will send campaigns or orchestrations from Amperity.

For example, if your brand sends a campaign to |destination-name| every 30 days, then the membership duration should be set to "30". If your brand sends a campaign every 14 days, then the membership duration should be set to "14".

If a campaign is sent every 30 days, but the membership duration is 14, then the audience size for the last 16 days of the duration window will be 0.

.. setting-the-trade-desk-membership-duration-example-end

**Segment name**

.. setting-the-trade-desk-segment-name-start

The name of a segment in |destination-name|.

.. setting-the-trade-desk-segment-name-end

**UID 2.0 agreement**

.. setting-the-trade-desk-uid2-agreement-start

|destination-name| supports using `UID 2.0 <https://unifiedid.com/docs/intro>`__ |ext_link| to help establish your customers' identifies without using third-party data. UID 2.0 enables publisher websites, mobile apps, and Connected TV (CTV) apps to monetize through programmatic workflows, while offering user transparency and privacy controls that meet local market requirements.

Your brand must have a UID 2.0 agreement in-place with The Trade Desk before configuring Amperity to send offline events to |destination-name|.

.. setting-the-trade-desk-uid2-agreement-end




**THE TRADE DESK: 3P MARKETPLACE**

This section contains settings that are unique to The Trade Desk (3P Marketplace).

**Membership duration**

See common.

**Segment taxonomy ID**

.. setting-the-trade-desk-3p-segment-taxonomy-id-start

The taxonomy ID for a monetized segment in The Trade Desk.

.. setting-the-trade-desk-3p-segment-taxonomy-id-end





**THE TRADE DESK: OFFLINE EVENTS**

This section contains settings that are unique to The Trade Desk: Offline Events.

**Tracking tag name**

.. setting-the-trade-desk-offline-tracking-tag-name-start

The name of the tracking tag for which offline events are associated. The name is a string, may have up to 256 characters, must be unique, and may not duplicate any previous name that was used for the same advertiser and offline data provider ID. The tracking tag name will appear in the UI for |destination-name| exactly as it is entered in Amperity.

.. setting-the-trade-desk-offline-tracking-tag-name-end

.. setting-the-trade-desk-offline-tracking-tag-name-context-start

|destination-name| uses a combination of the tracking tag name, your brand's advertiser ID, and offline data provider ID to build a unique offline tracking tag ID. Use the offline tracking ID to help measure the success of your brand's marketing campaigns.

.. setting-the-trade-desk-offline-tracking-tag-name-context-end





**TIKTOK ADS MANAGER**

This section contains settings that are unique to TikTok Ads Manager.

**Advertiser ID**

.. setting-tiktok-ads-manager-advertiser-id-start

The advertiser ID for your |destination-name| account. This is a nineteen character string similar to “7654321098765432109” that you can find from the drop-down menu in the top right of TikTok Ads Manager.

.. setting-tiktok-ads-manager-advertiser-id-end

**Custom audience name**

.. setting-tiktok-ads-manager-custom-audience-name-start

The name of the audience in |destination-name| that is managed by Amperity. This audience will be created by Amperity if it does not exist.

.. setting-tiktok-ads-manager-custom-audience-name-end

**User ID type**

.. setting-tiktok-ads-manager-user-id-type-start

The user ID type. This value must be one of the following: "AAID" (Google), "EMAIL" (email addresses), "IDFA" (Apple), or "PHONE" (phone numbers). Amperity is configured to send "EMAIL" and "PHONE" by default for campaigns.

.. setting-tiktok-ads-manager-user-id-type-end




**TIKTOK ADS MANAGER: OFFLINE EVENTS**

This section contains settings that are unique to TikTok Ads Manager: Offline Events.

**Advertiser ID**

.. setting-tiktok-ads-manager-offline-advertiser-id-start

TEMP: "The advertiser ID of the TikTok Ads account you want to use. + TikTok Ads Advertiser ID"

.. setting-tiktok-ads-manager-offline-advertiser-id-end

**Auto tracking?**

.. setting-tiktok-ads-manager-offline-auto-tracking-start

Select **Auto tracking** to use this event set for add tracking and attribution.

.. setting-tiktok-ads-manager-offline-auto-tracking-end

**Event set ID**

.. setting-tiktok-ads-manager-offline-event-set-id-start

The event set ID is a nineteen character string similar to “7654321098765432109”.

.. setting-tiktok-ads-manager-offline-event-set-id-end

.. setting-tiktok-ads-manager-offline-event-set-id-context-start

The event set must exist before you can send data to it from Amperity. You can `create an event set ID <https://business-api.tiktok.com/portal/docs?id=1771101027431425>`__ |ext_link| from the |destination-name| user interface.

If the event set ID already exists, from the TikTok Ads user interface open **Assets**, then **Events**, and then from the **Offline** box select **Manage**. Each event set will have its own card; the event set ID is located under the name of the event set.

.. setting-tiktok-ads-manager-offline-event-set-id-context-end

**Event set name**

.. setting-tiktok-ads-manager-offline-event-set-name-start

The name of the offline events set in TikTok Ads Manager.

.. setting-tiktok-ads-manager-offline-event-set-name-end

**Event source**

.. setting-tiktok-ads-manager-offline-event-source-start

The type of event to be uploaded to TikTok Ads Manager. May be one of “web” or "offline". Use "web" for events that took place on your website and were collected using the `payload helper <https://business-api.tiktok.com/portal/docs?id=1807346079965186>`__ |ext_link|. Use "offline" for events that took place in a physical store and are measured by an offline event set ID.

.. setting-tiktok-ads-manager-offline-event-source-end





**VIBES**

See SFTP.

**Filename template**

.. setting-vibes-filename-template-pattern-start

A |destination-name| `recipient list <https://developer-platform.vibes.com/docs/recipient-list-import>`__ |ext_link| must be assigned a name similar to "<filename>.recipient_list".

.. setting-vibes-filename-template-pattern-end




**WEBHOOK**

**Label name**

**Settings**




**YAHOO DSP**

**Short intro**

.. setting-yahoo-dsp-intro-start

Yahoo DSP is a demand-side platform (DSP) to which you can send audiences, and then advertise across the Yahoo brand ecosystem.

.. setting-yahoo-dsp-intro-end

**Membership duration**

Days. See common.

**Segment name**

.. setting-yahoo-dsp-segment-name-start

The name of the segment in |destination-name|. This can be the name of an existing segment or a new segment within the |destination-name| taxonomy. Segments are available in |destination-name| from "Audiences". Open the "Partner" audiences, and then choose "Amperity".

.. setting-yahoo-dsp-segment-name-start




**ZENDESK**

This section contains settings that are unique to Zendesk.

**Subdomain**

.. setting-zendesk-subdomain-start

Required. The subdomain for your brand's Zendesk account. For example: "socktown" is the subdomain for "socktown.zendesk.com".

.. setting-zendesk-subdomain-end
