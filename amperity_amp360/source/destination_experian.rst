.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: Experian
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **experian**
.. |sftp-hostname| replace:: **stm.experian.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Experian.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Experian.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Experian

==================================================
Send query results to Experian
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-experian-start
   :end-before: .. term-experian-end

.. sendto-experian-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-experian-build-query>`
#. :ref:`Add orchestration <sendto-experian-add-orchestration>`
#. :ref:`Run orchestration <sendto-experian-run-orchestration>`

.. sendto-experian-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-experian-build-query:

Build query
==================================================

.. sendto-experian-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by Experian. Data shaping is typically required only one time.

You can do this in the following ways:

#. Add a SQL table (using |sql_spark|) to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Add a SQL query (using |sql_presto|) that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use case (or cases) for downstream workflows.

.. sendto-experian-build-query-end


.. _sendto-experian-build-query-map-fields:

Map fields to Experian
--------------------------------------------------

.. sendto-experian-build-query-map-fields-required-start

Required fields will vary based on the Experian product (and downstream use case) to which Amperity will send data, but they generally require the following fields:

* Inquiry ID (A unique identifier that is present within Experian data)
* First and last names
* Complete addresses (street, city, state, zip code)

  .. important:: Ensure that zip code values do not contain leading zeroes.

.. sendto-experian-build-query-map-fields-required-end

.. sendto-experian-build-query-map-fields-start

Build a query that maps fields in Amperity to the Experian data schema. For example:

.. code-block:: sql

   SELECT
     amperity_id
     ,given_name AS firstname
     ,surname AS lastname
     ,CASE
       WHEN billing_address IS NOT NULL THEN billing_address
       ELSE shipping_address END AS address
     ,CASE
       WHEN billing_address IS NOT NULL THEN billing_address2
       ELSE shipping_address2 END AS address2
     ,CASE
       WHEN billing_address IS NOT NULL THEN billing_city
       ELSE shipping_city END AS city
     ,CASE
       WHEN billing_address IS NOT NULL THEN billing_state
       ELSE shipping_state END AS state
     ,CASE
       WHEN billing_address IS NOT NULL THEN billing_postal
       ELSE shipping_postal END AS postal
     ,email AS email_1
     ,phone AS phone_1
   FROM
     Customer360

.. sendto-experian-build-query-map-fields-end


.. _sendto-experian-build-query-append-data:

Append previous day's data
--------------------------------------------------

.. sendto-experian-build-query-append-data-start

In some use cases, you may want to append data that was sent to Amperity from Experian to the data that is sent from Amperity to Experian. The following example queries historical Experian data tables to collect data from the previous day, and then join it to the results:

.. code-block:: sql

   WITH Experian_Import_Table AS (
     SELECT
       clid
     FROM
       Experian_Append_Versioned
     WHERE
       amperity_version = (
         SELECT DISTINCT version
         FROM amperity_table_versions
         WHERE offset = 1
       )
   )

   SELECT
     ex.*
   FROM
     Experian_Append ex
     LEFT JOIN Experian_Import_Table pr ON pr.clid = ex.clid
   WHERE
     pr.clid IS NULL
     AND substr(ex.clid,14,1) = '-'

.. sendto-experian-build-query-append-data-end


.. _sendto-experian-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-experian-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
