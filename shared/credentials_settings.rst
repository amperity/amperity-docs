.. 
.. shared settings for destinations
.. 


.. vale off

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

.. vale on


.. vale off

**STEPS**

All the steps that all credentials follow. Custom information belongs in specific destination topics.

.. vale on

**Step 01**

.. credential-steps-add-credential-start

From the **Settings** page, select the **Credentials** tab, and then click the **Add credential** button.

.. credential-steps-add-credential-end

**Step 02**

.. credential-steps-select-type-start

In the **Create credentials** dialog box, do the following:

From the **Plugin** dropdown, select |plugin-name|.

Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

.. credential-steps-select-type-end

.. vale off

Notes: When a source or destination supports more than one credential type, use the "multiple" inclusion block, and then add "From the **Credential type** dropdown, select **credential-name**." See the Amazon S3 destination topic for an example.

.. vale on

.. credential-steps-select-type-multiple-start

In the **Create credentials** dialog box, do the following:

From the **Plugin** dropdown, select |plugin-name|.

Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

.. credential-steps-select-type-multiple-end

.. vale off

Notes: The "external" steps apply only to Amazon Ads, Criteo Audience API, Criteo Retail Audience API, DV360, Facebook, Google Ads, Google Analytics, Google Customer Match, Google Enhanced Conversions, Hubspot, LinkedIn DMP, Meta Ads Offline Events, Microsoft Ads, Pinterest, Reddit Ads, Snapchat, TikTok Ads, and TikTok Ads Offline Events

.. vale on

.. credential-steps-select-type-external-start

In the **Create credentials** dialog box, do the following:

From the **Plugin** dropdown, select |plugin-name|.

Click **Generate authorzation URL**, and then complete the external authorization steps shown for |destination-name|.

After the external authorization steps are completed, assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

.. credential-steps-select-type-external-end


**Step 03**

.. vale off

Notes: When a source or destination supports more than one credential type, copy the contents instead of using the inclusion, and then replace credential-type with the credential string. See the Amazon S3 destination topic for an example.

.. vale on

.. credential-steps-settings-intro-start

The settings that are available for a credential vary by credential type. For the |credential-type| credential type, configure settings, and then click **Save**.

.. credential-steps-settings-intro-end




.. vale off

**COMMON**

.. vale on

Credential settings that are not unique.

**Get details**

.. credential-get-details-both-types-start

Choose |credential-type| as the credential type. Configure a combination of host name, username and passphrase, host public key, port number, and private key settings as required by the credential type.

.. credential-get-details-both-types-end

.. credential-get-details-passphrase-start

Credentials for |destination-name| require a "username" and "passphrase". Set the host name to |sftp-hostname|.

.. credential-get-details-passphrase-end

.. credential-get-details-private-key-start

Credentials for |destination-name| require a "username" and "private key". Set the host name to |sftp-hostname|.

.. credential-get-details-private-key-end


**Configure credentials first**

.. credential-configure-first-start

Configure credentials for |destination-name| before adding a destination.

.. credential-configure-first-end

**Name and description**

.. credential-common-name-and-description-start

The name and description for a credential.

.. credential-common-name-and-description-end


**Port**

Applies to: most SFTP sources and destinations.

.. credential-common-port-start

The Transmission Control Protocol (TCP) port to use for Secure Shell (SSH) transfers. Default value: "22".

.. credential-common-port-end


.. vale off

**SnapPass callout**

.. vale on

.. credential-snappass-start

An individual with access to |destination-name| should use SnapPass to securely share |required-credentials| details with the individual who configures Amperity.

.. credential-snappass-end





.. vale off

**ACTIVECAMPAIGN**

Credentials that are unique to ActiveCampaign.

**API key**

.. credential-active-campaign-api-key-start

The `API key <https://developers.activecampaign.com/reference/authentication>`__ |ext_link| for your |destination-name| account.

.. credential-active-campaign-api-key-end

**API URL**

.. credential-active-campaign-url-start

The `base URL <https://developers.activecampaign.com/reference/url>`__ |ext_link| for your |destination-name| account. For example: ``https://<your-account>.api-us1.com/api/3/``.

.. credential-active-campaign-url-end




.. vale off

**ACXIOM**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.




.. vale off

**ADOBE CAMPAIGN**

**Hostname**

.. vale on

.. vale off

.. credential-adobe-campaign-hostname-start

"[value]" is the name of your tenant on |destination-name|. ".campaign.adobe.com" is appended automatically.

.. credential-adobe-campaign-hostname-end

.. vale on

**Private key**

See SFTP.

**Username**

See SFTP.




.. vale off

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

.. vale off

**Hostname**

.. vale on

TBD





.. vale off

**ADOBE CUSTOMER ATTRIBUTES**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.




.. vale off

**ADOBE EXPERIENCE CLOUD**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**ADOBE MARKETO**

.. vale on

The following settings are unique to Adobe Marketo.

**Access token**

Not a setting in Amperity, but the access token has the client ID and secret.

.. credential-adobe-marketo-access-token-start

