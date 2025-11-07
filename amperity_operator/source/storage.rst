.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure Amperity to use Amazon S3 bucket or Azure Blob Storage.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to use Amazon S3 bucket or Azure Blob Storage.

.. meta::
    :content class=swiftype name=title data-type=string:
        About storage

==================================================
About storage
==================================================

.. storage-about-start

Amperity stores the following outputs in Amazon S3 storage or Azure Blob Storage, depending on the cloud platform in which your Amperity tenant is provisioned. These outputs include:

* Data that was ingested to Amperity, and then loaded to domain tables
* Tables that are maintained by Stitch
* Stitch reports
* Validation reports
* Database tables
* File uploads
* SQL results, including Spark SQL checkpoints
* Orchestration and campaign results
* User audit logs
* Conversations with Amp AI

.. storage-about-start

.. storage-about-warning-start

.. warning:: Configured storage applies only to new Amperity tenants that are provisioned for Amazon S3 or Microsoft Azure.

.. storage-about-warning-end


.. _storage-configure-location:

Choose storage location
==================================================

.. storage-configure-location-start

The location in which Amperity stores outputs is configurable. The first step for a new tenant allows your brand to choose one of the following storage locations:

#. An :ref:`Amazon S3 storage location <storage-provision-location-aws>` that is owned and managed by your brand.

   **or**

   A :ref:`Microsoft Azure Blob Storage location <storage-provision-location-azure>` that is owned and managed by your brand.

#. An Amazon S3 storage location that is only used by your tenant that is provisioned automatically by default and managed by Amperity.

   **or**

   A Microsoft Azure Blob Storage location that is only used by your tenant that is provisioned automatically by default and managed by Amperity.

.. storage-configure-location-end


.. _storage-provision-location-aws:

Provision storage on Amazon AWS
==================================================

.. storage-provision-location-aws-start

Configure a new tenant to use an Amazon S3 storage location that is owned and managed by your brand.

.. storage-provision-location-aws-end

**To provision storage on Amazon AWS**

