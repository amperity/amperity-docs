.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Amazon Redshift


.. meta::
    :description lang=en:
        Amperity Bridge for Amazon Redshift uses an UNLOAD export pattern to bring approved Amazon Redshift tables and views into Amperity on a schedule.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity Bridge for Amazon Redshift uses an UNLOAD export pattern to bring approved Amazon Redshift tables and views into Amperity on a schedule.

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect Amperity Bridge to Amazon Redshift

==================================================
Connect Amperity Bridge to Amazon Redshift
==================================================

.. bridge-redshift-about-start

Amperity Bridge for |destination-name| lets you use approved |destination-name| tables and views as the data surface for the data that you send to Amperity. Your team defines the schemas, tables, and views that Amperity may access, and Amperity ingests from those approved objects on a schedule, without requiring you to build or maintain a separate file export or feed pipeline.

.. bridge-redshift-about-end

.. bridge-redshift-early-access-start

.. admonition:: Early access

   Amperity Bridge for |destination-name| is available as an inbound-only connection, offered to select customers as part of early access. Outbound support--writing data from Amperity to |destination-name|--is :ref:`not currently available <bridge-redshift-to-redshift>`. Contact your Amperity representative to learn more.

.. bridge-redshift-early-access-end

.. bridge-redshift-sync-behavior-start

.. important:: Amperity Bridge for |destination-name| performs full-table and full-view exports. Incremental synchronization is not currently supported.

   Review the :ref:`limitations <bridge-redshift-limitations>` before you configure a bridge.

.. bridge-redshift-sync-behavior-end


.. _bridge-redshift-how-it-works:

How it works
==================================================

.. bridge-redshift-how-it-works-start

Amperity Bridge for Databricks, Google BigQuery, and Snowflake connects through each platform's native data-sharing protocol. Amperity Bridge for |destination-name| is different. It uses an **UNLOAD** export pattern:

#. Amperity schedules and orchestrates the inbound bridge run.
#. Amperity uses an approved, role-based access path to run a query against your |destination-name| using the |destination-name| Data API.
#. |destination-name| unloads the result set of the configured table or view to the storage for your Amperity tenant.
#. Amperity ingests the exported files into your Amperity source and domain tables.

Because the compute for the export runs in your |destination-name|, you retain visibility into query history and workload impact, and you control what Amperity can query through standard |destination-name| grants.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Area
     - Behavior

   * - Query and export pattern
     - Amperity runs an **UNLOAD** statement from your |destination-name| to the storage for your Amperity tenant.

   * - Where compute runs
     - The query and the export run on your |destination-name| compute, which means that they appear in your query history and in your billing.

   * - Data surface
     - The bridge reads from the |destination-name| tables and views that you approve. You determine which objects are exposed to Amperity.

   * - Row and column selection
     - The bridge uses ``SELECT *`` against the configured table or view. To expose a subset of rows or columns, create a view and expose that view instead of the base table.

   * - Load behavior
     - Full load. Each run expects the configured object to represent the complete data set that Amperity should load. Incremental synchronization is not currently supported.

   * - Deployment models
     - Both provisioned clusters and Serverless workgroups are supported.

   * - Encryption
     - Exported objects use server-side encryption with AES256.

.. bridge-redshift-how-it-works-end


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

A connection between |destination-name| and Amperity brings tables from your |destination-name| account into Amperity as domain tables. It requires configuration steps to be made in both Amperity and |destination-name|.

Amperity accesses tables in your |destination-name| account using two IAM roles that you create. Amperity reaches your catalog through the first; your |destination-name| writes the exported data through the second.

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Role
     - Who assumes it
     - What it does

   * - Query role
     - Amperity
     - Reads your catalog--databases, schemas, and tables--and issues the **UNLOAD** statements that retrieve data.

   * - Unload role
     - |destination-name|, on your behalf
     - Chains into the Amperity storage role so that |destination-name| can write the exported data to the storage for your Amperity tenant.

.. bridge-redshift-from-redshift-end

.. bridge-redshift-from-redshift-links-start

#. :ref:`Get details <bridge-redshift-from-redshift-get-details>`
#. :ref:`Configure Amazon Redshift <bridge-redshift-from-redshift-configure-redshift>`
#. :ref:`Add inbound bridge <bridge-redshift-from-redshift-add-bridge>`

.. bridge-redshift-from-redshift-links-end


.. _bridge-redshift-from-redshift-get-details:

