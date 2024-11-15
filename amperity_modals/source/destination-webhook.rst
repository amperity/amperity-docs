.. 
.. /markdown
.. 

.. |destination-name| replace:: Webhook



Webhook
==================================================

Use a webhook to build custom integrations with Amperity using Amazon S3 storage and an AWS Lambda function. The AWS Lambda function is a template with which you can write custom code, and then send data to your preferred destination.

The AWS Lambda function generates a file in NDJSON format, publishes to Amazon S3, and then provides a pre-signed URL from which the NDJSON file may be downloaded.

After the NDJSON file is generated, the destination will send a request to an AWS Lambda endpoint that exists outside of the Amperity virtual private cloud (VPC).

Amperity provides an `AWS Serverless Application Repository <https://serverlessrepo.aws.amazon.com/applications>`__ |ext_link| that encapsulates all of the configuration to build your own custom destination.

This template enables two use cases:

#. A serverless application that is deployed directly to your AWS Lambda instance from the AWS Serverless Application Repository. **This is the recommended use case when a serverless application is available for the destination.**
#. A starting point from which you may build a custom Lambda function that is uploaded to your AWS Lambda instance.

More information about setting up and configuring a custom webhook is available from the `Amperity Docs site <https://docs.amperity.com/datagrid/destination_webhook.html>`__ |ext_link|.
