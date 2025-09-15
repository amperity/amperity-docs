.. https://docs.amperity.com/user/


.. |destination-name| replace:: PebblePost
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **pebblepost**
.. |sftp-hostname| replace:: **sftp.pebblepost.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to PebblePost.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to PebblePost.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to PebblePost

==================================================
Send query results to PebblePost
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pebblepost-start
   :end-before: .. term-pebblepost-end

.. sendto-pebblepost-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-pebblepost-build-query>`
#. :ref:`Add orchestration <sendto-pebblepost-add-orchestration>`
#. :ref:`Run orchestration <sendto-pebblepost-run-orchestration>`

.. sendto-pebblepost-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-pebblepost-build-query:

Build query
==================================================

.. sendto-pebblepost-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by PebblePost. Data shaping is typically required only one time.

You can do this in the following ways:

#. Use |sql_spark| to add a SQL table to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Use |sql_presto| to build a SQL query to filter within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

Choose the approach that works best for your use cases and downstream workflows.

.. sendto-pebblepost-build-query-end


.. _sendto-pebblepost-build-query-map-to-downstream-customer:

Map to customer data
--------------------------------------------------

.. sendto-pebblepost-build-query-map-to-downstream-customer-start

A SQL query built using Presto SQL as a query can return results that map to customer data as required for use with direct mail campaigns managed from PebblePost. Be sure to verify all of the fields required by PebblePost and any field requirements for downstream workflows and use cases:

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     amperity_id AS ID
     ,given_name AS FIRST_NAME
     ,surname AS LAST_NAME
     ,address AS ADDR1
     ,address2 AS ADDR2
     ,city AS CITY
     ,state AS REGION
     ,postal AS POSTAL_CODE
     ,phone AS PHONE
     ,date_format(order_date, '%Y-%m-%d') AS LAST_PURCHASE_DATE
     ,CASE
       WHEN order_date < (current_date - interval '2' month) THEN 'True'
       ELSE NULL
       END AS RECENT_CUSTOMER
   FROM Customer_360 c

   WHERE c.email_work = false
   AND c.amperity_id IS NOT NULL
   AND given_name IS NOT NULL
   AND last_name IS NOT NULL
   AND street IS NOT NULL
   AND postal IS NOT NULL
   AND email IS NOT NULL
   AND c.customer_status <> 'Loyalty'

.. sendto-pebblepost-build-query-map-to-downstream-customer-end


.. _sendto-pebblepost-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-pebblepost-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
