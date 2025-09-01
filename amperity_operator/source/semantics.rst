.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        How semantic tags work and how you should apply them to the individual fields across all of the data sources your brand pulls to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        How semantic tags work and how you should apply them to the individual fields across all of the data sources your brand pulls to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Apply semantic tags

==================================================
Apply semantic tags
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-semantic-start
   :end-before: .. term-semantic-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-semantic-tag-start
   :end-before: .. term-semantic-tag-end

.. semantics-noetl-start

.. admonition:: Extract, load, transform (ELT)

   An important benefit of semantic tagging is that it allows raw data to be provided directly to Amperity. This avoids a traditional and more expensive extract, transform, and load (ETL) operations. Amperity extracts, loads, and then transforms raw data from any number of data sources.

.. semantics-noetl-end

.. semantics-reference-links-start

.. vale off

The following groups of semantic tags are available: |semantics_customer_profile|, email address (|semantics_email_events|, |semantics_email_events_summary|, and |semantics_email_optin|), |semantics_product_catalog|, |semantics_keys_fk|, loyalty programs (|semantics_loyalty_profiles| and |semantics_loyalty_events|), |semantics_sms_optin|, and |semantics_transactions|.

.. vale on

.. semantics-reference-links-end

**To apply semantic tags**

.. semantics-steps-generic-start

#. From the **Sources** page, open the menu for a feed, and then select **Edit**. The **Feed Editor** page opens.

   .. note:: The **Feed Editor** page opens automatically after a file has completed loading when setting up a new feed.
#. Review all of the profile semantic tags that were automatically applied by Amperity to ensure that each tag was matched correctly.

   .. tip::

      .. include:: ../../shared/terms.rst
         :start-after: .. term-update-dt-start
         :end-before: .. term-update-dt-end

      The field that is associated with the **update-dt** semantic tag *should also* be selected as the field that is associated with the LAST UPDATED FIELD dropdown list.
#. Apply any other semantic tags, such as for transactions, itemized transactions, or custom semantic tags, as appropriate.

   .. important:: Semantic tags for interactions records, such as transactions, itemized transactions, loyalty profiles, and email events, may need to be reshaped prior to applying semantic tags. Use custom domain tables and reshape the data using domain SQL prior to applying semantic tags.

      In those situations, leave the semantic tag fields empty in the **Feed Editor**, build a custom domain table that shapes the fields to align to the semantic tagging requirements, and then apply semantic tags.
#. Click **Activate**.

.. semantics-steps-generic-end


.. _semantics-profile:

Profiles
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-semantic-start
   :end-before: .. term-pii-semantic-end

.. semantics-profile-important-start

.. important:: It is important to correctly tag all fields that contain PII, foreign keys, and certain other field types to ensure that the outcome of the Stitch process is as accurate as possible.

   The Stitch process relies on accurate semantic tagging to which a series of blocking strategies are applied that are used to identify all of the clusters of data that represent a unique individual in your data.

.. semantics-profile-important-end

.. semantics-profile-about-start

.. vale off

Semantic tagging is done while configuring a feed. A feed tells Amperity how to map your data to a series of standardized terms used by Amperity for PII data. These terms include:

* **email** (for email addresses)
* **phone** (for phone numbers)
* **given-name**, **surname**, **title**, **generational-suffix**, and **full-name** for all types of name combinations
* **address**, **city**, **state**, **postal** for addresses
* **birthdate** (for birthdays)

.. vale on

.. warning:: Fields to which the **postal** and **phone** semantic tags are applied must be configured to have a String data type. Fields to which the **birthdate** semantic tag is applied must be configured to have a Date data type. If these fields do not have the correct data type Amperity will show an error when saving the feed.

Custom semantic tags allow for additional tagging of certain types of fields, such as a field that identifies a loyalty membership ID. Use foreign keys to apply consistently across customer tables for certain types of identifiers.

One custom semantic tag is required by the **Merged Customers** table: **update-dt**. Use the **Last updated field** dropdown in the **Feed Editor** to specify the field to which this tag will be applied.

.. important:: Make sure that you do not miss any opportunities to correctly tag customer data for all semantics, custom semantics, and foreign keys. Make sure the application of custom semantics is done consistently across all data sources. Verify that custom semantics and foreign keys do not have any typos or misspellings.

.. semantics-profile-about-end


.. _semantics-profile-type-address:

Address groups
--------------------------------------------------

.. semantics-profile-type-address-start

An address group consists of a street address, city, state, and postal code. Some address groups also have apartment numbers or PO boxes. An address group depends on all of these details to define a complete address. Many individuals are often associated with home addresses, billing addresses, work addresses, and so on.

When a data source provides more than one address group in the data, it's important to apply the **address**, **address2**, **city**, **state**, and **postal** semantics to the correct fields in every group, and then apply a custom semantic that appends a namespace (recommended) or ordinal to each semantic within the address group to support potential downstream workflows.

.. semantics-profile-type-address-end


.. _semantics-profile-type-address-ordinals:

Apply ordinals to address groups
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-address-ordinals-start

Use an ordinal to append an integer to each semantic within an address group.

.. list-table::
   :widths: 150 150 150 150
   :header-rows: 1

   * - All
     - Home
     - Billing
     - Work
   * - address
     - address-1
     - address-2
     - address-3
   * - address2
     - address2-1
     - address2-2
     - address2-3
   * - city
     - city-1
     - city-2
     - city-3
   * - state
     - state-1
     - state-2
     - state-3
   * - postal
     - postal-1
     - postal-2
     - postal-3

This will create columns in the **Unified Coalesced** table like **address**, **address_1**, **address_2**, **address_3** and so on and will keep each location intact.

.. semantics-profile-type-address-ordinals-end


.. _semantics-profile-type-email:

