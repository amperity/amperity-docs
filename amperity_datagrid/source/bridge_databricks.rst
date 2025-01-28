.. https://docs.amperity.com/datagrid/


.. |destination-name| replace:: Databricks


==================================================
Configure bridge for Databricks
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-delta-sharing-start
   :end-before: .. term-delta-sharing-end

.. bridge-databricks-audits-and-encryption-start

.. admonition:: About encryption, credentials, and audit logs

   Delta Sharing uses end-to-end TLS encryption from client to server to storage account along with short-lived credentials, such as pre-signed URLs, to access data.

   Review |destination-name| documentation for `security best practices <https://www.databricks.com/blog/2022/08/01/security-best-practices-for-delta-sharing.html>`__ |ext_link|, including setting token lifetimes for metastores, rotating credentials, applying granularity for shares and recipients, configuring IP access lists, and audit logging.

   Audit logging occurs in Databricks *and* in Amperity.

   * `Audit logging <https://docs.amperity.com/reference/settings.html#about-activity-logs>`__ in Amperity shows each users actions and interactions along with access to a history of workflows with tasks that use a bridge to sync data between Amperity and Databricks.
   * Databricks captures `Delta Sharing provider events <https://docs.databricks.com/en/admin/account-settings/audit-logs.html#delta-sharing-events>`__ |ext_link|, which includes logging for when a recipient (Amperity) accesses data.

.. bridge-databricks-audits-and-encryption-end


.. _bridge-databricks-sync-with-amperity:

From Databricks
==================================================

.. bridge-databricks-sync-with-amperity-start

A sync from Databricks to Amperity requires configuration steps to be made in both Amperity and Databricks.

.. bridge-databricks-sync-with-amperity-end

.. bridge-databricks-sync-with-amperity-links-start

#. :ref:`Get details <bridge-databricks-sync-with-amperity-prerequisites>`
#. :ref:`Configure Databricks <bridge-databricks-sync-with-amperity-configure-databricks>`
#. :ref:`Configure subnet IDs <bridge-databricks-sync-with-amperity-subnet-ids>` (Microsoft Azure only)
#. :ref:`Add inbound bridge <bridge-databricks-sync-with-amperity-add-bridge>`

.. bridge-databricks-sync-with-amperity-links-end


.. _bridge-databricks-sync-with-amperity-prerequisites:

Get details
--------------------------------------------------

.. bridge-databricks-sync-with-amperity-prerequisites-start

Before you can create inbound sharing between Databricks and Amperity a recipient and share must be created in Databricks, after which tables are added to the share and access to the share is granted to the recipient.

