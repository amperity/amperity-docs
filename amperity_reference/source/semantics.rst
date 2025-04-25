.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Apply semantic tags to build a common understanding of individual points of data across all of your data sources.

.. meta::
    :content class=swiftype name=body data-type=text:
        Apply semantic tags to build a common understanding of individual points of data across all of your data sources.

.. meta::
    :content class=swiftype name=title data-type=string:
        About semantic tags

==================================================
About semantic tags
==================================================


.. include:: ../../shared/terms.rst
   :start-after: .. term-semantic-start
   :end-before: .. term-semantic-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-semantic-type-start
   :end-before: .. term-semantic-type-end

.. semantics-groups-list-start

The following semantic groups are available for tagging fields in customer records and interaction records:

* :ref:`semantics-blocklists`
* :ref:`semantics-compliance`
* :ref:`semantics-custom`
* :ref:`semantics-db`
* :ref:`semantics-email-event`
* :ref:`semantics-email-summary`
* :ref:`semantics-fiscal-calendar`
* :ref:`semantics-itemized-transactions`
* :ref:`semantics-keys`
* :ref:`semantics-loyalty`
* :ref:`semantics-optin-preferences`
* :ref:`semantics-product-catalog`
* :ref:`semantics-profile`
* :ref:`semantics-stitch-labels`

.. semantics-groups-list-end


.. _semantics-howitworks:

How semantic tags work
==================================================

.. semantics-howitworks-start

Semantic tags must be defined for every feed that will provide profile data to Stitch. This ensures that data from rich sources of profile data are brought into Amperity in a consistent manner, which improves the outcome of the Stitch process.

Semantic tagging works like this:

#. A field in the customer's system named "fname" stores an individual's given name.
#. A field in the customer's system named "lname" stores the same individual's last name.
#. A field in the customer's system named "primary-phone" stores a phone number.
#. A field in the customer's system named "date" stores an individual's birthdate.
#. And so on.

For those semantic tags, the feed should apply semantic tags like this:

.. list-table::
   :widths: 100 100
   :header-rows: 1

   * - Input field
     - Semantic tag
   * - fname
     - given-name
   * - lname
     - surname
   * - primary-phone
     - phone
   * - date
     - birthdate
   * - ...
     - ...

This same pattern is applied to every customer data source that is brought into Amperity and it results in every single semantically-tagged field being analyzed by Amperity during the Stitch process in exactly the same way.

Amperity has built-in semantic tags for personally-identifiable information (PII), transactions, and behaviors. In addition, custom semantic tagging may be applied to fields when adding them can help identify unique individuals across massive data sets.

Profile semantic tags are used by Amperity for identity resolution, which is the process that builds a unified customer profile for all of your unique customers. All other semantic tags, such as for transactions and itemized transactions, are used to associate your customer's interactions with your brand to their individual customer profiles.

.. semantics-howitworks-end

.. semantics-howitworks-profile-tags-start

.. admonition:: What semantic tags does Stitch rely on?

   Stitch relies on the following semantic tags to be applied to customer records:

   * **given-name** (first name) and **surname** (last name). In some cases, a **full-name** is inferred (if not available).
   * Other important profile details, such as **birthdate**, **email**, and **phone**.
   * The **address**, **address2**, **city**, **state**, and **postal** tags are combined to represent a complete physical address.
   * Other location details, such as **country** and **company**.
   * Additional profile details, when available, such as **gender**, **generational-suffix** (Jr., Sr., III, etc.), and **title**.

   Stitch uses foreign keys to associate individual customers to their interactions with your brands.

.. semantics-howitworks-profile-tags-end


.. _semantics-blocklists:

Blocklist
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-bad-values-blocklist-start
   :end-before: .. term-bad-values-blocklist-end

.. semantics-blocklists-table-about-start

The following table describes recommended patterns to use when defining semantic tags for a |blocklist_bad_values|. Blocklist semantics are prefixed with **blv/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-blocklists-table-about-end

.. semantics-blocklists-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **blv/datasource**
     - String
     - Apply to the ``datasource`` column in the bad-values blocklist table.
   * - **blv/semantic**
     - String
     - Apply to the ``semantic`` column in the bad-values blocklist table.
   * - **blv/value**
     - String
     - Apply to the ``value`` column in the bad-values blocklist table.

.. semantics-blocklists-table-end


.. _semantics-compliance:

Compliance
==================================================

.. semantics-compliance-about-start

The following table describes the semantic tags that are used for CCPA and/or GDPR compliance workflows. Compliance semantics are prefixed with **compliance/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-compliance-about-end

.. semantics-compliance-request-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Column
     - Description

   * - **id**
     - **Required**

       Semantic tag: **compliance/request-id**

       Usually a unique identifier for an inbound request. **Unified_Compliance_Overview** will report results for duplicates as if they were a single request.

       This identifier is used for validation purposes, allowing compliance actions to be easily linked to specific requests.


   * - **type**
     - **Required**

       Semantic tag: **compliance/request-type**

       The request type for the compliance action. May be one of:

       **dsar**
          Report discovered records without deleting data.

       **delete**
          Delete discovered records.

       **delete_pii**
          Delete only personally identifiable information (PII) from discovered records.

        .. important:: The delete_pii request type will only delete columns that are tagged with the **compliance/pii** semantic tag.


   * - **strategy**
     - **Required**

       Semantic tag: **compliance/request-strategy**

       The request strategy for the compliance action. May be one of:

       **exact**
          Default. Find all rows that exactly match the compliance request.

       **connected_pii**
          Find all rows that exactly match the compliance request *along with* any row in a stitched table that shares an Amperity ID with those records.


   * - **email**
     - **Optional**

       Semantic tag: **compliance/request-email**

       Find all records that match an email address. This action is case-insensitive.

       The values in this field will be checked against any domain table that has the **email** semantic tag.


   * - **phone**
     - **Optional**

       Semantic tag: **compliance/request-phone**

       Find all records that match a phone number.

       The values in this field will be checked against any domain table that has the **phone** semantic tag.


   * - **address**
     - **Optional**

       Semantic tags:
        * **compliance/request-address**
        * **compliance/request-address2**
        * **compliance/request-city**
        * **compliance/request-state**
        * **compliance/request-postal**
        * **compliance/request-country**

       The values in these fields will be checked against any domain table that has the **address**, **address2**, **city**, **state**, **postal**, and/or **country** semantic tags. If a domain table only has some of these values tagged, the missing values will be treated as **NULL**. 

        .. note:: An address group contains multiple fields, but is a single entity for a compliance action. In order to match to records in domain tables, ALL values must match. Address standardization should be applied upstream of Amperity so that address can be reliably used to identify source records.

   * - **custom-key**
     - **Optional**

       Semantic tag: **compliance/request-custom-key**

       Find all records that match a custom value. This action is case-insensitive.

       The values in this field will be checked against any domain table that has the **compliance/custom-key** semantic tag.

.. semantics-compliance-request-table-end

.. semantics-compliance-table-pii-note-start

.. note:: Source keys and linkage tables identify which source table records were used to create a custom domain table record. They do not trace individual fields, so **compliance/pii** semantic tags should be applied directly to the source tables, not on the custom domain tables, if the **delete_pii** compliance type is used.

.. semantics-compliance-table-pii-note-end


.. _semantics-custom:

Custom
==================================================

.. semantics-custom-start

