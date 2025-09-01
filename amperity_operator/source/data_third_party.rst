.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use third-party data sources with Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use third-party data sources with Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Third-party data sources

==================================================
Third-party data sources
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-third-party-data-start
   :end-before: .. term-third-party-data-end

.. data-third-party-start

Acquiring third-party data should be an important part of the effort to better understand how your customers interact with your products and your brand. Once acquired, third-party data can be used in a variety of ways:

* Improving personalization
* Improving identity resolution
* Providing address hygiene, often referred to as National Change of Address (NCOA)
* Identifying unique individuals from sparse data, often referred to as trade area append (TAA)

When third-party data is provided to Amperity alongside rich sets of first-party data, Amperity can support many use cases that can become part of your brand's strategy to build a complete understanding of your customers.

.. note:: Amperity does not directly license third-party data sources and instead offers a solution that can work with third-party data vendors, such as `Infutor <https://infutor.com/>`__ |ext_link| (a recommended partner of Amperity) or the third-party data vendor of your choice. Amperity is focused on first-party data; it is the responsibility of the customer to determine which types of third-party data will be provided to Amperity.

.. data-third-party-end


.. _third-party-use-cases:

Use cases
==================================================

.. third-party-use-cases-start

There are two broad use-cases for third-party data:

#. The customer does third-party matching outside of Amperity, and then provides this data to Amperity with fields already append to first-party data or with a unique ID with which Amperity can join third-party data to the results of the identity resolution process.
#. The customer provides third-party data to Amperity, which is then matched during the Amperity identity resolution process, just like with any other data source. Amperity will link the third- and first-party data together via the Amperity ID.

The following scenarios describe more specific approaches for using third-party data with Amperity:

#. :ref:`Applying trade area append (TAA) <data-third-party-trade-area-append>`
#. :ref:`Enriching customer records <data-third-party-enrich-customer-records>`
#. :ref:`Updating addresses (NCOA) <data-third-party-update-addresses>`
#. :ref:`Matching anonymous visitors <data-third-party-match-anonymous-visitors>`
#. :ref:`Identifying sparse customer records <data-third-party-identify-sparse-records>`
#. :ref:`Purchasing prospect lists <data-third-party-purchase-prospect-lists>`

.. caution:: It's important to identify the use case and it's intended outcome. This topic does not contain a complete list of use cases for third-party data for which Amperity can provide a solution.

.. third-party-use-cases-end


.. _data-third-party-trade-area-append:

Trade area append (TAA)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-taa-start
   :end-before: .. term-taa-end

.. data-third-party-trade-area-append-start

Customers use TAA to better understand the customers they know the least about. For example, a customer may have a rich set of data that contains PII and transaction data about their most loyal customers alongside decreasingly rich sets of data for customers who engage less frequently, belong to fewer loyalty programs, and participate in fewer channels. It is not unusual for 80% of a customer's data set to benefit from using some form of TAA to improve data quality.

.. data-third-party-trade-area-append-end

.. data-third-party-trade-area-append-context-start

Amperity can ingest a data source with sparse PII, such as point-of-sale credit card transactions that only capture first name, last name, a credit card token or hash, and information about the store at which the transaction occurred, and then match this to a third-party prospect file. The third-party prospect file contains rich PII, and by using TAA to match sparse PII to rich PII, the customer has a more complete understanding of who those customers are, which brands they prefer, and can better determine which types of engagements with those customers will be successful.

.. data-third-party-trade-area-append-context-end


.. _data-third-party-enrich-customer-records:

Enrich customer records
==================================================

.. data-third-party-enrich-customer-records-start

Amperity can help enrich customer records that contain personally identifiable information (PII) when data sources with some form of associated contact information, such as email addresses, physical addresses, or phone numbers, are provided to Amperity.

Because these data sources contain PII, it's more likely that Amperity can associate this information to high-quality data sources, after which additional third-party data sources that contain data for household income, gender, ethnicity, size of household, and so on, can also be associated.

.. data-third-party-enrich-customer-records-end

.. data-third-party-enrich-customer-records-scenarios-start

