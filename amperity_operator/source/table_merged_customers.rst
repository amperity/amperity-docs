.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Merged Customers table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Merged Customers table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Merged Customers table

==================================================
Merged Customers table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-merged-customers-table-start
   :end-before: .. term-merged-customers-table-end

.. table-merged-customers-important-start

.. tip:: This topic describes a recommended starting point for the **Merged Customers** table.

   The **Merged Customers** table collects PII data from the **Unified Coalesced** table, and then performs additional processing and grouping of this data *prior* to making this data available to the **Customer 360** table.

   Use the **Merged Customers** tables to apply bad-values blocklists to merge rules.

   The **Merged Customers** table is added to the customer 360 database when you create that database using a database template.

.. table-merged-customers-important-end

.. table-merged-customers-start

This topic describes the starting point for the **Merged Customers** table, and then steps through the process of updating it to be specific to your tenant. This topic does not attempt to address all of the specific use cases you may have for your tenant.

Common ways of extending this table to support additional use cases are described, along with providing links to more detailed examples, when available. Start with the SQL that is added to your tenant by the "Customer 360" database template, and then add support for all of your required use cases.

.. table-merged-customers-end


.. _table-merged-customers-requirements:

Requirements
==================================================

.. table-merged-customers-requirements-start

This topic assumes the following requirements are met:

* PII semantic tags are applied consistently, including assigning the correct data types, to all feeds that contain customer records. For custom PII semantics and/or non-PII data that must be accessible from the **Unified Coalesced** table, you may need to :ref:`extend the Merged Customers table <table-merged-customers-custom-semantics>` to support them.
* Feeds that contain customer records are made available to Stitch.
* Each feed has a primary key; foreign keys are applied consistently across all feeds that are made available to Stitch.
* At least one feed must contain a field that indicates when the data was last updated.

  .. include:: ../../shared/terms.rst
     :start-after: .. term-update-dt-start
     :end-before: .. term-update-dt-end

* You can extend the **Merged Customers** table to exclude common or "bad" values. Extensions may be done *after* the **Merged Customers** table is created because they often have both downstream and upstream dependencies within the Amperity workflow that will require some tuning within for the **Merged Customers** table.

.. table-merged-customers-requirements-end


.. _table-merged-customers-add-table:

Add table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-merged-customers-table-start
   :end-before: .. term-merged-customers-table-end

.. table-merged-customers-add-table-note-start

.. note:: The **Merged Customers** table uses a Spark SQL query to pull the Amperity ID, along with all PII data, from the **Unified Coalesced** table.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-unified-coalesced-table-start
      :end-before: .. term-unified-coalesced-table-end

.. table-merged-customers-add-table-note-end

**To add the Merged Customers table**

.. table-merged-customers-add-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Merged_Customers".
#. Set the build mode to **SQL**.
#. Click **Apply template**, and then select **Merged Customers**.
#. Update the placeholder names--shown as "Domain:Table" in the query--and set field-level priorities.
#. Click **Validate** to verify the SQL runs without error.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Verify that the **db/required** and **db/unique** database field semantics were applied to the **amperity_id** column.
#. Verify that semantic tags--**given_name**, **surname**, **email**, **phone**, **address**, **city**, **state**, **postal**, **birthdate**, **gender**, etc.--were applied to all PII fields correctly.

   .. tip:: You can clear incorrectly tagged semantics individually or for the entire table. To clear semantic tags for the entire table, under **Semantic Suggestions** click **Clear semantics**.
#. From the **Table Semantics** dropdown, select **Merged Customers**.
#. Under **Version History**, select **Enable table version history**.
#. Click **Save**.

.. table-merged-customers-add-steps-end


.. _table-merged-customers-sql-query:

SQL query
--------------------------------------------------

.. table-merged-customers-sql-query-start

The following SQL query is the recommended starting point for the **Merged Customers** table. It exists in two parts: a window function that collects and groups PII data, and then a statement that updates the **Merged Customers** table with the results. This query does the following:

#. Provides a location in which domain tables are assigned priority. This section must be updated to contain the names of the domain tables for your tenant that should be assigned a non-default priority.
#. Provides a location in which PII fields are assigned priority. This section must be updated to contain the names of the domain tables that are assigned source priority, and then be updated to assign priorities to logical groups of fields that contain PII data, such as email addresses and physical addresses.
#. Left joins the fields in the **Unified Coalesced** table into a temporary table for prioritization.
#. Left joins the fields in the **Unified Coalesced** table to form groupings of PII fields. For example, all address-related fields--**address**, **address2**, **city**, **state**, **postal**, and **country**--are grouped together. This is done for names, addresses, phone numbers, email addresses, birthdates, and gender.
#. Left joins the fields in the **Unified Coalesced** table by logical groups *and* by assigned priority.
#. Adds a set of fields to the temporary table for each of the logical groups, which are then added to the **Merged Customers** table.
#. Refreshes the data in the **Merged Customers** table.

