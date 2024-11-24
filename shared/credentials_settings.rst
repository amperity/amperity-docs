.. 
.. shared settings for destinations
.. 



**LOREM IPSUM**

.. TODO: Placeholder content for testing and validation.

.. credential-lorem-ipsum-long-start

Lorem ipsum dolor sit amet, duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. credential-lorem-ipsum-long-end

.. credential-lorem-ipsum-short-start

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. credential-lorem-ipsum-short-end

.. credential-lorem-ipsum-alt-start

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

.. credential-lorem-ipsum-alt-end



**STEPS**

This section contains the steps that all credentials follow. Custom information belongs in specific destination topics.

**Step 01**

.. credential-steps-add-credential-start

From the **Settings** page, select the **Credentials** tab, and then click the **Add credential** button.

.. credential-steps-add-credential-end

**Step 02**

.. credential-steps-select-type-start

In the **Credentials settings** dialog box, do the following:

From the **Plugin** dropdown, select |destination-name|.

Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

The |credential-type| credential type should already be selected in the **Credential type** drop-down.

.. credential-steps-select-type-end

Notes: When a source or destination supports more than one credential type, use the "multiple" inclusion block, and then add "From the **Credential type** drop-down, select **credential-name**." See the Amazon S3 destination topic for an example.

.. credential-steps-select-type-multiple-start

In the **Credentials settings** dialog box, do the following:

From the **Plugin** dropdown, select |destination-name|.

Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

.. credential-steps-select-type-multiple-end

**Step 03**

Notes: When a source or destination supports more than one credential type, copy the contents of this section instead of using the inclusion, and then replace credential-type with the credential string. See the Amazon S3 destination topic for an example.

.. credential-steps-settings-intro-start

The settings that are available for a credential are determined by the credential type. For the |credential-type| credential type, configure the following settings, and then click **Save**.

.. credential-steps-settings-intro-end




**COMMON**

This section contains credential settings that are not unique.

**Get details**

.. credential-get-details-both-types-start

Choose |credential-type| as the credential type, and then configure a combination of hostname, username and passphrase, host public key, port number, and private key settings as required by the credential type.

.. credential-get-details-both-types-end

.. credential-get-details-passphrase-start

Credentials for |destination-name| require a "username" and "passphrase". Set the hostname to |sftp-hostname|.

.. credential-get-details-passphrase-end

.. credential-get-details-private-key-start

Credentials for |destination-name| require a "username" and "private key". Set the hostname to |sftp-hostname|.

.. credential-get-details-private-key-end


**Configure credentials first**

.. credential-configure-first-start

Configure credentials for |destination-name| before adding a destination.

.. credential-configure-first-end

**Name and description**

.. credential-common-name-and-description-start

The name and description for a credential.

.. credential-common-name-and-description-end
**SnapPass callout**

.. credential-snappass-start

An individual with access to |destination-name| should use SnapPass to securely share |required-credentials| details with the individual who will configure Amperity.

.. credential-snappass-end





**ACTIVECAMPAIGN**

This section contains credentials that are unique to ActiveCampaign.

**API key**

.. credential-active-campaign-api-key-start

The `API key <https://developers.activecampaign.com/reference/authentication>`__ |ext_link| for your |destination-name| account.

.. credential-active-campaign-api-key-end

**API URL**

.. credential-active-campaign-url-start

The `base URL <https://developers.activecampaign.com/reference/url>`__ |ext_link| for your |destination-name| account. For example: `https://<your-account>.api-us1.com/api/3/`.

.. credential-active-campaign-url-end




**ACXIOM**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.




**ADOBE CAMPAIGN**

**Hostname**

.. credential-adobe-campaign-hostname-start

"[value]" is the name of your tenant on |destination-name|; ".campaign.adobe.com" is appended automatically.

.. credential-adobe-campaign-hostname-end

**Private key**

See SFTP.

**Username**

See SFTP.




**ADOBE COMMERCE**

Source only.

**Access token**

TBD

**Access token secret**

TBD

**Consumer key**

TBD

**Consumer secret**

TBD

**Hostname**

TBD





**ADOBE CUSTOMER ATTRIBUTES**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**ADOBE EXPERIENCE CLOUD**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**ADOBE MARKETO**

The following settings are unique to Adobe Marketo.

**Access token**

Not a setting in Amperity, but the access token contains the client ID and secret.

.. credential-adobe-marketo-access-token-start

The `client ID and secret <https://developers.marketo.com/rest-api/authentication/#creating_an_access_token>`__ |ext_link| are provided by custom services within |destination-name|.

.. credential-adobe-marketo-access-token-end

**API limits**

