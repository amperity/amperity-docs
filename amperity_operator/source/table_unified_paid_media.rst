.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Unified Paid Media table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Paid Media table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Paid Media table

==================================================
Unified Paid Media table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-paid-media-table-start
   :end-before: .. term-unified-paid-media-table-end

.. table-unified-paid-media-table-group-note-start

.. note:: The **Unified Paid Media** table is built from the **Unified Coalesced** table to build customer profiles that include *all known personally identifiable information (PII)*, including email addresses, phone numbers, and physical addresses.

   Add this table to your customer 360 database when your brand wants to send all known PII downstream for use with paid media campaigns.

.. table-unified-paid-media-table-group-note-end


.. _table-unified-paid-media-add:

Add table
==================================================

.. table-unified-paid-media-add-start

The **Unified Paid Media** table is an optional table for the customer 360 database. The **Unified Paid Media** table is built using a SQL template.

.. table-unified-paid-media-add-end

.. table-unified-paid-media-add-table-note-start

.. note:: The **Unified Paid Media** table uses a Spark SQL query to pull the Amperity ID, along with all known PII data, from the **Unified Coalesced** table.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-unified-coalesced-table-start
      :end-before: .. term-unified-coalesced-table-end

.. table-unified-paid-media-add-table-note-end

**To add the Unified Paid Media table**

.. table-unified-paid-media-add-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Unified_Paid_Media".
#. Set the build mode to **SQL**.
#. Click **Apply template**, and then select **Unified Paid Media**.
#. Click **Validate** to verify the SQL runs without error.
#. Optional. :ref:`Adjust the row limit <table-unified-paid-media-sql-query-optional-configure-row-limit>`.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Verify that semantic tags--**given_name**, **surname**, **email**, **phone**, **address**, **city**, **state**, **postal**, **birthdate**, **gender**, etc.--were applied to all PII fields correctly.

   .. tip:: You can clear incorrectly tagged semantics individually or for the entire table. To clear semantic tags for the entire table, under **Semantic Suggestions** click **Clear semantics**.
#. Under **Version History**, select **Enable table version history**.
#. Click **Save**.

.. table-unified-paid-media-add-steps-end


.. _table-unified-paid-media-sql-query:

SQL query
--------------------------------------------------

.. table-unified-paid-media-sql-query-start

The following SQL query is the recommended starting point for the **Unified Paid Media** table. It is a series of window function that collects and groups all known PII data, and then a statement that updates the **Unified Paid Media** table with the results.

.. table-unified-paid-media-sql-query-end


.. _table-unified-paid-media-sql-query-recommended:

Recommended starting point
--------------------------------------------------

.. table-unified-paid-media-sql-query-recommended-start

The following query is the starting point for the **Unified Paid Media** table.

