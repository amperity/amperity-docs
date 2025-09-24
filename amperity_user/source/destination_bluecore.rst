.. https://docs.amperity.com/user/


.. |destination-name| replace:: Bluecore
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **blue-core**
.. |sftp-hostname| replace:: **triggermail.exavault.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Bluecore.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Bluecore.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Bluecore

==================================================
Send query results to Bluecore
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-bluecore-start
   :end-before: .. term-bluecore-end

.. sendto-bluecore-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-bluecore-build-query>`
#. :ref:`Add orchestration <sendto-bluecore-add-orchestration>`
#. :ref:`Run orchestration <sendto-bluecore-run-orchestration>`

.. sendto-bluecore-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-bluecore-build-query:

Build query
==================================================

.. sendto-bluecore-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by Bluecore. Data shaping is typically required only one time.

.. note:: Do not include credit card information in results that are sent to Bluecore.

You can do this in the following ways:

#. Use |sql_spark| to add a SQL table to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Use |sql_presto| to add a SQL query that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use cases for downstream workflows.

.. sendto-bluecore-build-query-end


.. _sendto-bluecore-build-query-map-to-platform:

Map to Bluecore platform
--------------------------------------------------

.. sendto-bluecore-build-query-map-to-platform-start

Review the `data type requirements for the Bluecore platform <https://help.bluecore.com/en/articles/9621372-data-types-overview>`__ |ext_link| to verify all of the requirements for sending query results to Bluecore. The following sections show an example of sending data to Bluecore using the purchases data type.

.. sendto-bluecore-build-query-map-to-platform-end


.. _sendto-bluecore-build-query-map-to-platform-with-query:

Purchases query
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sendto-bluecore-build-query-map-to-platform-with-query-start

The purchase data type requires the following fields:

* **order_id**, which is the unique ID for the purchase
* **email**, which is the unique ID used within the Bluecore platform
* **created**, which identifies the date of the purchase, in one of the following patterns: "MM/DD/YYYY HH:MM" or "YYYY-MM-DDTHH:MM:SS".
* **total**, which identifies the sum of the purchase price for all products, including taxes, in the number format without commas and currency symbol
* **products**, which identifies the product ID for each product bought as part of the purchase, separated by a pipe ( | ) character

Add a SQL table with a **SELECT** statement similar to:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id
     ,order_id AS order_id
     ,LOWER(email) AS email
     ,order_date AS created
     ,order_total AS total
     ,ARRAY_JOIN(ARRAY_AGG(product_id), '|') AS products
   FROM Customer360
   LIMIT 1000

.. sendto-bluecore-build-query-map-to-platform-with-query-end


.. _sendto-bluecore-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. sendto-bluecore-add-orchestration-important-start

.. important:: Bluecore requires a header row to be present in CSV files. The header row cannot start with a number or contain any special characters other than underscores ( _ ) and must be less than 30 characters in length.

.. sendto-bluecore-add-orchestration-important-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-bluecore-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
