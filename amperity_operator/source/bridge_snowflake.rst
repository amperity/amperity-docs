.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Snowflake


.. meta::
    :description lang=en:
        Amperity Bridge for Snowflake is a first-class integration that uses secure data sharing to enable bi-directional data access between Amperity and Snowflake.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity Bridge for Snowflake is a first-class integration that uses secure data sharing to enable bi-directional data access between Amperity and Snowflake.

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect Amperity Bridge to Snowflake

==================================================
Connect Amperity Bridge to Snowflake
==================================================

.. bridge-snowflake-about-start

Amperity Bridge for Snowflake is a first-class integration that uses secure data sharing to enable bi-directional data access between Amperity and Snowflake without copying data or scheduling ETL workloads.

.. bridge-snowflake-about-end

.. bridge-snowflake-what-is-data-sharing-start

.. admonition:: What is Secure Data Sharing?

   `Secure Data Sharing <https://docs.snowflake.com/en/user-guide/data-sharing-intro>`__ |ext_link| enables data sharing between Snowflake accounts without copying or transferring data and instead relies on the services layer and metadata store within Snowflake. Your brand controls what data will be made available to Amperity directly from within your brand's Snowflake account.

.. bridge-snowflake-what-is-data-sharing-end

.. bridge-snowflake-switch-to-bridge-start

.. tip:: Amperity Bridge for Snowflake shares data directly with Snowflake. A bridge does not require a courier or a database export to be configured. A bridge can be configured to run automatically as part of any scheduled workflow.

   If your brand is using BI Connect to make data available in Snowflake your brand should consider moving the BI Connect workflow to Amperity Bridge. This increases the speed at which This allows your brand to self-service the data that is shared between Amperity and Snowflake directly from within your Snowflake account.

.. bridge-snowflake-switch-to-bridge-end


.. _bridge-snowflake-data-types:

Data types
==================================================

.. bridge-databricks-data-types-start

Most `Snowflake data types <https://docs.snowflake.com/en/sql-reference/intro-summary-data-types>`__ |ext_link| are supported by Amperity Bridge.

.. include:: ../../amperity_reference/source/bridge.rst
   :start-after: .. bridge-howto-sync-datatypes-start
   :end-before: .. bridge-howto-sync-datatypes-end

.. warning:: Complex types--arrays, objects, and maps--must have defined schemas.