Get details
--------------------------------------------------

.. bridge-redshift-from-redshift-get-details-start

Before you configure the bridge, gather the following from your AWS and |destination-name| environment.

.. list-table::
   :widths: 25 40 35
   :header-rows: 1

   * - Category
     - Information needed
     - Why it matters

   * - AWS and |destination-name| environment
     - The AWS account ID; the cluster identifier or Serverless workgroup name; the database name; the region.
     - Identifies the source environment and confirms the region and connectivity requirements.

   * - Approved data objects
     - The schema names; the table and view names; any column exclusions, row filters, or masking that is applied by a view.
     - Defines exactly what data Amperity can access.

   * - Amazon S3 landing location
     - Whether you are using Bring Your Own Storage (BYOS) or storage that is managed by Amperity.
     - Determines where the **UNLOAD** output lands and who manages the access policy for that bucket.

   * - Schedule and volume
     - The expected export cadence; the approximate table sizes and row counts.
     - Supports performance planning and helps size your first sync.

   * - Operational owner
     - Who owns IAM, |destination-name| grants, and troubleshooting on your side.
     - Gives Amperity a contact for schema changes and incident triage.

.. bridge-redshift-from-redshift-get-details-end


.. _bridge-redshift-from-redshift-get-details-responsibilities:

Configuration responsibilities
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-get-details-responsibilities-start

Amperity Bridge for |destination-name| is self-service. Configuration is split between the values that Amperity provides and the resources that you create in your AWS account.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Amperity provides
     - Your team configures

   * - * The **Amperity query role**.
       * The **External ID**.
       * The **Amperity storage role**.

       See :ref:`Values from Amperity <bridge-redshift-from-redshift-get-details-values>`.

     - * The |destination-name| schemas, tables, and views that Amperity may access.
       * The :ref:`query role <bridge-redshift-from-redshift-configure-redshift-query-role>`.
       * The :ref:`unload role <bridge-redshift-from-redshift-configure-redshift-unload-role>`.
       * The :ref:`database permissions and grants <bridge-redshift-from-redshift-configure-redshift-grants>`.
       * The :ref:`database user <bridge-redshift-from-redshift-configure-redshift-db-user>`, for a provisioned cluster.

.. bridge-redshift-from-redshift-get-details-responsibilities-end


.. _bridge-redshift-from-redshift-get-details-values:

Values from Amperity
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-get-details-values-start

The values that you need to write the IAM policies are specific to your tenant. Amperity shows them at the start of the bridge flow.

Open the **Sources** page. Under **Inbound shares** click **Add bridge**, choose **Amazon Redshift**, choose **Create new bridge**, and then give the bridge a name.

The dialog box displays three copyable values.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Value
     - Use it for

   * - **Amperity query role**
     - The principal that your query role must trust.

   * - **External ID**
     - Your query role should allow only principals with this external ID to assume it.

   * - **Amperity storage role**
     - The role that your unload role is given permission to assume.

.. important:: Copy all three values before continuing.

.. bridge-redshift-from-redshift-get-details-values-end


.. _bridge-redshift-from-redshift-configure-redshift:

Configure Amazon Redshift
--------------------------------------------------

.. bridge-redshift-from-redshift-configure-redshift-start

To configure |destination-name| to connect with Amperity you need to create the query role and the unload role in the AWS account that owns your |destination-name|, attach the unload role to your cluster or workgroup, and then grant read access within |destination-name| to the identity that the queries run as. On a provisioned cluster you must also create the database user that the queries run as.

.. note:: IAM gets Amperity as far as the cluster. It grants no access to any data. Access to data is granted inside |destination-name|, as described in :ref:`Grant database access <bridge-redshift-from-redshift-configure-redshift-grants>`.

.. bridge-redshift-from-redshift-configure-redshift-end


.. _bridge-redshift-from-redshift-configure-redshift-db-user:

Create the database user (provisioned cluster only)
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-configure-redshift-db-user-start

This step applies only if you are using a provisioned cluster. On a provisioned cluster the queries run as a named |destination-name| database user. Amperity does not create it, so create it now. The name that you choose goes into the :ref:`permission policy for the query role <bridge-redshift-from-redshift-configure-redshift-query-role>` in the next step.

Connect to your cluster as a superuser through the **Query editor v2** in the |destination-name| console, and then run the following. Modify the name to what you want, but use all lowercase characters.

