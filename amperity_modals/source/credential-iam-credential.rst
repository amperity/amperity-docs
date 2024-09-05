.. 
.. /markdown
.. 

.. |destination-name| replace:: Amazon S3
.. |where-send| replace:: Amazon S3



Amazon S3
==================================================

.. TODO: Repurposed from the "Get details" section in destination for Amazon S3.

IAM credentials require an access key, which is in two parts:

#. An access key ID
#. A secret access key

Both parts are required to authenticate requests to Amazon AWS resources.


Settings
==================================================

**IAM access key**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-iam-access-key-start
      :end-before: .. credential-amazon-s3-iam-access-key-end

**IAM secret key**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-iam-secret-key-start
      :end-before: .. credential-amazon-s3-iam-secret-key-end

**IAM role ARN**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-iam-role-arn-start
      :end-before: .. credential-amazon-s3-iam-role-arn-end

**S3 bucket name**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-amazon-s3-bucket-name-start
      :end-before: .. credential-amazon-s3-bucket-name-end