Custom services within |destination-name| give the `client ID and secret <https://developers.marketo.com/rest-api/authentication/#creating_an_access_token>`__ |ext_link|.

.. credential-adobe-marketo-access-token-end

**Client ID**

.. credential-adobe-marketo-client-id-start

A client ID is a unique identifier. A client secret is a unique string. Together they generate an access token that authorizes access to the Adobe Marketo REST API.

.. credential-adobe-marketo-client-id-end

**Client secret**

See client ID.

**Subdomain**

.. credential-adobe-marketo-subdomain-start

The `subdomain <https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/web-personalization/getting-started/add-subdomains-in-account-settings>`__ |ext_link| in |destination-name| in which Amperity manages audiences.

.. credential-adobe-marketo-subdomain-end




.. vale off

**ADOBE TARGET**

.. vale on

The following settings are unique to Adobe Target.

**Authentication token**

.. credential-adobe-target-authentication-token-start

The authentication token is created from the |destination-name| `user interface <https://experienceleague.adobe.com/en/docs/target-dev/developer/implementation/methods/profile-api-settings>`__ |ext_link| *or* from the `Adobe Target Admin API <https://developer.adobe.com/target/administer/admin-api/#tag/Authentication/operation/requestAuthorizationToken>`__ |ext_link|.

.. credential-adobe-target-authentication-token-end

**Client code**

.. credential-adobe-target-client-code-start

The name of the |destination-name| client. The client code is located in the URL for your instance of |destination-name|. For example, "socktown" is the client code in the ``socktown.tt.omtrdc.net`` URL.

.. credential-adobe-target-client-code-end




.. vale off

**AIRSHIP**

**Hostname**

.. vale on

See SFTP.

**Port**

.. credential-airship-port-start

|destination-name| requires port "5222".

.. credential-airship-port-end

**Private key**

See SFTP.

**Username**

See SFTP.





.. vale off

**AMAZON ADS**

.. vale on

**OAuth flow**

See "OAuth common flows".





.. vale off

**AMAZON S3**

.. vale on

Credentials that are unique to Amazon S3.

For iam-credential:

**Amperity role ARN**

.. credential-amazon-s3-amperity-role-arn-start

The intermediate IAM role ARN that assumes the target role. Amperity gives this value.

.. credential-amazon-s3-amperity-role-arn-end

**External ID**

.. vale off

.. credential-amazon-s3-external-id-start

The external ID that is used to assume the target IAM role.

An external ID is an alphanumeric string with 2-1224 characters without spaces that may include the following symbols: plus (+), equal (=), comma (,), period (.), at (@), colon (:), forward slash (/), and hyphen (-).

.. credential-amazon-s3-external-id-end

.. vale on

**IAM access key**

.. credential-amazon-s3-iam-access-key-start

The IAM access key is one part of two that allows Amperity to authenticate to an Amazon S3 bucket. The value for this part of the access key is the access key ID. For example: "AKIAIOSFODNN7EXAMPLE".

.. credential-amazon-s3-iam-access-key-end

**IAM role ARN**

.. credential-amazon-s3-iam-role-arn-start

The IAM role ARN used by Amperity to access a customer-managed Amazon S3 bucket.

.. credential-amazon-s3-iam-role-arn-end

**IAM secret key**

.. vale off

.. credential-amazon-s3-iam-secret-key-start

The IAM secret key is one part of two that allows Amperity to authenticate to an Amazon S3 bucket. The value for this part of the access key is the secret access key. For example: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY".

.. credential-amazon-s3-iam-secret-key-end

.. vale on

**S3 bucket name**

.. credential-amazon-s3-bucket-name-start

Required. The name of the Amazon S3 bucket.

.. credential-amazon-s3-bucket-name-end

**Target role ARN**

.. credential-amazon-s3-target-role-arn-start

The IAM role ARN used by Amperity to access a customer-managed Amazon S3 bucket.

.. credential-amazon-s3-target-role-arn-end

**Trust policy**

.. credential-amazon-s3-trust-policy-start

The complete trust policy is available from a link at the bottom of the credential configuration page.

.. credential-amazon-s3-trust-policy-end

.. vale off

**SETUP STEPS FOR ROLE-TO-ROLE**

.. vale on

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
* Access without requiring involvement by Amperity
* Revoke access at any time in either Amazon AWS account, after which data sharing ends immediately
* Directly troubleshoot incomplete or missing files

.. credential-amazon-s3-cross-account-roles-context-end

**Note to make files available for feed creation**

.. credential-amazon-s3-cross-account-roles-setup-start

After setting up cross-account role assumption, make a list of files by filename and file type available to feed creation, along with any sample files. Add these files directly to the shared location after configuring cross-account role assumption.

.. credential-amazon-s3-cross-account-roles-setup-end

**About AWS access point**

.. credential-amazon-s3-aws-access-point-start

.. admonition:: Using an Amazon AWS Access Point?

   Yes, but with the following limitations:

   #. Amperity accesses files located in a customer-managed Amazon S3 bucket
   #. Use a credential-free role-to-role access pattern
   #. Do not restrict traffic to VPC-only

