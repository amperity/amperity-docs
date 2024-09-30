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

After this destination is configured, business users may configure Amperity to |sendto-link| and |channel-link| to |destination-name|.

.. destinations-steps-business-users-end




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

The escape character to use in the file output.

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

Add a name and description for this destination.

.. setting-common-name-and-description-end

**Optional settings**

.. setting-common-optional-settings-start

All other Amperity file formatt settings for |destination-name| are optional.

.. setting-common-optional-settings-end

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

The instance within Amazon Marketing Cloud to which your brand will send audiences.

.. setting-amazon-ads-amc-instance-end

**Audience description**

.. setting-amazon-ads-audience-description-start

A description of the audience that is managed by Amperity.

.. setting-amazon-ads-audience-description-end

**Audience name**

.. setting-amazon-ads-audience-description-start

The name of the audience that is managed by Amperity.

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





**ATTENTIVE (API)**

This section contains settings that are unique to Attentive (API).

**Primary Identifier**

.. setting-attentive-primary-identifier-start

TEMP: "The primary identifier within your |destination-name| account."

.. setting-attentive-primary-identifier-end





**ATTENTIVE (SFTP)**

This section contains settings that are unique to Attentive (SFTP).

See SFTP for all common file settings.

**Client domain**

.. setting-attentive-primary-identifier-start

TEMP: "The client domain of the Attentive instance"

.. setting-attentive-primary-identifier-end





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

TEMP: "The instance where the Braze account was provisioned"

.. setting-braze-instance-end

**Profile updates?**

.. setting-braze-profile-updates-start

TEMP: "Only send updated audience profiles."

.. setting-braze-profile-updates-end

**User identifier**

.. setting-braze-user-identifier-start

TEMP: "The indentifier used to match users in Braze"

.. setting-braze-user-identifier-end





**CAMELOT SMM**

See SFTP.





**CORDIAL**

This section contains settings that are unique to Cordial.

**Audience primary key**

See common settings.

**List name**

.. setting-cordial-list-name-start

TEMP: "xxxxx"

.. setting-cordial-list-name-end

**Subscription status**

.. setting-cordial-subscription-status-start

UI field name: "Do not set subscription status automatically"

UI description: "Prevents updates without a channels.email.subscribeStatus from being automatically subscribed"

TEMP: "Prevents updates without a channels.email.subscribeStatus from being automatically subscribed"

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

The list name to which the |destination-name| connector will write. This can be the name of an existing list or a new list.

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

xxxxx

.. setting-klaviyo-list-name-end

**Update contacts?**

.. setting-klaviyo-update-contacts-start

TEMP: "Use full profile to update list"

.. setting-klaviyo-update-contacts-end





**KOUPON MEDIA**

See SFTP.





**LISTRAK**

This section contains settings that are unique to Listrak.

**Audience primary key**

See common settings.

**Field group**

.. setting-listrak-field-group-start

TEMP: "The field group to use for audience and attribute fields"

.. setting-listrak-field-group-end

**List name**

.. setting-listrak-list-name-start

The name of the list that will be managed in |destination-name|. This is often, but not always, named "Master List".

.. setting-listrak-list-name-end

**Segment name**

.. setting-listrak-segment-name-start

TEMP: "xxxxx"

.. setting-listrak-segment-name-end





**LIVERAMP**

See SFTP.





**MAILCHIMP**

This section contains settings that are unique to Mailchimp.

**Data center**

.. setting-mailchimp-data-center-start

TEMP: "The data center to used to talk to the Mailchimp API"

.. setting-mailchimp-data-center-end

**List ID**

.. setting-mailchimp-list-id-start

TEMP: "The id of the list to insert members"

.. setting-mailchimp-list-id-end





**META ADS MANAGER**

This section contains settings that are unique to Meta Ads Manager.

**Account ID**

.. setting-meta-ads-manager-account-id-start

TEMP: "Ad account ID"

.. setting-meta-ads-manager-account-id-end

**Custom audience name**

.. setting-meta-ads-manager-custom-audience-name-start

TEMP: "xxxxx"

.. setting-meta-ads-manager-custom-audience-name-end

**Customer file source**

.. setting-meta-ads-manager-customer-file-source-start

TEMP: "Where the data was sourced from for the custom audience (directly from users, 3rd party, or both)"

.. setting-meta-ads-manager-customer-file-source-end





**META ADS MANAGER: OFFLINE EVENTS**

This section contains settings that are unique to Meta Ads Manager: Offline Events.

**Dataset ID**

.. setting-meta-ads-manager-dataset-id-start

TEMP: "The dataset to associate your offline events with."

.. setting-meta-ads-manager-dataset-id-end





**MICROSOFT ADVERTISING**

This section contains settings that are unique to Microsoft Advertising.

**Account ID**

