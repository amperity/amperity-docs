.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Amazon Redshift


.. meta::
    :description lang=en:
        testtesttest

.. meta::
    :content class=swiftype name=body data-type=text:
        testtesttest

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect Amperity Bridge to Amazon Redshift

==================================================
Connect Amperity Bridge to Amazon Redshift
==================================================

.. bridge-redshift-about-start

.. bridge-redshift-about-end


.. _bridge-redshift-data-types:

Data types
==================================================

.. bridge-redshift-data-types-start

Most `Amazon Redshift data types <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__ |ext_link| are supported by Amperity Bridge.

.. include:: ../../amperity_reference/source/bridge.rst
   :start-after: .. bridge-howto-sync-datatypes-start
   :end-before: .. bridge-howto-sync-datatypes-end

.. note:: **GEOGRAPHY**, **GEOMETRY**, **HLLSKETCH**, **INTERVAL**, and **VARBYTE** data types are unsupported.

The following table describes how Amazon Redshift data types map to Amperity data types.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Amazon Redshift data type
     - Amperity data type

   * - `BIGINT <https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_types201.html#r_Numeric_types201-integer-types>`__ |ext_link|

       A signed eight-byte integer.

       .. note:: Synonymous with **INT8**.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `BOOLEAN <https://docs.aws.amazon.com/redshift/latest/dg/r_Boolean_type.html>`__ |ext_link|

       A value that can be **TRUE**, **FALSE**, or **NULL**.

       .. note:: Synonymous with **BOOL**.

     - **Boolean**

       A value that can be **TRUE**, **FALSE**, or **NULL**.


   * - `CHAR <https://docs.aws.amazon.com/redshift/latest/dg/r_Character_types.html#r_Character_types-char-or-character>`__ |ext_link|

       A fixed-length character string that is padded with blanks. Default length is 1. Maximum length is 4096 bytes.

       .. note:: Synonymous with **BPCHAR**, **CHARACTER**, and **NCHAR**.

     - **String**

       A string of characters.


   * - `DATE <https://docs.aws.amazon.com/redshift/latest/dg/r_Datetime_types.html#r_Datetime_types-date>`__ |ext_link|

       Calendar date values with no time element.

     - **Date**

       An ISO-8601 compliant date value, such as a birthdate. For example:

       * 2021-11-04


   * - `DECIMAL (p,s) <https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_types201.html#r_Numeric_types201-decimal-or-numeric-type>`__ |ext_link|

       A number with a specified precision and scale. Precision is 1-38 and scale is the number of digits to the right of the decimal point. Default precision and scale is (18,0).

       .. note:: Synonymous with **NUMERIC**.

       .. important:: The precision and scale of the Amazon Redshift column are carried through to Amperity. A decimal column that does not report both a precision and a scale cannot be synced.

     - **Decimal (p,s)**

       A fixed point number, such as for prices or message sizes. The number of characters in the decimal value is configurable. For example:

       * 1.50 (prices)
       * 1874.380 (message sizes)
       * 141.48042 (order subtotals)


   * - `DOUBLE PRECISION <https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_types201.html#r_Numeric_types201-floating-point-types>`__ |ext_link|

       A double-precision (64 bit) floating-point number.

       .. note:: Synonymous with **DOUBLE**, **FLOAT**, and **FLOAT8**.

     - **Float**

       A floating point number. For example:

       * 3.14
       * 3.14159


   * - `GEOGRAPHY <https://docs.aws.amazon.com/redshift/latest/dg/geospatial-overview.html>`__ |ext_link|

       A collection of points, linestrings, and polygons that represent a set or subset of the surface of the Earth.

     - .. warning:: The Amazon Redshift **GEOGRAPHY** data type is unsupported. Exclude fields with **GEOGRAPHY** data types from tables before sharing them with Amperity.


   * - `GEOMETRY <https://docs.aws.amazon.com/redshift/latest/dg/geospatial-overview.html>`__ |ext_link|

       A pairs of real numbers that represent features in a planar--Euclidean and Cartesian--coordinate system.

     - .. warning:: The Amazon Redshift **GEOMETRY** data type is unsupported. Exclude fields with **GEOMETRY** data types from tables before sharing them with Amperity.


   * - `HLLSKETCH <https://docs.aws.amazon.com/redshift/latest/dg/r_HLLSKTECH_type.html>`__ |ext_link|

       A HyperLogLog sketch that is used to estimate the number of distinct values in a data set.

     - .. warning:: The Amazon Redshift **HLLSKETCH** data type is unsupported. Exclude fields with **HLLSKETCH** data types from tables before sharing them with Amperity.


   * - `INTEGER <https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_types201.html#r_Numeric_types201-integer-types>`__ |ext_link|

       A signed four-byte integer.

       .. note:: Synonymous with **INT** and **INT4**.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `INTERVAL <https://docs.aws.amazon.com/redshift/latest/dg/r_interval_data_types.html>`__ |ext_link|

       Intervals of time on a scale of years to months or days to seconds.

       .. note:: Includes **INTERVAL DAY TO SECOND** and **INTERVAL YEAR TO MONTH**.

     - .. warning:: The Amazon Redshift **INTERVAL** data type is unsupported. Exclude fields with **INTERVAL** data types from tables before sharing them with Amperity.


   * - `REAL <https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_types201.html#r_Numeric_types201-floating-point-types>`__ |ext_link|

       A single-precision (32 bit) floating-point number.

       .. note:: Synonymous with **FLOAT4**.

     - **Float**

       A floating point number. For example:

       * 3.14
       * 3.14159


   * - `SMALLINT <https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_types201.html#r_Numeric_types201-integer-types>`__ |ext_link|

       A signed two-byte integer ranging from -32,768 to 32,767.

       .. note:: Synonymous with **INT2**.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * -12345


   * - `SUPER <https://docs.aws.amazon.com/redshift/latest/dg/r_SUPER_type.html>`__ |ext_link|

       A **SUPER** value stores semi-structured data, including arrays, structures, and scalar values.

     - **String**

       A string of characters.

       .. note:: A **SUPER** value is schemaless--its shape may vary from row to row--and does not map to a nested Amperity data type. Use a view or a custom domain table to cast or coerce the fields within a **SUPER** value to supported Amperity data types.


   * - `TIME <https://docs.aws.amazon.com/redshift/latest/dg/r_Datetime_types.html#r_Datetime_types-time>`__ |ext_link|

       Time data stored as ``HH:MI:SS`` without a time zone.

       .. note:: Synonymous with **TIME WITHOUT TIME ZONE**.

     - **String**

       A string of characters that represents ``HH:MI:SS`` time data.


   * - `TIMESTAMP <https://docs.aws.amazon.com/redshift/latest/dg/r_Datetime_types.html#r_Datetime_types-timestamp>`__ |ext_link|

       Date and time values without a time zone.

       .. note:: Synonymous with **TIMESTAMP WITHOUT TIME ZONE**.

     - **Datetime**

       ISO-8601 compliant date and time values, such as a purchase or transaction, the time at which data was last updated, or a campaign launch date. For example:

       * Mon Nov 30 2020 16:00:00 GMT-0800 (Pacific Standard Time)
       * Sat Sep 02 2017 14:36:19 GMT-0700 (Pacific Daylight Time)


   * - `TIMESTAMPTZ <https://docs.aws.amazon.com/redshift/latest/dg/r_Datetime_types.html#r_Datetime_types-timestamptz>`__ |ext_link|

       Date and time values with a time zone.

       .. note:: Synonymous with **TIMESTAMP WITH TIME ZONE**.

       .. important:: The time zone offset is dropped when a **TIMESTAMPTZ** value is synced to Amperity.

     - **Datetime**

       ISO-8601 compliant date and time values, such as a purchase or transaction, the time at which data was last updated, or a campaign launch date. For example:

       * Mon Nov 30 2020 16:00:00 GMT-0800 (Pacific Standard Time)
       * Sat Sep 02 2017 14:36:19 GMT-0700 (Pacific Daylight Time)


   * - `TIMETZ <https://docs.aws.amazon.com/redshift/latest/dg/r_Datetime_types.html#r_Datetime_types-timetz>`__ |ext_link|

       Time data stored as ``HH:MI:SS`` with a time zone.

       .. note:: Synonymous with **TIME WITH TIME ZONE**.

     - **String**

       A string of characters that represents ``HH:MI:SS`` time data with a time zone offset.


   * - `VARBYTE <https://docs.aws.amazon.com/redshift/latest/dg/r_VARBYTE_type.html>`__ |ext_link|

       A variable-length binary value. Default length is 64000 bytes. Maximum length is 16777216 bytes.

       .. note:: Synonymous with **BINARY**, **BINARY VARYING**, and **VARBINARY**.

     - .. warning:: The Amazon Redshift **VARBYTE** data type is unsupported.

          Amperity Bridge reads a Redshift table by unloading it to Parquet, and Amazon Redshift can `only unload VARBYTE columns to text or CSV format <https://docs.aws.amazon.com/redshift/latest/dg/r_UNLOAD.html#unload-usage-varbyte>`__ |ext_link|.

          Use a view or a custom domain table to coerce a binary column to a supported Amperity data type before sharing it with Amperity Bridge. For example, use `FROM_VARBYTE <https://docs.aws.amazon.com/redshift/latest/dg/r_FROM_VARBYTE.html>`__ |ext_link| to return the column as a string:

          .. code-block:: sql

             SELECT
               customer_id
               ,first_name
               ,last_name
               ,FROM_VARBYTE(email_bytes, 'utf8') AS email
               ,FROM_VARBYTE(phone_bytes, 'utf8') AS phone
             FROM binary_table


   * - `VARCHAR <https://docs.aws.amazon.com/redshift/latest/dg/r_Character_types.html#r_Character_types-varchar-or-character-varying>`__ |ext_link|

       A variable-length character string. Default length is 256 bytes. Maximum length is 65535 bytes.

       .. note:: Synonymous with **CHARACTER VARYING**, **NVARCHAR**, and **TEXT**.

     - **String**

       A sequence of characters, such as first and last names, email addresses, physical addresses, UUIDs and other IDs, phone numbers, ZIP codes, product names, and descriptions. May be empty. For example:

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

.. bridge-redshift-data-types-end


.. _bridge-redshift-from-redshift:

From Amazon Redshift
==================================================

.. bridge-redshift-from-redshift-start

.. bridge-redshift-from-redshift-end


.. _bridge-redshift-to-redshift:

To Amazon Redshift
==================================================

.. bridge-redshift-to-redshift-start

.. bridge-redshift-to-redshift-end