.. credential-amazon-s3-aws-access-point-end

**Intro to steps**

.. credential-amazon-s3-cross-account-roles-steps-intro-done-by-admins-start

The following steps describe how to configure Amperity to use cross-account role assumption to pull data from or push data to a customer-managed Amazon S3 bucket.

.. important:: These steps require users with administrative access to configure changes to customer-managed Amazon AWS accounts.

.. credential-amazon-s3-cross-account-roles-steps-intro-done-by-admins-end

**Settings context**

.. credential-amazon-s3-cross-account-roles-steps-settings-required-start

You must give the values for the **Target Role ARN** and **S3 Bucket Name** fields. Enter the target role ARN for the IAM role that Amperity uses to access the customer-managed Amazon S3 bucket, and then enter the name of the Amazon S3 bucket.

.. credential-amazon-s3-cross-account-roles-steps-settings-required-end

.. credential-amazon-s3-cross-account-roles-steps-settings-provided-start

The values for the **Amperity Role ARN** and **External ID** fields--the Amazon Resource Name (ARN) for your Amperity tenant and its external ID--are automatically provided.

.. credential-amazon-s3-cross-account-roles-steps-settings-provided-end

**Review policy**

.. credential-amazon-s3-cross-account-roles-steps-policy-example-intro-start

Review the following sample policy, and then add a policy to the customer-managed Amazon S3 bucket. Add this policy as a trusted policy to the IAM role used to manage access to the customer-managed Amazon S3 bucket.

.. credential-amazon-s3-cross-account-roles-steps-policy-example-intro-end

**Example policy**

.. credential-amazon-s3-cross-account-roles-steps-policy-example-start

The policy for the customer-managed Amazon S3 bucket is unique, but is similar to:

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

Click **Continue** to test the configuration and validate the connection to the customer-managed Amazon S3 bucket, after which you can continue the steps for adding a courier.

.. credential-amazon-s3-cross-account-roles-steps-save-credentials-end





.. vale off

**ATTENTIVE** API + SFTP

.. vale on

Credentials that are unique to Attentive SFTP + API connectors.

**API key**

.. credential-attentive-api-key-start

The API key for your |destination-name| account.

.. credential-attentive-api-key-end

.. vale off

**Hostname** SFTP

.. vale on

See SFTP.

**Passphrase** SFTP

See SFTP.

**Username** SFTP

See SFTP.





.. vale off

**AZURE BLOB STORAGE**

.. vale on

Credentials that are unique to Azure Blob Storage.

.. vale off

**Account name**

.. vale on

.. credential-azure-blob-storage-account-name-start

The name of your |destination-name| storage account.

.. credential-azure-blob-storage-account-name-end

**Connection string**

.. credential-azure-blob-storage-connection-string-start

A connection string allows access to a location within your |destination-name| storage account. A connection string is a combination of your storage account and your account access key.

.. credential-azure-blob-storage-connection-string-end

.. credential-azure-blob-storage-connection-string-overview-start

A `connection string <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account>`__ |ext_link| includes the information that allows Amperity to access your |destination-name| account.

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

Configure value of the blob within the URI as the value for the **Container** setting within Amperity.

.. credential-azure-blob-storage-container-end

**Shared access signature**

.. credential-azure-blob-storage-shared-access-signature-start

A shared access signature (SAS) grants limited access to containers and blobs in your storage account. The value of a SAS is the URI for the resource to which the SAS delegates access, followed by the SAS token.

.. credential-azure-blob-storage-shared-access-signature-end

.. vale off

.. credential-azure-blob-storage-shared-access-signature-overview-start

A `service-level shared access signature (SAS) <https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas>`__ |ext_link| specifies which resources in your |destination-name| account are accessible, what permissions that access allows on resources in the container, and the length of time for which the SAS token is valid.

.. credential-azure-blob-storage-shared-access-signature-overview-end

.. vale on

.. vale off

.. credential-azure-blob-storage-shared-access-signature-permissions-start

When Microsoft Azure is configured to use a shared access signature (SAS) to grant restricted access rights to Microsoft Azure storage resources, be sure to use the correct SAS token string for credentials within Amperity. Assign the SAS token the following permissions within Microsoft Azure: READ, ADD, CREATE, WRITE, DELETE, and LIST.

.. credential-azure-blob-storage-shared-access-signature-permissions-end

.. vale on


**Storage URI**

.. credential-azure-blob-storage-storage-uri-start

A URI for |destination-name| that has the name of the account and the name of the container in which blob storage is located. For example:

::

   https://myaccount.blob.core.windows.net/mycontainer

.. credential-azure-blob-storage-storage-uri-end

.. credential-azure-blob-storage-storage-uri-overview-start

Each |destination-name| resource has a `storage URI <https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#resource-uri-syntax>`__ |ext_link|, which has the name of the account and the name of the container in which blob storage is located.

.. credential-azure-blob-storage-storage-uri-overview-end