The following table describes how Snowflake data types map to Amperity data types.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Snowflake data type
     - Amperity data type

   * - `ARRAY <https://docs.snowflake.com/en/sql-reference/data-types-structured#specifying-a-structured-array-type>`__ |ext_link|

       A sequence of elements with the type of ``element_type``. Each element must have a data type that maps to a supported Amperity data type.

       .. warning:: A semi-structured **ARRAY** data type is unsupported.

          Use `data type coversion <https://docs.snowflake.com/en/sql-reference/data-type-conversion>`__ |ext_link| to cast or coerce data in a semi-structured **ARRAY** into fully structured data before sharing it with Amperity Bridge.

     - **Array**

       An ordered list of zero or more elements of non-array values by field name and value.

       Fields within an **Array** must contain values for data types supported by Amperity.

       .. note:: Only fully structured **ARRAY** data types are supported.


   * - `BINARY <https://docs.snowflake.com/en/sql-reference/data-types-text#binary>`__ |ext_link|

       Synonymous with `VARBINARY <https://docs.snowflake.com/en/sql-reference/data-types-text#varbinary>`__ |ext_link|.

     - .. warning:: The Snowflake **BINARY** data type is unsupported. Exclude fields with **BINARY** data types from tables before sharing them with Amperity.


   * - `BOOLEAN <https://docs.snowflake.com/en/sql-reference/data-types-logical#boolean>`__ |ext_link|

       A value that can be **TRUE**, **FALSE**, or **NULL**.

     - **Boolean**

       A value that can be **TRUE**, **FALSE**, or **NULL**.


   * - `CHAR and CHARACTER <https://docs.snowflake.com/en/sql-reference/data-types-text#char-character-nchar>`__ |ext_link|

       Synonymous with **VARCHAR**, except the default length is **VARCHAR(1)**.

     - **String**

       A string of characters.


   * - `DATE <https://docs.snowflake.com/en/sql-reference/data-types-datetime#label-datatypes-date>`__ |ext_link|

       Date values with no time element.

     - **Date**

       An ISO-8601 compliant date value, such as a birthdate. For example:

       * 2021-11-04


   * - `DATETIME <https://docs.snowflake.com/en/sql-reference/data-types-datetime#datetime>`__ |ext_link|

       An alias for **TIMESTAMP_NTZ**.

     - See **TIMESTAMP**.


   * - `FILE <https://docs.snowflake.com/en/sql-reference/data-types-unstructured#file-data-type>`__ |ext_link|

       A reference to a file in an internal or external stage.

     - .. warning:: The Snowflake **FILE** data type is unsupported. Exclude fields with **FILE** data types from tables before sharing them with Amperity.


   * - `FLOAT <https://docs.snowflake.com/en/sql-reference/data-types-numeric#float-float4-float8>`__ |ext_link|

       A double-precision (64 bit) IEEE 754 floating-point number.

       .. note:: Synonymous with **DOUBLE**, **DOUBLE PRECISION**, **FLOAT**, **FLOAT4**, **FLOAT8**, and **REAL** data types.

     - **Float**

       A floating point number. For example:

       * 3.14
       * 3.14159


   * - `GEOGRAPHY <https://docs.snowflake.com/en/sql-reference/data-types-geospatial#label-data-types-geography>`__ |ext_link|

       A collection of points, linestrings, and polygons that represent a set or subset of the surface of the Earth.

     - .. warning:: The Snowflake **GEOGRAPHY** data type is unsupported. Exclude fields with **GEOGRAPHY** data types from tables before sharing them with Amperity.


   * - `GEOMETRY <https://docs.snowflake.com/en/sql-reference/data-types-geospatial#label-data-types-geometry>`__ |ext_link|

       A pairs of real numbers that represent features in a planar--Euclidean and Cartesian--coordinate system.

     - .. warning:: The Snowflake **GEOMETRY** data type is unsupported. Exclude fields with **GEOMETRY** data types from tables before sharing them with Amperity.


   * - `MAP <https://docs.snowflake.com/en/sql-reference/data-types-structured#label-structured-types-specifying-map>`__ |ext_link|

       A set of key-value pairs. Each pair must have a data type that maps to a supported Amperity data type.

       .. warning:: A **MAP** can have value types for **ARRAY** or **OBJECT**.

          Use `data type coversion <https://docs.snowflake.com/en/sql-reference/data-type-conversion>`__ |ext_link| to cast or coerce **ARRAY** and **OBJECT** value types within a **MAP** data type into fully structured data before sharing it with Amperity Bridge.


     - **Map**

       A set of key-value pairs that map to supported Amperity data types.

       .. note:: Only **MAP** data types with fully structured value types are supported.


   * - `NUMBER <https://docs.snowflake.com/en/sql-reference/data-types-numeric#number>`__ |ext_link|

       A number with up to 38 digits without precision and scale.

       .. note:: Synonymous with **BIGINT**, **BYTEINT**, **INT**, **INTEGER**, **SMALLINT**, and **TINYINT**.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `NUMBER (p,s) <https://docs.snowflake.com/en/sql-reference/data-types-numeric#number>`__ |ext_link|

       A number with up to 38 digits and precision and scale. Default precision and scale is (38,0).

       .. note:: Synonymous with **DECIMAL** and **NUMERIC** data types.

     - **Decimal (p,s)**

       A fixed point number, such as for prices or message sizes. The number of characters in the decimal value is configurable. For example:

       * 1.50 (prices)
       * 1874.380 (message sizes)
       * 141.48042 (order subtotals)


   * - `OBJECT <https://docs.snowflake.com/en/sql-reference/data-types-structured#label-structured-types-specifying-object>`__ |ext_link|

       A container of ordered fields. Fields within an **OBJECT** must contain values for data types supported by Amperity.

       .. warning:: A semi-structured **OBJECT** data type is unsupported.

          Use `data type coversion <https://docs.snowflake.com/en/sql-reference/data-type-conversion>`__ |ext_link| to cast or coerce data in a semi-structured **OBJECT** into fully structured data before sharing it with Amperity Bridge.

     - **Struct**

       A container of ordered fields by name and type.

       .. note:: Only fully structured **OBJECT** data types are supported.


   * - `Semi-structured data types <https://docs.snowflake.com/en/sql-reference/data-types-semistructured>`__ |ext_link|

       Snowflake allows **ARRAY**, **OBJECT**, and **VARIANT** data types to be semi-structured.

     - .. warning:: Semi-structured data types are unsupported.

          Use `data type coversion <https://docs.snowflake.com/en/sql-reference/data-type-conversion>`__ |ext_link| to cast or coerce into fully structured data before sending data to Amperity Bridge.


   * - `TIME <https://docs.snowflake.com/en/sql-reference/data-types-datetime#time>`__ |ext_link|

       Time data stored as ``HH:MI:SS`` with optional precision. Default precision is 9.

     - **String**

       A string of characters that represents ``HH:MI:SS`` time data with optional precision.


   * - `TIMESTAMP <https://docs.snowflake.com/en/sql-reference/data-types-datetime#label-datatypes-timestamp-variations>`__ |ext_link|

       A timestamp, including UTC time, UTC time with an offset, or a time with a specified precision.

       .. note:: Synonymous with **TIMESTAMP_LTZ**, **TIMESTAMP_NTZ**, and **TIMESTAMP_TZ**.

     - **Datetime**

       ISO-8601 compliant date and time values, such as a purchase or transaction, the time at which data was last updated, or a campaign launch date. For example:

       * Mon Nov 30 2020 16:00:00 GMT-0800 (Pacific Standard Time)
       * Sat Sep 02 2017 14:36:19 GMT-0700 (Pacific Daylight Time)


   * - `VARCHAR <https://docs.snowflake.com/en/sql-reference/data-types-text#varchar>`__ |ext_link|

       A string of Unicode UTF-8 characters. Default length is 16777216 bytes. Maximum length is 134217728 bytes.

       .. note:: Synonymous with `STRING and TEXT <https://docs.snowflake.com/en/sql-reference/data-types-text#string-text-nvarchar-nvarchar2-char-varying-nchar-varying>`__ |ext_link|.

     - **String**

       A sequence of characters, such as first and last names, email addresses, physical addresses, UUIDs and other IDs, phone numbers, zip codes, product names, and descriptions. May be empty. For example:

       * John
       * Smith
       * John Smith
       * johnsmith @ domain.com
       * 123 Main Street
       * 206-555-1111
       * 00002ac0-0915-3cb4-b7c7-5ee192b3bd49
       * ACME
       * pants
       * 
       * "A data source that pulls from an Amazon S3 bucket."


   * - `VARIANT <https://docs.snowflake.com/en/sql-reference/data-types-semistructured#variant>`__ |ext_link|

       A **VARIANT** value stores values of any type, including **OBJECT** and **ARRAY**, and is an unsupported `semi-structured data type <https://docs.snowflake.com/en/sql-reference/data-types-semistructured>`__ |ext_link|.

     - .. warning:: The Snowflake **VARIANT** data type is unsupported. Exclude fields with **VARIANT** data types from tables before sharing them with Amperity.


   * - `VECTOR <https://docs.snowflake.com/en/sql-reference/data-types-vector>`__ |ext_link|

       A data type for encoding and processing vectors.

     - .. warning:: The Snowflake **VECTOR** data type is unsupported. Exclude fields with **VECTOR** data types from tables before sharing them with Amperity.