.. storage-provision-location-aws-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - **Choose a storage location**

       #. Log in to the Amazon AWS console as a user with credentials that allow storage to be configured for your brand from within `AWS CloudFormation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html>`__ |ext_link|, such as an administrator.

          .. important:: When Amperity opens **AWS CloudFormation** during the storage setup process the IAM roles that are used for operations and role assumption within **AWS CloudFormation** is inherited from the IAM role that is assigned to the logged-in user.

       #. Log in to your Amperity tenant.

          .. note:: If your brand has chosen Amperity-managed storage the following setup workflow steps are skipped.

       #. The **Storage Setup** page appears.

          .. image:: ../../images/storage-steps.png
             :width: 380 px
             :alt: The Storage Setup page.
             :align: left
             :class: no-scaled-link

          Each step must be completed before you can start using Amperity.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - **Specify regions**

       Specify the regions in which your brand wants to configure primary and backup storage, and then click **Continue**.

       Regions for configured storage should be the same regions in which Amperity is located.

       .. note:: Amperity is hosted in one of the following Amazon AWS regions:

          .. list-table::
             :widths: 50 50
             :header-rows: 0

             * - US West
               - **us-west-2**
             * - Canada
               - **ca-central-1**

          `Cross-region transfer costs <https://aws.amazon.com/s3/pricing/>`__ |ext_link| will apply when Amazon S3 storage is configured in different region than the one in which your Amperity tenant is hosted and will increase latency.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - **Create backup storage**

       Backup storage is provisioned using **AWS CloudFormation**.

       #. Click **Provision CloudFormation stack**. This opens the **Quick create stack** page in **AWS CloudFormation**.
       #. Provide the stack name.

          .. note:: The value for stack name is pre-populated by Amperity in the form of

             ::

                amperity-<tenant>-<infracode>-backup

             It is recommended to keep the pre-populated stack name.

       #. Optional. Configure the IAM role for **AWS CloudFormation** to *use for all operations performed on this stack*.

          .. note:: **AWS CloudFormation** will automatically use the credentials assigned to the user who is configuring the storage location.

       #. Review the parameters and configure the number of days for backups to be locked and retained.

          .. important:: The values for **InfraCode** and **Tenant** should not be changed.

       #. Optional. Configure the IAM role for **AWS CloudFormation** to *assume when performing operations on this stack*.

          .. note:: **AWS CloudFormation** will automatically use the credentials assigned to the user who is configuring the storage location.

       #. When finished, click **Create stack**.

          **AWS CloudFormation** will begin provisioning backup storage. This may take a few minutes.

          After provisioning for backup storage is complete return to the **Create backup storage** page in the storage setup workflow.

       #. On the **Create backup storage** page click **Continue**.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - **Create primary storage**

       Primary storage is provisioned using **AWS CloudFormation**.

       .. important:: The values for primary storage are prepopulated using the information that was provided for backup storage. You may change these values in **AWS CloudFormation**, if necessary.

       #. The steps for configuring primary storage are nearly identical to backup storage. Click **Provision CloudFormation stack**, which opens the **Quick create stack** page in **AWS CloudFormation**. Provide a stack name, review IAM credentials and parameters, and then provision primary storage.

          .. note:: The value for stack name is pre-populated by Amperity in the form of

             ::

                amperity-<tenant>-<infracode>-storage

             It is recommended to keep the pre-populated stack name.

          .. important:: You must allow **AWS CloudFormation** to create IAM resources. Select the checkbox under "The following resources require capabilities [AWS::IAM::Role]".

       #. When finished, click **Create stack**.

          **AWS CloudFormation** will begin provisioning primary storage. This may take a few minutes.

          After provisioning for primary storage is complete return to the **Create primary storage** page in the storage setup workflow.

       #. On the **Create primary storage** page click **Continue**.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - **Bind storage**

       After backup storage and primary storage are provisioned test the connection between Amperity and provisioned storage.

       #. Copy the value for the **AccessRole** for primary storage. Add the value to the **Access Role ARN** field in the **Bind storage** page. Click **Test connection**.

          .. tip:: The value for the access role ARN is found on the **Outputs** tab for the configured primary storage.

             .. image:: ../../images/storage-access-role-arn.png
                :width: 380 px
                :alt: Copy the access role ARN for primary storage and provide it to Amperity.
                :align: left
                :class: no-scaled-link

       #. If the connection is successful click **Finish** to bind your Amperity tenant to the configured backup and primary storage.

       After the storage setup workflow is finished you are redirected to your tenant and can configure identity resolution.

.. storage-provision-location-aws-steps-end


.. _storage-provision-location-azure:

Provision storage on Microsoft Azure
==================================================

.. storage-provision-location-azure-start

Configure a new tenant to use a Microsoft Azure Blob Storage location that is owned and managed by your brand.

.. storage-provision-location-azure-end

**To provision storage on Microsoft Azure**

