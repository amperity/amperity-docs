.. https://docs.amperity.com/guides

.. |source-name| replace:: Snowflake
.. |destination-name| replace:: Snowflake

.. meta::
    :description lang=en:
        Amperity Bridge for Snowflake is a first-class integration that uses secure data sharing to enable bi-directional data access between Amperity and Snowflake.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity Bridge for Snowflake is a first-class integration that uses secure data sharing to enable bi-directional data access between Amperity and Snowflake.

.. meta::
    :content class=swiftype name=title data-type=string:
        Add Snowflake

==================================================
Add Snowflake
==================================================

.. TODO: The anchor references in this topic are identical to the anchor references in /operator/bridge_snowflake.rst to ensure that reference links work in this topic.

.. include:: ../../amperity_operator/source/bridge_snowflake.rst
   :start-after: .. bridge-snowflake-about-start
   :end-before: .. bridge-snowflake-about-end

.. include:: ../../amperity_operator/source/bridge_snowflake.rst
   :start-after: .. bridge-snowflake-what-is-data-sharing-start
   :end-before: .. bridge-snowflake-what-is-data-sharing-end

.. source-snowflake-prerequisites-start

.. note:: Review `Connect Amperity Bridge to Snowflake <../operator/bridge_snowflake.html>`__ for more information about prerequisites, requirements, and optional configurations for |source-name|. This topic assumes that all configuration prerequisites and are finished before stepping through this workflow.

.. source-snowflake-prerequisites-start

**To add an inbound bridge**

.. bridge-snowflake-sync-amperity-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - On the **Identity resolution** page in **Quick start**, from the **Add data source** dropdown select **Snowflake**.

       .. image:: ../../images/mockup-guided-idres-source-bridge-snowflake.png
          :width: 500 px
          :alt: Add a data source.
          :align: left
          :class: no-scaled-link

       This opens the **Add bridge** dialog box.

       .. image:: ../../images/bridge-inbound-name-description.png
          :width: 500 px
          :alt: Add a bridge for a connection.
          :align: left
          :class: no-scaled-link

       Add a name and description for the bridge *or* select an existing bridge, and then click **Confirm**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
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
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Add the **Secure Share Identifier**.

       When finished, click **Continue**. This opens the **Select tables** dialog box.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Use the **Select tables** dialog box to select any combination of schemas and tables to be connected to Amperity.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

       If you select a schema, all tables in that schema will be connected. Any new tables added later need to be manually added to the connection. 

       When finished, click **Next**. This opens the **Domain table mapping** dialog box.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Map the tables that are connected from Snowflake to domain tables in Amperity.

       .. image:: ../../images/bridge-map-inbound-to-domain.png
          :width: 500 px
          :alt: Map connected tables to domain tables.
          :align: left
          :class: no-scaled-link

       Tables that are connected with Amperity are added as domain tables.

       * The names of connected tables must be unique among all domain tables.
       * Primary keys are not assigned.
       * Semantic tags are not applied.

       .. tip:: Use a custom domain table to assign primary keys, apply semantic tags, and shape data within connected tables to support any of your Amperity workflows.

       When finished, click **Save and sync**. This will start a workflow that synchronizes data from Snowflake to Amperity and creates the mapped domain table names.

       You can manually sync tables that are connected with Amperity using the **Sync** option from the **Actions** menu for the inbound bridge.

.. bridge-snowflake-sync-amperity-add-bridge-steps-end


.. _bridge-snowflake-data-types:

Data types
==================================================

.. include:: ../../amperity_operator/source/bridge_snowflake.rst
   :start-after: .. bridge-databricks-data-types-start
   :end-before: .. bridge-databricks-data-types-end
