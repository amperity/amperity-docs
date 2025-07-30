.. https://docs.amperity.com/operator/


.. |source-name| replace:: Google BigQuery
.. |destination-name| replace:: Google BigQuery

.. meta::
    :description lang=en:
        Amperity Bridge for Google BigQuery is a first-class integration that uses BigQuery Sharing to enable inbound data access to Amperity from Google BigQuery.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity Bridge for Google BigQuery is a first-class integration that uses BigQuery Sharing to enable inbound data access to Amperity from Google BigQuery.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure Amperity Bridge for Google BigQuery

==================================================
Configure Amperity Bridge for Google BigQuery
==================================================

.. bridge-google-bigquery-about-start

Amperity Bridge for Google BigQuery is a first-class integration enables inbound data access to Amperity from Google BigQuery without copying data or scheduling ETL workloads.

.. bridge-google-bigquery-about-end

.. bridge-google-bigquery-what-is-bigquery-sharing-start

.. admonition:: What is BigQuery Sharing?

   `BigQuery Sharing <https://console.cloud.google.com/bigquery/analytics-hub?inv=1&invt=Ab26qA>`__ |ext_link| publishes and shares datasets between organizations. Create an exchange, and then invite organizations to publish or subscribe to data in the exchange.

.. bridge-google-bigquery-what-is-bigquery-sharing-end

.. bridge-google-bigquery-switch-to-bridge-start

.. tip:: Amperity Bridge shares data directly with Google BigQuery. A bridge does not require a courier or a database export to be configured. A bridge can be configured to run automatically as part of any scheduled workflow.

.. bridge-google-bigquery-switch-to-bridge-end


.. _bridge-google-bigquery-sync-with-amperity:

From Google BigQuery
==================================================

.. bridge-google-bigquery-sync-amperity-start

A sync from |source-name| to Amperity requires configuration steps to be made in both Amperity and |source-name|.

.. bridge-google-bigquery-sync-amperity-end

.. bridge-google-bigquery-sync-amperity-links-start

#. :ref:`Get details <bridge-google-bigquery-sync-amperity-get-details>`
#. :ref:`Configure Google BigQuery <bridge-google-bigquery-sync-amperity-configure-bigquery>`
#. :ref:`Add inbound bridge <bridge-google-bigquery-sync-amperity-add-bridge>`

.. bridge-google-bigquery-sync-amperity-links-end


.. _bridge-google-bigquery-sync-amperity-get-details:

Get details
--------------------------------------------------

.. bridge-google-bigquery-sync-amperity-get-details-start

Before you can create inbound sharing between |source-name| and Amperity you will need to collect the following information.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: center
          :class: no-scaled-link
     - The individual who configures Amperity to share data with |destination-name| must be assigned the **Datagrid Administrator** policy in Amperity or have the ability to configure a bridge for |source-name| in a sandbox.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: center
          :class: no-scaled-link
     - A Google Cloud account with the `BigQuery API enabled <https://cloud.google.com/bigquery/docs/bigquery-web-ui>`__ |ext_link|.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: center
          :class: no-scaled-link
     - The user who creates the data exchange and listing in |source-name| must have permission to access to the Google Analytics Hub API. The following `permissions <https://cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges#required_permissions>`__ |ext_link| are required:

       * **serviceUsage.services.get**
       * **serviceUsage.services.list**
       * **serviceUsage.services.enable**

       .. note:: **roles/serviceusage.serviceUsageAdmin** is a predefined IAM role that includes the permissions required to access the Analytics Hub API.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: center
          :class: no-scaled-link
     - The user who creates the data exchange and listing in |destination-name| must have permission to create listings. The following `permissions <https://cloud.google.com/bigquery/docs/access-control#bigquery>`__ |ext_link| are required:

       * **bigquery.datasets.get**
       * **bigquery.datasets.update**

       .. note:: **roles/bigquery.dataOwner** and **roles/bigquery.admin** are predefined IAM roles that include the permissions required to create listings in |destination-name|.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: center
          :class: no-scaled-link
     - The following values are required to connect Amperity to a |source-name| data listing:

       #. **Share link** (for the data exchange)

          This value is available after creating the :ref:`data exchange <bridge-google-bigquery-sync-amperity-configure-bigquery-exchange>` and :ref:`data listing <bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing>` in |source-name|. Copy this value. It is required when :ref:`adding the inbound share <bridge-google-bigquery-sync-amperity-add-bridge>`.

          ::

             https://console.cloud.google.com/bigquery/analytics-hub/\
             exchanges/projects/123456789012/locations/<location>/\
             dataExchanges/<exchange>/listings/<listing>

       #. **Subscriber**

          Amperity generates an account identifer to use for activating sharing in |source-name|. Copy this value and use it to configure permissions to the data exchange. Add a principal using this value and assign it to the `Analytics Hub Subscriber <https://cloud.google.com/bigquery/docs/analytics-hub-grant-roles#ah-subscriber-role>`__ |ext_link| role.

          The account identifier generated by Amperity is similar to:

          ::

             amperity-bridge-<bridge-id>@amperity.iam.gserviceaccount.com


