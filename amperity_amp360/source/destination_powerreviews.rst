.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: PowerReviews
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **powerreviews**
.. |sftp-hostname| replace:: **sftp.powerreviews.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to PowerReviews.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to PowerReviews.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to PowerReviews

==================================================
Send query results to PowerReviews
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-powerreviews-start
   :end-before: .. term-powerreviews-end

.. sendto-powerreviews-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-powerreviews-build-query>`
#. :ref:`Add orchestration <sendto-powerreviews-add-orchestration>`
#. :ref:`Run orchestration <sendto-powerreviews-run-orchestration>`

.. sendto-powerreviews-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-powerreviews-build-query:

Build query
==================================================

.. sendto-powerreviews-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by PowerReviews. Data shaping is typically required only one time.

You can do this in the following ways:

#. Add a SQL table (using |sql_spark|) to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Add a SQL query (using |sql_presto|) that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use case (or cases) for downstream workflows.

.. sendto-powerreviews-build-query-end


.. _sendto-powerreviews-build-query-map-to-recipient-list:

Map to PowerReviews
--------------------------------------------------

.. sendto-powerreviews-build-query-map-to-recipient-list-start

You can send reviews data to PowerReviews from a query that maps data in the customer 360 database to required and optional fields in the PowerReviews data schema, as described in the `review import process <https://help.powerreviews.com/Content/Support%20Topics/Review%20Import%20Process.htm>`__ |ext_link|.

A SQL query built using Presto SQL as a query can return results for use with PowerReviews. Add a SQL table with a **SELECT** statement similar to:

.. code-block:: sql

   SELECT
     amperity_id AS "User ID"
     reviews_id AS "Review Id"
     reviews_page_id AS "Page Id"
     reviews_display AS "Review Display"
     reviews_title AS "Review Title"
     reviews_datetime AS "Review Date"
     reviews_location AS "Review Location"
     reviews_text AS "Review Text"
     reviews_rating AS "Rating"
     reviews_source AS "Review Source"
     reviews_status AS "Review Status"
     email AS "User Email"
   FROM customer360
   LIMIT 2000

.. note:: The fields in the example above represent custom fields in the customer 360 database that are built from data sources that contain reviews data for customers. This output must be mapped to the schema that is required by the PowerReviews `review import process <https://help.powerreviews.com/Content/Support%20Topics/Review%20Import%20Process.htm>`__ |ext_link|.

.. sendto-powerreviews-build-query-map-to-recipient-list-end


.. _sendto-powerreviews-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-powerreviews-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
