.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use address-based householding to group individuals together who share the same physical address.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use address-based householding to group individuals together who share the same physical address.

.. meta::
    :content class=swiftype name=title data-type=string:
        Address-based householding

==================================================
Address-based householding
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-householding-start
   :end-before: .. term-householding-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-address-based-householding-start
   :end-before: .. term-address-based-householding-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-household-id-start
   :end-before: .. term-household-id-end

.. householding-address-based-note-start

.. note:: This topic describes address-based householding as a starting point. An implementation of address-based householding can vary significantly across brand use cases, depending on the

   * Type and number of data sources
   * Number of addresses
   * Types of direct mail campaigns that will be based on the results

.. householding-address-based-note-end


.. _householding-address-how-it-works:

How it works
==================================================

.. householding-address-based-start

Address-based householding is built upon the results of the **Merged Customers** table. This enables address-based householding the ability to use the results of individual identity resolution that was performed by Amperity (and built into the **Merged Customers** table). Apply the results of address-based householding to campaigns that rely on physical addresses, such as direct mail campaigns, to ensure that a single household gets a single piece of direct mail, even when multiple unique individuals reside within the same household.

.. householding-address-based-end

.. householding-address-based-note-start

.. tip:: Address-based householding can be improved when used alongside standardization provided by national change of address (NCOA) and coding accuracy support system (CASS).

   .. include:: ../../shared/terms.rst
      :start-after: .. term-ncoa-start
      :end-before: .. term-ncoa-end

   .. include:: ../../shared/terms.rst
      :start-after: .. term-cass-start
      :end-before: .. term-cass-end

.. householding-address-based-note-end

.. householding-address-based-sections-start

The process for enabling address-based householding includes:

#. Reviewing the :doc:`Merged Customers table <table_merged_customers>` to identify any tenant-specific behaviors within the table that may need to be considered when extending Amperity for address-based householding.
#. Reviewing the :doc:`bad-values blocklist <blocklist_bad_values>` to identify any tenant-specific behaviors within the blocklist workflow and to identify the name of the domain table associated with :ref:`the bad-values blocklist feed <bad-values-blocklist-add-feed>`.
#. :ref:`Adding a feed for the address-standardization.csv file <householding-address-add-feed>`
#. :ref:`Adding a Merged Households table to the customer 360 database <householding-address-add-merged-households-table>`
#. Building segments that use the Household ID, which is a UUID that is available to segments from the **Merged Households** table.
#. Sending segment results to any downstream process.

.. householding-address-based-sections-end

.. householding-address-based-sections-tip-start

.. tip:: Additional configuration options for address-based householding include:

   #. Joining the **Merged Households** table to the **Customer 360** table to add the **household_id** and **household_size** fields. This makes them available as profile attributes.
   #. Using a common table expression (CTE) to flag a single individual that is associated with an address as the primary contact.
   #. Adding a **Household 360** table. This is similar to the **Customer 360** table and can merge values down to a single row per Household ID. This enables the use of summary attributes, such as identifying household lifetime value.

.. householding-address-based-sections-tip-end


.. _householding-address-add-feed:

Add the data asset
==================================================

.. householding-address-add-feed-start

Address standardization starts as a feed that loads a CSV file that contains a list of address variations for state and street names.

.. householding-address-add-feed-end

.. note::

   .. include:: ../../amperity_operator/source/add_data_assets.rst
      :start-after: .. data-asset-address-standardization-prerequisites-start
      :end-before: .. data-asset-address-standardization-prerequisites-end

**To add the address standardization data asset**

.. include:: ../../amperity_operator/source/add_data_assets.rst
   :start-after: .. data-asset-address-standardization-steps-start
   :end-before: .. data-asset-address-standardization-steps-end


.. _householding-address-add-merged-households-table:

Add Merged_Households table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-merged-households-table-start
   :end-before: .. term-merged-households-table-end

.. householding-address-add-merged-households-table-start

This section walks through the default SQL template that is used to define how address-based householding works in Amperity.

.. householding-address-add-merged-households-table-end

.. householding-address-add-merged-households-table-steps-start

#. From the **Customer 360** tab, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. Click **Add Table**. Name the table "Merged_Households".
#. Set **Build Mode** to "SQL", and then define a SQL query.

   .. tip:: You may `download a copy of Merged Households <../downloads/sql/merged_households.txt>`__ as a template or you may :ref:`refer to the example <householding-address-sql-template>` at the end of this topic.

   .. important:: Amperity uses a single table in the customer 360 database to collect rows from the **Unified Coalesced** table, and then collapses them into a single row per Amperity ID. This is referred to as the **Merged Customers** table. Prior to August 1, 2020 the name of this table was **Unified Merged**. Verify the name of this table as it is used for your tenant, and then update the template described in this topic so that it matches the name of the table in your tenant.

