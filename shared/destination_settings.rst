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




**COMMON**

This section contains settings that are identical across more than one destination.

.. TODO: Compare Amazon S3, Azure Blob Storage, Google Cloud Storage, and SFTP for common settings.

**Audience primary key**

Applies to: ActiveCampaign, Cordial, Criteo, HubSpot, Klaviyo, Listrak, Microsoft Ads, Oracle Eloqua, Pinterest, and Sailthru.

.. setting-common-audience-primary-key-start

The primary key for the audience. Set to "email".

.. setting-common-audience-primary-key-end

**Business user access**

.. TODO: These two settings are in an admonition block in docs pages; definition list in modals.

.. setting-common-business-user-access-allow-start

Select the **Allow business users** option to allow access to |destination-name| for users who are assigned the **Amp360 User** and/or **AmpIQ User** policies.

.. setting-common-business-user-access-allow-end

.. setting-common-business-user-access-restrict-pii-start

Some business users may have restricted access to PII, which will prevent them from sending data to |destination-name|. Select the **Allow limited PII access** option to allow access to |destination-name| for users who are assigned the **Restrict PII access** policy option.

.. setting-common-business-user-access-restrict-pii-end

**Compression**

.. setting-common-compression-start

The compression format to apply to the output file. May be one of "GZIP", "None", "TAR", "TGZ", or "ZIP". 

.. setting-common-compression-end

**Escape character**

.. setting-common-escape-character-start

The escape character that is required by |destination-name|.

.. setting-common-escape-character-end

.. setting-common-escape-character-unspecified-start

When an escape character is not specified *and* the quote mode is "None" files may be sent with unescaped and unquoted data. When an escape character is not specified, you should select a non-"None" option as the quote mode.

.. setting-common-escape-character-unspecified-end

**File format**

.. setting-common-file-format-start

Send |file-format| to |destination-name|.

.. setting-common-file-format-end

.. setting-common-file-format-custom-delimiter-start

Some file formats allow a custom delimiter. Choose the "Custom delimiter" file format, and then add a single character to represent the custom delimiter.

.. setting-common-file-format-custom-delimiter-end

**Filename template**

.. include:: ../../shared/terms.rst
   :start-after: .. term-filename-template-start
   :end-before: .. term-filename-template-end

**Header?**

.. setting-common-header-start

Enable to include header rows in output files.

.. setting-common-header-end

**Line ending**

.. setting-common-line-ending-start

The line ending to use in file output. May be one of "LF" or "CRLF".

.. setting-common-line-ending-end

**List name**

Applies to: currently unknown. Look at ActiveCampaign, Cordial, HubSpot, Klaviyo, and Listrak. Try to come up with some type of template.

.. setting-common-list-name-start

The primary key for the audience. Set to "email".

.. setting-common-list-name-end

**PGP public key**

.. setting-common-pgp-public-key-start

The PGP public key that Amperity uses to encrypt files that are sent to |destination-name|.

.. setting-common-pgp-public-key-end

**Quote mode**

.. setting-common-quote-mode-start

The quote mode to use within the file. May be one of "all fields", "all non-NULL fields", "fields with special characters only", "all non-numeric fields" or "None".

.. setting-common-quote-mode-end

.. setting-common-quote-mode-none-start

Unescaped, unquoted files may occur when quote mode is set to "None" and an escape character is not specified.

.. setting-common-quote-mode-none-end

**Remote folder**

.. setting-common-remote-folder-start

The remote folder to which Amperity will send data.

.. setting-common-remote-folder-end

.. setting-common-remote-folder-forward-slash-start

A "/" (forward slash) must be used as the first character for this value. For example: "/folder/name".

.. setting-common-remote-folder-forward-slash-end

.. setting-common-remote-folder-spaces-start

If the path to the remote folder contains a space, use a backslash (\) character to escape that space. For example, a folder named "From ACME" should be entered as "From\ ACME".

.. setting-common-remote-folder-spaces-end

**Success file**

.. setting-common-success-file-start

Enable to send a .DONE file when Amperity has finished sending data.

.. setting-common-success-file-end

.. setting-common-success-file-downstream-start

If a downstream sensor is listening for files sent from Amperity, configure that sensor to listen for the presence of the .DONE file.

.. setting-common-success-file-downstream-end

**Use Zip64?**

.. setting-common-use-zip64-start

Enable to apply data compression to very large files.

.. setting-common-use-zip64-end





**ACTIVECAMPAIGN**

This section contains settings that are unique to ActiveCampaign.