.. credential-adobe-marketo-api-limits-start

You may experience rate limits when sending very large audience lists to the Adobe Marketo API.

* Subscriptions are allocated 50,000 API calls per day. This resets daily at 12:00 AM, Central Standard Time.

* API access is rate limited to 100 calls per 20 seconds, with up to 10 concurrent API calls.

.. credential-adobe-market-api-limits-end

**Client ID**

.. credential-adobe-marketo-client-id-start

A client ID is a unique identifier. A client secret is a unique string. Together they are used to generate an access token that authorizes access to the Adobe Marketo REST API.

.. credential-adobe-marketo-client-id-end

**Client secret**

See client ID.

**Subdomain**

.. credential-adobe-marketo-subdomain-start

The `subdomain <https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/web-personalization/getting-started/add-subdomains-in-account-settings>`__ |ext_link| in |destination-name| in which Amperity will manage audiences.

.. credential-adobe-marketo-subdomain-end




**AIRSHIP**

**Hostname**

See SFTP.

**Port**

.. credential-airship-port-start

|destination-name| requires port "5222".

.. credential-airship-port-end

**Private key**

See SFTP.

**Username**

See SFTP.





**AMAZON ADS**

**OAuth flow**

See "OAuth common flows".



**AMAZON KINESIS DATA FIREHOSE**

xxxxx


**IAM access key**

.. credential-amazon-kinesis-iam-access-key-start

xxxxx

.. credential-amazon-kinesis-iam-access-key-end

**IAM role ARN**

.. credential-amazon-kinesis-iam-role-arn-start

xxxxx

.. credential-amazon-kinesis-iam-role-arn-end

**IAM secret key**

.. credential-amazon-kinesis-iam-secret-key-start

xxxxx

.. credential-amazon-kinesis-iam-secret-key-end

**S3 bucket name**

.. credential-amazon-kinesis-s3-bucket-name-start

xxxxx

.. credential-amazon-kinesis-s3-bucket-name-end




**AMAZON S3**

This section contains credentials that are unique to Amazon S3.

For iam-credential:

**Amperity role ARN**

.. credential-amazon-s3-amperity-role-arn-start

The intermediate IAM role ARN (Amazon Resource Name) that is used to assume the target role. Amperity provides this value.

.. credential-amazon-s3-amperity-role-arn-end

**External ID**

.. credential-amazon-s3-external-id-start

The external ID that is used to assume the target IAM role.

An external ID is an alphanumeric string between 2-1224 characters (without spaces) and may include the following symbols: plus (+), equal (=), comma (,), period (.), at (@), colon (:), forward slash (/), and hyphen (-).

.. credential-amazon-s3-external-id-end

**IAM access key**

.. credential-amazon-s3-iam-access-key-start

The IAM access key is one part (of two) that allows Amperity to autheticate to an Amazon S3 bucket. The value for this part of the access key is the access key ID. For example: "AKIAIOSFODNN7EXAMPLE".

.. credential-amazon-s3-iam-access-key-end

**IAM role ARN**

.. credential-amazon-s3-iam-role-arn-start

The IAM role ARN (Amazon Resource Name) that is used by Amperity to access a customer-managed Amazon S3 bucket.

.. credential-amazon-s3-iam-role-arn-end

**IAM secret key**

.. credential-amazon-s3-iam-secret-key-start

The IAM secret key is one part (of two) that allows Amperity to autheticate to an Amazon S3 bucket. The value for this part of the access key is the secret access key. For example: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY".

.. credential-amazon-s3-iam-secret-key-end

**S3 bucket name**

.. credential-amazon-s3-bucket-name-start

Required. The name of the Amazon S3 bucket.

.. credential-amazon-s3-bucket-name-end

**Target role ARN**

.. credential-amazon-s3-target-role-arn-start

The IAM role ARN (Amazon Resource Name) that is used by Amperity to access a customer-managed Amazon S3 bucket.

.. credential-amazon-s3-target-role-arn-end

**Trust policy**

.. credential-amazon-s3-trust-policy-start

The complete trust policy is availabe from a link at the bottom of the credential configuration page.

.. credential-amazon-s3-trust-policy-end

**SETUP STEPS FOR ROLE-TO-ROLE**

**Intro**

.. credential-amazon-s3-cross-account-roles-overview-start

Amperity prefers to pull data from and send data to customer-managed cloud storage.

Amperity recommends using cross-account role assumption to manage access to Amazon S3. This ensures that your brand manages the security policies that control access to your data.

.. credential-amazon-s3-cross-account-roles-overview-end

**Benefits**

.. credential-amazon-s3-cross-account-roles-context-start

