.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Add data sources that contain PII to Amperity and build customer profiles.

.. meta::
    :content class=swiftype name=body data-type=text:
        Add data sources that contain PII to Amperity and build customer profiles.

.. meta::
    :content class=swiftype name=title data-type=string:
        Add customer data

==================================================
Add customer data
==================================================

.. setup-customer-profiles-start

Amperity relies on data sources that contain personally identifiable information (PII) about your customers to build customer profiles.

For each data source that your brand makes available to Amperity that contains PII:

#. :ref:`Apply customer profile semantic tags to individual fields within data sources <setup-customer-profiles-apply-semantics>`
#. :ref:`Run input validations <setup-customer-profiles-input-validations>`
#. :ref:`Make domain tables that contain PII available to Stitch <setup-customer-profiles-stitch>`
#. :ref:`Build your brand's customer 360 database <setup-customer-profiles-build-database>`
#. :ref:`Activate database <setup-customer-profiles-activate-database>`

.. setup-customer-profiles-end


.. _setup-customer-profiles-apply-semantics:

Apply semantics
==================================================

.. setup-customer-profiles-apply-semantics-start

Use a feed or custom domain table to apply customer profile semantic tags to every data source that contains personally identifiable information (PII) about your customers.

Customer profile semantic tags include **address**, **birthdate**, **city**, **email**, **gender**, **given-name**, **phone**, **postal**, **state**, and **surname**. Apply them to individual fields within data sources to define a common schema across customer profiles in your customer 360 database.

Customer profile semantic tags do not require you to make any changes to the schemas that exist within an incoming data sources.

When a feed is activated, Amperity loads the data from the data source into a domain table.

.. setup-customer-profiles-apply-semantics-end

.. setup-customer-profiles-apply-semantics-multibrand-start

.. admonition:: Multi-brand databases

   To support multi-brand databases, you must ensure that a **brand** column exists within the data source. This enables filtering customer profiles by brand. Adding a **brand** column may require using a custom domain table.

.. setup-customer-profiles-apply-semantics-multibrand-end


.. _setup-customer-profiles-input-validations:

Review validations
==================================================

.. include:: ../../amperity_operator/source/validate_inputs.rst
   :start-after: .. validate-inputs-overview-start
   :end-before: .. validate-inputs-overview-end

.. setup-customer-profiles-validations-start

:doc:`Input validations <validate_inputs>` are run against domain tables that have been published, and then made available to the **Queries** page. Use input validation reports help your brand discover data quality issues with email addresses, phone numbers, and transactions.

.. setup-customer-profiles-validations-end

.. include:: ../../amperity_operator/source/validate_inputs.rst
   :start-after: .. validate-inputs-overview-note-start
   :end-before: .. validate-inputs-overview-note-end

.. _setup-customer-profiles-input-validations-checklist:

**Checklist for input validations**

.. setup-customer-profiles-stitch-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Review customer profile reports**

       .. include:: ../../amperity_operator/source/validate_inputs.rst
          :start-after: .. validate-inputs-review-reports-customer-profiles-start
          :end-before: .. validate-inputs-review-reports-customer-profiles-end

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Review transaction reports**

       .. include:: ../../amperity_operator/source/validate_inputs.rst
          :start-after: .. validate-inputs-review-reports-transactions-start
          :end-before: .. validate-inputs-review-reports-transactions-end

.. setup-customer-profiles-stitch-checklist-end


.. _setup-customer-profiles-stitch:

Run Stitch
==================================================

.. setup-customer-profiles-stitch-start

Stitch runs on a daily basis after all of your brand's data sources have provided refreshed data. This updates your brand's unified customer profiles and refreshes the transactions and engagment data that is associated with each unique customer profile.

.. setup-customer-profiles-stitch-end


.. _setup-customer-profiles-stitch-checklist:

**STITCH CHECKLIST**

.. setup-customer-profiles-stitch-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Make domain tables available to Stitch**

       All domain tables in which customer profile semantic tags were applied to one or more fields should be made available to Stitch.

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Run Stitch**

       Stitch evaluates all of the data to which customer profiles were applied and builds a unified customer profile for all of your customers, including linking each customer's interactions with your brand to their customer profile.

       .. tip:: Use courier groups to configure Amperity to run Stitch automatically.

.. setup-customer-profiles-stitch-checklist-end


.. _setup-customer-profiles-build-database:

Build database
==================================================

.. setup-customer-profiles-build-database-start

Your customer 360 database must be configured before you can use customer profiles to build audiences that support your brand's use cases and downstream workflows.

