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

Before you can create inbound sharing between |destination-name| and Amperity you need to collect the following information.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: center
          :class: no-scaled-link
     - The values that you need to write the IAM policies are specific to your tenant. Amperity shows them at the start of the bridge flow.

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


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: center
          :class: no-scaled-link
     - Permission to create IAM roles in the AWS account that owns your |destination-name|, and permission to associate an IAM role with your cluster or workgroup.

       Both the :ref:`query role <bridge-redshift-from-redshift-configure-redshift-query-role>` and the :ref:`unload role <bridge-redshift-from-redshift-configure-redshift-unload-role>` are created in that account.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: center
          :class: no-scaled-link
     - Superuser access to |destination-name|, or ownership of the objects that you plan to sync.

       Superuser access is required to :ref:`create the database user <bridge-redshift-from-redshift-configure-redshift-db-user>` on a provisioned cluster. :ref:`Granting database access <bridge-redshift-from-redshift-configure-redshift-grants>` requires a superuser or the owner of each object.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: center
          :class: no-scaled-link
     - The details of your |destination-name| deployment, which are :ref:`entered in Amperity <bridge-redshift-from-redshift-add-bridge>` after the roles exist:

       * Whether it is a provisioned cluster or a Serverless workgroup.
       * The region in which it runs, such as "us-west-2".
       * The cluster identifier, for a provisioned cluster, or the workgroup name, for a Serverless workgroup.
       * A database within your |destination-name| to use as an entry point.
       * The 12-digit AWS account ID that owns the two roles.

.. bridge-redshift-from-redshift-get-details-end


.. _bridge-redshift-from-redshift-configure-redshift:

Configure Amazon Redshift
--------------------------------------------------

.. bridge-redshift-from-redshift-configure-redshift-start

To configure |destination-name| to connect with Amperity you need to create the query role and the unload role in the AWS account that owns your |destination-name|, attach the unload role to your cluster or workgroup, and then grant read access within |destination-name| to the identity that the queries run as. On a provisioned cluster you must also create the database user that the queries run as.

.. note:: IAM gets Amperity as far as the cluster. It grants no access to any data. Access to data is granted inside |destination-name|, as described in :ref:`Grant database access <bridge-redshift-from-redshift-configure-redshift-grants>`.

.. bridge-redshift-from-redshift-configure-redshift-end


.. _bridge-redshift-from-redshift-configure-redshift-db-user:

Create the database user
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-configure-redshift-db-user-start

This step applies only to provisioned clusters. Skip it for a Serverless workgroup, where the database identity is :ref:`derived from the query role <bridge-redshift-from-redshift-configure-redshift-grants>`.

On a provisioned cluster the queries run as a named |destination-name| database user. Amperity does not create this user, so create it now. The name that you choose is used in the :ref:`permission policy for the query role <bridge-redshift-from-redshift-configure-redshift-query-role>` and is entered as the **Database user** when you :ref:`add the inbound bridge <bridge-redshift-from-redshift-add-bridge>`.

Connect to your cluster as a superuser using the **Query editor v2** in the |destination-name| console, and then run:

.. code-block:: sql

   CREATE USER amperity PASSWORD DISABLE;

You may use any name for this user. Use all lowercase characters.

.. note:: You may set a real password by replacing **DISABLE** with the password that you want. Nothing about the integration changes. Amperity is never given the password and never uses it.

   A password would only allow someone to log in as this user directly, which is not required by the bridge. Amperity recommends using **DISABLE**.

.. bridge-redshift-from-redshift-configure-redshift-db-user-end


.. _bridge-redshift-from-redshift-configure-redshift-query-role:

Create the query role
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-configure-redshift-query-role-start

In the AWS account that owns your |destination-name|, create an IAM role with a name that starts with "AmperityRedshiftBridge", such as "AmperityRedshiftBridgeQuery".

**Trust policy**

Substitute the **Amperity query role** and **External ID** values that you copied when you :ref:`got the details <bridge-redshift-from-redshift-get-details>`.

.. important:: Trust the Amperity query role ARN exactly as it is given, rather than the entire Amperity account.

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

**Permission policy for a Serverless workgroup**

Attach this policy for a Serverless workgroup. Replace **<REGION>** with the region in which your |destination-name| runs and **<YOUR_ACCOUNT_ID>** with the 12-digit AWS account that owns it.

**<WORKGROUP_UUID>** is the UUID for the workgroup, taken from its ARN, and not the name of the workgroup. Find it in the details for the workgroup in the |destination-name| console or by running:

.. code-block:: bash

   aws redshift-serverless get-workgroup --workgroup-name <WORKGROUP_NAME>

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

**Permission policy for a provisioned cluster**

Attach this policy instead for a provisioned cluster. Replace **<REGION>** with the region in which your |destination-name| runs and **<YOUR_ACCOUNT_ID>** with the 12-digit AWS account that owns it. **<CLUSTER_IDENTIFIER>** is the identifier for your cluster, **<DATABASE>** is the database that you connect through, and **<DB_USER>** is the :ref:`database user that you created <bridge-redshift-from-redshift-configure-redshift-db-user>`.

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

.. note:: **DescribeStatement** and **GetStatementResult** are keyed by statement ID rather than by a resource ARN, which is why AWS requires them to be applied to "*".

.. bridge-redshift-from-redshift-configure-redshift-query-role-end


.. _bridge-redshift-from-redshift-configure-redshift-unload-role:

Create the unload role
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-configure-redshift-unload-role-start

Create a second IAM role in the same AWS account. You may use any name for this role.

**Trust policy**

Replace **<YOUR_ACCOUNT_ID>** with the 12-digit AWS account that owns your |destination-name|, which is the same account in which you are creating these roles.

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

