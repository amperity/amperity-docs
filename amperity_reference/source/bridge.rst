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

#. :ref:`Prerequisites <bridge-outbound-share-prerequisites>`
#. :ref:`Add bridge <bridge-outbound-share-add-bridge>`
#. :ref:`Select tables to share <bridge-outbound-share-select-tables>`
#. :ref:`Download credential file <bridge-outbound-share-download-credentials>`
#. :ref:`Add provider <bridge-outbound-share-add-provider>`
#. :ref:`Add catalog from share <bridge-outbound-share-add-catalog-from-share>`
#. :ref:`Verify table sharing <bridge-outbound-share-verify-table-sharing>`

.. bridge-outbound-share-links-end


.. _bridge-outbound-share-prerequisites:

Prerequisites
--------------------------------------------------

.. bridge-outbound-share-prerequisites-start

Before you can create outbound sharing between Amperity and Databricks the Databricks CLI must be installed and configured on your workstation and you must have permission to create providers and catalogs in Databricks.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: left
          :class: no-scaled-link
     - The Databricks CLI must be installed and configured on your workstation.

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

       When finished, click **Create**. This will open the **Select tables to share** dialog box, in which you will :ref:`configure any combination of databases and tables <bridge-outbound-share-select-tables>` to share with Databricks.

.. bridge-outbound-share-add-bridge-steps-end


.. _bridge-outbound-share-select-tables:

Select tables to share
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-shared-dataset-start
   :end-before: .. term-shared-dataset-end

.. bridge-outbound-share-select-tables-start

You can configure Amperity to share any combination of databases and tables that are available from the **Customer 360** page.

.. bridge-outbound-share-select-tables-end

**To select databases and tables to share**

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
          :alt: Select databases and tables to be shared.
          :align: left
          :class: no-scaled-link

       You may select any combination of databases and tables.

       If you select a database, all tables in that database will be shared, including all changes made to all tables in that database.

       When finished, click **Save**. This will open the **Download credential** dialog box, from which you will :ref:`download the credentials.share file <bridge-outbound-share-download-credentials>` that is required by the Databricks CLI when :ref:`creating a catalog in Databricks <bridge-outbound-share-add-catalog-from-share>`.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - When a bridge is already configured, you may edit the list of databases and tables that are shared. From the **Destinations** page, under **Outbound shares**, open the **Actions** for a bridge, and then click **Edit**. This will open the **Select tables to share** dialog box.

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
