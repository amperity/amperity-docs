.. 
.. https://docs.amperity.com/reference/
.. 

.. meta::
    :description lang=en:
        Amperity Bridge allows users to share data between Amperity and a data lakehouse using industry-standard data formats.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity Bridge allows users to share data between Amperity and a data lakehouse using industry-standard data formats.

.. meta::
    :content class=swiftype name=title data-type=string:
        About Amperity Bridge


==================================================
Amperity Bridge
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amperity-bridge-start
   :end-before: .. term-amperity-bridge-end

.. bridge-context-start

Advantages of Amperity Bridge include:

* **Fast setup** Connect Amperity to a lakehouse in minutes using sharing keys instead of integrations.

* **Zero copy** Control access to shared tables without replicating data across platforms. Build pipelines faster and consolidate your brand's storage costs into a single location.

* **Scalable processing** Enrich massive volumes of data quickly. Data is not moved or transformed from where it resides. Model customer data directly in the lakehouse or model it in Amperity.

* **Live data** View customer data at rest in a lakehouse or in Amperity through a shared catalog. Explore and query data without waiting for refreshes or updates.

.. bridge-context-end

.. bridge-learning-lab-start

.. admonition:: Amperity Learning Lab

   .. list-table::
      :widths: 150 450
      :header-rows: 0

      * - .. image:: ../../images/learning-lab-bridge.png
             :width: 140 px
             :alt: Amperity Learning Lab
             :align: left
             :class: no-scaled-link
        - Amperity Bridge enables data sharing between Amperity and data lakehouses. Each bridge can be quickly configured for inbound and outbound shares to give your brand access to shared tables without replication.

          Start with an overview of data warehouses, compare Databricks and Snowflake, and then learn how Amperity Bridge shares data between Amperity and Databricks.

          Open **Learning Lab** to learn more about how |ext_learning_lab_bridge| works. Registration is required.

.. bridge-learning-lab-end


.. _bridge-inbound-share:

Inbound shares
==================================================

.. TODO: This section is specific to Databricks. Once we have more than one outbound share to document, we'll generalize a how-to section for outbound shares, and then move this content to bridge_databricks_outbound most likely. Possible to still consolidate the inbound/outbound sharing into one topic by vendor. If shared, the first three terms should be moved to the intro.

.. include:: ../../shared/terms.rst
   :start-after: .. term-delta-sharing-start
   :end-before: .. term-delta-sharing-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-bridge-start
   :end-before: .. term-bridge-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-inbound-share-start
   :end-before: .. term-inbound-share-end

.. bridge-inbound-share-start

An inbound share is configured in a series of steps across Databricks and Amperity.

.. bridge-inbound-share-end

.. bridge-inbound-share-links-start

#. :ref:`Inbound prerequisites <bridge-inbound-share-prerequisites>`
#. :ref:`Configure Databricks <bridge-inbound-share-configure-databricks>`
#. :ref:`Add bridge <bridge-inbound-share-add-bridge>`

.. bridge-inbound-share-links-end


.. _bridge-inbound-share-prerequisites:

Inbound prerequisites
--------------------------------------------------

.. bridge-inbound-share-prerequisites-start

Before you can create inbound sharing between Databricks and Amperity a recipient and share must be created in Databricks, after which tables are added to the share and access to the share is granted to the recipient. The user who performs these actions may use the Databricks CLI or the Databricks Catalog Explorer and must the **CREATE RECIPIENT**, **CREATE SHARE**, **USE CATALOG**, **USE SCHEMA**, and **SELECT** permissions, along with the ability to grant the recipient access to the share.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: left
          :class: no-scaled-link
     - The user who will create a recipient for sharing data from Databricks to Amperity must have |ext_databricks_permission_create_recipient| permissions in Databricks.

       .. note:: If a Databricks notebook is used to create the recipient the cluster must use Databricks Runtime 11.3 LTS (or higher) and must be running in shared mode or single-cluster access mode.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: left
          :class: no-scaled-link
     - The user who will create a share in the Unity Catalog metastore must have |ext_databricks_permission_create_share| permissions in Databricks.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: left
          :class: no-scaled-link

     - The user who will add tables to a share must:

       * Be a share owner; Databricks recommends to use a group as the share owner.
       * Have |ext_databricks_permission_use_catalog| *and* |ext_databricks_permission_use_schema| permissions on the catalog and schema in which the tables are located.
       * Have |ext_databricks_permission_select| permissions to each table.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: left
          :class: no-scaled-link

     - The user who grants the recipient access to the metastore must be one of the following:

       * A metastore administrator.
       * A user with delegated permissions or ownership on both the share and recipient objects. 

         If the user created the recipient and share, they are the share owner and recipient owner.

         If the user did not create the recipient and share they will need **USE SHARE** and **SET SHARE PERMISSION** on the share and **USE RECIPIENT** on the recipient.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 5.
          :align: left
          :class: no-scaled-link

     - The IP address for Amperity may need to be added to an allowlist.

       .. include:: ../../amperity_datagrid/source/send_data.rst
          :start-after: .. send-data-to-amperity-ip-allowlists-amperity-start
          :end-before: .. send-data-to-amperity-ip-allowlists-amperity-end


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 6.
          :align: left
          :class: no-scaled-link
     - For bridges that connect to Databricks environments running in Microsoft Azure and are using storage account firewalls, the :ref:`outbound subnet IDs <bridge-inbound-share-subnet-ids>` for Amperity Bridge must be configured in Microsoft Azure using the Azure CLI.

