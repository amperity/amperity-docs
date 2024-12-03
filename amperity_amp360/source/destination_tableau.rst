.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Tableau
.. |what-send| replace:: data

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Tableau.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Tableau.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Tableau

==================================================
Send query results to Tableau
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-tableau-start
   :end-before: .. term-tableau-end

.. sendto-tableau-important-start

.. important::

   .. include:: ../../amperity_amp360/source/sendto_analytics_bi.rst
      :start-after: .. sendto-tableau-important-start
      :end-before: .. sendto-tableau-important-end

.. sendto-tableau-important-end


.. _sendto-tableau-connect-to-amazon-redshift:

Connect to Amazon Redshift
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-redshift-start
   :end-before: .. term-amazon-redshift-end

.. include:: ../../amperity_datagrid/source/destination_tableau_amazon_redshift.rst
   :start-after: .. destination-tableau-amazon-redshift-workflow-start
   :end-before: .. destination-tableau-amazon-redshift-workflow-end

**To connect Tableau to Amazon Redshift**

.. include:: ../../amperity_datagrid/source/destination_tableau_amazon_redshift.rst
   :start-after: .. destination-tableau-amazon-redshift-steps-start
   :end-before: .. destination-tableau-amazon-redshift-steps-end


.. _sendto-tableau-connect-to-azure:

Connect to Azure Synapse Analytics
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-synapse-analytics-start
   :end-before: .. term-azure-synapse-analytics-end

.. include:: ../../amperity_datagrid/source/destination_tableau_azure_synapse_analytics.rst
   :start-after: .. destination-tableau-azure-synapse-analytics-workflow-start
   :end-before: .. destination-tableau-azure-synapse-analytics-workflow-end

**To connect Tableau to Azure Synapse Analytics**

.. include:: ../../amperity_datagrid/source/destination_tableau_azure_synapse_analytics.rst
   :start-after: .. destination-tableau-azure-synapse-analytics-steps-start
   :end-before: .. destination-tableau-azure-synapse-analytics-steps-end


.. _sendto-tableau-connect-to-databricks:

Connect to Databricks
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-databricks-start
   :end-before: .. term-databricks-end

.. admonition:: What is Delta table?

   .. include:: ../../shared/terms.rst
      :start-after: .. term-databricks-delta-table-start
      :end-before: .. term-databricks-delta-table-end

.. include:: ../../amperity_datagrid/source/destination_tableau_databricks.rst
   :start-after: .. destination-tableau-databricks-start
   :end-before: .. destination-tableau-databricks-end

**To connect Tableau to Databricks**

.. include:: ../../amperity_datagrid/source/destination_tableau_databricks.rst
   :start-after: .. destination-tableau-databricks-steps-start
   :end-before: .. destination-tableau-databricks-steps-end


.. _sendto-tableau-connect-to-google-bigquery:

Connect to Google BigQuery
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-bigquery-start
   :end-before: .. term-google-bigquery-end

.. include:: ../../amperity_datagrid/source/destination_tableau_google_big_query.rst
   :start-after: .. destination-tableau-google-big-query-workflow-start
   :end-before: .. destination-tableau-google-big-query-workflow-end

**To connect Tableau to Google BigQuery**

.. include:: ../../amperity_datagrid/source/destination_tableau_google_big_query.rst
   :start-after: .. destination-tableau-google-big-query-steps-start
   :end-before: .. destination-tableau-google-big-query-steps-end


.. _sendto-tableau-connect-to-snowflake:

Connect to Snowflake
==================================================

.. include:: ../../amperity_datagrid/source/destination_tableau_snowflake.rst
   :start-after: .. destination-tableau-snowflake-workflow-start
   :end-before: .. destination-tableau-snowflake-workflow-end

**To connect Tableau to Snowflake**

.. sendto-tableau-connect-to-snowflake-start

The steps required to configure Amperity to send data that is accessible to Tableau from a Snowflake data warehouse requires completion of a series of short workflows, some of which must be done outside of Amperity.

#. Configure Snowflake objects for the correct database, tables, roles, and users.
#. Send data to Snowflake from Amperity.
#. Connect Tableau to `Snowflake <https://help.tableau.com/current/pro/desktop/en-us/examples_snowflake.htm>`__ |ext_link|, and then access the data sent from Amperity.

   .. note:: The URL for the Snowflake data warehouse, the Snowflake username, the password, and the name of the Snowflake data warehouse are sent to the Tableau user within a SnapPass link. Request this information from your Amperity representative prior to attempting to connect Tableau to Snowflake.

#. Validate the workflow within Amperity and the data within Tableau.
#. Configure Amperity to automate this workflow for a regular (daily) refresh of data.

.. note:: Snowflake can be configured to run in Amazon AWS or Azure. When using the Amazon Data Warehouse you will use the same cloud platform as your Amperity tenant. When using your own instance of Snowflake, you should use the same Amazon S3 bucket or Azure Blob Storage container that is included with your tenant when configuring Snowflake for data sharing, but then connect Tableau directly to your own instance of Snowflake.

.. sendto-tableau-connect-to-snowflake-end