**Audience primary key**

See common settings.

**Group name**

.. setting-active-campaign-group-name-start

The user group to which Amperity will send data. This group must exist in |destination-name| and must have permission to view and interact with the contact list.

.. setting-active-campaign-group-name-end

**List name**

.. setting-active-campaign-list-name-start

The name of the contact list in |destination-name| that will be managed by Amperity.

.. setting-active-campaign-list-name-end

**Verbose logging**

.. setting-active-campaign-verbose-logging-start

Enable to return log details when |destination-name| rejects adding contacts to the contact list.

When this setting is enabled, a list of rejected contacts is returned by the response from ActiveCampaign. For each rejected contact, a contact identifier is provided along with a string that describes the reason why the contact was rejected.

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

**xxxxx**

.. setting-xxxxx-xxxxx-start

xxxxx

.. setting-xxxxx-xxxxx-end





**AIRSHIP**

See SFTP.





**AMAZON ADS**

This section contains settings that are unique to Amazon Ads.

**AMC instance**

.. setting-amazon-ads-amc-instance-start

xxxxx

.. setting-amazon-ads-amc-instance-end

**DSP advertiser**

.. setting-amazon-ads-dsp-advertiser-start

xxxxx

.. setting-amazon-ads-dsp-advertiser-end





**AMAZON S3**

This section contains settings that are unique to Amazon S3.

Applies to: Amazon S3, Cheetah Digital, Domo, Optimizely.

**Compression**

See Common.

**Escape character**

See Common.

**File format**

See Common.

**Filename template**

See Common.

**Header?**

See Common.

**PGP public key**

See Common.

**Quote mode**

See Common.

**S3 prefix**

.. setting-amazon-s3-s3-prefix-start

xxxxx

.. setting-amazon-s3-s3-prefix-end

**Success file**

See Common.

**Use Zip64?**

See Common.





**ATTENTIVE (API)**

This section contains settings that are unique to Attentive (API).

**Primary Identifier**

.. setting-attentive-primary-identifier-start

xxxxx

.. setting-attentive-primary-identifier-end





**ATTENTIVE (SFTP)**

This section contains settings that are unique to Attentive (SFTP).

See SFTP.





**AZURE BLOB STORAGE**

This section contains settings that are unique to Azure Blob Storage.

Applies to: Azure Blob Storage.

**Blob prefix**

.. setting-azure-blob-storage-blob-prefix-start

xxxxx

.. setting-azure-blob-storage-blob-prefix-end

**Compression**

See Common.

**Escape character**

See Common.

**File format**

See Common.

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





**BRAZE**

This section contains settings that are unique to Braze.

**Instance**

.. setting-braze-instance-start

xxxxx

.. setting-braze-instance-end

**Profile updates?**

.. setting-braze-profile-updates-start

xxxxx

.. setting-braze-profile-updates-end

**User identifier**

.. setting-braze-user-identifier-start

xxxxx

.. setting-braze-user-identifier-end





**CAMELOT SMM**

See SFTP.





**CORDIAL**

This section contains settings that are unique to Cordial.

**Audience primary key**

See common settings.

**List name**

.. setting-cordial-list-name-start

xxxxx

.. setting-cordial-list-name-end

**Subscription status**

.. setting-cordial-subscription-status-start

UI field name: "Do not set subscription status automatically"

UI description: "Prevents updates without a channels.email.subscribeStatus from being automatically subscribed"

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

.. setting-google-ads-audiewnce-description-start

xxxxx

.. setting-google-ads-audiewnce-description-end


**Audience name**

.. setting-google-ads-audiewnce-name-start

xxxxx

.. setting-google-ads-audiewnce-name-end

**Customer ID**

.. setting-google-ads-customer-id-start

xxxxx

.. setting-google-ads-customer-id-end

**Membership duration**

.. setting-google-ads-membership-duration-start

xxxxx

.. setting-google-ads-membership-duration-end

**Mobile app ID**

.. setting-google-ads-mobile-app-id-start

xxxxx

.. setting-google-ads-mobile-app-id-end

**Upload key type**

.. setting-google-ads-upload-key-type-start

xxxxx

.. setting-google-ads-upload-key-type-end





**GOOGLE CLOUD STORAGE**

This section contains settings that are unique to Google Cloud Storage.

Applies to: Google Cloud Storage.

**Compression**

See Common.

**Escape character**

See Common.

**File format**

See Common.

**Filename template**

See Common.

**Header?**

See Common.

**Object prefix**

