.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Add transactions data to your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Add transactions data to your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        Add transactions data

==================================================
Add transactions data
==================================================

.. setup-transactions-intro-start

Transactions are a type of interaction record that contain information about your customers' purchase histories with your brand. For example: what they purchased, when they purchased, how many items were purchased, how much money was spent, how often they made a purchase, and the locations from which each purchase was made.

.. setup-transactions-intro-end

.. setup-transactions-start

The process for adding transaction records to Amperity requires individual data sources that provide order-level, item-level, and product catalog data. The actual steps will vary from tenant to tenant, depending on how the individual data sources provide data for canceled and returned items, quantities, discounts, and revenue.

At a high level, start with deciding how to apply semantic tags to your brand's transaction records. After you have run Stitch you will then configure a series of tables that associate each transaction with a customer profile.

.. setup-transactions-end

.. setup-transactions-start

For each data source that your brand makes available to Amperity that contains transactions:

#. :ref:`Apply transactions semantic tags <setup-transactions-apply-semantics>`
#. :ref:`Review input validations <setup-transactions-input-validations>`
#. :ref:`Associate to customer profiles <setup-transactions-associate-to-profiles>`
#. :ref:`Extend database for transactions <setup-transactions-add-transaction-tables>`
#. :ref:`Configure optional attributes <setup-transactions-extend-attributes>`
#. :ref:`Refresh database <setup-transactions-refresh-database>`
#. :ref:`Review C360 validations <setup-transactions-validate-database>`
#. :ref:`Enable segments and campaigns <setup-transactions-enable-segments-and-campaigns>`

.. setup-transactions-end


.. _setup-transactions-apply-semantics:

Apply semantics
==================================================

.. setup-customer-profiles-apply-semantics-start

You should plan to use a custom domain table to apply |semantics_transactions_long| to data sources that contains transactions data.

Transaction semantics include a set of required semantic tags --- **is-cancellation**, **is-return**, **item-quantity**, **item-revenue**, **order-datetime**, **order-discount-amount**, **order-id**, **product-id**, **purchase-brand**, **purchase-channel**, and **store-id** --- along with a set of optional semantic tags, such as **item-cost** and **item-revenue**.