Email addresses
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-start
   :end-before: .. term-email-end

.. semantics-profile-type-email-start

A customer data source may have more than one field that contains an email address, such as for personal email and work email addresses.

When a data source provides more than one email address in the data, it's important to apply the **email** semantic to *all* of the fields, and then apply a custom semantic that appends a namespace (recommended) or ordinal to support potential downstream workflows.

.. semantics-profile-type-email-end

.. semantics-profile-type-email-options-start

There are some options available as you determine the best way to configure Amperity for email addresses:

* :ref:`semantics-profile-type-email-namespace` (recommended when multiple email addresses are present)
* :ref:`semantics-profile-type-email-ordinals`
* :ref:`semantics-profile-type-email-consolidate`
* :ref:`semantics-profile-type-email-exclude`
* :ref:`semantics-profile-type-email-ignore`
* :ref:`semantics-profile-type-email-update-merge-rules`

.. semantics-profile-type-email-options-end


.. _semantics-profile-type-email-namespace:

Apply namespaces to emails
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-email-namespace-start

A namespace appends a string to the **email** semantic. This approach provides a way for downstream processes to have an opportunity to query against specific types of email addresses, such as "email-primary" and "email-alternate".

For example, a data source has two columns for email addresses: personal_email and work_email. Apply the **email** semantic to both columns, and then apply **email-primary** to the **personal_email** column and **email-alternate** to the **work_email** column.

Amperity will create columns in the **Unified Coalesced** table similar to:

.. code-block:: mysql

   ------------------ ------------------ ------------------
    email              email_primary      email_alternate
   ------------------ ------------------ ------------------
   jcurrie@home.com,   jcurrie@home.com   justinc@work.com
   justinc@work.com
   ------------------ ------------------ ------------------
   clorenz@home.com,   clorenz@home.com   clorenz@work.com
   clorenz@work.com
   ------------------ ------------------ ------------------

.. semantics-profile-type-email-namespace-end


.. _semantics-profile-type-email-ordinals:

Apply ordinals to emails
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-email-ordinals-start

For example, a data source has two columns for email addresses: personal_email and work_email. Apply the **email** semantic to both columns, and then apply **email-1** to the **personal_email** column and **email-2** to the **work_email** column.

Amperity will create columns in the **Unified Coalesced** table similar to:

.. code-block:: mysql

   ------------------ ------------------ ------------------
    email              email_1            email_2
   ------------------ ------------------ ------------------
   jcurrie@home.com,   jcurrie@home.com   justinc@work.com
   justinc@work.com
   ------------------ ------------------ ------------------
   clorenz@home.com,   clorenz@home.com   clorenz@work.com
   clorenz@work.com
   ------------------ ------------------ ------------------

.. semantics-profile-type-email-ordinals-end


.. _semantics-profile-type-email-consolidate:

Consolidate emails
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-email-consolidate-start

All values to which the **email** semantic is applied are consolidated into a single column whether or not a custom semantic is applied to each type of email address value.

You can still access the individual email addresses within that field by using the **EXPLODE()** function. For example:

.. code-block:: sql

   SELECT
     *
     ,EXPLODE(SPLIT(email, ',')) AS email_exploded
   FROM Unified_Coalesced

.. semantics-profile-type-email-consolidate-end


.. _semantics-profile-type-email-exclude:

Exclude duplicate emails
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-email-exclude-start

In some situations you might discover a large number of email addresses that should not be associated with any customer profiles. For example, a long-running promotion for a free food item results in a large number of email addresses associated with the same first name, last name, and phone number. This results in a large number of nearly-identical records, many with a unique email address. You can use semantic exclusions to define a threshold over which records like this are collapsed into a trivial duplicate.

Configure Stitch to define a semantic exclusion for email addresses:

::

   :amperity.stitch.settings/soft-trivial-dupe-semantic-exclusions #{"email"}

and then define the threshold:

::

   :amperity.stitch.settings/soft-trivial-dupe-size-threshold 25

For each unique combination of PII--excluding email addresses!--the distinct email addresses that are associated with that unique combination of PII are compared. If there are more than 25 distinct email addresses, those records are collapsed into a trivial duplicate.

.. semantics-profile-type-email-exclude-end


.. _semantics-profile-type-email-ignore:

Ignore email addresses
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-email-ignore-start

Many email addresses are not useful for identity resolution. Some of them are generic, such as *info@some-domain.com*, and are often associated with a place of business and are never associated with a unique individual. Other email addresses are bogus, having been entered as a requirement for providing a genuine email address, but are otherwise fake, such as *123@some-domain.com*.

.. semantics-profile-type-email-ignore-end

.. semantics-profile-type-email-ignored-list-start

The following values associated with the **email** semantic are ignored by Stitch when performing identity resolution:

* **@NOEMAIL.COM**
* **@NOMAIL.COM**
* 0000000000
* **123@**
* **1234@**
* **99@**
* **ABC@**
* **ABC123@**
* ADMIN@
* BOOKING@
* CLIENT@
* CLIENTS@
* CONFIRMATION@
* CONFIRMATIONS@
* CONTACT@
* CUSTOMERSERVICE
* CUSTOMERSERVICE@
* CUSTOMERSERVICES
* CUSTOMERSERVICES@
* **DECLINE@**
* **DECLINED@**
* **DENIED@**
* EMAIL@
* @EMAIL.TST
* EXAMPLE@
* **FAKENAME@**
* GUEST@
* GUESTS@
* HELP@
* HELPS@
* HOTELHELP@
* HOTELPARTNER@
* HOTELPARTNERS@
* INFO@
* **JUNK@**
* MAIL@
* ME@
* N@A
* NAME@
* **NO@**
* **NOEMAIL@**
* **NOMAIL@**
* **NONE@**
* **NONENONE@**
* **NOREPLY@**
* **NOTHANKS@**
* **NOTHANKYOU@**
* ONLINERESERVATION
* ONLINERESERVATION@
* ONLINERESERVATIONS
* ONLINERESERVATIONS@
* OPERATION@
* OPERATIONS@
* QUERIES@
* QUERY@
* **REFUSED@**
* RES@
* RESERVAS
* RESERVATION@
* RESERVATIONS@
* ROOMRESERVATION@
* ROOMRESERVATIONS@
* SAMPLE@
* SAMPLES@
* SERVICE@
* SHOP@
* TEST@
* TESTING@
* TESTEMAIL@
* TRAVEL@
* TRAVELS
* VENDOR@
* VENDORS@
* **XXX@**