Using cross-account role assumption helps ensures that customers can:

* Directly manage the IAM policies that control access to data
* Directly manage the files that are available within the Amazon S3 bucket
* Modify access without requiring involvement by Amperity; access may be revoked at any time by either Amazon AWS account, after which data sharing ends immediately
* Directly troubleshoot incomplete or missing files

.. credential-amazon-s3-cross-account-roles-context-end

**Note to make files available for feed creation**

.. credential-amazon-s3-cross-account-roles-setup-start

After setting up cross-account role assumption, a list of files (by filename and file type), along with any sample files, must be made available to allow for feed creation. These files may be placed directly into the shared location after cross-account role assumption is configured.

.. credential-amazon-s3-cross-account-roles-setup-end

**About AWS access point**

.. credential-amazon-s3-aws-access-point-start

.. admonition:: Can I use an Amazon AWS Access Point?

   Yes, but with the following limitations:

   #. The direction of access is Amperity access files that are located in a customer-managed Amazon S3 bucket
   #. A credential-free role-to-role access pattern is used
   #. Traffic is not restricted to VPC-only

.. credential-amazon-s3-aws-access-point-end

**Intro to steps**

.. credential-amazon-s3-cross-account-roles-steps-intro-done-by-admins-start

The following steps describe how to configure Amperity to use cross-account role assumption to pull data from (or push data to) a customer-managed Amazon S3 bucket.

.. important:: These steps require configuration changes to customer-managed Amazon AWS accounts and must be done by users with administrative access.

.. credential-amazon-s3-cross-account-roles-steps-intro-done-by-admins-end

**Settings context**

.. credential-amazon-s3-cross-account-roles-steps-settings-required-start

You must provide the values for the **Target Role ARN** and **S3 Bucket Name** fields. Enter the target role ARN (Amazon Resource Name) for the IAM role that Amperity will use to access the customer-managed Amazon S3 bucket, and then enter the name of the Amazon S3 bucket.

.. credential-amazon-s3-cross-account-roles-steps-settings-required-end

.. credential-amazon-s3-cross-account-roles-steps-settings-provided-start

The values for the **Amperity Role ARN** and **External ID** fields -- the Amazon Resource Name (ARN) for your Amperity tenant and its external ID -- are provided automatically.

.. credential-amazon-s3-cross-account-roles-steps-settings-provided-end

**Review policy**

.. credential-amazon-s3-cross-account-roles-steps-policy-example-intro-start

Review the following sample policy, and then add a similar policy to the customer-managed Amazon S3 bucket that allows Amperity access to the bucket. Add this policy as a trusted policy to the IAM role that is used to manage access to the customer-managed Amazon S3 bucket.

.. credential-amazon-s3-cross-account-roles-steps-policy-example-intro-end

**Example policy**

.. credential-amazon-s3-cross-account-roles-steps-policy-example-start

The policy for the customer-managed Amazon S3 bucket is unique, but will be similar to:

::

   {
     "Statement": [
       {
         "Sid": "AllowAmperityAccess",
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::account:role/resource"
          },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
              "sts:ExternalId": "01234567890123456789"
           }
         }
       }
     ]
   }

The value for the role ARN is similar to:

::

   arn:aws:iam::1234567890:role/prod/amperity-plugin

.. credential-amazon-s3-cross-account-roles-steps-policy-example-end

**Save Amazon S3 credentials**

.. credential-amazon-s3-cross-account-roles-steps-save-credentials-start

Click **Continue** to test the configuration (and validate the connection) to the customer-managed Amazon S3 bucket, after which you will be able to continue the steps for adding a courier.

.. credential-amazon-s3-cross-account-roles-steps-save-credentials-end





**ATTENTIVE** (API + SFTP)

This section contains credentials that are unique to Attentive SFTP + API connectors.

**API key**

.. credential-attentive-api-key-start

The API key for your |destination-name| account.

.. credential-attentive-api-key-end

**Hostname** (SFTP)

See SFTP.

**Passphrase** (SFTP)

See SFTP.

**Username** (SFTP)

See SFTP.





**AZURE BLOB STORAGE**

This section contains credentials that are unique to Azure Blob Storage.

**Account name**

.. credential-azure-blob-storage-account-name-start

The name of your |destination-name| storage account.

.. credential-azure-blob-storage-account-name-end

**Connection string**

.. credential-azure-blob-storage-connection-string-start

A connection string allows access to a location within your |destination-name| storage account. A connection string is a combination of your storage account and your account access key.

.. credential-azure-blob-storage-connection-string-end

.. credential-azure-blob-storage-connection-string-overview-start

A `connection string <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account>`__ |ext_link| includes the information that allows Amperity to authorize to your |destination-name| account.

