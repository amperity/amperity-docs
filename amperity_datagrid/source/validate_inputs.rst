.. 
.. https://docs.amperity.com/datagrid/
.. 

.. meta::
    :description lang=en:
        Input validation reports measure the quality of data that is being pulled to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Input validation reports measure the quality of data that is being pulled to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Input validation reports

==================================================
Input validation reports
==================================================

.. validate-inputs-overview-start

The quality of the data sources your brand chooses to make available to Amperity matters when it comes to building unified customer profiles because your brand uses those profiles to activate your customers across a wide variety of downstream use cases. More accurate profiles lead to higher activation rates, better match rates, and increased returns on advertiser spend.

Amperity includes a series of input validation reports that help your brand measure the quality of email addresses, phone numbers, and transactions. Use them to quickly identify data quality issues so that your brand can work to resolve those data quality issues as soon as possible.

.. validate-inputs-overview-end

.. validate-inputs-overview-note-start

.. note:: Input validation reports are meant to be informative and to provide a way for your brand to explore data. They do not have pass or fail thresholds and will not stop automated workflows within Amperity.

   Some input validations measure against a single semantic tag, while others use a combination of semantic tags. All input validations are returned as a series of columns that describe the quality of your data as it relates to a specific report.

   You do not need to run Stitch *or* have a working customer 360 database to run input validations. Just publish the domain tables to make them available to the **Queries** page.

.. validate-inputs-overview-note-end


.. _validate-inputs-semantic-tags:

Semantic tags
==================================================

.. validate-inputs-semantic-tags-start

Input validation reports are based on the following semantic tags:

* **email**
* **phone**
* **txn-item/is-return**
* **txn-item/is-cancellation**
* **txn-item/item-discount-amount**
* **txn-item/item-discount-percent**
* **txn-item/item-list-price**
* **txn-item/item-quantity**
* **txn-item/item-revenue**
* **txn-item/order-datetime**
* **txn-item/order-id**
* **txn-item/product-id**
* **txn-item/purchase-channel**
* **txn-item/store-id**

.. validate-inputs-semantic-tags-end


.. _validate-inputs-generate-reports:

Generate reports
==================================================

.. validate-inputs-generate-reports-start

Input validation reports are run automatically.

To open input validation reports, expand the **Notifications** pane, expand the most recent notification that is titled "Input Validation Report", and then click **View Report**.

The **Input validation reports** dialog box will show you all of the individual reports that apply to the current state of your tenant. Each individual report describes what causes the report to be visible, which semantic tags were validated, and then returns a series of columns that shows the report status for each data source that was part of the individual report. A link to a query is provided. This query opens in the **Queries** page and can be used to run queries against domain table data that has been published to the **Queries** page.

.. validate-inputs-generate-reports-end

.. validate-inputs-generate-reports-important-start

.. important:: Custom domain table data *must* be made available to the **Queries** page. Click the **Publish to queries** link at the top of the **Custom domain table** section in the **Sources** page. This process publishes each of the custom domain tables so that it may be accessed by a query. Allow this process to complete before using input validation queries.

.. validate-inputs-generate-reports-important-end


.. _validate-inputs-review-reports:

Review reports
==================================================

.. validate-inputs-review-reports-start

The list of input validation reports that will be available in your tenant depends on the outcomes of running the validations. Each report is available from the **Notifications** pane.

.. validate-inputs-review-reports-end


.. _validate-inputs-review-reports-customer-profiles:

Customer profiles
++++++++++++++++++++++++++++++++++++++++++++++++++

.. validate-inputs-review-reports-customer-profiles-start

Email addresses and phone numbers are validated for the percentage of missing values, correctly formatted values, and the frequency at which unique values occur.

.. validate-inputs-review-reports-customer-profiles-end


.. _validate-inputs-review-reports-transactions:

Transactions
++++++++++++++++++++++++++++++++++++++++++++++++++

.. validate-inputs-review-reports-transactions-start

A complete transaction with good underlying data has a combination of values that work together to describe what was purchased, when it was purchased, where it was purchased, and so on. Incomplete transactions are shown using a variety of reports. For example:

* All items should be associated with a unique product ID.
* All orders should be associated with a store ID.
* All orders should have a quantity, a revenue amount, and an order date.
* All orders should have a unique order ID.
* An item cannot be returned *and* canceled.
* canceled item revenue should be negative
* Discount amounts should be positive
* Discount percent should be "discount amount / list price"
* From which store was a purchase made?
* Quantity should be negative when items were canceled or returned
* Quantity should be positive
* Returned item revenue should be negative
* Revenue should be "list price - discount amount"
* Revenue should be positive
* Through which channel was a purchase made?
* Was an item canceled or returned? This should be true or false.
* What percentage of product IDs are unique?

Each individual validation report shows the data sources that are associated with the report, the semantic tags that were validated, and the results of the validation. Explore the data that is associated with this report by clicking the **Validation query** link, which opens in the **Queries** page.

.. validate-inputs-review-reports-transactions-end


.. _validate-inputs-review-reports-privacy-rights:

Privacy rights
++++++++++++++++++++++++++++++++++++++++++++++++++

.. validate-inputs-review-reports-privacy-rights-start

A :doc:`privacy rights <privacy_rights>` workflow can help your organization stay in compliance with data protection and privacy regulations, such as those required by California Consumer Privacy Act (CCPA) or General Data Protection Regulation (GDPR).

.. validate-inputs-review-reports-privacy-rights-end

.. validate-inputs-review-reports-privacy-rights-validations-start

Privacy rights workflows include the following input validation reports:

* Missing request IDs
* Missing request types
* Missing request strategies
* Phone number validation
* Request strategy should be **connected_pii** or **exact**.
* Request type should be **delete**, **delete_pii**, or **dsar**.

.. validate-inputs-review-reports-privacy-rights-validations-end