.. code-block:: sql

   CREATE USER amperity PASSWORD DISABLE;

.. note:: You can set a real password by replacing **DISABLE** with the password that you want. Nothing about the integration changes. Amperity is never given the password and never uses it.

   A password would only let someone log in as this user directly, which is not needed for the bridge, which is why Amperity recommends **DISABLE**.

.. bridge-redshift-from-redshift-configure-redshift-db-user-end


.. _bridge-redshift-from-redshift-configure-redshift-query-role:

Create the query role
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-configure-redshift-query-role-start

In the AWS account that owns your |destination-name|, create an IAM role whose name starts with "AmperityRedshiftBridge", such as "AmperityRedshiftBridgeQuery".

**Trust policy**

Substitute the **Amperity query role** and **External ID** that you copied from the :ref:`values that Amperity provides <bridge-redshift-from-redshift-get-details-values>`.

.. important:: Trust the query role ARN exactly as it is given, rather than the whole Amperity account.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AmperityQueryRoleAssume",
         "Effect": "Allow",
         "Principal": {
           "AWS": "<AMPERITY_QUERY_ROLE_ARN>"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "sts:ExternalId": "<AMPERITY_EXTERNAL_ID>"
           }
         }
       }
     ]
   }

**Permission policy: Redshift Serverless**

Attach this policy for a Serverless workgroup. Replace **<REGION>** with the region that your |destination-name| runs in and **<YOUR_ACCOUNT_ID>** with the 12-digit AWS account that owns it. **<WORKGROUP_UUID>** is the workgroup's UUID from its ARN, and not its name.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "Execute",
         "Effect": "Allow",
         "Action": [
           "redshift-data:ListDatabases",
           "redshift-data:ListTables",
           "redshift-data:DescribeTable",
           "redshift-data:ExecuteStatement",
           "redshift-serverless:GetCredentials"
         ],
         "Resource": "arn:aws:redshift-serverless:<REGION>:<YOUR_ACCOUNT_ID>:workgroup/<WORKGROUP_UUID>"
       },
       {
         "Sid": "ReadResult",
         "Effect": "Allow",
         "Action": [
           "redshift-data:DescribeStatement",
           "redshift-data:GetStatementResult"
         ],
         "Resource": "*"
       }
     ]
   }

**Permission policy: provisioned Redshift instance**

Attach this policy instead for a provisioned cluster. Replace **<REGION>** with the region that your |destination-name| runs in and **<YOUR_ACCOUNT_ID>** with the 12-digit AWS account that owns it. **<CLUSTER_IDENTIFIER>** is your cluster's identifier, **<DATABASE>** is the database that you connect through, and **<DB_USER>** is the :ref:`database user that you created <bridge-redshift-from-redshift-configure-redshift-db-user>`.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "ExecuteCluster",
         "Effect": "Allow",
         "Action": [
           "redshift-data:ListDatabases",
           "redshift-data:ListTables",
           "redshift-data:DescribeTable",
           "redshift-data:ExecuteStatement",
           "redshift:GetClusterCredentials"
         ],
         "Resource": [
           "arn:aws:redshift:<REGION>:<YOUR_ACCOUNT_ID>:cluster:<CLUSTER_IDENTIFIER>",
           "arn:aws:redshift:<REGION>:<YOUR_ACCOUNT_ID>:dbuser:<CLUSTER_IDENTIFIER>/<DB_USER>",
           "arn:aws:redshift:<REGION>:<YOUR_ACCOUNT_ID>:dbname:<CLUSTER_IDENTIFIER>/<DATABASE>"
         ]
       },
       {
         "Sid": "ReadResult",
         "Effect": "Allow",
         "Action": [
           "redshift-data:DescribeStatement",
           "redshift-data:GetStatementResult"
         ],
         "Resource": "*"
       }
     ]
   }

.. note:: **DescribeStatement** and **GetStatementResult** are keyed by statement ID rather than by a resource ARN, which is why AWS requires them on "*".

.. bridge-redshift-from-redshift-configure-redshift-query-role-end


.. _bridge-redshift-from-redshift-configure-redshift-unload-role:

Create the unload role
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-configure-redshift-unload-role-start

Create a second IAM role in the same AWS account. You can name this anything you like.

**Trust policy**