.. credential-azure-blob-storage-connection-string-overview-end

.. credential-azure-blob-storage-connection-string-example-start

A connection string is similar to:

::

   DefaultEndpointsProtocol=https;
   AccountName=name;AccountKey=key

.. credential-azure-blob-storage-connection-string-example-end

**Container**

.. credential-azure-blob-storage-container-start

A container organizes a set of blobs, similar to a directory in a file system. Your |destination-name| account can include an unlimited number of containers. Each container can store an unlimited number of blobs.

A container name must be a valid DNS name, as it forms part of the unique uniform resource identifier (URI) used to address the container or its blobs.

The value of the blob within the URI must be configured as the value for the **Container** setting within Amperity.

.. credential-azure-blob-storage-container-end

**Shared access signature**

.. credential-azure-blob-storage-shared-access-signature-start

A shared access signature (SAS) grants limited access to containers and blobs in your storage account. The value of a SAS is the URI for the resource to which the SAS delegates access, followed by the SAS token.

.. credential-azure-blob-storage-shared-access-signature-end

.. credential-azure-blob-storage-shared-access-signature-overview-start

A `service-level shared access signature (SAS) <https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas>`__ |ext_link| specifies which resources in your |destination-name| account can be accessed, what permissions that access allows on resources in the container, and the length of time for which the SAS is valid.

.. credential-azure-blob-storage-shared-access-signature-overview-end

.. credential-azure-blob-storage-shared-access-signature-permissions-start

When Microsoft Azure is configured to use a shared access signature (SAS) to grant restricted access rights to Microsoft Azure storage resources, be sure to use the correct SAS token string for credentials within Amperity and that the SAS is assigned the following permissions within Microsoft Azure: READ, ADD, CREATE, WRITE, DELETE, and LIST.

.. credential-azure-blob-storage-shared-access-signature-permissions-end

**Storage URI**

.. credential-azure-blob-storage-storage-uri-start

A URI for |destination-name| that contains the name of the account and the name of the container in which blob storage is located. For example:

::

   https://myaccount.blob.core.windows.net/mycontainer

.. credential-azure-blob-storage-storage-uri-end

.. credential-azure-blob-storage-storage-uri-overview-start

Each |destination-name| resource has a `storage URI <https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#resource-uri-syntax>`__ |ext_link|, which contains the name of the account and the name of the container in which blob storage is located.

.. credential-azure-blob-storage-storage-uri-overview-end



**BAZAARVOICE**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**BLUECORE**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**BRAZE**

**API key**

.. credential-braze-api-key-start

Required. The API key for your |destination-name| account.

.. credential-braze-api-key-end





**CAMELOT SMM**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**CORDIAL**

.. TODO: Are the Cordial IAM + S3 bucket settings identical to Amazon S3 destination settings?

For cordial and cordial-aws both use API key and API URL.

**API key**

.. credential-cordial-api-key-start

Required. The API key for your |destination-name| account.

.. credential-cordial-api-key-end

**API URL**

.. credential-cordial-api-url-start

Required. The API URL for your |destination-name| account. May be one of the following: ``https://api.cordial.io/`` or ``https://api.usw2.cordial.io/``.

.. credential-cordial-api-url-end

**IAM access key**

.. credential-cordial-iam-access-key-start

Required. The IAM access key is one part (of two) that allows Amperity to autheticate to an Amazon S3 bucket. The value for this part of the access key is the access key ID. For example: "AKIAIOSFODNN7EXAMPLE".

.. credential-cordial-iam-access-key-end

**IAM secret key**

.. credential-cordial-iam-secret-key-start

Requried. The IAM secret key is one part (of two) that allows Amperity to autheticate to an Amazon S3 bucket. The value for this part of the access key is the secret access key. For example: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY".

.. credential-cordial-iam-secret-key-end

**S3 bucket name**

.. credential-cordial-s3-bucket-name-start

Required. The name of the Amazon S3 bucket.

.. credential-cordial-s3-bucket-name-end






**CRITEO**

See OAuth common.





**CROSS COUNTRY COMPUTER**

**Hostnamem**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**DATABRICKS**

xxxxx

For azure-databricks


**Server hostname**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end

**HTTP path**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end

**Personal access token**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end

**Azure Blob account name**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end

**Azure Blob shared access signature**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end

**Container**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end

For databricks

**HTTP path**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end

**Personal access token**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end

**Server hostname**

.. credential-xxxxx-xxxxx-start

xxxxx

.. credential-xxxxx-xxxxx-end





**EPSILON ABACUS**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**EPSILON CONVERSANT**

**Hostname**

