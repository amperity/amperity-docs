.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Enable Amperity for predictive modeling.

.. meta::
    :content class=swiftype name=body data-type=text:
        Enable Amperity for predictive modeling.

.. meta::
    :content class=swiftype name=title data-type=string:
        Enable predictive models

==================================================
Enable predictive models
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-predictive-models-start
   :end-before: .. term-predictive-models-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-predictive-attribute-start
   :end-before: .. term-predictive-attribute-end

.. add-predicted-models-caution-start

.. caution:: Predictive models are an optional component of Amperity. If you plan to enable predictive models it is recommended to review the :ref:`data requirements <add-campaigns-data-requirements-fields>`, and then take steps to configure :ref:`columns and tables <add-campaigns-data-requirements-columns-and-tables>` for predictive models *at the same time*.

.. add-predicted-models-caution-end


.. _add-predicted-models-workflow-start:

Predictive models workflow
==================================================

.. add-predicted-models-workflow-start

Predictive models are built outside of Amperity and require data from certain tables in the customer 360 database to be made available to it on a daily basis, after which the results are then pulled to Amperity and the related data science tables are updated.

The steps in the predictive models workflow include:

#. The **Merged Customers**, **Unified Transactions**, and **Unified Itemized Transactions** tables are exported on a daily basis from Amperity to an Amazon S3 bucket that is used for predictive models.
#. Predictive models are run against the **Merged Customers**, **Unified Transactions**, and **Unified Itemized Transactions** tables and the results are returned to the Amazon S3 bucket.
#. A set of couriers are configured to pull these results from the Amazon S3 bucket to your tenant on a daily basis.
#. Predictive models tables are loaded to Amperity using feeds, after which the associated predictive models domain tables are refreshed.
#. After the Stitch process is complete, refreshed predictive models tables are passed through to your customer 360 database.
#. Queries and segments that rely on predictive models table attributes use the refreshed data the next time they are run and any new queries and segments have access to the refreshed data.
#. A campaign uses refreshed data the next time it is scheduled to run.

**Predictive models components**

What components of predictive models are visible within Amperity?

.. list-table::
   :widths: 100 500
   :header-rows: 1

   * - Tab
     - Description
   * - **Sources**
     - Feeds that define the data model for predictive modeling tables within Amperity:

       * **PCLV**
       * **PCLV - Changes**
       * **Predicted Affinity ProductAttribute**
       * **Predicted Affinity Audience ProductAttribute**

       Domain tables that are refreshed on a daily basis:

       * **Predicted Pclv**
       * **Predicted PclvChanges**
       * **Predicted Affinity ProductAttribute**
       * **Predicted Affinity Audience ProductAttribute**.

       Couriers to pull the results of predictive modeling to Amperity on a daily basis:

       * **PCLV** (including **PCLV Changes** and **PCLV Metadata**)
       * **PCLV - Validation**
       * **Predicted Affinity**
       * **Predicted Affinity Audience**

   * - **Customer 360**
     - A series of passthrough database tables:

       * **Predicted CLV Attributes**
       * **Predicted Affinity ProductAttribute**


   * - **Queries**

       and

       **Segments**
     - Access to predictive models attributes from the following tables: :doc:`Predictive pCLV Attributes <table_predicted_clv_attributes>` and :doc:`Affinity (for recommended audiences) <table_predicted_affinity>`. Updated attributes are applied automatically the next time you run the segment or query.

   * - **Destinations**
     - A series of orchestrations that use database exports to send the following tables to predictive models on a daily basis:

       * **Merged Customers**
       * **Unified Itemized Transactions**
       * **Unified Transactions**

.. add-predicted-models-workflow-end


.. _add-predicted-models-verify-prerequisites:

Verify prerequisites
==================================================

Verify that predictive models have :ref:`met all prerequisites <add-campaigns-verify-prerequisites>`.


.. _add-predicted-models-data-requirements:

Data requirements
==================================================

.. add-predicted-models-data-requirements-start

Predictive models have :ref:`the same requirements as segments and campaigns <add-campaigns-data-requirements>`, along with the following additional requirements:

#. Data sources must provide at least four years of historical data to support predictive models; five or more years is recommended. Providing as much historical data as possible improves model performance and prediction quality.
#. A defined product catalog with 20-2000 distinct values is required to support recommended audience sizes for product affinity.

   .. important:: SKU-level recommendations are not supported.

#. If required fields are not available in customer data, maintain the column on the table with NULL values.

.. add-predicted-models-data-requirements-end

