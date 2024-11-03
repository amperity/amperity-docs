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

* **Fast setup** Connect Amperity to a data lakehouse in minutes using sharing keys instead of integrations.

* **Zero copy** Control access to shared tables without replicating data across platforms. Build pipelines faster and consolidate your brand's storage costs into a single location.

* **Scalable processing** Enrich massive volumes of data quickly. Data is not moved or transformed from where it resides. Model customer data directly in the data lakehouse or model it in Amperity.

* **Live data** View customer data at rest in a data lakehouse or in Amperity through a shared catalog. Explore and query data without waiting for refreshes or updates.

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

          Open **Learning Lab** to learn more about how `Amperity Bridge <https://learn.amperity.com/amperity-bridge-and-data-warehouses>`__ |ext_link| works. Registration is required.

.. bridge-learning-lab-end


.. _bridge-sync:

Sync data with ...
==================================================

.. bridge-sync-start

Configure Amperity Bridge to sync data with the following cloud databases:

* :ref:`bridge-sync-databricks`

.. bridge-sync-end


.. _bridge-sync-databricks:

Databricks
--------------------------------------------------

.. bridge-sync-databricks-start

Configure inbound and outbound shares in Amperity to enable `bi-directional syncing of data tables between Amperity and Databricks <https://docs.amperity.com/datagrid/bridge_databricks.html>`__. 

.. bridge-sync-databricks-end

.. admonition:: About Delta Sharing

   .. include:: ../../shared/terms.rst
      :start-after: .. term-delta-sharing-start
      :end-before: .. term-delta-sharing-end



.. _bridge-howtos:

How-tos
==================================================

* :ref:`bridge-howto-add-inbound`
* :ref:`bridge-howto-add-outbound`
* :ref:`bridge-howto-add-scheduled-workflow`
* :ref:`bridge-howto-delete`
* :ref:`bridge-howto-download-credentials`
* :ref:`bridge-howto-rename`
* :ref:`bridge-howto-sync`
* :ref:`bridge-howto-upload-credentials`


.. _bridge-howto-add-inbound:

Add inbound bridge
--------------------------------------------------

The steps for adding an inbound bridge depend on the location from which data will be synced to Amperity:

* `Databricks <https://docs.amperity.com/datagrid/bridge_databricks.html#from-databricks>`__


.. _bridge-howto-add-outbound:

Add outbound bridge
--------------------------------------------------

The steps for adding an outbound bridge depend on the location to which data will be synced from Amperity:

* `Databricks <https://docs.amperity.com/datagrid/bridge_databricks.html#to-databricks>`__


.. _bridge-howto-add-scheduled-workflow:

Add bridge to scheduled workflow
--------------------------------------------------

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-howto-add-bridge-start
   :end-before: .. courier-groups-howto-add-bridge-end

**To add a bridge to a scheduled workflow**

.. include:: ../../amperity_reference/source/courier_groups.rst
   :start-after: .. courier-groups-howto-add-bridge-steps-start
   :end-before: .. courier-groups-howto-add-bridge-steps-end


.. _bridge-howto-delete:

Delete a bridge
--------------------------------------------------

.. bridge-howto-delete-start

You may delete any unused bridge.

.. bridge-howto-delete-end

**To delete a bridge**

.. bridge-howto-delete-steps-start

#. Open the **Sources** or **Destinations** page.

#. Do one of the following:

   For an inbound share, from the **Sources** page, under **Inbound share**, select a bridge, and then from the ellipses menu, click **Delete**.

   For an outbound share, from the **Destinations** page, under **Outbound share**, select a bridge, and then from the ellipses menu, click **Delete**.

.. bridge-howto-delete-steps-end


.. _bridge-howto-download-credentials:

Download credentials for an outbound bridge
--------------------------------------------------

.. bridge-howto-download-credentials-start

To sync data from Amperity with a data lakehouse you may need to configure credentials for Amperity within the data lakehouse. You can download these credentials from the Amperity user interface.

.. bridge-howto-download-credentials-end

**To download credentials for a bridge**

.. bridge-howto-download-credentials-steps-start

#. Open the **Destinations** page.

#. From the **Destinations** page, under **Outbound share**, select a bridge, and then from the ellipses menu, click **Download credentials**.

.. bridge-howto-download-credentials-steps-end


.. _bridge-howto-rename:

Rename a bridge
--------------------------------------------------

.. bridge-howto-rename-start

You can rename a bridge.

.. bridge-howto-rename-end

**To rename a bridge**

.. bridge-howto-rename-steps-start

#. Open the **Sources** or **Destinations** page.

#. Do one of the following:

   For an inbound share, from the **Sources** page, under **Inbound share**, select a bridge, and then from the ellipses menu, click **Rename**.

   For an outbound share, from the **Destinations** page, under **Outbound share**, select a bridge, and then from the ellipses menu, click **Rename**.

.. bridge-howto-rename-steps-end


.. _bridge-howto-sync:

Sync a bridge
--------------------------------------------------

.. bridge-howto-sync-start

A sync that is not configured to run as part of a scheduled workflow may be synced manually.

.. bridge-howto-sync-end

**To sync a bridge**

.. bridge-howto-sync-steps-start

#. Open the **Sources** or **Destinations** page.

#. Do one of the following:

   For an inbound share, from the **Sources** page, under **Inbound share**, select a bridge, and then from the ellipses menu, click **Sync**.

   For an outbound share, from the **Destinations** page, under **Outbound share**, select a bridge, and then from the ellipses menu, click **Sync**.

.. bridge-howto-sync-steps-end


.. _bridge-howto-upload-credentials:

Upload credentials for an inbound bridge
--------------------------------------------------

.. bridge-howto-upload-credentials-start

To sync data to Amperity from a data lakehouse you may need to configure credentials for the data lakehouse within Amperity. You can upload these credentials directly from the Amperity user interface.

.. bridge-howto-upload-credentials-end

**To upload credentials for a bridge**

.. bridge-howto-upload-credentials-steps-start

#. Open the **Sources** page.

#. From the **Sources** page, under **Inbound share**, select a bridge, and then from the ellipses menu, click **Upload credentials**.

.. bridge-howto-upload-credentials-steps-end


.. _bridge-howto-view:

View bridge configuration details
--------------------------------------------------

.. bridge-howto-view-start

Configuration details for a bridge can be viewed from the **Sources** and **Destinations** pages.

.. bridge-howto-view-end

**To view configuration details for a bridge**

.. bridge-howto-view-steps-start

#. Open the **Sources** or **Destinations** page.

#. Do one of the following:

   For an inbound share, from the **Sources** page, under **Inbound share**, select a bridge, and then from the ellipses menu, click **View**.

   For an outbound share, from the **Destinations** page, under **Outbound share**, select a bridge, and then from the ellipses menu, click **View**.

.. bridge-howto-delete-steps-end
