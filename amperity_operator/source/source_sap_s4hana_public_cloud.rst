.. https://docs.amperity.com/operator/


.. |source-name| replace:: SAP S/4HANA Public Cloud
.. |plugin-name| replace:: SAP S/4HANA Public Cloud
.. |credential-type| replace:: **sap-s4hana-public-cloud**
.. |source-interface| replace:: |source-name|
.. |what-pull| replace:: sales orders, sales order line items, products, business partners, and plants
.. |credential-fields| replace:: the name of the credential, a description, and the |source-name| communication user and password


.. meta::
    :description lang=en:
        Configure Amperity to pull data from SAP S/4HANA Public Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from SAP S/4HANA Public Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from SAP S/4HANA Public Cloud

==================================================
Pull from SAP S/4HANA Public Cloud
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sap-s4hana-public-cloud-start
   :end-before: .. term-sap-s4hana-public-cloud-end

.. source-sap-s4hana-public-cloud-context-start

|source-name| can send |what-pull| to Amperity using the OData v2 APIs that SAP publishes for S/4HANA Cloud, Public Edition. Choose which data types to pull: **Business partners**, **Plants**, **Products**, **Sales order items**, and **Sales orders**. Amperity creates a feed and domain table for each data type you select.

Amperity lands every field that your SAP tenant returns for the selected records. Fields and field names are not modified, apart from the following: OData structural fields are removed, SAP timestamps are converted to standard timestamps, and fields that SAP returns as null are omitted from the record. A field that SAP returns as empty is landed as an empty value rather than omitted.

Only the fields on the record itself are landed. Data that SAP holds in related records, such as a sales order's partners or a business partner's addresses, is not included.

.. source-sap-s4hana-public-cloud-context-end

.. source-sap-s4hana-public-cloud-editions-start

.. important::

   This connector supports SAP S/4HANA Cloud, Public Edition only. SAP S/4HANA on-premise, SAP S/4HANA Cloud, Private Edition, and SAP ECC differ in how they authenticate, which APIs they publish, and how they are reached over a network. Assume this connector does not support them.

.. source-sap-s4hana-public-cloud-editions-end

.. source-sap-s4hana-public-cloud-beta-start

.. admonition:: Beta

   The |source-name| source connector is currently in beta. Contact your Amperity representative to learn more.

.. source-sap-s4hana-public-cloud-beta-end