This use case has two scenarios:

#. :ref:`Limited restrictions on the use of third-party data <data-third-party-enrich-customer-records-limited>`
#. :ref:`Significant restrictions on the use of third-party data <data-third-party-enrich-customer-records-significant>`

.. data-source-third-party-enrich-customer-records-scenarios-end


.. _data-third-party-enrich-customer-records-limited:

Limited use of third-party data
--------------------------------------------------

.. data-third-party-enrich-customer-records-limited-start

When the use of third-party data has fewer restrictions, such as the ability to use:

* Regional and location details
* Reverse appends for email addresses, phone numbers, physical addresses for only existing customers of the brand
* Legal use of end user data when communicating with them via marketing campaigns

Limited restrictions are placed on the data by the vendor. Amperity cannot enforce any of these limited restrictions.

.. warning:: Unacceptable restrictions on third-party data provided to Amperity include metered use of third-party data, including tracking where the data was used, and expiration times for third-party data, such as "expires 30 days after initial use".

In this scenario:

#. Amperity ingests first-party data to the tenant and builds customer profiles with customer records.
#. Amperity syndicates customer profiles to a third-party data provider with which the customer already has a relationship.

   .. note:: It's possible for Amperity to send data to an entity like Acxiom, or some other third-party data provider. Files exported to third-party providers must include the Amperity ID.

#. Amperity ingests the customer data.
#. Amperity runs identity resolution across this data, builds a custom segment that outputs a list of net-new prospects, and then makes it available for segmentation.

.. note:: Amperity will follow a manual process for deleting third-party data.

.. data-third-party-enrich-customer-records-limited-end


.. _data-third-party-enrich-customer-records-significant:

Significant use of third-party data
--------------------------------------------------

.. data-third-party-enrich-customer-records-significant-start

When the use of third-party data has significant restrictions, such as:

* Metered usage of third-party data, including tracking data
* Expiration times for third-party data, such as expiring 30-days after initial use

Amperity must comply with any data restrictions.

In this scenario:

#. Amperity ingests first-party data to the tenant and builds customer profiles with customer records.
#. Amperity syndicates customer profiles to a third-party data provider with which the customer already has a relationship.

   .. note:: It's possible for Amperity to send data to an entity like Acxiom, or some other third-party data provider. Files exported to third-party providers must include the Amperity ID.

#. Amperity ingests the customer data.
#. Amperity runs identity resolution across this data, builds a custom segment that outputs the data, and is then sent to the third-party data vendor, after which the third-party vendor will append Amperity results to the third-party data, and then provide those results to the customer.

.. data-third-party-enrich-customer-records-significant-end


.. _data-third-party-update-addresses:

Update addresses (NCOA)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-ncoa-start
   :end-before: .. term-ncoa-end

.. data-third-party-update-addresses-start

Amperity can help identify customers that have multiple sets of contact information across multiple sets of data. NCOA data contains data about the history of address changes that can be acquired from USPS or NationalChangeOfAddress.com or from third party data providers like Acxiom.

.. warning:: NCOA data can only be used for direct-mail use cases.

In this scenario:

#. Amperity is provided NCOA data from a customer that has access to this data.
#. Amperity ingests this data as first-party customer data.
#. Amperity runs identity resolution across this data, and then creates customer profiles.
#. Amperity sends the results to the NCOA data provider, including the Amperity ID associated with each unique customer. These results must include the first name, last name, and address of the customer in a format that matches the format for the NCOA provider.
#. The NCOA provider sends back to Amperity data that contains the latest and/or updated first name, last name, address of the customer, and their Amperity ID.
#. Amperity ingests the updated data and semantically tags the updated address as an "updated address". The resulting customer profiles contain the original and updated addresses both tied to each unique customer in the data results.

.. data-third-party-update-addresses-end


.. _data-third-party-match-anonymous-visitors:

Match anonymous visitors
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-anonymous-visitor-start
   :end-before: .. term-anonymous-visitor-end

.. data-third-party-match-anonymous-visitors-start

