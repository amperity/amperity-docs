.. https://docs.amperity.com/ampiq/


.. meta::
    :description lang=en:
        About the standard output tables that can be used to define audiences and build campaigns.

.. meta::
    :content class=swiftype name=body data-type=text:
        About the standard output tables that can be used to define audiences and build campaigns.

.. meta::
    :content class=swiftype name=title data-type=string:
        Standard output

==================================================
Standard output
==================================================

.. standard-output-overview-start

The following tables are standard output of Amperity. These tables (and the attributes within them) are always available to the **Segment Editor**:

* :ref:`Campaign Recipients <standard-output-campaign-recipients>`
* :ref:`Customer Attributes <standard-output-customer-attributes>`
* :ref:`Customer 360 <standard-output-customer-360>`
* :ref:`Predicted Affinity <standard-output-predicted-affinity>` (when predictive modeling is enabled for your tenant)
* :ref:`Predicted CLV Attributes <standard-output-predicted-clv-attributes>` (when predictive modeling is enabled for your tenant)
* :ref:`Transaction Attributes Extended <standard-output-transaction-attributes-extended>`
* :ref:`Unified Itemized Transactions <standard-output-unified-itemized-transactions>`
* :ref:`Unified Transactions <standard-output-unified-transactions>`

This topic collects *all* of the attributes that are available in standard output into a single topic. It is organized alphabetically by table, and then within each table attribues it is organized alphabetically by attribute name.

.. standard-output-overview-end

.. standard-output-overview-note-start

.. note:: It is not uncommon for certain tables---**Customer Attributes** and **Customer 360**, in particular---to contain additional attributes that are custom to your tenant. The :ref:`Merged Customers <standard-output-merged-customers>` table is visible when working in certain areas of the **Campaigns** page and is the underlying source of truth for attributes in the **Customer 360** table.

.. standard-output-overview-note-end

.. standard-output-overview-tip-start

.. tip:: This topic isn't designed to be read from end-to-end. You can if you want to, but it's more useful as a reference that you can browse when you need it. Use your browser's search function, type the name of an attribute you want to learn more about, and then find that attribute on the page.

.. standard-output-overview-tip-end


.. _standard-output-campaign-recipients:

Campaign Recipients
==================================================

.. standard-output-campaign-recipients-start

Campaign recipient attributes provide a record of campaigns that were sent from Amperity. Each campaign is associated with the segment that was used to build the audience (including control groups, treatment groups, and sub-audiences), the campaign launch date, and any destination to which the campaign was sent.

The following attributes are available from the **Campaign Recipients** table.

.. standard-output-campaign-recipients-end

.. standard-output-campaign-recipients-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **Campaign ID**
     - The unique ID for a campaign.
   * - **Campaign Name**
     - The name of the campaign.
   * - **Campaign Type**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-campaign-start
          :end-before: .. term-campaign-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-campaign-type-start
          :end-before: .. term-campaign-type-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-one-time-campaign-start
          :end-before: .. term-one-time-campaign-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-recurring-campaign-start
          :end-before: .. term-recurring-campaign-end

   * - **Database ID**
     - The unique ID for the database.
   * - **Database Name**
     - The name of the database.
   * - **Dataset Version**
     - A unique ID for the dataset used with this set of campaign recipients.
   * - **Delivery Datetime**
     - The date and time at which the associated campaign ID was delivered to the destination.
   * - **Destination ID**
     - The unique ID for a destination.
   * - **Destination Name**
     - The name of the destination to which the associated campaign ID was sent.
   * - **Is Control**
     - A flag that indicates if the **Treatment ID** represents a control group.
   * - **Launch Datetime**
     - The date and time at which the associated campaign ID was sent from Amperity to its downstream workflow.
   * - **Segment ID**
     - The unique ID for the segment that generated the list of recipients for the associated campaign ID.
   * - **Segment Name**
     - The name of the segment used with the associated campaign ID.
   * - **Treatment ID**
     - The ID for the treatment group to which the associated campaign was sent.
   * - **Treatment Name**
     - The name of the treatment group to which the associated campaign was sent. One or more treatment groups, along with a control group, are used to measure the quality of a campaign.

   * - **Workflow ID**
     - The unique ID for the workflow that managed the associated campaign.

