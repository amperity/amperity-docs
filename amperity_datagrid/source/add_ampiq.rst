.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Enable AmpIQ features---segments and campaigns---for your Amperity tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Enable AmpIQ features---segments and campaigns---for your Amperity tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        Enable AmpIQ


==================================================
Enable AmpIQ
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-ampiq-start
   :end-before: .. term-ampiq-end

.. ampiq-important-start

.. important:: This topic assumes that you have already configured Amperity using the recommended patterns and workflows for:

   #. :doc:`Customer profiles <add_customer_profiles>`, which contain profile and PII data for individual customers.
   #. :doc:`Transactions <add_transactions>`, which contain transactions, itemized transactions, and product catalogs that, when compared to customer records, identify how your customers interacted with your brands.

   Please refer to those topics for more information about how to configure customer records and interaction records as data sources for use with AmpIQ.

.. ampiq-important-end


.. _ampiq-enablement-steps:

Steps to enable
==================================================

.. ampiq-enablement-steps-start

AmpIQ provides a set of features--the **Campaigns** page, segment insights, and predictive attributes that help you understand your customer's preferences and behaviors, and then to make better informed decisions as to how often you choose to interact with them.

AmpIQ must be enabled by your Amperity representative after customer records and interaction records are loaded to Amperity and are configured correctly within your customer 360 database.

.. ampiq-enablement-steps-end

.. ampiq-enablement-steps-caution-start

.. caution:: Predictive modeling is an optional component of AmpIQ. If you plan to enable predictive modeling for AmpIQ it is recommended to review the :ref:`data requirements <ampiq-data-requirements-fields>`, and then take steps to configure :ref:`columns and tables <ampiq-data-requirements-columns-and-tables>` for predictive modeling *at the same time* as for AmpIQ.

.. ampiq-enablement-steps-caution-end

.. ampiq-enablement-steps-links-start

The following sections describe the process for enabling AmpIQ for your tenant:

#. :ref:`Verify prerequisites <ampiq-enablement-verify-prerequisites>`
#. :ref:`Request to enable AmpIQ <ampiq-enablement-request-to-enable>`
#. :ref:`Enable segments <ampiq-enablement-assign-database-tables-to-vse>`
#. :ref:`Review enabled features <ampiq-enablement-review-features>`

Please work closely with your Amperity representative during this process.

.. ampiq-enablement-steps-links-end


.. _ampiq-enablement-verify-prerequisites:

Verify prerequisites
==================================================

.. ampiq-enablement-verify-prerequisites-tip-start

.. tip:: If you closely followed the steps for configuring :doc:`customer profiles <add_customer_profiles>` and :doc:`transactions <add_transactions>` this section may be a formality. If your tenant has been on Amperity for a while and is moving to AmpIQ, you should carefully review of all data sources, Stitch results, and customer data tables to ensure that all of those components meet the requirements for AmpIQ.

.. ampiq-enablement-verify-prerequisites-tip-end

.. ampiq-enablement-verify-prerequisites-start

Verify each of the following items to ensure that AmpIQ is ready for enablement:

#. Data sources that contain customer records have profile semantic tags applied and each of those data sources run successfully from the **Sources** page.

#. Data sources that contain interaction records have semantic tag groupings applied for transactions, itemized transactions, and product catalogs, as appropriate and that each of those data sources are configured from the **Sources** page.

   .. note:: Interactions records may require the use of domain SQL to ensure that all fields that require semantic tags are present in the data.

#. All data sources are processed successfully by Stitch.

#. Stitch output includes the following tables specific to interactions records: **Transaction Attributes**, **Transaction Attributes Extended**, **Unified Itemized Transactions**, and **Unified Transactions**.

#. The customer 360 database contains passthrough tables for  **Transaction Attributes**, and **Transaction Attributes Extended**.

   .. tip:: Add passthrough tables in the customer 360 database for each table that was defined in the **Sources** page using domain SQL.

#. The **Unified Itemized Transactions** table is added as a SQL table.

#. The **Unified Transactions** table is added as a SQL table, into which attributes from the **Unified Itemized Transactions** table are rolled up.

#. The **Customer 360** table is updated to select attributes from the **Transaction Attributes** table.

#. The **Customer 360** table is updated to select attributes from other tables that you want to associate with AmpIQ, such as for loyalty programs.

#. Stitch QA has been performed against customer records and Transactions QA has been performed against interactions records. This should be thorough enough to understand that the data quality in the current customer 360 database is accurate and ready for predictive attribute modeling.

   .. note:: The Stitch QA effort is not a one-time effort. It should be performed as an ongoing activity, complete with individual inspection of query results as necessary, to ensure that the quality of the data is maintained over time.

.. ampiq-enablement-verify-prerequisites-end


.. _ampiq-data-requirements:

Data requirements
==================================================