.. vale off

**BAZAARVOICE**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**BLUECORE**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**BRAZE**

.. vale on

**API key**

.. credential-braze-api-key-start

Required. The API key for your |destination-name| account.

.. credential-braze-api-key-end





.. vale off

**CAMELOT SMM**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**CORDIAL**

.. TODO: Are the Cordial IAM + S3 bucket settings identical to Amazon S3 destination settings?

.. vale on

For cordial and cordial-aws both use API key and API URL.

**API key**

.. credential-cordial-api-key-start

Required. The API key for your |destination-name| account.

.. credential-cordial-api-key-end

**API URL**

.. credential-cordial-api-url-start

Required. The API URL of your |destination-name| account. May be one of the following: ``https://api.cordial.io/`` or ``https://api.usw2.cordial.io/``.

.. credential-cordial-api-url-end

**IAM access key**

.. credential-cordial-iam-access-key-start

Required. The IAM access key is one part of two that allows Amperity to authenticate to an Amazon S3 bucket. The value for this part of the access key is the access key ID. For example: "AKIAIOSFODNN7EXAMPLE".

.. credential-cordial-iam-access-key-end

**IAM secret key**

.. vale off

.. credential-cordial-iam-secret-key-start

Requried. The IAM secret key is one part of two that allows Amperity to authenticate to an Amazon S3 bucket. The value for this part of the access key is the secret access key. For example: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY".

.. credential-cordial-iam-secret-key-end

.. vale on


**S3 bucket name**

.. credential-cordial-s3-bucket-name-start

Required. The name of the Amazon S3 bucket.

.. credential-cordial-s3-bucket-name-end






.. vale off

**CRITEO**

.. vale on

See OAuth common.





.. vale off

**CROSS COUNTRY COMPUTER**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.




.. vale off

**DOTDIGITAL**

.. vale on

**API username**

.. credential-dotdigital-api-username-start

The username for the API user with permission to access |destination-name|. The API user must have permission to access account information, create and update contacts, manage address books, and manage data fields.

.. credential-dotdigital-api-username-end

**API password**

.. credential-dotdigital-api-password-start

The password for the API user.

.. credential-dotdigital-api-password-end





.. vale off

**EPSILON ABACUS**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**EPSILON CONVERSANT**

**Hostname**

.. vale on

.. credential-epsilon-conversant-hostname-start

"[value]" is the name of your tenant on |destination-name|.

.. credential-epsilon-conversant-hostname-end

**Passphrase**

See SFTP.

**Username**

See SFTP.






.. vale off

**EPSILON TARGETING**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.






.. vale off

**EXPERIAN**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Private key**

See SFTP.

**Username**

See SFTP.




.. vale off

**GOOGLE ADS**

.. vale on

See OAuth common.





.. vale off

**GOOGLE ANALYTICS** / **GOOGLE ANALYTICS 4** (source)

.. vale on

**OAuth flow**

See "OAuth common flows".





.. vale off

**GOOGLE ANALYTICS 4 (GA4)** (destination)

.. vale on

Settings unique to Google Analytics 4 (GA4).

**API secret**

.. credential-google-analytics-api-secret-start

The API secret generated from the Google Analytics admin console for your brand's instance of the `Measurement Protocol API <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=firebase>`__ |ext_link|.

.. credential-google-analytics-api-secret-end

.. credential-google-analytics-api-secret-howto-start

To create an API secret for the Measurement Protocol API log in to Google Analytics. Expand **Data collection** and choose **Data streams**. Choose the data stream to which you want to send purchase events. Click **Measurement Protocol API secrets**, and then click **Create**. Copy the secret and use that value to configure the destination for |destination-name| in Amperity.

.. credential-google-analytics-api-secret-howto-end

**Measurement ID**

.. credential-google-analytics-measurement-id-start

The `measurement ID <https://support.google.com/analytics/answer/12270356?hl=en>`__ |ext_link| associated with your Google Analytics account. All measurement IDs start with "G-" and are followed by a combination of letters and numbers. For example: "G-ABC1DE2FG3".

.. credential-google-analytics-measurement-id-end

.. credential-google-analytics-measurement-id-howto-start

To find the measurement ID log in to Google Analytics. Expand **Data collection** and choose **Data streams**. Select the data stream to which you want to send purchase events. The measurement ID is available under **Stream details**. Copy the measurement ID and use that value to configure the destination for |destination-name| in Amperity.

.. credential-google-analytics-measurement-id-howto-end

**Validate settings**

.. credential-google-analytics-verify-credential-start

|destination-name| only `validates purchase events <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=firebase#payload_validation_info>`__ |ext_link|. |destination-name| does not validate the measurement ID *or* the API secret associated with the payload. Verify that you have configured the correct measurement ID *and* added the correct API secret for the measurement ID.

.. credential-google-analytics-verify-credential-end



.. vale off

**GOOGLE CLOUD STORAGE**

.. vale on

Credentials that are unique to Google Cloud Storage.

**Bucket name**