.. credential-epsilon-conversant-hostname-start

"[value]" is the name of your tenant on |destination-name|.

.. credential-epsilon-conversant-hostname-end

**Passphrase**

See SFTP.

**Username**

See SFTP.






**EPSILON TARGETING**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.






**EXPERIAN**

xxxxx

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Private key**

See SFTP.

**Username**

See SFTP.




**GOOGLE ADS**

See OAuth common.





**GOOGLE ANALYTICS** / **GOOGLE ANALYTICS 4**

**OAuth flow**

See "OAuth common flows".





**GOOGLE CLOUD STORAGE**

This section contains credentials that are unique to Google Cloud Storage.

**Bucket name**

.. credential-google-cloud-storage-bucket-name-start

`Buckets <https://cloud.google.com/storage/docs/buckets>`__ |ext_link| are basic containers that hold data in |destination-name|. Use buckets to organize storage locations for your data, and then configure Amperity to send data to that bucket.

.. credential-google-cloud-storage-bucket-name-end

.. credential-google-cloud-storage-bucket-name-must-match-start

The bucket name must match the value of the ``<<GCS_BUCKET_NAME>>`` placeholder shown in the :ref:`service account key example <destination-google-cloud-storage-service-account-key-example>`.

.. credential-google-cloud-storage-bucket-name-must-match-end

**Service account key**

.. credential-google-cloud-storage-service-account-key-start

Google Cloud uses service account key-pairs for authentication. A public service account key is stored in Google Cloud; a private service account key allows applications access to your instance of |destination-name|.

.. credential-google-cloud-storage-service-account-key-end

.. credential-google-cloud-storage-service-account-key-value-start

The value of the private service account key is the contents of the JSON file downloaded from Google Cloud after `creating the service account key-pair <https://cloud.google.com/iam/docs/keys-create-delete>`__ |ext_link|. Open the JSON file in a text editor, select all of the content in the JSON file, copy it, and then paste it into the **Service account key** field.

.. credential-google-cloud-storage-service-account-key-value-end

**Service account role**

.. TODO: Is the service account role required for sending data *and* pulling data from Google Cloud Storage? Or just pulling data?

.. credential-google-cloud-storage-service-account-role-start

The **Storage Object Admin** role must be assigned to the service account.

.. credential-google-cloud-storage-service-account-role-end



**GOOGLE CUSTOMER MATCH**

See OAuth common.





**HUBSPOT**

See OAuth common.





**INFUTOR**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**KIBO**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**KLAVIYO**

**API key**

.. credential-klaviyo-api-key-start

Required. The API key for your |destination-name| account.

.. credential-klaviyo-api-key-end





**KOUPON MEDIA**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**LISTRAK**

**Allowlist callout**

.. credential-listrak-allowlist-start

The Amperity `IP address for allowlists <https://docs.amperity.com/datagrid/send_data.html#ip-allowlists>`__ |ext_link| must be added to the allowlist for the |destination-name| integration.

.. credential-listrak-allowlist-end

**Email client ID and client secret**

.. credential-listrak-email-client-id-secret-start

A client ID and secret for an email integration that is already set up in |destination-name|.

.. credential-listrak-email-client-id-secret-end

**SMS client ID and client secret**

.. credential-listrak-sms-client-secret-start

A client ID and secret for an SMS integration that is already set up in |destination-name|.

.. credential-listrak-sms-client-secret-end





**LIVERAMP**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**MAILCHIMP**

**API key**

.. credential-mailchimp-api-key-start

Required. The API key for your |destination-name| account.

.. credential-mailchimp-api-key-end





**META ADS MANAGER** (Facebook)

**OAuth flow**

See "OAuth common flows".





**META ADS MANAGER: OFFLINE EVENTS**

**OAuth flow**

See "OAuth common flows".





**MICROSOFT ADVERTISING**

**OAuth flow**

See "OAuth common flows".





**MICROSOFT DATAVERSE**

.. credential-microsoft-dataverse-requirements-start

Microsoft Azure must be configured for your Power Apps application, after which your Power Apps application must be added to the Microsoft Power Platform.

.. credential-microsoft-dataverse-requirements-end

**Azure tenant ID**

.. credential-microsoft-dataverse-azure-tenant-id-start

The Microsoft Azure tenant ID for your instance of |destination-name|.

.. credential-microsoft-dataverse-azure-tenant-id-end

**Azure client ID and client secret**

.. credential-microsoft-dataverse-azure-client-id-and-secret-start

A client ID and client secret for Microsoft Azure that has permission to access your instance of |destination-name|.

.. credential-microsoft-dataverse-azure-client-id-and-secret-end