.. important:: Most of the work required to build your customer 360 database happens during initial configuration.

   Depending on the types of data sources your brand adds to Amperity over time, you may need to make specific changes to specific tables in your customer 360 database to support these updates.

   For example, if your brand adds a data source that contains PII you may need to update the source and field priorities that are defined in the **Merged Customers** table.

The initial configuration of your customer 360 database requires using SQL to add or extend a series of tables that are the foundation of your brand's set of unified customer profiles.

#. :ref:`Unified Coalesced <setup-customer-profiles-build-database-table-uc>`
#. :ref:`Best email address <setup-customer-profiles-build-database-table-best-email>`
#. :ref:`Merged Customers <setup-customer-profiles-build-database-table-mc>`
#. :ref:`Customer 360 <setup-customer-profiles-build-database-table-c360>`

Your customer 360 database is typically refreshed on a daily basis, after Stitch has finished the process of analyzing and updating your customer profiles.

.. setup-customer-profiles-build-database-end


.. _setup-customer-profiles-build-database-table-uc:

Unified coalesced
--------------------------------------------------

.. setup-customer-profiles-build-database-table-uc-start

The **Unified Coalesced** table is an output of the Stitch identity resolution process. This table is refreshed every time Stitch runs and contains one row for each unique record from every data source that contains customer PII.

Individual rows within the **Unified Coalesced** table may not represent complete profiles. For example:

* Row 1 contains details from data source A and has customer email addresses, first and last names, and postal codes
* Row 2 contains details from data source B and has phone numbers and first names
* Row 3 contains details from data source C and has first and last names, postal codes, and phone numbers

Each row within the **Unified Coalesced** table is assigned an Amperity ID.

.. setup-customer-profiles-build-database-table-uc-end


.. _setup-customer-profiles-build-database-table-uc-checklist:

**UNIFIED COALESCED CHECKLIST**

.. setup-customer-profiles-build-database-table-uc-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Initial configuration only**

       The **Unified Coalesced** table is added to your customer 360 database as part of the "Customer 360" database template. The table is refreshed automatically after every Stitch run.

   * - .. image:: ../../images/checklist-multibrand.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Multi-brand databases only**

       To support multi-brand databases, you must update the customer 360 database to use the multi-brand SQL template for the **Unified Coalesced** table.

.. setup-customer-profiles-build-database-table-uc-checklist-end


.. _setup-customer-profiles-build-database-table-best-email:

Best email address
--------------------------------------------------

.. setup-customer-profiles-build-database-table-best-email-start

The **Email Ampid Assignment** table identifies the best email address to use for each customer profile in the **Merged Customers** table. This configuration is enabled by default and is configurable.

.. setup-customer-profiles-build-database-table-best-email-end

.. _setup-customer-profiles-build-database-table-best-email-checklist:

**Checklist for best email address**

.. setup-customer-profiles-build-database-table-best-email-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Initial configuration only**

       Add the :doc:`Email Ampid Assignemnt <table_email_ampid_assignment>` table to your customer 360 database. Use the **SQL** build mode option, and then select "Email Ampid Assigment" from the **Template** dropdown.

   * - .. image:: ../../images/checklist-caution.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Optional. Use email priority instead of Amperity ID assignment**

       The following steps are necessary to :ref:`update the Merged_Customers table to use email address priority and completion values <table-merged-customers-undo-ampid-assignment>` instead of the best email address identified by the **Email Ampid Assignment** table:

       .. include:: ../../amperity_operator/source/table_merged_customers.rst
          :start-after: .. table-merged-customers-undo-ampid-assignment-links-start
          :end-before: .. table-merged-customers-undo-ampid-assignment-links-end

.. setup-customer-profiles-build-database-table-best-email-checklist-end


.. _setup-customer-profiles-build-database-table-mc:

Merged customers
--------------------------------------------------

.. setup-customer-profiles-build-database-table-mc-start

The **Merged Customers** table contains one row for each Amperity ID in the **Unified Coalesced** table.

Individual rows within the **Merged Customers** table represent unique customer profiles. This is done by collapsing all of the rows in the **Unified Coalesced** table that share the same Amperity ID into a single row.

.. setup-customer-profiles-build-database-table-mc-end


.. _setup-customer-profiles-build-database-table-mc-checklist:

**MERGED CUSTOMERS CHECKLIST**