.. credential-google-cloud-storage-bucket-name-start

`Buckets <https://cloud.google.com/storage/docs/buckets>`__ |ext_link| are basic containers that hold data in |destination-name|. Use buckets to organize storage locations for your data, and then configure Amperity to send data to that bucket.

.. credential-google-cloud-storage-bucket-name-end

.. credential-google-cloud-storage-bucket-name-must-match-start

The bucket name must match the value of the ``<<GCS_BUCKET_NAME>>`` placeholder shown in the :ref:`service account key example <destination-google-cloud-storage-service-account-key-example>`.

.. credential-google-cloud-storage-bucket-name-must-match-end

**Service account key**

.. vale off

.. credential-google-cloud-storage-service-account-key-start

Google Cloud uses service account key-pairs for authentication. A public service account key is stored in Google Cloud. A private service account key allows applications access to your instance of |destination-name|.

.. credential-google-cloud-storage-service-account-key-end

.. vale on


.. credential-google-cloud-storage-service-account-key-value-start

The value of the private service account key is the contents of the JSON file downloaded from Google Cloud after `creating the service account key-pair <https://cloud.google.com/iam/docs/keys-create-delete>`__ |ext_link|. Open the JSON file in a text editor, select the content in the JSON file, copy it, and then paste it into the **Service account key** field.

.. credential-google-cloud-storage-service-account-key-value-end

**Service account role**

.. TODO: Is the service account role required for sending data *and* pulling data from Google Cloud Storage? Or just pulling data?

.. credential-google-cloud-storage-service-account-role-start

Assign the **Storage Object Admin** role to the service account.

.. credential-google-cloud-storage-service-account-role-end



.. vale off

**GOOGLE CUSTOMER MATCH**

.. vale on

See OAuth common.





.. vale off

**HUBSPOT**

.. vale on

See OAuth common.





.. vale off

**INFUTOR**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**KIBO**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**KLAVIYO**

.. vale on

**API key**

.. credential-klaviyo-api-key-start

Required. The API key for your |destination-name| account.

.. credential-klaviyo-api-key-end

.. credential-klaviyo-api-key-scopes-start

The `private API key <https://developers.klaviyo.com/en/docs/authenticate_#private-key-authentication>`__ |ext_link| used for authentication must have the following scopes added:

* **lists:write**
* **profiles:write**

.. credential-klaviyo-api-key-scopes-end





.. vale off

**KOUPON MEDIA**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**LISTRAK**

**Allowlist callout**

.. vale on

.. credential-listrak-allowlist-start

The Amperity `IP address for allowlists <https://docs.amperity.com/operator/send_data.html#ip-allowlists>`__ |ext_link| must belong to the allowlist for the |destination-name| integration.

.. credential-listrak-allowlist-end

**Client ID and client secret location**

.. credential-listrak-client-id-secret-location-start

.. tip:: The client ID and client secret are available from the **Integrations** menu in |destination-name|. Open the **Integrations** menu, select **Integrations Management**, and then from the **Integrations** page choose an integration. The client ID and client secret are on the **Setup** tab.

.. credential-listrak-client-id-secret-location-end

**Email client ID and client secret**

.. credential-listrak-email-client-id-secret-start

A client ID and secret for an email integration that is already set up in |destination-name|.

.. credential-listrak-email-client-id-secret-end

**SMS client ID and client secret**

.. credential-listrak-sms-client-id-secret-start

A client ID and secret for an SMS integration that is already set up in |destination-name|.

.. credential-listrak-sms-client-id-secret-end






.. vale off

**LIVERAMP**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**MAILCHIMP**

.. vale on

**API key**

.. credential-mailchimp-api-key-start

Required. The API key for your |destination-name| account.

.. credential-mailchimp-api-key-end





.. vale off

**META ADS MANAGER** Facebook

.. vale on

**OAuth flow**

See "OAuth common flows".





.. vale off

**META ADS MANAGER: EVENTS**

.. vale on

**OAuth flow**

See "OAuth common flows".





.. vale off

**MICROSOFT ADVERTISING**

.. vale on

**OAuth flow**

See "OAuth common flows".





.. vale off

**MICROSOFT DATAVERSE**

.. vale on

.. credential-microsoft-dataverse-requirements-start

Configure Microsoft Azure for your Power Apps application, and then add the Power Apps application to the Microsoft Power Platform.

.. credential-microsoft-dataverse-requirements-end

**Azure tenant ID**

.. credential-microsoft-dataverse-azure-tenant-id-start

The Microsoft Azure tenant ID for your instance of |destination-name|.

.. credential-microsoft-dataverse-azure-tenant-id-end

**Azure client ID and client secret**

.. credential-microsoft-dataverse-azure-client-id-and-secret-start

A client ID and client secret for Microsoft Azure that has permission to access your instance of |destination-name|.

.. credential-microsoft-dataverse-azure-client-id-and-secret-end





.. vale off

**MICROSOFT DYNAMICS 365 MARKETING**

.. vale on

**Azure client ID and client secret**