.. add-predicted-models-data-requirements-see-also-start

The following sections describe requirements for :ref:`columns and tables <add-predicted-models-data-requirements-columns-and-tables>`, and :ref:`fields <add-predicted-models-data-requirements-fields>`.

.. add-predicted-models-data-requirements-see-also-end


.. _add-predicted-models-data-requirements-columns-and-tables:

Columns and tables
--------------------------------------------------

.. add-predicted-models-data-requirements-columns-and-tables-start

Predictive models use specific columns across the following tables:

* **Merged Customers**
* **Transaction Attributes Extended**
* **Unified Customer**
* **Unified Itemized Transactions**
* **Unified Transactions**

The **Unified Customer** table is built as part of Stitch output when data sources with customer records have profile (PII) semantic tags applied.

The **Transaction Attributes Extended**, **Unified Itemized Transactions**, and **Unified Transactions** are built as part of Stitch output when data sources with interactions records have transactions and itemized transactions semantic tags applied.

The **Merged Customers** table is a version of the **Unified Customer** table that you must build in the customer 360 database to filter profile data. The **Merged Customers** table must be updated to roll-up transactions and itemized transactions.

These tables contain fields that are important components of predictive models.

.. add-predicted-models-data-requirements-columns-and-tables-end


.. _add-predicted-models-data-requirements-fields:

Fields
--------------------------------------------------

.. add-predicted-models-data-requirements-fields-start

The following columns are required by predictive models and must exist in the following tables as an output of the Stitch process or be part of the configuration of the customer 360 database:

.. list-table::
   :widths: 180 200 260
   :header-rows: 1

   * - Column Name
     - Required for
     - Description
   * - **amperity_id**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amperity-id-column-start
          :end-before: .. term-amperity-id-column-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customer**
       * **Unified Itemized Transactions**
       * **Unified Transactions**
       * **Transaction Attributes Extended**

   * - **birthdate**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-birthdate-start
          :end-before: .. term-birthdate-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customer**

   * - **city**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-city-start
          :end-before: .. term-city-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customer**

   * - **country**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-country-start
          :end-before: .. term-country-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customer**

   * - **digital_channel**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-digital-channel-start
          :end-before: .. term-digital-channel-end

       This column must be available from the following tables in the customer 360 database:

       * **Unified Itemized Transactions**
       * **Unified Transactions**

   * - **email**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

       This column must be available from the following table in the customer 360 database:

       * **Merged Customers**

   * - **gender**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-gender-start
          :end-before: .. term-gender-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customer**

   * - **given_name**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customer**

   * - **order_id**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-id-start
          :end-before: .. term-order-id-end

       This column must be available from the following tables in the customer 360 database:

       * **Unified Itemized Transactions**
       * **Unified Transactions**

   * - **order_datetime**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-date-start
          :end-before: .. term-order-date-end

       This column must be available from the following tables in the customer 360 database:

       * **Unified Itemized Transactions**
       * **Unified Transactions**

   * - **order_revenue**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-revenue-start
          :end-before: .. term-order-revenue-end

       This column must be available from the following table in the customer 360 database:

       * **Unified Transactions**

   * - **postal**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customer**

   * - **purchase_brand**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-brand-start
          :end-before: .. term-brand-end

       This column must be available from the following table in the customer 360 database:

       * **Unified Itemized Transactions**
       * **Unified Transactions**

   * - **purchase_channel**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-channel-start
          :end-before: .. term-channel-end

       This column must be available from the following table in the customer 360 database:

       * **Unified Itemized Transactions**
       * **Unified Transactions**

   * - **state**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customer**

   * - **surname**
     - Predictive models
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end

       This column must be available from the following table in the customer 360 database:

       * **Merged Customers**

.. add-predicted-models-data-requirements-fields-end


.. _add-predicted-models-request-to-enable:

Request to enable
==================================================

.. add-predicted-models-request-to-enable-start

After you have configured Amperity for the recommended patterns and workflows for data sources that contain interactions records, segments and campaigns are enabled, and all verification steps have been completed, contact your Amperity representative and request to enable predictive models.

.. add-predicted-models-request-to-enable-end

.. add-predicted-models-request-to-enable-important-start

.. important:: By default, predictive models are fit across all brands for a tenant, even if a tenant has multiple brands. To fit predictions for each brand:

   #. A customer must purchase predictive models for each individual brand.
   #. The tenant must be configured to support brand-specific databases, with a database for each brand with dedicated **Merged Customers**, **Unified Itemized Transactions**, and **Unified Transactions** tables.
   #. A taxonomy that defines product categories and brands.

      This taxonomy must be defined in the **Customer 360** database by extending the **Unified Itemized Transactions** table to include all of the columns that define the taxonomy.