**MICROSOFT DYNAMICS 365 MARKETING**

**Azure client ID and client secret**

.. credential-microsoft-dynamics-365-marketing-azure-client-id-and-secret-start

A client ID and client secret for Microsoft Azure that has permission to access your instance of |destination-name|.

.. credential-microsoft-dynamics-365-marketing-azure-client-id-and-secret-end

**Azure tenant ID**

.. credential-microsoft-dynamics-365-marketing-azure-tenant-id-start

The Microsoft Azure tenant ID for your instance of |destination-name|.

.. credential-microsoft-dynamics-365-marketing-azure-tenant-id-end






**MICROSOFT DYNAMICS**

**Client ID and client secret**

.. credential-microsoft-dynamics-client-id-and-secret-start

A client ID and client secret that has permission to access your instance of |destination-name|.

.. credential-microsoft-dynamics-client-id-and-secret-end





**MONETATE**

See Kibo.





**NEUSTAR**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

.. credential-neustar-passphrase-start

|destination-name| requires the SFTP passphrase to be rotated every 180 days. When rotated, it must also be updated in Amperity.

.. credential-neustar-passphrase-end

**Username**

See SFTP.





**OAuth common flows**

Applies to Amazon Ads, Criteo, Google Ads, Google Customer Match, HubSpot, Meta Ads Manager, Microsoft Advertising, Pinterest, Snapchat, TikTok Ads Manager

**OAuth flow**

.. credential-oauth-overview-start

TBD. See existing templates for OAuth.

.. credential-oauth-overview-end

**Refresh token**

.. credential-oauth-refresh-token-start

A refresh token is generated by the OAuth process that authorizes Amperity to send data to |destination-name|.

The value for the refresh token is updated automatically when a credential with permission to access |destination-name| is selected.

.. credential-oauth-refresh-token-end

**Reauthorize token**

.. credential-oauth-reauthorize-start

You may need to reauthorize access to |destination-name|. This is necessary when an authorization token has expired or when it has been removed by someone with permission to manage access within |destination-name|. To reauthorize access to |destination-name|, follow the steps to configure OAuth and create a new credential.

.. credential-oauth-reauthorize-end





**ORACLE DATA CLOUD**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.







**ORACLE ELOQUA**

**Company name**

.. credential-oracle-eloqua-company-name-start

The name of your company, as used within your |destination-name| account.

.. credential-oracle-eloqua-company-name-end

**Password**

.. credential-oracle-eloqua-password-start

The password associated with the |destination-name| username.

.. credential-oracle-eloqua-password-end

**Username**

See SFTP.





**ORACLE RESPONSYS**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Private key**

See SFTP.

**Username**

See SFTP.






**PANDA PRINTING**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.






**PEBBLEPOST**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**PERSADO**

**Hostname**

See SFTP.

**Private key**

See SFTP.

**Username**

See SFTP.





**PINTEREST**

See OAuth common.





**POWERREVIEWS**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**QUAD**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.






**RR DONNELLY**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.






**SAILTHRU**

**API key**

.. credential-sailthru-api-key-start

The API key for your |destination-name| account.

.. credential-sailthru-api-key-end

**Secret**

.. credential-sailthru-secret-start

The API secret for your |destination-name| account.

.. credential-sailthru-secret-end

.. credential-sailthru-api-find-key-and-secret-start

You can find the API key and secret after you log in to |destination-name| and authenticate to the Sailthru API. The API key and API secret are available on the "Setup – API & Postbacks" page.

.. credential-sailthru-api-find-key-and-secret-end






**SALESFORCE COMMERCE CLOUD**

xxxxx

**API token**

.. credential-salesforce-commerce-cloud-api-token-start

xxxxx

.. credential-salesforce-commerce-cloud-api-token-end





**SALESFORCE MARKETING CLOUD**

**API client ID and client secret**

.. credential-salesforce-marketing-cloud-api-client-secret-start

The client ID and client secret for your brand's instance of the Marketing Cloud SOAP API.

.. credential-salesforce-marketing-cloud-api-client-secret-end

**API subdomain**

.. credential-salesforce-marketing-cloud-api-subdomain-start

The authentication subdomain for your brand's instance of the Marketing Cloud SOAP API.

.. credential-salesforce-marketing-cloud-api-subdomain-end


.. credential-salesforce-marketing-cloud-api-subdomain-base-uri-start

The authentication subdomain for the `SOAP base URI <https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/your-subdomain-tenant-specific-endpoints.html>`__ |ext_link| is represented by a 28-character string that starts with the letters "mc", such as "mcabc123...".

.. credential-salesforce-marketing-cloud-api-subdomain-base-uri-end

