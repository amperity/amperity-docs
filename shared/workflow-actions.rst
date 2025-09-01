.. 
.. xxxxx
..



**TEMPLATE SECTIONS FOR WORKFLOW ACTIONS**
**TEMPLATE SECTIONS FOR WORKFLOW ACTIONS**
**TEMPLATE SECTIONS FOR WORKFLOW ACTIONS**



**INTRO**

.. workflow-actions-common-table-intro-start

A workflow will occasionally show an error that describes what prevented a workflow from completing successfully. These first appear as alerts in the notifications pane. The alert describes the error, and then links to the **Workflows** tab.

Open the **Workflows** page to review a list of workflow actions, choose an action to resolve the workflow error, and then follow the steps that are shown.

.. workflow-actions-common-table-intro-end


**TABLE, SECTION ONE**
**TABLE, SECTION ONE**
**TABLE, SECTION ONE**

.. workflow-actions-common-table-section-one-a-start

You may receive a notifications error for a configured |destination-name| destination. This appears as an alert in the notifications pane on the **Destinations** tab.

.. workflow-actions-common-table-section-one-a-end

.. workflow-actions-common-table-section-one-a-source-start

You may receive a notifications error for a configured |source-name| data source. This appears as an alert in the notifications pane on the **Destinations** tab.

.. workflow-actions-common-table-section-one-a-source-end

**IMAGE IS HERE**

.. workflow-actions-common-table-section-one-b-start

If you receive a notification error, review the details, and then click the **View Workflow** link to open this notification error in the **Workflows** page.

.. workflow-actions-common-table-section-one-b-end



**TABLE, SECTION TWO**
**TABLE, SECTION TWO**
**TABLE, SECTION TWO**

.. workflow-actions-common-table-section-two-start

On the **Workflows** page, review the individual steps to determine which steps have errors that require your attention, and then click **Show Resolutions** to review the list of workflow actions that were generated for this error.

.. workflow-actions-common-table-section-two-end

**IMAGE IS HERE**




**TABLE, SECTION THREE (THIS CAN HAVE BESPOKE SECTIONS SEE TODO)**
**TABLE, SECTION THREE (THIS CAN HAVE BESPOKE SECTIONS SEE TODO)**
**TABLE, SECTION THREE (THIS CAN HAVE BESPOKE SECTIONS SEE TODO)**

.. workflow-actions-common-table-section-three-a-start

A list of individual workflow actions are shown. Review the list to identify which action you should take.

.. workflow-actions-common-table-section-three-a-end

**IMAGE IS HERE**

.. workflow-actions-common-table-section-three-b-start

Some workflow actions are common across workflows and will often be available, such as retrying a specific task within a workflow or restarting a workflow. These types of actions can often resolve an error.

In certain cases, actions are specific and are shown when certain conditions exist in your tenant. These types of actions typically must be resolved and may require steps that must be done upstream or downstream from your Amperity workflow.

.. workflow-actions-common-table-section-three-b-end

.. TODO: Immediately after "section three" there is often a bespoke list of links to workflow action sections that are unique. See Salesforce Marketing Cloud, Zendesk, and/or Active Campaign for examples of how this can vary across topics.


**TABLE, SECTION FOUR**
**TABLE, SECTION FOUR**
**TABLE, SECTION FOUR**

.. workflow-actions-common-table-section-four-a-start

Select a workflow action from the list of actions, and then review the steps for resolving that error.

.. workflow-actions-common-table-section-four-a-end

.. workflow-actions-common-table-section-four-b-start

After you have completed the steps in the workflow action, click **Continue** to rerun the workflow.

.. workflow-actions-common-table-section-four-b-end






**GENERIC FILES BAD ARCHIVE**
**GENERIC FILES BAD ARCHIVE**
**GENERIC FILES BAD ARCHIVE**

.. TODO: This is a bit hand-wavy and vague.

.. workflow-actions-files-generic-bad-archive-start

Sometimes the contents of an archive are corrupted and cannot be loaded to Amperity.

To resolve this error, do the following.

#. Upload a new file to Amperity.
#. After the file to the workflow action, and then click **Resolve** to retry this workflow.

.. workflow-actions-files-generic-bad-archive-end




**AMAZON S3 INCORRECT BUCKET NAME**
**AMAZON S3 INCORRECT BUCKET NAME**
**AMAZON S3 INCORRECT BUCKET NAME**