.. setting-google-cloud-storage-object-prefix-start

xxxxx

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

**Customer ID**

.. setting-google-customer-match-customer-id-start

xxxxx

.. setting-google-customer-match-customer-id-end

**Compression**

.. setting-google-customer-match-customer-product-start

xxxxx

.. setting-google-customer-match-customer-product-end





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

xxxxx

.. setting-klaviyo-update-contacts-end





**KOUPON MEDIA**

See SFTP.





**LISTRAK**

This section contains settings that are unique to Listrak.

**Audience primary key**

See common settings.

**Field group**

.. setting-listrak-field-group-start

xxxxx

.. setting-listrak-field-group-end

**List name**

.. setting-listrak-list-name-start

The name of the list that will be managed in |destination-name|. This is often, but not always, named "Master List".

.. setting-listrak-list-name-end

**Segment name**

.. setting-listrak-segment-name-start

xxxxx

.. setting-listrak-segment-name-end





**LIVERAMP**

See SFTP.





**MAILCHIMP**

This section contains settings that are unique to Mailchimp.

**Data center**

.. setting-mailchimp-data-center-start

xxxxx

.. setting-mailchimp-data-center-end





**META ADS MANAGER**

This section contains settings that are unique to Meta Ads Manager.

**Account ID**

.. setting-meta-ads-manager-account-id-start

xxxxx

.. setting-meta-ads-manager-account-id-end

**Custom audience name**

.. setting-meta-ads-manager-custom-audience-name-start

xxxxx

.. setting-meta-ads-manager-custom-audience-name-end

**Customer file source**

.. setting-meta-ads-manager-customer-file-source-start

xxxxx

.. setting-meta-ads-manager-customer-file-source-end





**META ADS MANAGER: OFFLINE EVENTS**

This section contains settings that are unique to Meta Ads Manager: Offline Events.

**Dataset ID**

.. setting-meta-ads-manager-dataset-id-start

xxxxx

.. setting-meta-ads-manager-dataset-id-end





**MICROSOFT ADVERTISING**

This section contains settings that are unique to Microsoft Advertising.

**Account ID**

.. setting-microsoft-advertising-account-id-start

xxxxx

.. setting-microsoft-advertising-account-id-end

**Audience primary key**

See common settings.

**Customer ID**

.. setting-microsoft-advertising-customer-id-start

xxxxx

.. setting-microsoft-advertising-customer-id-end





**MICROSOFT DATAVERSE**

This section contains settings that are unique to Microsoft Dataverse.

**Power Apps environment name**

.. setting-microsoft-dataverse-powerapps-name-start

xxxxx

.. setting-microsoft-dataverse-powerapps-name-end

**Power Apps environment region**

.. setting-microsoft-dataverse-powerapps-region-start

xxxxx

.. setting-microsoft-dataverse-powerapps-region-end





**MICROSOFT DYNAMICS 365 MARKETING**

This section contains settings that are unique to Microsoft Dynamics 365 Marketing.

**xxxxx**

.. setting-xxxxx-xxxxx-start

xxxxx

.. setting-xxxxx-xxxxx-end





**MICROSOFT DYNAMICS**

This section contains settings that are unique to Microsoft Dynamics.

**Azure Active Directory ID**

.. setting-microsoft-dynamics-azure-ad-id-start

xxxxx

.. setting-microsoft-dynamics-azure-ad-id-end

**Dynamics URL**

.. setting-microsoft-dynamics-url-start

xxxxx

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

xxxxx

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

xxxxx

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

xxxxx?

.. setting-sailthru-list-name-end





**SALESFORCE MARKETING CLOUD**

This section contains settings that are unique to Salesforce Marketing Cloud.

Note: There is an SFTP-based connector also.

**Account ID**

.. setting-salesforce-marketing-cloud-account-id-start

xxxxx

.. setting-salesforce-marketing-cloud-account-id-end

**Folder name**

.. setting-salesforce-marketing-cloud-folder-name-start

xxxxx

.. setting-salesforce-marketing-cloud-folder-name-end

**Import location**

.. setting-salesforce-marketing-cloud-import-location-start

xxxxx

.. setting-salesforce-marketing-cloud-import-location-end

**Primary key**

.. setting-salesforce-marketing-cloud-primary-key-start

xxxxx

.. setting-salesforce-marketing-cloud-primary-key-end

**Subscriber field**

.. setting-salesforce-marketing-cloud-subscriber-field-start

xxxxx. "Subscriber key" or "Email address".