The values in **bold** are always ignored.

.. semantics-profile-type-email-ignored-list-end

.. semantics-profile-type-email-update-list-start

Stitch may be configured to allow certain generic email addresses to be available to Stitch as part of identity resolution when the **pre-processing-profile** configuration setting is set to:

.. code-block:: clojure

   pre-processing-profile :allow-business-email

When this setting is updated, only the following email address patterns are ignored by Stitch:

* @NOEMAIL.COM
* @NOMAIL.COM
* 123@
* 1234@
* 99@
* ABC@
* ABC123@
* DECLINE@
* DECLINED@
* DENIED@
* FAKENAME@
* JUNK@
* NO@
* NOEMAIL@
* NOMAIL@
* NONE@
* NONENONE@
* NOREPLY@
* NOTHANKS@
* NOTHANKYOU@
* REFUSED@
* XXX@

Use a :doc:`bad-values blocklist <blocklist_bad_values>` to configure Amperity to continue ignoring any of the email address patterns that were removed from the default list of ignored email patterns.

.. semantics-profile-type-email-update-list-end


.. _semantics-profile-type-email-update-merge-rules:

Update email merge rules
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_operator/source/table_merged_customers.rst
   :start-after: .. table-merged-customers-extend-pii-semantic-email-start
   :end-before: .. table-merged-customers-extend-pii-semantic-email-end

**To update merge rules to support custom email semantics**

.. include:: ../../amperity_operator/source/table_merged_customers.rst
   :start-after: .. table-merged-customers-extend-pii-semantic-email-steps-start
   :end-before: .. table-merged-customers-extend-pii-semantic-email-steps-end


.. _semantics-profile-type-loyalty:

Loyalty programs
--------------------------------------------------

.. semantics-profile-type-loyalty-start

