.. https://docs.amperity.com/operator/


.. |source-name| replace:: Microsoft Fabric
.. |plugin-name| replace:: Microsoft Fabric
.. |feed-name| replace:: Active members
.. |example-filename| replace:: dbo.vw_active_members.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **microsoft-fabric**
.. |source-interface| replace:: |source-name|
.. |what-pull| replace:: tables and views
.. |credential-fields| replace:: the name of the credential, a description, and the |source-name| **Server**, **Database**, **Client ID**, and **Client Secret**


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Microsoft Fabric.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Microsoft Fabric.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Microsoft Fabric

==================================================
Pull from Microsoft Fabric
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-fabric-start
   :end-before: .. term-microsoft-fabric-end

.. source-microsoft-fabric-context-start

|source-name| can send |what-pull| to Amperity from a Warehouse or a Lakehouse SQL analytics endpoint. Name each table or view to pull, and then Amperity reads each one and lands it as a CSV file.

Each run reads every table and view that you configure, in full. There is no option to pull only the records that changed.

.. source-microsoft-fabric-context-end

.. source-microsoft-fabric-views-start

Amperity can read both tables and views. A view in |source-name| is a saved query that is evaluated when it is read, so what Amperity lands is the output of the view rather than the contents of the tables beneath it.

.. source-microsoft-fabric-views-end

.. source-microsoft-fabric-network-start

.. important::

   Amperity connects to the `SQL analytics endpoint <https://learn.microsoft.com/en-us/fabric/data-warehouse/connectivity>`__ |ext_link| over TDS on TCP port 1433, the same protocol and port that Microsoft SQL Server uses. No REST API is involved.

   Allow outbound access on TCP 1433, and make sure that any firewall between Amperity and |source-name| treats that port as MSSQL or TDS traffic. Protocol-aware inspection that assumes HTTPS on 1433 breaks the connection even when the port itself is open.

.. source-microsoft-fabric-network-end

.. source-microsoft-fabric-item-types-start

.. note::

   A Warehouse and a Lakehouse SQL analytics endpoint are configured the same way. A workspace serves both from one server address, and the two are told apart only by the name that you enter in **Database**. You do not need to know which kind of item you have.

.. source-microsoft-fabric-item-types-end

.. source-microsoft-fabric-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Configure Microsoft Entra access <source-microsoft-fabric-configure-entra>`
#. :ref:`Get details <source-microsoft-fabric-get-details>`
#. :ref:`Add courier <source-microsoft-fabric-add-courier>`
#. :ref:`Get sample files <source-microsoft-fabric-get-sample-files>`
#. :ref:`Add feeds <source-microsoft-fabric-add-feeds>`
#. :ref:`Add load operations <source-microsoft-fabric-add-load-operations>`
#. :ref:`Run courier <source-microsoft-fabric-run-courier>`
#. :ref:`Add to courier group <source-microsoft-fabric-add-to-courier-group>`

.. source-microsoft-fabric-steps-to-pull-end


.. _source-microsoft-fabric-configure-entra:

Configure Microsoft Entra access
==================================================

.. source-microsoft-fabric-configure-entra-start

|source-name| does not accept a user name and password. The SQL analytics endpoint supports `Microsoft Entra authentication <https://learn.microsoft.com/en-us/fabric/data-warehouse/entra-id-authentication>`__ |ext_link| only. Amperity connects as a Microsoft Entra service principal, which must be created and authorized in your Microsoft tenant before a credential can connect.

These steps are usually owned by three different groups. Identify who performs each one before you start, because a step that is discovered midway through an implementation can take days to schedule.

.. list-table::
   :widths: 46 54
   :header-rows: 1

   * - Step
     - Who performs it
   * - `Register an application <https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app>`__ |ext_link| in the `Microsoft Entra admin center <https://entra.microsoft.com/>`__ |ext_link|. This produces the **Client ID**.
     - Your identity or IT team. Registering an application is often restricted to that team.
   * - `Create a client secret <https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#add-a-client-secret>`__ |ext_link| on that application. This is the **Client Secret**.
     - Your identity or IT team. The value is shown once, when it is created, and is masked afterward. Record it at that point.
   * - Enable the tenant setting **Service principals can use Fabric APIs**, under **Admin portal > Tenant settings > Developer settings**.
     - A Fabric administrator. No one else can change a tenant setting.
   * - `Grant the service principal access <https://learn.microsoft.com/en-us/fabric/fundamentals/give-access-workspaces>`__ |ext_link| to the workspace that holds the data.
     - The team that owns the workspace, which is usually the team requesting the integration. Any workspace role is sufficient to connect, including **Viewer**.