The user who performs these actions may use the Databricks CLI or the Databricks Catalog Explorer and must be assigned the **CREATE RECIPIENT**, **CREATE SHARE**, **USE CATALOG**, **USE SCHEMA**, and **SELECT** permissions, along with the ability to grant the recipient access to the share.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: left
          :class: no-scaled-link
     - Enable Delta Sharing on the `Unity Catalog metastore <https://docs.databricks.com/en/delta-sharing/set-up.html#enable-delta-sharing-on-a-metastore>`__ |ext_link|.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: left
          :class: no-scaled-link
     - The user who will create a recipient for sharing data from Databricks to Amperity must have `CREATE CATALOG <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#create-catalog>`__ |ext_link| permissions in Databricks.

       .. note:: If a Databricks notebook is used to create the recipient the cluster must use Databricks Runtime 11.3 LTS (or higher) and must be running in shared mode or single-cluster access mode.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: left
          :class: no-scaled-link
     - The user who will create a share in the Unity Catalog metastore must have `CREATE SHARE <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#create-share>`__ |ext_link| permissions in Databricks.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: left
          :class: no-scaled-link

     - The user who will add tables to a share must:

       * Be a share owner; Databricks recommends to use a group as the share owner.
       * Have `USE CATALOG <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#use-catalog>`__ |ext_link| *and* `USE SCHEMA <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#use-schema>`__ |ext_link| permissions on the catalog and schema in which the tables are located.
       * Have `SELECT <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#select>`__ |ext_link| permissions to each table.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 5.
          :align: left
          :class: no-scaled-link

     - The user who grants the recipient access to the metastore must be one of the following:

       * A metastore administrator.
       * A user with delegated permissions or ownership on both the share and recipient objects. 

         If the user created the recipient and share, they are the share owner and recipient owner.

         If the user did not create the recipient and share they will need **USE SHARE** and **SET SHARE PERMISSION** on the share and **USE RECIPIENT** on the recipient.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 6.
          :align: left
          :class: no-scaled-link

     - The IP address for Amperity may need to be added to an allowlist when :ref:`subnet IDs are not configured in a Microsoft Azure environment <bridge-databricks-sync-with-amperity-subnet-ids>`.

       Most connections are made directly to your Amperity tenant. Use one of the following Amperity IP addresses for an allowlist that is required by an upstream system. The specific IP address to use depends on the location in which your tenant is hosted:

       * On Amazon AWS use "52.42.237.53"
       * On Amazon AWS (Canada) use "3.98.199.97"
       * On Microsoft Azure use "104.46.106.84" and "20.81.91.210"
       * On Microsoft Azure (EU) use "20.123.127.54"


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 7.
          :align: left
          :class: no-scaled-link
     - For bridges that connect to Databricks environments running in Microsoft Azure and are using storage account firewalls, the :ref:`outbound subnet IDs <bridge-databricks-sync-with-amperity-subnet-ids>` for Amperity Bridge must be configured in Microsoft Azure using the Azure CLI.

.. bridge-databricks-sync-with-amperity-prerequisites-end


.. _bridge-databricks-sync-with-amperity-configure-databricks:

Configure Databricks
--------------------------------------------------

.. bridge-databricks-sync-with-amperity-configure-databricks-start

To configure Databricks to sync data with Amperity you will need to `CREATE SHARE <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#create-share>`__ |ext_link| and add tables to that share, `CREATE RECIPIENT <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#create-recipient>`__ |ext_link|, `grant the recipient access to the share <https://docs.databricks.com/en/data-sharing/create-recipient.html#grant-the-recipient-access-to-a-share>`__ |ext_link|, and then get an `activation link <https://docs.databricks.com/en/data-sharing/create-recipient.html#step-2-get-the-activation-link>`__ |ext_link|. The activation link allows a user to download a credential file that is required to :ref:`configure inbound sharing <bridge-databricks-sync-with-amperity-add-bridge>` in Amperity.

.. note:: The following section briefly describes using the Databricks Catalog Explorer to configure Databricks to be ready to sync data with Amperity, along with links to Databricks documentation for each step. You may use the Databricks CLI if you prefer. Instructions for using the Databricks CLI are available from the linked pages.

.. bridge-databricks-sync-with-amperity-configure-databricks-end

**To configure Databricks for inbound sharing to Amperity**

.. bridge-databricks-sync-with-amperity-configure-databricks-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - A share is a securable object in Unity Catalog that can be configured to share tables with Amperity.

       Open the Databricks Catalog Explorer. Under Delta Sharing, choose **Shared by me**, then select **Share data**, and then `create a share <https://docs.databricks.com/en/data-sharing/create-share.html#create-a-share-object>`__ |ext_link|.

       After you have created the share you may `add tables to the share <https://docs.databricks.com/en/data-sharing/create-share.html#add-tables-to-a-share>`__ |ext_link|. Click **Add assets**, and then select the tables to share.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - A recipient in Databricks represents the entity that will consume shared data: Amperity. Configure the recipient for open sharing and to use token-based authentication.

       Open the Databricks Catalog Explorer. Under Delta Sharing, choose **Shared by me**, and then click **New recipient** to `create a recipient <https://docs.databricks.com/en/data-sharing/create-recipient.html#step-1-create-the-recipient>`__ |ext_link|.

       After the recipient is created, `grant the recipient access to the share <https://docs.databricks.com/en/data-sharing/create-recipient.html#grant-the-recipient-access-to-a-share>`__ |ext_link|.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Open sharing uses token-based authentication.

       The credentials file that contains the token is available from an `activation link <https://docs.databricks.com/en/data-sharing/create-recipient.html#step-2-get-the-activation-link>`__ |ext_link|. Use a secure channel to share the activation link with the user who will download the credentials file, and then :ref:`configure Amperity for inbound sharing <bridge-databricks-sync-with-amperity-add-bridge>`.

       .. important:: You can download the credential file only once. Recipients should treat the downloaded credential as a secret and must not share it outside of their organization. If you have concerns that a credential may have been handled insecurely, you can `rotate credentials <https://docs.databricks.com/en/data-sharing/create-recipient.html#security-considerations-for-tokens>`__ |ext_link| at any time.

