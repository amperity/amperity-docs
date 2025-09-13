.. https://docs.amperity.com/user/


.. |destination-name| replace:: Adobe Campaign
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **adobe-campaign**
.. |sftp-hostname| replace:: **[tenant].campaign.adobe.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Adobe Campaign.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Adobe Campaign.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Adobe Campaign

==================================================
Send query results to Adobe Campaign
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-adobe-campaign-start
   :end-before: .. term-adobe-campaign-end

.. sendto-adobe-campaign-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-adobe-campaign-build-query>`
#. :ref:`Add orchestration <sendto-adobe-campaign-add-orchestration>`
#. :ref:`Run orchestration <sendto-adobe-campaign-run-orchestration>`

.. sendto-adobe-campaign-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-adobe-campaign-build-query:

Build query
==================================================

.. sendto-adobe-campaign-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by Adobe Campaign. Data shaping is typically required only one time.

You can do this in the following ways:

#. Use |sql_spark| to add a SQL table to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Use |sql_presto| to add a SQL query that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use cases for downstream workflows.

.. sendto-adobe-campaign-build-query-end


.. _sendto-adobe-campaign-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-adobe-campaign-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