.. bridge-databricks-data-types-end


.. _bridge-snowflake-sync-with-amperity:

From Snowflake
==================================================

.. bridge-snowflake-sync-amperity-start

A connection between Snowflake to Amperity requires configuration steps to be made in both Amperity and Snowflake.

.. bridge-snowflake-sync-amperity-end

.. bridge-snowflake-sync-amperity-links-start

#. :ref:`Get details <bridge-snowflake-sync-amperity-get-details>`
#. :ref:`Configure Snowflake <bridge-snowflake-sync-amperity-configure-snowflake>`
#. :ref:`Add inbound bridge <bridge-snowflake-sync-amperity-add-bridge>`

.. bridge-snowflake-sync-amperity-links-end


.. _bridge-snowflake-sync-amperity-get-details:

Get details
--------------------------------------------------

.. bridge-snowflake-sync-amperity-get-details-start

Before you can create inbound sharing between Snowflake and Amperity you need to collect the following information.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: center
          :class: no-scaled-link
     - The organization name and account name for your brand's |destination-name| account.

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-organization-start
          :end-before: .. credential-snowflake-organization-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-account-name-start
          :end-before: .. credential-snowflake-account-name-end

       .. tip:: To `find your organization name and account name <https://docs.snowflake.com/en/user-guide/admin-account-identifier#finding-the-organization-and-account-name-for-an-account>`__ |ext_link| use **Snowsight**.

          Open the account selector and browse to the account for which Amperity Bridge will be configured. Hover over the account name to view additional details, and then copy the account identifier.

          The copied identifier contains both organization and account name in the format `organization-name.account-name`.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-region-start
          :end-before: .. credential-snowflake-region-end


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: center
          :class: no-scaled-link
     - Before you can configure Amperity Bridge for data sharing with Snowflake you must :ref:`create a share in Snowflake <bridge-snowflake-sync-amperity-configure-snowflake-create-share>`, add a secure share identifier to that share, identify the correct account locator, and then add the :ref:`Amperity account locator ID <bridge-snowflake-sync-amperity-configure-snowflake-account-locator>` to the share.

       Use the `CURRENT_ACCOUNT <https://docs.snowflake.com/en/sql-reference/functions/current_account>`__ |ext_link| argument in |destination-name| to return the locator ID for your Snowflake account.

       .. important:: Secure data sharing should :ref:`only share secure views <bridge-snowflake-sync-amperity-configure-snowflake-secure-views>` with Amperity.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: center
          :class: no-scaled-link
     - A secure share identifier in Snowflake is a unique string--A-Z, 0-9, $, and _ (underscores)--that is added when creating a share. This string must configured in Amperity to enable the bridge.

       Copy the secure share identifier from the Snowflake user interface, and then share the identifier with the individual who will configure Amperity for secure data sharing with Snowflake.