.. bridge-google-bigquery-sync-amperity-get-details-end


.. _bridge-google-bigquery-sync-amperity-configure-bigquery:

Configure Google BigQuery
--------------------------------------------------

.. bridge-google-bigquery-sync-amperity-configure-bigquery-start

To configure |source-name| to sync data with Amperity do the following:

#. :ref:`Create data exchange <bridge-google-bigquery-sync-amperity-configure-bigquery-exchange>`
#. :ref:`Create data listing <bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing>`
#. :ref:`Configure subscriber and share link <bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share>`

.. bridge-google-bigquery-sync-amperity-configure-bigquery-end


.. _bridge-google-bigquery-sync-amperity-configure-bigquery-exchange:

Create data exchange
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-google-bigquery-sync-amperity-configure-bigquery-exchange-start

A `data exchange <https://cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges#console>`__ |ext_link| in |destination-name| is private by default. Only users and groups that have access to the data exchange can view or subscribe to data listings within the data exchange.

`Create a data exchange <https://cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges#create-exchange>`__ |ext_link| in |destination-name| and then allow Amperity access to that data exchange.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-exchange-end

**To create a Google BigQuery data exchange**

.. bridge-google-bigquery-sync-amperity-configure-bigquery-exchange-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - Open the **BigQuery Console** to the **Sharing** page.

       On the **Sharing** page click **Create exchange**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - In the **Exchange configuration** pane, do the following:

       #. Select the project and region for the data exchange.
       #. Enter a display name.
       #. Add your Amperity account locator.

       .. note:: If you are configuring a new bridge, leave the Amperity account locator field blank. This will be added after the :ref:`account identifier is created <bridge-google-bigquery-sync-amperity-add-bridge>`.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - Click **Create exchange**.

       .. important:: Do not configure permissions for the data exchange. The value for the **Add principal** field must be the value that is :ref:`generated by Amperity <bridge-google-bigquery-sync-amperity-add-bridge>`.

       Click **Skip**.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-exchange-steps-end


.. _bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing:

Create data listing
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing-start

A `data listing <https://cloud.google.com/bigquery/docs/analytics-hub-manage-listings>`__ |ext_link| in |destination-name| is a reference to a shared dataset that exists in a data exchange. A data listing is private by default.

A `data listing within a private data exchange <https://cloud.google.com/bigquery/docs/analytics-hub-manage-listings#create_a_listing>`__ |ext_link| may be shared with Amperity.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing-end

**To create a Google BigQuery data listing**

.. bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - On the **Sharing** page click the name of the exchange.

       On the **Listings** tab for the exchange click **Create listing**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - From the **Resource type** dropdown select "BigQuery Dataset", and then select a dataset.

       .. note:: Configuring data egress controls is optional.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - Configure a series of details for the data listing.

       Click **Next**.

       * Required. Add a display name.
       * Optional. Configure listing details, discoverability, and email logging.

       Click **Next**

       * Optional. Configure the contact information for primary, provider, and publisher contacts.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - Click **Publish**.

       On the **Listings** tab, in the row for the listing that will be shared with Amperity, from the ellipses menu select **Copy share link**.

       Amperity generates a URL similar to:

       ::

          https://console.cloud.google.com/bigquery/analytics-hub/exchanges/projects/123456789012/locations/<location>/dataExchanges/<exchange>/listings/<listing>

       Configure this identifier in |source-name| as the :ref:`subscriber for the data listing <bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share>`.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing-steps-end


.. _bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share:

Configure subscriber and share link
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share-start

A `subscriber is allowed to view and access a data listing <https://cloud.google.com/bigquery/docs/analytics-hub-manage-subscriptions>`__ |ext_link|. Configure Amperity as the subscriber to the |source-name| data listing.

A share link allows a subscriber to connect to a data listing. Copy the share link for the data listing in |source-name| and configure that link in Amperity.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share-end

**To configure a Google BigQuery subscriber and share link**

.. bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - On the **Sharing** page in the row for the exchange that will share data with Amperity select **Set permissions** from the ellipses menu.

       Click **Add principal**

       Paste the Amperity account identifier into the **New principal** field and set the role to be `Analytics Hub Subscriber <https://cloud.google.com/bigquery/docs/analytics-hub-grant-roles#ah-subscriber-role>`__ |ext_link|.

       Click **Save**

       This returns you to the **Sharing** page.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - On the **Sharing** page in the row for the exchange that will share data with Amperity select **Copy share link** from the ellipses menu.

       .. important:: This value required when :ref:`adding the inbound share <bridge-google-bigquery-sync-amperity-add-bridge>`.


.. bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share-steps-end


.. _bridge-google-bigquery-sync-amperity-add-bridge:

Add inbound bridge
--------------------------------------------------

.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-start

Configure an inbound bridge to sync data from Google BigQuery to Amperity.

.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-end

**To add an inbound bridge for Google BigQuery**

.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - Open the **Sources** page. Under **Inbound shares** click **Add bridge**. 

       Choose **Google BigQuery**.

       .. image:: ../../images/bridge-inbound-choose-bigquery.png
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
          :align: center
          :class: no-scaled-link
     - Add the :ref:`share link <bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share>` that was copied from the |source-name| data exchange.

       Amperity generates the subscriber link *after* the share link has been configured. The share link is a URL similar to:

       ::

          https://console.cloud.google.com/bigquery/analytics-hub/exchanges/projects/123456789012/locations/<location>/dataExchanges/<exchange>/listings/<listing>

       Configure this identifier in |source-name| as the :ref:`subscriber for the data listing <bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share>`.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
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
          :align: center
          :class: no-scaled-link
     - Map the tables that are synced from |source-name| to domain tables in Amperity.

       .. image:: ../../images/bridge-map-inbound-to-domain.png
          :width: 500 px
          :alt: Map synced tables to domain tables.
          :align: left
          :class: no-scaled-link

       Tables that are synced with Amperity are added as domain tables.

       * The names of synced tables must be unique among all domain tables.
       * Primary keys are not assigned.
       * Semantic tags are not applied.

       .. tip:: Use a custom domain table to assign primary keys, apply semantic tags, and shape data within synced tables to support any of your Amperity workflows.

       When finished, click **Save and sync**. This will start a workflow that synchronizes data from |source-name| to Amperity and will create the mapped domain table names.

       You can manually sync tables that are synced with Amperity using the **Sync** option from the **Actions** menu for the inbound bridge.


.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-steps-end