.. bridge-databricks-sync-with-amperity-configure-databricks-steps-end


.. _bridge-databricks-sync-with-amperity-subnet-ids:

Configure subnet IDs
--------------------------------------------------

.. bridge-databricks-sync-with-amperity-subnet-ids-start

For bridges that connect to Databricks environments running in Microsoft Azure and are using storage account firewalls, the outbound subnet IDs for Amperity Bridge must be configured in Microsoft Azure using the Azure CLI. This step is only required for Microsoft Azure storage accounts running in any of the following regions: :ref:`az-prod East US 2 <az-prod-east-us-2>`, :ref:`az-prod East US <az-prod-east-us>`, or :ref:`az-prod-en1 North Europe <az-prod-en1-north-europe>`.

.. important:: The following command line examples use placeholders. Replace "myresourcegroup" and "mystorageaccount" to the names of the resource group and storage account that exists within your Microsoft Azure environment.

.. bridge-databricks-sync-with-amperity-subnet-ids-end


.. _az-prod-east-us-2:

**az-prod East US 2**

.. code-block:: bash

   az storage account network-rule add --subnet \
   /subscriptions/e733fc0a-b51a-4e9d-b6bb-fffc216f4d87/ \
   resourceGroups/prod/providers/Microsoft.Network/ \
   virtualNetworks/prod/subnets/compute-spark-outbound \
   --resource-group "myresourcegroup" \
   --account-name "mystorageaccount"


.. _az-prod-east-us:

**az-prod East US**

.. code-block:: bash

   az storage account network-rule add --subnet \
   /subscriptions/e733fc0a-b51a-4e9d-b6bb-fffc216f4d87/ \
   resourceGroups/prod-compute-failover/providers/Microsoft.Network/ \
   virtualNetworks/prod-compute-failover/subnets/compute-spark-outbound \
   --resource-group "myresourcegroup" \
   --account-name "mystorageaccount"


.. _az-prod-en1-north-europe:

**az-prod-en1 North Europe**

.. code-block:: bash

   az storage account network-rule add --subnet \
   /subscriptions/0e2b72b5-de51-4c28-8ba3-355fc7db10b7/ \
   resourceGroups/prod-en1/providers/Microsoft.Network/ \
   virtualNetworks/vnet/subnets/compute-spark-outbound \
   --resource-group "myresourcegroup" \
   --account-name "mystorageaccount"



.. _bridge-databricks-sync-with-amperity-add-bridge:

Add inbound bridge
--------------------------------------------------

Configure an inbound bridge to sync data from Databricks to Amperity.

**To add an inbound bridge**

