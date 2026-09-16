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

.. note:: Address-based householding is a starting point. An implementation of address-based householding can vary across brand use cases, depending on the

   * Type and number of data sources
   * Number of addresses
   * Types of direct mail campaigns that will be based on the results

.. householding-address-based-note-end


.. _householding-address-how-it-works:

How it works
==================================================

.. householding-address-based-start

Address-based householding is built upon the results of the **Merged Customers** table. This enables address-based householding the ability to use the results of individual identity resolution that is available from the **Merged Customers** table.

Apply the results of address-based householding to campaigns that rely on physical addresses, such as direct mail campaigns, to ensure that a single household gets a single piece of direct mail, even when many unique individuals reside within the same household.

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

Address standardization starts as a feed that loads a CSV file that has a list of address variations for state and street names.

.. householding-address-add-feed-end

.. note::

   .. include:: ../../amperity_operator/source/data_assets.rst
      :start-after: .. data-asset-address-standardization-prerequisites-start
      :end-before: .. data-asset-address-standardization-prerequisites-end

**To add the address standardization data asset**

.. include:: ../../amperity_operator/source/data_assets.rst
   :start-after: .. data-asset-address-standardization-steps-start
   :end-before: .. data-asset-address-standardization-steps-end


.. _householding-address-add-merged-households-table:

Add Merged Households table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-merged-households-table-start
   :end-before: .. term-merged-households-table-end

.. householding-address-add-merged-households-table-start

The **Merged Households** table starts as a SQL template that defines how address-based householding works in Amperity.

.. householding-address-add-merged-households-table-end

.. householding-address-add-merged-households-table-steps-start

#. From the **Customer 360** tab, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. Click **Add Table**. Name the table "Merged_Households".
#. Set **Build Mode** to "SQL", and then define a SQL query.

   .. important:: Amperity uses a single table in the customer 360 database to collect rows from the **Unified Coalesced** table, and then collapses them into a single row per Amperity ID.

   This is referred to as the **Merged Customers** table. Prior to August 1, 2020 the name of this table was **Unified Merged**. Verify the name of this table as it is used for your tenant, and then update the template to match the name of the table in your tenant.

#. The section titled "Basic address standardization" is a common table expression (CTE) that performs address standardization.

   .. admonition:: What is address standardization?

      Address standardization is a process that

      * Removes non-alphanumeric characters
      * Trims for leading, trailing, and repeating whitespace
      * Converts characters to uppercase
      * Converts all valid names of states in the United States to their two-character representation
      * Converts all postal codes to five digits
      * Converts common representations of street addresses into standardized variants

   Physical street addresses, as identified by the **address** field, are standardized by splitting on spaces. Each of the second, third, fourth, etc. elements of an address are compared to a lookup table. When matches are found, they are replaced with standardized values.

#. The section titled "Build the Household ID" builds a universally unique identifier (UUID) from unique combinations of the **address** and **surname** fields.

#. The section titled "Get count of Amperity ID per Household ID" associates a count of Amperity IDs to each Household ID.

   .. tip:: Additional SQL may be added to handle custom statistics on a per-household basis and to support other tenant-specific use cases. The default behavior only associates the Amperity ID to the Household ID, but can be tailored to support most use cases.

      For example, you could add support for checking the number of Amperity IDs associated with a household, and if that exceeds a threshold, that address could be flagged as a business address or some other non-household entity.

#. The section titled "Create flag for addresses in bad-values blocklist" identifies if addresses have been added to the bad-values blocklist.

   If you are using the bad-values blocklist, uncomment the following sections.

   The **blv_address** block (lines 209 to 220):

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

   .. tip:: Extend to support additional use cases, such as for specific household-level statistics or to add filter criteria that checks for **BL.amperity_id IS NULL** or for **ST.amperity_id IS NULL**.

#. Click **Validate** to verify that the SQL query runs correctly.
#. Make the table available to the visual **Segment Editor** by checking the box in the **Show in VSE?** column.

   .. note:: The **Merged Households** table has the Amperity ID and should be made available to the **Visual Segment Editor**.
#. Click **Activate** to update the customer 360 database with your changes, and then run the customer 360 database to update the **Merged Households** table.

.. householding-address-add-merged-households-table-steps-end


.. _householding-address-build-segments:

Build queries and segments
==================================================

.. householding-address-build-segments-start

The default **Merged Households** table makes available two new columns for segmentation: **household_id** (the address-based Household ID) and **household_size** (the number of unique individuals who share the same physical address).

As a SELECT statement, the **Merged Household** table is similar to:

.. code-block:: sql
   :linenos:

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
   FROM Merged_Households

.. householding-address-build-segments-end