.. standard-output-campaign-recipients-table-end


.. _standard-output-customer-360:

Customer 360
==================================================

.. standard-output-customer-360-start

Customer 360 attributes present a unified view of your customers across all points of engagement, including attributes that cross systems.

The following attributes are available from the **Customer 360** table.

.. standard-output-customer-360-end

.. standard-output-customer-360-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **Given Name**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end
   * - **Surname**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end
   * - **Email**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end
   * - **Phone**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end
   * - **Address**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address-start
          :end-before: .. term-address-end
   * - **City**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-city-start
          :end-before: .. term-city-end
   * - **State**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end
   * - **Postal**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end
   * - **Birthdate**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-birthdate-start
          :end-before: .. term-birthdate-end
   * - **Gender**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-gender-start
          :end-before: .. term-gender-end

.. standard-output-customer-360-table-end


.. _standard-output-customer-attributes:

Customer Attributes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-customer-attributes-table-start
   :end-before: .. term-customer-attributes-table-end

.. standard-output-customer-attributes-start

.. note:: The **Customer Attributes** table is built (and often customized) for your tenant. It is not part of standard output until after it has been added to your tenant, but is included here because it is often used closely with standard output to support a variety of complex use cases, such as churn prevention campaigns.

.. standard-output-customer-attributes-end

.. standard-output-customer-attributes-start

The **Customer Attributes** table contains the following columns:

.. standard-output-customer-attributes-end

.. standard-output-customer-attributes-table-start

.. list-table::
   :widths: 200 100 300
   :header-rows: 1

   * - Column Name
     - Data type
     - Description
   * - **Amperity ID**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-amperity-id-column-start
          :end-before: .. term-amperity-id-column-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-amperity-id-format-start
          :end-before: .. term-amperity-id-format-end

   * - **Churn Trigger**
     - String
     - The predicted churn status for a customer. Possible values:

       * Active
       * Cooling down
       * At risk
       * Highly at risk
       * Lost
       * Blank

       .. tip:: Use these values as part of your churn prevention campaigns.

   * - **Churn Trigger Start Datetime**
     - Datetime
     - The date and time at which the predicted **Churn Trigger** status begins.

   * - **Contactable Address**
     - Boolean
     - A flag that indicates if a customer can be contacted by a physical mailing address.

   * - **Contactable Email**
     - Boolean
     - A flag that indicates if a customer can be contacted by an email address.

   * - **Contactable Global**
     - Boolean
     - A flag that indicates if a customer can be contacted by phone number, email address, or physical mailing address.

   * - **Contactable Paid Social**
     - Boolean
     - A flag that indicates if a customer has personally identifiable information (PII) that could be used to contact them using paid social media channels.

   * - **Contactable Phone**
     - Boolean
     - A flag that indicates if a customer can be contacted by phone.

   * - **Contactable SMS**
     - boolean
     - A flag that indicates if a customer can be contacted by SMS.

   * - **Customer Classifications**
     - String
     - A string that contains all of the classifications for a customer. For example: "is_reseller, is_outlier" or "is_test_account". A value of " " (an empty space) indicates that all classifications are false.

   * - **Customer Type**
     - String
     - The type of user: "customer" or "prospect". A customer has a historical revenue relationship with a brand. A prospect does not have a revenue relationship with a brand.

   * - **Historical Prospect Lifecycle Status**
     - String
     - A prospect is a potential customer to whom you may want to conduct marketing activity. The status for a customer who is a "prospect".

   * - **Historical Purchaser Lifecycle Status**
     - String
     - The status for a customer, based on their history and recency of interactions a brand. Possible values: "new", "active", "lapsed", "dormant", and "prospect".

       .. include:: ../../shared/terms.rst
          :start-after: .. term-customer-lifecycle-status-configure-start
          :end-before: .. term-customer-lifecycle-status-configure-end

   * - **Is Business**
     - Boolean
     - A flag that indicates if a customer is a known or likely business.

   * - **Is Employee**
     - Boolean
     - A flag that indicates if a customer is or has been an employee of the brand at any time.

   * - **Is Gift Giver**
     - Boolean
     - A flag that indicates if a customer has purchased items as gifts.

   * - **Is No PII Amperity ID**
     - Boolean
     - A flag that indicates of the customer does not have personally identifiable information (PII) for name (given name, surname, full name), address (street address, city, state, postal code), email address, or phone number.

   * - **Is Outlier**
     - Boolean
     - A flag that indicates if the customer has abnormally high purchase behaviors in comparison to other purchasers.

   * - **Is Primary Buyer Household**
     - Boolean
     - A flag that indicates if a customer is the individual within a household who represents the highest lifetime revenue for that household.

       .. note:: This attribute requires the **Merged Households** table.

   * - **Is Prospect**
     - Boolean
     - A flag that indicates if a customer does not have a purchase history with a brand.

   * - **Is Purchaser**
     - Boolean
     - A flag that indicates if the customer has a purchase history with a brand.

   * - **Is Reseller**
     - Boolean
     - A flag that indicates if the customer is a known or likely reseller of a product.

       .. tip:: A reseller should be defined as an early repeat purchaser with a high lifetime order frequency. Use the following fields from the **Transaction Attributes Extended** table to define a reseller: 

          * **Early Repeat Purchaser** (set to "true")
          * **Lifetime Order Frequency** (define an order frequency threshold, such as "greater than 50")

   * - **Is Test Account**
     - Boolean
     - A flag that indicates if the customer is a known test account for a brand.

   * - **Marketable Address**
     - Boolean
     - A flag that indicates if a customer has a marketable physical mailing address *and* has given permission to be contacted.

   * - **Marketable Email**
     - Boolean
     - A flag that indicates if a customer has a marketable email mailing address *and* has given permission to be contacted.

   * - **Marketable Global**
     - Boolean
     - A flag that indicates if a customer has a marketable phone number, email address, SMS number, or physical mailing address *and* has given permission to be contacted.

   * - **Marketable Phone**
     - Boolean
     - A flag that indicates if a customer has a marketable phone number *and* has given permission to be contacted.

   * - **Marketable SMS**
     - Boolean
     - A flag that indicates if a customer has a marketable SMS number *and* has given permission to be contacted.