Anonymous visitors can be matched to known customers by using a combination of IP addresses and device information, though it is possible for the same customer to browse a website using multiple devices and multiple IP addresses.

It is difficult to personalize a website experience while an anonymous visitor is browsing a website, even when that visitor can be associated to a known customer. Some degree of personalization can be provided to those customers as follow-up items, such as sending an abandoned browse or abandoned cart email.

.. data-third-party-match-anonymous-visitors-end

.. data-third-party-match-anonymous-visitors-context-start

As a brand, because anonymous visitors represent a significant percentage of traffic, it is important to make some effort to associate this traffic to known customers.

Amperity has some capability to address this issue when data sources that contain third-party data are provided to Amperity alongside more rich data sources that contain first-party data obtained directly by the customer, especially when the website traffic has a higher percentage of users that log in to the site while browsing.

Amperity generally cannot solve this type of problem all by itself and works best when paired alongside a dedicated vendor that specializes in device ID, tagging, and cookie tracking.

.. data-third-party-match-anonymous-visitors-context-end

.. data-third-party-identify-anonymous-visitors-start

.. note:: It's difficult to use third-party data to identify anonymous visitors. Legally, it is not possible to personally identify an anonymous visitor for the purpose of 1:1 communication. Amperity can perform tag, cookie, and device ID management that can be passed to downstream workflows.

.. data-third-party-identify-anonymous-visitors-end


.. _data-third-party-identify-sparse-records:

Identify sparse customer records
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sparse-customer-record-start
   :end-before: .. term-sparse-customer-record-end

.. data-third-party-identify-sparse-records-start

A brand with a large brick-and-mortar presence likely has sparse customer data associated with purchases made by customers in physical stores. A common scenario for identifying consumers from sparse customer records is to associate the sparse data with better data that contains more PII, including email addresses, physical addresses, income, gender, age, profession, and so on.

.. note:: Third-party data providers often use more PII than last name and the last 4 digits of a credit card to match a brand's record to a customer file. The approaches will vary depending on the provider.

Amperity can help with this effort, but the outcome depends on the quality of the match-rate between third- and first-party data. What can improve this scenario is to improve in-store and digital experiences in a way to encourage customers to provide additional information about themselves.

In this scenario:

#. Amperity ingests first-party data to the tenant and builds customer profiles with sparse customer records.
#. Amperity can identify clusters for rare last names, and then match on the last 4 digits of credit card data.
#. If electronic receipts are available, Amperity can use probabilistic matching to identify typos, shared usernames, and conflicting email address domains.
#. Sparse clusters area matched to point-of-sale for brands that have dense customer data sets, such as loyalty card members.
#. Amperity syndicates these stitched customer profiles to a third-party data provider with which the customer already has a relationship.

.. data-third-party-identify-sparse-records-end


.. _data-third-party-purchase-prospect-lists:

Purchase prospect lists
==================================================

.. data-third-party-purchase-prospect-lists-start

A brand with niche customer audiences, such as groups of professionals, high net-worth individuals, and so on, might want to seek out new customers by purchasing lists from third-party data providers. These lists must be a match to existing first-party data to ensure that marketing campaign spend is focused only on new prospects.

.. data-third-party-purchase-prospect-lists-end

.. data-third-party-purchase-prospect-lists-context-start

Amperity can help improve the quality of prospect lists, but this is not a common use case. The best scenario for prospect lists is net-new, where Amperity can de-duplicate existing first-party data sources to improve the quality of prospect lists.

In this scenario:

#. Amperity creates a tenant focused on the prospect lists that is different from the tenant focused on customer data.
#. Amperity ingests the same first-party data to the tenant focused on the prospect list.
#. Amperity ingests the prospect data.
#. Amperity runs identity resolution across all data, builds a custom segment that outputs a list of net-new prospects, and then sends it as a one-time output to the brand.

This approach ensures that the results for the prospect list effort are not co-mingled with the results of the core customer data platform. This is typically a one-time effort, after which the Amperity tenant dedicated to the prospect list is shut down.

.. data-third-party-purchase-prospect-lists-context-end