.. workflow-actions-s3-generic-incorrect-bucket-name-destination-start

The name of the Amazon S3 bucket to which Amperity pushes data must be correctly specified in the configuration for the destination in the **Destinations** page.

To resolve this error, do the following.

#. Open the AWS management console and verify the name of the Amazon S3 bucket.
#. Open the **Destinations** page in Amperity, and then open the destination that is associated with this workflow.
#. Update the destination for the correct Amazon S3 bucket name.
#. Return to the workflow action, and then click **Resolve** to retry.

.. workflow-actions-s3-generic-incorrect-bucket-name-destination-end

.. workflow-actions-s3-generic-incorrect-bucket-name-source-start

The name of the Amazon S3 bucket from which Amperity pulls data must be correctly specified in the configuration for the courier in the **Sources** page.

To resolve this error, do the following.

To resolve this error, verify name of the Amazon S3 bucket, and then update the configuration in Amperity to match.

#. Open the AWS management console and verify the name of the Amazon S3 bucket.
#. Open the **Sources** page in Amperity, and then open the courier that is associated with this workflow.
#. Update the courier configuration for the correct Amazon S3 bucket name.
#. Return to the workflow action, and then click **Resolve** to retry.

.. workflow-actions-s3-generic-incorrect-bucket-name-source-end




**GENERIC FILES MISSING FILE**
**GENERIC FILES MISSING FILE**
**GENERIC FILES MISSING FILE**

.. workflow-actions-files-generic-missing-file-start

An archive that does not contain a file that is expected to be within an archive will return a workflow error; Amperity will be unable to complete the workflow until the issue is resolved.

To resolve this error, do the following.

#. Add the required file to the archive.

   *or*

   Update the configuration for the courier that is attempting to load the missing file to not require that file.
#. After the file is added to the archive *or* removed from the courier configuration, click **Resolve** to retry this workflow.

.. workflow-actions-files-generic-missing-file-end




**GENERIC FILES UNABLE TO DECOMPRESS FILE**
**GENERIC FILES UNABLE TO DECOMPRESS FILE**
**GENERIC FILES UNABLE TO DECOMPRESS FILE**

.. workflow-actions-files-unable-to-decompress-file-start

An archive that cannot be decompressed will return a workflow error; Amperity will be unable to complete the workflow until the issue is resolved.

This issue may be shown when the name of the archive doesn't match the name of the configured archive or when Amperity is attempting to decompress a file (and not an archive). In some cases, the contents of the archive file may be the reason why Amperity is unable to decompress the archive.

To resolve this error, do the following.

#. Verify the configuration for the archive, and then verify the contents of the archive.

   Update the configuration, if neccessary. For example, when Amperity is attempting to decompress a file, update the configuration to specify a file and not an archive.

   In some cases, re-loading the archive to the location from which Amperity is attempting to pull the archive is necessary.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. workflow-actions-files-unable-to-decompress-file-end





**GENERIC INVALID CREDENTIALS**
**GENERIC INVALID CREDENTIALS**
**GENERIC INVALID CREDENTIALS**

.. workflow-actions-generic-invalid-credentials-start

The credentials that are defined in Amperity are invalid.

To resolve this error, verify that the credentials required by this workflow are valid.

#. Open the **Credentials** page.
#. Review the details for the credentials used with this workflow. Update the credentials for |destination-name| if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. workflow-actions-generic-invalid-credentials-end

.. workflow-actions-generic-invalid-credentials-source-start

The credentials that are defined in Amperity are invalid.

To resolve this error, verify that the credentials required by this workflow are valid.

#. Open the **Credentials** page.
#. Review the details for the credentials used with this workflow. Update the credentials for |source-name| if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. workflow-actions-generic-invalid-credentials-source-end


**GENERIC PGP ERROR**
**GENERIC PGP ERROR**
**GENERIC PGP ERROR**

.. workflow-actions-generic-pgp-error-start

A workflow action is created when a file cannot be decrypted using the provided PGP key.

To resolve this error, verify the PGP key.

#. Open the **Sources** page.
#. Review the details for the PGP key.

   If the PGP key is correct, verify that the file that is associated with this workflow error was encrypted using the correct PGP key. If necessary, upload a new file.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. workflow-actions-generic-pgp-error-end




**GENERIC STATUS 401**
**GENERIC STATUS 401**
**GENERIC STATUS 401**

.. workflow-actions-generic-status-401-start