.. standard-output-customer-attributes-table-end


.. _standard-output-merged-customers:

Merged Customers
==================================================

.. standard-output-merged-customers-start

Merged customer attributes represent your unique customers across all of the data sources that you provided to Amperity. These attributes group customer profile data---names, email addresses, phone numbers, physical addresses---based on how it was discovered from across all of the data sources that were provided to your tenant.

The following attributes are available from the **Merged Customers** table.

.. standard-output-merged-customers-end

.. standard-output-merged-customers-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **Address**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address-start
          :end-before: .. term-address-end
   * - **Address2**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address2-start
          :end-before: .. term-address2-end
   * - **Birthdate**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-birthdate-start
          :end-before: .. term-birthdate-end
   * - **City**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-city-start
          :end-before: .. term-city-end
   * - **Company**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-company-start
          :end-before: .. term-company-end
   * - **Country**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-country-start
          :end-before: .. term-country-end
   * - **Email**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end
   * - **Full Name**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-full-name-start
          :end-before: .. term-full-name-end
   * - **Gender**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-gender-start
          :end-before: .. term-gender-end
   * - **Generational Suffix**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-generational-suffix-start
          :end-before: .. term-generational-suffix-end
   * - **Given Name**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end
   * - **Loyalty ID**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-loyalty-id-start
          :end-before: .. term-loyalty-id-end
   * - **Phone**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end
   * - **Postal**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end
   * - **State**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end
   * - **Surname**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end
   * - **Title**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-title-start
          :end-before: .. term-title-end

.. standard-output-merged-customers-table-end


.. _standard-output-predicted-affinity:

Predicted Affinity
==================================================

.. standard-output-predicted-affinity-start

Product affinity attributes associate your customers to recommended audience sizes and rankings by products. 

The following attributes are available from the **Predicted Affinity** table.

.. standard-output-predicted-affinity-end