#. The section titled "Basic address standardization" is a common table expression (CTE) that performs address standardization. This process removes non-alphanumeric characters, trims for leading, trailing, and repeating whitespace, converts characters to uppercase, converts all valid names of states in the United States to their two-character representation, converts all postal codes to five digits, and converts common representations of street addresses into standardized variants.

   Physical street addresses (as identified by the **address** field) are standardized by splitting on spaces. Each of the second, third, fourth, etc. elements of an address are compared to a lookup table. When matches are found, they are replaced with standardized values.

#. The section titled "Build the Household ID ..." builds a universally unique identifier (UUID) from unique combinations of the **address** and **surname** fields.

#. The section titled "Get count of Amperity ID per Household ID" associates a count of Amperity IDs to each Household ID.

   .. tip:: This section is where additional SQL is added to handle custom statistics on a per-household basis and to support other tenant-specific use cases. The default behavior only associates the Amperity ID to the Household ID, but can be tailored to support most use cases.

      For example, you could add support for checking the number of Amperity IDs associated with a household, and if that exceeds a threshold, that address could be flagged as a business address (or some other non-household entity).

#. The section titled "Create flag for addresses in bad-values blocklist" identifies if addresses have been added to the bad-values blocklist.

   If you are using the bad-values blocklist, uncomment the following sections.

   The **blv_address** block (lines 209 - 220):

   ::

      blv_addresses AS (
        SELECT
          amperity_id,
          CASE
            WHEN (blv.value IS NOT NULL)
            THEN TRUE
            ELSE FALSE
          END AS blv_address
        FROM clean_addresses AS AD
        LEFT JOIN Blocklist_Values AS BLV
          ON AD.address = UPPER(BLV.value)
      )

   where **Blocklist_Values** must be updated to be identical to the name of the domain table that is created by :ref:`the bad-values blocklist feed <bad-values-blocklist-add-feed>`.

   .. tip:: The **blv_addresses** block may cause duplicate rows. Use **SELECT DISTINCT** if you run into issues with duplicate rows.

   .. caution:: When uncommenting the **blv_addresses** block, be sure to add a comma after the closing parentheses (")") in the **household_stats** block or you will get a validation error.

   The **blv_address** line in the last **SELECT** statement (line 230):

   ::

      ,BL.blv_address

   The **LEFT JOIN** for **blv_addresses** (lines 248-249):

   ::

      LEFT JOIN blv_addresses AS BL
        ON CONCAT_WS(' ',AD.address,AD.address2) = UPPER(BLV.value)

#. The section titled "Build Merged_Households table" combines everything into the **Merged Households** table.

   .. tip:: Extend this section to support additional use cases, such as for specific household-level statistics or to add filter criteria that checks for **BL.amperity_id IS NULL** or for **ST.amperity_id IS NULL**.

#. Click **Validate** to verify that the SQL query runs correctly.
#. Make the table available to the visual **Segment Editor** by checking the box in the **Show in VSE?** column.

   .. note:: The **Merged Households** table contains the Amperity ID and should be made available to the **Visual Segment Editor**.
#. Click **Activate** to update the customer 360 database with your changes, and then run the customer 360 database to update the **Merged Households** table.

.. householding-address-add-merged-households-table-steps-end


.. _householding-address-build-segments:

Build queries and segments
==================================================

.. householding-address-build-segments-start

The default **Merged Households** table (as described in this topic) makes available two new columns for segmentation: **household_id** (the address-based Household ID) and **household_size** (the number of unique individuals who share the same physical address).

As a SELECT statement, the **Merged Household** table is similar to:

.. code-block:: sql

   SELECT
     amperity_id AS "amperity_id"
     ,household_id AS "household_id"
     ,household_size AS "household_size"
     ,full_address AS "full_address"
     ,given_name AS "given_name"
     ,surname AS "surname"
     ,address AS "address"
     ,address2 AS "address2"
     ,city AS "city"
     ,state AS "state"
     ,postal AS "postal"
   FROM
     Merged_Households

.. householding-address-build-segments-end


.. _householding-address-sql-template:

Merged Households template
==================================================

