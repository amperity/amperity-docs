.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Amperity supports many file types. Use Amazon S3, Azure Blob Storage, Google Cloud Storage, or any SFTP site with these file types.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity supports many file types. Use Amazon S3, Azure Blob Storage, Google Cloud Storage, or any SFTP site with these file types.

.. meta::
    :content class=swiftype name=title data-type=string:
        File formats

==================================================
File formats
==================================================

.. grid-formats-about-start

Amperity supports many file types, including CSV, JSON, NDJSON, Parquet, and streaming JSON.

.. grid-formats-about-end

.. grid-formats-about-start

.. grid:: 1 1 2 2
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: About file formats
      :link: format_common.html

      Settings and options that are common to all file formats.


   .. grid-item-card:: Apache Parquet
      :link: format_parquet.html

      A free and open source column-oriented data storage format developed within the Apache Hadoop ecosystem.


   .. grid-item-card:: Apache Avro
      :link: format_avro.html

      A row-oriented remote procedure call and data serialization framework developed within the Apache Hadoop ecosystem.


   .. grid-item-card:: CBOR
      :link: format_cbor.html

      A binary data serialization format based on JSON.


   .. grid-item-card:: CSV
      :link: format_csv.html

      A delimited text file that uses a comma to separate values.


   .. grid-item-card:: JSON
      :link: format_json.html

      A language-independent data format similar to JavaScript.


   .. grid-item-card:: NDJSON
      :link: format_ndjson.html

      A format for structured data that defines the structure of JSON data using lines as separators.


   .. grid-item-card:: PSV
      :link: format_psv.html

      A delimited text file that uses a pipe to separate values. A PSV file stores tabular data in plain text.


   .. grid-item-card:: Streaming JSON
      :link: format_json_streaming.html

      A format for increments of data using NDJSON within each increment. Each line of NDJSON file is a valid JSON value.


   .. grid-item-card:: TSV
      :link: format_tsv.html

      A delimited text file that uses a tab to separate values and stores tabular data in plain text.


   .. grid-item-card:: XML
      :link: format_xml.html

      A standalone file that uses eXtensible Markup Language (XML).

.. grid-formats-about-end


.. toctree::
   :caption: File formats
   :maxdepth: 2
   :hidden:

   About file formats <format_common>
   Apache Avro files <format_avro>
   Apache Parquet files <format_parquet>
   CBOR files <format_cbor>
   CSV files <format_csv>
   JSON files <format_json>
   NDJSON files <format_ndjson>
   PSV files <format_psv>
   Streaming JSON <format_json_streaming>
   TSV files <format_tsv>
   XML files <format_xml>