Microsoft requires the tenant setting in the third step before a service principal may use a SQL connection string at all. There is no way to work around it, and a service principal that is otherwise configured correctly cannot connect until a Fabric administrator enables it.

.. source-microsoft-fabric-configure-entra-end

.. source-microsoft-fabric-secret-expiry-start

.. important::

   Client secrets expire. Microsoft sets an expiration when the secret is created, and the maximum is 24 months. Data stops arriving when a secret expires, and the only sign of it is a failed courier run.

   Whoever owns the application registration must rotate the secret, and that is usually not the person who notices that data has stopped arriving. Record the expiration date when the secret is created, and decide then who renews it.

.. source-microsoft-fabric-secret-expiry-end


.. _source-microsoft-fabric-get-details:

Get details
==================================================

.. source-microsoft-fabric-get-details-start

|source-name| requires the following configuration details:

#. The **Server** for the workspace.

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-microsoft-fabric-find-credentials-start
      :end-before: .. credential-microsoft-fabric-find-credentials-end

   |source-name| shows this value as the **SQL connection string**, on the Warehouse or on the settings for the Lakehouse SQL analytics endpoint. It is a host name that ends in ``datawarehouse.fabric.microsoft.com``.

   .. important::

      Despite that label, this value is a host name and not a full connection string. A value that includes ``Server=tcp:`` or a port number does not work. Enter only the host name.

#. The **Database** to read from. This is the name of the Warehouse or the Lakehouse SQL analytics endpoint. Names that contain spaces are supported.

#. The **Client ID** and **Client Secret** for the Microsoft Entra service principal, from :ref:`Configure Microsoft Entra access <source-microsoft-fabric-configure-entra>`.

#. The **Tables** to read. Enter each table or view using its fully qualified name, including the schema. For example: ``dbo.vw_active_members``. Enter at least one.

.. tip:: Use |ext_snappass| to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-microsoft-fabric-get-details-end


.. _source-microsoft-fabric-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-microsoft-fabric-add-courier-start

#. From the **Sources** page, click **Add Courier**. The **Add Courier** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.
#. Enter the name of the courier. For example: "|source-name|".

   From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.

   When finished click **Continue**.

#. Under **Tables**, enter the fully qualified name of each table or view to read. For example: ``dbo.vw_active_members``.
#. Click **Save**.

.. source-microsoft-fabric-add-courier-end

.. source-microsoft-fabric-add-courier-test-start

.. note::

   Every courier run begins by reading one row from each table and view that you named. This verifies that each object exists and can be read, rather than verifying only that the service principal can sign in. A misspelled object, or one that the service principal cannot read, fails the run at the start instead of partway through.

.. source-microsoft-fabric-add-courier-test-end


.. _source-microsoft-fabric-get-sample-files:

Get sample files
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-start
   :end-before: .. sources-get-sample-files-end

.. source-microsoft-fabric-sample-file-names-start

Amperity names each file after the table or view that it was read from, with ``.csv`` appended. For example, a view named ``dbo.vw_active_members`` lands as ``dbo.vw_active_members.csv``. The first row of each file is a header row.

.. source-microsoft-fabric-sample-file-names-end

**To get sample files**

.. source-microsoft-fabric-get-sample-files-steps-start

#. From the **Sources** tab, open the |fa-kebab| menu for a courier configured for |source-name| with empty load operations, and then select **Run**. The **Run Courier** dialog box opens.
#. Select **Load all data**. This is the only load option that |source-name| supports.
#. Click **Run**.

   .. important:: The courier run fails, but this process will successfully return a list of files from |source-name|.

   These files will be available for selection as an existing source from the **Add Feed** dialog box.
#. Wait for the notification for this courier run to return an error similar to:

   ::

      Error running load-operations task
      Cannot find required feeds: "df-xxxxxx"

.. source-microsoft-fabric-get-sample-files-steps-end


.. _source-microsoft-fabric-add-feeds:

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


.. _source-microsoft-fabric-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-start
   :end-before: .. sources-add-load-operation-example-intro-end

.. source-microsoft-fabric-add-load-operations-example-start

Refer to each file by the name of the table or view, without the ``.csv`` extension.

