.. https://docs.amperity.com/guides/

:orphan:

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
        Add Google BigQuery

==================================================
Add Google BigQuery
==================================================

.. TODO: The anchor references in this topic are identical to the anchor references in /operator/bridge_google_bigquery.rst to ensure that reference links work in this topic.

.. include:: ../../amperity_operator/source/bridge_google_bigquery.rst
   :start-after: .. bridge-google-bigquery-about-start
   :end-before: .. bridge-google-bigquery-about-end

.. include:: ../../amperity_operator/source/bridge_google_bigquery.rst
   :start-after: .. bridge-google-bigquery-what-is-bigquery-sharing-start
   :end-before: .. bridge-google-bigquery-what-is-bigquery-sharing-end

.. source-google-bigquery-prerequisites-start

.. note:: Review `Connect Amperity Bridge to Google BigQuery <../operator/bridge_google_bigquery.html>`__ for more information about prerequisites, requirements, and optional configurations for |source-name|. All configuration prerequisites must be completed before stepping through this workflow.

.. source-google-bigquery-prerequisites-start

**To add an inbound bridge for Google BigQuery**

.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - On the **Identity resolution** page in **Quick start**, from the **Add data source** dropdown select **Google BigQuery**.

       .. image:: ../../images/mockup-guided-idres-source-bridge-google-bigquery.png
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
     - Add the share link that was copied from the |source-name| data exchange.

       Amperity generates the subscriber link *after* the share link has been configured. The share link is a URL similar to:

       ::

          https://console.cloud.google.com/bigquery/ \
          analytics-hub/exchanges/projects/123456789012/ \
          locations/<location>/dataExchanges/<exchange>/ \
          listings/<listing>

       Configure this identifier in |source-name| as the subscriber for the data listing.


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
     - Map the tables that are connected from |source-name| to domain tables in Amperity.

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

       When finished, click **Save and sync**. This will start a workflow that connects data from |source-name| to Amperity and creates the mapped domain table names.

       You can manually sync tables that are connected with Amperity using the **Sync** option from the **Actions** menu for the inbound bridge.


.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-steps-end


.. _bridge-google-bigquery-data-typesa:

Data types
==================================================

.. include:: ../../amperity_operator/source/bridge_google_bigquery.rst
   :start-after: .. bridge-google-bigquery-data-types-start
   :end-before: .. bridge-google-bigquery-data-types-end