.. credential-microsoft-dynamics-365-marketing-azure-client-id-and-secret-start

A client ID and client secret for Microsoft Azure that has permission to access your instance of |destination-name|.

.. credential-microsoft-dynamics-365-marketing-azure-client-id-and-secret-end

**Azure tenant ID**

.. credential-microsoft-dynamics-365-marketing-azure-tenant-id-start

The Microsoft Azure tenant ID for your instance of |destination-name|.

.. credential-microsoft-dynamics-365-marketing-azure-tenant-id-end






.. vale off

**MICROSOFT DYNAMICS**

.. vale on

**Client ID and client secret**

.. credential-microsoft-dynamics-client-id-and-secret-start

A client ID and client secret with permission to access your instance of |destination-name|.

.. credential-microsoft-dynamics-client-id-and-secret-end

.. credential-microsoft-dynamics-client-id-and-secret-expiration-start

Set the expiration date for client secrets to "expires in 1 year", "expires in 2 years", or "never expires".

.. credential-microsoft-dynamics-client-id-and-secret-expiration-end




.. vale off

**MONETATE**

.. vale on

See Kibo.





.. vale off

**NEUSTAR**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

.. credential-neustar-passphrase-start

|destination-name| requires rotating SFTP passphrases every 180 days. A rotated passphrase must updated in Amperity.

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

.. vale off

.. credential-oauth-refresh-token-start

A refresh token is generated by the OAuth process and authorizes Amperity to send data to |destination-name|. The value for the refresh token is automatically updated.

.. credential-oauth-refresh-token-end

.. vale on

**Reauthorize token**

.. vale off

.. credential-oauth-reauthorize-start

You may need to reauthorize access to |destination-name|. This is necessary when an authorization token expires or is removed. To reauthorize access to |destination-name|, follow the steps to configure OAuth and create a new credential.

.. credential-oauth-reauthorize-end

.. vale on




.. vale off

**ORACLE DATA CLOUD**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.







.. vale off

**ORACLE ELOQUA**

.. vale on

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





.. vale off

**ORACLE RESPONSYS**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Private key**

See SFTP.

**Username**

See SFTP.






.. vale off

**PANDA PRINTING**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.






.. vale off

**PEBBLEPOST**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**PERSADO**

**Hostname**

.. vale on

See SFTP.

**Private key**

See SFTP.

**Username**

See SFTP.





.. vale off

**PINTEREST**

.. vale on

See OAuth common.




.. vale off

**PINTEREST EVENTS**

.. vale on

.. credential-pinterest-events-conversion-access-token-start

A Bearer token generated from `Pinterest Ads Manager <https://ads.pinterest.com/>`__ |ext_link|.

.. credential-pinterest-events-conversion-access-token-end

.. credential-pinterest-events-conversion-access-token-find-start

Log in to |destination-name| Ads Manager, select **Ad Account Overview**, **Conversions**, **Conversions API**, and then **Set up API**. Select **Conversion access token** and then click **Generate new token**. Copy the token, and then use it to configure the **Conversion access token** credential setting in Amperity.

.. credential-pinterest-events-conversion-access-token-find-end

.. credential-pinterest-events-conversion-access-token-owner-or-admin-start

.. important:: The user account that generates the access token `must be the Owner of the ads account or be assigned the Admin, Analyst, Audience, or Campaign role <https://help.pinterest.com/en/business/article/business-manager-access-roles-and-permissions>`__ |ext_link| in |destination-name|.

.. credential-pinterest-events-conversion-access-token-owner-or-admin-end





.. vale off

**POWERREVIEWS**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**QUAD**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.






.. vale off

**RR DONNELLY**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.






.. vale off

**SAILTHRU**

.. vale on

**API key**

.. credential-sailthru-api-key-start

The API key for your |destination-name| account.

.. credential-sailthru-api-key-end

**Secret**

.. credential-sailthru-secret-start

The API secret for your |destination-name| account.

.. credential-sailthru-secret-end

.. vale off

.. credential-sailthru-api-find-key-and-secret-start

You can find the API key and secret after you log in to |destination-name| and authenticate to the Sailthru API. The API key and API secret are available on the "Setup – API & Postbacks" page.

.. credential-sailthru-api-find-key-and-secret-end

.. vale on





.. vale off

**SALESFORCE COMMERCE CLOUD**

.. vale on





.. vale off

**SALESFORCE MARKETING CLOUD**

.. vale on

**API client ID and client secret**

.. credential-salesforce-marketing-cloud-api-client-secret-start

The client ID and client secret for your brand's instance of the Marketing Cloud SOAP API.

.. credential-salesforce-marketing-cloud-api-client-secret-end

**API subdomain**

.. credential-salesforce-marketing-cloud-api-subdomain-start

The authentication subdomain for your brand's instance of the Marketing Cloud SOAP API.

.. credential-salesforce-marketing-cloud-api-subdomain-end


.. vale off

.. credential-salesforce-marketing-cloud-api-subdomain-base-uri-start