.. bridge-inbound-share-prerequisites-end


.. _bridge-inbound-share-configure-databricks:

Configure Databricks
--------------------------------------------------

.. bridge-inbound-share-configure-databricks-start

To configure Databricks to share data with Amperity you will need to |ext_databricks_catalog_explorer_create_share| and add tables to that share, |ext_databricks_catalog_explorer_create_recipient|, |ext_databricks_catalog_explorer_grant_access_to_share|, and then get an |ext_databricks_catalog_explorer_activation_link|. The activation link allows a user to download a credential file that is required to :ref:`configure inbound sharing <bridge-inbound-share-add-bridge>` in Amperity.

.. note:: The following section briefly describes using the Databricks Catalog Explorer to configure Databricks to be ready to share data with Amperity, along with links to Databricks documentation for each step. You may use the Databricks CLI if you prefer. Instructions for using the Databricks CLI are available from the linked pages.

.. bridge-inbound-share-configure-databricks-end

**To configure Databricks for inbound sharing to Amperity**

.. bridge-inbound-share-configure-databricks-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - A share is a securable object in Unity Catalog that can be configured to share tables with Amperity.

       Open the Databricks Catalog Explorer. Under Delta Sharing, choose **Shared by me**, then select **Share data**, and then |ext_databricks_catalog_explorer_create_share_object|.

       After you have created the share you may |ext_databricks_catalog_explorer_create_share_add_tables|. Click **Add assets**, and then select the tables to share.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - A recipient in Databricks represents the entity that will consume shared data: Amperity. Configure the recipient for open sharing and to use token-based authentication.

       Open the Databricks Catalog Explorer. Under Delta Sharing, choose **Shared by me**, and then click **New recipient** to |ext_databricks_catalog_explorer_create_recipient_object|.

       After the recipient is created, |ext_databricks_catalog_explorer_grant_access_to_share|.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Open sharing uses token-based authentication.

       The credentials file that contains the token is available from an |ext_databricks_catalog_explorer_activation_link|. Use a secure channel to share the activation link with the user who will download the credentials file, and then :ref:`configure Amperity for inbound sharing <bridge-inbound-share-add-bridge>`.

       .. important:: You can download the credential file only once. Recipients should treat the downloaded credential as a secret and must not share it outside of their organization. If you have concerns that a credential may have been handled insecurely, you can |ext_databricks_rotate_credentials| at any time.

.. bridge-inbound-share-configure-databricks-steps-end


.. _bridge-inbound-share-subnet-ids:

Configure subnet IDs
--------------------------------------------------

.. bridge-inbound-share-subnet-ids-start

For bridges that connect to Databricks environments running in Microsoft Azure and are using storage account firewalls, the outbound subnet IDs for Amperity Bridge must be configured in Microsoft Azure using the Azure CLI. This step is only required for Microsoft Azure storage accounts running in any of the following regions: :ref:`az-prod East US 2 <az-prod-east-us-2>`, :ref:`az-prod East US <az-prod-east-us>`, or :ref:`az-prod-en1 North Europe <az-prod-en1-north-europe>`.

.. important:: The following command line examples use placeholders. Replace "myresourcegroup" and "mystorageaccount" to the names of the resource group and storage account that exists within your Microsoft Azure environment.

.. bridge-inbound-share-subnet-ids-end


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



.. _bridge-inbound-share-add-bridge:

Add inbound bridge
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-bridge-start
   :end-before: .. term-bridge-end

**To add an inbound bridge**