A custom semantic is a string that is applied as a semantic tag when configuring a feed. Some use cases for custom semantics include specifying keys (primary, customer, and foreign), assigning ordinals or namespaces to email and phone PII semantics, or arbitrary strings to capture specific customer use cases.

.. semantics-custom-end

.. semantics-custom-table-about-start

The following table describes recommended patterns to use when defining custom semantics:

.. semantics-custom-table-about-end

.. semantics-custom-table-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Custom Semantic Pattern
     - Description
   * - **itemized transactions**
     - All custom semantics that are associated with itemized transactions must be prefixed with **txn-item/**.
   * - **keys**
     - Keys are used to identify signals in source data that can be applied during the Stitch process.

   * - **loyalty-id**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-loyalty-id-start
          :end-before: .. term-loyalty-id-end

       A loyalty ID may be associated with a customer key (**ck**) or a foreign key (**fk-[namespace]**), but otherwise follows all patterns associated with PII semantics.

       .. tip:: Use additional custom semantic tags when the data contains more information about loyalty programs. Keep the prefix **loyalty-**, and then append an appropriate string to improve the user experience with downstream workflows. For example, if the data contains a field for loyalty points, use a custom semantic named **loyalty-points** to tag that field.

   * - **PII**
     - All custom semantics that are associated with transactions should be prefixed with the PII semantic to which the custom semantic is most closely associated. For example: **email-personal** and **email-work** are most closely associated with the **email** semantic.

       .. note:: In general, the use of custom semantics for PII is limited to namespace or ordinal variation of **email** and **phone**.
   * - **product**
     - All custom semantics that are associated with products must be prefixed with **pc/**.

.. semantics-custom-table-end


.. _semantics-db:

Database
==================================================

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-set-validation-rules-start
   :end-before: .. databases-database-howto-set-validation-rules-end

.. include:: ../../amperity_reference/source/databases.rst
   :start-after: .. databases-database-howto-set-validation-rules-warning-start
   :end-before: .. databases-database-howto-set-validation-rules-warning-end

.. semantics-db-table-about-start

The following semantics may be used to tag fields as required, as unique, or as both required *and* unique in database tables:

.. semantics-db-table-about-end

.. semantics-db-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **required**
     - 
     - Indicates if the field is required to have a non-NULL value.

       .. note:: This tag is assigned automatically to all fields that contain the Amperity ID.

       A field that is assigned the **required** semantic requires every value for that field within the same table to have a non-NULL value, but does not require values to be unique. NULL values will cause an error during validation. All other values, including zero-length strings, will pass validation.

       .. note::

          A field may be assigned the **db/required** *and* **db/unique** semantics. Use this only for fields that must be present *and* unique, such as for the Amperity ID.

   * - **unique**
     - 
     - Indicates if the field is required to be a unique field in the customer 360 database.

       A field that is assigned the **unique** semantic requires every value for that field within the same table to be unique. Fields with NULL values are ignored by validation, but all other values, including zero-length strings, must pass.

       .. note::

          A field may be assigned the **db/required** *and* **db/unique** semantics. Use this only for fields that must be present *and* unique, such as for the Amperity ID.

.. semantics-db-table-end


.. _semantics-email:

Email engagement
==================================================

.. semantics-email-start

Email engagement semantic tags capture email events data, such as clicks, opens, bounces, opt-ins, opt-outs, and conversions from any email service provider (ESP) data source.

#. Use :ref:`email events <semantics-email-event>` semantic tags when raw email events data is sent directly to Amperity.

   .. caution:: The data volume for email events data can be very large. Talk with your Amperity representative before applying email events semantic tags to raw email events data.

#. Use :ref:`email summary <semantics-email-summary>` semantic tags when data is aggregated prior to sending it to Amperity.

.. semantics-email-end


.. _semantics-email-event:

Email events
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-events-start
   :end-before: .. term-email-events-end

.. semantics-email-events-start

Apply email event semantic tags to data sources that contain data for raw email events. Use the built-in list of semantics when building a feed or custom domain table. Email event semantics are prefixed with **email-event/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-email-events-end

.. semantics-email-events-important-start

.. important:: Email events semantic tags should only be applied to data sources that provide at least 15 months of raw email events data. The storage requirements for this type of data can be significant. Talk with your Amperity representative about your downstream use cases prior to applying email events semantic tags to raw email events data sources.

.. semantics-email-events-important-end

.. semantics-email-event-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-email-event-table-about-end

.. semantics-email-event-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **brand**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-brand-start
          :end-before: .. email-events-brand-end

   * - **campaign-id**
     - String
     - The unique ID for a campaign.

   * - **campaign-name**
     - String
     - The name of the campaign.

   * - **email**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-email-start
          :end-before: .. email-events-email-end
   * - **event-datetime**
     - Datetime
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-datetime-start
          :end-before: .. email-events-datetime-end
   * - **event-type**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-type-start
          :end-before: .. email-events-type-end

   * - **region**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-region-start
          :end-before: .. email-events-region-end

   * - **send-id**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-send-id-start
          :end-before: .. email-events-send-id-end

   * - **treatment-id**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-treatment-id-start
          :end-before: .. term-treatment-id-end

   * - **treatment-name**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-treatment-name-start
          :end-before: .. term-treatment-name-end

.. semantics-email-event-table-end


.. _semantics-email-summary:

Email summary
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-summary-start
   :end-before: .. term-email-summary-end

.. semantics-email-summary-start

Apply email summary semantic tags to data sources that contain email summary data for how customers interact with emails sent to them from your brands. Use the built-in list of semantics when building a feed. Email summary semantics are prefixed with **email-summary/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-email-summary-end

.. semantics-email-summary-warning-start

.. warning:: Email summary semantic tags cannot be applied to raw email events data.

.. semantics-email-summary-warning-end

.. semantics-email-summary-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-email-summary-table-about-end

.. semantics-email-summary-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **brand**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-brand-start
          :end-before: .. email-events-brand-end

   * - **email**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-email-start
          :end-before: .. email-events-email-end

   * - **email-click-rate-lifetime**
     - Decimal
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-click-rate-lifetime-start
          :end-before: .. email-events-click-rate-lifetime-end

   * - **email-clicks-last-x-days**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-clicks-x-days-start
          :end-before: .. email-events-clicks-x-days-end

   * - **email-clicks-last-x-months**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-clicks-x-months-start
          :end-before: .. email-events-clicks-x-months-end

   * - **email-clicks-lifetime**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-clicks-lifetime-start
          :end-before: .. email-events-clicks-lifetime-end

   * - **email-open-rate-lifetime**
     - Decimal
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-open-rate-lifetime-start
          :end-before: .. email-events-open-rate-lifetime-end

   * - **email-opens-last-x-days**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-opens-x-days-start
          :end-before: .. email-events-opens-x-days-end

   * - **email-opens-last-x-months**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-opens-x-months-start
          :end-before: .. email-events-opens-x-months-end

   * - **email-opens-lifetime**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-opens-lifetime-start
          :end-before: .. email-events-opens-lifetime-end

   * - **engagement-frequency-last-15-months**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-engagement-frequency-15-months-start
          :end-before: .. email-events-engagement-frequency-15-months-end

   * - **engagement-status-last-15-months**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-engagement-status-15-months-start
          :end-before: .. email-events-engagement-status-15-months-end

   * - **first-email-click-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-first-click-start
          :end-before: .. email-events-first-click-end

   * - **first-email-open-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-first-open-start
          :end-before: .. email-events-first-open-end

   * - **first-email-send-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-first-send-start
          :end-before: .. email-events-first-send-end

   * - **most-recent-bounce-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-bounce-start
          :end-before: .. email-events-most-recent-bounce-end

   * - **most-recent-email-click-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-click-start
          :end-before: .. email-events-most-recent-click-end

   * - **most-recent-email-open-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-open-start
          :end-before: .. email-events-most-recent-open-end

   * - **most-recent-email-optin-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-optin-start
          :end-before: .. email-events-most-recent-optin-end

   * - **most-recent-email-optout-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-optout-start
          :end-before: .. email-events-most-recent-optout-end

   * - **most-recent-email-send-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-send-start
          :end-before: .. email-events-most-recent-send-end

   * - **region**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-region-start
          :end-before: .. email-events-region-end

.. semantics-email-summary-table-end


.. _semantics-fiscal-calendar:

Fiscal calendar
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-fiscal-calendar-start
   :end-before: .. term-fiscal-calendar-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-454-calendar-start
   :end-before: .. term-454-calendar-end

.. semantics-fiscal-calendar-start

Fiscal calendar semantics should be applied to data sources that contain the days, weeks, months, and holidays that define your brand's fiscal calendar. Fiscal calendar semantics are prefixed with **fiscal/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-fiscal-calendar-end

.. semantics-fiscal-calendar-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-fiscal-calendar-table-about-end

.. semantics-fiscal-calendar-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **calendar-date**
     - Date
     - |checkmark-required| **Required**

       The standard calendar date.

       .. important:: The field to which this semantic tag is applied must also be the primary key for the table.

   * - **day-of-week**
     - String
     - *Optional* The day of the week on which this calendar date falls.

   * - **fiscal-month**
     - String
     - |checkmark-required| **Required**

       The fiscal month that is associated with the calendar date.

   * - **fiscal-quarter**
     - String
     - |checkmark-required| **Required**

       The fiscal quarter that is associated with the calendar date.

   * - **fiscal-week-number**
     - Integer
     - |checkmark-required| **Required**

       The week within the fiscal year on which the calendar date falls. This field indicates on which month a fiscal year starts.

   * - **fiscal-week-start**
     - Date
     - |checkmark-required| **Required**

       The start of the fiscal week on which the calendar date falls.

   * - **fiscal-year**
     - Integer
     - |checkmark-required| **Required**

       The fiscal year that is associated with the calendar date.

   * - **holiday-sale-name**
     - String
     - *Optional* The holiday date (or date range) into which this calendar date falls.

.. semantics-fiscal-calendar-table-end


.. _semantics-keys:

Keys
==================================================

.. semantics-keys-start

Keys are used to identify signals in source data that can be applied during the Stitch process. For example, a table that contains customer records automatically assigns the **pk** semantic to any field identified as a primary key. For tables that contain interaction records, a foreign key is often used to associate important fields for interaction records to primary keys for customer records. This allows interaction records to be correlated with the Amperity ID as an outcome of the Stitch process even though interaction records are (typically) not processed by Stitch for the purpose of identity resolution.

.. semantics-keys-end

* :ref:`semantics-key-blocking`
* :ref:`semantics-key-customer`
* :ref:`semantics-key-foreign`
* :ref:`semantics-key-primary`
* :ref:`semantics-key-separation`


.. _semantics-key-blocking:

Blocking keys (bk)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-bk-start
   :end-before: .. term-bk-end

.. semantics-key-blocking-start

You can define custom blocking labels using **bk-[label]**, and then use them as a blocking strategy for Stitch.

.. semantics-key-blocking-end

.. semantics-key-blocking-caution-start

.. caution:: Use blocking keys carefully and be sure to verify that Stitch results contain the desired outcome.

.. semantics-key-blocking-caution-end


.. _semantics-key-customer:

Customer keys (ck)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ck-start
   :end-before: .. term-ck-end

.. semantics-key-customer-tip-start

.. tip:: What happens to customer keys in the **Unified Coalesced** table?

   * Records may have NULL customer keys.
   * There may be only one customer key per data source.

.. semantics-key-customer-tip-end


.. _semantics-key-foreign:

Foreign keys (fk)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-foreign-key-start
   :end-before: .. term-foreign-key-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-fk-start
   :end-before: .. term-fk-end

.. semantics-key-foreign-start

A foreign key semantic tag may be applied to any column in any data source, but should be associated with a field that can also act as a primary key for that data source *and* is present in other tables.

A foreign key may be used once within a table. A table may have more than one foreign key. For example, if a data source contains customer and audience identifiers, apply **fk-customer** to the customer identifier and **fk-audience** to the audience identifier.

.. semantics-key-foreign-end

.. semantics-key-foreign-default-start

Amperity is configured by default to prioritize foreign key matching over separation key unmatching.

.. semantics-key-foreign-default-end

.. semantics-key-foreign-common-start

The most common use cases for foreign keys associate fields that act like primary keys within interaction records to the primary keys within customer records, such as:

* A customer identifier for transactions and itemized transactions associated to the primary key in a loyalty table.
* A strong identifier within clickstream data to the primary key in a customer profile table.

Use foreign keys to define meaningful connections across all types of data sources to enable deterministic matching of record pairs during pairwise comparison.

.. semantics-key-foreign-common-end

.. semantics-key-foreign-tip-start

.. tip:: What happens to foreign keys in the **Unified Coalesced** table?

   * Records may have NULL foreign keys.
   * There may be multiple foreign keys in the data source, but there may not be duplicate foreign keys.
   * There may be multiple foreign keys per Amperity ID.
   * There should not be multiple Amperity IDs per foreign key.

.. semantics-key-foreign-tip-end

.. semantics-key-foreign-trivial-duplicates-start

.. note:: If foreign keys are linked together by a trivial duplicate they will appear in the **Unified Preprocessed Raw** table as a comma-separated list.

.. semantics-key-foreign-trivial-duplicates-end

.. semantics-key-foreign-important-start

.. important:: A foreign key may also be tagged as a separation key. A foreign key applies when two records have the same value for the key. A separation key applies when two records have different values for the key.

Tagging the same field as both foreign and separation keys can be useful when customer data has a strong identifier that is also associated with an important profile semantic tag, such as **phone** or **email**.

.. semantics-key-foreign-important-end

.. semantics-key-foreign-hide-pii-start

.. tip:: In an unusual case where a foreign key is associated with a field to which :ref:`a profile (PII) semantic tag is applied <semantics-profile>` be sure to configure the column created by the foreign key in customer 360 database tables to :ref:`hide values from users without permission to view PII <policies-option-restrict-pii>`.

.. semantics-key-foreign-tip-hide-pii-end


.. _semantics-key-primary:

Primary keys (pk)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-primary-key-start
   :end-before: .. term-primary-key-end

.. semantics-key-primary-caution-start

.. caution:: Amperity allows you to assign the **pk** semantic tag to more than one field in the **Feed Editor**. This is because with some data sources, such as data that contains events -- clickstream, email, web activity, mobile app activity, and so on -- often contain many fields that could be used like a primary key.

   A domain table can have only one primary key. When the **pk** semantic tag is applied to more than one field in the **Feed Editor**, those values are concatenated into a primary key, which is stored in the **_pk** field in the domain table. You should limit the number of fields to which the **pk** semantic tag is applied.

.. semantics-key-primary-caution--end

.. include:: ../../shared/terms.rst
   :start-after: .. term-pk-start
   :end-before: .. term-pk-end

.. semantics-key-primary-tip-start

.. tip:: What happens to primary keys in the **Unified Coalesced** table?

   * Each record in the **Unified Coalesced** table must have a primary key.
   * A primary key is unique within a data source, but that primary key may not be unique across all data sources.
   * There can be only one primary key per data source; each record in the **Unified Coalesced** table can be uniquely identified by the pair of values defined in the "datasource" and "pk" columns.
   * Each record in the Unified Coalesced table may only be associated with a single Amperity ID.

.. semantics-key-primary-tip-end


.. _semantics-key-separation:

Separation keys (sk)
--------------------------------------------------

.. semantics-key-separation-non-default-start

Amperity is configured by default to prioritize foreign key matching over separation key unmatching. Prioritizing separation key unmatching can help prevent address overclustering problems for groups of records with similar names and similar households.

.. semantics-key-separation-non-default-end

.. semantics-key-separation-warning-start

.. note:: To use separation keys you must configure the classifier for Stitch model selection to be set to ``:general-ordinal-sk-priority``.

.. semantics-key-separation-warning-end

.. semantics-key-separation-start

Use a separation key (sk) for deterministic unmatching of records. This prevents Stitch from matching certain types of records during pairwise comparison, which is a step in the Stitch process that scores all of the possible connections between all records in a group of records.

.. semantics-key-separation-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-sk-start
   :end-before: .. term-sk-end

.. semantics-key-separation-assign-pairs-start

A record pair is assigned a non-matching score (0.0) when separation keys contain conflicting values during pairwise comparison. A record pair is split into two clusters when both pairs contain a non-NULL value.

.. note:: The following separation keys do not consider approximately matched values to be conflicting values:

   * **sk-given-name**  For example, Mike and Michael are not conflicting values.
   * **sk-birthdate**  For example, 1981-09-08 and 1981-08-09 are not conflicting values.
   * **sk-generational-suffix**

.. semantics-key-separation-assign-pairs-end

.. semantics-key-separation-important-start

.. tip:: A separation key may also be tagged as a foreign key. Tagging the same field as a foreign and separation key can be useful when customer data has a strong identifier that is also associated with an important profile semantic tag, such as **phone** or **email**.

.. semantics-key-separation-important-end


.. _semantics-loyalty:

Loyalty programs
==================================================

.. semantics-loyalty-start

Loyalty programs help brands increase customer loyalty and provide incentives for customers to opt-in to email and SMS communication.

Adding this data to Amperity can help your brand understand the value of your loyalty program and run more effective campaigns based on how your customers interact with your loyalty program and your brand.

Amperity provides the following groups of semantic tags for use with loyalty programs:

* :ref:`Loyalty events <semantics-loyalty-events>`
* :ref:`Loyalty profiles <semantics-loyalty-profiles>`

.. semantics-loyalty-end


.. _semantics-loyalty-events:

Loyalty events
--------------------------------------------------

.. semantics-loyalty-events-start

Apply loyalty events semantic tags to data sources that contain data that captures customer interactions with your brand's loyalty program. Loyalty events semantics are prefixed with **loy-event/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-loyalty-events-end

.. semantics-loyalty-events-make-available-to-stitch-start

.. note:: Loyalty events are unique by Amperity ID and event datetime when:

   #. The **fk-loyalty-id** semantic tag is applied to the same source field as the **loy-event/loyalty-id** field.
   #. The **loy-event/email** semantic tag is applied to fields that contain email addresses.

.. semantics-loyalty-events-make-available-to-stitch-end

.. semantics-loyalty-events-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-loyalty-events-table-about-end

.. semantics-loyalty-events-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description

   * - **loyalty-id**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-id-start
          :end-before: .. loyalty-id-end

       .. important:: Apply the **fk-loyalty-id** foreign key to this field.

   * - **accrual-amount**
     - Integer
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-accrual-amount-start
          :end-before: .. loyalty-event-accrual-amount-end

   * - **accrual-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-accrual-datetime-start
          :end-before: .. loyalty-event-accrual-datetime-end

   * - **award-id**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-award-id-start
          :end-before: .. loyalty-event-award-id-end

   * - **current-balance**
     - Integer
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-current-balance-start
          :end-before: .. loyalty-event-current-balance-end

   * - **current-tier**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-current-tier-start
          :end-before: .. loyalty-event-current-tier-end

   * - **email**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-email-start
          :end-before: .. loyalty-email-end

       .. important:: In addition to the **loy-event/email** semantic tag, apply the **email** customer profile semantic tag to this field.

   * - **event-datetime**
     - Datetime
     - |checkmark-required| **Required**.

       .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-datetime-start
          :end-before: .. loyalty-event-datetime-end

   * - **event-description**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-description-start
          :end-before: .. loyalty-event-description-end

   * - **event-type**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-type-start
          :end-before: .. loyalty-event-type-end

   * - **expiration-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-expiration-datetime-start
          :end-before: .. loyalty-event-expiration-datetime-end

   * - **order-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-order-datetime-start
          :end-before: .. loyalty-event-order-datetime-end

   * - **order-id**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-order-id-start
          :end-before: .. loyalty-event-order-id-end

   * - **previous-point-balance**
     - Integer
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-previous-balance-start
          :end-before: .. loyalty-event-previous-balance-end

   * - **previous-tier**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-previous-tier-start
          :end-before: .. loyalty-event-previous-tier-end

   * - **redemption-amount**
     - Decimal
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-redemption-amount-start
          :end-before: .. loyalty-event-redemption-amount-end

   * - **redemption-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-redemption-datetime-start
          :end-before: .. loyalty-event-redemption-datetime-end

   * - **reservation-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-reservation-datetime-start
          :end-before: .. loyalty-event-reservation-datetime-end

   * - **reservation-id**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-reservation-id-start
          :end-before: .. loyalty-event-reservation-id-end

   * - **tier-end-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-tier-end-datetime-start
          :end-before: .. loyalty-event-tier-end-datetime-end

   * - **tier-start-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-event-tier-start-datetime-start
          :end-before: .. loyalty-event-tier-start-datetime-end

.. semantics-loyalty-events-table-end


.. _semantics-loyalty-profiles:

Loyalty profiles
--------------------------------------------------

.. semantics-loyalty-profiles-start

Apply loyalty profile semantic tags to data sources that contain data that provides details about customers who belong to your brand's loyalty program. Loyalty profile semantics are prefixed with **loy/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-loyalty-profiles-end

.. semantics-loyalty-profiles-make-available-to-stitch-start

.. note:: Loyalty profiles are unique by Amperity ID when:

   #. The **fk-loyalty-id** semantic tag is applied to the same source field as the **loy/loyalty-id** field.
   #. The **loy/email** semantic tag is applied to fields that contain email addresses.
   #. The **loy/birthdate** semantic tag is applied to fields that contain birthdates.

.. semantics-loyalty-profiles-make-available-to-stitch-end

.. semantics-loyalty-profiles-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-loyalty-profiles-table-about-end

.. semantics-loyalty-profiles-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description

   * - **loyalty-id**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-id-start
          :end-before: .. loyalty-id-end

       .. important:: Apply the **fk-loyalty-id** foreign key to this field.

   * - **birthdate**
     - Date
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-birthdate-start
          :end-before: .. loyalty-birthdate-end

       .. important:: In addition to the **loy/birthdate** semantic tag, apply the **birthdate** customer profile semantic tag to this field.

   * - **current-balance**
     - Integer
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-balance-start
          :end-before: .. loyalty-current-balance-end

   * - **current-balance-expiration-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-balance-expiration-datetime-start
          :end-before: .. loyalty-current-balance-expiration-datetime-end

   * - **current-tier**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-tier-start
          :end-before: .. loyalty-current-tier-end

   * - **current-tier-expiration-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-tier-expiration-datetime-start
          :end-before: .. loyalty-current-tier-expiration-datetime-end

   * - **current-tier-start-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-tier-start-datetime-start
          :end-before: .. loyalty-current-tier-start-datetime-end

   * - **email**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-email-start
          :end-before: .. loyalty-email-end

       .. important:: In addition to the **loy/email** semantic tag, apply the **email** customer profile semantic tag to this field.

   * - **is-opted-in**
     - Boolean
     - |checkmark-required| **Required**.

       .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-is-opted-in-start
          :end-before: .. loyalty-is-opted-in-end

   * - **latest-opt-out-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-latest-opt-out-datetime-start
          :end-before: .. loyalty-latest-opt-out-datetime-end

   * - **latest-opted-in-datetime**
     - Datetime
     - |checkmark-required| **Required**.

       .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-latest-opted-in-datetime-start
          :end-before: .. loyalty-latest-opted-in-datetime-end

   * - **latest-update-datetime**
     - Datetime
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-latest-update-datetime-start
          :end-before: .. loyalty-latest-update-datetime-end

   * - **lifetime-balance**
     - Integer
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-lifetime-balance-start
          :end-before: .. loyalty-lifetime-balance-end

   * - **next-tier**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-next-tier-start
          :end-before: .. loyalty-next-tier-end

   * - **sign-up-channel**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-sign-up-channel-start
          :end-before: .. loyalty-sign-up-channel-end

   * - **sign-up-method**
     - String
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-sign-up-method-start
          :end-before: .. loyalty-sign-up-method-end

   * - **spend-to-keep-tier**
     - Decimal
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-spend-to-keep-tier-start
          :end-before: .. loyalty-spend-to-keep-tier-end

   * - **spend-to-next-tier**
     - Decimal
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-spend-to-next-tier-start
          :end-before: .. loyalty-spend-to-next-tier-end

.. semantics-loyalty-profiles-table-end


.. _semantics-optin-preferences:

Opt-in preferences
==================================================

.. semantics-optin-preferences-start

Semantic tags for opt-in preferences capture your customer's opt-in status. Use them to determine when and how your brand can use email and SMS to communicate with your customers.

#. Use :ref:`email opt-in <semantics-optin-email-status>` semantic tags for data sources that contain your customer's opt-in preferences, the programs they have opted-in to, and their preferences for how your brand should communicate with them using their email address.

#. Use :ref:`SMS opt-in <semantics-optin-sms-status>` semantic tags for data sources that contain your customer's opt-in preferences, the programs they have opted-in to, and their preferences for how your brand should communicate with them using their phone number.

.. semantics-optin-preferences-end


.. _semantics-optin-email-status:

Email opt-in status
--------------------------------------------------

.. semantics-optin-email-start

Apply email opt-in status semantic tags to data sources that contain data that indicates when customers have given their consent to your brand for using their email address as part of your marketing campaign. Email opt-in status semantics are prefixed with **email-opt/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-optin-email-end

.. semantics-optin-email-table-important-start

.. warning:: Tables that contain data for email opt status *should not* also be tagged with :ref:`foreign key <semantics-key-foreign>` or :ref:`customer profile <semantics-profile>` semantic tags. Only use **email-opt/** semantic tags with tables that contain email opt status data. An Amperity ID will be available in the **Email Opt Status** table in the customer 360 database.

.. semantics-optin-email-table-important-end

.. semantics-optin-email-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-optin-email-table-about-end

.. semantics-optin-email-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **brand**
     - String
     - |checkmark-recommended| **Recommended** (when your tenant has data for multiple brands).

       The brand to which the opt-in status applies.

   * - **email**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

   * - **email-frequency**
     - String
     - The preferred frequency for email messages.

   * - **email-program**
     - String
     - The email program to which the customer has opted-in.

   * - **is-email-opted-in**
     - Boolean
     - |checkmark-required| **Required**.

       Indicates whether a customer has given consent to being contacted by your brand using the customer's email address.

       .. important:: The field to which this semantic tag is applied **must** have a Boolean data type. If the data source to which you want to apply this tag is not a Boolean, use a custom domain table to shape the data into a Boolean data type, and then apply this semantic tag.

   * - **language-preference**
     - String
     - The customer's preferred language for email messages.

   * - **region**
     - String
     - The region to which the opt-in status applies.

.. semantics-optin-email-table-end


.. _semantics-optin-sms-status:

SMS opt-in status
--------------------------------------------------

.. semantics-optin-sms-start

Apply SMS opt-in status semantic tags to data sources that contain data that indicates when customers have given their consent to your brand for using their phone number as part of your marketing campaign. SMS opt-in status semantics are prefixed with **sms-opt/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-optin-sms-end

.. semantics-optin-sms-table-important-start

.. warning:: Tables that contain data for email opt status *should not* also be tagged with :ref:`foreign key <semantics-key-foreign>` or :ref:`customer profile <semantics-profile>` semantic tags. Only use **sms-opt/** semantic tags with tables that contain SMS opt status data. An Amperity ID will be available in the **SMS Opt Status** table in the customer 360 database.

.. semantics-optin-sms-table-important-end

.. semantics-optin-sms-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-optin-sms-table-about-end

.. semantics-optin-sms-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **brand**
     - String
     - |checkmark-recommended| **Recommended** (when your tenant has data for multiple brands).

       The brand to which the opt-in status applies.

   * - **is-sms-opted-in**
     - Boolean
     - |checkmark-required| **Required**

       Indicates whether a customer has opted-in to being contacted by your brand using the customer's phone number.

       .. important:: The field to which this semantic tag is applied **must** have a Boolean data type. If the data source to which you want to apply this tag is not a Boolean, use a custom domain table to shape the data into a Boolean data type, and then apply this semantic tag.

   * - **language-preference**
     - String
     - The customer's preferred language for SMS messages.

   * - **phone**
     - String
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

   * - **region**
     - String
     - The region to which the opt-in status applies.

   * - **sms-frequency**
     - String
     - The preferred frequency for SMS communications.

   * - **sms-program**
     - String
     - The SMS program to which the customer has opted-in.

.. semantics-optin-sms-table-end


.. _semantics-product-catalog:

Product catalog
==================================================

.. semantics-product-catalog-start

Product catalog semantics may be applied to data sources that contain product catalog data. Product semantics may applied alongside other semantics, depending on the data source. Use the built-in list of semantics when building a feed. Product catalog semantics are prefixed with **pc/** in the semantics dropdown menu in the **Feed Editor**. Use the combination of product semantic tags that best describes the structure of your product catalog.

.. semantics-product-catalog-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-product-catalog-table-with-ampiq-start
   :end-before: .. term-unified-product-catalog-table-with-ampiq-end

.. semantics-product-catalog-table-important-start

.. tip:: You may choose to :ref:`apply product catalog semantic tags directly to data sources that contain itemized transaction data <semantics-itemized-transactions>` using a **txn-item/** as the prefix instead of **pc/**.

.. semantics-product-catalog-table-important-start

.. semantics-product-catalog-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-product-catalog-table-about-end

.. semantics-product-catalog-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description

   * - **product-brand**
     - String
     - Optional. The brand name of a product or item.

   * - **product-brand-id**
     - String
     - Optional. The ID for the brand name of a product or item.

   * - **product-category**
     - String
     - |checkmark-recommended| **Recommended**

       A category to which a product belongs. Use this semantic tag to identify how a customer categorizes individual products within their product catalog.

   * - **product-category-id**
     - String
     - Optional. The ID for the category to which a product belongs.

   * - **product-class**
     - String
     - Optional. The name of the class (or grouping) to which a product or item belongs.

   * - **product-class-id**
     - String
     - Optional. The ID for the name of the class (or grouping) to which a product or item belongs.

   * - **product-collection**
     - String
     - Optional. The name of the collection to which a product or item belongs.

   * - **product-collection-id**
     - String
     - Optional. The ID for the name of the collection to which a product or item belongs.

   * - **product-color**
     - String
     - Optional. The color of a product or item.

   * - **product-color-id**
     - String
     - Optional. The ID for the color of a product or item.

   * - **product-department**
     - String
     - Optional. The department to which a product or item belongs.

   * - **product-department-id**
     - String
     - Optional. The ID for the department to which a product or item belongs.

   * - **product-description**
     - String
     - |checkmark-recommended| **Recommended**

       A description of the product.

   * - **product-division**
     - String
     - Optional. The division to which a product or item belongs.

   * - **product-division-id**
     - String
     - Optional. The ID for the division to which a product or item belongs.

   * - **product-fabric**
     - String
     - Optional. The fabric used for a product or item.

   * - **product-fabric-id**
     - String
     - Optional. The ID for the fabric used for a product or item.

   * - **product-gender**
     - String
     - |checkmark-recommended| **Recommended**

       Apply this as a custom semantic tag to a fields that contain a list of gender options for products. For example: F, M, unisex, NULL (for unknown).

   * - **product-group**
     - String
     - Optional. The group to which a product or item belongs.

   * - **product-id**
     - String
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-product-id-start
          :end-before: .. term-product-id-end

       .. important:: Predictive modeling requires a product catalog to contain between 20-2000 unique product IDs. A product ID is often associated with a stock keeping unit (SKU).

          .. include:: ../../shared/terms.rst
             :start-after: .. term-sku-start
             :end-before: .. term-sku-end

          For example, a shirt with the same color and material, but with three different sizes would be represented by three unique SKUs and would also be represented by three unique product IDs.

          Each customer has their own definition for product IDs and SKUs. Be sure to understand this definition before applying semantic tags to fields with product IDs to ensure they accurately reflect the customer's definition *and* meet the requirements for predictive modeling (if enabled).

   * - **product-material**
     - String
     - Optional. The material used for a product or item.

   * - **product-material-id**
     - String
     - Optional. The ID for the material used for a product or item.

   * - **product-msrp**
     - String
     - Optional. The manufacturer's suggested retail price (MSRP) for a product or item.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-msrp-start
          :end-before: .. term-msrp-end

   * - **product-name**
     - String
     - Optional. The name of the product or item.

   * - **product-season**
     - String
     - Optional. The season to which a product or item is associated.

   * - **product-season-id**
     - String
     - Optional. The ID for the season to which a product or item is associated.

   * - **product-silhouette**
     - String
     - Optional.

   * - **product-size**
     - String
     - Optional. The size of a product or item.

   * - **product-size-id**
     - String
     - Optional. The ID for the size of a product or item.

   * - **product-sku**
     - String
     - Optional. The stock keeping unit, or SKU, for the product or item.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-sku-start
          :end-before: .. term-sku-end

   * - **product-style**
     - String
     - Optional. The style of a product or item.

   * - **product-subcategory**
     - String
     - |checkmark-recommended| **Recommended**

       The subcategory or secondary variant to which a product belongs.

   * - **product-subcategory-id**
     - String
     - Optional. The ID for the subcategory or secondary variant to which a product belongs.

   * - **product-subclass**
     - String
     - Optional. The subclass to which a product or item is assigned.

   * - **product-subclass-id**
     - String
     - Optional. The ID for the subclass to which a product or item is assigned.

   * - **product-subdepartment**
     - String
     - Optional. The sub-department to which a product or item is assigned.

   * - **product-subdepartment-id**
     - String
     - Optional. The ID for the sub-department to which a product or item is assigned.

   * - **product-type**
     - String
     - Optional. The type assigned to a product or item.

   * - **product-upc**
     - String
     - Optional. The UPC code for the product or item.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-upc-code-start
          :end-before: .. term-upc-code-end

.. semantics-product-catalog-table-end


.. _semantics-profile:

Profile (PII)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-semantic-start
   :end-before: .. term-pii-semantic-end

.. semantics-profile-start

Profile semantics should be applied to customer records that contain three (or more) good sources of PII data. Profile semantics should be applied to interaction records only when customer records are stored alongside transaction details *and* when there are three (or more) good sources of PII data.

.. semantics-profile-end

.. semantics-profile-table-about-start

The following table lists the tags available to this semantic group:

.. semantics-profile-table-about-end

.. semantics-profile-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **address**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address-start
          :end-before: .. term-address-end

   * - **address2**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address2-start
          :end-before: .. term-address2-end

   * - **birthdate**
     - Date
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-birthdate-start
          :end-before: .. term-birthdate-end

       .. tip:: A field that is tagged with the **birthdate** semantic tag will return an error when the feed is saved and the data type is not set to Date.

   * - **city**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-city-start
          :end-before: .. term-city-end

   * - **company**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-company-start
          :end-before: .. term-company-end

       .. note:: Do not use the **company** semantic tag when data that belongs to a business is stitched. The **company** semantic tag should be applied to fields that represent an individual's employer.

          Use the **full-name** semantic tag on the business name when stitching data that belongs to a business.

   * - **country**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-country-start
          :end-before: .. term-country-end

       .. important:: A field to which the **country** semantic tag is applied is added to the **Unified Coalesced** table, but is otherwise ignored by Stitch.

   * - **create-dt**
     - 
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-create-dt-start
          :end-before: .. term-create-dt-end

   * - **email**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

   * - **full-name**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-full-name-start
          :end-before: .. term-full-name-end

   * - **gender**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-gender-start
          :end-before: .. term-gender-end

       Supported values for fields associated with the **gender** semantic tag include:

       * F
       * FEMALE (is normalized to F)
       * M
       * MALE (is normalized to M)
       * MAN (is normalized to M)
       * NONE (is treated as NULL)
       * WOMAN (is normalized to F)
       * X
       * NONBINARY (is normalized to X)
       * NON-BINARY (is normalized to X)
       * ENBY (is normalized to X)
       * NB (is normalized to X)
       * OTHER (is normalized to X)

   * - **generational-suffix**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-generational-suffix-start
          :end-before: .. term-generational-suffix-end

       .. caution:: The **generational-suffix** semantic tag should only be applied once per feed and only to a field that contains the suffix separated from the first and last names.

   * - **given-name**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end

       .. caution:: The **given-name** semantic tag may only be applied once per feed.

   * - **phone**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

       .. tip:: A field that is tagged with the **phone** semantic tag will return an error when the feed is saved and the data type is not set to String.

       .. important::

          Amperity uses the last 10-digits of phone numbers for identity resolution.

          Use the `input validation report <https://docs.amperity.com/operator/validate_inputs.html>`__ to find data sources that contain records with phone numbers that exceed 10 digits.

          You should exclude extensions from phone numbers whenever possible. You may use a custom domain table to apply additional formatting to phone numbers, such as removing extensions.

          Alternately provide data sources to Amperity that have already removed the extensions or have moved them into a different field.


   * - **postal**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end

       A full 9-digit zip code is derived from fields that contain zip code data.

       .. tip:: A field that is tagged with the **postal** semantic tag will return an error when the feed is saved and the data type is not set to String.

   * - **state**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end

   * - **surname**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end

       .. caution:: The **surname** semantic tag may only be applied once per feed.

   * - **title**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-title-start
          :end-before: .. term-title-end

   * - **update-dt**
     - 
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-update-dt-start
          :end-before: .. term-update-dt-end

.. semantics-profile-table-end


.. _semantics-stitch-labels:

Stitch labels
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-stitch-labels-start
   :end-before: .. term-stitch-labels-end

.. semantics-stitch-labels-table-about-start

The following table describes recommended patterns to use when defining semantic tags for |stitch_labels|.

.. semantics-stitch-labels-table-about-end

.. semantics-stitch-labels-table-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Stitch Labels Semantic Pattern
     - Description
   * - **sl/datasource**
     - Apply this semantic tag to the ``datasource`` column.

   * - **sl/label-id**
     - Apply this semantic tag to the ``label_id`` column.

   * - **sl/partition-id**
     - Apply this semantic tag to the ``partition_id`` column.

   * - **sl/semantic**
     - Apply this semantic tag to columns that are associated with the matching value, for example to a column that matches the **email** semantic tag.

   * - **sl/value**
     - Apply this semantic tag to the ``value`` column.

.. semantics-stitch-labels-table-end


.. _semantics-subscriber-status:

Subscriber status
==================================================

.. semantics-subscriber-status-start

Subscriber status -- whether a customer has opted-in or opted-out to receiving communication -- can be difficult to track when it is not consolidated into a single table within your customer 360 database. Use subscriber status semantic tags to consolidate email and/or phone subscriber status information into a single table.

The following semantic tags consolidate your customers' email and phone subscriber status:

* :ref:`semantics-subscriber-status-email`
* :ref:`semantics-subscriber-status-sms`

.. semantics-subscriber-status-end


.. _semantics-subscriber-status-email:

Email
--------------------------------------------------

.. semantics-subscriber-status-email-start

Use email subscriber status semantic tags to consolidate opt-in and opt-out data for email addresses into a single table. Email semantics are prefixed with **email-opt/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-subscriber-status-email-end

.. semantics-subscriber-status-email-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-subscriber-status-email-table-about-end

.. semantics-subscriber-status-email-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **brand**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-brand-start
          :end-before: .. email-events-brand-end

   * - **email**
     - String
     - |checkmark-required| **Required**

       The email address to which a marketing may (or may not) be sent.

   * - **is-email-opted-in**
     - Boolean
     - |checkmark-required| **Required**

       Indicates if the customer associated with an email address has opted-in or opted-out to receiving email from your brand.

       .. note:: You may need to use a custom domain table to ensure that the field that returns your customers email opt status is a Boolean field. Apply this semantic tag to the field in the custom domain table.

   * - **region**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-region-start
          :end-before: .. email-events-region-end

.. semantics-subscriber-status-email-table-end


.. _semantics-subscriber-status-sms:

Phone (SMS)
--------------------------------------------------

.. semantics-subscriber-status-sms-start

Use phone (SMS) subscriber status semantic tags to consolidate opt-in and opt-out data for phone numbers into a single table. Phone (SMS) semantics are prefixed with **sms-opt/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-subscriber-status-sms-end

.. semantics-subscriber-status-sms-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-subscriber-status-sms-table-about-end

.. semantics-subscriber-status-sms-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **brand**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-brand-start
          :end-before: .. email-events-brand-end

   * - **is-sms-opted-in**
     - Boolean
     - |checkmark-required| **Required**

       Indicates if the customer associated with a phone number has opted-in or opted-out to receiving messages from your brand.

       .. note:: You may need to use a custom domain table to ensure that the field that returns your customers phone opt status is a Boolean field. Apply this semantic tag to the field in the custom domain table.

   * - **phone**
     - String
     - |checkmark-required| **Required**

       The phone number to which a marketing may (or may not) be sent.

   * - **region**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-region-start
          :end-before: .. email-events-region-end

.. semantics-subscriber-status-sms-table-end


.. _semantics-itemized-transactions:

Transactions
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-itemized-transactions-semantic-start
   :end-before: .. term-itemized-transactions-semantic-end

.. semantics-itemized-transactions-start

Itemized transaction semantics should be applied to data sources that contain records for individual items in a transaction. Itemized transaction semantics may applied alongside other semantics, depending on the data source. Use the built-in list of semantics when building a feed.

Itemized transaction semantics are prefixed with **txn-item/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-itemized-transactions-end

.. semantics-itemized-transactions-important-start

.. important:: This collection of semantic tags is used by Amperity to build the :ref:`Unified Itemized Transactions table <data-tables-unified-itemized-transactions>`. Each semantic tag is directly associated with a column in that table. For example, values identified by the **is-cancellation**, **item-cost**, and **order-id** semantic tags are added to the **is_cancellation**, **item_cost**, and **order_id** columns, respectively.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-unified-itemized-transactions-table-start
      :end-before: .. term-unified-itemized-transactions-table-end

   Carefully review the data in the **Unified Itemized Transactions** table, including column values that are calculated from values in other columns in this table or the :ref:`Unified Transactions table <data-tables-unified-transactions>`, to verify their accuracy and to ensure that associated semantic tags have been applied correctly.

.. semantics-itemized-transactions-important-end

.. semantics-itemized-transactions-table-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. semantics-itemized-transactions-table-about-end

.. semantics-itemized-transactions-table-start

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Semantic name
     - Datatype
     - Description
   * - **[custom-semantic]**
     - String
     - |checkmark-required| **Required**

       Use a foreign key (recommended) *or* a custom semantic tag (such as ``customer-id``) within interaction records to associate them to the Amperity ID.

       .. important:: See **fk-[namespace]**. At least one field must have the **[custom-semantic]** or **fk-[namespace]** semantic tags applied to it to support downstream processing requirements for interaction records. You may apply more than one, or use a combination, of these semantic tags.

       When a custom semantic tag is added to itemized transactions data it:

       * Must be a unique customer identifier that can be used to join interaction records (transactions and itemized transactions) to tables that contain the Amperity ID.
       * Must be unique for each order ID in the **Unified Itemized Transactions** table.

   * - **currency**
     - String
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-currency-start
          :end-before: .. term-currency-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. currency-must-be-consistent-across-orders-start
             :end-before: .. currency-must-be-consistent-across-orders-end

   * - **digital-channel**
     - String
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-digital-channel-start
          :end-before: .. term-digital-channel-end

       .. note:: This semantic tag should only be used when **purchase-channel** specifies an online channel.

   * - **fk-[namespace]**
     - String
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-fk-start
          :end-before: .. term-fk-end

       A namespaced foreign key must be present in interaction records that contain transactions data. A foreign key may used along with a customer ID.

       .. important:: See **[custom-semantic]**. At least one field must have the **fk-[namespace]** or **[custom-semantic]** semantic tags applied to it to support downstream processing requirements for interaction records. You may apply more than one, or use a combination, of these semantic tags.

       When a foreign key is added to transactions data it:

       * Must match a foreign key in a table that is output by Stitch.
       * Must be well-distributed across the data source (a high percentage of values must not be 0).
       * Must be unique for each order ID in the **Unified Itemized Transactions** table.
       * May contain a ``NULL`` value.

   * - **is-cancellation**
     - Boolean
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-is-canceled-start
          :end-before: .. term-is-canceled-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-is-canceled-important-note-regarding-possible-values-start
          :end-before: .. term-is-canceled-important-note-regarding-possible-values-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. is-canceled-is-return-cannot-be-same-start
             :end-before: .. is-canceled-is-return-cannot-be-same-end

   * - **is-return**
     - Boolean
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-is-return-start
          :end-before: .. term-is-return-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-is-return-important-note-regarding-possible-values-start
          :end-before: .. term-is-return-important-note-regarding-possible-values-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. is-canceled-is-return-cannot-be-same-start
             :end-before: .. is-canceled-is-return-cannot-be-same-end

   * - **item-cost**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-cost-start
          :end-before: .. term-item-cost-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **item-discount-amount**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-discount-amount-start
          :end-before: .. term-item-discount-amount-end

       This value should equal item quantity multiplied by unit discount amounts.

       This value is used by Amperity for discount sensitivity analysis.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **item-discount-percent**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-discount-percent-start
          :end-before: .. term-item-discount-percent-end

       This value is used by Amperity for discount sensitivity analysis.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. between-zero-and-one-start
             :end-before: .. between-zero-and-one-end

   * - **item-list-price**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-list-price-start
          :end-before: .. term-item-list-price-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-msrp-start
          :end-before: .. term-msrp-end

       This value should equal item revenue plus item discount amount.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **item-profit**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-profit-start
          :end-before: .. term-item-profit-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **item-quantity**
     - Integer
     - |checkmark-required| **Required** 

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-quantity-start
          :end-before: .. term-item-quantity-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. less-than-or-equal-to-zero-semantic-is-return-canceled-start
             :end-before: .. less-than-or-equal-to-zero-semantic-is-return-canceled-end

   * - **item-revenue**
     - Decimal
     - |checkmark-required| **Required** 

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-revenue-start
          :end-before: .. term-item-revenue-end

       This value should equal item list price minus item discount amount.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. less-than-or-equal-to-zero-semantic-is-return-canceled-start
             :end-before: .. less-than-or-equal-to-zero-semantic-is-return-canceled-end

   * - **item-subtotal**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-subtotal-start
          :end-before: .. term-item-subtotal-end

       This value should equal unit list price times item quantity.

       This value is used by Amperity to calculate discounts for discount sensitivity analysis.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **item-tax-amount**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-item-tax-amount-start
          :end-before: .. term-item-tax-amount-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **order-datetime**
     - Datetime
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-order-date-start
          :end-before: .. term-order-date-end

       The order date:

       * Must have a consistent time zone across all dates in the transactions data.
       * Should be a local time zone.
       * Should be a timestamp, which is converted to datetime automatically when a date is present in the timestamp.
       * When **is-return** is TRUE, the date and time on which the order was returned.
       * When **is-cancellation** is TRUE, the date and time on which the order was canceled.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. related-order-dates-should-be-added-to-upc-start
             :end-before: .. related-order-dates-should-be-added-to-upc-end

   * - **order-discount-amount**
     - Decimal
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-order-discount-amount-start
          :end-before: .. term-order-discount-amount-end

       This tag provides the following data:

       * The total amount per order appears as the same amount on each row.
       * The pro-rated amount per line item appears as either a different amount or 0 per row.

       .. note:: This field appears as a positive for a purchase and a 0 for a cancellation or return for minimum, maximum, and total order discount amounts in the Unified Transactions table.

   * - **order-id**
     - String
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-order-id-start
          :end-before: .. term-order-id-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. order-id-should-never-change-start
             :end-before: .. order-id-should-never-change-end

       .. important::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. recycled-order-ids-not-guaranteed-to-be-unique-start
             :end-before: .. recycled-order-ids-not-guaranteed-to-be-unique-end

   * - **payment-method**
     - String
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-payment-method-start
          :end-before: .. term-payment-method-end

   * - **Product catalogs**
     - String
     - *Optional*

       Product catalog semantics may be applied to data sources that contain product catalog data. There are two sets of product catalog semantic tags: **txn-item/** and **pc/**.

       #. You may use **txn-item/** product catalog semantic tags when product catalog data appears within data sources that contain details about your product catalog when it exists alongside details about orders and items.

          Fields to which **txn-item/** product catalog semantic tags are applied will be built into the **Unified Itemized Transactions** table in your customer 360 database.

       #. You may use **pc/** product catalog semantic tags in any data source that contains details about your product catalog. Fields to which the **pc/** product catalog semantic tags are applied will be built into the **Unified Product Catalog** table.

       .. important:: The names of the semantic tags that are available for product catalogs are identical. For example: "product-brand", "product-category", and "product-gender". The difference is the prefix that you choose to use and the pattern your tenant chooses for defining your product catalog within Amperity. You should determine which pattern you want to use early in your configuration and deployment process. Talk with your Amperity representative if you have questions about the best ways to approach this within your tenant.

       To review the descriptions for all of the product catalog semantic tags you may prefix with **txn-item/** refer to the section in this topic about product catalog semantic tags.

   * - **product-id**
     - String
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-product-id-start
          :end-before: .. term-product-id-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-sku-start
          :end-before: .. term-sku-end

       For example, a shirt with the same color and material, but with three different sizes would be represented by three unique SKUs and would also be represented by three unique product IDs.

       For data that contains itemized transactions, where a single transaction includes more than one of the same product, the product ID must appear only once per order ID in the **Unified Itemized Transactions** table. Multiple instances of the same product must be added to the item quantity in the same row.

       .. caution:: Every customer has their own definition for SKUs and product IDs. Be sure to understand this definition before applying semantic tags to fields with product IDs to ensure they accurately reflect the customer's definition.

   * - **purchase-brand**
     - String
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-purchase-brand-start
          :end-before: .. term-purchase-brand-end

       .. caution:: This semantic tag should only be used when interaction records contain transaction data for more than one brand.

   * - **purchase-channel**
     - String
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-purchase-channel-start
          :end-before: .. term-purchase-channel-end

   * - **store-id**
     - String
     - |checkmark-required| **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-store-id-start
          :end-before: .. term-store-id-end

   * - **unit-cost**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-cost-start
          :end-before: .. term-unit-cost-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **unit-discount-amount**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-discount-amount-start
          :end-before: .. term-unit-discount-amount-end

       This discount is often applied to all units of the same item within a single transaction.

       This value is used by Amperity for discount sensitivity analysis.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **unit-list-price**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-list-price-start
          :end-before: .. term-unit-list-price-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-msrp-start
          :end-before: .. term-msrp-end

       This value should equal the unit discount amount plus the unit subtotal.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **unit-profit**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-profit-start
          :end-before: .. term-unit-profit-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **unit-revenue**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-revenue-start
          :end-before: .. term-unit-revenue-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. less-than-or-equal-to-zero-semantic-is-return-canceled-start
             :end-before: .. less-than-or-equal-to-zero-semantic-is-return-canceled-end

   * - **unit-subtotal**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-subtotal-start
          :end-before: .. term-unit-subtotal-end

       This value is used by Amperity to calculate discounts for discount sensitivity analysis.

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

   * - **unit-tax-amount**
     - Decimal
     - *Optional*

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unit-tax-amount-start
          :end-before: .. term-unit-tax-amount-end

       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. greater-than-or-equal-to-zero-purchases-start
             :end-before: .. greater-than-or-equal-to-zero-purchases-end

.. semantics-itemized-transactions-table-end