.. code-block:: sql
   :caption: sql-unified-paid-media
   :linenos:

   WITH pii_row_limit AS (
     SELECT 10 AS limit
   )

   ,all_ampids AS (
     SELECT DISTINCT
       amperity_id
     FROM Unified_Coalesced
   )

   ,address_and_details_prep AS (
     SELECT DISTINCT
       amperity_id
       ,LOWER(given_name) AS given_name
       ,LOWER(surname) AS surname
       ,LOWER(address) AS address
       ,LOWER(address2) AS address_line_2
       ,LOWER(city) AS city
       ,CASE
         WHEN TRIM(LOWER(state)) IN ('alabama','al') THEN 'AL'
         WHEN TRIM(LOWER(state)) IN ('alaska','ak') THEN 'AK'
         WHEN TRIM(LOWER(state)) IN ('arizona','az') THEN 'AZ'
         WHEN TRIM(LOWER(state)) IN ('arkansas','ar') THEN 'AR'
         WHEN TRIM(LOWER(state)) IN ('california','ca') THEN 'CA'
         WHEN TRIM(LOWER(state)) IN ('colorado','co') THEN 'CO'
         WHEN TRIM(LOWER(state)) IN ('connecticut','ct') THEN 'CT'
         WHEN TRIM(LOWER(state)) IN ('delaware','de') THEN 'DE'
         WHEN TRIM(LOWER(state)) IN ('district of columbia','dc') THEN 'DC'
         WHEN TRIM(LOWER(state)) IN ('florida','fl') THEN 'FL'
         WHEN TRIM(LOWER(state)) IN ('georgia','ga') THEN 'GA'
         WHEN TRIM(LOWER(state)) IN ('hawaii','hi') THEN 'HI'
         WHEN TRIM(LOWER(state)) IN ('idaho','id') THEN 'ID'
         WHEN TRIM(LOWER(state)) IN ('illinois','il') THEN 'IL'
         WHEN TRIM(LOWER(state)) IN ('indiana','IN') THEN 'IN'
         WHEN TRIM(LOWER(state)) IN ('iowa','ia') THEN 'IA'
         WHEN TRIM(LOWER(state)) IN ('kansas','ks') THEN 'KS'
         WHEN TRIM(LOWER(state)) IN ('kentucky','ky') THEN 'KY'
         WHEN TRIM(LOWER(state)) IN ('louisiana','la') THEN 'LA'
         WHEN TRIM(LOWER(state)) IN ('maine','me') THEN 'ME'
         WHEN TRIM(LOWER(state)) IN ('maryland','md') THEN 'MD'
         WHEN TRIM(LOWER(state)) IN ('massachusetts','ma') THEN 'MA'
         WHEN TRIM(LOWER(state)) IN ('michigan','mi') THEN 'MI'
         WHEN TRIM(LOWER(state)) IN ('minnesota','mn') THEN 'MN'
         WHEN TRIM(LOWER(state)) IN ('mississippi','ms') THEN 'MS'
         WHEN TRIM(LOWER(state)) IN ('missouri','mo') THEN 'MO'
         WHEN TRIM(LOWER(state)) IN ('montana','mt') THEN 'MT'
         WHEN TRIM(LOWER(state)) IN ('nebraska','ne') THEN 'NE'
         WHEN TRIM(LOWER(state)) IN ('nevada','nv') THEN 'NV'
         WHEN TRIM(LOWER(state)) IN ('new hampshire','nh') THEN 'NH'
         WHEN TRIM(LOWER(state)) IN ('new jersey','nj') THEN 'NJ'
         WHEN TRIM(LOWER(state)) IN ('new mexico','nm') THEN 'NM'
         WHEN TRIM(LOWER(state)) IN ('new york','ny') THEN 'NY'
         WHEN TRIM(LOWER(state)) IN ('north carolina','nc') THEN 'NC'
         WHEN TRIM(LOWER(state)) IN ('north dakota','nd') THEN 'ND'
         WHEN TRIM(LOWER(state)) IN ('ohio','oh') THEN 'OH'
         WHEN TRIM(LOWER(state)) IN ('oklahoma','ok') THEN 'OK'
         WHEN TRIM(LOWER(state)) IN ('oregon','or') THEN 'OR'
         WHEN TRIM(LOWER(state)) IN ('pennsylvania','pa') THEN 'PA'
         WHEN TRIM(LOWER(state)) IN ('rhode island','ri') THEN 'RI'
         WHEN TRIM(LOWER(state)) IN ('south carolina', 'sc') THEN 'SC'
         WHEN TRIM(LOWER(state)) IN ('south dakota', 'sd') THEN 'SD'
         WHEN TRIM(LOWER(state)) IN ('tennessee', 'tn') THEN 'TN'
         WHEN TRIM(LOWER(state)) IN ('texas', 'tx') THEN 'TX'
         WHEN TRIM(LOWER(state)) IN ('utah', 'ut') THEN 'UT'
         WHEN TRIM(LOWER(state)) IN ('vermont', 'vt') THEN 'VT'
         WHEN TRIM(LOWER(state)) IN ('virginia', 'va') THEN 'VA'
         WHEN TRIM(LOWER(state)) IN ('washington', 'wa') THEN 'WA'
         WHEN TRIM(LOWER(state)) IN ('west virginia', 'wv') THEN 'WV'
         WHEN TRIM(LOWER(state)) IN ('wisconsin', 'wi') THEN 'WI'
         WHEN TRIM(LOWER(state)) IN ('wyoming', 'wy') THEN 'WY'
         WHEN TRIM(LOWER(state)) IN ('american samoa', 'as') THEN 'AS'
         WHEN TRIM(LOWER(state)) IN ('guam', 'gu') THEN 'GU'
         WHEN TRIM(LOWER(state)) IN ('northern mariana islands', 'mp') THEN 'MP'
         WHEN TRIM(LOWER(state)) IN ('puerto rico', 'pr') THEN 'PR'
         WHEN TRIM(LOWER(state)) IN ('us virgin islands', 'vi') THEN 'VI'
         WHEN TRIM(LOWER(state)) IN ('us minor outlying islands', 'um') THEN 'UM'
         WHEN TRIM(LOWER(state)) IN ('marshall islands', 'mh') THEN 'MH'
         WHEN TRIM(LOWER(state)) IN ('micronesia', 'fm') THEN 'FM'
         WHEN TRIM(LOWER(state)) IN ('palau', 'pw') THEN 'PW'
         WHEN TRIM(LOWER(state)) IN ('us armed forces americas', 'aa') THEN 'AA'
         WHEN TRIM(LOWER(state)) IN ('us armed forces europe', 'ae') THEN 'AE'
         WHEN TRIM(LOWER(state)) IN ('us armed forces pacific', 'ap') THEN 'AP'
         WHEN TRIM(LOWER(state)) IN ('alberta', 'ab') THEN 'AB'
         WHEN TRIM(LOWER(state)) IN ('british columbia', 'bc') THEN 'BC'
         WHEN TRIM(LOWER(state)) IN ('manitoba', 'mb') THEN 'MB'
         WHEN TRIM(LOWER(state)) IN ('new brunswick', 'nb') THEN 'NB'
         WHEN TRIM(LOWER(state)) IN ('newfoundland AND labrador', 'nl') THEN 'NL'
         WHEN TRIM(LOWER(state)) IN ('nova scotia', 'ns') THEN 'NS'
         WHEN TRIM(LOWER(state)) IN ('ontario', 'on') THEN 'ON'
         WHEN TRIM(LOWER(state)) IN ('prince edward island', 'pe') THEN 'PE'
         WHEN TRIM(LOWER(state)) IN ('quebec', 'qc') THEN 'QC'
         WHEN TRIM(LOWER(state)) IN ('saskatchewan', 'sk') THEN 'SK'
         WHEN TRIM(LOWER(state)) IN ('northwest territories','nt') THEN 'NT'
         WHEN TRIM(LOWER(state)) IN ('nunavut','nu') THEN 'NU'
         WHEN TRIM(LOWER(state)) IN ('yukon','yt') THEN 'YT'
         ELSE UPPER(state)
       END AS state
       ,postal AS zip
       ,CASE
         WHEN LOWER(country) IN ('united states','usa') THEN 'us'
         ELSE LOWER(country)
       END AS country
       ,birthdate
       ,CASE
         WHEN LOWER(gender) IN ('female','woman','w') THEN 'f'
         WHEN LOWER(gender) IN ('male','man') THEN 'm'
         WHEN LOWER(gender) IN ('unknown','undefined','u','null') THEN null
         ELSE LOWER(gender)
       END AS gender
       ,MAX(update_dt) AS update_dt
       ,MAX(pk) AS pk
     FROM Unified_Coalesced  
     GROUP BY amperity_id
       ,given_name
       ,surname
       ,address
       ,address_line_2
       ,city
       ,state
       ,zip
       ,country
       ,birthdate
       ,gender
   )

   ,address_and_details AS (
     SELECT DISTINCT
       amperity_id
       ,given_name
       ,surname
       ,address
       ,address_line_2
       ,city
       ,state
       ,zip
       ,country
       ,birthdate
       ,gender
     FROM (
       SELECT
         amperity_id
         ,given_name
         ,surname
         ,address
         ,address_line_2
         ,city
         ,state
         ,zip
         ,country
         ,birthdate
         ,gender
         ,ROW_NUMBER() OVER (
           PARTITION BY amperity_id
           ORDER BY (
             INT(ISNOTNULL(address)) +
             INT(ISNOTNULL(given_name)) +
             INT(ISNOTNULL(surname)) +
             INT(ISNOTNULL(zip))
           ) DESC
           ,update_dt DESC
           ,pk
         ) AS update_rank
       FROM address_and_details_prep
       WHERE COALESCE (
         given_name
         ,surname
         ,address
         ,address_line_2
         ,city
         ,state
         ,zip
         ,country
         ,birthdate
         ,gender
       ) IS NOT NULL
     )
     WHERE update_rank <= (
       SELECT limit FROM pii_row_limit
     )
   )

   ,cleaned_emails AS (
       SELECT
       DISTINCT
       amperity_id
       ,email
     FROM (
       SELECT
         amperity_id
         ,EXPLODE(SPLIT(LOWER(email), ',')) AS email
         ,update_dt
         ,pk
         ,ROW_NUMBER() OVER (
           PARTITION BY amperity_id
           ORDER BY update_dt DESC
           ,pk
         ) AS update_rank
       FROM Unified_Coalesced
       WHERE email IS NOT NULL
     )
     WHERE update_rank <= (
       SELECT limit FROM pii_row_limit
     )
   )

   ,cleaned_phones AS (
     SELECT DISTINCT
       amperity_id
       ,phone
     FROM (
       SELECT
         amperity_id
         ,EXPLODE(SPLIT(REGEXP_REPLACE(phone, '[-.()]', ''), ',')) AS phone
         ,update_dt
         ,pk
         ,ROW_NUMBER() OVER (
           PARTITION BY amperity_id
           ORDER BY update_dt DESC
           ,pk
         ) AS update_rank
       FROM Unified_Coalesced
       WHERE phone IS NOT NULL
     )
     WHERE update_rank <= (
       SELECT limit FROM pii_row_limit
     )
   )

   SELECT
     aa.amperity_id
     ,ad.given_name
     ,ad.surname
     ,TRIM(ce.email) AS email
     ,TRIM(cp.phone) AS phone
     ,ad.address
     ,ad.address_line_2
     ,ad.city
     ,ad.state
     ,ad.zip
     ,ad.country
     ,ad.birthdate
     ,ad.gender
   FROM all_ampids aa
   LEFT JOIN address_and_details ad ON aa.amperity_id = ad.amperity_id
   LEFT JOIN cleaned_emails ce ON aa.amperity_id=ce.amperity_id
   LEFT JOIN cleaned_phones cp ON aa.amperity_id=cp.amperity_id
     WHERE (
       ISNOTNULL(ad.address)
       AND ISNOTNULL(ad.zip)
     )
   OR ISNOTNULL(COALESCE(ce.email,cp.phone))