.. table-merged-customers-sql-query-end

.. table-merged-customers-sql-query-updates-start

Refer to the :ref:`required updates <table-merged-customers-sql-query-required-updates>` and :ref:`the example of updates <table-merged-customers-sql-query-required-update-examples>` for more information about how to apply the recommended query to the specific domain tables in your tenant.

.. table-merged-customers-sql-query-updates-end


.. _table-merged-customers-sql-query-recommended:

Recommended starting point
--------------------------------------------------

.. table-merged-customers-sql-query-recommended-intro-start

The following query represents the recommended starting point for the **Merged Customers** table. This query :ref:`requires updates in at least two locations <table-merged-customers-sql-query-required-updates>`.

.. table-merged-customers-sql-query-recommended-intro-end

.. table-merged-customers-sql-query-recommended-start

.. code-block:: sql
   :caption: sql-merged-customers
   :linenos:

   WITH
     Source_Priority AS (
       SELECT *
       FROM VALUES
         ("Domain:Table", NULL)
         ,("Domain:Table", NULL)
       AS (sp_datasource, priority)
     )

     ,Field_Priority AS (
       SELECT *
       FROM VALUES
         ("Domain:Table", NULL, NULL, NULL, NULL, NULL, NULL)
         ,("Domain:Table", NULL, NULL, NULL, NULL, NULL, NULL)
       AS (fp_datasource, name_pri, address_pri, email_pri, phone_pri, birthdate_pri, gender_pri)
     )

     ,Unified_Preprocessed AS (
       SELECT *
       FROM Unified_Coalesced uc
       LEFT JOIN Source_Priority sp ON sp.sp_datasource = uc.datasource
     )

     ,Unified_Structs AS (
       SELECT
         amperity_id

         ,NAMED_STRUCT(
           'given_name', given_name
           ,'surname', surname
           ,'full_name', full_name
           ,'generational_suffix', generational_suffix
           ,'pk', pk
           ,'update_dt', update_dt
           ,'datasource', datasource
           ,'priority', COALESCE(fp.name_pri, up.priority, 999)
           ,'completion', INT((ISNOTNULL(given_name)
                          AND ISNOTNULL(surname))
                          OR ISNOTNULL(full_name))
         ) AS `name_struct`
          
         ,NAMED_STRUCT(
           'address', address
           ,'address2', address2
           ,'city', city
           ,'state', state
           ,'postal', postal
           ,'country', country
           ,'pk', pk
           ,'update_dt', update_dt
           ,'datasource', datasource
           ,'priority', COALESCE(fp.address_pri, up.priority, 999)
           ,'completion', (INT(ISNOTNULL(address))
                         + INT(ISNOTNULL(city))
                         + INT(ISNOTNULL(state))
                         + INT(ISNOTNULL(postal)))
         ) AS `address_struct`

         -- NAMED_STRUCT block for email addresses goes here if your
         -- tenant is not using the Email_Ampid_Assignment table.

         ,NAMED_STRUCT(
           'phone', phone
           ,'pk', pk
           ,'update_dt', update_dt
           ,'datasource', datasource
           ,'priority', COALESCE(fp.phone_pri, up.priority, 999)
           ,'completion', INT(ISNOTNULL(phone))
         ) AS `phone_struct`

         ,NAMED_STRUCT(
           'birthdate', birthdate
           ,'pk', pk
           ,'update_dt', update_dt
           ,'datasource', datasource
           ,'priority', COALESCE(fp.birthdate_pri, up.priority, 999)
           ,'completion', INT(ISNOTNULL(birthdate))
         ) AS `birthdate_struct`

         ,NAMED_STRUCT(
           'gender', gender
           ,'pk', pk
           ,'update_dt', update_dt
           ,'datasource', datasource
           ,'priority', COALESCE(fp.gender_pri, up.priority, 999)
           ,'completion', INT(ISNOTNULL(gender))
         ) AS `gender_struct`

       FROM Unified_Preprocessed up
       LEFT JOIN Field_Priority fp ON fp.fp_datasource = up.datasource
     )     

     ,Unified_Prioritized AS (
       SELECT DISTINCT
         amperity_id
         ,FIRST(name_struct)
           OVER (
             PARTITION BY amperity_id
             ORDER BY name_struct.completion DESC
                      ,name_struct.priority
                      ,name_struct.update_dt DESC
                      ,name_struct.pk
           ) AS name_struct

         ,FIRST(address_struct)
           OVER (
             PARTITION BY amperity_id
             ORDER BY address_struct.completion DESC
             ,address_struct.priority
             ,address_struct.update_dt DESC
             ,address_struct.pk
           ) AS address_struct

         -- FIRST block for email priority goes here if your
         -- tenant is not using the Email_Ampid_Assignment table.

         ,FIRST(phone_struct)
           OVER (
             PARTITION BY amperity_id
             ORDER BY phone_struct.completion DESC
                      ,phone_struct.priority
                      ,phone_struct.update_dt DESC
                      ,phone_struct.pk
           ) AS phone_struct

         ,FIRST(birthdate_struct)
           OVER (
             PARTITION BY amperity_id
             ORDER BY birthdate_struct.completion DESC
                      ,birthdate_struct.priority
                      ,birthdate_struct.update_dt DESC
                      ,birthdate_struct.pk
           ) AS birthdate_struct

         ,FIRST(gender_struct)
           OVER (
             PARTITION BY amperity_id
             ORDER BY gender_struct.completion DESC
                      ,gender_struct.priority
                      ,gender_struct.update_dt DESC
                      ,gender_struct.pk
           ) AS gender_struct

     FROM Unified_Structs us
   )

   SELECT
     up.amperity_id
   
     ,up.name_struct.given_name
     ,up.name_struct.surname
     ,up.name_struct.full_name
     ,up.name_struct.generational_suffix
     ,up.name_struct.pk AS `name_pk`
     ,up.name_struct.update_dt AS `name_update_dt`
     ,up.name_struct.datasource AS `name_datasource`
     ,up.name_struct.priority AS `name_priority`
     ,up.name_struct.completion AS `name_completion`

     ,up.address_struct.address
     ,up.address_struct.address2
     ,up.address_struct.city
     ,up.address_struct.state
     ,up.address_struct.postal
     ,up.address_struct.country
     ,up.address_struct.pk AS `address_pk`
     ,up.address_struct.update_dt AS `address_update_dt`
     ,up.address_struct.datasource AS `address_datasource`
     ,up.address_struct.priority AS `address_priority`
     ,up.address_struct.completion AS `address_completion`

    -- Get email completion from Email_Ampid_Assignment table
    ,email_ampid_assignment.email
    ,CASE
      WHEN email_ampid_assignment.email IS NULL
      THEN 0
      ELSE 1
    END AS email_completion

     ,up.phone_struct.phone
     ,up.phone_struct.pk AS `phone_pk`
     ,up.phone_struct.update_dt AS `phone_update_dt`
     ,up.phone_struct.datasource AS `phone_datasource`
     ,up.phone_struct.priority AS `phone_priority`
     ,up.phone_struct.completion AS `phone_completion`

     ,up.birthdate_struct.birthdate
     ,up.birthdate_struct.pk AS `birthdate_pk`
     ,up.birthdate_struct.update_dt AS `birthdate_update_dt`
     ,up.birthdate_struct.datasource AS `birthdate_datasource`
     ,up.birthdate_struct.priority AS `birthdate_priority`
     ,up.birthdate_struct.completion AS `birthdate_completion`

     ,up.gender_struct.gender
     ,up.gender_struct.pk AS `gender_pk`
     ,up.gender_struct.update_dt AS `gender_update_dt`
     ,up.gender_struct.datasource AS `gender_datasource`
     ,up.gender_struct.priority AS `gender_priority`
     ,up.gender_struct.completion AS `gender_completion`

   FROM Unified_Prioritized up
   LEFT JOIN email_ampid_assignment
   ON email_ampid_assignment.amperity_id = up.amperity_id