.. bridge-snowflake-sync-amperity-get-details-end


.. _bridge-snowflake-sync-amperity-configure-snowflake:

Configure Snowflake
--------------------------------------------------

.. bridge-snowflake-sync-amperity-configure-snowflake-start

Before you can configure Amperity Bridge for data sharing with Snowflake you must create a share in Snowflake, add a secure share identifier to that share, and then identify the correct account locator.

.. bridge-snowflake-sync-amperity-configure-snowflake-end


.. _bridge-snowflake-sync-amperity-configure-snowflake-create-share:

Create share
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-snowflake-sync-amperity-configure-snowflake-create-share-start

To enable data sharing between Snowflake and Amperity `a share must be created in Snowflake <https://docs.snowflake.com/en/user-guide/data-sharing-provider#using-snowsight-to-create-a-share>`__ |ext_link|. You may `use Snowsight, the Snowflake user interace, to create the share <https://docs.snowflake.com/en/user-guide/data-sharing-provider#creating-a-share>`__ |ext_link|, as described here, or you may use Snowflake SQL, starting with the `CREATE SHARE <https://docs.snowflake.com/en/sql-reference/sql/create-share>`__ |ext_link| command.

.. bridge-snowflake-sync-amperity-configure-snowflake-create-share-end

**To create a share in Snowflake**

.. bridge-snowflake-sync-amperity-configure-snowflake-create-share-steps-start

#. Log in to Snowsight.
#. Select **Data Products**, and then **Private Sharing**.
#. Select **Share**, and then **Create a Direct Share**.
#. For the share, select a source database, along with one or more target objects within the source database.
#. A **Secure Share Identifier** is required for data sharing with Amperity.

   A secure share identifier in Snowflake is a unique string--A-Z, 0-9, $, and _ (underscores)--that is added when creating a share. This string must be configured in Amperity to enable the bridge.