A "Status 401" error is an authorization error: Amperity was unable to connect to |destination-name|. This *may* be a transient error; however, this type of error is more likely caused by a configuration issue within Amperity. For example, the currently-configured API key is invalid because the API key was rotated.

To resolve this error, verify that the credentials required by this workflow are valid.

#. Open the **Credentials** page.
#. Review the details for the credentials used with this workflow. Update the credentials for |destination-name| if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. workflow-actions-generic-status-401-end




**MICROSOFT AZURE SAS TOKENS**
**MICROSOFT AZURE SAS TOKENS**
**MICROSOFT AZURE SAS TOKENS**

.. workflow-actions-azure-sas-intro-start

Microsoft Azure may be configured to use a shared access signature (SAS) to grant restricted access rights to Microsoft Azure storage resources.

.. workflow-actions-azure-sas-intro-end

.. workflow-actions-azure-sas-whatis-start

.. admonition:: What is a shared access signature (SAS)?

   A shared access signature (SAS) grants limited access to storage resources in Microsoft Azure. A SAS may be constrained to access only specific storage resources, have specific permissions to those resources, and be configured to expire after a set amount of time. Every SAS is signed with a key.

   The SAS is appended to the URI for a storage resource. The combined URI and SAS become a token that contains a set of query parameters that indiciate how a storage resource may be accessed. Use the SAS token to configure Amperity credentials to storage resources in Microsoft Azure.

.. workflow-actions-azure-sas-whatis-end

.. workflow-actions-azure-sas-invalid-permissions-start

An SAS token may have invalid permissions for any of the following situations:

#. The SAS token may be configured incorrectly within Amperity. For example: an extra character within or at at the end of the SAS token. Verify the string, and then make any updates that are required for the credentials within Amperity.

#. The permissions for the SAS token were configured incorrectly. Amperity requires an SAS token to be assigned the following permissions: READ, ADD, CREATE, WRITE, DELETE, and LIST.

#. The SAS token may have expired or the signing key associated with the SAS token may have been rotated.

   These situations will require generating a new SAS token, and then updating the credentials in Amperity.

.. workflow-actions-azure-sas-invalid-permissions-end

.. workflow-actions-azure-sas-report-problem-start

.. note:: If the shared access signature was provisioned by Amperity, please use the "Report a problem" feature in Amperity to contact your Amperity Support team and ask for help resolving this workflow issue.

   The "Report a problem" option is available from the |fa-help-circle| menu in the top navigation.

.. workflow-actions-azure-sas-report-problem-end

.. workflow-actions-azure-sas-steps-start

To resolve this error, determine the cause for the invalid permissions error.

#. Do one or more of the following:

   Verify that the SAS token was configured correctly within Amperity.

   Verify the permissions that have been assigned to the SAS token. This can be done from the Microsoft Azure Portal or by using `Azure Storage Explorer <https://azure.microsoft.com/en-in/products/storage/storage-explorer/>`__ |ext_link|. The policy for the SAS token must be assigned the following permissions: READ, ADD, CREATE, WRITE, DELETE, and LIST.

   Verify that the SAS token and/or the signing key associated with the SAS token is valid (and has not expired). If either have expired, generate a new SAS token (using a new signing key, if necessary).

#. After you have determined the cause of the invalid permissions error, make the appropriate updates within Microsoft Azure and/or the credentials for this destination within Amperity.

#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. workflow-actions-azure-sas-steps-end



**SFTP UNAVAILABLE (SHARED)**
**SFTP UNAVAILABLE (SHARED)**
**SFTP UNAVAILABLE (SHARED)**

.. TODO: This is a bit hand-wavy and vague.

.. workflow-actions-sftp-generic-unavailable-start

The SFTP site at |sftp-hostname| is unavailable. This may be due to any of the following issues:

* A configuration error within Amperity.
* The SFTP server is unavailable or unresponsive.
* The SFTP server does not have enough storage space.
* Too many connection attempts were made to the SFTP server.

.. note:: Amperity will make multiple attempts to connect to an SFTP server before showing this workflow error.

To resolve this error, do any of the following.

#. Verify the configuration for |sftp-hostname|.
#. Verify that the SFTP server is available and responsive.
#. Verify the amount of storage space that is available on the SFTP server.
#. Decrease the number of couriers in Amperity that are configured to connect to |sftp-hostname|.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. workflow-actions-sftp-generic-unavailable-end