Use the **loy/** and **loy-event/** semantic tag collections to apply semantic tags to data sources that contain information about your brand's loyalty programs. You may define custom semantic tags within the **loy/** and **loy-event/** semantic namespaces.

.. semantics-profile-type-loyalty-end

.. semantics-profile-type-loyalty-make-available-to-stitch-start

.. important:: Loyalty profiles are unique by Amperity ID; loyalty events are unique by Amperity ID and event datetime when:

   #. The **fk-loyalty-id** semantic tag is applied to the same source fields as the **loy/loyalty-id** and **loy-event/loyalty-id** fields.
   #. The **loy/email** and **loy-event/email** semantic tags are applied to fields that contain email addresses.
   #. The **loy/birthdate** semantic tag is applied to fields that contain birthdates.

   Source tables for loyalty profiles and events should not be made available to Stitch.

.. semantics-profile-type-loyalty-make-available-to-stitch-end


.. _semantics-profile-type-names:

Names
--------------------------------------------------

.. semantics-profile-type-names-start

Names are tagged using a combination of semantic tags. Apply the **given-name** and **surname** semantic tags to fields that contain the first and last names for customers. Apply the **full-name** semantic tag to fields that contain complete customer names, such as first, middle, and last. Apply the **generational-suffix** tag to fields that contain *only* suffixes like Jr, Sr, III, and so on.

.. semantics-profile-type-names-end

.. semantics-profile-type-names-important-start

The **given-name**, **surname**, and **generational-suffix** semantic tags may only be applied once per feed.

.. semantics-profile-type-names-important-end


.. _semantics-profile-type-names-derived:

Deriving names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-names-derived-start

Stitch will derive given names and surnames from **full-name** when a data source can have the **full-name** semantic tag applied, but:

* Fields tagged with **given-name** and **surname** do not have explicit values
* Fields cannot be tagged with **given-name** or **surname**

When a table does not contain given names and/or surnames, values associated with **full-name** will not be available from the **Unified Coalesced** table for that data source, but values will be available from the **Unified Preprocessed Raw** table.

.. semantics-profile-type-names-derived-end

.. semantics-profile-type-names-derived-table-start

The following table shows records with various combinations of values for fields to which the **given-name**, **surname**, and **full-name** semantic tags are applied. The **Raw** column represents values that are present in the customer data. The **Derived** column represents values for **given-name** and **surname** as derived from the value in **full-name**. The **Preprocessed** value represents the values that are provided to Stitch. When **given-name** or **surname** are empty or **NULL**, **full-name** values is used to derive a value, along with identifying a **generational-suffix**, if present.

.. list-table::
   :widths: 40 140 140 140 140
   :header-rows: 1

   * - Record
     - Semantic
     - Raw
     - Derived
     - Preprocessed
   * - **1**
     - **given-name**

       **surname**

       **full-name**

     - *Justin*

       *Currie*

       *Amperity*

     - *Justin*

       *Currie*

       *NULL*, *Amperity*

     - *Justin*

       *Currie*

   * - **2**
     - **given-name**

       **surname**

       **full-name**

     - *Justin*

       *Currie*

       *NULL*

     - *Justin*

       *Currie*

       *NULL*, *NULL*

     - *Justin*

       *Currie*

   * - **3**
     - **given-name**

       **surname**

       **full-name**

     - *NULL*

       *NULL*

       *Amperity*

     - *NULL*

       *Amperity*

       *NULL*, *Amperity*

     - *NULL*

       *Amperity*

   * - **4**
     - **given-name**

       **surname**

       **full-name**

     - *Justin*

       *NULL*

       *Amperity*

     - *Justin*

       *Amperity*

       *NULL*, *Amperity*

     - *Justin*

       *Amperity*

   * - **5**
     - **given-name**

       **surname**

       **full-name**

     - *NULL*

       *Currie*

       *Amperity*

     - *NULL*

       *Currie*

       *NULL*, *Amperity*

     - *NULL*

       *Currie*

   * - **6**
     - **given-name**

       **surname**

       **full-name**

     - *Justin*

       *Currie*

       *Amperity Company*

     - *Justin*

       *Currie*

       *Amperity*, *Company*

     - *Justin*

       *Currie*

   * - **7**
     - **given-name**

       **surname**

       **full-name**

     - *Justin*

       *Currie*

       *NULL*

     - *Justin*

       *Currie*

       *NULL*, *NULL*

     - *Justin*

       *Currie*

   * - **8**
     - **given-name**

       **surname**

       **full-name**

     - *NULL*

       *NULL*

       *Amperity Company*

     - *NULL*

       *NULL*

       *Amperity*, *Company*

     - *Amperity*

       *Company*

   * - **9**
     - **given-name**

       **surname**

       **full-name**

     - *Justin*

       *NULL*

       *Amperity Company*

     - *Justin*

       *Company*

       *Amperity*, *Company*

     - *Justin*

       *Company*

   * - **10**
     - **given-name**

       **surname**

       **full-name**

     - *NULL*

       *Currie*

       *Amperity Company*

     - *Amperity*

       *Currie*

       *Amperity*, *Company*

     - *Amperity*

       *Currie*

   * - **11**
     - **given-name**

       **surname**

       **full-name**

     - *Justin*

       *NULL*

       *Amperity Q Company*

     - *Justin*

       *Company*

       *Amperity Q*, *Company*

     - *Justin*

       *Company*

   * - **12**
     - **given-name**

       **surname**

       **full-name**

     - *NULL*

       *Currie*

       *Amperity Q Company*

     - *Amperity Q*

       *Currie*

       *Amperity Q*, *Company*

     - *Amperity Q*

       *Currie*

.. semantics-profile-type-names-derived-table-end


.. _semantics-profile-type-generational-suffix-derived:

Deriving generational suffix
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-generational-suffix-start
   :end-before: .. term-generational-suffix-end

.. semantics-profile-type-generational-suffix-derived-start

A generational suffix is derived automatically by Stitch based on the values for the fields to which the **given-name** and **surname** semantic tags were applied *or* when **generational-suffix** is empty, **NULL**, or not tagged in a feed.

When Stitch generates clusters of customer records, a generational suffix is used to split customer records in the following situations:

#. The generational suffixes associated with customer records do not match.
#. The generational suffixes associated with customer records do match, but the birthdates associated with the records do not.

.. semantics-profile-type-generational-suffix-derived-end

.. semantics-profile-type-generational-suffix-derived-caution-start

.. caution:: The **generational-suffix** semantic tag should only be applied once per feed and only to a field that contains the suffix separated from the first and last names.

.. semantics-profile-type-generational-suffix-derived-caution-end


.. _semantics-profile-type-phone:

Phone numbers
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-phone-start
   :end-before: .. term-phone-end

.. semantics-profile-type-phone-start

A customer data source may have more than one field that contains a phone number, such as a home phone number, a work phone number, a mobile phone number, and so on.

When a data source provides more than one phone number in the data, it's important to apply the **phone** semantic to *all* of the fields, and then apply a custom semantic that appends a namespace (recommended) or ordinal to support potential downstream workflows.

.. semantics-profile-type-phone-end

.. semantics-profile-type-phone-options-start

There are some options available as you determine the best way to configure Amperity for phone numbers:

* :ref:`semantics-profile-type-phone-namespaces` (recommended when multiple phone numbers are present)
* :ref:`semantics-profile-type-phone-ordinals`
* :ref:`semantics-profile-type-phone-consolidate`

.. semantics-profile-type-phone-options-end


.. _semantics-profile-type-phone-last-10:

Last 10 digits
++++++++++++++++++++++++++++++++++++++++++++++++++

.. TODO: THis is also in amperity_reference/semantics.rst for profile/phone.

.. semantics-profile-type-phone-digits-start

Amperity uses the last 10 digits of phone numbers for identity resolution.

Use the `input validation report <https://docs.amperity.com/operator/validate_inputs.html>`__ to find data sources that contain records with phone numbers that exceed 10 digits.

You should exclude extensions from phone numbers whenever possible. You may use a custom domain table to apply additional formatting to phone numbers, such as removing extensions.

Alternately provide data sources to Amperity that have already removed the extensions or have moved them into a different field.

.. semantics-profile-type-phone-digits-end


.. _semantics-profile-type-phone-namespaces:

Apply namespaces to phone
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-phone-namespaces-start

A namespace appends an string to the **phone** semantic. This approach provides a way for downstream processes to have an opportunity to query against specific types of phone numbers, such as "phone-home", "phone-mobile" and "phone-work".

.. tip:: Using a namespace pattern is better because it makes it easier for other users of Amperity to understand the intent of the custom semantic.

For example, a data source has three columns for phone numbers: personal_phone, mobile_phone, and work_phone. Apply the **phone** semantic to all columns, and then apply **phone-home** to the **personal_phone**, **phone-mobile** to the **mobile_phone** column, and **phone-work** to the **work_phone** column.

Amperity will create columns in the **Unified Coalesced** table similar to:

.. code-block:: mysql

   --------------- --------------- --------------- ---------------
    phone           phone-home      phone-mobile    phone-work
   --------------- --------------- --------------- ---------------
    1(234)5678910   1(234)5678910   1(432)5670198   1(987)6543210
    1(432)5670198
    1(987)6543210
   --------------- --------------- --------------- ---------------

.. semantics-profile-type-phone-namespaces-end


.. _semantics-profile-type-phone-ordinals:

Apply ordinals to phone
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-phone-ordinals-start

An ordinal appends an integer to the **phone** semantic. This approach provides a way for downstream processes to have an opportunity to query against specific types of phone numbers, such as "phone-1", "phone-2" and "phone-3".

.. caution:: Consider the ability of other users to discern which type of phone number is meant by each ordinal when choosing an ordinal over a namespace. Does everybody know what "-1" is vs. "-2"?

For example, a data source has three columns for phone numbers: personal-phone, mobile-phone, and work-phone. Apply the **phone** semantic to all columns, and then apply **phone-1** to the **personal-phone**, **phone-2** to the **mobile-phone** column, and **phone-3** to the **work-phone** column.

Amperity will create columns in the **Unified Coalesced** table similar to:

.. code-block:: mysql

   --------------- --------------- --------------- ---------------
    phone           phone-1         phone-2         phone-3
   --------------- --------------- --------------- ---------------
    1(234)5678910   1(234)5678910   1(432)5670198   1(987)6543210
    1(432)5670198
    1(987)6543210
   --------------- --------------- --------------- ---------------

.. semantics-profile-type-phone-ordinals-end


.. _semantics-profile-type-phone-consolidate:

Consolidate numbers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-profile-type-phone-consolidate-start

All values to which the **phone** semantic is applied are consolidated into a single column whether or not a custom semantic is applied to each type of phone value.

You can still access the individual phone values within that field by using the **EXPLODE()** function. For example:

.. code-block:: sql

   SELECT
     *
     ,EXPLODE(SPLIT(phone, ',')) AS phone_exploded
   FROM Unified_Coalesced

.. semantics-profile-type-phone-consolidate-end


.. _semantics-profile-type-phone-update-merge-rules:

Update phone merge rules
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_operator/source/table_merged_customers.rst
   :start-after: .. table-merged-customers-extend-pii-semantic-phone-start
   :end-before: .. table-merged-customers-extend-pii-semantic-phone-end

**To update merge rules to support custom phone semantics**

.. include:: ../../amperity_operator/source/table_merged_customers.rst
   :start-after: .. table-merged-customers-extend-pii-semantic-phone-steps-start
   :end-before: .. table-merged-customers-extend-pii-semantic-phone-steps-end


.. _semantics-interactions:

Interactions
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-interaction-record-start
   :end-before: .. term-interaction-record-end

.. semantics-interactions-start

All interaction records in which transaction and itemized transactions semantic tags are applied may be used to associate these attributes with an Amperity ID.

.. semantics-interactions-end


.. _semantics-interactions-domain-sql-vs-feeds:

Domain SQL vs. feeds
--------------------------------------------------

.. semantics-interactions-domain-sql-vs-feeds-start

The most important decision to make when providing transaction records to Amperity is which method to use when applying semantic tags. You can do this directly from the **Feed Editor**, but more likely will need to use a custom domain table to shape the SQL prior to applying semantic tags.

Some things to consider when determining the best approach for applying semantic tags:

* What shape is the data after it has been loaded to the **Feed Editor**? Can all of the required tags be applied to fields that exist within the data?
* What shape do you want to work with downstream, including the customer 360 database, segments that are sent from Amperity to downstream systems, and the **Campaigns** page within Amperity.
* Can the data be trimmed using a saved query prior to loading it to Amperity? Consider clickstream data, which offers a very wide set of fields, many of which are not applicable to using interaction records to associate your customers with their most important activities.
* Do high quality customer records and interaction records exist side-by-side within this data source? In some cases, using domain SQL to build custom domain tables to capture the customer records separately from the interactions records may be necessary. In this situation, the same feed can be used to load the data, after which two custom tables are built using domain SQL.

.. semantics-interactions-domain-sql-vs-feeds-end


.. _semantics-interactions-associate-to-amperity-ids:

Associate to Amperity IDs
--------------------------------------------------

.. semantics-interactions-associate-to-amperity-ids-start

An Amperity ID must be associated with interaction records. This association is made using one of the following methods, in order of preference:

#. A foreign key that is :ref:`associated with customer records <semantics-interactions-customer-records>`
#. A foreign key that is :ref:`associated with interaction records <semantics-interactions-interaction-records>`
#. An :ref:`arbitrary identifier or key <semantics-interactions-custom-semantics>`

.. semantics-interactions-associate-to-amperity-ids-end


.. _semantics-interactions-customer-records:

Customer records
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-interactions-customer-records-start

If customer records use foreign keys, such as **fk-[namespace]**, as semantic tags *and* the same types of fields exist within interaction records, apply those foreign key semantic tags to the corresponding fields in the interaction records.

This will directly associate the customer records to the interaction records and will create stitched output that adds the Amperity ID to both record types.

.. semantics-interactions-customer-records-end


.. _semantics-interactions-interaction-records:

Interaction records
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-interactions-interaction-records-start

If interaction records use foreign keys, such as **fk-[namespace]**, as semantic tags and the same types of fields exist within customer records, apply those foreign key semantic tags to the corresponding fields in the customer records.

This will directly associate the interaction records to the customer records and will create stitched output that adds the Amperity ID to both record types.

In this scenario, be sure to verify Stitch output to look for the presence of clusters that are matching on this foreign key.

.. semantics-interactions-interaction-records-end


.. _semantics-interactions-custom-semantics:

Custom semantics
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-interactions-custom-semantics-start

In a scenario where foreign keys are not available, apply a custom semantic tag, such as **customer-id**, to a column that best identifies the customer within interaction records. Use a SQL join in the customer 360 database to associate this field, along with the interaction records, to the Amperity ID.

Apply this type of custom semantic to both interaction records and customer records in a similar way as foreign keys. Use the following naming patterns:

* For customer records: **customer-id** without a prefix
* For transactions data: **customer-id**

and then use SQL in the customer 360 database similar to join transactions to the customer 360 table. For example:

.. code-block:: sql

   Unified_Transactions ut
   JOIN Unified_Coalesced uc ON ut.customer_id  = uc.customer_id

or:

.. code-block:: sql

   Unified_Itemized_Transaction uit
   JOIN  Unified_Coalesced uc on uit.customer_id = uc.customer_id

.. semantics-interactions-custom-semantics-end


.. _semantics-keys:

Keys
==================================================

.. semantics-keys-start

Keys are used to identify signals in source data that can be applied during the Stitch process. For example, a table that contains customer records automatically assigns the **pk** semantic to any field identified as a primary key. For tables that contain interaction records, a foreign key is often used to associate important fields for interaction records to primary keys for customer records. This allows interaction records to be correlated with the Amperity ID as an outcome of the Stitch process even though interaction records are not processed by Stitch for the purpose of identity resolution.

.. semantics-keys-end


.. _semantics-key-blocking:

Blocking keys (bk)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-bk-start
   :end-before: .. term-bk-end

.. semantics-key-blocking-start

You can define custom blocking labels using **bk-[label]**, and then use them as a blocking strategy within Stitch.

.. semantics-key-blocking-end

.. semantics-key-blocking-caution-start

.. caution:: Use blocking keys carefully and be sure to verify that Stitch results contain the desired outcome.

.. semantics-key-blocking-caution-end


.. _semantics-key-blocking-label-fk:

Label foreign key as blocking key
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-key-blocking-label-fk-start

Label a blocking key as a foreign key to force Stitch to score all records that match the blocking key, but without assigning a 5.0 score. This will result in better recall for Stitch results, especially when noisy foreign keys are present in customer data, such as to those associated with a credit card hash or to phone numbers used as identifiers.

.. semantics-key-blocking-label-fk-end

**To label a foreign key as a blocking key**

.. semantics-key-blocking-label-fk-steps-start

#. Use a custom semantic tag on the foreign key that starts with **bk**. For example: **bk-cc-hash**.
#. Add a :ref:`blocking strategy <configure-stitch-advanced-clustering-blocking>` to Stitch configuration that is identical to the custom semantic tag. For example:

   .. code-block:: clojure

      :stitch/blocking-strategies #{:dnf1 :dnf3 :dnf4 :dnf5 :dnf6 :dnf7 :dnf8 :email :fk :bk-cc-hash}

#. Update the Stitch configuration that applies semantic exclusions to :ref:`trivial duplicates <configure-stitch-advanced-trivial-duplicates>`:

   .. code-block:: clojure

      :stitch/soft-trivial-dupe-semantic-exclusions #{":bk-cc-hash"}

.. semantics-key-blocking-label-fk-steps-end


.. _semantics-key-blocking-update:

Update blocking strategies
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-key-blocking-update-start

Blocking is a non-trivial step for record linking in the Stitch process. An overly generous blocking strategy may result in a high recall rate, which means too many pairs are evaluated, along with negative system performance.

An overly conservative blocking strategy may result in a low recall rate, which means too few pairs are evaluated. The right combination of blocking keys creates the ideal recall rate for Stitch results.

.. semantics-key-blocking-update-end


.. _semantics-key-customer:

Customer keys (ck)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ck-start
   :end-before: .. term-ck-end

.. semantics-key-customer-tip-start

.. tip:: What happens to customer keys in the **Unified Coalesced** table?

   * Records may have NULL customer keys; NULL customer keys are ignored by Stitch.
   * There may be only one customer key per data source.
   * There may be multiple customer keys per Amperity ID. This is because customer keys may also be tagged as foreign keys.

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

.. semantics-key-foreign-context-start

A foreign key semantic tag may be applied to any column in any data source, but should be associated with a field that can also act as a primary key for that data source *and* is present in other tables.

A foreign key may be used once within a table. A table may have more than one foreign key. For example, if a data source contains customer and audience identifiers, apply **fk-customer** to the customer identifier and **fk-audience** to the audience identifier.

.. semantics-key-foreign-context-end

.. semantics-key-foreign-start

A record pair is assigned an exact match score (5.0) when foreign keys contain identical values during pairwise comparison.

The most common use cases for foreign keys associate fields that act like primary keys within interaction records to the primary keys within customer records, such as:

* A customer identifier for transactions and itemized transactions associated to the primary key in a loyalty table.
* A strong identifier within clickstream data to the primary key in a customer profile table.

Use foreign keys to define meaningful connections across all types of data sources to enable deterministic matching of record pairs during pairwise comparison.

.. semantics-key-foreign-end

.. semantics-key-foreign-tip-start

.. tip:: What happens to foreign keys in the **Unified Coalesced** table?

   * Records may have NULL foreign keys.
   * There may be multiple foreign keys in the data source, but there may not be duplicate foreign keys.
   * There may be multiple foreign keys per Amperity ID.
   * There should not be multiple Amperity IDs per foreign key.

.. semantics-key-foreign-tip-end

.. semantics-key-foreign-note-trivial-duplicates-start

.. note:: If foreign keys are linked together by a trivial duplicate they will appear in the **Unified Preprocessed Raw** table as a comma-separated list.

.. semantics-key-foreign-note-trivial-duplicates-end

.. semantics-key-foreign-important-start

.. important:: A foreign key may also be tagged as a separation key. A foreign key applies when two records have the same value for the key. A separation key applies when two records have different values for the key.

Tagging the same field as both foreign and separation keys can be useful when customer data has a strong identifier that is also associated with an important profile semantic tag, such as **phone** or **email**.

.. semantics-key-foreign-important-end


.. _semantics-key-foreign-link-transactions:

Link transactions to profiles
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-key-foreign-link-transactions-start

Use foreign keys to link identifiers in tables that contain interactions records with tables that contain customer records.

.. tip:: Is there an appropriate foreign key that is already in use with customer records that are already made available to the Stitch process? Is this foreign key well-distributed across interaction records?

If fields in a data source are unable to meet the requirements for using a foreign key, use **customer-id**. This will added the **customer_id** column to the **Unified Itemized Transactions** table.

There can be only one customer ID per transaction.

.. note:: Transforms made in support of foreign key semantic tagging may also be required for interaction records that contain the corresponding transaction-level details to provide support for downstream JOIN operations.

.. semantics-key-foreign-link-transactions-end


.. _semantics-key-foreign-prioritize-matching:

Prioritize foreign key matching
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-key-foreign-prioritize-matching-start

The matching strategy classifier tells Amperity how to apply the results of the blocking strategies, including which groups to analyze and the order in which that analysis should take place, when foreign keys and separation keys are present.

Amperity prioritizes foreign key matching by default. When foreign key matching is the priority, Amperity scores record pairs in the following order:

#. Does the record contain identical foreign key values?
#. If true, assign score 5.0. Stop.
#. If false, does the reorder contain conflicting separation key values?
#. If true, assign score 0.0. Stop.
#. If false, use pairwise comparison scoring.

.. semantics-key-foreign-prioritize-matching-end

.. image:: ../../images/classifier-fk-match.png
   :width: 450 px
   :alt: Foreign key matching priority.
   :align: left
   :class: no-scaled-link


.. _semantics-key-foreign-case-sensitive:

Use case-sensitive foreign keys
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-key-foreign-case-sensitive-start

Values associated with foreign keys are case-insensitive by default. To configure values for particular foreign keys to be case-sensitive, add the following configuration setting to Stitch:

.. code-block:: clojure

   :amperity.stitch.settings/case-sensitive-fks #{"fk-name"}

where **fk-name** is a the name of the foreign key for which values will be treated as case-sensitive.

.. semantics-key-foreign-case-sensitive-end


.. _semantics-key-primary:

Primary keys (pk)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-primary-key-start
   :end-before: .. term-primary-key-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-pk-start
   :end-before: .. term-pk-end

.. semantics-key-primary-tip-start

.. tip:: What happens to primary keys in the **Unified Coalesced** table?

   * Each record in the **Unified Coalesced** table must have a primary key.
   * A primary key is unique within a data source, but that primary key may not be unique across all data sources.
   * There can be only one primary key per data source; each record in the **Unified Coalesced** table can be uniquely identified by the pair of values defined in the "datasource" and "pk" columns.
   * Each record in the **Unified Coalesced** table may only be associated with a single Amperity ID.

.. semantics-key-primary-tip-end


.. _semantics-key-separation:

Separation keys (sk)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-separation-key-start
   :end-before: .. term-separation-key-end

.. semantics-key-separation-about-start

A record pair is assigned a non-matching score (0.0) when separation keys contain conflicting values during pairwise comparison. A record pair is split into two clusters when both pairs contain a non-NULL value.

.. note:: The following separation keys do not consider approximately matched values to be conflicting values:

   * **sk-given-name**  For example, Mike and Michael are not conflicting values.
   * **sk-birthdate**  For example, 1981-09-08 and 1981-08-09 are not conflicting values.
   * **sk-generational-suffix**

Use separation keys to prevent Stitch from matching records during pairwise comparison.

.. semantics-key-separation-about-end

.. semantics-key-separation-important-start

.. important:: A separation key may also be tagged as a foreign key. Tagging the same field as a foreign and separation key can be useful when customer data has a strong identifier that is also associated with an important profile semantic tag, such as **phone** or **email**.

.. semantics-key-separation-important-end


.. _semantics-key-separation-apply-to-brand:

Apply to brand names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-key-separation-apply-to-brand-start

A separation key can be useful in situations where records associated with different brands should not belong to the same cluster of records.

This is possible when data is provided to Amperity in a way that allows a separation key to be directly associated with a primary key that represents a single brand.

Assign a unique separation key to each primary key to prevent clusters from being associated with more than one separation key. 

.. semantics-key-separation-apply-to-brand-end

.. semantics-key-separation-apply-to-brand-caution-start

.. caution:: This approach can result in the assignment of more than one Amperity ID for the same unique individual. For example, a customer shops at both ACME and ACME Deluxe and both data sources contain what would normally be scored as an exact match for profile (PII) data.

   A separation key associated to the brands will create a cluster for each brand, despite the profile data matching well enough to score all of those records as belonging to the same customer.

.. semantics-key-separation-apply-to-brand-caution-end

**To assign separation keys to brands**

.. semantics-key-separation-apply-to-brand-steps-start

#. Use domain SQL to apply a separation keys for brands. For example, for ACME:

   .. code-block:: sql

      IF(brand="ACME", uuid_pk, NULL) AS sk_brand_acme

   and for ACME Deluxe:

   .. code-block:: sql

      IF(brand="ACME Deluxe", uuid_pk, NULL) AS sk_brand_acme_deluxe

#. Define custom semantic tags for each separation key, and then associate them to a primary key.

   For example, for ACME:

   .. list-table::
      :widths: 35 65
      :header-rows: 1

      * - Column name
        - Semantic tags
      * - **brand**
        - **pk**, **sk-brand-acme**
      * - **order_number**
        - **order-quantity**
      * - etc.
        - ...

   and for ACME Deluxe:

   .. list-table::
      :widths: 35 65
      :header-rows: 1

      * - Column name
        - Semantic tags
      * - **brand**
        - **pk**, **sk-brand-acme-deluxe**
      * - **order_number**
        - **order-quantity**
      * - etc.
        - ...

When **sk-brand-acme** and **sk-brand-acme-deluxe** appear in the same cluster, they will be scored as non-matching and the records will be separated.

* Records with the same brand share a separation key, but those values are guaranteed to be different because they are primary keys.
* Records with different brands will have no non-**NULL** separation keys in common and will use the standard classifier.

.. semantics-key-separation-apply-to-brand-steps-end


.. _semantics-key-separation-associate-to-semantic:

Associate to semantic tags
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-key-separation-associate-to-semantic-start

By default, Amperity derives separation keys for **given-name** and **generational-suffix**. You may configure Amperity to use separation keys for any profile semantic tag by using the same namespace prefixed by **sk-**. For example: **sk-birthdate**, **sk-title**, or **sk-surname**. A separation key may not be applied more than once within the same table.

.. semantics-key-separation-associate-to-semantic-end

.. semantics-key-separation-associate-to-semantic-warning-start

.. warning:: Using non-default separation keys to help resolve overclustering problems related to similarities in customer profile data, such as with names and households, requires the classifier for Stitch model configuration to be set to **:general-ordinal-sk-priority**.

.. semantics-key-separation-associate-to-semantic-warning-end


.. _semantics-key-separation-associate-to-birthdate:

sk-birthdate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. semantics-key-separation-associate-to-birthdate-start

**sk-birthdate** is true when two birthdates meet all of the following conditions:

* Are not exact string matches.
* Are not off by 1 character.
* Do not have the month and day swapped.
* Exactly one of month, day, or year are off by 1 character from each other.
* Are not NULL.

Add the **sk-birthdate** separation key to fields that are tagged with the **birthdate** semantic to prevent Stitch from using birthdates to match records.

For example, a tenant has a datasource with high-quality **birthdate** data, yet post-Stitch output contains generational issues where parents and siblings are clustered together despite having different birth dates. 

.. semantics-key-separation-associate-to-birthdate-end


.. _semantics-key-separation-associate-to-title:

sk-title
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. semantics-key-separation-associate-to-title-start

Amperity will infer title from gender during preprocessing, after which those values may be used as separation keys. When gender conflicts are present they are resolved as if they were a given name conflict.

.. semantics-key-separation-associate-to-title-end


.. _semantics-key-separation-prioritize-unmatching:

Prioritize separation key unmatching
++++++++++++++++++++++++++++++++++++++++++++++++++

.. semantics-key-separation-prioritize-unmatching-start

The matching strategy classifier tells Amperity how to apply the results of blocking strategies when foreign keys and separation keys are present, including which groups to analyze and the order in which that analysis should take place.

.. semantics-key-separation-prioritize-unmatching-end

.. semantics-key-separation-prioritize-unmatching-default-start

The default behavior :ref:`prioritizes separation key unmatching <semantics-key-separation-prioritize-unmatching>`. Amperity derives separation keys for **sk-given-name** and **sk-generational-suffix**. You may configure Amperity to prioritize foreign keys over separation keys.

.. semantics-key-separation-prioritize-unmatching-default-end

.. semantics-key-separation-prioritize-unmatching-about-start

When separation key unmatching is the priority, Amperity scores record pairs in the following order:

#. Does the record contain conflicting separation key values?
#. If true, assign score 0.0. Stop.
#. If false, does the record contain identical foreign key values?
#. If true, assign score 5.0. Stop.
#. If false, use pairwise comparison scoring.

.. semantics-key-separation-prioritize-unmatching-about-end

.. image:: ../../images/classifier-sk-unmatch.png
   :width: 450 px
   :alt: Separation key matching priority.
   :align: left
   :class: no-scaled-link


.. _semantics-product-catalogs:

Product catalogs
==================================================

.. semantics-product-catalog-start

Product catalog semantics should be applied to data sources that contain product catalog data. Product semantics may applied alongside other semanztics, depending on the data source. Use the built-in list of semantics when building a feed. Product semantics are prefixed with **pc/** in the semantics dropdown menu in the **Feed Editor**.

.. semantics-product-catalog-end


.. _semantics-product-catalog-define:

Define product catalogs
--------------------------------------------------

.. semantics-product-catalog-define-start

A :ref:`product catalog taxonomy <add-predicted-models-product-catalog>` must be defined to support predictive modeling. Amperity provides a set of semantic tags for product catalog taxonomies that will generate the **Unified Product Catalog** table. The **product-id** semantic tag identifies the field against which predictions will be made must be joined to the **Unified Itemized Transactions** table.

.. semantics-product-catalog-define-end

**Example**

.. semantics-product-catalog-define-example-start

ACME Beverages defines its product catalog taxonomy using a simple hierarchy:

::

   Category
     Subcategory
       Beverage Type
         Beverages by Brand

This taxonomy results in approximately 400 individual types of beverages that are spread across 6 top-level categories with approximately 5000 individual beverages by brand.

When determining the correct size of a product catalog for use with predictive modeling you want to choose the node in the taxonomy that will provide between 20-2000 unique values. ACME Beverages chooses to use beverage type as the node within the taxonomy that is to be associated with predictive modeling for recommended audiences.

By default, predictive modeling returns up to the top 50 values within the product catalog taxonomy, or the top 50 types of beverages within the product catalog. 

.. note:: If there are more than 50 eligible values, the model can be configured to return up to the top 100 values.

.. semantics-product-catalog-define-example-end