.. add-predicted-models-request-to-enable-important-end

.. add-predicted-models-request-to-enable-process-start

The typical process for setting up predictive models follows a series of general steps:

#. (~1 week) Ensure that data is made available to Amperity that meets the semantic tagging requirements (along with any :ref:`predicted-models-specific fields <add-predicted-models-data-requirements-fields>`), including for transactions, itemized transactions, and product catalog. Use domain SQL to perform pre-Stitch data transforms as necessary.

   Verify that data is being processed correctly to the following tables in the customer 360 database: **Unified Transactions**, **Unified Itemized Transactions**, and **Transaction Attributes Extended**.

#. (~1 week) Amperity begins the process of training the models, validating backtesting, and optimizing predictions.

#. (~1-2 weeks) Amperity performs stability testing on the models and the predictive results. This step may require some tuning of the model and takes longer for very large data sets.

Once this process is complete, the predicted attributes are available on a 1-day delayed rolling basis. These :ref:`tables are added to your tenant as a feed <add-predicted-models-configure>` in the **Sources** page and are available for use with segments and queries.

.. add-predicted-models-request-to-enable-process-end


.. _add-predicted-models-configure:

Configure predictive tables
==================================================

.. add-predicted-models-configure-start

A series of predictive tables is added to your tenant under a feed in the **Sources** page named **Predicted**. This is done as part of the enablement process for predictive models. These tables are refreshed automatically on a daily basis, are not processed by Stitch, and are made available to your customer 360 database, the **Queries** page, and the **Segments** page as passthrough tables:

* **Predicted Affinity ProductAttribute**
* **Predicted Pclv**
* **Predicted PclvChanges**
* **Predicted Affinity Audience ProductAttribute**

where **ProductCategory** is a string that best represents the unique products and brands within your tenant.

#. The **Predicted Pclv** series of tables provides data to the **Predicted CLV Attrbutes** table, which represents the current view of your customer and transaction data.

#. The **Predicted Affinity ProductAttribute** and **Predicted Affinity Audience ProductAttribute** tables are used for product affinity and are associated with the **Affinity** table.

.. add-predicted-models-configure-end

.. add-predicted-models-configure-steps-start

Make the following updates in your customer 360 database:

* :ref:`Add Affinity table <add-predicted-models-configure-affinity>`
* :ref:`Add Predicted CLV Attributes table <add-predicted-models-configure-pclv>`

.. add-predicted-models-configure-steps-end


.. _add-predicted-models-configure-affinity:

Add Affinity table
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-affinity-table-start
   :end-before: .. term-affinity-table-end

.. include:: ../../amperity_operator/source/table_predicted_affinity.rst
   :start-after: .. table-affinity-add-table-about-start
   :end-before: .. table-affinity-add-table-about-end

**To add the Affinity table**

.. include:: ../../amperity_operator/source/table_predicted_affinity.rst
   :start-after: .. table-affinity-add-table-steps-start
   :end-before: .. table-affinity-add-table-steps-end


.. _add-predicted-models-configure-pclv:

Add pCLV attributes table
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-predicted-clv-attributes-table-start
   :end-before: .. term-predicted-clv-attributes-table-end

.. include:: ../../amperity_operator/source/table_predicted_clv_attributes.rst
   :start-after: .. table-predicted-clv-attributes-add-start
   :end-before: .. table-predicted-clv-attributes-add-end

**To add the Predicted CLV Attributes table**

.. include:: ../../amperity_operator/source/table_predicted_clv_attributes.rst
   :start-after: .. table-predicted-clv-attributes-add-as-passthrough-steps-start
   :end-before: .. table-predicted-clv-attributes-add-as-passthrough-steps-end


.. _add-predicted-models-product-catalog:

Define product catalog
==================================================

.. add-predicted-models-product-catalog-start

A product catalog must be defined, and then joined to the **Unified Itemized Transactions** table.

#. A data source must be available with :ref:`product catalog semantic tags <semantics-product-catalogs>` applied.

   .. note:: Amperity documentation refers to this data source as the :doc:`Unified Product Catalog table <table_unified_product_catalog>`, but it may have a different name in your tenant.