.. standard-output-predicted-affinity-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **Audience Size Large**
     - A flag that indicates the recommended audience size. When this value is "true" the recommended audience size is large.

       A large audience is predicted to include ~90% of future purchasers, while also including a high number of non-purchasers.
   * - **Audience Size Medium**
     - A flag that indicates the recommended audience size. When this value is "true" the recommended audience size is medium.

       A medium audience is predicted to include ~70% of future purchasers, though it may also include a moderate number of non-purchasers.
   * - **Audience Size Small**
     - A flag that indicates the recommended audience size. When this value is "true" the recommended audience size is small.

       A small audience is predicted to include ~50% of future purchasers, while including the fewest non-purchasers. Use a small audience size to help prevent wasted spend and reduce opt-outs.
   * - **Product Attribute**
     - The field against which product affinity is measured. For example: a category, a class, or a brand.

   * - **Ranking**
     - A ranking of customers by their score for this product. A rank that is less than or equal to X will provide the top N customers with an affinity for this product.

   * - **Score**
     - The strength of a customers's affinity for this product, shown as an uncalibrated probability.

       .. tip:: This score is used internally by Amperity and does not directly correlate to ranking and/or audience size. Sort results by **ranking**, and then compare to audience sizes. Higher rankings within smaller audience sizes correlate with stronger affinity.

.. standard-output-predicted-affinity-table-end

.. _standard-output-predicted-clv-attributes:

Predicted CLV Attributes
==================================================

.. standard-output-predicted-clv-attributes-start

Customer lifetime value (CLV) attributes use historical customer behavior to predict customer lifetime value during the next calendar year, including by historical customer status and historical lifetime value tier.

The following attributes are available from the **Predicted CLV Attributes** table.

.. standard-output-predicted-clv-attributes-end

.. standard-output-predicted-clv-attributes-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **Predicted Average Order Revenue Next 365d**
     - The predicted average order revenue over the next 365 days.

   * - **Predicted CLV Next 365d**
     - The total predicted customer spend over the next 365 days.

   * - **Predicted Customer Lifecycle Status**
     - A probabilistic grouping of a customer's likelihood to purchase again. Groupings include the following tiers:

       #. Active
       #. Cooling down
       #. At risk
       #. Highly at risk
       #. Lost

   * - **Predicted Customer Lifetime Value Tier**
     - A percentile grouping of customers by pCLV. Groupings include:

       #. Platinum: top 1% of customers
       #. Gold: top 1%-5% of customers
       #. Silver: top 5%-10% of customers
       #. Bronze: top 10%-25% of customers
       #. Medium: top 25%-50% of customers
       #. Low: bottom 50% of customers

   * - **Predicted Order Frequency Next 365d**
     - The predicted number of orders over the next 365 days.

   * - **Predicted Probability of Transaction Next 365d**
     - The probability a customer will purchase again in the next 365 days.

.. standard-output-predicted-clv-attributes-table-end


.. _standard-output-transaction-attributes-extended:

Transaction Attributes Extended
==================================================

.. standard-output-transaction-attributes-extended-start

Transaction attributes are a set of extended attributes that are based on inputs from known orders and items, including first and second orders broken down by brands, channels, stores, totals, dates and times.

Transaction attributes provide the days in-between transaction events and time period rollups across prices, numbers of items within individual orders, average order values, order frequencies, and RFM scores.

.. standard-output-transaction-attributes-extended-end

.. standard-output-transaction-attributes-extended-links-start

Extended transaction attributes are presented as a single table (with many columns), including an Amperity ID, and fit into the following categories:

* :ref:`Customer flags <standard-output-transaction-attributes-extended-customer-flags>`
* :ref:`Customer orders <standard-output-transaction-attributes-extended-customer-orders>`
* :ref:`Date differences <standard-output-transaction-attributes-extended-date-differences>`
* :ref:`Time period rollups <standard-output-transaction-attributes-extended-period-rollups>`
* :ref:`RFM <standard-output-transaction-attributes-extended-rfm>`

.. standard-output-transaction-attributes-extended-links-end


.. _standard-output-transaction-attributes-extended-customer-flags:

Customer flags
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-customer-flags-start
   :end-before: .. data-tables-transaction-attributes-extended-customer-flags-end

.. standard-output-transaction-attributes-extended-customer-flags-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description

   * - **Early Repeat Purchaser**
     - Indicates if a customer made a repeat purchase within the previous 30 days.

   * - **Multi Purchase Brand**
     - Indicates if a customer has interacted with more than one brand.

   * - **Multi Purchase Channel**
     - Indicates if a customer has interacted with more than one channel.

   * - **One and Done**
     - Indicates if a customer has made only one purchase.

       .. important:: Amperity resolves one-and-done for the data provided to it. For example, if data is provided that spans 2015-2020, a purchase in 2014 will not be in the results.

.. standard-output-transaction-attributes-extended-customer-flags-table-end


.. _standard-output-transaction-attributes-extended-customer-orders:

Customer orders
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-customer-orders-start
   :end-before: .. data-tables-transaction-attributes-extended-customer-orders-end

.. standard-output-transaction-attributes-extended-customer-orders-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **<x> Order Datetime**
     - The datetime on which the order was made. Available attributes:

       * **First Order Datetime**
       * **Second Order Datetime**
       * **Latest Order Datetime**

   * - **<x> Order ID**
     - The ID of the order. Available attributes:

       * **First Order ID**
       * **Second Order ID**
       * **Latest Order ID**

   * - **<x> Order Purchase Brand**
     - The brand of the order made by the customer. Available attributes:

       * **First Order Purchase Brand**
       * **Second Order Purchase Brand**
       * **Latest Order Purchase Brand**

   * - **<x> Order Purchase Channel**
     - The channel in which the customer's order was made. Available attributes:

       * **First Order Purchase Channel**
       * **Second Order Purchase Channel**
       * **Latest Order Purchase Channel**

   * - **<x> Order Revenue**
     - The total revenue for orders at each interval. Available attributes:

       * **First Order Revenue**
       * **Second Order Revenue**
       * **Latest Order Revenue**

   * - **<x> Store ID**
     - The ID of the store where the customer made their order. This value may be **NULL** if the associated channel is not retail or some equivalent. Available attributes:

       * **First Order Store ID**
       * **Second Order Store ID**
       * **Latest Order Store ID**

   * - **<x> total items**
     - The total number of items in the order. Available attributes:

       * **First Order Total Items**
       * **Second Order Total Items**
       * **Latest Order Total Items**

.. standard-output-transaction-attributes-extended-customer-orders-table-end


.. _standard-output-transaction-attributes-extended-date-differences:

Date differences
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-date-differences-start
   :end-before: .. data-tables-transaction-attributes-extended-date-differences-end

.. standard-output-transaction-attributes-extended-date-differences-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **Days Since Latest Order**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-days-since-last-order-start
          :end-before: .. term-days-since-last-order-end

   * - **First to Latest Order Days**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-first-to-latest-order-days-start
          :end-before: .. term-first-to-latest-order-days-end

   * - **First to Second Order Days**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-first-to-second-order-days-start
          :end-before: .. term-first-to-second-order-days-end

.. standard-output-transaction-attributes-extended-date-differences-table-end


.. _standard-output-transaction-attributes-extended-period-rollups:

Time period rollups
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-period-rollups-start
   :end-before: .. data-tables-transaction-attributes-extended-period-rollups-end

