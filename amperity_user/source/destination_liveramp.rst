.. https://docs.amperity.com/user/


.. |destination-name| replace:: LiveRamp
.. |what-send| replace:: CSV, TSV, or PSV files
.. |sftp-type| replace:: **liveramp**
.. |sftp-hostname| replace:: **files.liveramp.com**,**sftp-au.liverampapac.com**, or **sftp.liveramp.com**
.. |file-format| replace:: CSV, TSV, or PSV
.. |encoding-method| replace:: "GZip".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to LiveRamp.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to LiveRamp.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to LiveRamp

==================================================
Send query results to LiveRamp
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-liveramp-start
   :end-before: .. term-liveramp-end

.. sendto-liveramp-start

You can associate records in Amperity to an audience in |destination-name| by sending a combination of identifier data and query data. |destination-name| uses:

* Identifier data to match records to other `identifiers <https://docs.liveramp.com/connect/en/identity-and-identifier-terms-and-concepts.html#identifier-data>`__ |ext_link| in the |destination-name| Identity Graph.
* Segment data to group records into `segments <https://docs.liveramp.com/connect/en/segment-data.html>`__ |ext_link| based on certain attributes for downstream targeting, measurement, and personalization. 

|destination-name| requires an audience ID. This may be a client customer ID from another application, it may be the |destination-name| audience ID itself (from |destination-name| data that was imported to Amperity), or it may be the Amperity ID.

.. sendto-liveramp-end

.. sendto-liveramp-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-liveramp-build-query>`
#. :ref:`Add orchestration <sendto-liveramp-add-orchestration>`
#. :ref:`Run orchestration <sendto-liveramp-run-orchestration>`

.. sendto-liveramp-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-liveramp-build-query:

Build query
==================================================

.. sendto-liveramp-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by |destination-name|. Data shaping is typically required only one time.

You can do this in the following ways:

#. Use |sql_spark| to add a SQL table to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Use |sql_presto| to add a SQL query that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use cases for downstream workflows.

.. sendto-liveramp-build-query-end

.. sendto-liveramp-build-query-important-start

.. important:: Uploads to |destination-name| may fail when:

   * The headers in the output file do not match the headers in |destination-name|.
   * Two or more headers in the output file are identical.
   * The audience key in the output file does not match the audience key in LiveRamp.
   * The audience key is missing.
   * Mismatched identifiers. For example, if |destination-name| expects first and last names to be in the same field, but the output contains first and last names in separate fields.

.. sendto-liveramp-build-query-important-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-liveramp-build-query-pii:

LiveRamp and PII data
--------------------------------------------------

.. sendto-liveramp-build-query-pii-start

`LiveRamp terms of service restrict PII data <https://docs.liveramp.com/connect/en/liveramp-data-restrictions.html>`__ |ext_link| -- government-issued identification numbers (like social security numbers), financial and customer account numbers, birthdates, gender, email addresses, names (first, last, and full), and similar data -- should be excluded from query data that is sent to |destination-name|.

Because the data sent to |destination-name| contains the Amperity ID, should you need to associate data with PII, you can use other systems that allow PII data along with the Amperity ID to make these associations.

`Hash fields that must be sent to LiveRamp <https://docs.liveramp.com/connect/en/hashing-identifiers.html>`__ |ext_link| by using :ref:`one-way SHA-256 hashing <sendto-liveramp-build-query-sha-256>` or by :ref:`casting the value to a random unique identifier (UUID) <sendto-liveramp-build-query-cast-as-uuid>`.

.. sendto-liveramp-build-query-pii-end


.. _sendto-liveramp-build-query-sha-256:

One-way SHA-256 hash
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-style-guide-one-way-sha256-hashes-start
   :end-before: .. sql-presto-style-guide-one-way-sha256-hashes-end

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-style-guide-one-way-sha256-hash-syntax-start
   :end-before: .. sql-presto-style-guide-one-way-sha256-hash-syntax-end

.. sendto-liveramp-build-query-sha-256-start

For example:

.. code-block:: sql

   TO_HEX(SHA256(TO_UTF8(UPPER(TRIM(email)))))

.. sendto-liveramp-build-query-sha-256-end


.. _sendto-liveramp-build-query-cast-as-uuid:

CAST as UUID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-cast-start
   :end-before: .. sql-presto-function-cast-end

.. sendto-liveramp-build-query-cast-as-uuid-start

For example:

.. code-block:: sql

   ,CAST(email AS UUID) AS "EMAIL1"

.. sendto-liveramp-build-query-cast-as-uuid-end


.. _sendto-liveramp-build-query-map-to-audience:

Map to audience
--------------------------------------------------

.. sendto-liveramp-build-query-map-to-audience-start

A SQL query can `output results that map to an audience in LiveRamp <https://docs.liveramp.com/connect/en/formatting-column-based-files.html#headers-to-use-for-u-s--pii-data-files>`__ |ext_link|. Add a SQL query with a **SELECT** statement similar to:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS CCID
     ,REGEXP_REPLACE(given_name, '[*@/.,_-]', '') AS FIRSTNAME
     ,REGEXP_REPLACE(surname, '[*@/.,_-]', '') AS LASTNAME
     ,address AS ADDRESS1
     ,address2 AS ADDRESS2
     ,city AS CITY
     ,UPPER(state) AS ST
     ,REGEXP_EXTRACT(postal,'^(\d{5})') AS ZIP
     ,CONCAT('+1','',REGEXP_REPLACE(phone,'[\D]','')) AS PHONE1
   FROM customer360
   LIMIT 2000

and then assign this query to a destination that sends results to |destination-name|.

.. note:: The **CCID** field is optional, but may be used as an audience key. The example shows using the Amperity ID as the audience key.

.. sendto-liveramp-build-query-map-to-audience-end


.. _sendto-liveramp-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. sendto-liveramp-add-orchestration-important-start

.. important:: Sending data to |destination-name| should follow recommendations for `uploading data <https://docs.liveramp.com/connect/en/uploading-data.html>`__ |ext_link|. Review |destination-name| `file limitations <https://docs.liveramp.com/connect/en/liveramp-data-restrictions.html>`__ |ext_link|. |destination-name| prefers `GPG encryption <https://docs.liveramp.com/connect/en/encrypting-files-for-uploading.html>`__ |ext_link| and GZip compression. |destination-name| supports the following `file formats <https://docs.liveramp.com/connect/en/formatting-file-data.html>`__ |ext_link|:

   * CSV
   * PSV
   * TSV

   Enable the **Include header row in output files** option for the Amperity destination.

.. sendto-liveramp-add-orchestration-important-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-liveramp-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