#. Find the :ref:`Amperity account locator ID <bridge-snowflake-sync-amperity-configure-snowflake-account-locator>`, and then add it to the configuration for the **Secure Share Identifier**.

#. Copy the secure share identifier from the Snowflake user interface, and then save the share.

#. Click **Add consumer**, and then configure the share to use the :ref:`Amperity account locator ID <bridge-snowflake-sync-amperity-configure-snowflake-account-locator>` as the consumer.

.. bridge-snowflake-sync-amperity-configure-snowflake-create-share-steps-end


.. _bridge-snowflake-sync-amperity-configure-snowflake-secure-views:

Configure secure views
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-snowflake-sync-amperity-configure-snowflake-secure-views-start

Secure data sharing should `only share secure views <https://docs.snowflake.com/en/user-guide/views-secure#creating-secure-views>`__ |ext_link| with Amperity. Amperity recommends that all views that are shared with Amperity be configured as secure views in Snowflake.

Alternatively, your brand may choose to configure Snowflake to `allow sharing of non-secure views <https://docs.snowflake.com/en/user-guide/data-sharing-views>`__ |ext_link| with Amperity.

.. bridge-snowflake-sync-amperity-configure-snowflake-secure-views-end


.. _bridge-snowflake-sync-amperity-configure-snowflake-account-locator:

Amperity account locator IDs
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-snowflake-sync-amperity-configure-snowflake-account-locator-start

Snowflake must be configured for the correct `account locator IDs <https://docs.snowflake.com/en/user-guide/admin-account-identifier#format-2-account-locator-in-a-region>`__ |ext_link| used by Amperity. Account locator IDs are specific to the stack in which your Amperity tenant is provisioned *and* the `region ID <https://docs.snowflake.com/en/user-guide/admin-account-identifier#region-ids>`__ |ext_link| in which your Snowflake account resides.

.. list-table::
   :widths: 33 33 34
   :header-rows: 1

   * - Amperity stack
     - Snowflake region
     - Account locator
   * - aws-prod
     - aws_us_west_2
     - GUB98973
   * - aws-prod
     - aws_us_east_1
     - MVB61607
   * - aws-prod
     - aws_us_east_2
     - BL95184
   * - aws-prod
     - azure_westus2
     - PZ39828
   * - aws-prod-cc1
     - aws_us_west_2
     - EXB14788
   * - aws-prod
     - gcp_us_east4
     - YU29648
   * - az-prod
     - azure_centralus
     - MC75461
   * - az-prod
     - azure_eastus2
     - DSA38111
   * - az-prod
     - aws_us_west_2
     - BCB42530
   * - az-prod-en1
     - aws_us_west_2
     - WKB77434
   * - az-prod
     - azure_westeurope
     - RN08588
   * - az-prod-en1
     - azure_australiaeast
     - TD45616
   * - az-prod
     - azure_australiaeast
     - MD18696

.. important:: If the account ID / region ID pair does not exist in your stack please contact Amperity Support.

.. bridge-snowflake-sync-amperity-configure-snowflake-account-locator-end


.. _bridge-snowflake-sync-amperity-add-bridge:

Add inbound bridge
--------------------------------------------------

Configure an inbound bridge to connect Snowflake with Amperity.

**To add an inbound bridge**