.. standard-output-transaction-attributes-extended-period-rollups-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **<x> Average Item Price**
     - The average item price during the time period. Available attributes:

       * **L30D Average Item Price**
       * **L3M Average Item Price**
       * **L6M Average Item Price**
       * **L12M Average Item Price**
       * **LY12M Average Item Price**
       * **Lifetime Average Item Price**

   * - **<x> Average Num Items**
     - The average number of items during the time period. Available attributes:

       * **L30D Average Num Items**
       * **L3M Average Num Items**
       * **L6M Average Num Items**
       * **L12M Average Num Items**
       * **LY12M Average Num Items**
       * **Lifetime Average Num Items**

   * - **<x> Average Order Value**
     - The Average Order Value during the time period. Available attributes:

       * **L30D Average Order Value**
       * **L3M Average Order Value**
       * **L6M Average Order Value**
       * **L12M Average Order Value**
       * **LY12M Average Order Value**
       * **Lifetime Average Order Value**

   * - **<x> Order Frequency**
     - The count of distinct order IDs that are associated with the customer during the time period. Available attributes:

       * **L30D Order Frequency**
       * **L3M Order Frequency**
       * **L6M Order Frequency**
       * **L12M Order Frequency**
       * **LY12M Order Frequency**
       * **Lifetime Order Frequency**

   * - **<x> Order Revenue**
     - The total revenue for orders in the time period. Available attributes:

       * **L30D Order Revenue**
       * **L3M Order Revenue**
       * **L6M Order Revenue**
       * **L12M Order Revenue**
       * **LY12M Order Revenue**
       * **Lifetime Order Revenue**

   * - **<x> Preferred Purchase Brand**  
     - The brand with the greatest number of orders during the time period. Available attributes:

       * **L30D Preferred Purchase Brand**  
       * **L3M Preferred Purchase Brand**  
       * **L6M Preferred Purchase Brand**  
       * **L12M Preferred Purchase Brand**  
       * **LY12M Preferred Purchase Brand**  
       * **Lifetime Preferred Purchase Brand**  

   * - **<x> Preferred Purchase Channel**
     - The channel with the greatest number of orders during the time period. Available attributes:

       * **L30D Preferred Purchase Channel**
       * **L3M Preferred Purchase Channel**
       * **L6M Preferred Purchase Channel**
       * **L12M Preferred Purchase Channel**
       * **LY12M Preferred Purchase Channel**
       * **Lifetime Preferred Purchase Channel**

   * - **<x> Preferred Store ID**
     - The store ID with the greatest number of orders during the time period. Available attributes:

       * **L30D Preferred Store ID**
       * **L3M Preferred Store ID**
       * **L6M Preferred Store ID**
       * **L12M Preferred Store ID**
       * **LY12M Preferred Store ID**
       * **Lifetime Preferred Store ID**

   * - **<x> Purchase Brands**
     - The count of the distinct brands a customer interacted with during the time period. Available attributes:

       * **L30D Purchase Brands**
       * **L3M Purchase Brands**
       * **L6M Purchase Brands**
       * **L12M Purchase Brands**
       * **LY12M Purchase Brands**
       * **Lifetime Purchase Brands**

   * - **<x> Purchase Channels**
     - The count of the distinct channels (online, in store, etc.) that the customer interacted with during during the time period. Available attributes:

       * **L30D Purchase Channels**
       * **L3M Purchase Channels**
       * **L6M Purchase Channels**
       * **L12M Purchase Channels**
       * **LY12M Purchase Channels**
       * **Lifetime Purchase Channels**

   * - **<x> Stores**
     - The count of the distinct stores that the customer interacted with during the time period. Available attributes:

       * **L30D Stores**
       * **L3M Stores**
       * **L6M Stores**
       * **L12M Stores**
       * **LY12M Stores**
       * **Lifetime Stores**

   * - **<x> Total Items**
     - The total number of items purchased by the customer during the time period. Available attributes:

       * **L30D Total Items**
       * **L3M Total Items**
       * **L6M Total Items**
       * **L12M Total Items**
       * **LY12M Total Items**
       * **Lifetime Total Items**

.. standard-output-transaction-attributes-extended-period-rollups-table-end


.. _standard-output-transaction-attributes-extended-rfm:

RFM
--------------------------------------------------

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-transaction-attributes-extended-rfm-start
   :end-before: .. data-tables-transaction-attributes-extended-rfm-end

.. standard-output-transaction-attributes-extended-rfm-note-start

.. note:: RFM uses approximate calculations to optimize the performance of the **Transaction Attributes Extended** table.

.. standard-output-transaction-attributes-extended-rfm-note-end