.. table-unified-paid-media-sql-query-recommended-end


.. _table-paid-media-sql-query-optional-updates:

Optional updates
==================================================

.. unified-paid-media-sql-query-optional-updates-start

The **Unified Paid Media** does not require customization, but you may make the following updates:

* :ref:`Configure the row limit <table-unified-paid-media-sql-query-optional-configure-row-limit>`
* :ref:`State, province, and territory codes <table-unified-paid-media-sql-query-optional-configure-codes>`

.. unified-paid-media-sql-query-optional-updates-end


.. _table-unified-paid-media-sql-query-optional-configure-row-limit:

Configure the row limit
--------------------------------------------------

.. table-unified-paid-media-sql-query-optional-configure-row-limit-start

The **Unified Paid Media** table is configured by default to include a ranked list of up to 10 phone numbers, email addresses, and address details for each unique Amperity ID.

.. important:: Amperity IDs are duplicated in the **Unified Paid Media** table, but are limited by the configured row limit.

You can configure the row limit by changing a value in the **pii_row_limit** common table expression at the start of the query. For example, a value of "3" will include the top 3 ranked phone numbers, email addresses, and physical addresses for each unique Amperity ID:

.. code-block:: sql
   :linenos:
   :emphasize-lines: 2

   WITH pii_row_limit AS (
     SELECT 3 AS limit
   )