.. setting-microsoft-advertising-account-id-start

TEMP: "Microsoft Ads account ID"

.. setting-microsoft-advertising-account-id-end

**Audience primary key**

See common settings.

**Customer ID**

.. setting-microsoft-advertising-customer-id-start

TEMP: "Customer ID for the Microsoft Ads account"

.. setting-microsoft-advertising-customer-id-end





**MICROSOFT DATAVERSE**

This section contains settings that are unique to Microsoft Dataverse.

**Dataverse table logical name**

.. setting-microsoft-dataverse-table-logical-name-start

TEMP: "xxxxx"

.. setting-microsoft-dataverse-table-logical-name-end

**Power Apps environment name**

.. setting-microsoft-dataverse-powerapps-name-start

TEMP: "xxxxx"

.. setting-microsoft-dataverse-powerapps-name-end

**Power Apps environment region**

.. setting-microsoft-dataverse-powerapps-region-start

TEMP: "xxxxx"

.. setting-microsoft-dataverse-powerapps-region-end

**Truncate table?**

.. setting-microsoft-dataverse-truncate-table-start

TEMP: "xxxxx"

.. setting-microsoft-dataverse-truncate-table-end





**MICROSOFT DYNAMICS 365 MARKETING**

This section contains settings that are unique to Microsoft Dynamics 365 Marketing.

**Dynamics 365 marketing segment name**

.. setting-microsoft-dynamics-365-segment-name-start

TEMP: "The name for your Dynamics 365 Marketing Segment."

.. setting-microsoft-dynamics-365-segment-name-end

**Power Apps environment name**

.. setting-microsoft-dynamics-365-environment-name-start

TEMP: "The unique name for your Power Apps environment. For example: “acme”."

.. setting-microsoft-dynamics-365-environment-name-end

**Power Apps environment region**

.. setting-microsoft-dynamics-365-environment-region-start

TEMP: "The region in which your data center is located. For example: “crm”."

.. setting-microsoft-dynamics-365-environment-region-end





**MICROSOFT DYNAMICS**

This section contains settings that are unique to Microsoft Dynamics.

**Azure Active Directory ID**

.. setting-microsoft-dynamics-azure-ad-id-start

TEMP: "The tenant identifier"

.. setting-microsoft-dynamics-azure-ad-id-end

**Dynamics entity**

.. setting-microsoft-dynamics-entity-start

TEMP: "The dynamics entity"

.. setting-microsoft-dynamics-entity-end

**Dynamics URL**

.. setting-microsoft-dynamics-url-start

TEMP: "The URL of the customers Dynamics instance"

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

See common settings.

**Shared list name**

.. setting-oracle-eloqua-shared-list-name-start

TEMP: "The shared list name in Eloqua to update. It will be created if it doesn't currently exist"

.. setting-oracle-eloqua-shared-list-name-end





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

TEMP: "The Ad Account ID for Pinterest"

.. setting-pinterest-ad-account-id-end

**Audience primary key**

See common settings.





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

?????

.. setting-sailthru-list-name-end





**SALESFORCE MARKETING CLOUD**

This section contains settings that are unique to Salesforce Marketing Cloud.

Note: There is an SFTP-based connector also.

**Account ID**

.. setting-salesforce-marketing-cloud-account-id-start

TEMP: "xxxxx"

.. setting-salesforce-marketing-cloud-account-id-end

**Append data**

.. setting-salesforce-marketing-cloud-append-data-start

TEMP: "Append onto the data extension"

.. setting-salesforce-marketing-cloud-append-data-end

**Folder name**

.. setting-salesforce-marketing-cloud-folder-name-start

TEMP: "Name of the folder you wish to send the data to"

.. setting-salesforce-marketing-cloud-folder-name-end

**Import location**

.. setting-salesforce-marketing-cloud-import-location-start

TEMP: "File transfer location object name that points to the import directory"

.. setting-salesforce-marketing-cloud-import-location-end

**Primary key**

.. setting-salesforce-marketing-cloud-primary-key-start

TEMP: "Field to be used as the customer primary key in SFMC"

.. setting-salesforce-marketing-cloud-primary-key-end

**Subscriber field**

.. setting-salesforce-marketing-cloud-subscriber-field-start

TEMP: "Field to be used as the customer subscriber field in SFMC" May be: "Subscriber key" or "Email address".

.. setting-salesforce-marketing-cloud-subscriber-field-end





**SALESFORCE SALES CLOUD**

This section contains settings that are unique to Salesforce Sales Cloud.

**Connect to sandbox instance?**

.. setting-salesforce-sales-cloud-connect-to-sandbox-start

TEMP: "Set to 'Yes' to connect to a Salesforce sandbox for testing rather than a production instance. (Note: this setting is ignored if a custom login url is specified)"