.. householding-address-sql-template-start

.. code-block:: sql

   -------------------------------------------------------------------------
   -- Merged_Households query                                             --
   --                                                                     --
   -- This query generates a UUID household_id for records with an exact  --
   -- match on full_address and surname. It uses Merged_Customers as a    --
   -- foundation, which means that householding occurs AFTER the best     --
   -- address has been selected, after which business rules are applied   --
   -- to define what qualifies as a household.                            --
   -------------------------------------------------------------------------

   WITH 

   -------------------------------------------------------------------------
   -- Basic address standardization                                      --
   -------------------------------------------------------------------------

   clean_addresses AS (
     SELECT
       core.*
       ,REGEXP_REPLACE(
         REPLACE(
           REPLACE(
             REPLACE(
               REPLACE(
                 REPLACE(
                   REPLACE(
                     REPLACE(
                       REPLACE(
                         CONCAT_WS(' ', core.a1,
                           COALESCE(a2clean.converted, core.a2),
                           COALESCE(a3clean.converted, core.a3),
                           COALESCE(a4clean.converted, core.a4),
                           COALESCE(a5clean.converted, core.a5),
                           core.a6,
                           core.a7,
                           address2,
                           city,
                           COALESCE(stateclean.converted, core.state),
                           postal)
                         ,' APT')
                       ,' STE')
                     ,' UNIT')
                   ,' RM')
                 ,' SPACE')
               ,' APARTMENT')
             ,' SUITE')
           ,' ROOM')
         ,' +'
       ,''
     )
     AS full_address
     FROM (
       SELECT
         amperity_id
         ,UPPER(given_name) AS given_name
         ,UPPER(COALESCE(surname, REVERSE(SPLIT(full_name,' '))[0])) AS surname
         ,UPPER(address) AS address
         ,REGEXP_REPLACE(UPPER(address2),'[.,\\/#!$%\\^&\\*;:{}=\\-_~()\\.]', '') AS address2
         ,UPPER(city) AS city
         ,TRIM(UPPER(state)) AS state
         ,UPPER(SUBSTR(postal,1,5)) AS postal
         ,CASE
           WHEN NOT SIZE(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')) >= 1 THEN ''
           ELSE REGEXP_REPLACE(UPPER(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')[0]), '[.,\\/#!$%\\^&\\*;:{}=\\-_~()\\. ]', '')
         END AS a1
         ,CASE
           WHEN NOT SIZE(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')) >= 2 THEN ''
           ELSE REGEXP_REPLACE(UPPER(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')[1]), '[.,\\/#!$%\\^&\\*;:{}=\\-_~()\\. ]', '')
         END AS a2
         ,CASE
           WHEN NOT SIZE(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')) >= 3 THEN ''
           ELSE REGEXP_REPLACE(UPPER(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')[2]), '[.,\\/#!$%\\^&\\*;:{}=\\-_~()\\. ]', '')
         END AS a3
         ,CASE
           WHEN NOT SIZE(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')) >= 4 THEN ''
           ELSE REGEXP_REPLACE(UPPER(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')[3]), '[.,\\/#!$%\\^&\\*;:{}=\\-_~()\\. ]', '')
         END AS a4
         ,CASE
           WHEN NOT SIZE(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')) >= 5 THEN ''
           ELSE REGEXP_REPLACE(UPPER(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')[4]), '[.,\\/#!$%\\^&\\*;:{}=\\-_~()\\. ]', '')
         END AS a5
         ,CASE
           WHEN NOT SIZE(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')) >= 6 THEN ''
           ELSE REGEXP_REPLACE(UPPER(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')[5]), '[.,\\/#!$%\\^&\\*;:{}=\\-_~()\\. ]', '')
         END AS a6
         ,CASE
           WHEN NOT SIZE(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')) >= 7 THEN ''
           ELSE REGEXP_REPLACE(UPPER(SPLIT(REGEXP_REPLACE(address,' {2,}',' '), ' ')[6]), '[.,\\/#!$%\\^&\\*;:{}=\\-_~()\\. ]', '')
         END AS a7

       FROM
         Merged_Customers
         WHERE address IS NOT NULL
         AND city IS NOT NULL
         AND state IS NOT NULL
         AND postal IS NOT NULL
         AND COALESCE(surname, REVERSE(SPLIT(full_name,' '))[0]) IS NOT NULL
     ) AS core

     LEFT JOIN (
       SELECT
         UPPER(before) AS before
         ,UPPER(convert) AS converted
       FROM LookupTables_AddressStandardization
       WHERE type = 'STREET'
     ) AS a1clean ON (a1clean.before = core.a1)

     LEFT JOIN (
       SELECT
         UPPER(before) AS before
         ,UPPER(convert) AS converted
       FROM LookupTables_AddressStandardization
       WHERE type = 'STREET'
     ) AS a2clean ON (a2clean.before = core.a2)

     LEFT JOIN (
       SELECT
         UPPER(before) AS before
         ,UPPER(convert) AS converted
       FROM LookupTables_AddressStandardization
       WHERE type = 'STREET'
     ) AS a3clean ON (a3clean.before = core.a3)

     LEFT JOIN (
       SELECT
         UPPER(before) AS before
         ,UPPER(convert) AS converted
       FROM LookupTables_AddressStandardization
       WHERE type = 'STREET'
     ) AS a4clean ON (a4clean.before = core.a4)

     LEFT JOIN (
       SELECT
         UPPER(before) AS before
         ,UPPER(convert) AS converted
       FROM LookupTables_AddressStandardization
       WHERE type = 'STREET'
     ) AS a5clean ON (a5clean.before = core.a5)

     LEFT JOIN (
       SELECT
         UPPER(before) AS before
         ,UPPER(convert) AS converted
       FROM LookupTables_AddressStandardization
       WHERE type = 'STREET'
     ) AS a6clean ON (a6clean.before = core.a6)

     LEFT JOIN (
       SELECT
         UPPER(before) AS before
         ,UPPER(convert) AS converted
       FROM LookupTables_AddressStandardization
       WHERE type = 'STREET'
     ) AS a7clean ON (a7clean.before = core.a7)

     LEFT JOIN (
       SELECT
         UPPER(before) AS before
         ,UPPER(convert) AS converted
       FROM LookupTables_AddressStandardization
       WHERE type = 'STATE'
     ) AS stateclean ON (stateclean.before = core.state)

   ),

   -------------------------------------------------------------------------
   -- Build the Household ID from full_address + surname as a UUID        --
   -------------------------------------------------------------------------

   uuid_ids AS (
     SELECT
       amperity_id
       ,CONCAT_WS(
         '-'
         ,substr(household_id, 1,  8)
         ,substr(household_id, 9,  4)
         ,substr(household_id, 13, 4)
         ,substr(household_id, 17, 4)
         ,substr(household_id, 21, 12)) AS household_id
     FROM (
       SELECT
         amperity_id
         ,SHA(CONCAT(full_address, surname)) AS household_id
       FROM
         clean_addresses
     )
   ),

   -------------------------------------------------------------------------
   -- Get count of Amperity ID per Household ID                           --
   -- For use with downstream filters                                     --
   -------------------------------------------------------------------------

   household_stats AS (
     SELECT
       household_id
       ,COUNT(DISTINCT amperity_id) AS amperity_id_count
     FROM uuid_ids
     WHERE household_id IS NOT NULL
     GROUP BY 1
   ),

   -------------------------------------------------------------------------
   -- Create flag for addresses in bad-values blocklist                   --
   -- Blocklist_Values is the name of a domain table; verify then update  --
   -- For use with downstream filters                                     --
   -------------------------------------------------------------------------

   blv_addresses AS (
     SELECT
       amperity_id,
       CASE
         WHEN (blv.value IS NOT NULL)
         THEN TRUE
         ELSE FALSE
       END AS blv_address
     FROM clean_addresses AS AD
     LEFT JOIN Blocklist_Values AS BLV
       ON CONCAT_WS(' ',AD.address,AD.address2) = UPPER(BLV.value)
   )

   -------------------------------------------------------------------------
   -- Build Merged_Households table                                       --
   -------------------------------------------------------------------------

   SELECT distinct
     AD.amperity_id
     ,ID.household_id
     ,ST.amperity_id_count AS household_size
     ,BL.blv_address
     ,AD.full_address
     ,AD.given_name
     ,AD.surname
     ,AD.address
     ,AD.address2
     ,AD.city
     ,AD.state
     ,AD.postal

   FROM clean_addresses AS AD

   LEFT JOIN uuid_ids AS ID
     ON AD.amperity_id = ID.amperity_id

   LEFT JOIN household_stats AS ST
     ON ID.household_id = ST.household_id

   LEFT JOIN blv_addresses AS BL
     ON AD.amperity_id = BL.amperity_id

.. householding-address-sql-template-end
