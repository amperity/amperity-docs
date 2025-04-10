.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure Amperity to send data to Tableau.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Tableau.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Tableau

==================================================
Send data to Tableau
==================================================

.. destination-tableau-start

Many organizations use Tableau to enable its users -- data analysts, data scientists, and business users -- to explore data, discover insights, and share the results in a visual way across across the organization.

Tableau connects to Amperity data indirectly. You must first configure Amperity to send the results of a query or a database export to any of the following cloud-based data warehouses:

* :doc:`Amazon Redshift <destination_tableau_amazon_redshift>`
* :doc:`Azure Synapse Analytics <destination_tableau_azure_synapse_analytics>`
* :doc:`Databricks <destination_tableau_databricks>`
* :doc:`Google BigQuery <destination_tableau_google_big_query>`
* :doc:`Snowflake <destination_tableau_snowflake>`

after which you can connect Tableau to that data, and then start building dashboards and charts, analyzing data, defining stories, and enabling any other data visualization use case your organization requires.

.. image:: ../../images/destination-tableau-generic.png
   :width: 600 px
   :alt: Connect Tableau to your data warehouse.
   :align: left
   :class: no-scaled-link

All workflows that make data available to Tableau should be configured to update automatically on a daily (or weekly) schedule. This ensures that users in your organization who will work in Tableau always have access to the latest data.

.. destination-tableau-end

.. destination-tableau-bi-connect-start

.. admonition:: About the Amperity Data Warehouse

   Amperity offers additional services that allow Amperity to run as the Amperity Data Warehouse, also referred to as BI Connect, which is synchronized to your Amperity tenant. (This is, currently, run as a Snowflake data warehouse that is accessible to only your Amperity tenant.) Tableau may be configured to connect directly to the Amperity Data Warehouse. Or you may send data directly to Snowflake by configuring the Snowflake destination to send data to your Snowflake tenant.

   #. :ref:`Request to enable the Business Intelligence Connect data warehouse <destination-bic-request-to-enable>`
   #. :ref:`Send data to the data warehouse <destination-bic-send-to-data-warehouse>`
   #. :ref:`Use SSO to access the data warehouse <destination-bic-send-to-data-warehouse-sso>`
   #. :ref:`Connect Tableau Desktop <destination-bic-connect-to-tableau>`

.. destination-tableau-bi-connect-end
