.. https://docs.amperity.com/operator/

.. |legacy-feature| replace:: The Streaming API
.. |legacy-replacement| replace:: Real-time Profiles, which receives events on event streams and updates customer profiles, real-time segments, and real-time journeys as each event arrives
.. |legacy-instead| replace:: For new integrations, use the `Real-time API <explorer-real-time-api_>`__ instead.


.. |source-name| replace:: Streaming Ingest
.. |plugin-name| replace:: Streaming Ingest
.. |feed-name| replace:: WebEvents
.. |example-filename| replace:: filename_YYYY-MM-DD.json
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: streamed data
.. |filter-the-list| replace:: "stream"


.. meta::
    :description lang=en:
        Use the Streaming API to send events data to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use the Streaming API to send events data to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Streaming API

==================================================
Streaming API |legacy|
==================================================

.. include:: ../../shared/legacy.rst
   :start-after: .. legacy-notice-start
   :end-before: .. legacy-notice-end

.. TODO: Link "Real-time Profiles" to reference/page_real_time.html once the real-time docs (PR #973) merge.

.. include:: ../../shared/terms.rst
   :start-after: .. term-streaming-ingest-api-start
   :end-before: .. term-streaming-ingest-api-end


.. _streaming-ingest-rest-api-overview:

Overview
==================================================

.. streaming-ingest-rest-api-overview-start

The Streaming API is designed for streaming events and profile updates. It is a low latency, high throughput REST API, designed to accept billions of records per day.

The Streaming API is configured to use different streams to load data into individual feeds. For example, order events might be sent to one stream while profile updates are sent to another. Individual streams have a distinguished endpoint ``/stream/v0/data/<stream-id>``.

The Streaming API supports the following payload types:

#. JSON, which converts streaming data to NDJSON. Recommended.
#. XML, which converts streaming data to CBOR

A stream may only be one payload type.

For the endpoint's base URL, headers, payload formats, examples, limits, and response codes, and to send test requests, see the `Streaming API reference <explorer-streaming-api_>`__.

.. streaming-ingest-rest-api-overview-end


.. _streaming-ingest-rest-api-keys-and-jwt:

API keys and access tokens
==================================================

.. streaming-ingest-rest-api-keys-and-jwt-start

Requests to the Streaming API need an access token from an API key that has the **Streaming Ingest Write Access** option. To generate an access token and find your tenant ID, see `How to authenticate with Amperity APIs <https://docs.amperity.com/api/authentication.html>`__.

.. streaming-ingest-rest-api-keys-and-jwt-end


.. _streaming-ingest-endpoints:

Configure endpoints
==================================================

.. streaming-ingest-endpoints-start

You can self-manage the endpoints your brand uses to stream data to Amperity.

.. streaming-ingest-endpoints-end

**To manage Streaming API endpoints**

.. streaming-ingest-endpoints-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Sources** page.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Under **Streaming Ingest** click **Add stream**.

       .. image:: ../../images/api-streaming-ingest-add-stream.png
          :width: 500 px
          :alt: Add a Streaming API endpoint.
          :align: left
          :class: no-scaled-link

       Enter a name and description for the Streaming API endpoint.

       .. image:: ../../images/api-streaming-ingest-add-stream-name-desc.png
          :width: 420 px
          :alt: Add a name and description for the Streaming API endpoint.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - The ID for the Streaming API endpoint is available from the **Stream ID** column:

       .. image:: ../../images/api-streaming-ingest-stream-ids.png
          :width: 500 px
          :alt: Get the ID for the Streaming API endpoint.
          :align: left
          :class: no-scaled-link

       :ref:`Use this identifier in the path for the POST request <streaming-ingest-rest-api-streams>` when sending data to the Streaming API endpoint.

       For example:

       .. code-block:: none

          POST /stream/v0/data/is-AbCDefGH HTTP/1.1

.. streaming-ingest-endpoints-steps-end


.. _streaming-ingest-rest-api-streams:

Send to data streams
==================================================

.. streaming-ingest-rest-api-streams-start

Send data to a stream with a POST request to ``/stream/v0/data/{stream-id}``, using the stream ID from the :ref:`stream's endpoint <streaming-ingest-endpoints>`. For the base URL, headers, payload formats, examples, limits, and response codes, see the `Streaming API reference <explorer-streaming-api_>`__.

.. streaming-ingest-rest-api-streams-end

.. streaming-ingest-rest-api-configure-streams-postman-start

.. admonition:: About Postman

   .. include:: ../../shared/terms.rst
      :start-after: .. term-postman-start
      :end-before: .. term-postman-end

   Amperity provides complete details for using a |ext_download_postman_api_streaming| when your tenant is initialized. Use this template as the starting point for building out the API stream for your data source.

.. streaming-ingest-rest-api-configure-streams-postman-end


.. _streaming-ingest-rest-api-stream-define:

Load stream data
==================================================

.. streaming-ingest-rest-api-stream-define-start

Once data is sent to a stream, it is batched and collected to be made ready for ingest. Similar to loading files-based data, streamed data is loaded into feeds through couriers and is done from the **Sources** page.

.. streaming-ingest-rest-api-stream-define-end

.. streaming-ingest-rest-api-load-json-note-start

.. note::

   * The Streaming API only accepts individual JSON payloads and does not accept NDJSON payloads
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

NDJSON data is loaded to Amperity using the NDJSON file format. Configure a courier `load settings and operations <../reference/format_ndjson.html#couriers>`__, and then `define a feed <../reference/format_ndjson.html#couriers>`__.

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

Nested JSON data is loaded to Amperity using the NDJSON file format. Define an ingest query to flatten the data into a tabular format, configure a courier `load settings and operations <../reference/format_ndjson.html#couriers>`__, and then `define a feed <../reference/format_ndjson.html#couriers>`__.

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

XML data sent to the Streaming API is loaded to Amperity using the CBOR file format. Define an ingest query, configure courier `load settings and operations <../reference/format_cbor.html#couriers>`__, and then `define a feed <../reference/format_cbor.html#feeds>`__.

.. streaming-ingest-rest-api-stream-load-cbor-end


Pull from Streaming Ingest
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-streaming-ingest-api-start
   :end-before: .. term-streaming-ingest-api-end

.. source-streaming-ingest-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Add courier <source-streaming-ingest-legacy-add-courier>`
#. :ref:`Get sample files <source-streaming-ingest-legacy-get-sample-files>`
#. :ref:`Add feeds <source-streaming-ingest-legacy-add-feeds>`
#. :ref:`Add load operations <source-streaming-ingest-legacy-add-load-operations>`
#. :ref:`Run courier <source-streaming-ingest-legacy-run-courier>`
#. :ref:`Add to courier group <source-streaming-ingest-legacy-add-to-courier-group>`

.. source-streaming-ingest-steps-to-pull-end


.. _source-streaming-ingest-legacy-add-courier:

Add courier
--------------------------------------------------

.. source-streaming-ingest-legacy-add-courier-start

The Streaming Ingest courier pulls your data from the location that the Streaming API streams data to Amperity. A courier is required for each data stream.

.. source-streaming-ingest-legacy-add-courier-end

**To add a courier for Streaming Ingest**

.. source-streaming-ingest-legacy-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.
#. Enter the name of the courier. For example: "|source-name|".
#. A courier that pulls data that was streamed to Amperity by the Streaming API does not require a credential even though the configuration steps will ask you to add a credential. Create a new credential, name it "<tenant>-streaming-ingest" and give it a description like "Pull streams to Amperity for Streaming API".

#. Under **Streaming Ingest Settings**, add the Streaming Ingest endpoint ID which is available from the **Stream ID** column in the **Sources** page.

   Specify the **File format**, which can be `XML <../reference/format_xml.html>`__, `NDJSON <reference/format_ndjson.html>`__, or `JSON <reference/format_json.html>`__.

   Set the **File tag** to **streaming**. Set this within the file tag in load operations and the file tag text box.

   Enter the **File pattern prefix**, which is useful for time based ingestion of streaming data. This setting may be configured to load data on an hourly basis. Possible values range from ``00`` - ``24``, each of which represents an hour in a 24 hour window. For example, use ``00`` to load data at 12:00 AM, ``08`` to load data at 8:00 AM, or ``12`` to load data at 12:00 PM. A courier may only be configured to use a single file pattern prefix.

#. Set the load operations to a string that is wrong, such as **df-PLACEHOLDER**. You may also set the load operation to empty: "{}".

   .. tip:: If you use a wrong string, the load operation settings will be saved in the courier configuration. After the schema for the feed is defined and the feed is activated, you can edit the courier and replace the feed ID with the correct identifier.

   .. caution:: If load operations are not set to "{}" the validation test for the courier configuration settings fails.

#. Click **Save**.

.. source-streaming-ingest-legacy-add-courier-steps-end


.. _source-streaming-ingest-legacy-get-sample-files:

Get sample files
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-streaming-ingest-legacy-add-feeds:

Add feeds
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-note-file-start
   :end-before: .. sources-add-feed-note-file-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-streaming-ingest-legacy-add-load-operations:

Add load operations
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-streaming-ingest-legacy-add-load-operations-example-start

For example:

::

   {
     "FEED_ID": [
       {
         "type": "load",
         "file": "file_tag"
       }
     ]
   }

.. source-streaming-ingest-legacy-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-streaming-ingest-legacy-run-courier:

Run courier manually
--------------------------------------------------

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-streaming-ingest-legacy-add-to-courier-group:

Add to courier group
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

.. important:: Be sure to configure a courier that is associated with a streaming endpoint to have `a 24-hour offset <https://docs.amperity.com/reference/courier_groups.html#number-of-days>`__. This will ensure that all data that is streamed to the endpoint will be available to the scheduled workflow.

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