.. bridge-inbound-share-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Sources** page. Under **Inbound shares** click **Add bridge**. This opens the **Create bridge** dialog box. 

       .. image:: ../../images/bridge-inbound-name-description.png
          :width: 500 px
          :alt: Add a bridge for an inbound share.
          :align: left
          :class: no-scaled-link

       Add the name for the bridge and a description *or* select an existing bridge, and then click **Confirm**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Connect the bridge to Databricks by uploading the credential file that was downloaded from the |ext_databricks_catalog_explorer_activation_link|. There are two ways to upload the credential file:

       #. Uploading the credentials as the second step when adding a bridge. Drop the file into the dialog box or browse to a location on your local machine.
       #. Choosing the **Upload credential** option from the **Actions** menu for an inbound share.

       After the credential file is uploaded, click **Continue**.

       .. important:: You can download the credential file only once. Recipients should treat the downloaded credential as a secret and must not share it outside of their organization. If you have concerns that a credential may have been handled insecurely, you can |ext_databricks_rotate_credentials| at any time.

       When finished, click **Continue**. This will open the **Select tables to share** dialog box.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Use the **Select tables to share** dialog box to select any combination of schemas and tables to be synced to Amperity.

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
     - Map the tables that are shared from Databricks to domain tables in Amperity.

       .. image:: ../../images/bridge-map-inbound-to-domain.png
          :width: 500 px
          :alt: Map inbound shared tables to domain tables.
          :align: left
          :class: no-scaled-link

       Tables that are shared with Amperity are added as domain tables.

       * The names of shared tables must be unique among all domain tables.
       * Primary keys are not assigned.
       * Semantic tags are not applied.

       .. tip:: Use a custom domain table to assign primary keys, apply semantic tags, and shape data within shared tables to support any of your Amperity workflows.

       When finished, click **Save and sync**. This will start a workflow that synchronizes data from Databricks to Amperity and will create the mapped domain table names.

       You can manually sync tables that are shared with Amperity using the **Sync** option from the **Actions** menu for the inbound bridge.

.. bridge-inbound-share-add-bridge-steps-end


.. _bridge-outbound-shares:

Outbound shares
==================================================

.. TODO: This section is specific to Databricks. Once we have more than one outbound share to document, we'll generalize a how-to section for outbound shares, and then move this content to bridge_databricks_outbound most likely. Possible to still consolidate the inbound/outbound sharing into one topic by vendor. If shared, the first three terms should be moved to the intro.

.. include:: ../../shared/terms.rst
   :start-after: .. term-delta-sharing-start
   :end-before: .. term-delta-sharing-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-bridge-start
   :end-before: .. term-bridge-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-outbound-share-start
   :end-before: .. term-outbound-share-end

.. bridge-outbound-share-start

An outbound share is configured in a series of steps across Databricks and Amperity.

.. tip:: If you have already installed and configured the Databricks CLI and have permission to configure catalogs and providers in Databricks, the configuration process for outbound shares takes about 5 minutes.

.. bridge-outbound-share-end

.. bridge-outbound-share-links-start

#. :ref:`Outbound prerequisites <bridge-outbound-share-prerequisites>`
#. :ref:`Add bridge <bridge-outbound-share-add-bridge>`
#. :ref:`Select tables to share <bridge-outbound-share-select-tables>`
#. :ref:`Download credential file <bridge-outbound-share-download-credentials>`
#. :ref:`Add provider <bridge-outbound-share-add-provider>`
#. :ref:`Add catalog from share <bridge-outbound-share-add-catalog-from-share>`
#. :ref:`Verify table sharing <bridge-outbound-share-verify-table-sharing>`

.. bridge-outbound-share-links-end


.. _bridge-outbound-share-prerequisites:

Outbound prerequisites
--------------------------------------------------

.. bridge-outbound-share-prerequisites-start

Before you can create outbound sharing between Amperity and Databricks you must have permission to create providers and catalogs in Databricks. You may create the provider :ref:`using the Databricks CLI <bridge-outbound-share-add-provider-cli>`, :ref:`from the Databricks user interface <bridge-outbound-share-add-provider-ui>`, or by :ref:`using Python <bridge-outbound-share-add-provider-python>`.


.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: left
          :class: no-scaled-link
     - To use the Databricks CLI it must be installed and configured on your workstation.

       .. admonition:: For new users ...

          If you have not already set up and configured the Databricks CLI you will need to do the following:

          #. Install the |ext_databricks_cli_install|.
          #. Get a |ext_databricks_cli_personal_access_token|.
          #. Configure the Databricks CLI for your local machine.

             Run the |ext_databricks_cli_run_databricks_configure| command, after which you will be asked to enter the hostname for your instance of Databricks along with your personal access token.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: left
          :class: no-scaled-link
     - The user who will run the Databricks CLI and add a schema to Databricks for outbound sharing from Amperity must have |ext_databricks_permission_create_provider| permissions in Databricks.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: left
          :class: no-scaled-link
     - The user who will add the schema to a catalog in Databricks must have |ext_databricks_permission_create_catalog| permissions in Databricks.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: left
          :class: no-scaled-link
     - A user who will run queries against tables in a schema must have |ext_databricks_permission_select| permissions in Databricks. **SELECT** permissions may be granted on a specific table, on a schema, or on a catalog.


.. bridge-outbound-share-prerequisites-end


.. _bridge-outbound-share-add-bridge:

Add outbound bridge
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-bridge-start
   :end-before: .. term-bridge-end

**To add an outbound bridge**

.. bridge-outbound-share-add-bridge-steps-start

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
          :alt: Add a bridge for an outbound share.
          :align: left
          :class: no-scaled-link

       Optional. You may restrict access to specific IPs or to a valid CIDR (for a range of IPs). Place separate entries on a new line. Expand **Advanced Settings** to restrict access.

       When finished, click **Create**. This will open the **Select tables to share** dialog box, in which you will :ref:`configure any combination of schemas and tables <bridge-outbound-share-select-tables>` to share with Databricks.

.. bridge-outbound-share-add-bridge-steps-end


.. _bridge-outbound-share-select-tables:

Select tables to share
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-shared-dataset-start
   :end-before: .. term-shared-dataset-end

.. bridge-outbound-share-select-tables-start

You can configure Amperity to share any combination of schemas and tables that are available from the **Customer 360** page.

.. bridge-outbound-share-select-tables-end

**To select schemas and tables to share**

.. bridge-outbound-share-select-tables-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - After you have :ref:`configured the settings for the bridge <bridge-outbound-share-add-bridge>`, click **Next** to open the **Select tables to share** dialog box.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

       You may select any combination of schemas and tables.

       If you select a schema, all tables in that schema will be shared, including all changes made to all tables in that schema.

       When finished, click **Save**. This will open the **Download credential** dialog box, from which you will :ref:`download the credentials.share file <bridge-outbound-share-download-credentials>` that is required by the Databricks CLI when :ref:`creating a catalog in Databricks <bridge-outbound-share-add-catalog-from-share>`.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - When a bridge is already configured, you may edit the list of schemas and tables that are shared. From the **Destinations** page, under **Outbound shares**, open the **Actions** for a bridge, and then click **Edit**. This will open the **Select tables to share** dialog box.

.. bridge-outbound-share-select-tables-steps-end


.. _bridge-outbound-share-download-credentials:

Download credential file
--------------------------------------------------

.. bridge-outbound-share-download-credentials-start

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

.. bridge-outbound-share-download-credentials-end


.. _bridge-outbound-share-add-provider:

Add provider
--------------------------------------------------

.. bridge-outbound-share-add-provider-start

Databricks supports a variety of methods for adding a provider to a catalog. Use the method that works best for your organization:

* :ref:`bridge-outbound-share-add-provider-ui`
* :ref:`bridge-outbound-share-add-provider-cli`
* :ref:`bridge-outbound-share-add-provider-python`

.. bridge-outbound-share-add-provider-end


.. _bridge-outbound-share-add-provider-ui:

Databricks UI
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-outbound-share-add-provider-ui-start

You can create a provider directly from the Databricks user interface. Upload the Amperity share credentials directly as part of this process.

.. bridge-outbound-share-add-provider-ui-end

.. bridge-outbound-share-add-provider-ui-steps-start

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
     - On the providers page, click **Create catalog** to :ref:`add a catalog <bridge-outbound-share-add-catalog-from-share>` for the data that is shared from Amperity.

.. bridge-outbound-share-add-provider-ui-steps-end


.. _bridge-outbound-share-add-provider-cli:

Databricks CLI
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-outbound-share-add-provider-cli-start

You can use the Databricks CLI to create a provider in Databricks. Attach the credentials that were downloaded from Amperity to the schema as part of the command that creates the bridge between Amperity and the provider in Databricks.

.. bridge-outbound-share-add-provider-cli-start

.. bridge-outbound-share-add-provider-cli-steps-start

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
     - Run the |ext_databricks_api_providers_create| command:

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

.. bridge-outbound-share-add-provider-cli-steps-end


.. _bridge-outbound-share-add-provider-python:

Python
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-outbound-share-add-provider-python-start

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

.. bridge-outbound-share-add-provider-python-end


.. _bridge-outbound-share-add-catalog-from-share:

Add catalog from share
--------------------------------------------------

.. bridge-outbound-share-add-catalog-from-share-start

A catalog is the first layer in a Unity Catalog namespace and is used to organize data assets within Databricks.

.. bridge-outbound-share-add-catalog-from-share-end

**To add a schema to a catalog in Databricks**

.. bridge-outbound-share-add-catalog-from-share-steps-start

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

.. bridge-outbound-share-add-catalog-from-share-steps-end


.. _bridge-outbound-share-verify-table-sharing:

Verify table sharing
--------------------------------------------------

.. bridge-outbound-share-verify-table-sharing-start

Verify that the tables shared from Amperity are available from a catalog in Databricks.

.. bridge-outbound-share-verify-table-sharing-end

**To verify that tables were shared from Amperity to Databricks**

.. bridge-outbound-share-verify-table-sharing-steps-start

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

.. bridge-outbound-share-verify-table-sharing-steps-end