.. standard-output-transaction-attributes-extended-rfm-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **L12M RFM Score**
     - The RFM score for the customer based on transactions that occurred within the last 12 months. The RFM score is represented as an integer between "0" and "999" and is concatenated using the individual recency, frequency, and monetary scores or is **NULL** if the customer has zero purchases within the last 12 months.

   * - **L12M Recency**
     - The recency score for customer transactions that occurred within the last 12 months. The recency score is represented as an integer between "0" and "9". Each integer represents 10%:

       * 0: 0-10th percentile
       * 1: 10-20th percentile
       * 2: 20-30th percentile
       * 3: 30-40th percentile
       * 4: 4-50th percentile
       * 5: 5-60th percentile
       * 6: 60-70th percentile
       * 7: 70-80th percentile
       * 8: 80-90th percentile
       * 9: 90-100th percentile

   * - **L12M Frequency**
     - The frequency score for customer transactions that occurred within the last 12 months. The frequency score is represented as an integer between "0" and "9". Each integer represents 10%:

       * 0: 0-10th percentile
       * 1: 10-20th percentile
       * 2: 20-30th percentile
       * 3: 30-40th percentile
       * 4: 4-50th percentile
       * 5: 5-60th percentile
       * 6: 60-70th percentile
       * 7: 70-80th percentile
       * 8: 80-90th percentile
       * 9: 90-100th percentile
   * - **L12M Monetary**
     - The monetary score for customer transactions that occurred within the last 12 months. The monetary score is represented as an integer between "0" and "9". Each integer represents 10%:

       * 0: 0-10th percentile
       * 1: 10-20th percentile
       * 2: 20-30th percentile
       * 3: 30-40th percentile
       * 4: 4-50th percentile
       * 5: 5-60th percentile
       * 6: 60-70th percentile
       * 7: 70-80th percentile
       * 8: 80-90th percentile
       * 9: 90-100th percentile

.. standard-output-transaction-attributes-extended-rfm-table-end


.. _standard-output-unified-itemized-transactions:

Unified Itemized Transactions
==================================================

.. standard-output-unified-itemized-transactions-start

Item attributes provide a history of the interactions your customers have had with your products---returns, cancellations, costs, discounts, quantities, prices---sorted by customer orders for individual items, and then associated to the transactions made by your unique customers.

The following attributes are available from the **Unified Itemized Transaction** table.

.. standard-output-unified-itemized-transactions-end

.. standard-output-unified-itemized-transactions-note-start

.. note:: Your product catalog is joined to this table in your Customer 360 database. You should expect to find the attributes for your product catalog within this table.

   Product catalog attributes describe all of the products, categories, and sub-categories that exist within your brand.

   Common product attributes include **Product Category**, **Product Description**, **Product ID**, and **Product Subcategory**; however, product catalogs are often tenant-specific and you should expect to see additional product attributes that are unique to your tenant.

.. standard-output-unified-itemized-transactions-note-end

.. standard-output-unified-itemized-transactions-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **Customer ID**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-customer-id-start
          :end-before: .. term-customer-id-end
   * - **Is Cancellation**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-is-canceled-start
          :end-before: .. term-is-canceled-end
   * - **Is Return**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-is-return-start
          :end-before: .. term-is-return-end
   * - **Item Cost**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-cost-start
          :end-before: .. term-item-cost-end
   * - **Item Discount Amount**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-discount-amount-start
          :end-before: .. term-item-discount-amount-end
   * - **Item Discount Percent**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-discount-percent-start
          :end-before: .. term-item-discount-percent-end
   * - **Item List Price**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-list-price-start
          :end-before: .. term-item-list-price-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-msrp-start
          :end-before: .. term-msrp-end
   * - **Item Profit**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-profit-start
          :end-before: .. term-item-profit-end
   * - **Item Quantity**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-quantity-start
          :end-before: .. term-item-quantity-end
   * - **Item Revenue**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-revenue-start
          :end-before: .. term-item-revenue-end
   * - **Item Subtotal**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-item-subtotal-start
          :end-before: .. term-item-subtotal-end
   * - **Order Datetime**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-date-start
          :end-before: .. term-order-date-end
   * - **Order ID**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-id-start
          :end-before: .. term-order-id-end
   * - **Product ID**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-product-id-start
          :end-before: .. term-product-id-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-sku-start
          :end-before: .. term-sku-end

       For example, a shirt with the same color and material, but with three different sizes would be represented by three unique SKUs and would also be represented by three unique product IDs.
   * - **Unit Cost**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-cost-start
          :end-before: .. term-unit-cost-end
   * - **Unit Discount Amount**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-discount-amount-start
          :end-before: .. term-unit-discount-amount-end
   * - **Unit List Price**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-list-price-start
          :end-before: .. term-unit-list-price-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-msrp-start
          :end-before: .. term-msrp-end
   * - **Unit Profit**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-profit-start
          :end-before: .. term-unit-profit-end
   * - **Unit Revenue**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-revenue-start
          :end-before: .. term-unit-revenue-end
   * - **Unit Subtotal**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-subtotal-start
          :end-before: .. term-unit-subtotal-end