.. ampiq-data-requirements-start

AmpIQ has the following requirements:

#. Data sources that contain interaction records--customer orders, items purchased by customers, products, brands, preferences, etc.--must be made available to Amperity.
#. Data sources should allow for applying semantic tags to support transactions and itemized transactions, either directly to the feed or (more likely) after reshaping the interaction records with domain SQL.
#. All required tables are present, along with all of the required fields for each table.

   The **Merged Customers** table must have fields for given name, surname, birthdate, city, state, postal, and loyalty membership.

   The **Unified Transactions** table must have fields for orders (date and time, revenue, quantity, and discount amount), purchases (brand and channel), digital channel, and store ID.

   .. important:: The **Unified Itemized Transactions** table is not a requirement for AmpIQ; however, it is a requirement for :ref:`using predictive modeling <add-predicted-models-data-requirements>` with AmpIQ.

   .. note:: Required fields for which there is no historical data should be added to the tables and should be configured to have **NULL** values.

#. Validation of revenue numbers. Compare the revenue numbers the customer expects to the revenue numbers that Amperity shows after processing all data to the customer 360 database. These numbers should be in alignment, though may not need to be exact.

#. Enable automated validations for transactions. Open the database in edit mode, and then under **Features** enable the **AmpIQ** option. This enables automatic validations for transactions data. Run the database, and then view the validation report. In the notification for the database run click **Customer 360 validation report**. Resolve issues that are highlighted in the report.

.. ampiq-data-requirements-end

.. ampiq-data-requirements-caution-for-predictive-modeling-start

.. caution:: If you are planning to use predictive modeling with AmpIQ, please review the :ref:`data requirements for predictive modeling prior to enabling AmpIQ <add-predicted-models-data-requirements>`.

.. ampiq-data-requirements-caution-for-predictive-modeling-end

.. ampiq-data-requirements-see-also-start

The following sections describe requirements for :ref:`columns and tables <ampiq-data-requirements-columns-and-tables>`, :ref:`fields <ampiq-data-requirements-fields>`, and :ref:`additional data requirements <ampiq-data-requirements-supporting-data-sources>`.

.. ampiq-data-requirements-see-also-start


.. _ampiq-data-requirements-columns-and-tables:

Columns and tables
--------------------------------------------------

.. ampiq-data-requirements-columns-and-tables-start

AmpIQ uses specific columns across the following tables to enable features within AmpIQ:

* **Merged Customers**
* **Transaction Attributes**
* **Unified Customers**
* **Unified Scores**
* **Unified Transactions**

The **Unified Customers** and **Unified Scores** tables are built as part of Stitch output when data sources with customer records have profile (PII) semantic tags applied.

The **Transaction Attributes** and **Unified Transactions** are built as part of Stitch output when data sources with interactions records have transactions and itemized transactions semantic tags applied.

The **Merged Customers** table is a version of the **Unified Customers** table that you must build in the customer 360 database to filter profile data. The **Merged Customers** table must be updated to roll-up transactions and itemized transactions.

These tables contain fields that are important to components of AmpIQ.

.. note:: Ask your Amperity representative to add the **Campaign Recipients** table and enable it for your tenant.

.. ampiq-data-requirements-columns-and-tables-end


.. _ampiq-data-requirements-fields:

Fields
--------------------------------------------------

.. ampiq-data-requirements-fields-start

The fields required by AmpIQ fall into three broad categories:

* Demographic fields include details such as gender, age, and location. Demographic fields help marketers understand the segments to which their customers belong.
* Product fields include details about individual products, such as brand, department, and categories. Product fields help marketers understand which products their customers prefer.
* Channel and location fields include details about how the customer chose a certain product, such as digital, in-store (and store location), and online. Channel and location fields help marketers understand from where a customer chose to purchase a product or a service. 

The following table describes the fields that are required by components of AmpIQ by column name, which component requires them, and the table (or tables) from which they are available. Columns that are required by predictive modeling are optional for tenants that do not plan to enable that feature of AmpIQ.

.. important:: You must tag interactions records with transactions and itemized transactions semantic tags. Use domain SQL to reshape data sources to meet specific data requirements before applying those semantic tags as necessary.

.. ampiq-data-requirements-fields-end

.. ampiq-data-requirements-fields-table-start

The following columns must exist in the following tables as an output of the Stitch process or be part of the configuration of the customer 360 database:

.. list-table::
   :widths: 180 200 260
   :header-rows: 1

   * - Column Name
     - Required for ...
     - Description
   * - **address**
     - **Campaigns** page

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address-start
          :end-before: .. term-address-end

       AmpIQ expects this column to be available from the following table in the customer 360 database:

       * **Merged Customers**

   * - **amperity_id**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amperity-id-column-start
          :end-before: .. term-amperity-id-column-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**
       * **Unified Transactions**
       * **Transaction Attributes**

   * - **birthdate**
     - *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-birthdate-start
          :end-before: .. term-birthdate-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **city**
     - **Campaigns** page

       *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-city-start
          :end-before: .. term-city-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **country**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-country-start
          :end-before: .. term-country-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **digital_channel**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-digital-channel-start
          :end-before: .. term-digital-channel-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Unified Transactions**

   * - **email**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

       AmpIQ expects this column to be available from the following table in the customer 360 database:

       * **Merged Customers**

   * - **gender**
     - *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-gender-start
          :end-before: .. term-gender-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **given_name**
     - **Campaigns** page

       *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

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

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Unified Transactions**

   * - **order_datetime**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-date-start
          :end-before: .. term-order-date-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Unified Transactions**

   * - **order_revenue**
     - *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-revenue-start
          :end-before: .. term-order-revenue-end

       AmpIQ expects this column to be available from the following table in the customer 360 database:

       * **Unified Transactions**

   * - **phone**
     - **Campaigns** page

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

       AmpIQ expects this column to be available from the following table in the customer 360 database:

       * **Merged Customers**

   * - **postal**
     - **Campaigns** page

       *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

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

       AmpIQ expects this column to be available from the following table in the customer 360 database:

       * **Unified Transactions**

   * - **purchase_channel**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-channel-start
          :end-before: .. term-channel-end

       AmpIQ expects this column to be available from the following table in the customer 360 database:

       * **Unified Transactions**

   * - **state**
     - **Campaigns** page

       *Predictive modeling*

       Segment insights
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end

       AmpIQ expects this column to be available from the following tables in the customer 360 database:

       * **Merged Customers**
       * **Unified Customers**

   * - **surname**
     - **Campaigns** page

       *Predictive modeling*
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end

       AmpIQ expects this column to be available from the following table in the customer 360 database:

       * **Merged Customers**

.. ampiq-data-requirements-fields-table-end


.. _ampiq-data-requirements-supporting-data-sources:

Additional data sources
--------------------------------------------------

.. ampiq-data-requirements-supporting-data-sources-start

Additional data should be made available to Amperity beyond what is provided to support the basic requirements for AmpIQ. Additional data will improve the quality of the downstream workflows that are available to you from within AmpIQ and will increase your ability to identify the right customer segments and profiles for which you will run campaigns.

The following types of data are recommended to be made available to Amperity as additional data sources that support AmpIQ:

#. Product information that contains details about categories, subcategories, and departments.

#. Channel information that contains details about purchases (in-store and online), channel types (digital, direct, and organic), social engagement (Facebook, Twitter, Pinterest, etc.), and first-party data (Google Analytics and Adobe Analytics).

#. Specific demographics data, such as age, state, country, and gender. This type of data may already available from customer records that have made available to Amperity.

   However, this information is often available from data sources that are not ideal for identity resolution. These data sources are still usable for AmpIQ and can be configured as passthrough tables to your customer 360 database.

   Another useful type of demographics data is one that provides detailed data about and across a broad collection of consumer categories. For example, Mosaic USA segments from Experian are a good choice for providing rich demographics data to Amperity for supporting AmpIQ.

#. Contact information that provides downstream campaigns the ability to contact the customer. This type of data may be in the form of an opt-in email list or it may be in the form of a list of addresses to which you can send direct mail.

.. important:: None of these types of additional data sources have a strict requirement for AmpIQ. When determining if additional data sources should be made available to Amperity, consider the following:

   #. What product categories does your marketing team typically use to make decisions?
   #. What types of channels are used to determine budget allocation?
   #. What types of demographic data do you use to better understand your customers?
   #. What type of information does your company typically use to determine how to segment customers?
   #. What types of attributes are important for your customer segments?

.. ampiq-data-requirements-supporting-data-sources-end


.. _ampiq-enablement-request-to-enable:

Request to enable AmpIQ
==================================================

.. ampiq-enablement-request-to-enable-start

Ask your Amperity representative to enable AmpIQ features, including the **Campaigns** page, and updates to the **Segments** page that enable segment insights and recommended segments.

.. note:: Your Amperity representative will let you know when this step is completed.

.. ampiq-enablement-request-to-enable-end


.. _ampiq-enablement-assign-database-tables-to-vse:

Enable visual segments
==================================================

.. ampiq-enablement-assign-database-tables-to-vse-start

.. important:: Only tables that contain the Amperity ID *and* have been configured for use within the **Segment Editor** will be available to the **Segments** page.

.. ampiq-enablement-assign-database-tables-to-vse-end

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


.. _ampiq-enablement-review-features:

Review AmpIQ features
==================================================

.. ampiq-enablement-review-features-start

After AmpIQ is enabled, the following features are available in Amperity:

* The **Segments** page.
* The **Campaigns** page.

.. ampiq-enablement-review-features-end