.. important:: All transaction semantic tags are prefixed with **txn-item/**. For example: **txn-item/order-datetime**.

Apply these semantic tags to individual fields within data sources that describe the products your customers have purchased from your brand.

.. setup-customer-profiles-apply-semantics-end

.. setup-customer-profiles-apply-semantics-multibrand-start

.. admonition:: Multi-brand databases

   To support multi-brand databases, you must ensure that a **brand** column exists within each data source. This enables filtering transactions by brand. Adding a **brand** column for transactions data should be done using a custom domain table.

.. setup-customer-profiles-apply-semantics-multibrand-end


.. _setup-transactions-apply-semantics-purchase:

Purchase histories
--------------------------------------------------

.. database-interactions-apply-to-itemized-transactions-start

For each incoming data source that contains item-level data, you should plan to use the domain SQL editor to reshape the data into a schema against which individual transaction semantic tags can be applied.

.. database-interactions-apply-to-itemized-transactions-end

.. database-interactions-apply-to-itemized-transactions-tip-start

.. tip:: Use a custom domain table per data source to shape the data, and then apply semantic tags. This will make it easier to find specific transaction records when troubleshooting data quality issues.

.. database-interactions-apply-to-itemized-transactions-tip-end

.. database-interactions-apply-to-itemized-transactions-important-start

.. important:: Itemized transactions must be transformed in way that allows each row to represent a distinct transaction for a given item for a given order:

   #. A row for each purchase.
   #. A row for each return.
   #. A row for each cancellation.

.. database-interactions-apply-to-itemized-transactions-important-end


.. _setup-transactions-apply-semantics-product-catalogs:

Product catalogs
--------------------------------------------------

.. setup-transactions-apply-semantics-product-catalogs-start

Use **txn-item/pc** semantic tags--a subset of **txn-item/** semantic tags--when your brand wants to use your product catalog for segmentation, building audiences, and sending product catalog data alongside (or as part of) audiences. These tags add your brand's product catalog to the **Unified Itemized Transactions** table alongside your customers' purchase histories.

In some cases, you may need to use the domain SQL editor to reshape the data into a schema to which product catalog semantic tags can be applied.

.. setup-transactions-apply-semantics-product-catalogs-end


.. _setup-transactions-input-validations:

Review validations
==================================================

.. include:: ../../amperity_operator/source/validate_inputs.rst
   :start-after: .. validate-inputs-overview-start
   :end-before: .. validate-inputs-overview-end

.. setup-transactions-validations-start

:doc:`Input validations <validate_inputs>` are run against domain tables that have been published, and then made available to the **Queries** page. Use input validation reports help your brand discover data quality issues with email addresses, phone numbers, and transactions.

.. setup-transactions-validations-end

.. include:: ../../amperity_operator/source/validate_inputs.rst
   :start-after: .. validate-inputs-overview-note-start
   :end-before: .. validate-inputs-overview-note-end

.. _setup-transactions-input-validations-checklist:

**INPUT VALIDATIONS CHECKLIST**

.. setup-transactions-stitch-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - **Review customer profile reports**

       .. include:: ../../amperity_operator/source/validate_inputs.rst
          :start-after: .. validate-inputs-review-reports-customer-profiles-start
          :end-before: .. validate-inputs-review-reports-customer-profiles-end

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - **Review transaction reports**

       .. include:: ../../amperity_operator/source/validate_inputs.rst
          :start-after: .. validate-inputs-review-reports-transactions-start
          :end-before: .. validate-inputs-review-reports-transactions-end

.. setup-transactions-stitch-checklist-end


.. _setup-transactions-associate-to-profiles:

Associate to profiles
==================================================

.. setup-transactions-associate-to-profiles-start

Use a :ref:`foreign key <semantics-key-foreign>` to :ref:`link transaction records to customer records <semantics-key-foreign-link-transactions>`. A transaction record will inherit the Amperity ID of a customer profile when both share the same foreign key.

.. setup-transactions-associate-to-profiles-end


.. _setup-transactions-add-transaction-tables:

Extend database
==================================================

.. setup-transactions-add-transaction-tables-start

Extend your customer 360 database for transactions by adding the following tables:

#. :ref:`Itemized transactions <setup-transactions-extend-database-uit>`
#. :ref:`Unified transactions <setup-transactions-extend-database-ut>`
#. :ref:`Extended attributes <setup-transactions-extend-database-tae>`

.. setup-transactions-add-transaction-tables-end

.. setup-transactions-add-transaction-tables-important-start

.. important:: Most of the work required to extend your customer 360 database for transaction histories and product catalogs happens one time.

   Depending on the types of data sources your brand adds to Amperity over time, you may need to make specific changes to specific tables in your customer 360 database to support these updates. For example, if your brand adds a data source that contains PII you may need to update the source and field priorities that are defined in the **Merged Customers** table.

   The initial configuration of your customer 360 database requires using SQL to add or extend a series of tables that are an extension that captures the interactions your brand has with your customers.

.. setup-transactions-add-transaction-tables-important-end


.. _setup-transactions-extend-database-uit:

Itemized transactions
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-itemized-transactions-table-start
   :end-before: .. term-unified-itemized-transactions-table-end

.. _setup-transactions-build-database-table-uit-checklist:

**UNIFIED ITEMIZED TRANSACTIONS CHECKLIST**

.. setup-transactions-build-database-table-uit-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - **Initial configuration only**

       .. include:: ../../amperity_operator/source/table_unified_itemized_transactions.rst
          :start-after: .. table-unified-itemized-transactions-add-start
          :end-before: .. table-unified-itemized-transactions-add-end

       Review the list of semantic tags that are available for **txn-items/** and ensure that data sources that contain your brand's purchase histories for your customers have these tags applied.


   * - .. image:: ../../images/checklist-multibrand.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - **Multi-brand databases only**

         Switch to multi-brand template:

         .. code-block:: sql

            SELECT
              uit.*
            FROM Unified_Itemized_Transactions uit
            INNER JOIN Database_Key dk
            ON uit.purchase_brand = dk.purchase_brand


   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - **Initial configuration only**

       .. include:: ../../amperity_operator/source/table_unified_itemized_transactions.rst
          :start-after: .. table-unified-itemized-transactions-add-start
          :end-before: .. table-unified-itemized-transactions-add-end

.. setup-transactions-build-database-table-uit-checklist-end


.. _setup-transactions-extend-database-ut:

Unified transactions
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-transactions-table-start
   :end-before: .. term-unified-transactions-table-end

.. _setup-transactions-build-database-table-ut-checklist:

**UNIFIED TRANSACTIONS CHECKLIST**

.. setup-transactions-build-database-table-ut-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - **Pre-requisite**

       The **Unified Itemized Transactions** table must be available to your customer 360 database.


   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - **Initial configuration only**

       Add the :ref:`Unified Transactions table <table-unified-transactions-add>` to your customer 360 database.


   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - **Initial configuration only**

       Review the :ref:`list of optional attributes <table-unified-transactions-extend-attributes>` to determine which attributes should be enabled for your tenant.

.. setup-transactions-build-database-table-ut-checklist-end


.. _setup-transactions-extend-database-tae:

Extended attributes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-transaction-attributes-extended-table-start
   :end-before: .. term-transaction-attributes-extended-table-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-start
   :end-before: .. data-tables-transaction-attributes-extended-end

.. _setup-transactions-build-database-table-tae-checklist:

**TRANSACTION ATTRIBUTES EXTENDED CHECKLIST**

.. setup-transactions-build-database-table-tae-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - **Pre-requisite**

       The **Unified Transactions** table must be configured and activated in your customer 360 database.


   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - **Initial configuration only**

       Add the :ref:`Transaction Attributes Extended table <table-transaction-attributes-extended-add>` to your customer 360 database.


   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - **Initial configuration only**

       Review the :ref:`list of optional attributes <table-transaction-attributes-extended-extend-attributes>` to determine which attributes should be enabled for your tenant.

.. setup-transactions-build-database-table-tae-checklist-end


.. _setup-transactions-extend-attributes:

Optional attributes
==================================================

.. setup-transactions-extend-attributes-start

You can extend the set of attributes that are available from the **Unified Transactions** and **Transaction Attributes Extended** tables to include any of the following:

* :ref:`setup-transactions-extend-attributes-cancellations`
* :ref:`setup-transactions-extend-attributes-fiscal-calendars`
* :ref:`setup-transactions-extend-attributes-net-order-revenue`
* :ref:`setup-transactions-extend-attributes-order-costs`
* :ref:`setup-transactions-extend-attributes-order-discount-amounts`
* :ref:`setup-transactions-extend-attributes-returns`
* :ref:`setup-transactions-extend-attributes-rfm`

.. note:: These attributes are built into the SQL templates for the **Unified Transactions** and **Transaction Attributes Extended** tables, but are commented out. Some sets of attributes require updates be made to both tables, while others may only require updates be made to one table. Some sets allow for additional customization.

.. setup-transactions-extend-attributes-end


.. _setup-transactions-extend-attributes-cancellations:

Cancellations
--------------------------------------------------

.. TODO: Needs an intro.

**To add extended attributes for canceled items**

.. setup-transactions-extend-attributes-cancellations-steps-start

#. Required. Apply the **is-cancellation** semantic tag to transaction data sources that contain data for canceled items.
#. Optional. :ref:`Extended attributes for canceled items attributes may be added to the Transaction Attributes Extended table <table-transaction-attributes-extended-extend-attributes-cancellations>`.

.. setup-transactions-extend-attributes-cancellations-steps-end


.. _setup-transactions-extend-attributes-fiscal-calendars:

Fiscal calendars
--------------------------------------------------

.. term-fiscal-calendar-start

A fiscal calendar is a yearly accounting period that aligns the weeks and months in a calendar year with holidays and a brand's marketing goals to align the business for an entire calendar year. A common fiscal calendar used by brands is the 4-5-4 fiscal calendar.

.. term-fiscal-calendar-end

.. term-454-calendar-start

A 4-5-4 calendar divides years into months using a 4 weeks - 5 weeks - 4 weeks pattern. Each week starts on a Sunday and ends on a Saturday. Each quarter has the same number of days. A 4-5-4 calendar can be useful for comparing like days for sales reporting purposes.

.. term-454-calendar-end

**To add fiscal calendar attributes**

.. setup-transactions-extend-attributes-fiscal-calendars-steps-start

#. Pre-requisite. Apply fiscal calendar attributes to a data source that contains the data that defines your brand's fiscal calendar.
#. Optional. :ref:`Extended attributes for fiscal calendars may be added to the Transaction Attributes Extended table <table-transaction-attributes-extended-extend-attributes-net-order-revenue>`.

.. setup-transactions-extend-attributes-fiscal-calendars-steps-end


.. _setup-transactions-extend-attributes-net-order-revenue:

Net order revenue
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-net-order-revenue-start
   :end-before: .. term-net-order-revenue-end

**To add attributes for Net Order Revenue**

.. setup-transactions-extend-attributes-net-order-revenue-steps-start

#. Required. :ref:`Add Net Order Revenue to the Unified Transactions table <table-unified-transactions-extend-attributes-net-order-revenue>`.
#. Optional. :ref:`Extended attributes for calculated net order revenue may be added to the Transaction Attributes Extended table <table-transaction-attributes-extended-extend-attributes-net-order-revenue>`.

.. setup-transactions-extend-attributes-net-order-revenue-steps-end


.. _setup-transactions-extend-attributes-order-costs:

Order costs
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-cost-start
   :end-before: .. term-order-cost-end

**To add attributes for Order Cost**

.. setup-transactions-extend-attributes-order-costs-steps-start

#. Required. :ref:`Add Order Cost to the Unified Transactions table <table-unified-transactions-extend-attributes-order-costs>`.
#. Optional. :ref:`Extended attributes for calculated order cost attributes may be added to the Transaction Attributes Extended table <table-transaction-attributes-extended-extend-attributes-order-costs>`.

.. setup-transactions-extend-attributes-order-costs-steps-end


.. _setup-transactions-extend-attributes-order-discount-amounts:

Order discount amounts
--------------------------------------------------

.. include:: ../../amperity_operator/source/table_unified_transactions.rst
   :start-after: .. table-unified-transactions-extend-attributes-order-discount-amounts-start
   :end-before: .. table-unified-transactions-extend-attributes-order-discount-amounts-end

.. include:: ../../amperity_operator/source/table_unified_transactions.rst
   :start-after: .. table-unified-transactions-extend-attributes-order-discount-amounts-list-start
   :end-before: .. table-unified-transactions-extend-attributes-order-discount-amounts-list-end


.. _setup-transactions-extend-attributes-returns:

Returns
--------------------------------------------------

.. TODO: Needs an intro.

**To add extended attributes for returned items**

.. setup-transactions-extend-attributes-returns-steps-start

#. Required. Apply the **is-return** semantic tag to transaction data sources that contain data for returned items.
#. Optional. :ref:`Extended attributes for returned items attributes may be added to the Transaction Attributes Extended table <table-transaction-attributes-extended-extend-attributes-returns>`.

.. setup-transactions-extend-attributes-returns-steps-end


.. _setup-transactions-extend-attributes-rfm:

RFM
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-rfm-start
   :end-before: .. term-rfm-end

.. setup-transactions-extend-attributes-rfm-start

You can :ref:`extend the Transaction Attributes Extended table to include calculated attributes for RFM scores <table-transaction-attributes-extended-extend-attributes-rfm>`.

.. setup-transactions-extend-attributes-rfm-end


.. _setup-transactions-refresh-database:

Refresh database
==================================================

.. setup-transactions-refresh-database-start

To associate purchase histories with customer profiles apply transaction semantic tags to data sources that contain purchase histories, and then refresh the database. This is typically done manually during initial configuration, after which the process is automated to run on a daily basis after Stitch has finished updating customer profiles.

.. setup-transactions-refresh-database-end

**REFRESH DATABASE CHECKLIST**

.. setup-transactions-refresh-database-checklist-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/checklist-multibrand.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - **Run Stitch**

       You must run Stitch to associate purchase histories with customer profiles.

       .. important:: Data tables that contain purchase histories and not customer PII should not be made available to Stitch. The Stitch process evaluates your customers' purchase histories, and then identifies which purchases should be associated to each unique customer profile.

          The results are added to the **Unified Itemized Transactions** table, which associates your customer's Amperity ID to their purchase history. A row exists in the **Unified Itemized Transactions** table for each item that was purchased.

   * - .. image:: ../../images/checklist-item.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - **Refresh the customer 360 database**

       Activate, and then run the customer 360 database. This will refresh the data to include your customers' purchase histories as part of their unified customer profiles. When courier groups are configured in your tenant, this step will be done automatically after Stitch has finished processing.

       The Stitch process maintains the **Unified Itemized Transactions** and **Unified Product Catalog** tables.

.. setup-transactions-refresh-database-checklist-end


.. _setup-transactions-validate-database:

C360 validations
==================================================

.. setup-transactions-validate-database-start

A customer 360 validation report is generated as an output of running the database. You can access this report from the Notifications pane on the **Databases** page.

You should work through any of the individual validations in the report that indicate a validation error. In some cases, you may choose to ignore the error or adjust a threshold. In many cases, you should investigate the report to try to identify what is causing the error, and then determine if any adjustments can be made.

.. setup-transactions-validate-database-end

.. setup-transactions-validate-database-reports-start

There are many types of C360 validation reports, including for customer attributes, email addresses, loyalty programs, fiscal calendars, and transactions. Each individual report describes the issue, suggests potential ways to address the issue, and then links to the SQL that generated the validation report. Use these reports to improve the quality of data in your tenant.

.. setup-transactions-validate-database-reports-end

**Customer attributes**

.. setup-transactions-validate-database-reports-customer-attributes-start

Validation reports for customer attributes include:

* Are records associated with multiple Amperity IDs?
* Are known purchasers also classified as prospects?
* Are any prospects associated with a purchase history?
* Are physical addresses complete?
* Are email addresses complete?
* Are phone numbers complete?
* Are Amperity IDs grouped by household? (This validation is only available when your tenant uses the **Merged Households** table.)

.. setup-transactions-validate-database-reports-customer-attributes-end

**Email addresses and phone numbers**

.. setup-transactions-validate-database-reports-email-phone-start

Validation reports for email addresses and phone numbers include:

* Are email events associated with multiple Amperity IDs?
* Are email events unique by brand?
* Does an email event have an associated event type, such as opens or clicks?
* Are there conflicting opt-in preferences for email addresses or phone numbers?

.. setup-transactions-validate-database-reports-email-phone-end

**Loyalty programs**

.. setup-transactions-validate-database-reports-loyalty-start

Validation reports for loyalty programs include:

* Is the loyalty ID unique?
* Has the customer set an opt-in or opt-out preference?
* Do accrual events have an associated amount and datetime?
* Do redemption events have an associated amount and datetime?
* Is a customer's current and previous tier status available?

.. setup-transactions-validate-database-reports-loyalty-end

**Fiscal calenders**

.. setup-transactions-validate-database-reports-fiscal-start

Validation reports for fiscal calenders include:

* Are fiscal calendar dates unique?
* Are fiscal calendars complete after joining them to the **Unified Transactions** table?

.. setup-transactions-validate-database-reports-fiscal-end

**Transactions**

.. setup-transactions-validate-database-reports-transactions-start

Validation reports for transactions include:

* Are there records without an associated Amperity ID?
* Are orders associated with multiple Amperity IDs?
* Are there records without an associated order ID?
* Are orders associated with multiple order IDs?
* Are orders associated with a store ID?
* Are there orders without associated product information, such as ID, category, subcategory, or description?
* Are costs, quantities, and revenue non-positive for returns and cancellations?
* Are returns and cancellations associated with their original order ID?
* Are costs, list prices, discount amounts, discount percents, subtotals, and revenue positive for purchases?
* Is revenue greater than purchase revenue?
* Does the differece between list price and revenue match discounted amounts?
* Does revenue equal the sum of cost and profit?
* Are discount percents accurate?
* Is item revenue missing?
* Is quantity positive for all purchases?
* Are order dates missing or in the future?

.. setup-transactions-validate-database-reports-transactions-end


.. _setup-transactions-enable-segments-and-campaigns:

Enable segments and campaigns
==================================================

.. database-interactions-enable-segments-and-campaigns-start

Segments and campaigns are a collection of features that may be enabled after interaction records are configured. Once enabled, predictive analytics, metrics cards, segment insights, and campaigns are available from within Amperity.

.. database-interactions-enable-segments-and-campaigns-end


.. _setup-transactions-more-transactions-data:

More transactions data
==================================================

.. setup-transactions-more-transactions-data-start

Many brands add transactions to their tenant over time. Adding new transactions, along with data for other customer interactions, follow the same steps that were used for previous transactions. More sources helps Amperity build better profiles *and* helps your brand undersand how your customers' preferences for how they interact with your brand.

.. setup-transactions-more-transactions-data-end
