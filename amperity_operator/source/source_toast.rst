.. https://docs.amperity.com/internal/



==================================================
Pull orders data from Toast
==================================================


.. .. include:: ../../shared/terms.rst
..    :start-after: .. term-toast-start
..    :end-before: .. term-toast-end

Toast is a collection of cloud-based restaurant products and tools that integrates restaurant operations with the Toast point-of-sale app and Toast hardware to process orders and payments at restaurant locations.

.. source-toast-about-start

The `Toast Orders API <https://doc.toasttab.com/openapi/orders/overview/>`__ |ext_link| has information on orders, including checks, items ordered, prices, payment methods, discounts, and customer data.

.. source-toast-about-end


.. _source-toast-options:

Configuration options
==================================================

.. source-toast-options-start

Amperity does not integrate directly with the Toast Orders API. Orders data must be collected as an intermediate step, after which it can be sent to Amperity. Options include:

#. Building an AWS Lambda workflow. Use an Amazon AWS Lambda function to access the Toast Orders API and collect order data for the past seven days, serialize order data to Amazon S3 storage as a gzipped JSON file, and then send order data on a weekly schedule to the Amperity Streaming API.

   The option to use an :ref:`example AWS Lambda workflow <source-toast-configure-aws>` requires custom AWS Lambda code that must be validated by your brand. The specific steps your brand requires may be different.

   Access to the Toast Orders API and access to an Amperity streaming endpoint is required. Use this approach when your brand wants direct control over how data is accessed and where that data is stored.

#. Using :doc:`Fivetran <source_fivetran>` to access to the Toast Orders API, and then configure Amperity to pull orders data from Toast using Fivetran. Use this option when Fivetran can be given permission to access your brand's Toast account.

.. source-toast-options-end


.. _source-toast-configure-aws:

Configure Amazon AWS
==================================================

.. source-toast-configure-aws-start

