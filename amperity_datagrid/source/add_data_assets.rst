.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Add a variety of data assets, including data sources that show email engagement and loyalty programs, to your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Add a variety of data assets, including data sources that show email engagement and loyalty programs, to your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        Data assets

==================================================
Data assets
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-assets-start
   :end-before: .. term-data-assets-end


.. _data-asset-customer-attributes:

Customer attributes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-customer-attributes-table-start
   :end-before: .. term-customer-attributes-table-end

.. data-asset-customer-attributes-start

The :doc:`Customer Attributes <table_customer_attributes>` table has a small number of specific requirements. A series of recommended and optional configurations are also available. You may enable any of the optional configurations for your tenant. In some cases, an optional configuration has its own set of specific requirements.

.. data-asset-customer-attributes-end


.. _data-asset-customer-consent:

Customer consent
==================================================

.. data-asset-customer-consent-start

Customer consent data assets help your brand keep track of which customers can (and cannot) be sent email and/or SMS messages.

.. data-asset-customer-consent-end


.. _data-asset-customer-consent-all-opted-email:

All opted-in email addresses
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-all-opted-in-emails-table-start
   :end-before: .. term-all-opted-in-emails-table-end

.. data-asset-customer-consent-all-opted-email-start

The **All Opted In Emails** table requires the :ref:`Email Opt Status <data-asset-customer-consent-email>` table, after which you can extend support for additional requirements.

.. data-asset-customer-consent-all-opted-email-end


.. _data-asset-customer-consent-email:

Email opt status
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-opt-status-table-start
   :end-before: .. term-email-opt-status-table-end

.. data-asset-customer-consent-email-start

Apply **email-opt** semantic tags to data sources, and then add the :doc:`Email Opt Status <table_email_opt_status>` table to your customer 360 database as a passthrough table.

.. data-asset-customer-consent-email-end


.. _data-asset-customer-consent-sms:

SMS opt status
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-sms-opt-status-table-start
   :end-before: .. term-sms-opt-status-table-end

.. data-asset-customer-consent-sms-start

Apply **sms-opt** semantic tags to data sources, and then add the :doc:`SMS Opt Status <table_sms_opt_status>` table to your customer 360 database as a passthrough table.

.. data-asset-customer-consent-sms-end


.. _data-asset-email-engagement:

Email engagement
==================================================

.. data-asset-email-engagement-start

Email engagement captures interactions with the emails that your brand has sent to your customers. There are three sets of data that you can make available in your tenant:

* :ref:`Email engagment attributes <data-asset-email-engagement-attributes>`
* :ref:`Email engagment summaries <data-asset-email-engagement-summary>`
* :ref:`Unified email events <data-asset-email-unified-events>`

.. data-asset-email-engagement-end


.. _data-asset-email-engagement-attributes:

Engagement attributes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-engagement-attributes-table-start
   :end-before: .. term-email-engagement-attributes-table-end

.. data-asset-email-engagement-attributes-start