.. setup-customer-profiles-build-database-table-mc-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Initial configuration only**

       :ref:`Add the Merged Customers table <table-merged-customers-add-table>` to your customer 360 database. Use the **SQL** build mode option, and then select "Merged Customers" from the **Template** dropdown.

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Repeat for all data sources that contain PII**

       A data source that is made available to Stitch may be :ref:`assigned a value for source priority <table-merged-customers-sql-query-required-update-source-priority>`. An integer value will assign priority, where 1 has a higher priority than 2. Domain tables may be assigned the same priority.

       For each data source that is made available to Stitch, review the source priority section in the **Merged Customers** table and verify that each data source is assigned a source priority.

       Tables that are not included in the source priority list are assigned a 999 priority.

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **Repeat for all data sources that contain PII**

       A data source that is made available to Stitch may :ref:`assign field priorities for names, physical addresses, email addresses, birthdates, and gender <table-merged-customers-sql-query-required-update-field-priority>`.

       A NULL field priority value uses the source priority value as the field priority value.

       An integer priority value takes precedence over source priority when the field priority value is higher than the source priority value.

       The list of tables defined for field priority should be the same as the list of tables defined for source priority.

       For each data source that is made available to Stitch, review the field priority section in the **Merged Customers** table and verify that each field within a data source is assigned a field priority.

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - **Configure best email address**

       Narrow the many-to-many relationships between Amperity IDs and email addresses down to a one-to-one relationship, and then :ref:`make that email address available <table-merged-customers-undo-ampid-assignment>` to a customer profile in the **Merged Customers** table.

       .. important:: The **Email Ampid Assignment** table determines the best email address to be associated with each unique customer in the **Merged Customers** table.

.. setup-customer-profiles-build-database-table-mc-checklist-end


.. _setup-customer-profiles-build-database-table-c360:

Customer 360
--------------------------------------------------

.. setup-customer-profiles-build-database-table-c360-start

The **Customer 360** table contains all of your brand's unified customer profiles combined with the individual actions each of your customers have had with your brand.

Individual rows within the **Customer 360** table represent customer profiles and their interactions with your brand, unique by Amperity ID.

.. setup-customer-profiles-build-database-table-c360-end


.. _setup-customer-profiles-build-database-table-c360-checklist:

**CUSTOMER 360 CHECKLIST**

.. setup-customer-profiles-build-database-table-c360-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Initial configuration only**

       :ref:`Add the Customer 360 table <table-customer360-add>` to your customer 360 database. Use the **SQL** build mode option, and then select "Customer 360" from the **Template** dropdown.

       *- or -*

       You may extend the **Customer 360** table to include attributes from the **Unified Transactions** and **Transaction Attributes Extended** tables.

       Use the **SQL** build mode option, select "Customer 360 with Transaction Attributes" from the **Template** dropdown, and then uncomment the attributes you want to include. You may add any attribute in the **Unified Transactions** and **Transaction Attributes Extended** tables to the **Customer 360** table.

   * - .. image:: ../../images/checklist-caution.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Optional. Extend for custom attributes**

       You may extend the **Customer 360** table to include attributes that may be required by downstream use cases.

       For example, adding :ref:`hashed email addresses or hashed phone numbers <table-customer360-add-hashed-columns>`.

.. setup-customer-profiles-build-database-table-c360-checklist-end


.. _setup-customer-profiles-activate-database:

Activate database
==================================================

.. setup-customer-profiles-run-database-start

To make data available in your customer 360 database you must activate, and then run the database. This is typically done manually during initial configuration, after which the process is automated to run on a daily basis after Stitch has finished updating customer profiles.

.. setup-customer-profiles-run-database-end

**ACTIVATE DATABASE CHECKLIST**

.. setup-customer-profiles-run-database-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-multibrand.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Multi-brand databases only**

       Use the **SQL** build mode option, select "Database Key" from the **Template** dropdown, and then configure the SQL in that template to support the brand that should be associated with this customer 360 database.

       .. important:: Add the **Database Key** table *before* running the customer 360 database.

       .. caution:: Multi-brand databases also require using a multi-brand SQL template for the **Unified Itemized Transactions** table. That table should be configured before running the customer 360 database. You can extend the **Unified Itemized Transactions** table after, but should finish extending that table before you use the initial customer 360 database as a template for each multi-brand database.

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Run the customer 360 database**

       Active, and then run the customer 360 database. After the run is complete review the output for each table.

.. setup-customer-profiles-run-database-checklist-end


.. _setup-customer-profiles-more-customer-data:

More customer data
==================================================

.. setup-customer-profiles-more-customer-data-start

Many brands add data sources to their tenant over time. Adding new data sources follows the same steps that were used for previous sources. More data sources help Amperity build better profiles *and* helps your brand undersand how the records in individual data sources match with your most valuable customers. This is true even when new data sources are of lower quality than the data sources you originally provided to Amperity.

.. setup-customer-profiles-more-customer-data-end