**SFTP hostname**

.. credential-salesforce-marketing-cloud-hostname-start

"[hostname]" is the name of your tenant on |destination-name|.

.. credential-salesforce-marketing-cloud-hostname-end

.. credential-salesforce-marketing-cloud-hostname-context-start

The SFTP hostname is represented by a 28-character string that starts with the letters “mc”, such as "mcabc123...". This is the same 28-character string that represents the subdomain, which is part of the SOAP base URI for Salesforce Marketing Cloud.

.. credential-salesforce-marketing-cloud-hostname-context-end

**SFTP passphrase**

See SFTP.

**SFTP username**

See SFTP.





**SALESFORCE SALES CLOUD**

**Security token**

.. credential-salesforce-sales-cloud-security-token-start

The Salesforce security token associated with the username. This setting is not required when IP range policies are configured from the Salesforce admin console.

.. credential-salesforce-sales-cloud-security-token-end

**Username and password**

.. credential-salesforce-sales-cloud-username-and-password-start

The username and password of a Salesforce account configured for API access.

.. credential-salesforce-sales-cloud-username-and-password-end





**SFTP**

This section contains credentials that are unique to SFTP. These credentials apply to all sources and destinations that use SFTP, including Acxiom, Adobe Campaign, Adobe Customer Attributes, Adobe Experience Platform, Airship, Attentive, BazaarVoice, Bluecore, Camelot SMM, Cheetah Digital, Criteo (offline events), Cross Country Computer, Emarsys, Epsilon, Evocalize, Experian, Infutor, Iterable, Kibo, Koupon Media, LiveRamp, Neustar, Oracle Data Cloud, Oracle DMP, Oracle Responsys, PebblePost, Persado, Pinterest (product catalogs), PowerReviews, Quad, Reddit Ads, RR Donnelly, Salesforce Commerce Cloud, Salesforce Marketing Cloud, Salesforce Marketing Cloud Personalization, SMG, SoundCommerce, Vibes.

.. credential-sftp-about-start

Secure File Transfer Protocol (SFTP) is a network connection that is configured using a combination of a hostname and a username, along with a passphrase, public key, or private key.

.. credential-sftp-about-end

**Host public key**

.. credential-sftp-host-public-key-start

The host public key for |where-send|.

.. credential-sftp-host-public-key-end

**Hostname**

.. credential-sftp-hostname-start

Required. The hostname for |where-send|. For example: |sftp-hostname|.

.. credential-sftp-hostname-end

**Passphrase**

.. credential-sftp-passphrase-start

The passphrase that is associated with the username.

.. credential-sftp-passphrase-end

**Port**

.. credential-sftp-port-start

The port number required by |where-send|. Use this setting only when the SFTP site uses a non-default port value.

.. credential-sftp-port-end

**Private key**

.. credential-sftp-private-key-start

A private key that is used to encrypt files that are sent to |where-send|.

.. credential-sftp-private-key-end

.. credential-sftp-private-key-required-start

This setting is only required when the "private-key" credential type is selected.

.. credential-sftp-private-key-required-end

**Username**

.. credential-sftp-username-start

Required. A username with access to |where-send|. This username must be allowed to write data to the remote folder to which Amperity will send data.

.. credential-sftp-username-end




**SHOPIFY**

xxxxx

**Access token**

.. credential-shopify-access-token-start

xxxxx

.. credential-shopify-access-token-end

**Shop name**

.. credential-shopify-shop-name-start

xxxxx

.. credential-shopify-shop-name-end




**SMG**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





**SNAPCHAT**

See OAuth.





**SNOWFLAKE**

These settings apply to destination *and* bridge.

**Account name**

.. credential-snowflake-account-name-start

The unique name of an account that exists within your brand's |destination-name| organization.

.. credential-snowflake-account-name-end

.. credential-snowflake-account-name-required-permissions-start

.. important:: This role must be granted :ref:`write permission to Snowflake objects <source-snowflake-azure-configure-objects>`, :ref:`permission to access each table <source-snowflake-azure-configure-tables>`, and permission to :ref:`write table output to Azure Blob Storage <source-snowflake-azure-configure-storage-integration>`.

.. credential-snowflake-account-name-required-permissions-end

**Organization**

.. credential-snowflake-organization-start

An `organization <https://docs.snowflake.com/en/user-guide/organizations>`__ is a first-class object in |destination-name| that links accounts and allows the use of secure data sharing.

.. credential-snowflake-organization-end

**Password**

.. credential-snowflake-password-start

The password for the username.

.. credential-snowflake-password-end

**Region**

.. credential-snowflake-region-start