Apply **email-attributes/** semantic tags to data sources, and then add the :doc:`Email Engagement Attributes <table_email_engagement_attributes>` table to your customer 360 database using a built-in SQL template. Some customization of this SQL template is necessary to align the behavior of this table to the data that exists in your tenant.

.. data-asset-email-engagement-attributes-end


.. _data-asset-email-engagement-summary:

Engagement summary
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-engagement-summary-table-start
   :end-before: .. term-email-engagement-summary-table-end

.. data-asset-email-engagement-summary-start

The :doc:`Email Engagement Summary <table_email_engagement_summary>` table is generated as Stitch output after applying |semantics_email_events_summary| semantic tags (when available) alongside |semantics_email_events| semantic tags to data sources that contain email engagement data, such as opens, clicks, opt-in and opt-out preferences, or conversions.

.. data-asset-email-engagement-summary-end


.. _data-asset-email-unified-events:

Unified email events
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-email-events-table-start
   :end-before: .. term-unified-email-events-table-end

.. data-asset-email-unified-events-start

The :doc:`Unified Email Events <table_unified_email_events>` table is generated as Stitch output after applying |semantics_email_events| semantic tags to data sources that contain email engagement data, such as opens, clicks, opt-in and opt-out preferences, or conversions.

.. data-asset-email-unified-events-end


.. _data-asset-fiscal-calendars:

Fiscal calendars
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-fiscal-calendar-start
   :end-before: .. term-fiscal-calendar-end

.. data-asset-fiscal-calendars-start

You may use one of the following data assets to define a fiscal calendar or you may provide to Amperity a file that contains your brand's complete fiscal calendar:

* :ref:`data-asset-fiscal-calendar-nrf`
* :ref:`data-asset-fiscal-calendar-extended`

.. data-asset-fiscal-calendars-end


.. _data-asset-fiscal-calendar-nrf:

NRF calendar
--------------------------------------------------

.. data-asset-fiscal-calendar-nrf-start

The NRF calendars data asset contains a |ext_nrf_454| that spans from 2016-2024 and divides each year into months based on a 4 weeks - 5 weeks - 4 weeks format. Each month has the same number of Saturdays and Sundays, which ensures like days can be compared.

.. data-asset-fiscal-calendar-nrf-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-454-calendar-start
   :end-before: .. term-454-calendar-end

**To add the NRF calendar data asset**

.. data-asset-fiscal-calendar-nrf-steps-start

Add the NRF calendar data asset to your tenant by pulling the file that is available from **Amperity Data Assets**, which is the name of an Amazon S3 bucket that can be made available to your tenant. Follow the steps for :ref:`adding a data source and feed <source-amazon-s3-add-data-source>`. Click **Browse** and select the "NRF_Calendar.csv" file from the **Amperity Data Assets** Amazon S3 bucket.

.. note:: If Amperity data assets credentials are not available on your tenant, make a request to Amperity Support to enable Amperity data assets for your tenant.

Add a passthrough table to your customer 360 database named **NRF Calendar**, and then run your customer 360 database to build the **NRF Calendar** table.

.. data-asset-fiscal-calendar-nrf-steps-end


.. _data-asset-fiscal-calendar-extended:

Extended fiscal calendar
--------------------------------------------------

.. data-asset-fiscal-calendar-extended-start

.. important:: Ask your Amperity representative for help building a customized fiscal calendar for your tenant that includes holidays and marketing windows that are important for your brand.

You can |ext_fiscal_calendar_download| that runs from 2016 to 2030 and uses a 4-5-4 pattern. This fiscal calendar includes the following holidays:

* New Year's Day
* Martin Luther King Day
* Valentine's Day
* President's Day
* St. Patrick's Day
* Memorial Day weekend
* Canada Day
* Independence Day
* Juneteenth
* Labor Day weekend
* Halloween
* Thanksgiving weekend
* Black Friday
* Cyber Monday
* Christmas
* Boxing Day

Use this CSV file to explore what a fiscal calendar looks like. Use a text editor to add additional holidays, extend for additional years, and so on. You may upload this CSV file to Amperity directly using the **Feed Editor**, and then apply semantic tags for fiscal calendars.

.. data-asset-fiscal-calendar-extended-end


.. _data-asset-loyalty-programs:

Loyalty programs
==================================================

.. data-asset-loyalty-programs-start

A loyalty program helps your brand build positive experiences with your customers in the form of rewards, referral programs, early access, incentives, customer community, more direct ways to provide feedback, and more.

Your highest-value customers are often members of your brand's loyalty program. Use the loyalty data assets to analyze the performance of your loyalty program and look for ways to improve the experiences your customers have with your brand.

.. data-asset-loyalty-programs-end


.. _data-asset-loyalty-events:

Loyalty events
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-loyalty-events-table-start
   :end-before: .. term-unified-loyalty-events-table-end

.. data-asset-loyalty-events-start

Apply |semantics_loyalty_events| semantic tags to data sources, and then add the :doc:`Unified Loyalty Events <table_unified_loyalty_events>` table to your customer 360 database as a passthrough table.

.. data-asset-loyalty-events-end


.. _data-asset-loyalty-profiles:

Loyalty profiles
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-loyalty-table-start
   :end-before: .. term-unified-loyalty-table-end

.. data-asset-loyalty-profiles-start

Apply |semantics_loyalty_profiles| semantic tags to data sources, and then add the :doc:`Unified Loyalty <table_unified_loyalty>` table to your customer 360 database as a passthrough table, after which you can analyze retention rates and customer value for your loyalty program. For example:

* :ref:`table-unified-loyalty-example-retention-analysis`
* :ref:`table-unified-loyalty-example-value-analysis`

.. data-asset-loyalty-profiles-end


.. _data-asset-reference:

Reference data assets
==================================================

.. data-asset-reference-start

The following file-based data assets are available:

* :ref:`data-asset-address-standardization`
* :ref:`data-asset-gender-name-ratios`
* :ref:`data-asset-lookup-table-row`
* :ref:`data-asset-lookup-table-usa`
* :ref:`data-asset-lookup-table-zip`
* :ref:`data-asset-fiscal-calendar-nrf`

.. data-asset-reference-end


.. _data-asset-reference-enable:

Enable file-based data assets
--------------------------------------------------

.. data-asset-files-request-to-enable-start

Amperity makes CSV files available to your tenant from an Amazon S3 bucket. Create a support ticket and request to enable the "Amperity data assets Amazon S3 bucket" for your tenant. Use any of these options:

* The `Amperity Support Portal <../support/index.html>`__
* The **Report a problem** option in Amperity
* By sending an email to support@amperity.com

After the Amperity data assets Amazon S3 bucket is enabled, use a courier to pull individual data assets from that location to your tenant using an Amazon S3 data source.

.. data-asset-files-request-to-enable-end


.. _data-asset-address-standardization:

Address standardization
--------------------------------------------------

.. data-asset-address-standardization-start

Address standardization is a data asset that contains a list of address variations for state and street names within the United States. Use this data asset to support :doc:`address-based householding <householding>` workflows.

.. data-asset-address-standardization-end

.. data-asset-address-standardization-prerequisites-start

The address standardization data asset is available from an Amazon S3 bucket named **Amperity Data Assets**. You may make a request to Amperity Support to :ref:`enable file-based data assets <data-asset-reference-enable>`, after which you can use the `Amazon S3 data source <https://docs.amperity.com/datagrid/source_amazon_s3.html>`__ to load the "address_standardization_conversion.csv" file from the "/householding" directory in that bucket.

.. data-asset-address-standardization-prerequisites-end

**To add the address standardization data asset**

.. data-asset-address-standardization-steps-start

Add the address standardization data asset to your tenant by following the steps for :ref:`adding a data source and feed from an Amazon S3 bucket <source-amazon-s3-add-data-source>`. Click **Browse** and select the "address_standardization_conversion.csv" file from the **Amperity Data Assets** Amazon S3 bucket, which is located in the "householding" directory in the bucket.

Use all three fields – **before**, **convert**, and **type** as the primary key.

Add a passthrough table to your customer 360 database named **LookupTables AddressStandardization**, and then run your customer 360 database to build the **LookupTables AddressStandardization** table.

.. important:: The **LookupTables AddressStandardization** table is used within the **Merged Households** SQL template in a series of LEFT JOIN operations that are used to standardize addresses. For example:

   .. code-block:: sql

      LEFT JOIN (
        SELECT
          UPPER(before) AS before
          ,UPPER(convert) AS converted
        FROM LookupTables_AddressStandardization
        WHERE type = 'STREET'
      ) AS a7clean ON (a7clean.before = core.a7)

   You can name this table *anything* else, such as **Address Standardization USA**. If you use the **Merged Households** SQL template, you will need to update the LEFT JOIN sections within that template to contain the updated table name.

.. data-asset-address-standardization-steps-end


.. _data-asset-gender-name-ratios:

Gender name ratios
--------------------------------------------------

.. data-asset-gender-name-ratios-link-start

Use the gender name ratios data asset to use :doc:`gender prediction <predict_gender>` to apply personalization strategies to your marketing campaigns.

.. data-asset-gender-name-ratios-link-end

.. data-asset-gender-name-ratios-start

The **gender_name_ratios.csv** file contains a list of baby names from the past ~130 years, along with their associated gender.

The source of the data in the **gender_name_ratios.csv** file is from United States Social Security Administration records for |baby_names|. These records were used to generate the **gender_name_ratios.csv** file, which is similar to:

.. code-block:: text

   given_name,predicted_gender,gender_name_ratio,male_count,female_count
   EMILIA,F,7178.6,5,35893
   THERESE,F,7025.0,5,35125
   AILEEN,F,6969.8,5,34849
   ...
   LINDSEY,F,20.2,7710,156111
   MORRISON,M,20.2,1496,74
   ROLLA,M,20.1,1306,65

The most important column is **gender_name_ratio**, which describes what proportion of **given_name** is associated with one gender versus the other.

.. note:: Only names with a ratio greater than 20 are included. This ensures that any prediction has a ~95% chance of being accurate based on the given name.

   Only names with at least 1000 male or female examples were included. This filters out very uncommon names.

.. data-asset-gender-name-ratios-end

**To add the gender name ratios data asset**

.. data-asset-gender-name-ratios-steps-start

Add the gender name ratios data asset to your tenant by pulling the file that is available from **Amperity Data Assets**, which is the name of an Amazon S3 bucket that can be made available to your tenant. Follow the steps for :ref:`adding a data source and feed <source-amazon-s3-add-data-source>`. Click **Browse** and select the "gender_name_ratios.csv" file from the **Amperity Data Assets** Amazon S3 bucket.

Use **given_name** as the primary key.

.. note:: If Amperity data assets credentials are not available on your tenant, make a request to Amperity Support to enable Amperity data assets for your tenant.

You can add predicted gender to your customer 360 database in two ways, depending on how your brand wants to use predicted gender to build segments:

#. Extend the **Customer 360** and/or **Merged Customers** tables to include predicted gender (recommended).
#. Add predicted gender values to your customer 360 database as a standalone table.

**Extend the Merged_Customers table (recommended)**

.. note:: The steps are the same for both the **Customer 360** and **Merged Customers** tables.

   Edit the **Merged Customers** table and extend the table for predicted gender.

Use a common table expression (CTE) to pull data from the domain table that contains predicted gender data ("Predictions_Gender"):

.. code-block:: sql

   predict_gender AS (
     SELECT
       mc.amperity_id
       ,CASE
         WHEN UPPER(ratios.predicted_gender) = 'M' THEN 'Male'
         WHEN UPPER(ratios.predicted_gender) = 'F' THEN 'Female'
         ELSE ratios.predicted_gender
       END AS predicted_gender
     FROM Merged_Customers AS mc
     LEFT JOIN Predictions_Gender AS ratios
     ON UPPER(
       COALESCE(mc.given_name, SPLIT(mc.full_name,' ')[0])
     ) = ratios.given_name
   ),

Update the list of columns in the **Merged Customers** table to include predicted gender and combined gender:

.. code-block:: sql

   ,pg.predicted_gender
   ,COALESCE(mc.gender,pg.predicted_gender) AS combined_gender

.. note:: The combined gender column uses the value from the **gender** column in the **Merged Customers** table when a value exists, and then uses the value from the **predicted_gender** column if the **gender** column in the **Merged Customers** table is empty. 

Use a **LEFT JOIN** to join the values from the common table expression to the **Merged Customers** table:
 
.. code-block:: sql

   LEFT JOIN predict_gender pg ON pg.amperity_id = mc.amperity_id

**Add a table for predicted gender (optional)**

Your brand's use cases for predicted gender may prefer using a standalone table.

#. Add a passthrough table to your customer 360 database named **Gender Name Ratios**.
#. Add a SQL table to your customer 360 database named **Predicted Gender**.
#. Choose **SQL** as the build mode, and then use SQL similar to:

   .. code-block:: sql

      WITH ratios AS (
        SELECT * 
        FROM Gender_Name_Ratios 
        WHERE gender_name_ratio >= 100
      )

      SELECT
        mc.amperity_id
        ,ratios.predicted_gender
      FROM Merged_Customers AS mc
      LEFT JOIN Gender_Name_Ratios AS ratios
      ON UPPER(
        COALESCE(mc.given_name, SPLIT(mc.full_name,' ')[0])
      ) = ratios.given_name

   where "100" represents a 99% accuracy threshold. Increase or decrease this value as necessary.

   .. tip:: This table will be unique by Amperity ID and may be made available to the **Segment Editor** for use with campaigns.

.. data-asset-gender-name-ratios-steps-end


.. _data-asset-lookup-tables:

Lookup tables
--------------------------------------------------

.. data-asset-lookup-tables-start

The following lookup tables are available from Amperity data assets:

* :ref:`data-asset-lookup-table-row`
* :ref:`data-asset-lookup-table-usa`
* :ref:`data-asset-lookup-table-zip`

.. data-asset-lookup-tables-end


.. _data-asset-lookup-table-row:

Lookup: Countries
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-asset-lookup-table-row-start

The country lookup data asset provides a set of standardized names and codes for all countries, along with categories for regions (Americas, Asia, Africa, etc.), sub-regions (Latin America and the Caribbean, Sub-Saharan Africa, etc.), and region codes.

.. data-asset-lookup-table-row-end

**To add the country lookups data asset**

.. data-asset-lookup-table-row-steps-start

Add the country lookups data asset to your tenant by pulling the file that is available from **Amperity Data Assets**, which is the name of an Amazon S3 bucket that can be made available to your tenant. Follow the steps for :ref:`adding a data source and feed <source-amazon-s3-add-data-source>`. Click **Browse** and select the "lookup_country.csv" file from the **Amperity Data Assets** Amazon S3 bucket.

Use **country_name** and **country_code** as the primary key.

.. note:: If Amperity data assets credentials are not available on your tenant, make a request to Amperity Support to enable Amperity data assets for your tenant.

Add a passthrough table to your customer 360 database named **Lookup Countries**, and then run your customer 360 database to build the **Lookup Countries** table.

.. data-asset-lookup-table-row-steps-end


.. _data-asset-lookup-table-usa:

Lookup: United States
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-asset-lookup-table-usa-start

The country lookup data asset provides a set of standardized names and codes for the United States, including states and territories, along with United States Postal Service (USPS) and International Organization for Standardization (ISO) codes.

.. data-asset-lookup-table-usa-end

**To add the United States lookups data asset**

.. data-asset-lookup-table-usa-steps-start

Add the United States lookup data asset to your tenant by pulling the file that is available from **Amperity Data Assets**, which is the name of an Amazon S3 bucket that can be made available to your tenant. Follow the steps for :ref:`adding a data source and feed <source-amazon-s3-add-data-source>`. Click **Browse** and select the "lookup_us_state_territory.csv" file from the **Amperity Data Assets** Amazon S3 bucket.

Use a combination of **US_State_Territory_Name**, **USPS_Code**, and **ISO_Code_2** as the primary key.

.. note:: If Amperity data assets credentials are not available on your tenant, make a request to Amperity Support to enable Amperity data assets for your tenant.

Add a passthrough table to your customer 360 database named **Lookup USA**, and then run your customer 360 database to build the **Lookup USA** table.

.. data-asset-lookup-table-usa-steps-end


.. _data-asset-lookup-table-zip:

Lookup: Zip codes
++++++++++++++++++++++++++++++++++++++++++++++++++

.. data-asset-lookup-table-zip-start

The zip codes lookup data asset provides a list of zip codes that:

* Identifies if a zip code is standard, a post office box, or unique
* Associates the primary city for each zip code
* The state, county, and time zone in which a zip code is located
* The phone number area codes associated with a zip code
* The number of households and population counts within each zip code, including demographics
* Geolocation data for each zip code

.. data-asset-lookup-table-zip-end

**To add the zip codes lookups data asset**

.. data-asset-lookup-table-zip-steps-start

Add the zip codes lookups data asset to your tenant by pulling the file that is available from **Amperity Data Assets**, which is the name of an Amazon S3 bucket that can be made available to your tenant. Follow the steps for :ref:`adding a data source and feed <source-amazon-s3-add-data-source>`. Click **Browse** and select the "zip_code_database_small_business.csv" file from the **Amperity Data Assets** Amazon S3 bucket.

Use **zip** as the primary key.

.. note:: If Amperity data assets credentials are not available on your tenant, make a request to Amperity Support to enable Amperity data assets for your tenant.

Add a passthrough table to your customer 360 database named **Lookup Zip Codes**, and then run your customer 360 database to build the **Lookup Zip Codes** table.

.. data-asset-lookup-table-zip-steps-end

.. _data-asset-lookup-table-normalization-usa:

Normalization: United States
--------------------------------------------------

.. data-asset-lookup-table-normalization-usa-start

The normalization for United States data asset provides a list of long and abbreviated names for all 50 states within the United States.

.. data-asset-lookup-table-normalization-usa-end

**To add the zip codes lookups data asset**

.. data-asset-lookup-table-normalization-usa-steps-start

Add the normalization for United States data asset to your tenant by pulling the file that is available from **Amperity Data Assets**, which is the name of an Amazon S3 bucket that can be made available to your tenant. Follow the steps for :ref:`adding a data source and feed <source-amazon-s3-add-data-source>`. Click **Browse** and select the "US_State_Normalization.csv" file from the **Amperity Data Assets** Amazon S3 bucket.

Use **US_State_Abbrev** and **US_State_Long** as the primary key.

.. note:: If Amperity data assets credentials are not available on your tenant, make a request to Amperity Support to enable Amperity data assets for your tenant.

Add a passthrough table to your customer 360 database named **Normalization United States**, and then run your customer 360 database to build the **Normalization United States** table.

.. data-asset-lookup-table-normalization-usa-steps-end