Because |source-name| is read in full on every run, pair each load with a truncate operation. The truncate empties the domain table so that each run replaces its contents. Without it, every run appends another full copy of the table.

For example:

::

   {
     "df-A1B2C3": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "dbo.vw_active_members"
       }
     ],
     "df-D4E5F6": [
       {
         "type": "truncate"
       },
       {
         "type": "load",
         "file": "dbo.transactions"
       }
     ]
   }

.. source-microsoft-fabric-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-microsoft-fabric-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. source-microsoft-fabric-run-courier-steps-start

#. From the **Sources** tab, open the |fa-kebab| menu for the courier with updated load operations that is configured for |source-name|, and then select **Run**. The **Run Courier** dialog box opens.
#. Select **Load all data**, the only load option that |source-name| supports. Actual data will be loaded to a domain table because the feed is configured.
#. Click **Run**.

   This time the notification will return a message similar to:

   ::

      Completed in 5 minutes 12 seconds

.. source-microsoft-fabric-run-courier-steps-end


.. _source-microsoft-fabric-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end


.. _source-microsoft-fabric-how-data-is-pulled:

How data is pulled
==================================================

.. source-microsoft-fabric-full-reads-start

**Every run reads everything.** Each run reads every table and view that you configure, in full. There is no incremental or date-windowed pull, and there is no setting that requests one.

Because each object is read in full, a record that was deleted in |source-name| can stop appearing in Amperity after the next run. This requires load operations that truncate the domain table before loading, as described in :ref:`Add load operations <source-microsoft-fabric-add-load-operations>`. A load operation without a truncate appends each run to the previous one, and a delete is never reflected.

.. source-microsoft-fabric-full-reads-end

.. source-microsoft-fabric-capacity-start

.. important::

   Reading a table or a view is a query, and each run consumes the |source-name| capacity that is assigned to your workspace. Take this into account when you set the schedule for the courier group, especially for large tables.

.. source-microsoft-fabric-capacity-end

.. source-microsoft-fabric-view-semantics-start

**A view is evaluated when it is read.** Filters and expressions in the view definition are applied by |source-name| before any data reaches Amperity. What Amperity lands is the output of the view, not the contents of the tables beneath it. A view that filters on a status column and lowercases an email address returns only the matching rows, already lowercased.

.. source-microsoft-fabric-view-semantics-end

.. source-microsoft-fabric-nulls-start

**A SQL NULL lands as an empty value.** CSV cannot distinguish an empty value from an empty string, so the difference between the two is lost when the data is read. If that distinction matters to a downstream workflow, preserve it in the view definition. For example, return a specific value in place of NULL.

.. source-microsoft-fabric-nulls-end

.. source-microsoft-fabric-column-types-start

**Every column is read as text.** Amperity converts each column to a string as it writes the CSV file, so dates, timestamps, decimals, and other typed columns land in whatever text form the SQL driver produces for them. Review a sample file before you configure the feed, and cast a column in the view definition when a downstream workflow requires a specific format.

.. source-microsoft-fabric-column-types-end


.. _source-microsoft-fabric-connection-errors:

Troubleshoot errors
==================================================

.. source-microsoft-fabric-connection-errors-start

The following errors may occur when a courier runs.

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Error
     - Resolution
   * - Microsoft Entra rejected the service principal.
     - The client ID or client secret is incorrect, or the client secret has expired. Confirm both values with whoever owns the application registration, and check the expiration date on the secret.
   * - The credential could not connect to the configured database.
     - The database name does not match a Warehouse or Lakehouse SQL analytics endpoint in the workspace, or the service principal has not been granted access to the workspace. |source-name| reports both of these the same way, so check both.
   * - Invalid object name ``'dbo.vw_active_members'``.
     - A configured table or view does not exist. The name is misspelled, is missing its schema, or names an object that the service principal cannot read. Enter the fully qualified name, such as ``dbo.vw_active_members``.
   * - A message from |source-name| about a system update, a shutdown in progress, or a workspace that is temporarily unavailable.
     - |source-name| interrupted the connection for maintenance or an internal operation. Amperity retries these automatically.
   * - Reading a table or view stopped making progress.
     - The read was ended after ten minutes without progress, rather than being left running. The error names the table or view and the number of rows that had been read. Amperity retries these automatically. Contact your Amperity representative if the error recurs.
   * - Any other error reported by |source-name|.
     - An error that Amperity does not recognize is retried automatically. Contact your Amperity representative if the error recurs.

.. source-microsoft-fabric-connection-errors-end