.. storage-provision-location-azure-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - **Choose a storage location**

       #. Log in to the Microsoft Azure console as a user with credentials that allow provisioning storage, IAM and user roles, and the ability to deploy resources using `Azure Resource Manager <https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview>`__ |ext_link|.

       #. Log in to your Amperity tenant.

          .. note:: If your brand has chosen Amperity-managed storage the following setup workflow steps are skipped.

       #. The **Storage Setup** page appears.

          Each step must be completed before you can start using Amperity.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - **Grant admin consent**

       Your brand must allow Amperity as an enterprise application within your Microsoft Azure account by `granting Amperity admin consent <https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal>`__ |ext_link|.

       .. important:: This step must be done by a Microsoft Azure user account with one of the following administrator roles: "Privileged Role", "Cloud Application", or "Application".

       #. Click **Grant admin consent**. This will redirect you to the Microsoft Azure console.

          .. image:: ../../images/storage-azure-grant-admin-consent.png
             :width: 460 px
             :alt: Grant admin consent to Amperity.
             :align: left
             :class: no-scaled-link

       #. `Approve Amperity <https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps-pane>`__ |ext_link| as an enterprise application.

          .. image:: ../../images/storage-azure-approve-admin-consent.png
             :width: 160 px
             :alt: Grant admin consent to Amperity.
             :align: left
             :class: no-scaled-link

          .. note:: You can grant admin consent from the Microsoft Entra admin center. Navigate to the `Microsoft Entra <https://entra.microsoft.com/>`__ |ext_link| admin center.

             Under **Security** select **Permissions**. On the **Permissions** page click the **Grant admin consent for Amperity** button.

             An **Entra ID** is created for Amperity in your Microsoft Azure account, along with an `application object <https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser#application-object>`__ |ext_link|, after which you are redirected back to Amperity.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - **Provision storage resources**

       Amperity requires the **Object ID** for the Microsoft Azure application to generate a deployment template.

       .. note:: The **Name** of the enterprise application is shown on the **Provision storage resources** page and is a string. For example: ``az-prod-socktown-storage``.

       #. Navigate to the `Microsoft Entra <https://entra.microsoft.com/>`__ |ext_link| admin center and open the list of `enterprise applications <https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/view-applications-portal>`__ |ext_link|.

       #. Click the enterprise application with the matching **Name**, and then copy the **Object ID**.

       #. On the **Provision storage resources** page in Amperity paste the **Object ID** into the empty field, and then click the **Generate deployment template** button.

          .. image:: ../../images/storage-azure-paste-object-id.png
             :width: 460 px
             :alt: Configure the Object ID.
             :align: left
             :class: no-scaled-link

       #. After the Azure Resource Manager (ARM) deployment template is generated click the **Deploy to Azure** button.

          This will open the ARM deployment template in the Microsoft Azure console.

          .. tip:: In the Microsoft Azure console click the **Edit** button to review the ARM deployment template generated by Amperity, including the resources and access levels for objects in the template.

       #. In the Microsoft Azure console, select the regions in which primary and backup storage are located.

          .. note:: Amperity is hosted in one of the following Microsoft Azure regions:

             .. list-table::
                :widths: 50 50
                :header-rows: 0

                * - US West
                  - **west-us-2.azure**
                * - US East
                  - **east-us-2.azure**
                * - North Europe
                  - **north-europe.azure**
                * - West Europe
                  - **west-europe.azure**

             `Cross-region transfer costs <https://azure.microsoft.com/en-us/pricing/details/bandwidth/>`__ |ext_link| will apply when Azure Blob Storage is configured in different region than the one in which your Amperity tenant is hosted and will increase latency.

       #. When you are finished configuring the ARM deployment template click **Revew + Create**. Microsoft Azure will validate the ARM deployment template, and then create resources using the ARM deployment template.

       #. When Microsoft Azure is finished creating resources, return to Amperity and click **Complete step**.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - **Configure storage access**

       The last step is to configure permission for Amperity to access your brand's Microsoft Azure storage resources. This requires a tenant ID and a subscription ID.

       .. image:: ../../images/storage-azure-paste-object-id.png
          :width: 460 px
          :alt: Configure the Object ID.
          :align: left
          :class: no-scaled-link

       #. Navigate to the `Microsoft Entra <https://entra.microsoft.com/>`__ |ext_link| admin center and copy the `tenant ID <https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-microsoft-entra-tenant>`__ |ext_link|.

          Paste the tenant ID into the box above the **Test connection** butto on the **Configure storage access** page.

       #. Click **Add credentials** to register Microsoft Azure storage to your Amperity account. After storage is registered Amperity tests and validates the connection.

       #. When Amperity is finished validating the connection copy the `subscription ID <https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-azure-subscription>`__ |ext_link|.

          Paste the subscription ID into the box below the **Test connection** button on the **Configure storage access** page.

       #. Click **Finish** to bind Microsoft Azure storage to your Amperity account.

.. storage-provision-location-azure-steps-end
