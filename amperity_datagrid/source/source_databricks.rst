.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |source-name| replace:: Databricks
.. |plugin-name| replace:: Databricks
.. |feed-name| replace:: DatabricksTable
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **databricks**
.. |credential-details| replace:: server hostname, HTTP path, and personal access token
.. |what-pull| replace:: data tables


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Databricks.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Databricks.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Databricks

==================================================
Pull from Databricks
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-databricks-start
   :end-before: .. term-databricks-end

.. source-databricks-about-start

Use this connector to pull database tables from |source-name| to Amperity.

.. source-databricks-about-end

.. source-databricks-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Cluster requirements <source-databricks-cluster-requirements>`
#. :ref:`Get details <source-databricks-get-details>`
#. :ref:`Add courier <source-databricks-add-courier>`
#. :ref:`Get sample files <source-databricks-get-sample-files>`
#. :ref:`Add feeds <source-databricks-add-feeds>`
#. :ref:`Add load operations <source-databricks-add-load-operations>`
#. :ref:`Run courier <source-databricks-run-courier>`
#. :ref:`Add to courier group <source-databricks-add-to-courier-group>`

.. source-databricks-steps-to-pull-end


.. _source-databricks-cluster-requirements:

Cluster requirements
==================================================

.. source-databricks-cluster-requirements-start

The |source-name| data source recommends the following cluster configuration:

#. **Databricks Runtime Version:** 11.3 LTS (Spark 3.3.0)
#. Can perform Python and SQL functions

.. important:: Cluster must be able to perform Python functions like `spark.conf.set('fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider')`: 

.. source-databricks-cluster-requirements-end

.. _source-databricks-get-details:

Get details
==================================================

.. source-databricks-get-details-start

The |source-name| data source requires the following configuration details:

#. The **Server Hostname** for your |source-name| data warehouse. For example: "acme.cloud.databricks.com".
#. The **HTTP Path** to your |source-name| data warehouse. For example: "sql/protocolv1/o/1abc2d3456e7f890a/abcd-1234-wxyz-6789".
#. A **Personal Access Token** to allow access to |source-name|. A personal access token is a generated string. For example: "dapi1234567890b2cd34ef5a67bc8de90fa12b".

   .. important:: |source-name| recommends using a |ext_databricks_personal_access_token| that belongs to service principals instead of workspace users.
#. Optional. **Storage Credentials** for your cloud storage container/bucket. 

   .. tip:: Using the **databricks** credential type allows you to use an Amperity-owned storage bucket. 

   .. caution:: The **databricks** credential type is recommended for ingests that take less than 1 hour. If you anticipate your data will take longer than 1 hour, please contact Amperity support.

You can find your |ext_databricks_connection_details| from the |source-name| workspace.

.. tip:: Use SnapPass to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-databricks-get-details-end


.. _source-databricks-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. tip::

   .. include:: ../../amperity_reference/source/couriers.rst
      :start-after: .. couriers-run-without-load-operations-start
      :end-before: .. couriers-run-without-load-operations-end

**To add a courier**

.. source-databricks-add-courier-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the name of the courier. For example: "|source-name|".
#. From the **Credential** drop-down, select **Create a new credential**. This opens the **Create New Credential** page.
#. Enter a name for the credential, the |credential-details|. Click **Save**.
#. Under **Databricks Settings**, add an optional folder prefix to output files in your storage bucket and a square-bracketed list of fully qualified table names.
   ::

      [
        "catalog_1.schema_1.table_1",
        "catalog_2.schema_2.table_2",
        "catalog_3.schema_3.table_3"
      ]
#. To pull a table using a query, click "Add Databricks query". In the expanded box, provide a unique query name. A query name may contain alphanumeric characters (A-Z, a-z), underscores, hyphens, and/or periods. For example: "Query_name.12-345a".

   Use |ext_databricks_sql_reference| to build a query to run against a table that is to be pulled to Amperity.

   .. important:: The name of the query must be added to the **file** parameter within the load operations. For example:

      ::

         "FEED_ID": [
           {
             "type": "load",
             "file": "Query_name.12-345a"
           }
         ]

#. Configure the load operations to have the correct feed ID, operation, and file name. (The file name is the name of the table in |source-name|.)
#. Click **Save**.

.. source-databricks-add-courier-steps-end


.. _source-databricks-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-databricks-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. note:: A feed must be added for each table that is pulled from |source-name|.

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-databricks-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-databricks-add-courier-load-operations-example-start

For example:

::

   {
     "DATABRICKS-TABLE-FEED-ID": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "catalog_name.schema_name.table_name"
       }
     ]
   }

.. source-databricks-add-courier-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-databricks-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-databricks-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