.. table-unified-paid-media-sql-query-optional-configure-row-limit-end

.. table-unified-paid-media-sql-query-optional-configure-row-limit-admonition-start

.. admonition:: How many rows are defined by the row limit?

   If the limit is set to 10, and there are 10 rows each for email addresses, phone numbers, and address details, there will be "10 times 10 times 10" combinations of rows, or 1000 rows in the **Unified Paid Media** table.

   If the limit is set to 5, and there are 5 rows each, there will be "5 times 5 times 5" combinations of rows, or 125 rows.

   If the limit is set to 3, and there are 3 rows each, there will be "3 times 3 times 3" combinations of rows, or 27 rows.

   Adjust the row limit to control the size of the **Unified Paid Media** table, as required to support your brand's goals for match rates and customer matches in downstream marketing applications.

   When an audiences is sent to a destination and that audience uses the **Unified Paid Media** table, only the fields that are supported by the downstream marketing application is sent. For example, if a downstream marketing tool only requires email addresses, a row limit of 10 sends up to 10 email addresses *for each Amperity ID* that matched the audience that was built in Amperity.

.. table-unified-paid-media-sql-query-optional-configure-row-limit-admonition-end


.. _table-unified-paid-media-sql-query-optional-configure-codes:

State, province, and territory codes
--------------------------------------------------

