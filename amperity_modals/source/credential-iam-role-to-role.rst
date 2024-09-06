.. 
.. /markdown
.. 

.. |destination-name| replace:: Amazon S3
.. |where-send| replace:: Amazon S3



Amazon S3
==================================================

.. TODO: Repurposed from the "Get details" section in destination for Amazon S3.

For cross-account role assumption you will need the value for the IAM role ARN that allows Amperity to add data to an Amazon S3 bucket that is managed by your brand.

The values for the **Amperity Role ARN** and the **External ID** fields are provided by Amperity.


Settings
==================================================

**Amperity role ARN**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-amperity-role-arn-start
      :end-before: .. credential-amazon-s3-amperity-role-arn-end

**External ID**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-external-id-start
      :end-before: .. credential-amazon-s3-external-id-end

**S3 bucket name**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-bucket-name-start
      :end-before: .. credential-amazon-s3-bucket-name-end

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-trust-policy-start
      :end-before: .. credential-amazon-s3-trust-policy-end

**Target role ARN**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-target-role-arn-start
      :end-before: .. credential-amazon-s3-target-role-arn-end

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-cross-account-roles-steps-settings-provided-start
      :end-before: .. credential-amazon-s3-cross-account-roles-steps-settings-provided-end