.. setting-salesforce-marketing-cloud-subscriber-field-end





**SALESFORCE SALES CLOUD**

This section contains settings that are unique to Salesforce Sales Cloud.

**Connect to sandbox instance?**

.. setting-salesforce-sales-cloud-connect-to-sandbox-start

xxxxx

.. setting-salesforce-sales-cloud-connect-to-sandbox-end

**Custom Salesforce login URL**

.. setting-salesforce-sales-cloud-custom-login-url-start

xxxxx

.. setting-salesforce-sales-cloud-custom-login-url-end

**Salesforce object**

.. setting-salesforce-sales-cloud-salesforce-object-start

xxxxx

.. setting-salesforce-sales-cloud-salesforce-object-end





**SFTP**

This section contains settings that are unique to SFTP.

Applies to: Acxiom, Adobe AEP, Adobe Campaign, Adobe Customer Attributes, Airship, BazaarVoice, Bluecore, Evocalize, Experian, Infutor, Kibo (Monetate), Koupon Media, Neustar, Oracle Data Cloud, Oracle DMP, Oracle Responsys, PebblePost, Persado, PowerReviews, SFTP, Vibes.

**About**

.. setting-sftp-about-start

`Secure File Transfer Protocol (SFTP) <https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol>`__ is a network protocol that provides file access, file transfer, and file management over any reliable data stream.

.. setting-sftp-about-end

**Compression**

See Common.

**Escape character**

See Common.

**File format**

See Common.

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

xxxxx

.. setting-snapchat-ad-account-id-end





**SNOWFLAKE**

This section contains settings that are unique to Snowflake.

**Account name**

.. setting-snowflake-account-name-start

xxxxx

.. setting-snowflake-account-name-end

**Region ID**

.. setting-snowflake-region-id-start

xxxxx

.. setting-snowflake-region-id-end

**Stage**

.. setting-snowflake-stage-start

xxxxx

.. setting-snowflake-stage-end

**Warehouse**

.. setting-snowflake-warehouse-start

xxxxx

.. setting-snowflake-warehouse-end





**SOUND COMMERCE**

See SFTP.





**THE TRADE DESK**

This section contains settings that are unique to The Trade Desk.

**Membership duration**

.. setting-the-trade-desk-membership-duration-start

Membership duration defines the length of time (in days) at which individual audience members will belong to the segment in |destination-name|.

.. setting-the-trade-desk-membership-duration-end

.. setting-the-trade-desk-membership-duration-minmax-start

The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the default duration. The maximum value is "180".

.. setting-the-trade-desk-membership-duration-minmax-end

.. setting-the-trade-desk-membership-duration-settozero-start

Set this value to "0" to remove all audience members.

.. setting-the-trade-desk-membership-duration-settozero-end

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

.. setting-the-trade-desk-3p-membership-duration-start

xxxxx. (in days)

.. setting-the-trade-desk-3p-membership-duration-end





**THE TRADE DESK: OFFLINE EVENTS**

This section contains settings that are unique to The Trade Desk: Offline Events.

**Tracking tag name**

.. setting-the-trade-desk-offline-tracking-tag-name-start

xxxxx

.. setting-the-trade-desk-offline-tracking-tag-name-end





**TIKTOK ADS MANAGER**

This section contains settings that are unique to TikTok Ads Manager.

**Advertiser ID**

.. setting-tiktok-ads-manager-advertiser-id-start

xxxxx

.. setting-tiktok-ads-manager-advertiser-id-end

**Custom audience name**

.. setting-tiktok-ads-manager-custom-audience-name-start

xxxxx

.. setting-tiktok-ads-manager-custom-audience-name-end

**User ID type**

.. setting-tiktok-ads-manager-user-id-type-start

xxxxx. IDFA, AAID, EMAIL, PHONE.

.. setting-tiktok-ads-manager-user-id-type-end




**TIKTOK ADS MANAGER: OFFLINE EVENTS**

This section contains settings that are unique to TikTok Ads Manager: Offline Events.

**Advertiser ID**

.. setting-tiktok-ads-manager-offline-advertiser-id-start

xxxxx

.. setting-tiktok-ads-manager-offline-advertiser-id-end





**VIBES**

See SFTP.





**ZENDESK**

This section contains settings that are unique to Zendesk.

**Subdomain**

.. setting-zendesk-subdomain-start

The subdomain is part of your |destination-name| URL. For example: "acme" is the subdomain for "acme.zendesk.com".

.. setting-zendesk-subdomain-end