.. table-unified-paid-media-sql-query-optional-configure-codes-start

Amperity uses a **CASE** statement ot define standardized state and province codes for states and territories within the United States and provinces and territories within Canada.

The default **CASE** statement located in the **address_and_details_prep** common table expression standardizes states, provinces, and territories into two digit codes:

.. code-block:: sql
   :linenos:

   ,CASE
     WHEN TRIM(LOWER(state)) IN ('alabama','al') THEN 'AL'
     WHEN TRIM(LOWER(state)) IN ('alaska','ak') THEN 'AK'
     [... 72 rows ...]
     WHEN TRIM(LOWER(state)) IN ('nunavut','nu') THEN 'NU'
     WHEN TRIM(LOWER(state)) IN ('yukon','yt') THEN 'YT'
     ELSE UPPER(state)
   END AS state

You may update the codes within the **CASE** statement located in the **address_and_details_prep** common table expression to align to the codes your brand uses or you may use a separate mapping file that is joined to this table.

.. table-unified-paid-media-sql-query-optional-configure-codes-end


.. _table-unified-paid-media-reference:

Column reference
==================================================

.. table-unified-paid-media-reference-start

The **Unified Paid Media** table only contains field associated with customer profile semantic tags (names, physical addresses, phone numbers, email addresses, birthdates, and gender) along with the Amperity ID.

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Column name
     - Data type
     - Description

   * - **Amperity ID**
     - String
     - The unique identifier that is assigned to clusters of customer records that all represent the same individual. Each row in this table is associated with an Amperity ID. Rows in this table are not unique by Amperity ID.

   * - **Address**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address-start
          :end-before: .. term-address-end

   * - **Address Line 2**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address2-start
          :end-before: .. term-address2-end

   * - **Birthdate**
     - Date
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-birthdate-start
          :end-before: .. term-birthdate-end

   * - **City**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-city-start
          :end-before: .. term-city-end

   * - **Country**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-country-start
          :end-before: .. term-country-end

   * - **Email**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

   * - **Gender**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-gender-start
          :end-before: .. term-gender-end

   * - **Given Name**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end

   * - **Phone**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

   * - **Zip**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end

   * - **State**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end

   * - **Surname**
     - String
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end

.. table-unified-paid-media-reference-end