The `region <https://docs.snowflake.com/en/user-guide/intro-regions>`__ |ext_link| in which your |destination-name| account is hosted. Use the `CURRENT_REGION <https://docs.snowflake.com/en/sql-reference/functions/current_region>`__ |ext_link| argument in |destination-name| to return the value for your region.

.. credential-snowflake-region-end

**Username**

.. credential-snowflake-username-start

A username with permission to access |destination-name|.

.. credential-snowflake-username-end

**SNOWFLAKE** (AWS-specific)

**IAM access key**

.. credential-snowflake-iam-access-key-start

Required. The IAM access key (along with the secret key) that that allows Amperity to autheticate to Snowflake.

.. credential-snowflake-iam-access-key-end

**IAM role ARN**

.. credential-snowflake-iam-role-arn-start

The IAM role ARN (Amazon Resource Name) that is used by Amperity to access Snowflake.

.. credential-snowflake-iam-role-arn-end

**IAM secret key**

.. credential-snowflake-iam-secret-key-start

Requried. The IAM secret key (along with the access key) that allows Amperity to autheticate to Snowflake.

.. credential-snowflake-iam-secret-key-end

**SNOWFLAKE** (Azure-specific)

**Account name**

.. credential-snowflake-account-name-start

The account name for Microsoft Azure Blob Storage.

.. credential-snowflake-account-name-end

**Shared access signature**

.. credential-snowflake-shared-access-signature-start

The shared access signature that allows access to a Microsoft Azure Blob Storage container.

.. credential-snowflake-shared-access-signature-end













**SOUNDCOMMERCE**

**Hostname**

See SFTP.

**Private key**

See SFTP.

**Username**

See SFTP.





**THE TRADE DESK**

**Advertiser ID**

.. credential-the-trade-desk-advertiser-id-start

The advertiser ID for your account with The Trade Desk.

.. credential-the-trade-desk-advertiser-id-end

**Advertiser secret**

.. credential-the-trade-desk-advertiser-secret-start

The advertiser secret for your account with The Trade Desk.

.. credential-the-trade-desk-advertiser-secret-end

**Where is the ID and secret?**

.. credential-the-trade-desk-find-id-and-secret-start

You can find the advertiser ID and secret key from the management console within The Trade Desk. Open "Preferences", and then "First Party Data Credentials". The advertiser ID and secret key are shown there.

.. credential-the-trade-desk-find-id-and-secret-end





**THE TRADE DESK: 3P MARKETPLACE**

**Advertiser secret**

See The Trade Desk.

**Advertiser ID**

See The Trade Desk.

**Platform API token**

.. credential-the-trade-desk-platform-api-token-start

A long-lived token that allows access to The Trade Desk Platform API.

.. credential-the-trade-desk-platform-api-token-end

**Provider ID**

.. credential-the-trade-desk-provider-id-start

The provider ID for your account with The Trade Desk. Ask your The Trade Desk representative for details.

.. credential-the-trade-desk-provider-id-end





**THE TRADE DESK: OFFLINE EVENTS**

**Advertiser ID**

See The Trade Desk.

**Advertiser secret**

See The Trade Desk.





**TIKTOK ADS MANAGER**

See OAuth.

**Required permissions**

.. credential-tiktok-ads-manager-oauth-requirements-start

TikTok Advertiser Accounts must use OAuth. The account that is used to authorize to |destination-name| is assigned "TikTok Ad Account Operator" or "TikTok Ad Account Admin" permission. OAuth will not work if your account is assigned "TikTok Ad Account Analyst" permission.

.. credential-tiktok-ads-manager-oauth-requirements-end




**TIKTOK ADS MANAGER: OFFLINE EVENTS**

See OAuth.

See TikTok Ads Manager.




**UID2**

**UID2 key**

.. credential-uid2-key-start

xxxxx

.. credential-uid2-key-end

**UID2 secret**

.. credential-uid2-secret-start

xxxxx

.. credential-uid2-secret-end





**VIBES**

**Hostname**

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.




**YAHOO DSP**

**Site MDM ID**

.. credential-yahoo-dsp-mdm-id-start

Required. The "Site MDM ID" is the value of your brand's Master Data Management (MDM) ID in |destination-name|. This is a unique advertiser ID that assigns your brand a specific location within the |destination-name| taxonomy.

.. credential-yahoo-dsp-mdm-id-end





**ZENDESK**

**API token**

.. credential-zendesk-api-token-start

Required. Your brand's Zedesk API token.

.. credential-zendesk-api-token-end


**Email address**

.. credential-zendesk-email-address-start

Required. The email address for the Zendesk API user.

.. credential-zendesk-email-address-end
