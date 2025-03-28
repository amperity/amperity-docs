.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: Evocalize
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **evocalize**
.. |sftp-hostname| replace:: **files.evocalize.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Evocalize.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Evocalize.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Evocalize

==================================================
Send query results to Evocalize
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-evocalize-start
   :end-before: .. term-evocalize-end

.. sendto-evocalize-cloud-storage-load-using-api-start

Provide customer data to |destination-name| in CSV format, and then use the `POST management/v1/audience <https://api-docs.evocalize.com/#upload-audience-data-csv>`__ |ext_link| to upload the audience to |destination-name|.

.. sendto-evocalize-cloud-storage-load-using-api-end

.. sendto-evocalize-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-evocalize-build-query>`
#. :ref:`Add orchestration <sendto-evocalize-add-orchestration>`
#. :ref:`Run orchestration <sendto-evocalize-run-orchestration>`

.. sendto-evocalize-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-evocalize-build-query:

Build query
==================================================

.. sendto-evocalize-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by Evocalize. Data shaping is typically required only one time.

You can do this in the following ways:

#. Add a SQL table (using |sql_spark|)  to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Add a SQL query (using |sql_presto|) that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use case (or cases) for downstream workflows.

.. sendto-evocalize-build-query-end


.. _sendto-evocalize-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-evocalize-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