.. table-merged-customers-sql-query-recommended-end


.. _table-merged-customers-sql-query-required-updates:

Required updates
==================================================

.. table-merged-customers-sql-query-required-updates-start

The recommended starting point for the **Merged Customers** table requires the following updates:

* Update the list of :ref:`domain tables under Source_Priority <table-merged-customers-sql-query-required-update-source-priority>` to contain *at least one* domain table with fields tagged for PII semantics.
* Update the list of :ref:`domain tables under Field_Priority <table-merged-customers-sql-query-required-update-field-priority>` to contain *the same list of domain tables*, and then specify individual field priorities across all tables. The order of the fields under each **Domain:Table** must match the order of the fields under **fp_datasource**.

.. table-merged-customers-sql-query-required-updates-end

.. table-merged-customers-sql-query-required-updates-visual-template-start

.. note:: You may use the visual template for the **Merged Customers** table to define source and field priorities.

   #. From **Database Editor** set **Build Mode** to "Visual template", and then select **Merged Customers** from the **Target table** dropdown.
   #. Follow the directions in the visual template page for the selected table.

      Update the list of domain tables under **General source priority** to contain *at least one* domain table with fields tagged for PII semantics.

      Optional. You may define priority by semantic tag.

      When finished, click **Next**.
   #. Validate, and then save the **Merged Customers** table.

.. table-merged-customers-sql-query-required-updates-visual-template-end


.. _table-merged-customers-sql-query-required-update-source-priority:

Source priority
--------------------------------------------------

.. table-merged-customers-sql-query-required-update-source-priority-start

Update the list of domain tables under **Source_Priority** to contain *at least one* domain table with fields tagged for PII semantics. Only domain tables that are made available to Stitch may be listed in the source priority. An integer value will assign priority, where "1" has a higher priority than "2". Domain tables may be assigned the same priority. Any domain table not specified here is assigned a default priority of "999".