Configure Amazon AWS for a AWS Lambda function, Amazon S3 storage, and logging.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-00.png
          :width: 60 px
          :alt: Step zero.
          :align: center
          :class: no-scaled-link
     - **Prerequisites**

       To access the Toast Orders API you will need the following:

       #. A client ID and client secret.
       #. A restaurant GUID.
       #. API permissions to access Orders endpoint.

       To configure your Amazon AWS account you will need permission to:

       #. Create and manage AWS Lambda functions.
       #. Create and manage Amazon S3 buckets.
       #. Create and manage IAM roles.
       #. Create and manage EventBridge rules.

       To access the Amperity Streaming API:

       #. An API key for the Streaming API.
       #. The tenant ID.


   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Create an Amazon S3 bucket**

       #. Log in to the `AWS S3 Console <https://s3.console.aws.amazon.com/>`__ |ext_link|.
       #. Click **Create bucket** and name the bucket. For example: "toast-orders-bucket".
       #. Set the region, configure any other necessary settings, and then create the bucket


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Create an IAM role for AWS Lambda**

       #. Log in to the `AWS IAM Console <https://console.aws.amazon.com/iam/>`__ |ext_link|.
       #. Click **Roles**, and then **Create role**.
       #. Choose **AWS service**, and then choose **Lambda**.
       #. Attach the following policies:

          **AWSLambdaBasicExecutionRole** for CloudWatch logs.

          A custom policy with S3 permissions:

          .. code-block:: json

             {
               "Version": "2012-10-17",
               "Statement": [
                 {
                   "Effect": "Allow",
                   "Action": [
                     "s3:PutObject",
                     "s3:PutObjectAcl",
                     "s3:GetObject"
                   ],
                   "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
                 },
                 {
                   "Effect": "Allow",
                   "Action": [
                     "s3:ListBucket"
                   ],
                   "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME"
                 }
               ]
             }

       #. Name the role. For example: "toast-orders-lambda-role".


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **Create an AWS Lambda function**

       #. Log in to the `AWS Lambda Console <https://console.aws.amazon.com/lambda/>`__ |ext_link|
       #. Click **Create function**, and then select **Author from scratch**.
       #. Configure the following:

          **Function name**: "toast-orders-processor"

          **Runtime**: Python 3.11 or Python 3.12

          **Execution role**: Use the custom role created in step 2.

       #. Click **Create function**.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - **Deploy the code for the AWS Lambda function**

       #. In the AWS Lambda function console, go to the **Code** tab.
       #. Delete the default ``lambda_function.py`` code.
       #. Copy the entire contents of :ref:`toast-orders.py <source-toast-example>` into the code editor.
       #. Update the environment variables within the code and validate the function works.
       #. Click **Deploy**.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - **Install dependencies**

       The function uses external libraries. Add an AWS Lambda layer or package the dependencies.

       **AWS Lambda Layer**

       #. Create a deployment package with dependencies:

          .. code-block:: bash

             mkdir python
             pip install requests -t python/
             zip -r requests-layer.zip python/

       #. Create a layer with the zip file.
       #. Add the layer to your function.

       **Deployment Package**

       #. Create a local directory and install dependencies:

          .. code-block:: bash

             mkdir toast-orders-package
             cd toast-orders-package
             pip install requests -t .

       #. Copy the :ref:`toast-orders.py <source-toast-example>` file as "lambda_function.py" and then zip the package.

          .. code-block:: bash

             zip -r ../toast-orders-deployment.zip .

       #. Upload the zip file to the AWS Lambda function.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - **Configure environment variables**

       #. In the Lambda function console, go to the **Configuration** tab.
       #. Click **Environment variables**, then **Edit**, and then add the following environment variables:

          .. list-table::
             :widths: 40 60
             :header-rows: 0

             * - **TOAST_API_URL**
               - ``https://ws-api.toasttab.com/orders/v2/orders``

             * - **TOAST_CLIENT_ID**
               - ``your-toast-client-id``

             * - **TOAST_CLIENT_SECRET**
               - ``your-toast-client-secret``

             * - **TOAST_RESTAURANT_GUID**
               - ``12345678-1234-1234-1234-123456789012``

             * - **S3_BUCKET_NAME**
               - ``toast-orders-bucket``

             * - **S3_PREFIX**
               - ``toast-orders/``

             * - **AMPERITY_API_URL**
               - ``https://socktown.amperity.com/api/v1/streaming``

             * - **AMPERITY_API_KEY**
               - ``your-amperity-api-key``

       #. Click **Save**.


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step seven.
          :align: center
          :class: no-scaled-link
     - **Configure function settings**

       #. In the Lambda function console, go to the **Configuration** tab.
       #. Click **General configuration**, then **Edit**, and then set the following:

          **Timeout**: 5 minutes, or 300 seconds.

          **Memory**: 512 MB. Adjust this value based on your Toast orders data volume.

       #. Click **Save**.


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step eight.
          :align: center
          :class: no-scaled-link
     - **Create schedule**

       #. Go to the `Amazon EventBridge Console <https://console.aws.amazon.com/events/>`__ |ext_link|.
       #. Click **Rules**, then **Create rule**, and then set the following:

          **Name**: "toast-orders-weekly-trigger"

          **Description**: "Triggers Toast orders processing every Monday at 4:00 AM UTC"

          **Rule type**: Schedule

          **Schedule pattern**: Cron expression

          **Cron expression**: ``0 4 ? * MON *``, which is "every Monday at 4:00 AM UTC".

       #. Click **Next**, and then select the target:

          **Target type**: AWS service

          **Select a target**: Lambda function

          **Function**: Select the "toast-orders-processor" function

       #. Click **Next**, then **Next**, and then **Create rule**.


   * - .. image:: ../../images/steps-09.png
          :width: 60 px
          :alt: Step nine.
          :align: center
          :class: no-scaled-link
     - **Validate the function**

       #. Open the AWS Lambda console, and then click **Test**.
       #. Create a new test event using the default template.
       #. Click **Test** to run the function.
       #. Check the execution results and review the Amazon CloudWatch logs.

.. source-toast-configure-aws-end

.. _source-toast-example:

Example Lambda function: toast-orders.py
==================================================

.. source-toast-example-start

The following example is a Lambda function that:

#. Authenticates to the Toast API and uses the correct headers.
#. Automatically calculates the previous week's date range.
#. Fetches orders data, using pagination for large results.
#. Serializes orders data into JSON, and then compresses the results using gzip.
#. Includes metadata, such as export timestamps, data ranges, and order counts.
#. Applies error handling and retry logic.

.. source-toast-example-end

**Example Lambda function**

.. source-toast-example-python-start

.. code-block:: python

   import json
   import boto3
   import gzip
   import os
   import requests
   from datetime import datetime, timedelta
   from typing import Dict, Any, Optional
   import logging

   # Configure logging
   logger = logging.getLogger()
   logger.setLevel(logging.INFO)

   class ToastOrdersProcessor:
     def __init__(self):
       # Toast API configuration - Set these as environment variables
       self.toast_api_url = os.environ.get('TOAST_API_URL')  # e.g., "https://ws-api.toasttab.com/orders/v2/orders"
       self.toast_client_id = os.environ.get('TOAST_CLIENT_ID')  # Your Toast client ID
       self.toast_client_secret = os.environ.get('TOAST_CLIENT_SECRET')  # Your Toast client secret
       self.toast_restaurant_guid = os.environ.get('TOAST_RESTAURANT_GUID')  # Your restaurant GUID

       # AWS S3 configuration - Set these as environment variables
       self.s3_bucket = os.environ.get('S3_BUCKET_NAME')  # e.g., "my-toast-orders-bucket"
       self.s3_prefix = os.environ.get('S3_PREFIX', 'toast-orders/')  # Optional prefix for S3 objects

       # Amperity configuration - Set these as environment variables
       self.amperity_api_url = os.environ.get('AMPERITY_API_URL')  # e.g., "https://socktown.amperity.com/api/v1/streaming"
       self.amperity_api_key = os.environ.get('AMPERITY_API_KEY')  # Your Amperity API key
       self.amperity_tenant_id = "socktown"  # Fixed tenant ID as specified

       # Initialize AWS clients
       self.s3_client = boto3.client('s3')

   def get_toast_access_token(self) -> Optional[str]:
     """
     Authenticate with Toast API using client credentials flow.
     Returns access token or None if authentication fails.
     """
     try:
       auth_url = "https://ws-api.toasttab.com/authentication/v1/authentication/login"

       payload = {
         "clientId": self.toast_client_id,
         "clientSecret": self.toast_client_secret,
         "userAccessType": "TOAST_MACHINE_CLIENT"
       }

       headers = {
         "Content-Type": "application/json",
         "Toast-Restaurant-External-ID": self.toast_restaurant_guid
       }

       response = requests.post(auth_url, json=payload, headers=headers, timeout=30)
       response.raise_for_status()

       auth_data = response.json()
       return auth_data.get('sessionToken')

     except Exception as e:
       logger.error(f"Failed to authenticate with Toast API: {str(e)}")
       return None

   def fetch_toast_orders(self, access_token: str) -> Optional[Dict[str, Any]]:
     """
     Fetch orders from Toast API for the past week.
     Returns orders data or None if fetch fails.
     """
     try:
       # Calculate date range for the past week
       end_date = datetime.utcnow()
       start_date = end_date - timedelta(days=7)

       # Format dates for Toast API (ISO 8601 format)
       start_date_str = start_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
       end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

       headers = {
         "Authorization": f"Bearer {access_token}",
         "Content-Type": "application/json",
         "Toast-Restaurant-External-ID": self.toast_restaurant_guid
       }

       # Toast API parameters for fetching orders
       params = {
         "startDate": start_date_str,
         "endDate": end_date_str,
         "pageSize": 100  # Adjust based on your needs, max is typically 100
       }

       all_orders = []
       page_token = None

       # Handle pagination
       while True:
         if page_token:
           params["pageToken"] = page_token

           response = requests.get(
             self.toast_api_url,
             headers=headers,
             params=params,
             timeout=60
           )
           response.raise_for_status()

           data = response.json()
           orders = data.get('orders', [])
           all_orders.extend(orders)

           # Check for next page
           page_token = data.get('nextPageToken')
           if not page_token:
             break

           logger.info(f"Fetched {len(orders)} orders, continuing to next page...")

         logger.info(f"Successfully fetched {len(all_orders)} total orders from Toast API")

         return {
           "orders": all_orders,
           "metadata": {
             "fetch_date": end_date.isoformat(),
             "start_date": start_date_str,
             "end_date": end_date_str,
             "total_orders": len(all_orders)
           }
         }

     except Exception as e:
       logger.error(f"Failed to fetch orders from Toast API: {str(e)}")
       return None

   def upload_to_s3(self, data: Dict[str, Any]) -> Optional[str]:
     """
     Upload gzipped JSON data to S3 bucket.
     Returns S3 key if successful, None otherwise.
     """
     try:
       # Generate filename with datestamp
       timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
       filename = f"toast-orders_{timestamp}.json.gz"
       s3_key = f"{self.s3_prefix}{filename}"

       # Convert data to JSON and compress with gzip
       json_data = json.dumps(data, indent=2)
       compressed_data = gzip.compress(json_data.encode('utf-8'))

       # Upload to S3
       self.s3_client.put_object(
         Bucket=self.s3_bucket,
         Key=s3_key,
         Body=compressed_data,
         ContentType='application/json',
         ContentEncoding='gzip',
         Metadata={
           'source': 'toast-orders-lambda',
           'timestamp': timestamp,
           'total_orders': str(data.get('metadata', {}).get('total_orders', 0))
         }
       )

       logger.info(f"Successfully uploaded {filename} to S3 bucket {self.s3_bucket}")
       return s3_key

     except Exception as e:
       logger.error(f"Failed to upload to S3: {str(e)}")
       return None

   def send_to_amperity(self, s3_key: str, data: Dict[str, Any]) -> Dict[str, Any]:
     """
     Send data to Amperity Streaming API.
     Returns response with status code and message.
     """
     try:
       headers = {
         "Authorization": f"Bearer {self.amperity_api_key}",
         "Content-Type": "application/json",
         "Amperity-Tenant": self.amperity_tenant_id
       }

       # Prepare payload for Amperity
       # Note: Adjust this payload structure based on Amperity's exact requirements
       amperity_payload = {
         "source": "toast-orders",
         "data_type": "orders",
         "s3_location": f"s3://{self.s3_bucket}/{s3_key}",
         "metadata": {
           "total_records": data.get('metadata', {}).get('total_orders', 0),
           "fetch_date": data.get('metadata', {}).get('fetch_date'),
           "start_date": data.get('metadata', {}).get('start_date'),
           "end_date": data.get('metadata', {}).get('end_date')
         },
         "tenant_id": self.amperity_tenant_id
       }

       response = requests.post(
         self.amperity_api_url,
         headers=headers,
         json=amperity_payload,
         timeout=60
       )

       if response.status_code == 200:
         logger.info("Successfully sent data to Amperity")
         return {
           "statusCode": 200,
           "message": "Data successfully sent to Amperity",
           "amperity_response": response.json() if response.text else {}
         }
         elif response.status_code == 400:
           logger.error(f"Amperity validation error: {response.text}")
           return {
             "statusCode": 400,
             "message": f"Amperity validation failed: {response.text}",
             "error_details": response.text
           }
         else:
           logger.error(f"Amperity API error: {response.status_code} - {response.text}")
           return {
             "statusCode": 500,
             "message": f"Amperity API error: HTTP {response.status_code}",
             "error_details": response.text
           }

       except requests.exceptions.Timeout:
         logger.error("Timeout while sending data to Amperity")
         return {
           "statusCode": 500,
           "message": "Timeout while sending data to Amperity"
         }
       except requests.exceptions.RequestException as e:
         logger.error(f"Network error while sending to Amperity: {str(e)}")
         return {
           "statusCode": 500,
           "message": f"Network error: {str(e)}"
         }
       except Exception as e:
         logger.error(f"Unexpected error while sending to Amperity: {str(e)}")
         return {
           "statusCode": 500,
           "message": f"Unexpected error: {str(e)}"
         }

   def lambda_handler(event, context):
     """
     Main Lambda function handler.
     This function will be triggered weekly on Monday at 4:00 AM UTC.
     """
     processor = ToastOrdersProcessor()

     try:
       # Validate required environment variables
       required_vars = [
         'TOAST_API_URL', 'TOAST_CLIENT_ID', 'TOAST_CLIENT_SECRET', 
         'TOAST_RESTAURANT_GUID', 'S3_BUCKET_NAME', 'AMPERITY_API_URL', 
         'AMPERITY_API_KEY'
       ]

       missing_vars = [var for var in required_vars if not os.environ.get(var)]
       if missing_vars:
         error_msg = f"Missing required environment variables: {', '.join(missing_vars)}"
         logger.error(error_msg)
         return {
           "statusCode": 500,
           "body": json.dumps({
             "error": error_msg,
             "missing_variables": missing_vars
           })
         }

       # Step 1: Authenticate with Toast API
       logger.info("Starting Toast Orders processing...")
       access_token = processor.get_toast_access_token()

       if not access_token:
         return {
           "statusCode": 500,
           "body": json.dumps({
             "error": "Failed to authenticate with Toast API"
           })
         }

       # Step 2: Fetch orders from Toast API
       orders_data = processor.fetch_toast_orders(access_token)

       if not orders_data:
         return {
           "statusCode": 500,
           "body": json.dumps({
             "error": "Failed to fetch orders from Toast API"
           })
         }

       # Step 3: Upload to S3
       s3_key = processor.upload_to_s3(orders_data)

       if not s3_key:
         return {
           "statusCode": 500,
           "body": json.dumps({
             "error": "Failed to upload data to S3"
           })
         }

       # Step 4: Send to Amperity
       amperity_result = processor.send_to_amperity(s3_key, orders_data)

       # Return final result
       return {
         "statusCode": amperity_result["statusCode"],
         "body": json.dumps({
           "message": "Toast Orders processing completed",
           "s3_location": f"s3://{processor.s3_bucket}/{s3_key}",
           "total_orders": orders_data.get('metadata', {}).get('total_orders', 0),
           "amperity_status": amperity_result["message"],
           "timestamp": datetime.utcnow().isoformat()
         })
       }

   except Exception as e:
     logger.error(f"Unexpected error in lambda_handler: {str(e)}")
     return {
       "statusCode": 500,
       "body": json.dumps({
         "error": f"Unexpected error: {str(e)}",
         "timestamp": datetime.utcnow().isoformat()
       })
     }