Substitute the **Amperity storage role** value that you copied when you :ref:`got the details <bridge-redshift-from-redshift-get-details>`. This is the only permission that this role has. It holds no storage access of its own and reaches storage by chaining.

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

.. important:: This step is required. |destination-name| can use only IAM roles that are associated with it, which means a correctly written role that is not attached still fails when the **UNLOAD** statement runs.

Associate the unload role using the |destination-name| console:

* For a provisioned cluster, open your cluster, and then from the **Actions** menu select **Manage IAM roles**.
* For a Serverless workgroup, open your namespace, and then under **Security and encryption** select **Manage IAM roles**.

.. bridge-redshift-from-redshift-configure-redshift-unload-role-end


.. _bridge-redshift-from-redshift-configure-redshift-grants:

Grant database access
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-redshift-from-redshift-configure-redshift-grants-start

IAM gets Amperity as far as the cluster. It grants no access to any data. Access to data is granted inside |destination-name|, to the database identity that the queries run as.

**Which identity to grant to**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Deployment
     - Identity

   * - Provisioned cluster
     - The :ref:`database user that you created <bridge-redshift-from-redshift-configure-redshift-db-user>`, which is the same user that you enter as the **Database user** when you :ref:`add the inbound bridge <bridge-redshift-from-redshift-add-bridge>`.

   * - Serverless workgroup
     - |destination-name| derives the identity from the query role that Amperity assumes and names it "IAMR:<QUERY_ROLE_NAME>".

**Grant the reads**

The statements are the same for both deployments. Only the grantee is different. Run them as a superuser or as the owner of the objects, once for each schema and once for each table that you intend to sync.

For a provisioned cluster the grantee is the database user.

.. code-block:: sql

   GRANT USAGE ON SCHEMA <SCHEMA> TO <DB_USER>;
   GRANT SELECT ON <SCHEMA>.<TABLE_OR_VIEW> TO <DB_USER>;

For a Serverless workgroup the name of the identity contains a colon, which is why |destination-name| requires it to be wrapped in double quotes.

.. code-block:: sql

   GRANT USAGE ON SCHEMA <SCHEMA> TO "IAMR:<QUERY_ROLE_NAME>";
   GRANT SELECT ON <SCHEMA>.<TABLE_OR_VIEW> TO "IAMR:<QUERY_ROLE_NAME>";

Grant only what you want Amperity to see. Amperity can read exactly what this identity can read, and nothing more.

.. tip:: To give Amperity access to only a subset of the columns in a table, create a view that exposes only those columns, and then grant **SELECT** on the view instead of on the table.

.. important:: Permission management for external tables is less fine-grained than it is for standard internal tables.

   |destination-name| grants access to external tables, such as those in Amazon Redshift Spectrum or in external schemas, at the schema level and not for each table. This means you cannot expose a single external table without granting access to the entire schema.

   To keep exposure scoped, create a view that selects only the intended external table, and then grant Amperity **SELECT** on the view instead.

**How much to grant**

Grant only the schemas and objects that you plan to sync. You do not have to open up every database on the cluster. Amperity lists the databases that this identity can read and skips the rest.

You can widen the grants later. New grants are picked up the next time that Amperity reads your catalog.

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
     - Open the **Sources** page. Under **Inbound shares** click **Add bridge**.

       Choose **Amazon Redshift**, choose **Create new bridge**, and then give the bridge a name.

       The dialog box displays the **Amperity query role**, **External ID**, and **Amperity storage role** values that are required by the :ref:`query role <bridge-redshift-from-redshift-configure-redshift-query-role>` and the :ref:`unload role <bridge-redshift-from-redshift-configure-redshift-unload-role>`. :ref:`Copy all three <bridge-redshift-from-redshift-get-details>` before continuing.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Enter the connection details.

       .. list-table::
          :widths: 30 20 50
          :header-rows: 1

          * - Field
            - Applies to
            - What to enter

          * - **Deployment**
            - Both
            - Provisioned cluster or Serverless workgroup.

          * - **Region**
            - Both
            - The region in which your |destination-name| runs, such as "us-west-2".

          * - **Cluster identifier**
            - Provisioned
            - The identifier for the cluster.

          * - **Workgroup name**
            - Serverless
            - The name of the workgroup, and not its UUID.

          * - **Database**
            - Both
            - Any database in your |destination-name|. Amperity uses it as an entry point and discovers the other databases on the cluster through it.

          * - **Database user**
            - Provisioned
            - The user that the query runs as. This user must exist and must hold **SELECT** on your tables.

          * - **AWS account ID**
            - Both
            - The 12-digit account that owns the two roles.

          * - **Query role ARN**
            - Both
            - The full ARN, such as "arn:aws:iam::123456789012:role/AmperityRedshiftBridgeQuery".

          * - **Unload role name**
            - Both
            - The name of the role, and not an ARN.

       When finished, click **Save and continue**. Amperity reads your catalog as soon as the connection is saved.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Select the tables to sync.

       Amperity presents your catalog as a tree of database, schema, and object. Both tables and views may be selected. The **information_schema** and **pg_*** schemas that belong to |destination-name| are hidden.

       .. note:: A database that your query role cannot read is skipped, rather than failing the entire listing. If a database that you expected is missing, review the :ref:`grants for the query identity <bridge-redshift-from-redshift-configure-redshift-grants>`.

.. bridge-redshift-from-redshift-add-bridge-steps-end


.. _bridge-redshift-to-redshift:

To Amazon Redshift
==================================================

.. bridge-redshift-to-redshift-start

Coming soon.

.. bridge-redshift-to-redshift-end