Attach this policy for this role. Replace **<YOUR_ACCOUNT_ID>** with the 12-digit AWS account that owns your |destination-name|, which is the same account that you are creating these roles in.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "RedshiftAssume",
         "Effect": "Allow",
         "Principal": {
           "Service": [
             "redshift-serverless.amazonaws.com",
             "redshift.amazonaws.com"
           ]
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "<YOUR_ACCOUNT_ID>"
           }
         }
       }
     ]
   }

**Permission policy**

Attach this policy for this role. Substitute the **Amperity storage role** that you copied from the :ref:`values that Amperity provides <bridge-redshift-from-redshift-get-details-values>`. This is the role's only permission. It holds no storage access of its own and reaches storage by chaining.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AssumeAmperityStorageRole",
         "Effect": "Allow",
         "Action": "sts:AssumeRole",
         "Resource": "<AMPERITY_STORAGE_ROLE_ARN>"
       }
     ]
   }

**Attach the role to your Amazon Redshift**

.. important:: This step is required. |destination-name| can only use IAM roles that are associated with it, so a correctly written role that is not attached still fails at **UNLOAD** time.

Associate the unload role using the |destination-name| console:

* For a provisioned cluster, open your cluster, and then from the **Actions** menu select **Manage IAM roles**.
* For a Serverless workgroup, open your namespace, and then under **Security and encryption** select **Manage IAM roles**.

.. bridge-redshift-from-redshift-configure-redshift-unload-role-end


.. _bridge-redshift-from-redshift-configure-redshift-grants:

Grant database access
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-configure-redshift-grants-start

IAM gets Amperity as far as the cluster. It grants no access to any data. That is granted inside |destination-name|, to the database identity that the queries run as.

**Which identity to grant to**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Deployment
     - Identity

   * - Provisioned cluster
     - The :ref:`database user that you created <bridge-redshift-from-redshift-configure-redshift-db-user>`, which is the same one that you enter as the **Database user** when you :ref:`add the inbound bridge <bridge-redshift-from-redshift-add-bridge>`.

   * - Serverless
     - |destination-name| derives the identity from the query role that Amperity assumes and names it "IAMR:<QUERY_ROLE_NAME>".

**Grant the reads**

The statements are the same for both deployments. Only the grantee differs. Run them as a superuser or as the owner of the objects, once per schema and once per table that you intend to sync.

On a provisioned cluster the grantee is simply your database user.

.. code-block:: sql

   GRANT USAGE ON SCHEMA <SCHEMA> TO <DB_USER>;
   GRANT SELECT ON <SCHEMA>.<TABLE_OR_VIEW> TO <DB_USER>;

On Serverless the identity name contains a colon, which is why |destination-name| requires it in double quotes.

.. code-block:: sql

   GRANT USAGE ON SCHEMA <SCHEMA> TO "IAMR:<QUERY_ROLE_NAME>";
   GRANT SELECT ON <SCHEMA>.<TABLE_OR_VIEW> TO "IAMR:<QUERY_ROLE_NAME>";

Grant only what you want Amperity to see. Amperity can read exactly what this identity can read, and nothing more. If you want Amperity to have access to only a subset of the columns on a particular table, consider creating a view that exposes only those columns, and granting **SELECT** on the view instead of the table.

.. important:: **External table access**

   If some of your |destination-name| tables are external tables rather than standard internal tables, be aware that permission management for external tables is less fine-grained. |destination-name| grants access to external tables, such as Amazon Redshift Spectrum or external schemas, at the schema level and not per table. This means that you will not be able to expose a single external table without granting access to the entire schema, which may be inconvenient.

   Workaround: create a view that selects only the intended external table, and then grant Amperity **SELECT** permission on the view instead, to keep exposure scoped.

**How much to grant**

Grant only the schemas and objects that you plan to sync. You do not have to open up every database on the cluster. Amperity lists the databases that this identity can read and skips the rest.

You can widen the grants later. New ones are picked up the next time that Amperity reads your catalog.

.. bridge-redshift-from-redshift-configure-redshift-grants-end


.. _bridge-redshift-from-redshift-add-bridge:

Add inbound bridge
--------------------------------------------------

.. bridge-redshift-from-redshift-add-bridge-start

Configure an inbound bridge to connect |destination-name| with Amperity.

.. bridge-redshift-from-redshift-add-bridge-end

**To add an inbound bridge**

