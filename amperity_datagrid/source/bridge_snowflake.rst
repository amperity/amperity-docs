.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |destination-name| replace:: Snowflake


==================================================
Configure bridge for Snowflake
==================================================

.. bridge-snowflake-about-start

Snowflake Bridge is a first-class integration that leverages secure data sharing to enable bi-directional data access between Amperity and Snowflake without copying data or scheduling ETL workloads.

.. bridge-snowflake-about-end

.. bridge-snowflake-what-is-data-sharing-start

.. admonition:: What is Secure Data Sharing?

   `Secure Data Sharing <https://docs.snowflake.com/en/user-guide/data-sharing-intro>`__ |ext_link| enables data sharing between Snowflake accounts without copying or transferring data and instead relies on the services layer and metadata store within Snowflake. Your brand controls what data will be made available to Amperity directly from within your brand's Snowflake account.

.. bridge-snowflake-what-is-data-sharing-end

.. bridge-snowflake-switch-to-bridge-start

.. tip:: Amperity Bridge shares data directly with Snowflake. A bridge does not require a courier or a database export to be configured. A bridge can be configured to run automatically as part of any scheduled workflow.

   If your brand is currently using BI Connect to make data available in Snowflake your brand should consider moving the BI Connect workflow to Amperity Bridge. This will increase the speed at which This will allow your brand to self-service the data that is shared between Amperity and Snowflake directly from within your Snowflake account.

.. bridge-snowflake-switch-to-bridge-end


.. _bridge-snowflake-sync-with-amperity:

From Snowflake
==================================================

.. bridge-snowflake-sync-amperity-start

A sync from Snowflake to Amperity requires configuration steps to be made in both Amperity and Snowflake.

.. bridge-snowflake-sync-amperity-end

.. bridge-snowflake-sync-amperity-links-start

#. :ref:`Get details <bridge-snowflake-sync-amperity-get-details>`
#. :ref:`Configure Snowflake <bridge-snowflake-sync-amperity-configure-snowflake>`
#. :ref:`Add inbound bridge <bridge-snowflake-sync-amperity-add-bridge>`

.. bridge-snowflake-sync-amperity-links-end


.. _bridge-snowflake-sync-amperity-get-details:

Get details
--------------------------------------------------

.. bridge-snowflake-sync-amperity-get-details-start

Before you can create inbound sharing between Snowflake and Amperity you will need to collect the following information.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: left
          :class: no-scaled-link
     - The organization name and account name for your brand's |destination-name| account.

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-organization-start
          :end-before: .. credential-snowflake-organization-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-account-name-start
          :end-before: .. credential-snowflake-account-name-end

       .. tip:: To `find your organization name and account name <https://docs.snowflake.com/en/user-guide/admin-account-identifier#finding-the-organization-and-account-name-for-an-account>`__ |ext_link| use **Snowsight**.

          Open the account selector and browse to the account for which Amperity Bridge will be configured. Hover over the account name to view additional details, and then copy the account identifier.

          The copied identifier contains both organization and account name in the format `organization-name.account-name`.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-region-start
          :end-before: .. credential-snowflake-region-end


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: left
          :class: no-scaled-link
     - Before you can configure Amperity Bridge for data sharing with Snowflake you must `create a share in Snowflake <bridge-snowflake-sync-amperity-configure-snowflake-create-share>`, add a secure share identifier to that share, identify the region for your Snowflake account, and add the :ref:`locator ID <bridge-snowflake-sync-amperity-configure-snowflake-account-locator>` for the Amperity account in the same region as your Snowflake account and stack as your Amperity tenant.

       Use the `CURRENT_REGION <https://docs.snowflake.com/en/sql-reference/functions/current_region>`__ |ext_link| function to return the name of the region for the account where the current user is logged in.

       Use the `CURRENT_ACCOUNT <https://docs.snowflake.com/en/sql-reference/functions/current_account>`__ |ext_link| argument in |destination-name| to return the locator ID for your Snowflake account.

       .. important:: When using secure data sharing to share views, Snowflake strongly recommends only :ref:`sharing secure views <bridge-snowflake-sync-amperity-configure-snowflake-secure-views>`. It is not recommended to share `non-secured views <https://docs.snowflake.com/en/user-guide/data-sharing-views#label-sharing-non-secure-view-limitations>`__ |ext_link|.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: left
          :class: no-scaled-link
     - A secure share identifier in Snowflake is a unique string---A-Z, 0-9, $, and _ (underscores)---that is added when creating a share. This string must configured in Amperity to enable the bridge.

       Copy the secure share identifier from the Snowflake user interface, and then share the identifier with the individual who will configure Amperity for secure data sharing with Snowflake.


.. bridge-snowflake-sync-amperity-get-details-end


.. _bridge-snowflake-sync-amperity-configure-snowflake:

Configure Snowflake
--------------------------------------------------

.. bridge-snowflake-sync-amperity-configure-snowflake-start

Before you can configure Amperity Bridge for data sharing with Snowflake you must create a share in Snowflake, add a secure share identifier to that share, and then identify and add the correct account locator.

.. bridge-snowflake-sync-amperity-configure-snowflake-end


.. _bridge-snowflake-sync-amperity-configure-snowflake-create-share:

Create share
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-snowflake-sync-amperity-configure-snowflake-create-share-start

To enable data sharing between Snowflake and Amperity `a share must be created in Snowflake <https://docs.snowflake.com/en/user-guide/data-sharing-provider#using-snowsight-to-create-a-share>`__ |ext_link|. You may `use Snowsight (the Snowflake user interace) to create the share <https://docs.snowflake.com/en/user-guide/data-sharing-provider#creating-a-share>`__ |ext_link|, as described in this topic, or you may use Snowflake SQL, starting with the `CREATE SHARE <https://docs.snowflake.com/en/sql-reference/sql/create-share>`__ |ext_link| command.

.. bridge-snowflake-sync-amperity-configure-snowflake-create-share-end

**To create a share in Snowflake**

.. bridge-snowflake-sync-amperity-configure-snowflake-create-share-steps-start

#. Log in to Snowsight.
#. Select **Data Products**, and then **Private Sharing**.
#. Select **Share**, and then **Create a Direct Share**.
#. For the share, select a source database, along with one or more target objects within the source database.
#. A **Secure Share Identifier** is required for data sharing with Amperity.

   A secure share identifier in Snowflake is a unique string---A-Z, 0-9, $, and _ (underscores)---that is added when creating a share. This string must be configured in Amperity to enable the bridge.

#. Find the :ref:`Amperity account locator ID <bridge-snowflake-sync-amperity-configure-snowflake-account-locator>`, and then add it to the configuration for the **Secure Share Identifier**.

#. Copy the secure share identifier from the Snowflake user interface, and then save the share.

#. Click **Add consumer**, and then configure the share to use the :ref:`Amperity account locator ID <bridge-snowflake-sync-amperity-configure-snowflake-account-locator>` in the same region as the consumer.

.. bridge-snowflake-sync-amperity-configure-snowflake-create-share-steps-end


.. _bridge-snowflake-sync-amperity-configure-snowflake-secure-views:

Configure secure views
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-snowflake-sync-amperity-configure-snowflake-secure-views-start

When using secure data sharing to share views, Snowflake strongly recommends only `sharing secure views <https://docs.snowflake.com/en/user-guide/views-secure#creating-secure-views>`__ |ext_link|. It is not recommended to share `non-secured views <https://docs.snowflake.com/en/user-guide/data-sharing-views#label-sharing-non-secure-view-limitations>`__ with Amperity.

.. bridge-snowflake-sync-amperity-configure-snowflake-secure-views-end


.. _bridge-snowflake-sync-amperity-configure-snowflake-account-locator:

Amperity account locator IDs
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-snowflake-sync-amperity-configure-snowflake-account-locator-start

Snowflake must be configured for the correct `account locator IDs <https://docs.snowflake.com/en/user-guide/admin-account-identifier#format-2-account-locator-in-a-region>`__ |ext_link| used by Amperity. Account locator IDs are specific to the stack in which your Amperity tenant is provisioned *and* the `region ID <https://docs.snowflake.com/en/user-guide/admin-account-identifier#region-ids>`__ |ext_link| in which your Snowflake account resides.

.. list-table::
   :widths: 33 33 34
   :header-rows: 1

   * - Amperity stack
     - Snowflake region
     - Account locator
   * - aws-prod
     - aws_us_west_2
     - GUB98973
   * - aws-prod
     - aws_us_east_1
     - MVB61607
   * - aws-prod
     - aws_us_east_2
     - BL95184
   * - aws-prod
     - azure_westus2
     - PZ39828
   * - az-prod
     - aws_us_west_2
     - BCB42530
   * - az-prod
     - azure_eastus2
     - DSA38111
   * - aws-prod-cc1
     - aws_us_west_2
     - EXB14788
   * - az-prod-en1
     - aws_us_west_2
     - WKB77434

.. important:: If the account ID / region ID pair does ot exist in your stack please contact Amperity Support.

.. bridge-snowflake-sync-amperity-configure-snowflake-account-locator-end


.. _bridge-snowflake-sync-amperity-add-bridge:

Add inbound bridge
--------------------------------------------------

Configure an inbound bridge to sync data from Snowflake to Amperity.
**To add an inbound bridge**

.. bridge-snowflake-sync-amperity-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Sources** page. Under **Inbound shares** click **Add bridge**. 

       Choose **Snowflake**.

       .. image:: ../../images/bridge-inbound-choose-snowflake.png
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
     - Configure the organization, account name, and region.

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-organization-start
          :end-before: .. credential-snowflake-organization-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-account-name-start
          :end-before: .. credential-snowflake-account-name-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-region-start
          :end-before: .. credential-snowflake-region-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Add the **Secure Share Identifier**.

       When finished, click **Continue**. This will open the **Select tables** dialog box.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 4.
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


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - Map the tables that are synced from Snowflake to domain tables in Amperity.

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

       When finished, click **Save and sync**. This will start a workflow that synchronizes data from Snowflake to Amperity and will create the mapped domain table names.

       You can manually sync tables that are synced with Amperity using the **Sync** option from the **Actions** menu for the inbound bridge.

.. bridge-snowflake-sync-amperity-add-bridge-steps-end