.. bridge-databricks-sync-with-amperity-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Sources** page. Under **Inbound shares** click **Add bridge**.

       Choose **Databricks**.

       .. image:: ../../images/bridge-inbound-choose-databricks.png
          :width: 320 px
          :alt: Add a bridge for a sync.
          :align: left
          :class: no-scaled-link

       This opens the **Add bridge** dialog box.

       .. image:: ../../images/bridge-inbound-name-description.png
          :width: 500 px
          :alt: Add a bridge for a sync.
          :align: left
          :class: no-scaled-link

       Add a name and description for the bridge *or* select an existing bridge, and then click **Confirm**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Connect the bridge to Databricks by uploading the credential file that was downloaded from the `activation link <https://docs.databricks.com/en/data-sharing/create-recipient.html#step-2-get-the-activation-link>`__ |ext_link|. There are two ways to upload the credential file:

       #. Uploading the credentials as the second step when adding a bridge. Drop the file into the dialog box or browse to a location on your local machine.
       #. Choosing the **Upload credential** option from the **Actions** menu for a sync.

       After the credential file is uploaded, click **Continue**.

       .. important:: You can download the credential file only once. Recipients should treat the downloaded credential as a secret and must not share it outside of their organization. If you have concerns that a credential may have been handled insecurely, you can `rotate credentials <https://docs.databricks.com/en/data-sharing/create-recipient.html#security-considerations-for-tokens>`__ |ext_link| at any time.

       When finished, click **Continue**. This will open the **Select tables** dialog box.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Use the **Select tables** dialog box to select any combination of schemas and tables to be synced to Amperity.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

       If you select a schema, all tables in that schema will be synced. Any new tables added later will need to be manually added to the sync.

       When finished, click **Next**. This will open the **Domain table mapping** dialog box.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Map the tables that are synced from Databricks to domain tables in Amperity.

       .. image:: ../../images/bridge-map-inbound-to-domain.png
          :width: 500 px
          :alt: Map inbound synced tables to domain tables.
          :align: left
          :class: no-scaled-link

       Tables that are synced with Amperity are added as domain tables.

       * The names of synced tables must be unique among all domain tables.
       * Primary keys are not assigned.
       * Semantic tags are not applied.

       .. tip:: Use a custom domain table to assign primary keys, apply semantic tags, and shape data within synced tables to support any of your Amperity workflows.

       When finished, click **Save and sync**. This will start a workflow that synchronizes data from Databricks to Amperity and will create the mapped domain table names.

       You can manually sync tables with Amperity using the **Sync** option from the **Actions** menu for the bridge.

.. bridge-databricks-sync-with-amperity-add-bridge-steps-end


.. _bridge-databricks-sync-with-databricks:

To Databricks
==================================================

.. bridge-databricks-sync-with-databricks-start

A sync from Amperity to Databricks requires configuration steps to be made in both Amperity and Databricks.

.. tip:: If you have already installed and configured the Databricks CLI and have permission to configure catalogs and providers in Databricks, the configuration process for outbound shares takes about 5 minutes.

.. bridge-databricks-sync-with-databricks-end

.. bridge-databricks-sync-with-databricks-links-start

#. :ref:`Get details <bridge-databricks-sync-with-databricks-prerequisites>`
#. :ref:`Add bridge <bridge-databricks-sync-with-databricks-add-bridge>`
#. :ref:`Select tables to share <bridge-databricks-sync-with-databricks-select-tables>`
#. :ref:`Download credential file <bridge-databricks-sync-with-databricks-download-credentials>`
#. :ref:`Add provider <bridge-databricks-sync-with-databricks-add-provider>`
#. :ref:`Add catalog from share <bridge-databricks-sync-with-databricks-add-catalog-from-share>`
#. :ref:`Verify table sharing <bridge-databricks-sync-with-databricks-verify-table-sharing>`

.. bridge-databricks-sync-with-databricks-links-end


.. _bridge-databricks-sync-with-databricks-prerequisites:

Get details
--------------------------------------------------

.. bridge-databricks-sync-with-databricks-prerequisites-start

Before you can create outbound sharing between Amperity and Databricks you must have permission to create providers and catalogs in Databricks. You may create the provider :ref:`from the Databricks user interface <bridge-databricks-sync-with-databricks-add-provider-ui>`, :ref:`using the Databricks CLI <bridge-databricks-sync-with-databricks-add-provider-cli>`, or by :ref:`using Python <bridge-databricks-sync-with-databricks-add-provider-python>`.