.. bridge-redshift-from-redshift-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - In Amperity, go to **Sources** and add a new |destination-name| bridge.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Enter the Amperity Access Role ARN, your |destination-name| deployment details (cluster identifier or Serverless workgroup), database name, and region.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Test the connection. Amperity validates the role, external ID, and network path.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Discover the approved schemas, tables, and views, and select the objects that you want to bring into Amperity.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Map each selected object to an Amperity source or domain table.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - Save the bridge. Amperity schedules and runs the sync, and shows run status, runtime, and any errors on the bridge's detail page.

.. bridge-redshift-from-redshift-add-bridge-steps-end

.. bridge-redshift-from-redshift-add-bridge-after-start

Once saved, the bridge runs alongside any other bridges or couriers that you already use. You do not need to migrate everything to Amperity Bridge for |destination-name| at once.

.. tip:: Amperity recommends starting with one to three representative tables or views, including at least one higher-volume feed, to validate |destination-name| query runtime, **UNLOAD** duration, ingestion timing, and workload impact before expanding further.

.. bridge-redshift-from-redshift-add-bridge-after-end


.. _bridge-redshift-to-redshift:

To Amazon Redshift
==================================================

.. bridge-redshift-to-redshift-start

Coming soon.

An outbound bridge--writing data from Amperity to |destination-name|--is not currently available. Amperity Bridge for |destination-name| supports inbound data into Amperity only.

Contact your Amperity representative if outbound |destination-name| connectivity is required for your use case.

.. bridge-redshift-to-redshift-end


.. _bridge-redshift-limitations:

Limitations
==================================================

.. bridge-redshift-limitations-start

Amperity Bridge for |destination-name| has the following limitations.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Limitation
     - Details

   * - Full loads only
     - Each configured table or view must represent the complete data set that Amperity should load during that run. Delta-only and incremental synchronization are not currently supported.

   * - Schema changes require the bridge to be re-saved
     - If columns are added, removed, or renamed on a table or view that is used by the bridge, syncs may fail until the bridge is reopened and saved again.

       Row-level logic behind a view--such as filters, masking, or business logic--can be changed without affecting the bridge, as long as the exposed column schema stays the same.

   * - ``SELECT *`` semantics
     - The bridge reads the full result set of the configured object. To expose a subset of rows or columns, :ref:`create a view <bridge-redshift-from-redshift-configure-redshift-grants>` and point the bridge at that view.

   * - Your compute is used
     - The query and the **UNLOAD** statement run on your |destination-name| compute. Your team should monitor the workload and the associated |destination-name| costs.

   * - Cross-region transfer costs may apply
     - If your |destination-name| and the storage that is used by your Amperity tenant are in different AWS regions, AWS cross-region data transfer charges may apply.

   * - Outbound is not available
     - Amperity Bridge for |destination-name| supports :ref:`inbound data into Amperity only <bridge-redshift-to-redshift>`.

.. bridge-redshift-limitations-end


.. _bridge-redshift-faq:

Frequently asked questions
==================================================

.. bridge-redshift-faq-start

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Question
     - Answer

   * - Does the bridge support incremental loads?
     - No. The bridge performs full loads and expects the configured table or view to represent the complete data set that Amperity should load during each run.

   * - Can I change which rows are included without reconfiguring the bridge?
     - Yes. You can update the row filters or the business logic behind an approved view without re-registering the bridge, as long as the exposed column schema does not change.

   * - Can Amperity ingest directly from Amazon S3 instead of |destination-name|?
     - Direct Amazon S3 ingestion may be available for some architectures. Amperity Bridge for |destination-name| is designed for the case where you want Amperity to read directly from approved |destination-name| tables and views, and to have |destination-name| perform the export.

   * - Can I use this bridge alongside other bridges and ingestion methods?
     - Yes. You can use Amperity Bridge for |destination-name| for selected feeds and continue to use other bridges or file-based ingestion for others.

   * - Who pays for the |destination-name| compute?
     - The query and the **UNLOAD** statement run on your |destination-name| compute, which means that your team should monitor and budget for that workload.

   * - Does |destination-name| query history show what Amperity users query inside Amperity?
     - No. It shows the export query that the bridge generates, which is a ``SELECT *`` against the approved table or view as part of the **UNLOAD** statement.

   * - What encryption is used for exported files?
     - Exported objects use server-side encryption with AES256.

   * - Is an outbound bridge available?
     - No. Amperity Bridge for |destination-name| supports inbound data into Amperity only. Contact your Amperity representative if outbound |destination-name| connectivity is required for your use case.

.. bridge-redshift-faq-end