The authentication subdomain for the `SOAP base URI <https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/your-subdomain-tenant-specific-endpoints.html>`__ |ext_link| is a 28-character string that starts with the letters "mc", such as "mcabc123...".

.. credential-salesforce-marketing-cloud-api-subdomain-base-uri-end

.. vale on

.. vale off

**SFTP hostname**

.. vale on

.. vale off

.. credential-salesforce-marketing-cloud-hostname-start

"[hostname]" is the name of your tenant on |destination-name|.

.. credential-salesforce-marketing-cloud-hostname-end

.. vale on

.. vale off

.. credential-salesforce-marketing-cloud-hostname-context-start

The SFTP host name is a 28-character string that starts with the letters "mc", such as "mcabc123...". This is the same 28-character string that represents the subdomain, which is part of the SOAP base URI for Salesforce Marketing Cloud.

.. credential-salesforce-marketing-cloud-hostname-context-end

.. vale on

**SFTP passphrase**

See SFTP.

**SFTP username**

See SFTP.





.. vale off

**SALESFORCE SALES CLOUD**

.. vale on

**Security token**

.. credential-salesforce-sales-cloud-security-token-start

The Salesforce security token associated with the username. This setting is not required when configuring IP range policies from the Salesforce administrator console.

.. credential-salesforce-sales-cloud-security-token-end

**Username and password**

.. credential-salesforce-sales-cloud-username-and-password-start

The username and password of a Salesforce account configured for API access.

.. credential-salesforce-sales-cloud-username-and-password-end




.. vale off

**SAP EMARSYS**

.. vale on

SAP Emarsys uses OAuth, but for this connector you must provide the client ID and client secret as a config setting in Amperity.

**Client ID and secret**

.. setting-sap-emarsys-client-id-and-secret-start

A client ID and client secret with permission to access your instance of |destination-name|. These values are part of the `API credentials <https://help.sap.com/docs/SAP_EMARSYS/5d44574160f44536b0130abf58cb87cc/fdf4b58974c110149353957a3e7ef453.html?locale=en-US&state=PRODUCTION&version=CLOUD&q=client%20id>`__ |ext_link| configured for your instance of |destination-name|.

.. important:: The OAuth user associated with the client ID and secret must have `contact, contactlist, and field <https://dev.emarsys.com/docs/emarsys-core-api-guides/ef41493bd7812-endpoint-permission-settings>`__ |ext_link| permissions to the SAP Emarsys Rest API.

.. setting-sap-emarsys-client-id-and-secret-end




.. vale off

**SFTP**

Credentials that are unique to SFTP. These credentials apply to all sources and destinations that use SFTP, including Acxiom, Adobe Campaign, Adobe Customer Attributes, Adobe Experience Platform, Airship, Attentive, BazaarVoice, Bluecore, Camelot SMM, Cheetah Digital, Criteo (events), Cross Country Computer, Emarsys, Epsilon, Evocalize, Experian, Infutor, Iterable, Kibo, Koupon Media, LiveRamp, Neustar, Oracle Data Cloud, Oracle DMP, Oracle Responsys, PebblePost, Persado, Pinterest (product catalogs), PowerReviews, Quad, Reddit Ads, RR Donnelly, Salesforce Commerce Cloud, Salesforce Marketing Cloud, Salesforce Marketing Cloud Personalization, SMG, SoundCommerce, Vibes.

.. vale on

.. credential-sftp-about-start

Secure File Transfer Protocol (SFTP) is a network connection that uses a combination of host name and username, along with a passphrase, public key, or private key.

.. credential-sftp-about-end

**Host public key**

.. credential-sftp-host-public-key-start

The host public key for |where-send|.

.. credential-sftp-host-public-key-end

.. vale off

**Hostname**

.. vale on

.. credential-sftp-hostname-start

Required. The host name for |where-send|. For example: |sftp-hostname|.

.. credential-sftp-hostname-end

**Passphrase**

.. credential-sftp-passphrase-start

The passphrase associated with the username.

.. credential-sftp-passphrase-end

**Port**

.. credential-sftp-port-start

The port number required by |where-send|. Use this setting only when the SFTP site uses a non-default port value.

.. credential-sftp-port-end

**Private key**

.. credential-sftp-private-key-start

A private key for encrypting files sent to |where-send|.

.. credential-sftp-private-key-end

.. vale off

.. credential-sftp-private-key-required-start

This setting is required by the "private-key" credential type.

.. credential-sftp-private-key-required-end

.. vale on

**Username**

.. credential-sftp-username-start

Required. A username with access to |where-send|. This username must have permission to write data to the remote folder to which Amperity sends data.

.. credential-sftp-username-end




.. vale off

**SHOPIFY**

.. vale on

**Access token**

.. credential-shopify-access-token-start

.. TODO: xxxxx

.. credential-shopify-access-token-end

**Shop name**

.. credential-shopify-shop-name-start

.. TODO: xxxxx

.. credential-shopify-shop-name-end




.. vale off

**SMG**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.





.. vale off

**SNAPCHAT**

.. vale on