.. table-merged-customers-sql-query-required-update-source-priority-end

.. table-merged-customers-sql-query-required-update-source-priority-sql-start

.. code-block:: sql
   :linenos:
   :emphasize-lines: 5,6

   WITH
     Source_Priority AS (
       SELECT *
       FROM VALUES
         ("Domain:Table", x)
         ,("Domain:Table", x)
       AS (sp_datasource, priority)
     )

.. table-merged-customers-sql-query-required-update-source-priority-sql-end


.. _table-merged-customers-sql-query-required-update-field-priority:

Field priority
--------------------------------------------------

.. table-merged-customers-sql-query-required-update-field-priority-start

Use the field priority table to assign priorities for individual fields that are different from the priority assigned generally to each source domain table **Source_Priority**. Update the list of tables to match the same domain tables that were specified for **Source_Priority**, and then update the field priority table to specify individual priorities.

* A NULL value will use the priority assigned to the source domain table or, when a priority is not assigned by a source domain table, the default priority of "999".
* An integer value will assign priority, where "1" has a higher priority than "2".

.. table-merged-customers-sql-query-required-update-field-priority-end

.. table-merged-customers-sql-query-required-update-field-priority-sql-start

.. code-block:: sql
   :linenos:

   ,Field_Priority AS (
     SELECT *
     FROM VALUES
       ("Domain:Table", null, null, null, null, null, null)
       ,("Domain:Table", null, null, null, null, null, null)
     AS (fp_datasource, name_pri, address_pri, email_pri, phone_pri, birthdate_pri, gender_pri)

.. table-merged-customers-sql-query-required-update-field-priority-sql-end

.. table-merged-customers-sql-query-required-update-field-priority-caution-start

.. caution:: The order of the fields under each **Domain:Table** matches the order of the fields under **fp_datasource**. Be sure to apply the priority in the correct location. For example, assigning field priority for email addresses:

   .. code-block:: none

      ,null      ,null         ,1          ,null       ,null           ,null

      ,null      ,null         ,2          ,null       ,null           ,null

      ,name_pri  ,address_pri  ,email_pri  ,phone_pri  ,birthdate_pri  ,gender_pri

.. table-merged-customers-sql-query-required-update-field-priority-caution-end


.. _table-merged-customers-sql-query-required-update-examples:

Example of updates
--------------------------------------------------

.. table-merged-customers-sql-query-required-update-examples-start

The following example shows three domain tables: **Table A**, **Table B**, and **Table C**, with source priority assigned in the same order. The email address in **Table B** is assigned the highest priority, the address and phone in **Table C** is assigned the highest priority, and the name is assigned the highest priority in all three tables.

The database in this tenant also includes three other tables: **Table D**, **Table E**, and **Table F**. These tables contain fields tagged with PII semantics, but none of them are higher priority than **Table A**, **Table B**, or **Table C**. By not adding **Table D**, **Table E**, and **Table F** to the SQL query for the **Merged Customers** table, these tables will be automatically assigned the default priority of 999.

.. table-merged-customers-sql-query-required-update-examples-end

.. table-merged-customers-sql-query-required-update-example-query-start

.. code-block:: sql
   :linenos:

   WITH
     Source_Priority AS (
       SELECT *
       FROM VALUES
         ("Table:A",  1)
         ,("Table:B", 2)
         ,("Table:C", 3)
       AS (sp_datasource, priority)
     )

     ,Field_Priority AS (
       SELECT *
       FROM VALUES
         ("Table:A",1,2,2,2,null,null)
         ,("Table:B",1,2,1,2,null,null)
         ,("Table:C",1,1,2,1,null,null)
       AS (fp_datasource, name_pri, address_pri, email_pri, phone_pri, birthdate_pri, gender_pri)
     )

.. table-merged-customers-sql-query-required-update-example-query-start


.. _table-merged-customers-undo-ampid-assignment:

Best email address
==================================================

.. include:: ../../amperity_operator/source/table_email_ampid_assignment.rst
   :start-after: .. table-email-ampid-assignment-start
   :end-before: .. table-email-ampid-assignment-end

.. table-merged-customers-undo-ampid-assignment-start

The :doc:`table_email_ampid_assignment` is configured by default in the SQL template for the **Merged Customers** table. It is recommended that your tenant use the **Email Ampid Assignment** table to ensure that downstream workflows can access the best email addresses for each Amperity ID.

.. table-merged-customers-undo-ampid-assignment-end

.. include:: ../../amperity_operator/source/table_email_ampid_assignment.rst
   :start-after: .. table-email-ampid-assignment-note-start
   :end-before: .. table-email-ampid-assignment-note-end

.. table-merged-customers-undo-ampid-assignment-steps-start

Using the **Email Ampid Assignment** table is strongly recommended, but may be byassed when email opt status and/or email engagement data is not available in your tenant.

If your tenant chooses to bypass the **Email Ampid Assignment** table, the following steps are required to update the **Merged Customers** table to use email address priority and completion values that do not rely on the **Email Ampid Assignment** table.

.. table-merged-customers-undo-ampid-assignment-steps-end

.. table-merged-customers-undo-ampid-assignment-links-start

#. :ref:`Add NAMED_STRUCT for email addresses <table-merged-customers-undo-ampid-assignment-named-struct>`
#. :ref:`Add email address priority <table-merged-customers-undo-ampid-assignment-first>`
#. :ref:`Replace email completion <table-merged-customers-undo-ampid-assignment-completion>`
#. :ref:`Undo LEFT JOIN <table-merged-customers-undo-ampid-assignment-left-join>`

.. table-merged-customers-undo-ampid-assignment-links-end

.. table-merged-customers-undo-ampid-assignment-callout-start

.. important:: The previous steps are only necessary when the **Email Ampid Assignment** table is not configured for your tenant.

.. table-merged-customers-undo-ampid-assignment-callout-end


.. _table-merged-customers-undo-ampid-assignment-named-struct:

Add NAMED_STRUCT for email addresses
--------------------------------------------------

.. table-merged-customers-undo-ampid-assignment-named-struct-start

When your tenant is not using the **Email Ampid Assignment** table you must replace the following comment:

.. code-block:: sql

   -- NAMED_STRUCT block for email addresses goes here if your
   -- tenant is not using the Email_Ampid_Assignment table.

with:

.. code-block:: sql
   :linenos:

   ,NAMED_STRUCT(
     'email', email
     ,'pk', pk
     ,'update_dt', update_dt
     ,'datasource', datasource
     ,'priority', COALESCE(fp.email_pri, up.priority, 999)
     ,'completion', INT(ISNOTNULL(email))
   ) AS `email_struct`

This should be placed in-between the **NAMED_STRUCT** blocks for **address** and **phone**. Refer to the :ref:`recommended starting point <table-merged-customers-sql-query-recommended>` in this topic to refernce the position of this block within the SQL template for the **Merged Customers** table.

.. table-merged-customers-undo-ampid-assignment-named-struct-end


.. _table-merged-customers-undo-ampid-assignment-first:

Add email address priority
--------------------------------------------------

.. table-merged-customers-undo-ampid-assignment-first-start

When your tenant is not using the **Email Ampid Assignment** table you must replace the following comment:

.. code-block:: sql

   -- FIRST block for email priority goes here if your
   -- tenant is not using the Email_Ampid_Assignment table.

with:

.. code-block:: sql
   :linenos:

   ,FIRST(email_struct)
     OVER (
       PARTITION BY amperity_id
       ORDER BY email_struct.completion DESC
                ,email_struct.priority
                ,email_struct.update_dt DESC
                ,email_struct.pk
     ) AS email_struct

This should be placed in-between the **FIRST** blocks for **address** and **phone**. Refer to the :ref:`recommended starting point <table-merged-customers-sql-query-recommended>` in this topic to refernce the position of this block within the SQL template for the **Merged Customers** table.

.. note:: If your tenant is using the bad-values blocklist you must also add the following line:

   .. code-block:: sql

      ,email_struct.blv

.. table-merged-customers-undo-ampid-assignment-first-end


.. _table-merged-customers-undo-ampid-assignment-completion:

Replace email completion
--------------------------------------------------

.. table-merged-customers-undo-ampid-assignment-completion-start

When your tenant is not using the **Email Ampid Assignment** table you must replace the following SQL:

.. code-block:: sql
   :linenos:

    -- Get email completion from Email Ampid Assignment table
    ,email_ampid_assignment.email
    ,CASE
      WHEN email_ampid_assignment.email IS NULL
      THEN 0
      ELSE 1
    END AS email_completion

with:

.. code-block:: sql
   :linenos:

   ,up.email_struct.email
   ,up.email_struct.pk AS `email_pk`
   ,up.email_struct.update_dt AS `email_update_dt`
   ,up.email_struct.datasource AS `email_datasource`
   ,up.email_struct.priority AS `email_priority`
   ,up.email_struct.completion AS `email_completion`

.. note:: If your tenant is using the bad-values blocklist you must also add the following line:

   .. code-block:: sql

      ,up.email_struct.blv AS `email_blv`

.. table-merged-customers-undo-ampid-assignment-completion-end


.. _table-merged-customers-undo-ampid-assignment-left-join:

Undo LEFT JOIN
--------------------------------------------------

.. table-merged-customers-undo-ampid-assignment-left-join-start

When your tenant is not using the **Email Ampid Assignment** table you must remove the following **LEFT JOIN** at the bottom of the SQL template:

.. code-block:: sql
   :linenos:

   LEFT JOIN email_ampid_assignment
   ON email_ampid_assignment.amperity_id = up.amperity_id

.. table-merged-customers-undo-ampid-assignment-left-join-end


.. _table-merged-customers-custom-semantics:

Extend PII semantics
==================================================

You can extend the **Merged Customers** table to preprocess fields that contain PII semantics to improve the quality of the data that ends up in the **Customer 360** table:

* :ref:`table-merged-customers-extend-pii-semantic-custom`
* :ref:`table-merged-customers-extend-analyze-pii-by-datasource`
* :ref:`table-merged-customers-extend-bad-values-blocklist`
* :ref:`table-merged-customers-extend-pii-semantic-full-names`
* :ref:`table-merged-customers-extend-pii-semantic-email`
* :ref:`table-merged-customers-extend-pii-semantic-phone`


.. _table-merged-customers-extend-pii-semantic-custom:

Add custom semantics
--------------------------------------------------

.. table-merged-customers-extend-pii-semantic-custom-start

You can create custom semantics for PII and non-PII fields. All custom semantics are added to the **Unified Coalesced** table.

#. Apply the custom semantics to to feeds. Ensure each custom semantic uses a consistent data type across all feeds.
#. Extend the **Merged Customers** table with custom merge rules that load the column created by the custom semantic from the **Unified Coalesced** table.
#. Apply similar merge patterns used for PII semantics.

Within the **Merged Customers** table, you must decide if the custom semantic requires source and/or field priority:

* :ref:`Assign field priority <table-merged-customers-extend-pii-semantic-custom-assign-priority>`
* :ref:`Skip field priority <table-merged-customers-extend-pii-semantic-custom-skip-priority>`

For example, a company may have data sources that provide data about its own employees, such as internal email addresses, phone numbers, and so on. Use a custom PII semantic named **email-internal** to tag the fields that contain internal email addresses. Apply this custom PII semantic to all fields in all data sources that contain internal email addresses.

Consistently tagging fields with internal email addresses with the **email-internal** custom PII semantic will create a column named **email_internal** in the **Unified Coalesced** table. The **Merged Customers** table can use this column to extend the merge rules to include rules for internal email addresses.

.. important:: Do not apply the default **email** semantic to the **email-internal** columns or add the **email-internal** semantic to any merge rules that handle the presence of namespaced or ordinal custom email semantics.

.. table-merged-customers-extend-pii-semantic-custom-end


.. _table-merged-customers-extend-pii-semantic-custom-assign-priority:

Assign field priority
++++++++++++++++++++++++++++++++++++++++++++++++++

.. table-merged-customers-extend-pii-semantic-custom-without-priority-start

Assigning field priority to a custom PII semantic is optional and should only be done when a custom PII semantic is tagged in multiple data sources, requires a priority other than the default priority ("999"), and requires these data sources to be assigned different priorities.

.. table-merged-customers-extend-pii-semantic-custom-without-priority-end

**To extend merge rules to assign field priority**

.. table-merged-customers-extend-pii-semantic-custom-with-priority-steps-start

#. From the **Customer 360** page, under **All Databases**, open the menu for the customer 360 database, and then select **Edit**.
#. Open the **Merged Customers** table.
#. Find the **Field_Priority** section and update it to add the **email_internal** column to the field priority list:

   .. code-block:: sql
      :linenos:

      ,Field_Priority AS (
        SELECT *
        FROM VALUES
          ("Domain:Table", null, null, null, null, null, null)
          ,("Domain:Table", null, null, null, null, null, null)
        AS (fp_datasource, name_pri, address_pri, email_pri, phone_pri, birthdate_pri, gender_pri)
      )

#. Find the **Unified_Structs** sections, and then add a named struct for the **email_internal** column:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 6

      ,NAMED_STRUCT(
        'email_internal', email_internal
        ,'pk', pk
        ,'update_dt', update_dt
        ,'datasource', datasource
        ,'priority', COALESCE(fp.email_internal_pri, up.priority, 999)
        ,'completion', INT(ISNOTNULL(email_internal))
      ) AS `email_internal_struct`

#. Find the **Unified_Prioritized** section, and then add a first value block for the **email_internal** column:

   .. code-block:: sql
      :linenos:

      ,FIRST(email_internal_struct)
        OVER (
          PARTITION BY amperity_id
          ORDER BY email_internal_struct.completion DESC
                   ,email_internal_struct.priority
                   ,email_internal_struct.update_dt DESC
                   ,email_internal_struct.pk
        ) AS email_internal_struct

#. Find the SELECT statement that builds the **Merged Customers** table, and then add the columns for **email_internal**:

   .. code-block:: sql
      :linenos:

      ,up.email_internal_struct.email_internal
      ,up.email_internal_struct.pk AS `email_internal_pk`
      ,up.email_internal_struct.update_dt AS `email_internal_update_dt`
      ,up.email_internal_struct.datasource AS `email_internal_datasource`
      ,up.email_internal_struct.priority AS `email_internal_priority`
      ,up.email_internal_struct.completion AS `email_internal_completion`

#. Validate the query.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Verify these settings, and then click **Save**.
#. Run the customer 360 database.

.. table-merged-customers-extend-pii-semantic-custom-with-priority-steps-end


.. _table-merged-customers-extend-pii-semantic-custom-skip-priority:

Skip field priority
++++++++++++++++++++++++++++++++++++++++++++++++++

.. table-merged-customers-extend-pii-semantic-custom-without-priority-start

Field priority is only necessary when a custom PII semantic is tagged in multiple data sources, requires a priority other than the default priority ("999"), and requires these data sources to be assigned different priorities. Any custom semantic that does not meet this criteria should be assigned a default field priority and should not be added to the columns in the field priority list.

.. table-merged-customers-extend-pii-semantic-custom-without-priority-end

**To extend merge rules to skip field priority**

.. table-merged-customers-extend-pii-semantic-custom-without-priority-steps-start

#. From the **Customer 360** page, under **All Databases**, open the menu for the customer 360 database, and then select **Edit**.
#. Open the menu for the **Merged Customers** table and select **Edit**.
#. Find the **Unified_Structs** sections, and then add a named struct for the **email_internal** column:

   .. code-block:: sql
      :linenos:

      ,NAMED_STRUCT(
        'email_internal', email_internal
        ,'pk', pk
        ,'update_dt', update_dt
        ,'datasource', datasource
        ,'priority', COALESCE(up.priority, 999)
        ,'completion', INT(ISNOTNULL(email_internal))
      ) AS `email_internal_struct`

#. Find the **Unified_Prioritized** section, and then add a first value block for the **email_internal** column:

   .. code-block:: sql
      :linenos:

      ,FIRST(email_internal_struct)
        OVER (
          PARTITION BY amperity_id
          ORDER BY email_internal_struct.completion DESC
                   ,email_internal_struct.priority
                   ,email_internal_struct.update_dt DESC
                   ,email_internal_struct.pk
        ) AS email_internal_struct

#. Find the SELECT statement that builds the **Merged Customers** table, and then add the columns for **email_internal**:

   .. code-block:: sql
      :linenos:

      ,up.email_internal_struct.email_internal
      ,up.email_internal_struct.pk AS `email_internal_pk`
      ,up.email_internal_struct.update_dt AS `email_internal_update_dt`
      ,up.email_internal_struct.datasource AS `email_internal_datasource`
      ,up.email_internal_struct.priority AS `email_internal_priority`
      ,up.email_internal_struct.completion AS `email_internal_completion`

#. Validate the query.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Verify these settings, and then click **Save**.
#. Run the customer 360 database.

.. table-merged-customers-extend-pii-semantic-custom-without-priority-steps-end


.. _table-merged-customers-extend-analyze-pii-by-datasource:

Analyze PII by datasource
--------------------------------------------------

.. table-merged-customers-extend-analyze-pii-by-datasource-start

You can measure how much data a single feed contributes to the larger set of data by using **datasource** columns in the **Merged Customers** table. These columns are associated with the original primary key and updated dates and allow queries to be built in the customer 360 database to analyze the effects of one data source on the larger set of data in the customer 360 database.

The **Merged Customers** table is already configured to provide this data. For example:

.. code-block:: sql
   :linenos:
   :emphasize-lines: 11

   SELECT
     up.amperity_id
     ,up.address_struct.address
     ,up.address_struct.address2
     ,up.address_struct.city
     ,up.address_struct.state
     ,up.address_struct.postal
     ,up.address_struct.country
     ,up.address_struct.pk AS `address_pk`
     ,up.address_struct.update_dt AS `address_update_dt`
     ,up.address_struct.datasource AS `address_datasource`
     ,up.address_struct.priority AS `address_priority`
     ,up.address_struct.completion AS `address_completion`

If this is missing, you must add the following line to each grouping, updated correctly for each semantic:

.. code-block:: sql

   ,up.address_struct.datasource AS `address_datasource`:

.. table-merged-customers-extend-analyze-pii-by-datasource-end


.. _table-merged-customers-extend-bad-values-blocklist:

Bad-values blocklist
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-bad-values-blocklist-start
   :end-before: .. term-bad-values-blocklist-end

.. table-merged-customers-extend-bad-values-blocklist-start

When using the bad-values blocklist, you must update the **Merged Customers** table include the bad-values blocklist items in the merge rules.

.. table-merged-customers-extend-bad-values-blocklist-end


.. _table-merged-customers-extend-pii-semantic-full-names:

Concatenate full names
--------------------------------------------------

.. table-merged-customers-extend-pii-semantic-full-names-start

The following example shows how to extend the **Merged Customers** table to concatenate full names based on the **given-name** and **surname** semantic tags.

.. table-merged-customers-extend-pii-semantic-full-names-end

**To concatenate full names**

.. table-merged-customers-extend-pii-semantic-full-names-steps-start

#. From the **Customer 360** tab, under **All Databases**, open the menu for the customer 360 database, and then select **Edit**.
#. Open the menu for the **Merged Customers** table and select **Edit**.
#. Find the **Unified_Preprocessed** section and add the highlighted line:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 3

      ,Unified_Preprocessed AS (
        SELECT *
        ,CONCAT_WS(' ', given_name, surname) AS full_name_p
        FROM Unified_Coalesced uc
        LEFT JOIN Source_Priority sp ON sp.sp_datasource = uc.datasource
      )

#. Find the **NAMED_STRUCT** with the **name** column, and then update it to use the coalesced column **full_name_p**. This must be done in the following locations:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 4,12

      ,NAMED_STRUCT(
        'given_name', given_name
        ,'surname', surname
        ,'full_name', full_name_p
        ,'generational_suffix', generational_suffix
        ,'pk', pk
        ,'update_dt', update_dt
        ,'datasource', datasource
        ,'priority', COALESCE(fp.name_pri, up.priority, 999)
        ,'completion', INT((ISNOTNULL(given_name)
                       AND ISNOTNULL(surname))
                       OR ISNOTNULL(full_name_p))
 
      ) AS `name_struct`

#. Validate the query.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Verify these settings, and then click **Save**.
#. Run the customer 360 database.

.. table-merged-customers-extend-pii-semantic-full-names-steps-end


.. _table-merged-customers-extend-pii-semantic-email:

Multiple email addresses
--------------------------------------------------

.. table-merged-customers-extend-pii-semantic-email-start

The following example shows how to extend the **Merged Customers** table to support email addresses that are tagged with namespaced custom email semantic tags: **email-home** and **email-work**. These tags are applied in addition to the default **email** semantic. These tags will create two columns in the **Unified Coalesced** table: **email_home** and **email_work**.

.. table-merged-customers-extend-pii-semantic-email-end

**To support custom email semantics**

.. table-merged-customers-extend-pii-semantic-email-steps-start

#. From the **Customer 360** page, under **All Databases**, open the menu for the customer 360 database, and then select **Edit**.
#. Open the menu for the **Merged Customers** table and select **Edit**.
#. Find the **Unified_Preprocessed** section and add the highlighted line:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 3

      ,Unified_Preprocessed AS (
        SELECT *
        ,COALESCE(email_home, email_work) AS email_p
        FROM Unified_Coalesced uc
        LEFT JOIN Source_Priority sp ON sp.sp_datasource = uc.datasource
      )

   Replace **email_home** and **email_work** with the correct names for the custom semantic tags pattern you are using for your tenant.

#. Find the **NAMED_STRUCT** with the **email** column, and then update it to use the coalesced column **email_p**. This must be done in the following locations:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 2,7

      ,NAMED_STRUCT(
        'email', email_p
        ,'pk', pk
        ,'update_dt', update_dt
        ,'datasource', datasource
        ,'priority', COALESCE(fp.email_pri, up.priority, 999)
        ,'completion', INT(ISNOTNULL(email_p))
      ) AS `email_struct`

#. Validate the query.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Verify these settings, and then click **Save**.
#. Run the customer 360 database.

.. table-merged-customers-extend-pii-semantic-email-steps-end


.. _table-merged-customers-extend-pii-semantic-phone:

Multiple phone numbers
--------------------------------------------------

.. table-merged-customers-extend-pii-semantic-phone-start

The following example shows how to extend the **Merged Customers** table to support multiple phone numbers that are tagged with ordinal custom semantic tags: **phone-1** and **phone-2**. These tags are applied in addition to the default **phone** semantic. These tags will create two columns in the **Unified Coalesced** table: **phone_1** and **phone_2**.

.. table-merged-customers-extend-pii-semantic-phone-end

**To support custom phone semantics**

.. table-merged-customers-extend-pii-semantic-phone-steps-start

#. From the **Customer 360** page, under **All Databases**, open the menu for the customer 360 database, and then select **Edit**.
#. Open the menu for the **Merged Customers** table and select **Edit**.
#. Find the **Unified_Preprocessed** section and add the highlighted line:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 3

      ,Unified_Preprocessed AS (
        SELECT *
        ,COALESCE(phone_1, phone_2) AS phone_p
        FROM Unified_Coalesced uc
        LEFT JOIN Source_Priority sp ON sp.sp_datasource = uc.datasource
      )

   Replace **phone_1** and **phone_2** with the correct names for the custom semantic tags pattern you are using for your tenant.

#. Find the **NAMED_STRUCT** with the **phone** column, and then update it to use the coalesced column **phone_p**. This must be done in the following locations:

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 2,7

      ,NAMED_STRUCT(
        'phone', phone_p
        ,'pk', pk
        ,'update_dt', update_dt
        ,'datasource', datasource
        ,'priority', COALESCE(fp.phone_pri, up.priority, 999)
        ,'completion', INT(ISNOTNULL(phone_p))
      ) AS `phone_struct`

#. Validate the query.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Verify these settings, and then click **Save**.
#. Run the customer 360 database.

.. table-merged-customers-extend-pii-semantic-phone-steps-end
