.. https://docs.amperity.com/operator/


.. |source-name| replace:: Salesforce Sales Cloud
.. |plugin-name| replace:: Salesforce Sales Cloud
.. |feed-name| replace:: Accounts
.. |example-filename| replace:: accounts.ndjson
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: customer records
.. |credential-type| replace:: **salesforce**


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Salesforce Sales Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Salesforce Sales Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Salesforce Sales Cloud

==================================================
Pull from Salesforce Sales Cloud
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-sales-cloud-start
   :end-before: .. term-salesforce-sales-cloud-end

.. source-salesforce-sales-cloud-rest-api-start

Salesforce Sales Cloud is a REST API that provides data for files and reports. Amperity can pull this data from Salesforce Sales Cloud for any or all of the resources that are defined for the Salesforce account.

* Salesforce Sales Cloud query results are always loaded into Amperity in full.
* Any date range supplied indirectly via a courier group is ignored.
* No input is needed when running a query manually.

.. source-salesforce-sales-cloud-rest-api-end

.. source-salesforce-sales-cloud-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-salesforce-sales-cloud-get-details>`
#. :ref:`Add courier with empty load operation <source-salesforce-sales-cloud-add-courier>`
#. :ref:`Get sample NDJSON files <source-salesforce-sales-cloud-get-sample-ndjson-files>`
#. :ref:`Add feeds <source-salesforce-sales-cloud-add-feeds>`
#. :ref:`Add load operations <source-salesforce-sales-cloud-add-load-operations>`
#. :ref:`Run courier manually <source-salesforce-sales-cloud-run-courier>`
#. :ref:`Add to courier group <source-salesforce-sales-cloud-add-to-courier-group>`

.. source-salesforce-sales-cloud-steps-to-pull-end


.. _source-salesforce-sales-cloud-get-details:

Get details
==================================================

.. source-salesforce-sales-cloud-get-details-start

Salesforce Sales Cloud requires the following configuration details:

#. The username and password of a Salesforce account configured for API access.
#. The Salesforce Sales Cloud security token that belongs to username. (The security token is not required if IP range policies are configured from the Salesforce admin console.)
#. The scheme and host for a custom Salesforce Sales Cloud URL, if used by customer.
#. If Salesforce Sales Cloud will send data to Amperity from a sandbox instance.
#. A sample for each file to simplify feed creation.

.. tip:: Use SnapPass to securely share the credentials and setup information for |source-name| between your company and your Amperity representative.

.. source-salesforce-sales-cloud-get-details-end


.. _source-salesforce-sales-cloud-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier for Salesforce Sales Cloud**

.. source-salesforce-sales-cloud-get-sample-csv-file-steps-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. From the **Credential** dropdown, select **Create a new credential**.
#. Enter the username, password, and security token.

#. Under **Salesforce Sales Cloud Settings** configure **Queries** to specify the tables (and object names) from which Amperity will pull data. For example:

   ::

      [
        {
          "from": "Account",
          "fields": [
            "*"
          ],
          "file/tag": "accounts-file"
        }
      ]

   where **from** is the table name and "*" represents the object names, in this case "all object names". Verify the names of the object names as they are defined in Salesforce Sales Cloud before configuring a specific list of fields.

   .. note:: If there is more than one table, separate each table with a comma.

      ::

         [
           {
             "from": "Account",
             "fields": [
               "field1",
               "field2"
             ],
             "file/tag": "accounts-file"
           },
           {
             "from": "OtherTable",
             "fields": [
               "field1",
               "field2"
             ],
             "file/tag": "accounts-file"
           }
         ]


#. Under **Salesforce Sales Cloud Settings** set the load operations to "{}".

   .. caution:: If load operations are not set to "{}" the validation test for the courier configuration settings will fail.

   .. important:: Do not connect to a Salesforce sandbox or enter a custom login URL.

   .. note:: You can enable a sandbox or add a custom login URL for this courier later. A custom URL for Salesforce logins requires only the scheme (http:// or https://) and hostname parts of the URL. For example: "https://<hostname>" or "http://<hostname>". The rest of the path is added automatically by Amperity. A sandbox instance is ignored when a custom URL for Salesforce logins is used.

#. Click **Save**.

.. source-salesforce-sales-cloud-get-sample-csv-file-steps-end


.. _source-salesforce-sales-cloud-get-sample-ndjson-files:

Get sample files
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-ndjson-start
   :end-before: .. term-ndjson-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

**To get sample files**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-steps-start
   :end-before: .. sources-get-sample-files-steps-end


.. _source-salesforce-sales-cloud-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-note-file-start
   :end-before: .. sources-add-feed-note-file-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-salesforce-sales-cloud-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-salesforce-sales-cloud-add-load-operations-example-start

For example:

::

   {
     "ACCOUNTS-FEED-ID": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "accounts-file"
       }
     ],
     "CUSTOM-OBJECTS-FEED-ID": [
       {
         "type": "load",
         "file": "custom-objects-file"
       }
     ]
   }

.. source-salesforce-sales-cloud-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-salesforce-sales-cloud-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

.. source-salesforce-sales-cloud-run-courier-start

.. note:: Salesforce Sales Cloud query results are always loaded into Amperity in full. No input is needed when running it manually and any date range supplied indirectly via a courier group will be ignored.

.. source-salesforce-sales-cloud-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-salesforce-sales-cloud-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