.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: left
          :class: no-scaled-link
     - The user who will add the schema to a catalog in Databricks must have `CREATE CATALOG <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#create-catalog>`__ |ext_link| permissions in Databricks.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: left
          :class: no-scaled-link
     - A user who will run queries against tables in a schema must have `SELECT <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#select>`__ |ext_link| permissions in Databricks. **SELECT** permissions may be granted on a specific table, on a schema, or on a catalog.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: left
          :class: no-scaled-link
     - To use the Databricks CLI, it must be installed and configured on your workstation.

       .. admonition:: For new users ...

          If you have not already set up and configured the Databricks CLI you will need to do the following:

          #. Install the `Databricks CLI <https://docs.databricks.com/en/dev-tools/cli/install.html>`__ |ext_link|.
          #. Get a `personal access token <https://docs.databricks.com/en/dev-tools/auth/pat.html#databricks-personal-access-tokens-for-workspace-users>`__ |ext_link|.
          #. Configure the Databricks CLI for your local machine.

             Run the `databricks configure <https://docs.databricks.com/en/dev-tools/cli/configure-commands.html>`__ |ext_link| command, after which you will be asked to enter the hostname for your instance of Databricks along with your personal access token.

       The user who will run the Databricks CLI and add a schema to Databricks for outbound sharing from Amperity must have `CREATE PROVIDER <https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#create-provider>`__ |ext_link| permissions in Databricks.


.. bridge-databricks-sync-with-databricks-prerequisites-end


.. _bridge-databricks-sync-with-databricks-add-bridge:

Add outbound bridge
--------------------------------------------------

.. bridge-databricks-sync-with-databricks-add-bridge-start

Configure an outbound bridge to sync data from Amperity to Databricks.

.. bridge-databricks-sync-with-databricks-add-bridge-end

**To add an outbound bridge**

.. bridge-databricks-sync-with-databricks-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Destinations** page. Under **Outbound shares** click **Add bridge**. This opens the **Create bridge** dialog box.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Add the name for the bridge and a description, and then set the duration for which the token will remain active.

       .. image:: ../../images/bridge-add-name-and-set-token.png
          :width: 500 px
          :alt: Add a bridge for a sync.
          :align: left
          :class: no-scaled-link

       Optional. You may restrict access to specific IPs or to a valid CIDR (for a range of IPs). Place separate entries on a new line. Expand **Advanced Settings** to restrict access.

       When finished, click **Create**. This will open the **Select tables** dialog box, in which you will :ref:`configure any combination of schemas and tables <bridge-databricks-sync-with-databricks-select-tables>` to share with Databricks.

.. bridge-databricks-sync-with-databricks-add-bridge-steps-end


.. _bridge-databricks-sync-with-databricks-select-tables:

Select tables to share
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-shared-dataset-start
   :end-before: .. term-shared-dataset-end

.. bridge-databricks-sync-with-databricks-select-tables-start

You can configure Amperity to share any combination of schemas and tables that are available from the **Customer 360** page.

.. bridge-databricks-sync-with-databricks-select-tables-end

**To select schemas and tables to share**

.. bridge-databricks-sync-with-databricks-select-tables-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - After you have :ref:`configured the settings for the bridge <bridge-databricks-sync-with-databricks-add-bridge>`, click **Next** to open the **Select tables** dialog box.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

       You may select any combination of schemas and tables.

       If you select a schema, all tables in that schema will be shared, including all changes made to all tables in that schema.

       When finished, click **Save**. This will open the **Download credential** dialog box, from which you will :ref:`download the credentials.share file <bridge-databricks-sync-with-databricks-download-credentials>` that is required by the Databricks CLI when :ref:`creating a catalog in Databricks <bridge-databricks-sync-with-databricks-add-catalog-from-share>`.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - When a bridge is already configured, you may edit the list of schemas and tables that are shared. From the **Destinations** page, under **Outbound shares**, open the **Actions** for a bridge, and then click **Edit**. This will open the **Select tables** dialog box.

.. bridge-databricks-sync-with-databricks-select-tables-steps-end


.. _bridge-databricks-sync-with-databricks-download-credentials:

Download credential file
--------------------------------------------------

.. bridge-databricks-sync-with-databricks-download-credentials-start

