.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Adobe Customer Attributes
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **adobe-customer-attributes**
.. |sftp-hostname| replace:: **ftp5.adobe.net**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Adobe Customer Attributes.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Adobe Customer Attributes.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Adobe Customer Attributes

==================================================
Send query results to Adobe Customer Attributes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-adobe-customer-attributes-start
   :end-before: .. term-adobe-customer-attributes-end

.. sendto-adobe-customer-attributes-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-adobe-customer-attributes-build-query>`
#. :ref:`Add orchestration <sendto-adobe-customer-attributes-add-orchestration>`
#. :ref:`Run orchestration <sendto-adobe-customer-attributes-run-orchestration>`

.. sendto-adobe-customer-attributes-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-adobe-customer-attributes-build-query:

Build query
==================================================

.. sendto-adobe-customer-attributes-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by Adobe Customer Attributes. Data shaping is typically required only one time.

You can do this in the following ways:

#. Add a SQL table (using |sql_spark|) to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or using the |sql_spark_cast| function to convert to a UUID.

#. Add a SQL query (using |sql_presto|) that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or using the |sql_spark_cast| function to convert to a UUID.

The correct approach here depends on the data and the desired use case (or cases) for downstream workflows.

.. sendto-adobe-customer-attributes-build-query-end


.. _sendto-adobe-customer-attributes-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-adobe-customer-attributes-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