.. bridge-snowflake-sync-amperity-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - Open the **Sources** page. Under **Inbound shares** click **Add bridge**. 

       Choose **Snowflake**.

       .. image:: ../../images/bridge-inbound-choose-snowflake.png
          :width: 320 px
          :alt: Add a bridge for a connection.
          :align: left
          :class: no-scaled-link

       This opens the **Add bridge** dialog box. 

       .. image:: ../../images/bridge-inbound-name-description.png
          :width: 500 px
          :alt: Add a bridge for a connection.
          :align: left
          :class: no-scaled-link

       Add a name and description for the bridge *or* select an existing bridge, and then click **Confirm**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - Configure the organization, account name, and region.

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-organization-start
          :end-before: .. credential-snowflake-organization-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-account-name-start
          :end-before: .. credential-snowflake-account-name-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-region-start
          :end-before: .. credential-snowflake-region-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - Add the **Secure Share Identifier**.

       When finished, click **Continue**. This opens the **Select tables** dialog box.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - Use the **Select tables** dialog box to select any combination of schemas and tables to be connected to Amperity.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

       If you select a schema, all tables in that schema will be connected. Any new tables added later need to be manually added to the connection. 

       When finished, click **Next**. This opens the **Domain table mapping** dialog box.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - Map the tables that are connected from Snowflake to domain tables in Amperity.

       .. image:: ../../images/bridge-map-inbound-to-domain.png
          :width: 500 px
          :alt: Map connected tables to domain tables.
          :align: left
          :class: no-scaled-link

       Tables that are connected with Amperity are added as domain tables.

       * The names of connected tables must be unique among all domain tables.
       * Primary keys are not assigned.
       * Semantic tags are not applied.

       .. tip:: Use a custom domain table to assign primary keys, apply semantic tags, and shape data within connected tables to support any of your Amperity workflows.

       When finished, click **Save and sync**. This will start a workflow that synchronizes data from Snowflake to Amperity and creates the mapped domain table names.

       You can manually sync tables that are connected with Amperity using the **Sync** option from the **Actions** menu for the inbound bridge.

.. bridge-snowflake-sync-amperity-add-bridge-steps-end


.. _bridge-snowflake-sync-with-snowflake:

To Snowflake
==================================================

.. bridge-snowflake-sync-with-snowflake-start

A connection between Amperity and Snowflake requires configuration steps to be made in both Amperity and Snowflake.

.. bridge-snowflake-sync-with-snowflake-end

.. bridge-snowflake-sync-sandbox-start

.. note:: Configuration state for an outbound bridge **is not copied** from production to a sandbox. An outbound bridge must be configured within a sandbox.

.. bridge-snowflake-sync-sandbox-end

.. bridge-snowflake-sync-with-snowflake-links-start

#. :ref:`Get details <bridge-snowflake-sync-with-snowflake-prerequisites>`
#. :ref:`Add bridge <bridge-snowflake-sync-with-snowflake-add-bridge>`
#. :ref:`Select tables to share <bridge-snowflake-sync-with-snowflake-select-tables>`
#. :ref:`Configure Snowflake <bridge-snowflake-sync-with-snowflake-configure>`
#. :ref:`Verify table sharing <bridge-snowflake-sync-with-snowflake-verify-table-sharing>`

.. bridge-snowflake-sync-with-databricks-links-end


.. _bridge-snowflake-sync-with-snowflake-prerequisites:

Get details
--------------------------------------------------

.. bridge-snowflake-sync-with-snowflake-prerequisites-start

Before you can create outbound sharing between Snowflake and Amperity you need to collect the following information.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: center
          :class: no-scaled-link
     - The organization name and account name for your brand's |destination-name| account.

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-organization-start
          :end-before: .. credential-snowflake-organization-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-account-name-start
          :end-before: .. credential-snowflake-account-name-end

       .. tip:: To `find your organization name and account name <https://docs.snowflake.com/en/user-guide/admin-account-identifier#finding-the-organization-and-account-name-for-an-account>`__ |ext_link| use **Snowsight**.

          Open the account selector and browse to the account for which Amperity Bridge will be configured. Hover over the account name to view additional details, and then copy the account identifier.

          The copied identifier contains both organization and account name in the format `organization-name.account-name`.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-region-start
          :end-before: .. credential-snowflake-region-end


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: center
          :class: no-scaled-link
     - A user with the `ACCOUNTADMIN role <https://docs.snowflake.com/en/user-guide/security-access-privileges-shares>`__ |ext_link| must :ref:`create a database in Snowflake using the data that was shared from Amperity <bridge-snowflake-sync-with-snowflake-configure>`.

.. bridge-snowflake-sync-with-snowflake-prerequisites-end


.. _bridge-snowflake-sync-with-snowflake-add-bridge:

Add outbound bridge
--------------------------------------------------

.. bridge-snowflake-sync-with-snowflake-add-bridge-start