.. source-toast-example-python-end


.. _source-toast-example-json:

Example JSON payload
==================================================

.. source-toast-example-json-start

.. code-block:: json

   {
     "orders": [
       {
         "guid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
         "entityType": "Order",
         "externalId": null,
         "orderNumber": "12345",
         "openedDate": "2025-09-19T14:30:00.000Z",
         "closedDate": "2025-09-19T14:45:00.000Z",
         "modifiedDate": "2025-09-19T14:45:00.000Z",
         "businessDate": 20250919,
         "promisedDate": "2025-09-19T14:45:00.000Z",
         "channelGuid": "b2c3d4e5-f6g7-8901-bcde-f23456789012",
         "source": "ONLINE",
         "duration": 900,
         "dining": {
           "guid": "c3d4e5f6-g7h8-9012-cdef-345678901234",
           "entityType": "DiningOption",
           "behavior": "DELIVERY",
           "curbsidePickupInfo": null
         },
         "restaurant": {
           "guid": "d4e5f6g7-h8i9-0123-def4-56789012345a",
           "entityType": "Restaurant",
           "locationName": "Main Street Location",
           "locationId": "MAIN_001"
         },
         "revenueCenter": {
           "guid": "e5f6g7h8-i9j0-1234-efg5-6789012345ab",
           "entityType": "RevenueCenter",
           "name": "Online Orders"
         },
         "server": {
           "guid": "f6g7h8i9-j0k1-2345-fgh6-789012345abc",
           "entityType": "Employee",
           "firstName": "System",
           "lastName": "Online",
           "email": "system@restaurant.com"
         },
         "checks": [
           {
             "guid": "g7h8i9j0-k1l2-3456-ghi7-89012345abcd",
             "entityType": "Check",
             "displayNumber": "1",
             "selections": [
               {
                 "guid": "h8i9j0k1-l2m3-4567-hij8-9012345abcde",
                 "entityType": "Selection",
                 "item": {
                   "guid": "i9j0k1l2-m3n4-5678-ijk9-012345abcdef",
                   "entityType": "MenuItem",
                   "name": "Margherita Pizza",
                   "plu": "PIZZA001"
                 },
                 "itemGroup": {
                   "guid": "j0k1l2m3-n4o5-6789-jkl0-12345abcdef0",
                   "entityType": "MenuGroup",
                   "name": "Pizzas"
                 },
                 "quantity": 1,
                 "unitOfMeasure": "NONE",
                 "selectionType": "NONE",
                 "deferred": false,
                 "preDiscountPrice": 1599,
                 "price": 1599,
                 "tax": 144,
                 "voided": false,
                 "voidDate": null,
                 "voidBusinessDate": null,
                 "modifiers": [
                   {
                     "guid": "k1l2m3n4-o5p6-789a-klm1-2345abcdef01",
                     "entityType": "Selection",
                     "item": {
                       "guid": "l2m3n4o5-p6q7-89ab-lmn2-345abcdef012",
                       "entityType": "MenuItem",
                       "name": "Extra Cheese",
                       "plu": "MOD001"
                     },
                     "quantity": 1,
                     "unitOfMeasure": "NONE",
                     "selectionType": "NONE",
                     "preDiscountPrice": 200,
                     "price": 200,
                     "tax": 18
                   }
                 ]
               },
               {
                 "guid": "m3n4o5p6-q7r8-9abc-mno3-45abcdef0123",
                 "entityType": "Selection",
                 "item": {
                   "guid": "n4o5p6q7-r8s9-abcd-nop4-5abcdef01234",
                   "entityType": "MenuItem",
                   "name": "Caesar Salad",
                   "plu": "SALAD001"
                 },
                 "itemGroup": {
                   "guid": "o5p6q7r8-s9t0-bcde-opq5-abcdef012345",
                   "entityType": "MenuGroup",
                   "name": "Salads"
                 },
                 "quantity": 1,
                 "unitOfMeasure": "NONE",
                 "selectionType": "NONE",
                 "deferred": false,
                 "preDiscountPrice": 899,
                 "price": 899,
                 "tax": 81,
                 "voided": false,
                 "voidDate": null,
                 "voidBusinessDate": null,
                 "modifiers": []
               }
             ],
             "customer": {
               "guid": "p6q7r8s9-t0u1-cdef-pqr6-bcdef0123456",
               "entityType": "Customer",
               "firstName": "John",
               "lastName": "Smith",
               "email": "john.smith@email.com",
               "phone": "+1-555-123-4567"
             },
             "payments": [
               {
                 "guid": "q7r8s9t0-u1v2-def0-qrs7-cdef01234567",
                 "entityType": "Payment",
                 "paidDate": "2025-09-19T14:42:00.000Z",
                 "paidBusinessDate": 20250919,
                 "type": "CREDIT",
                 "amount": 2961,
                 "tipAmount": 300,
                 "amountTendered": 2961,
                 "cardEntryMode": "KEYED",
                 "last4Digits": "1234",
                 "cardType": "VISA"
               }
             ],
             "appliedDiscounts": [],
             "taxAmount": 243,
             "totalAmount": 2961,
             "paymentStatus": "PAID"
           }
         ],
         "appliedDiscounts": [],
         "discountAmount": 0,
         "netAmount": 2698,
         "taxAmount": 243,
         "totalAmount": 2961,
         "paidDate": "2025-09-19T14:42:00.000Z",
         "closed": true,
         "voidDate": null,
         "voidBusinessDate": null,
         "voided": false,
         "approvalStatus": "APPROVED",
         "deliveryInfo": {
           "address": {
             "address1": "123 Main Street",
             "address2": "Apt 4B",
             "city": "Anytown",
             "state": "CA",
             "zipCode": "12345",
             "country": "US",
             "latitude": 37.7749,
             "longitude": -122.4194
           },
           "deliveryDate": "2025-09-19T15:15:00.000Z",
           "deliveryCharge": 0,
           "deliveryInstructions": "Ring doorbell twice"
         }
       },
       {
         "guid": "r8s9t0u1-v2w3-ef01-rst8-def012345678",
         "entityType": "Order",
         "externalId": null,
         "orderNumber": "12346",
         "openedDate": "2025-09-19T16:15:00.000Z",
         "closedDate": "2025-09-19T16:30:00.000Z",
         "modifiedDate": "2025-09-19T16:30:00.000Z",
         "businessDate": 20250919,
         "promisedDate": "2025-09-19T16:45:00.000Z",
         "channelGuid": "s9t0u1v2-w3x4-f012-stu9-ef0123456789",
         "source": "POS",
         "duration": 900,
         "dining": {
           "guid": "t0u1v2w3-x4y5-0123-tuv0-f012345678ab",
           "entityType": "DiningOption",
           "behavior": "DINE_IN",
           "curbsidePickupInfo": null
         },
         "restaurant": {
           "guid": "d4e5f6g7-h8i9-0123-def4-56789012345a",
           "entityType": "Restaurant",
           "locationName": "Main Street Location",
           "locationId": "MAIN_001"
         },
         "revenueCenter": {
           "guid": "u1v2w3x4-y5z6-1234-uvw1-012345678abc",
           "entityType": "RevenueCenter",
           "name": "Dine In"
         },
         "server": {
           "guid": "v2w3x4y5-z6a7-2345-vwx2-12345678abcd",
           "entityType": "Employee",
           "firstName": "Jane",
           "lastName": "Doe",
           "email": "jane.doe@restaurant.com"
         },
         "table": {
           "guid": "w3x4y5z6-a7b8-3456-wxy3-2345678abcde",
           "entityType": "Table",
           "name": "Table 12"
         },
         "checks": [
           {
             "guid": "x4y5z6a7-b8c9-4567-xyz4-345678abcdef",
             "entityType": "Check",
             "displayNumber": "1",
             "selections": [
               {
                 "guid": "y5z6a7b8-c9d0-5678-yza5-45678abcdef0",
                 "entityType": "Selection",
                 "item": {
                   "guid": "z6a7b8c9-d0e1-6789-zab6-5678abcdef01",
                   "entityType": "MenuItem",
                   "name": "Grilled Chicken Sandwich",
                   "plu": "SAND001"
                 },
                 "itemGroup": {
                   "guid": "a7b8c9d0-e1f2-789a-abc7-678abcdef012",
                   "entityType": "MenuGroup",
                   "name": "Sandwiches"
                 },
                 "quantity": 1,
                 "unitOfMeasure": "NONE",
                 "selectionType": "NONE",
                 "deferred": false,
                 "preDiscountPrice": 1299,
                 "price": 1299,
                 "tax": 117,
                 "voided": false,
                 "voidDate": null,
                 "voidBusinessDate": null,
                 "modifiers": []
               }
             ],
             "customer": null,
             "payments": [
               {
                 "guid": "b8c9d0e1-f2g3-89ab-bcd8-78abcdef0123",
                 "entityType": "Payment",
                 "paidDate": "2025-09-19T16:28:00.000Z",
                 "paidBusinessDate": 20250919,
                 "type": "CASH",
                 "amount": 1500,
                 "tipAmount": 84,
                 "amountTendered": 1500,
                 "cardEntryMode": null,
                 "last4Digits": null,
                 "cardType": null
               }
             ],
             "appliedDiscounts": [],
             "taxAmount": 117,
             "totalAmount": 1416,
             "paymentStatus": "PAID"
           }
         ],
         "appliedDiscounts": [],
         "discountAmount": 0,
         "netAmount": 1299,
         "taxAmount": 117,
         "totalAmount": 1416,
         "paidDate": "2025-09-19T16:28:00.000Z",
         "closed": true,
         "voidDate": null,
         "voidBusinessDate": null,
         "voided": false,
         "approvalStatus": "APPROVED",
         "deliveryInfo": null
       }
     ],
     "metadata": {
       "fetch_date": "2025-09-26T04:00:00.000Z",
       "start_date": "2025-09-19T04:00:00.000Z",
       "end_date": "2025-09-26T04:00:00.000Z",
       "total_orders": 2
     }
   }

.. source-toast-example-json-end
