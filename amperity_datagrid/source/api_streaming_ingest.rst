.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        This topic describes how the Streaming Ingest API works.

.. meta::
    :content class=swiftype name=body data-type=text:
        This topic describes how the Streaming Ingest API works.

.. meta::
    :content class=swiftype name=title data-type=string:
        Streaming Ingest API

==================================================
Streaming Ingest API
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-streaming-ingest-api-start
   :end-before: .. term-streaming-ingest-api-end


.. _streaming-ingest-rest-api-overview:

Overview
==================================================

.. streaming-ingest-rest-api-overview-start

The Streaming Ingest API is designed for streaming events and profile updates. It is a low latency, high throughput REST API, designed to accept billions of records per day.

The Streaming Ingest API is configured to use different streams to load data into individual feeds. For example, order events might be sent to one stream while profile updates are sent to another. Individual streams have a distinguished endpoint ``/stream/v0/data/<stream-id>``.

The Streaming Ingest API supports the following payload types:

#. JSON (preferred), which converts streaming data to NDJSON
#. XML, which converts streaming data to CBOR

A stream may only be one payload type.

.. streaming-ingest-rest-api-overview-end


.. _streaming-ingest-rest-api-keys-and-jwt:

API Keys and JWTs
==================================================

.. streaming-ingest-rest-api-keys-and-jwt-start

Amperity uses a |ext_jwt| for authentication to the Streaming Ingest API. A single access token may be used to access any endpoint in your tenant's Streaming Ingest API.

The access token is self-generated from the Amperity user interface and authorizes write access to the Streaming Ingest API for your tenant. A self-generated access token ensures that only your team has access to the token and supports organizational security policies like periodic access token rotation.

The access token must be available to each request made to the Streaming Ingest API.

.. note:: More information about Amperity |api_keys| is available, including sections about |api_keys_add|, |api_keys_delete|, |api_keys_rotate|, |api_keys_access_generate|, and |api_keys_access_refresh|.

.. streaming-ingest-rest-api-keys-and-jwt-end


.. _streaming-ingest-api-enable-add-api-key:

Add API key
--------------------------------------------------

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-api-token-add-streaming-ingest-start
   :end-before: .. api-keys-api-token-add-streaming-ingest-end


.. _streaming-ingest-api-enable-generate-access-token:

Generate an access token
--------------------------------------------------

.. api-keys-access-tokens-generate-start

Access tokens that enable authentication to the Amperity API are managed directly from the **Users & Activity** page in Amperity.

**To generate access tokens**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Users & Activity** page.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Under **API keys** find the API key for which you want to generate an access token, and then from the **Actions** menu select "Generate access token".

       .. image:: ../../images/api-keys-generate-access-token-streaming.png
          :width: 500 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Select the number of days this token will allow access to the API, after which it will expire. For example, 3 days:

       .. image:: ../../images/api-keys-set-token-expiration.png
          :width: 240 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link

       The token is generated, and then automatically copied to your clipboard.

       .. image:: ../../images/api-keys-token-saved-to-clipboard.png
          :width: 240 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link

       .. important:: You are the only person who will have access to the newly-generated access key. Amperity does not save the access key anywhere and it will disappear when you close this dialog. Store the access key in a safe place.

.. api-keys-access-tokens-generate-end


.. _streaming-ingest-endpoints:

Configure endpoints
==================================================

.. streaming-ingest-endpoints-start

You can self-manage the endpoints your brand uses to stream data to Amperity.

**To manage Streaming Ingest API endpoints**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Sources** page.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Under **Streaming Ingest** click **Add stream**.

       .. image:: ../../images/api-streaming-ingest-add-stream.png
          :width: 500 px
          :alt: Add a Streaming Ingest API endpoint.
          :align: left
          :class: no-scaled-link

       Enter a name and description for the Streaming Ingest API endpoint.

       .. image:: ../../images/api-streaming-ingest-add-stream-name-desc.png
          :width: 420 px
          :alt: Add a name and description for the Streaming Ingest API endpoint.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - The ID for the Streaming Ingest API endpoint is available from the **Stream ID** column:

       .. image:: ../../images/api-streaming-ingest-stream-ids.png
          :width: 500 px
          :alt: Get the ID for the Streaming Ingest API endpoint.
          :align: left
          :class: no-scaled-link

       :ref:`Use this identifier in the path for the POST request <streaming-ingest-rest-api-streams>` when sending data to the Streaming Ingest API endpoint.

       For example:

       .. code-block:: none

          POST /stream/v0/data/is-AbCDefGH HTTP/1.1