Configure an outbound bridge to connect with Snowflake.

.. bridge-snowflake-sync-with-snowflake-add-bridge-end

**To add an outbound bridge**

.. bridge-snowflake-sync-with-databricks-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - Open the **Destinations** page. Select the **Outbound shares** tab, and then click **Add bridge**. Choose Snowflake. This opens the **Create bridge** dialog box.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - Add a name and description for the bridge *or* select an existing bridge.

       Configure the organization, account name, and region.

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-organization-start
          :end-before: .. credential-snowflake-organization-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-account-name-start
          :end-before: .. credential-snowflake-account-name-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-snowflake-region-start
          :end-before: .. credential-snowflake-region-end

       Click **Next**, after which you will :ref:`select the tables to be shared with Snowflake <bridge-snowflake-sync-with-snowflake-select-tables>`.

.. bridge-snowflake-sync-with-databricks-add-bridge-steps-end


.. _bridge-snowflake-sync-with-snowflake-select-tables:

Select tables to share
--------------------------------------------------

.. bridge-snowflake-sync-with-snowflake-select-tables-start

You can configure Amperity to share any combination of schemas and tables that are available from the **Customer 360** page.

.. bridge-snowflake-sync-with-snowflake-select-tables-end

**To select schemas and tables to share**

.. bridge-snowflake-sync-with-snowflake-select-tables-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - After you have :ref:`configured the settings for the bridge <bridge-snowflake-sync-with-snowflake-add-bridge>`, click **Next** to open the **Select tables** dialog box.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - You may select any combination of schemas and tables.

       If you select a schema, all tables in that schema will be shared, including all changes made to all tables in that schema.

       When finished, click **Save**. :ref:`The next steps are done in Snowflake <bridge-snowflake-sync-with-snowflake-configure>`.

.. bridge-snowflake-sync-with-snowflake-select-tables-steps-end


.. _bridge-snowflake-sync-with-snowflake-configure:

Configure Snowflake
--------------------------------------------------

.. bridge-snowflake-sync-with-snowflake-configure-start

After tables have been shared you need to create a database in Snowflake using the data that was shared from Amperity.

.. bridge-snowflake-sync-with-snowflake-configure-end

**To create a database in Snowflake from shared data**

.. bridge-snowflake-sync-with-snowflake-configure-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - `Access the consumer listings that are available in your Snowflake account <https://docs.snowflake.com/en/user-guide/data-exchange-using#access-consumer-listings>`__ |ext_link|.

       From the **Snowsight** user interface in Snowflake, expand **Data Products**, then expand **Private Sharing**, and then find the direct share that was created for sharing Amperity data.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - `Switch the role to the ACCOUNTADMIN role <https://docs.snowflake.com/en/user-guide/security-access-privileges-shares>`__ |ext_link|.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - `Create the database in Snowflake from data that was shared from Amperity <https://docs.snowflake.com/en/user-guide/data-share-consumers#creating-a-database-from-a-share>`__ |ext_link|.

       Open the database, and then click the **Get Data** button. This opens the **Get Data** dialog box.

       Replace the value in the **Database name** field with the name of the database, and then choose the role, in addition to the **ACCOUNTADMIN** role, that have access to this database. Click **Get Data**.

       After the database is created click **View Database**.

.. bridge-snowflake-sync-with-snowflake-configure-steps-end


.. _bridge-snowflake-sync-with-snowflake-verify-table-sharing:

Verify table sharing
--------------------------------------------------

.. bridge-snowflake-sync-with-snowflake-verify-table-sharing-start

Verify that the tables shared from Amperity are available from a database in Snowflake.

.. bridge-snowflake-sync-with-snowflake-verify-table-sharing-end

**To verify that tables were shared from Amperity to Snowflake**

.. bridge-snowflake-sync-with-snowflake-verify-table-sharing-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - From the **Snowsight** user interface in Snowflake, expand **Data**, then expand **Databases**, and then find the database that was created for sharing Amperity data.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - Open the database, and then verify that the tables you shared from Amperity are available in the database.

.. bridge-snowflake-sync-with-snowflake-verify-table-sharing-steps-end
