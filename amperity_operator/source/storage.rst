.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure Amperity to use your brand's Amazon S3 bucket.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to use your brand's Amazon S3 bucket.

.. meta::
    :content class=swiftype name=title data-type=string:
        Storage

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

.. warning:: This topic applies only to new Amperity tenants that are provisioned for Amazon S3.


.. _storage-configure-location:

Choose storage location
==================================================

.. storage-configure-location-start

The location in which Amperity stores outputs is configurable. The first step for a new tenant allows your brand to choose one of the following storage locations:

* An Amazon S3 storage location that is owned and managed by your brand
* An Amazon S3 storage location that is only used by your tenant that is provisioned automatically by default

.. storage-configure-location-end

**Configure storage location**

.. storage-configure-location-steps-start

To configure Amperity to use an Amazon S3 storage location that is owned and managed by your brand do the following:

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

          .. important:: When Amperity opens **AWS CloudFormation** during the storage setup process the IAM roles that are used for operations and role assumption within **AWS CloudFormation** will be inherited from the IAM role that is assigned to the logged-in user.

       #. Log in to your tenant.

          .. note:: If your brand has chosen Amperity-managed storage the following setup workflow steps are skipped.

       #. The **Storage Setup** page appears.

          .. image:: ../../images/storage-steps.png
             :width: 380 px
             :alt: The Storage Setup page.
             :align: left
             :class: no-scaled-link

          Each of the four steps must be completed before you can start using Amperity.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - **Specify regions**

       Specify the regions in which your brand wants to configure primary and backup storage, and then click **Continue**.

       Regions for configured storage should be the same regions in which Amperity is located.


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

.. storage-configure-location-steps-end
