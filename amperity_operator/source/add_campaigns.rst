.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Enable segments and campaigns for your Amperity tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Enable segments and campaigns for your Amperity tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        Enable segments and campaigns


.. TODO: adjust for a world where Activations tab replaces Campaigns in all tenants

==================================================
Enable activations
==================================================

.. add-campaigns-steps-start

Amperity provides a set of features--the **Campaigns** page, segment insights, and predictive attributes--to help you understand your customer's preferences and behaviors, and then to make better informed decisions as to how often you choose to interact with them.

.. add-campaigns-steps-end

.. add-campaigns-important-start

.. important:: You must have already configured Amperity using the recommended patterns and workflows for:

   #. :doc:`Customer profiles <add_customer_data>`, which contain profile and PII data for individual customers.
   #. :doc:`Transactions <add_transactions>`, which contain transactions, itemized transactions, and product catalogs that, when compared to customer records, identify how your customers interacted with your brands.

   Please refer to those topics for more information about how to configure customer records and interaction records as data sources for use with segments and campaigns.

.. add-campaigns-important-end


.. _add-campaigns-enablement-steps:

Steps to enable
==================================================

.. add-campaigns-steps-caution-start

.. caution:: Predictive modeling is an optional component of Amperity. If you plan to enable predictive modeling it is recommended to review the :ref:`data requirements <add-campaigns-data-requirements-fields>`, and then take steps to configure :ref:`columns and tables <add-campaigns-data-requirements-columns-and-tables>` for predictive modeling.

.. add-campaigns-steps-caution-end

.. add-campaigns-steps-links-start

The following sections describe the process for enabling segments and campaigns for your tenant:

#. :ref:`Verify prerequisites <add-campaigns-verify-prerequisites>`
#. :ref:`Enable segments <add-campaigns-assign-database-tables-to-vse>`
#. :ref:`Review enabled features <add-campaigns-review-features>`

.. add-campaigns-steps-links-end


.. _add-campaigns-verify-prerequisites:

Verify prerequisites
==================================================

.. add-campaigns-verify-prerequisites-tip-start

.. tip:: If you followed the steps for configuring :doc:`customer profiles <add_customer_data>` and :doc:`transactions <add_transactions>` verifying prerequisites may be a formality.

   If your tenant has been on Amperity for a while and wants to enable segments and campaigns, you should review all data sources, Stitch results, and customer data tables to ensure that all of those components meet all requirements.

.. add-campaigns-verify-prerequisites-tip-end

.. add-campaigns-verify-prerequisites-start

Verify each of the following items to ensure that Amperity is ready for enablement:

#. Data sources that contain customer records have profile semantic tags applied and each of those data sources run successfully from the **Sources** page.

#. Data sources that contain interaction records have semantic tag groupings applied for transactions, itemized transactions, and product catalogs, as appropriate and that each of those data sources are configured from the **Sources** page.

   .. note:: Interactions records may require the use of domain SQL to ensure that all fields that require semantic tags are present in the data.

#. All data sources are processed successfully by Stitch.

#. Stitch output includes the following tables specific to interactions records: **Transaction Attributes Extended**, **Unified Itemized Transactions**, and **Unified Transactions**.

#. The customer 360 database contains passthrough tables for **Transaction Attributes Extended**.

   .. tip:: Add passthrough tables in the customer 360 database for each table that was defined in the **Sources** page using domain SQL.

#. The **Unified Itemized Transactions** table is added as a SQL table.

#. The **Unified Transactions** table is added as a SQL table, into which attributes from the **Unified Itemized Transactions** table are rolled up.

#. The **Customer 360** table is updated to select attributes from the **Transaction Attributes Extended** table.

#. The **Customer 360** table is updated to select attributes from other tables that you want to associate with segments and campaigns, such as for loyalty programs.

#. Stitch QA has been performed against customer records and Transactions QA has been performed against interactions records. This should be thorough enough to understand that the data quality in the current customer 360 database is accurate and ready for predictive attribute modeling.

   .. note:: The Stitch QA effort is not a one-time effort. It should be performed as an ongoing activity, complete with individual inspection of query results as necessary, to ensure that the quality of the data is maintained over time.

.. add-campaigns-verify-prerequisites-end


.. _add-campaigns-data-requirements:

Data requirements
==================================================

.. add-campaigns-data-requirements-start

Amperity has the following requirements for segments and campaigns:

#. Data sources that contain interaction records--customer orders, items purchased by customers, products, brands, preferences, etc.--must be made available to Amperity.
#. Data sources should allow for applying semantic tags to support transactions and itemized transactions, either directly to the feed or after reshaping the interaction records with domain SQL.
#. All required tables are present, along with all of the required fields for each table.

   The **Merged Customers** table must have fields for given name, surname, birthdate, city, state, postal, and loyalty membership.

   The **Unified Transactions** table must have fields for order dates and times, order revenue, order quantity, order discount amount, purchase channel, brand channel, digital channel, and store ID.

   .. note:: Required fields for which there is no historical data should be added to the tables and should be configured to have **NULL** values.

#. Validation of revenue numbers. Compare the revenue numbers the customer expects to the revenue numbers that Amperity shows after processing all data to the customer 360 database. These numbers should be in alignment, though may not need to be exact.

#. Enable automated validations for transactions. Open the database in edit mode, and then under **Features** enable the **AmpIQ** option. This enables automatic validations for transactions data. Run the database, and then view the validation report. In the notification for the database run click **Customer 360 validation report**. Resolve issues that are highlighted in the report.

.. add-campaigns-data-requirements-end

.. add-campaigns-data-requirements-caution-for-predictive-modeling-start

.. caution:: If you are planning to use predictive modeling, please review the :ref:`data requirements for predictive modeling <add-predicted-models-data-requirements>`.

.. add-campaigns-data-requirements-caution-for-predictive-modeling-end

.. add-campaigns-data-requirements-see-also-start

The following sections describe requirements for :ref:`columns and tables <add-campaigns-data-requirements-columns-and-tables>`, :ref:`fields <add-campaigns-data-requirements-fields>`, and :ref:`additional data requirements <add-campaigns-data-requirements-supporting-data-sources>`.

.. add-campaigns-data-requirements-see-also-start


.. _add-campaigns-data-requirements-columns-and-tables:

Columns and tables
--------------------------------------------------

.. add-campaigns-data-requirements-columns-and-tables-start

Amperity uses specific columns across the following tables to enable features to support segments and campaigns:

* **Merged Customers**
* **Transaction Attributes Extended**
* **Unified Customers**
* **Unified Scores**
* **Unified Transactions**

The **Unified Customers** and **Unified Scores** tables are built as part of Stitch output when data sources with customer records have profile (PII) semantic tags applied.

The **Transaction Attributes Extended** and **Unified Transactions** are built as part of Stitch output when data sources with interactions records have transactions and itemized transactions semantic tags applied.

The **Merged Customers** table is a version of the **Unified Customers** table that you must build in the customer 360 database to filter profile data. The **Merged Customers** table must be updated to roll-up transactions and itemized transactions.

.. note:: Ask your Amperity representative to add the **Campaign Recipients** table and enable it for your tenant.

.. add-campaigns-data-requirements-columns-and-tables-end


.. _add-campaigns-data-requirements-fields:

Fields
--------------------------------------------------

.. add-campaigns-data-requirements-fields-start

The fields required by segments and campaigns fall into three broad categories:

* Demographic fields include details such as gender, age, and location. Demographic fields help marketers understand the segments to which their customers belong.
* Product fields include details about individual products, such as brand, department, and categories. Product fields help marketers understand which products their customers prefer.
* Channel and location fields include details about how the customer chose a certain product, such as digital, in-store, and online. Channel and location fields help marketers understand from where a customer chose to purchase a product or a service. 

The following table describes the fields that are required by column name, which component requires them, and the table (or tables) from which they are available. Columns that are required by predictive modeling are optional for tenants that do not plan to enable that feature.

.. important:: You must tag interactions records with transactions and itemized transactions semantic tags. Use domain SQL to reshape data sources to meet specific data requirements before applying those semantic tags as necessary.

.. add-campaigns-data-requirements-fields-end

.. add-campaigns-data-requirements-fields-table-start

The following columns must exist in the following tables as an output of the Stitch process or be part of the configuration of the customer 360 database:

.. list-table::
   :widths: 180 200 260
   :header-rows: 1

   * - Column Name
     - Required for
     - Description
   * - **address**
     - **Campaigns** page

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address-start
          :end-before: .. term-address-end

       This column must be available from the following table in the customer 360 database:

       * **Merged Customers**

   * - **amperity_id**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amperity-id-column-start
          :end-before: .. term-amperity-id-column-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**
       * **Unified Transactions**
       * **Transaction Attributes Extended**

   * - **birthdate**
     - *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-birthdate-start
          :end-before: .. term-birthdate-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **city**
     - **Campaigns** page

       *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-city-start
          :end-before: .. term-city-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **country**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-country-start
          :end-before: .. term-country-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **digital_channel**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-digital-channel-start
          :end-before: .. term-digital-channel-end

       This column must be available from the following tables in the customer 360 database:

       * **Unified Transactions**

   * - **email**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

       This column must be available from the following table in the customer 360 database:

       * **Merged Customers**

   * - **gender**
     - *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-gender-start
          :end-before: .. term-gender-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **given_name**
     - **Campaigns** page

       *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **item_discount_amount**
     - Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-discount-amount-start
          :end-before: .. term-item-discount-amount-end

   * - **order_id**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-id-start
          :end-before: .. term-order-id-end

       This column must be available from the following tables in the customer 360 database:

       * **Unified Transactions**

   * - **order_datetime**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-date-start
          :end-before: .. term-order-date-end

       This column must be available from the following tables in the customer 360 database:

       * **Unified Transactions**

   * - **order_revenue**
     - *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-revenue-start
          :end-before: .. term-order-revenue-end

       This column must be available from the following table in the customer 360 database:

       * **Unified Transactions**

   * - **phone**
     - **Campaigns** page

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

       This column must be available from the following table in the customer 360 database:

       * **Merged Customers**

   * - **postal**
     - **Campaigns** page

       *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **product_category**
     - **Campaigns** page

       Segment insights
     - 

   * - **product_id**
     - **Campaigns** page
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-product-id-start
          :end-before: .. term-product-id-end

   * - **purchase_brand**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-brand-start
          :end-before: .. term-brand-end

       This column must be available from the following table in the customer 360 database:

       * **Unified Transactions**

   * - **purchase_channel**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-channel-start
          :end-before: .. term-channel-end

       This column must be available from the following table in the customer 360 database:

       * **Unified Transactions**

   * - **state**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end

       This column must be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **surname**
     - **Campaigns** page

       *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end

       This column must be available from the following table in the customer 360 database:

       * **Merged Customers**

.. add-campaigns-data-requirements-fields-table-end


.. _add-campaigns-data-requirements-supporting-data-sources:

Additional data sources
--------------------------------------------------

.. add-campaigns-data-requirements-supporting-data-sources-start

Additional data should be made available to Amperity beyond what is provided to support the basic requirements for segments and campaigns. Additional data will improve the quality of the downstream workflows that are available and increases your ability to identify the right customer segments and profiles for which you run campaigns.

The following types of data are recommended to be made available to Amperity as additional data sources:

#. Product information that contains details about categories, subcategories, and departments.

#. Channel information that contains details about purchases (in-store and online), channel types (digital, direct, and organic), social engagement (Facebook, Twitter, Pinterest, etc.), and first-party data (Google Analytics and Adobe Analytics).

#. Specific demographics data, such as age, state, country, and gender. This type of data may already available from customer records that have made available to Amperity.

   However, this information is often available from data sources that are not ideal for identity resolution. These data sources are still usable and can be configured as passthrough tables to your customer 360 database.

   Another useful type of demographics data is one that provides detailed data about and across a broad collection of consumer categories. For example, Mosaic USA segments from Experian are a good choice for providing rich demographics data to Amperity.

#. Contact information that provides downstream campaigns the ability to contact the customer. This type of data may be in the form of an opt-in email list or it may be in the form of a list of addresses to which you can send direct mail.

.. important:: None of these types of additional data sources have a strict requirement. When determining if additional data sources should be made available to Amperity, consider the following:

   #. What product categories does your marketing team typically use to make decisions?
   #. What types of channels are used to determine budget allocation?
   #. What types of demographic data do you use to better understand your customers?
   #. What type of information does your company typically use to determine how to segment customers?
   #. What types of attributes are important for your customer segments?

.. add-campaigns-data-requirements-supporting-data-sources-end


.. _add-campaigns-assign-database-tables-to-vse:

Enable visual segments
==================================================

.. add-campaigns-assign-database-tables-to-vse-start

.. important:: Only tables that contain the Amperity ID *and* have been configured for use within the **Segment Editor** will be available to the **Segments** page.

.. add-campaigns-assign-database-tables-to-vse-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-visual-segment-editor-start
   :end-before: .. term-visual-segment-editor-end

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-allow-tables-in-segments-start
   :end-before: .. databases-database-howto-allow-tables-in-segments-end

**To enable visual segments**

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-allow-tables-in-segments-steps-start
   :end-before: .. databases-database-howto-allow-tables-in-segments-steps-end


.. _add-campaigns-review-features:

Review features
==================================================

.. add-campaigns-review-features-start

After segments and campaigns are enabled, the following features are available in Amperity:

* The **Segments** page.
* The **Campaigns** page.

.. add-campaigns-review-features-end
