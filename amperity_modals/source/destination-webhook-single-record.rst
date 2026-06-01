.. /downloads/markdown/


.. |destination-name| replace:: Single-record profiles


Single-record profiles
==================================================

The |destination-name| destination sends a single customer profile payload as an HTTP **POST**, **PUT**, or **PATCH** request to any endpoint that can accept it. Use this destination to connect to any system or programmatic workflow that accepts authenticated HTTP requests.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Webhook URL**

The HTTPS endpoint to which the payload is sent. Must be a public HTTPS endpoint. Plain HTTP and private network addresses are rejected during configuration.

**API key** (Optional)

A Bearer token sent in the **Authorization** header. Leave blank for endpoints that do not require authentication. Bearer token is the only supported authorization scheme — HMAC signing, mutual TLS, and custom headers are not supported.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**HTTP method**

The HTTP method used when sending the payload. One of: **POST**, **PUT**, or **PATCH**. Default: **POST**.

**Content type**

The **Content-Type** header sent with the request. One of: **application/json** or **text/plain**. Default: **application/json**.

**Payload field**

The key under which the profile record is wrapped in the request body. Default: **data**. Change this for endpoints that expect a different wrapper key.