#. Apply the **product-id** semantic tag to product catalog data as required by predictive modeling; the **product-category**, **product-description**, and **product-subcategory** semantic tags are optional.

   .. important:: Product affinity modeling requires the field that defines product categories -- **product-category** in the **Unified Product Catalog** table -- to contain between 20 and 2000 unique values.

#. A list of custom attributes may be defined. These must be available as columns in the **Customer 360** database and must be added to the **Unified Itemized Transactions** table.

#. Tables that define :ref:`product catalog semantic tags <semantics-product-catalogs>` and custom attributes are managed as a data source and should be maintained as part of your organization's regular Amperity workflow.

Extend the **Unified Itemized Transactions** to include the taxonomy that defines your products and brands:

#. Add the column to which the **product-id** semantic tag was applied
#. Add other columns to which product catalog semantic tags were applied
#. Add any columns that define custom attributes, as necessary

The following example extends the **Unified Itemized Transactions** table using a table named **Unified Product Catalog** that has columns for each of the optional product catalog semantic tags:

.. code-block:: sql
   :linenos:

   SELECT
     uit.*
     ,upc.product_category AS `product_category`
     ,upc.product_description AS `product_description`
     ,upc.product_subcategory AS `product_subcategory`
   FROM Unified_Itemized_Transactions uit
   LEFT JOIN Unified_Product_Catalog upc ON uit.product_id = upc.product_id

Some brands require a single parameter to define a taxonomy and some require more than one. The following example shows a taxonomy that defines custom attributes for a class and subclass:

.. code-block:: sql
   :linenos:

   SELECT 
     uit.*,
     ,product_class AS `product_class`
     ,product_subclass AS `product_subclass`
   FROM Unified_Itemized_Transactions uit
   LEFT JOIN Product_Metadata pm ON uit.product_id = pm.product_id
   WHERE uit.is_return IS NULL AND uit.is_cancellation IS NULL
   AND uit.item_revenue >= 0

.. important:: Every brand is unique. Discuss with your Amperity representative how to extend the **Unified Itemized Transactions** table to support the taxonomy that is required for your products and brands.

.. add-predicted-models-product-catalog-end


.. _add-predicted-models-configure-edit-customer360:

Add pCLV attributes to Customer360 table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-customer360-table-start
   :end-before: .. term-customer360-table-end

.. add-predicted-models-configure-edit-customer360-start

You must edit the **SELECT** statement in the **Customer 360** table to select attributes from the **Predicted CLV Attributes** table.

.. add-predicted-models-configure-edit-customer360-end

**To add predictive models table attributes to the Customer 360 table**

.. add-predicted-models-configure-edit-customer360-steps-start

#. From the **Customer 360** page, under **All Databases**, open the menu for the customer 360 database, and then select **Edit**. The **Database Editor** page opens.
#. Select the **Customer 360** table.
#. Edit the **Customer 360** table to update the **SELECT** statement for attributes from the **Predicted CLV Attributes** table, similar to:

   .. code-block:: sql
      :linenos:

      -- Predicted Attributes from Predicted_CLV_Attributes pa
      ,pa.predicted_probability_of_transaction_next_365d AS `predicted_probability_of_transaction_next_365d`
      ,pa.predicted_order_frequency_next_365d AS `predicted_order_frequency_next_365d`
      ,pa.predicted_average_order_revenue_next_365d AS `predicted_average_order_revenue_next_365d`
      ,pa.predicted_clv_next_365d AS `predicted_clv_next_365d`
      ,pa.historical_order_frequency_lifetime AS `historical_order_frequency_lifetime`
      ,pa.days_since_last_order AS `days_since_last_order`
      ,pa.predicted_customer_lifecycle_status AS `predicted_customer_lifecycle_status`
      ,pa.predicted_customer_lifetime_value_tier AS `predicted_customer_lifetime_value_tier`

#. Add a **LEFT JOIN** for the **Predicted CLV Attributes** table below the **FROM** clause, similar to:

   .. code-block:: sql

      LEFT JOIN Predicted_CLV_Attributes pa ON pa.amperity_id = mc.amperity_id

#. Click **Next**.
#. Click the icon or empty space in the **Icon** column to open the **Select an Icon** dialog box, after which you can choose an icon or search for additional icons on the `Font Awesome <https://fontawesome.com/v5/search>`__ |ext_link| website.

   .. include:: ../../shared/databases.rst
      :start-after: .. databases-font-awesome-picker-useany-start
      :end-before: .. databases-font-awesome-picker-useany-end

#. Click **Save**.
#. Click **Activate**.
#. Run the customer 360 database.

.. add-predicted-models-configure-edit-customer360-steps-end