There are two ways to download the credential file:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Click the **Download credential** button as part of the steps shown when you configure a bridge by clicking the **Add bridge** button located under **Outbound shares** on the **Destinations** page.

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Choosing the **Download credential** option from the **Actions** menu for an outbound share.

.. bridge-databricks-sync-with-databricks-download-credentials-end


.. _bridge-databricks-sync-with-databricks-add-provider:

Add provider
--------------------------------------------------

.. bridge-databricks-sync-with-databricks-add-provider-start

Databricks supports a variety of methods for adding a provider to a catalog. Use the method that works best for your organization:

* :ref:`bridge-databricks-sync-with-databricks-add-provider-ui`
* :ref:`bridge-databricks-sync-with-databricks-add-provider-cli`
* :ref:`bridge-databricks-sync-with-databricks-add-provider-python`

.. bridge-databricks-sync-with-databricks-add-provider-end


.. _bridge-databricks-sync-with-databricks-add-provider-ui:

Databricks UI
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-databricks-sync-with-databricks-add-provider-ui-start

You can create a provider directly from the Databricks user interface. Upload the Amperity share credentials directly as part of this process.

.. bridge-databricks-sync-with-databricks-add-provider-ui-end

.. bridge-databricks-sync-with-databricks-add-provider-ui-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the Databricks user interface. Open **Catalog Explorer**, then **Delta Sharing**, and then **Shared with me**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - At the bottom of the **Shared with me** page, click the **Import provider directly** button. This opens the **Import Provider** dialog.

       .. image:: ../../images/bridge-add-provider-databricks-ui.png
          :width: 400 px
          :alt: Add a provider using the Databricks user interface.
          :align: left
          :class: no-scaled-link

       Give the provider a name, and then upload the credential for the Amperity share.

       Click **Import**. This opens the providers page.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - On the providers page, click **Create catalog** to :ref:`add a catalog <bridge-databricks-sync-with-databricks-add-catalog-from-share>` for the data that is shared from Amperity.

.. bridge-databricks-sync-with-databricks-add-provider-ui-steps-end


.. _bridge-databricks-sync-with-databricks-add-provider-cli:

Databricks CLI
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-databricks-sync-with-databricks-add-provider-cli-start

You can use the Databricks CLI to create a provider in Databricks. Attach the credentials that were downloaded from Amperity to the schema as part of the command that creates the bridge between Amperity and the provider in Databricks.

.. bridge-databricks-sync-with-databricks-add-provider-cli-start

.. bridge-databricks-sync-with-databricks-add-provider-cli-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the Databricks CLI in a command window.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Run the `databricks providers create <https://docs.databricks.com/api/workspace/providers/create>`__ |ext_link| command:

       .. code-block:: bash

          $ databricks providers create socktown \ 
            TOKEN \
            -recipient-profile-str "$(< path/to/config.share)"

       where **TOKEN** is your Databricks personal access token, **socktown** is the name of the provider, and "path/to/config.share" represents the path to the location into which the Amperity credentials file was downloaded.

       .. admonition:: Databricks CLI and Windows environments

          If you are running the Databricks CLI using Powershell, the command is similar to:

          .. code-block:: bash

             $ databricks providers create socktown \ 
               TOKEN \ 
               --recipient-profile-str \ 
                 (Get-Content -Raw path\to\config.share)

          If you are running the Databricks CLI using CMD, the command is similar to:

          .. code-block:: bash

             setlocal enabledelayedexpansion ^
             set "str=" ^
             for /f "delims=" %a in (path\to\config.share) ^
             do set "str=!str!%a" ^
             databricks providers create socktown TOKEN ^
             --recipient-profile-str "!str!" ^
             endlocal


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - A successful response from Databricks is similar to:

       .. code-block:: json

          {
            "authentication_type":"TOKEN",
            "created_at":1714696789105,
            "created_by":"user@socktown.com",
            "name":"socktown",
            "owner":"user@socktown.com",
            "recipient_profile": {
              "endpoint":"URL for Amperity bridge endpoint",
              "share_credentials_version":1
            },
            "updated_at":1714696789105,
            "updated_by":"user@socktown.com"
          }

       .. admonition:: You must have CREATE PROVIDER permissions

          An error message is returned when a user who runs the **databricks providers create** command does not have **CREATE PROVIDER** permissions to the Databricks metastore.

          This error is similar to:

          .. code-block:: bash

             Error: User does not have CREATE PROVIDER \
             on Metastore '<metastore>'.

          If you receive this error message:

          #. Ask your Databricks administrator to assign to your Databricks user account the **CREATE PROVIDER** permission.
          #. Rerun the **databricks providers create** command.

