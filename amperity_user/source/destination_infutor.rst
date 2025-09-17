.. https://docs.amperity.com/user/


.. |destination-name| replace:: Infutor
.. |what-send| replace:: CSV files


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Infutor.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Infutor.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Infutor

==================================================
Send query results to Infutor
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-infutor-start
   :end-before: .. term-infutor-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-infutor-build-query>`
#. :ref:`Add orchestration <sendto-infutor-add-orchestration>`
#. :ref:`Run orchestration <sendto-infutor-run-orchestration>`

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending query results to |destination-name|.


.. _sendto-infutor-build-query:

Build query
==================================================

.. sendto-infutor-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by |destination-name|. Data shaping is typically required only one time.

You can do this in the following ways:

#. Use |sql_spark| to add a SQL table to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Use |sql_presto| to add a SQL query that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use cases for downstream workflows.

.. sendto-infutor-build-query-end


.. _sendto-infutor-build-query-pii:

Infutor and PII data
--------------------------------------------------

.. sendto-infutor-build-query-pii-start

Data that is sent to Infutor primarily contains PII for use with building and maintaining enriched customer profile data for downstream workflows.

In certain cases, it may be necessary to hash the data, such as for birthdates or for other individual-specific identifiers like a social security number (SSN).

If a field does require hashing, use :ref:`one-way SHA-256 hashing <sendto-infutor-build-query-sha-256>` or :ref:`cast the value to a random unique identifier (UUID) <sendto-infutor-build-query-cast-as-uuid>`.

.. sendto-infutor-build-query-pii-end


.. _sendto-infutor-build-query-sha-256:

One-way SHA-256 hash
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-style-guide-one-way-sha256-hashes-start
   :end-before: .. sql-presto-style-guide-one-way-sha256-hashes-end

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-style-guide-one-way-sha256-hash-syntax-start
   :end-before: .. sql-presto-style-guide-one-way-sha256-hash-syntax-end

.. sendto-infutor-build-query-sha-256-start

For example:

.. code-block:: sql

   TO_HEX(SHA256(TO_UTF8(UPPER(TRIM(Birthdate)))))

.. sendto-infutor-build-query-sha-256-end


.. _sendto-infutor-build-query-cast-as-uuid:

CAST as UUID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-cast-start
   :end-before: .. sql-presto-function-cast-end

For example:

.. sendto-infutor-build-query-cast-as-uuid-start

.. code-block:: sql

   ,CAST(birthdate AS UUID) AS "Birthdate"

.. sendto-infutor-build-query-cast-as-uuid-end


.. _sendto-infutor-build-query-map-fields:

Map fields to Infutor
--------------------------------------------------

.. sendto-infutor-build-query-map-fields-start

The following **SELECT** statement collects data from Amperity and :ref:`maps it to the preferred field <sendto-infutor-fields>`.

.. code-block:: sql
   :linenos:

   SELECT
     ,amperity_id AS "Amperity ID"
     ,full_name AS "Full Name"
     ,given_name AS "First Name"
     ,surname AS "Last Name"
     ,address AS "Address1"
     ,address2 AS "Address2"
     ,state AS "State"
     ,postal AS "Zip5"
     ,phone-1 AS "Phone"
     ,phone-2 AS "Phone2"
     ,email AS "Email"
     ,ip_address AS "IP"
   FROM Customer360

.. sendto-infutor-build-query-map-fields-end


.. _sendto-infutor-fields:

Infutor field reference
--------------------------------------------------

.. sendto-infutor-fields-start

Map fields in Amperity to the following fields in Infutor. (The Amperity column lists the names of the fields as if they were identical to the semantic tag associated with that field.) Most Infutor fields allow alternate field names.

.. important:: Talk to your Infutor Solutions Engineering representative about date of birth (DOB) or social security number (SSN) data prior to sending results with that data to Infutor.

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity column
     - Infutor field
     - Description

   * - **full_name**
     - **Full Name**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-full-name-start
          :end-before: .. term-full-name-end

       Alternate field names: **Full Individual Name**, **UnparsedName**, **FullName**, **Full_Name**, **Full_Individual_Name**, **Individual_Name**, and **Name**.

   * - **given_name**
     - **First Name**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end

       Alternate field names: **FName**, **Given Name**, **Given_Name**, and **First_Name**.

   * - **surname**
     - **Last Name**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end

       Alternate field names: **LName**, **LastName**, **Surname**, **Last_Name**, **Family Name**, **Family_Name**, and **FamilyName**.

   * - **address**
     - **Address1**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address-start
          :end-before: .. term-address-end

       Alternate field names: **Address Line 1**, **Address_Line_1**, **Address 1**, **Street Address 1**, and **Full Address**.

   * - **address2**
     - **Address2**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-address2-start
          :end-before: .. term-address2-end

       Alternate field names: **Address Line 2**, **Address_Line_2**, and **Address 2**.

   * - **state**
     - **State**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end

       Alternate field names: **State_Code**, **StateCode**, and **State Code**.

   * - **postal**
     - **Zip5**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end

       Alternate field names: **Postal Code**, **Postal_Code**, and **5 Digit Zip Code**.

   * - **phone**

       **phone-1**
     - **Phone**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

       Alternate field names: **Phone Number**, **Phone_Number**, **Telephone Number**, **Telephone_Number**, **Phone1**, and **Telephone**.

   * - **phone-2**
     - **Phone2**
     - An additional phone number that is created by phone ordinal semantic tags that are used when multiple phone numbers are available in the source data.

       Alternate field names: **Second Phone**, **Second Phone Number**, **Second_Phone**, **Second_Phone_Number**, and **Phone Number 2**.

   * - **email**
     - **Email**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

       Alternate field names: **Email Address** and **Email_Address**.

   * - [no default]
     - **IP**
     - The IP address associated with this individual, if available.

       Alternate field names: **IP Address**.

.. sendto-infutor-fields-end


.. _sendto-infutor-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-infutor-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