.. standard-output-unified-itemized-transactions-table-end


.. _standard-output-unified-transactions:

Unified Transactions
==================================================

.. standard-output-unified-transactions-start

Orders attributes provide a history of the transactions your customers have made with your brand---channel (store, online, etc.), currency, dates and times, costs, discounts, quantities---sorted by each transaction made by your unique customers.

The following attributes are available from the **Unified Transactions** table.

.. standard-output-unified-transactions-end

.. standard-output-unified-transactions-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attributes
     - Description
   * - **Currency**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-currency-start
          :end-before: .. term-currency-end
   * - **Customer ID**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-customer-id-start
          :end-before: .. term-customer-id-end
   * - **Digital Channel**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-digital-channel-start
          :end-before: .. term-digital-channel-end
   * - **Order canceled Quantity**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-canceled-quantity-start
          :end-before: .. term-order-canceled-quantity-end
   * - **Order canceled Revenue**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-canceled-revenue-start
          :end-before: .. term-order-canceled-revenue-end
   * - **Order Cost**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-cost-start
          :end-before: .. term-order-cost-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-cogs-start
          :end-before: .. term-cogs-end
   * - **Order Datetime**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-date-start
          :end-before: .. term-order-date-end
   * - **Order Discount Amount**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-discount-amount-start
          :end-before: .. term-order-discount-amount-end
   * - **Order Discount Percent**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-discount-percent-start
          :end-before: .. term-order-discount-percent-end
   * - **Order ID**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-id-start
          :end-before: .. term-order-id-end
   * - **Order List Price**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-list-price-start
          :end-before: .. term-order-list-price-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-msrp-start
          :end-before: .. term-msrp-end
   * - **Order Profit**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-profit-start
          :end-before: .. term-order-profit-end
   * - **Order Quantity**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-quantity-start
          :end-before: .. term-order-quantity-end
   * - **Order Returned Quantity**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-returned-quantity-start
          :end-before: .. term-order-returned-quantity-end
   * - **Order Returned Revenue**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-returned-revenue-start
          :end-before: .. term-order-returned-revenue-end
   * - **Order Revenue**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-revenue-start
          :end-before: .. term-order-revenue-end
   * - **Order Shipping Amount**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-shipping-amount-start
          :end-before: .. term-order-shipping-amount-end
   * - **Order Subtotal**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-subtotal-start
          :end-before: .. term-order-subtotal-end
   * - **Order Tax Amount**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-order-tax-amount-start
          :end-before: .. term-order-tax-amount-end
   * - **Payment Method**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-payment-method-start
          :end-before: .. term-payment-method-end
   * - **Purchase Brand**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-purchase-brand-start
          :end-before: .. term-purchase-brand-end

       .. note:: This attribute should only used when more than one brand is present in your tenant.

   * - **Purchase Channel**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-purchase-channel-start
          :end-before: .. term-purchase-channel-end
   * - **Store ID**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-store-id-start
          :end-before: .. term-store-id-end
   * - **Sum Item Discount Amount**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-sum-of-discount-amounts-start
          :end-before: .. term-sum-of-discount-amounts-end
   * - **Sum Item Revenue**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-sum-of-itemized-revenue-start
          :end-before: .. term-sum-of-itemized-revenue-end

.. standard-output-unified-transactions-table-end