.. streaming-ingest-endpoints-end


.. _streaming-ingest-rest-api-streams:

Send to data streams
==================================================

.. streaming-ingest-rest-api-streams-start

A data stream is generated for you by Amperity on request. Contact your support representative via the `Amperity Support Portal <../support/index.html>`__ (or send email to support@amperity.com) to request a new data stream.

Data can be sent to the Streaming Ingest API by issuing POST requests to the ``/stream/v0/data/<stream-id>`` endpoint.

.. streaming-ingest-rest-api-stream-schema-important-start

.. important:: Amperity does not enforce any particular data schema. Each data schema is a unique stream that depends on what is being sent. You cannot have multiple data schemas on a single stream, instead use multiple streams to support multiple schemas.

.. streaming-ingest-rest-api-stream-schema-important-end

.. streaming-ingest-rest-api-configure-streams-postman-start

.. admonition:: About Postman

   .. include:: ../../shared/terms.rst
      :start-after: .. term-postman-start
      :end-before: .. term-postman-end

   Amperity will provide complete details for using a |ext_download_postman_api_streaming| when your tenant is initialized. Use this template as the starting point for building out the API stream for your data source.

.. streaming-ingest-rest-api-configure-streams-postman-end


.. _streaming-ingest-rest-api-send-json-using-http:

Send JSON using HTTP
--------------------------------------------------

.. streaming-ingest-rest-api-send-json-using-http-start

To send JSON data to a stream using HTTP, submit a request similar to:

.. code-block:: none

   POST /stream/v0/data/<stream-id> HTTP/1.1
   Host: https://<tenant-name>.amperity.com
   Content-Type: application/json
   X-Amperity-Tenant: <tenant-name>
   Authorization: Bearer <Streaming Ingest JWT token>
   Content-Length: 32164

   {"field1": "value1",
    "field2": "value2"}

.. streaming-ingest-rest-api-send-json-using-http-end


.. _streaming-ingest-rest-api-send-json-using-curl:

Send JSON using cURL
--------------------------------------------------

.. streaming-ingest-rest-api-send-json-using-curl-start

To send JSON data to a stream using cURL, submit a request similar to:

.. code-block:: none

   curl -XPOST \
   -H "Content-Type: application/json" \
   -H "X-Amperity-Tenant: <tenant-name>" \
   -H "Authorization: Bearer <Streaming Ingest JWT token>" \
   https://<tenant-name>.amperity.com/stream/v0/data/<stream-id> \
   --data-binary \
   ' {"field1": "value1",
      "field2": "value2"}'

.. streaming-ingest-rest-api-send-json-using-curl-end


.. _streaming-ingest-rest-api-send-xml-using-http:

Send XML using HTTP
--------------------------------------------------

.. streaming-ingest-rest-api-send-xml-using-http-start

To send XML data to a stream using HTTP, submit a request similar to:

.. code-block:: none

   POST /stream/v0/data/<stream-id> HTTP/1.1
   Host: https://<tenant-name>.amperity.com
   Content-Type: application/xml
   X-Amperity-Tenant: <tenant-name>
   Authorization: Bearer <Streaming Ingest JWT token>
   Content-Length: 32164

    <records>
    <record>
    <field1>value1</field1>
    ...
    </record>
    <record>
    <field1>value2</field1>
    ... t
    </record>
    </records>

.. streaming-ingest-rest-api-send-xml-using-http-end


.. _streaming-ingest-rest-api-send-xml-using-curl:

Send XML using cURL
--------------------------------------------------

.. streaming-ingest-rest-api-send-xml-using-curl-start

To send XML data to a stream using cURL, submit a request similar to:

.. code-block:: none

   curl -XPOST \
   -H "Content-Type: application/xml" \
   -H "X-Amperity-Tenant: <tenant-name>" \
   -H "Authorization: Bearer <Streaming Ingest JWT token>" \
   https://<tenant-name>.amperity.com/stream/v0/data/<stream-id> \
   --data-binary \
   '<records>
    <record>
    <field1>value1</field1>
    </record>
    <record>
    <field1>value2</field1>
    </record>
    </records>
   '

.. streaming-ingest-rest-api-send-xml-using-curl-end


.. _streaming-ingest-rest-api-http-status-codes:

HTTP response status codes
==================================================

.. streaming-ingest-rest-api-http-status-codes-start

The Streaming Ingest API has the following HTTP status codes:

.. list-table::
   :widths: 180 380 50
   :header-rows: 1

   * - HTTP code
     - Description
     - Retry?
   * - **202**
     - Accepted.
     - N/A
   * - **400**
     - Request malformed.

       .. note:: XML payloads are not checked synchronously; a 202 response does not guarantee that XML payloads will be parsable downstream.
     - No
   * - **401**
     - Unauthorized. JWT could not be verified or is expired.
     - No
   * - **413**
     - Request is too large.

       .. note:: Amperity limits the maximum payload size to 254 kb.
     - No
   * - **429**
     - Request throttled.

       .. note:: The request limit is set above the expected traffic volume.
     - Yes
   * - **500**
     - Internal error.
     - Yes
   * - **503**
     - Service unavailable.
     - Yes
   * - **504**
     - Gateway timeout.

       .. note:: All retries have exponential back off.
     - Yes

.. streaming-ingest-rest-api-http-status-codes-end


.. _streaming-ingest-rest-api-stream-define:

Load stream data
==================================================

.. streaming-ingest-rest-api-stream-define-start

Once data is sent to a stream, it is batched and collected to be made ready for ingest. Similar to loading files-based data, streamed data is loaded into feeds through couriers and is done from the **Sources** page. 

.. streaming-ingest-rest-api-stream-define-end

.. streaming-ingest-rest-api-load-json-note-start

.. note::

   * The Streaming Ingest API only accepts individual JSON payloads (and does not accept NDJSON payloads)
   * JSON payloads are combined into a single NDJSON file
   * Nested JSON payloads require a saved query to flatten the data
   * XML payloads are converted into CBOR by the streaming API
   * CBOR requires a saved query to transform the data into a tabular format

.. streaming-ingest-rest-api-load-json-note-end


.. _streaming-ingest-rest-api-stream-load-json-simple:

Load simple JSON data
--------------------------------------------------

.. streaming-ingest-rest-api-stream-load-json-simple-start

Simple JSON data is batched together into NDJSON files that can be loaded directly to Amperity. A simple JSON schema does not contain nested values, which means that none of the values in the schema are JSON objects or arrays. For example:

.. code-block:: none

  {'field1': 'value1',
   'field2': 'value2'}

NDJSON data is loaded to Amperity using the NDJSON file format. Configure a courier |format_cbor_couriers|, and then |format_cbor_feeds|.

.. streaming-ingest-rest-api-stream-load-json-simple-end


.. _streaming-ingest-rest-api-stream-load-json-nested:

Load nested JSON data
--------------------------------------------------

.. streaming-ingest-rest-api-stream-load-json-nested-start

Nested JSON data requires a saved query to parse the nested values, after which the data is parsed into NDJSON files that can be loaded directly to Amperity. A nested JSON schema has values that are JSON objects or arrays. For example:

.. code-block:: none

  {'field1': 'value1',
   'field2': {'nested-field1': 'nested-value1',
              'nested-field2': 'nested-value2'}}

Nested NDJSON data is loaded to Amperity using the NDJSON file format. Define an |format_ndjson_ingest_query| to flatten the data into a tabular format, configure a courier |format_cbor_couriers|, and then |format_cbor_feeds|.

.. streaming-ingest-rest-api-stream-load-json-nested-end


.. _streaming-ingest-rest-api-stream-load-cbor:

Load CBOR data
--------------------------------------------------

.. streaming-ingest-rest-api-stream-load-cbor-start

To load streamed XML data that has been converted to CBOR format into Amperity, it must first be flattened into tabular format using a saved query. Use Spark SQL to extract any part of the CBOR file, and then format it into columns.

.. include:: ../../shared/terms.rst
   :start-after: .. term-saved-query-start
   :end-before: .. term-saved-query-end

.. tip:: Use Databricks to design the saved query workflow. In most cases you can design a query against a stream that is located in the container that comes with the Amperity tenant. This is an Amazon S3 bucket or an Azure Blob Storage container, depending on the cloud platform in which your tenant runs.

   #. Connect Databricks to the container.
   #. Load the CBOR file from the container to Databricks.
   #. Define a SQL query that shapes the data.
   #. Create a sample file, and then use it to add a feed, below.

XML data sent to the Streaming Ingest API is loaded to Amperity using the CBOR file format. Define an |format_cbor_ingest_query|, configure courier |format_cbor_couriers|, and then |format_cbor_feeds|.

.. streaming-ingest-rest-api-stream-load-cbor-end
