.. https://docs.amperity.com/guides

.. |source-name| replace:: Databricks
.. |destination-name| replace:: Databricks

.. meta::
    :description lang=en:
        Amperity Bridge for Databricks is a first-class integration that uses Delta Sharing to enable bi-directional data access between Amperity and Databricks.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity Bridge for Databricks is a first-class integration that uses Delta Sharing to enable bi-directional data access between Amperity and Databricks.

.. meta::
    :content class=swiftype name=title data-type=string:
        Add Databricks

==================================================
Add Databricks
==================================================

.. TODO: The anchor references in this topic are identical to the anchor references in /operator/bridge_databricks.rst to ensure that reference links work in this topic.

.. include:: ../../amperity_operator/source/bridge_databricks.rst
   :start-after: .. bridge-databricks-about-start
   :end-before: .. bridge-databricks-about-end

.. include:: ../../amperity_operator/source/bridge_databricks.rst
   :start-after: .. bridge-databricks-sync-with-amperity-start
   :end-before: .. bridge-databricks-sync-with-amperity-end

.. include:: ../../amperity_operator/source/bridge_databricks.rst
   :start-after: .. bridge-databricks-audits-and-encryption-start
   :end-before: .. bridge-databricks-audits-and-encryption-end

.. source-databricks-prerequisites-start

.. note:: Review `Connect Amperity Bridge to Databricks <../operator/bridge_databricks.html>`__ for more information about prerequisites, requirements, and optional configurations for |source-name|. This topic assumes that all configuration prerequisites and are finished before stepping through this workflow.

.. source-databricks-prerequisites-start

**To add an inbound bridge**

.. bridge-databricks-sync-with-amperity-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - On the **Identity resolution** page in **Quick start**, from the **Add data source** dropdown select **Databricks**.

       .. image:: ../../images/mockup-guided-idres-source-bridge-databricks.png
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
     - Connect the bridge to Databricks by uploading the credential file that was downloaded from the `activation link <https://docs.databricks.com/en/data-sharing/create-recipient.html#step-2-get-the-activation-link>`__ |ext_link|. There are two ways to upload the credential file:

       #. Uploading the credentials as the second step when adding a bridge. Drop the file into the dialog box or browse to a location on your local machine.
       #. Choosing the **Upload credential** option from the **Actions** menu for a connection.

       After the credential file is uploaded, click **Continue**.

       .. important:: You can download the credential file only once. Recipients should treat the downloaded credential as a secret and must not share it outside of their organization. If you have concerns that a credential may have been handled insecurely, you can `rotate credentials <https://docs.databricks.com/en/data-sharing/create-recipient.html#security-considerations-for-tokens>`__ |ext_link| at any time.

       When finished, click **Continue**. This opens the **Select tables** dialog box.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
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


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Map the tables that are connected from Databricks to domain tables in Amperity.

       .. image:: ../../images/bridge-map-inbound-to-domain.png
          :width: 500 px
          :alt: Map inbound connected tables to domain tables.
          :align: left
          :class: no-scaled-link

       Tables that are connected with Amperity are added as domain tables.

       * The names of connected tables must be unique among all domain tables.
       * Primary keys are not assigned.
       * Semantic tags are not applied.

       .. tip:: Use a custom domain table to assign primary keys, apply semantic tags, and shape data within connected tables to support any of your Amperity workflows.

       When finished, click **Save and sync**. This will start a workflow that synchronizes data from Databricks to Amperity and creates the mapped domain table names.

       You can manually connect tables with Amperity using the **Sync** option from the **Actions** menu for the bridge.

.. bridge-databricks-sync-with-amperity-add-bridge-steps-end


.. _bridge-databricks-data-types:

Data types
==================================================

.. include:: ../../amperity_operator/source/bridge_databricks.rst
   :start-after: .. bridge-databricks-data-types-start
   :end-before: .. bridge-databricks-data-types-end