.. bridge-databricks-sync-with-databricks-add-provider-cli-steps-end


.. _bridge-databricks-sync-with-databricks-add-provider-python:

Python
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-databricks-sync-with-databricks-add-provider-python-start

You can use Python to create a provider from the Databricks UI. This requires the same information to be provided to Databricks as the CLI and is similar to:

.. code-block:: python

   import requests

   headers = {
     'Authorization': f'Bearer {ACCESS_TOKEN}'
   }
   workspace = 'WORKSPACE_NAME'
   endpoint = "api/2.1/unity-catalog/providers"
   url = f"https://{workspace}.cloud.databricks.com/{endpoint}"

   data = {
     "name": "BRIDGE_NAME",
     "authentication_type": "TOKEN",
     "comment": "Amperity Bridge",
     "recipient_profile_str": "path/to/config.share"
   }

   response = requests.post(url, headers=headers, json=data)
   response.json()

.. bridge-databricks-sync-with-databricks-add-provider-python-end


.. _bridge-databricks-sync-with-databricks-add-catalog-from-share:

Add catalog from share
--------------------------------------------------

.. bridge-databricks-sync-with-databricks-add-catalog-from-share-start

A catalog is the first layer in a Unity Catalog namespace and is used to organize data assets within Databricks.

.. bridge-databricks-sync-with-databricks-add-catalog-from-share-end

**To add a schema to a catalog in Databricks**

.. bridge-databricks-sync-with-databricks-add-catalog-from-share-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Log in to Databricks, and then open the **Catalog Explorer**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - In the **Catalog Explorer**, expand **Delta Sharing**, and then select **Shared with me**.

       This will display the list of schemas to which you have access.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - From the list of schemas, select the schema you just created.

       Click the **Create catalog** button, and then in the **Create a new catalog** dialog add the catalog name. A catalog name should clearly identify that data tables are shared from Amperity. For example: "Amperity Socktown outbound share". A catalog name cannot include a period, space, or forward slash. When finihsed, click **Create**.

       .. admonition:: You must have CREATE CATALOG permissions

          An error message is returned when a user who attempts to add a schema to a catalog does not have **CREATE CATALOG** permissions to the Databricks metastore.

          This error is similar to:

          .. code-block:: bash

             Requires permission CREATE CATALOG \
             on Metastore '<metastore>'.

          If you receive this error message:

          #. Ask your Databricks administrator to assign to your Databricks user account the **CREATE CATALOG** permission.
          #. Click the **Create catalog** button and retry adding the schema to the catalog.

.. bridge-databricks-sync-with-databricks-add-catalog-from-share-steps-end


.. _bridge-databricks-sync-with-databricks-verify-table-sharing:

Verify table sharing
--------------------------------------------------

.. bridge-databricks-sync-with-databricks-verify-table-sharing-start

Verify that the tables shared from Amperity are available from a catalog in Databricks.

.. bridge-databricks-sync-with-databricks-verify-table-sharing-end

**To verify that tables were shared from Amperity to Databricks**

.. bridge-databricks-sync-with-databricks-verify-table-sharing-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - From the **Catalog Explorer** in Databricks, expand **Catalog**, and then find the catalog that was created for sharing Amperity data.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Open the catalog, and then verify that the tables you shared from Amperity are available in the catalog.

       .. image:: ../../images/databricks-catalog-view.png
          :width: 440 px
          :alt: Amperity data in a Databricks Unity Catalog.
          :align: left
          :class: no-scaled-link

.. bridge-databricks-sync-with-databricks-verify-table-sharing-steps-end