.. setting-salesforce-sales-cloud-connect-to-sandbox-end

**Custom Salesforce login URL**

.. setting-salesforce-sales-cloud-custom-login-url-start

TEMP: "Login to Salesforce using a custom url. Specify the scheme and host part only. The path will be set automatically."

.. setting-salesforce-sales-cloud-custom-login-url-end

**External ID field**

.. setting-salesforce-sales-cloud-external-id-field-start

TEMP: "The external ID field to use to identify existing objects to update when performing an upsert load."

.. setting-salesforce-sales-cloud-external-id-field-end

**Load data in parallel?**

.. setting-salesforce-sales-cloud-load-data-in-parallel-start

TEMP: "Whether or not batches of data should be loaded in parallel. Parallelism may increase performance, but it can also cause lock contention for highly overlapping data."

.. setting-salesforce-sales-cloud-load-data-in-parallel-end

**Operation**

.. setting-salesforce-sales-cloud-operation-start

TEMP: "The type of API operation to perform with the input data."

.. setting-salesforce-sales-cloud-operation-end

**Salesforce object**

.. setting-salesforce-sales-cloud-salesforce-object-start

TEMP: "The Salesforce object that the data should be loaded into."

.. setting-salesforce-sales-cloud-salesforce-object-end

**Use NULL for empty fields?**

.. setting-salesforce-sales-cloud-use-null-for-empty-fields-start

TEMP: Convert empty fields in the data set to null values. When false empty fields will be ignored.

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

TEMP: "The ID of the ad account to create/update"

.. setting-snapchat-ad-account-id-end





**SNOWFLAKE**

This section contains settings that are unique to Snowflake.

**Account name**

.. setting-snowflake-account-name-start

TEMP: "The name of the Snowflake account"

.. setting-snowflake-account-name-end

**Create table?**

.. setting-snowflake-create-table-start

TEMP: "Create table if not present?"

.. setting-snowflake-create-table-end

**Drop table?**

.. setting-snowflake-drop-table-start

TEMP: "Drop table before loading data?"

.. setting-snowflake-drop-table-end

**Region ID**

.. setting-snowflake-region-id-start

TEMP: "The ID for the Snowflake region where the account is located"

.. setting-snowflake-region-id-end

**Snowflake location**

.. setting-snowflake-snowflake-location-start

TEMP: "The target Snowflake location to export data to (format: Database.Schema[.Table])."

.. setting-snowflake-snowflake-location-end

**Stage**

.. setting-snowflake-stage-start

TEMP: "The external stage used for staging the data. Case sensitive."

.. setting-snowflake-stage-end

**Truncate table?**

.. setting-snowflake-truncate-table-start

TEMP: "Truncate table before loading data?"

.. setting-snowflake-truncate-table-end

**Warehouse**

.. setting-snowflake-warehouse-start

TEMP: "The Snowflake Virtual Warehouse to use when loading and transforming data"

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





**THE TRADE DESK: 3P MARKETPLACE**

This section contains settings that are unique to The Trade Desk (3P Marketplace).

**Membership duration**

See common.

See extra info at The Trade Desk.





**THE TRADE DESK: OFFLINE EVENTS**

This section contains settings that are unique to The Trade Desk: Offline Events.

**Tracking tag name**

.. setting-the-trade-desk-offline-tracking-tag-name-start

TEMP: "The tracking tag name to associate your offline events with."

.. setting-the-trade-desk-offline-tracking-tag-name-end





**TIKTOK ADS MANAGER**

This section contains settings that are unique to TikTok Ads Manager.

**Advertiser ID**

.. setting-tiktok-ads-manager-advertiser-id-start

TEMP: "The advertiser ID of the TikTok Ads account you want to use. + TikTok Ads Advertiser ID"

.. setting-tiktok-ads-manager-advertiser-id-end

**Custom audience name**

.. setting-tiktok-ads-manager-custom-audience-name-start

?????

.. setting-tiktok-ads-manager-custom-audience-name-end

**User ID type**

.. setting-tiktok-ads-manager-user-id-type-start

TEMP: "Audience primary key type." May be: IDFA, AAID, EMAIL, PHONE.

.. setting-tiktok-ads-manager-user-id-type-end




**TIKTOK ADS MANAGER: OFFLINE EVENTS**

This section contains settings that are unique to TikTok Ads Manager: Offline Events.

**Advertiser ID**

.. setting-tiktok-ads-manager-offline-advertiser-id-start

TEMP: "The advertiser ID of the TikTok Ads account you want to use. + TikTok Ads Advertiser ID"

.. setting-tiktok-ads-manager-offline-advertiser-id-end

**Event set ID**

.. setting-tiktok-ads-manager-offline-event-set-id-start

TEMP: "Event Set ID"

.. setting-tiktok-ads-manager-offline-event-set-id-end




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