See OAuth.





.. vale off

**SNOWFLAKE**

.. vale on

These settings apply to destination *and* bridge.

.. vale off

**Account name**

.. vale on

.. credential-snowflake-account-name-start

The unique name of an account that exists within your brand's |destination-name| organization.

.. credential-snowflake-account-name-end

.. vale off

.. credential-snowflake-account-name-required-permissions-start

.. important:: Grant the role :ref:`write permission to Snowflake objects <source-snowflake-azure-configure-objects>`, :ref:`permission to access each table <source-snowflake-azure-configure-tables>`, and permission to :ref:`write table output to Azure Blob Storage <source-snowflake-azure-configure-storage-integration>`.

.. credential-snowflake-account-name-required-permissions-end

.. vale on

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

The `region <https://docs.snowflake.com/en/user-guide/intro-regions>`__ |ext_link| that hosts your |destination-name| account. Use the `CURRENT_REGION <https://docs.snowflake.com/en/sql-reference/functions/current_region>`__ |ext_link| argument in |destination-name| to return the value for your region.

.. credential-snowflake-region-end

**Username**

.. credential-snowflake-username-start

A username with permission to access |destination-name|.

.. credential-snowflake-username-end

.. vale off

**SNOWFLAKE** AWS-specific

.. vale on

**IAM access key**

.. credential-snowflake-iam-access-key-start

Required. The IAM access key, along with the secret key, that allows Amperity to authenticate to Snowflake.

.. credential-snowflake-iam-access-key-end

**IAM role ARN**

.. credential-snowflake-iam-role-arn-start

The IAM role ARN used by Amperity to access Snowflake.

.. credential-snowflake-iam-role-arn-end

**IAM secret key**

.. credential-snowflake-iam-secret-key-start

Required. The IAM secret key, along with the access key, that allows Amperity to authenticate to Snowflake.

.. credential-snowflake-iam-secret-key-end

.. vale off

**SNOWFLAKE** Azure-specific

**Account name**

.. vale on

.. credential-snowflake-account-name-start

The account name for Microsoft Azure Blob Storage.

.. credential-snowflake-account-name-end

**Shared access signature**

.. credential-snowflake-shared-access-signature-start

The shared access signature that allows access to a Microsoft Azure Blob Storage container.

.. credential-snowflake-shared-access-signature-end




.. vale off

**SOUNDCOMMERCE**

**Hostname**

.. vale on

See SFTP.

**Private key**

See SFTP.

**Username**

See SFTP.





.. vale off

**THE TRADE DESK**

.. vale on

**Advertiser ID**

.. credential-the-trade-desk-advertiser-id-start

The advertiser ID for your account with |destination-name|.

.. credential-the-trade-desk-advertiser-id-end

**Advertiser secret**

.. credential-the-trade-desk-advertiser-secret-start

The advertiser secret for your account with |destination-name|.

.. credential-the-trade-desk-advertiser-secret-end

**Where is the ID and secret?**

.. credential-the-trade-desk-find-id-and-secret-start

You can find the advertiser ID and secret key from the management console within |destination-name|. Open "Preferences", and then "First Party Data Credentials" to view the advertiser ID and secret key.

.. credential-the-trade-desk-find-id-and-secret-end





.. vale off

**THE TRADE DESK: 3P MARKETPLACE**

.. vale on

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





.. vale off

**THE TRADE DESK: EVENTS**

.. vale on

**Advertiser ID**

See The Trade Desk.

**Advertiser secret**

See The Trade Desk.





.. vale off

**TIKTOK ADS MANAGER**

.. vale on

See OAuth.

**Required permissions**

.. credential-tiktok-ads-manager-oauth-requirements-start

TikTok Advertiser Accounts must use OAuth. Assign the account used to allow access to |destination-name| the "TikTok Ad Account Operator" or the "TikTok Ad Account Admin" permission. OAuth does not work with the "TikTok Ad Account Analyst" permission.

.. credential-tiktok-ads-manager-oauth-requirements-end




.. vale off

**TIKTOK ADS MANAGER: EVENTS**

.. vale on

See OAuth.

See TikTok Ads Manager.





.. vale off

**VIBES**

**Hostname**

.. vale on

See SFTP.

**Passphrase**

See SFTP.

**Username**

See SFTP.




.. vale off

**YAHOO DSP**

.. vale on

**Site MDM ID**

.. vale off

.. credential-yahoo-dsp-mdm-id-start

Required. The "Site MDM ID" is the value of your brand's Master Data Management (MDM) ID in |destination-name|. This is a unique advertiser ID that assigns your brand a specific location within the |destination-name| taxonomy.

.. credential-yahoo-dsp-mdm-id-end

.. vale on




.. vale off

**ZENDESK**

.. vale on

**API token**

.. credential-zendesk-api-token-start

Required. Your brand's Zendesk API token.

.. credential-zendesk-api-token-end


**Email address**

.. credential-zendesk-email-address-start

Required. The email address for the Zendesk API user.

.. credential-zendesk-email-address-end