.. source-sap-s4hana-public-cloud-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Configure SAP access <source-sap-s4hana-public-cloud-configure-sap>`
#. :ref:`Get details <source-sap-s4hana-public-cloud-get-details>`
#. :ref:`Add courier <source-sap-s4hana-public-cloud-add-courier>`
#. :ref:`Run courier <source-sap-s4hana-public-cloud-run-courier>`
#. :ref:`Review feed and domain table <source-sap-s4hana-public-cloud-review-data>`
#. :ref:`Add to courier group <source-sap-s4hana-public-cloud-add-to-courier-group>`

.. source-sap-s4hana-public-cloud-steps-to-pull-end


.. _source-sap-s4hana-public-cloud-configure-sap:

Configure SAP access
==================================================

.. source-sap-s4hana-public-cloud-configure-sap-start

SAP S/4HANA Cloud, Public Edition does not allow an external application to authenticate on its own. Your SAP administrator must configure access in SAP before Amperity can pull any data.

**To configure SAP access**

.. TODO: verify with SAP administrator / PO — the communication system step below is standard SAP procedure but is not described anywhere in /app, and no one at Amperity has walked it on a tenant. No screenshots exist for either SAP-side screen.

#. Create a communication user for Amperity using the **Maintain Communication Users** app. Record the user name and password.
#. Create a communication system that registers Amperity as the calling system, and then assign the communication user to it for inbound communication.
#. Create and activate a communication arrangement for each communication scenario in the table below. A communication arrangement is based on a communication scenario, which determines the APIs that the communication user is allowed to call.

.. source-sap-s4hana-public-cloud-configure-sap-end

.. source-sap-s4hana-public-cloud-scenarios-start

Access is granted per communication scenario, not per data type. Each scenario in the following table requires its own communication arrangement, and selecting a data type in Amperity does not grant access to it.

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Data type
     - Communication scenario
   * - Business partners
     - SAP_COM_0008
   * - Plants
     - Not identified. See the note below.
   * - Products
     - SAP_COM_0009
   * - Sales order items
     - SAP_COM_0109
   * - Sales orders
     - SAP_COM_0109

Sales orders and sales order items are served by the same scenario, so one communication arrangement covers both.

.. note::

   The communication scenario that exposes plant data is not identified. SAP does not document which scenario publishes this API for Public Edition. Before you select **Plants**, confirm with your SAP administrator that this data can be read from your tenant. Plant records carry the plant identifier and name and the company code and name. They do not include an address.

Adding a data type later requires a communication arrangement for its scenario, unless a data type you already pull uses the same one. Amperity creates a feed and domain table for each data type that you add.

.. source-sap-s4hana-public-cloud-scenarios-end


.. _source-sap-s4hana-public-cloud-get-details:

Get details
==================================================

.. source-sap-s4hana-public-cloud-get-details-start

|source-name| requires the following configuration details:

#. The **Communication User** and **Password** for the communication user that your SAP administrator created for Amperity.

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-sap-s4hana-public-cloud-find-credentials-start
      :end-before: .. credential-sap-s4hana-public-cloud-find-credentials-end

#. The **API URL** for your SAP tenant. This must start with ``https://``. For example: ``https://my123456-api.s4hana.cloud.sap``.

   .. important::

      The API URL is not the address that your staff use to sign in to SAP. It is a separate host, and the two are easily confused. Amperity verifies that the API URL is a secure address, but cannot verify that it is the correct host, so an incorrect value appears as a failed connection rather than as a validation message.

#. The **Data types** to pull. Select any combination of **Business partners**, **Plants**, **Products**, **Sales order items**, and **Sales orders**. Select at least one.

.. tip:: Use |ext_snappass| to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-sap-s4hana-public-cloud-get-details-end


.. _source-sap-s4hana-public-cloud-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-sap-s4hana-public-cloud-add-courier-start

#. From the **Sources** page, click **Add Courier**. The **Add Courier** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.
#. Enter the name of the courier. For example: "|source-name|".

   From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.

   When finished click **Continue**.

#. Enter the **API URL** for your SAP tenant.
#. Under **Data types**, select the data types to pull.
#. Click **Create**.

   Amperity creates a feed and domain table for each selected data type.

.. source-sap-s4hana-public-cloud-add-courier-end

.. source-sap-s4hana-public-cloud-add-courier-test-start

.. note::

   When you save the configuration, Amperity reads one record from every data type you selected. This verifies that the communication arrangement for each data type is active, rather than verifying only that the communication user can sign in. A data type whose communication arrangement is missing is named on this page, instead of failing later during an unattended courier run.

.. source-sap-s4hana-public-cloud-add-courier-test-end


.. _source-sap-s4hana-public-cloud-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

.. source-sap-s4hana-public-cloud-run-courier-first-start

.. important::

   Run the courier manually and select the option to load all available data before you add the courier to a scheduled courier group. A first run is not automatically a full load. A scheduled courier group always pulls a bounded time period, so a first run that is scheduled returns no records if nothing changed during that period. The courier succeeds and the domain table appears to be broken rather than empty.

.. source-sap-s4hana-public-cloud-run-courier-first-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-sap-s4hana-public-cloud-review-data:

Review feed and domain table
==================================================

.. source-sap-s4hana-public-cloud-review-data-start

After running the |source-name| courier, Amperity creates a feed and domain table for each data type you selected. You may apply semantic tags to the fields in these tables and you may make each domain table available to Stitch, depending on your use case.

The fields in each domain table are the fields that your SAP tenant returns for that record type, which vary between SAP customers because SAP customers activate different parts of the product. Expect a wide table: a sales order header in SAP's own sample data carries around 94 fields. Expect many of its columns to be empty. SAP returns an empty value for every field that your tenant does not use, and those fields are landed rather than dropped, so more than half of the columns in a domain table can be empty. That is normal for SAP data and is not a sign that the pull was incomplete. The authoritative field list for your tenant comes from your own SAP system rather than from SAP's general documentation. Contact your Amperity representative if you need the exact field list for your tenant.

.. source-sap-s4hana-public-cloud-review-data-end


.. _source-sap-s4hana-public-cloud-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end

.. source-sap-s4hana-public-cloud-courier-group-lookback-start

.. important::

   Leave **Only retrieve files dropped in the past day?** cleared unless the courier group runs daily. A scheduled courier group calculates the start of its time period from the schedule, not from the last successful run, so a failed run loses that period permanently.

   The courier group settings do not offer a longer look-back period than one day. Contact your Amperity representative to set a look-back period that is at least twice the schedule interval. Pulling the same time period twice has no adverse effect, because loading the same record again updates it.

.. source-sap-s4hana-public-cloud-courier-group-lookback-end


.. _source-sap-s4hana-public-cloud-incremental:

Incremental pulls and deleted records
==================================================

.. source-sap-s4hana-public-cloud-incremental-start

A courier group that runs on a schedule pulls records that changed during the scheduled time period, for the data types that support it. The remaining data types are pulled in full on every run.

.. list-table::
   :widths: 34 26 40
   :header-rows: 1

   * - Data type
     - Pulled incrementally
     - Notes
   * - Business partners
     - No
     - Pulled in full on every run. SAP does not populate a last-changed date on business partner records reliably enough to filter on, and filtering on it would omit records without reporting an error.
   * - Plants
     - No
     - Pulled in full on every run. SAP does not publish a last-changed timestamp for this record type.
   * - Products
     - Yes
     - Filtered on the product's last-changed timestamp.
   * - Sales order items
     - Yes
     - Filtered on the parent sales order's last-changed timestamp. SAP does not maintain a last-changed timestamp on line items.
   * - Sales orders
     - Yes
     - Filtered on the sales order's last-changed timestamp.

.. source-sap-s4hana-public-cloud-incremental-end

.. source-sap-s4hana-public-cloud-deletes-start

**Deleted records**

SAP does not expose deleted records through these APIs. A record that is deleted in SAP stops being readable, and SAP provides no indication that it was deleted. An incremental pull can therefore never remove a record from Amperity after it is deleted in SAP. Do not treat an incremental pull as a complete replica of your SAP data.

Sales orders are less affected than other data types, because SAP users typically reject a sales order rather than delete it. A rejection is an ordinary field change that an incremental pull collects.

To clear records that were deleted in SAP, configure a second courier that uses the **Truncate and upsert** load option, and then add it to a courier group that runs infrequently. Whether a courier empties a table before loading is a property of the courier rather than of an individual run, so a single courier cannot do this only sometimes. Point the second courier at the same feeds, settings, and credential as the first. This courier group requires a look-back period that is longer than the history held in your SAP tenant, which is longer than the courier group settings offer. Contact your Amperity representative to set it.

.. source-sap-s4hana-public-cloud-deletes-end


.. _source-sap-s4hana-public-cloud-connection-errors:

Troubleshoot errors
==================================================

.. source-sap-s4hana-public-cloud-connection-errors-start

The following errors may occur when you test the connection to |source-name| or when a courier runs.

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Error
     - Resolution
   * - SAP rejected the communication user.
     - The user name or password is incorrect, or the communication user is locked or expired. Confirm the credential with whoever provided it.
   * - SAP authenticated the communication user, but refused to read a data type.
     - The communication arrangement for that data type is not active for this user. The error names the data type and the communication scenario to activate. Only your SAP administrator can resolve this.
   * - SAP returned Not Found for a data type.
     - The API URL is usually incorrect, most often because it is the address used to sign in to SAP rather than the API host. This can also indicate a missing communication arrangement.
   * - SAP is rate limiting this tenant.
     - Try again shortly.
   * - Amperity could not reach the SAP OData service.
     - Confirm that the API URL is correct and that the host is reachable.
   * - SAP returned a server error.
     - A problem on the SAP side. Amperity retries these before reporting the run as failed. If it persists, ask your SAP administrator to check the tenant.
   * - The connection to SAP was lost while reading a data type.
     - A network interruption during the pull. Run the courier again.
   * - SAP rejected the request as invalid.
     - Retrying does not resolve this. Contact your Amperity representative.
   * - SAP returned a partial page while reading a data type.
     - The pull stopped rather than loading an incomplete set of records. Contact your Amperity representative.
   * - Landing stalled while reading a data type.
     - The pull stopped making progress and was ended rather than left running. The error includes the number of records that had been read, which distinguishes a pull that never started from one that stopped partway through. This is not usually caused by SAP. Contact your Amperity representative.

If one data type fails, the entire courier run is reported as failed, even though the data that was already pulled is retained. A partially loaded set of ERP data that was reported as a success would be harder to detect than a clear failure.

.. source-sap-s4hana-public-cloud-connection-errors-end
