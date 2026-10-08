.. /downloads/markdown/


.. |destination-name| replace:: Webhook
.. |what-send| replace:: customer profile attributes
.. |where-send| replace:: an HTTP endpoint


Webhook
==================================================

Send |what-send| to |where-send| as soon as Amperity sees the customer interaction. Amperity sends one HTTP request for each customer.

Use this connector to call your own web service, or any API that accepts HTTP requests.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Credential type**

Choose how Amperity authenticates with your endpoint: an API key, or OAuth 2.0 client credentials. Both credential types require a webhook URL.

**Webhook URL**

Required. The URL of the endpoint that receives each request. The **route-params** field on the journey's **Activate** node can add a path to this URL.

**API key**

Optional, for the API key credential type. When set, Amperity sends it in an "Authorization: Bearer <API key>" header. Leave this empty if your endpoint does not require authentication.

**Token URL**

Required for OAuth. The OAuth 2.0 token endpoint. Amperity requests an access token using the client credentials grant, sends it in an "Authorization: Bearer" header, and requests a new one five minutes before it expires. If the token response has no "expires_in" value, Amperity requests a new token before every request.

**Client ID** and **Client secret**

Required for OAuth. The client ID and secret that Amperity exchanges for an access token.

**Client authentication**

Optional, for OAuth. How the client ID and secret are sent to the token endpoint: "client_secret_basic" sends them in an HTTP Basic header, and "client_secret_post" sends them in the form body. Defaults to "client_secret_basic".

**Scope**

Optional, for OAuth. Space-separated scopes to request, if the token endpoint requires them.

.. note:: Testing the connection sends a POST request with the JSON body {"text": "This is a simple message."} to the webhook URL. Your endpoint must return a success status code for the test to pass.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Business user access**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-business-user-access-allow-start
   :end-before: .. setting-common-business-user-access-allow-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-business-user-access-restrict-pii-start
   :end-before: .. setting-common-business-user-access-restrict-pii-end

**HTTP method**

The HTTP method for each request. May be "POST", "PUT", or "PATCH". Defaults to "POST".

**Content type**

The value of the "Content-Type" header. May be "application/json" or "text/plain". Defaults to "application/json".

**Send record as body**

Disabled by default, so that the customer's attributes are nested under the **payload-field** set on the journey's **Activate** node, for example {"data": {...}}. Enable this option to send the customer's attributes as the whole request body. The **payload-field** is then ignored.

**Custom headers**

Optional. Extra headers sent with every request, as "Name: value" pairs separated by semicolons. For example: "X-Client-ID: CDP_AMPERITY; X-Env: dev". Header values cannot contain semicolons. Custom headers cannot set "Authorization" or "Content-Type"; use the credential and the **Content type** setting instead.

.. important:: Custom headers are not stored as secrets. Do not put API keys, tokens, or other credentials in this setting.

**Request ID header**

Optional. A header name, such as "X-Tracking-ID". When set, each request gets this header with a new UUID. Log it in your endpoint so that Amperity Support can match a failed request to your logs.


Activate node settings
==================================================

The rest of the configuration for this connector belongs to the journey that sends to it. Add this destination to an **Activate** node in the journey, then configure the following fields on that node. Two nodes may send to the same destination with different **payload-field** and **route-params** values.

**payload-field**

The name of the field that the customer's attributes are nested under in the request body. Defaults to "data". Ignored when **Send record as body** is enabled.

**route-params**

Optional. A path appended to the webhook URL for requests from this node. Set a fixed value, or use a profile attribute to send each customer's request to a different path. For example, with a webhook URL of "https://api.example.com/v1" and **route-params** set to "customers/12345", Amperity sends requests to "https://api.example.com/v1/customers/12345". Any query string on the webhook URL is kept.


Request body
==================================================

Each request carries one customer's attributes:

* The attributes mapped to this destination on the journey's **Activate** node, using the names they are mapped to. These may come from the customer's profile or from the event that triggered the journey.
* Any custom attributes configured on the same node. A custom attribute with the same name as a mapped attribute replaces it.
* "amperity_profile_id", the Amperity profile ID of the customer.
* "amperity_collection_id", the ID of the profile collection the customer belongs to.

For example, with the default **payload-field** and **Send record as body** disabled:

::

   {
     "data": {
       "email": "customer@example.com",
       "first_name": "Ada",
       "amperity_profile_id": "...",
       "amperity_collection_id": "..."
     }
   }

Your endpoint must respond within 30 seconds with a success status code. A request that times out or returns an error status code fails, and Amperity does not retry it. With OAuth, the one exception is a 401 response, which Amperity retries once with a new access token.
