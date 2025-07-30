.. https://docs.amperity.com/user/


.. |destination-name| replace:: Optimizely
.. |plugin-name| replace:: Amazon S3
.. |what-send| replace:: CSV files


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Optimizely.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Optimizely.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Optimizely

==================================================
Send query results to Optimizely
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-optimizely-start
   :end-before: .. term-optimizely-end

.. sendto-optimizely-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-optimizely-build-query>`
#. :ref:`Add orchestration <sendto-optimizely-add-orchestration>`
#. :ref:`Run orchestration <sendto-optimizely-run-orchestration>`

.. sendto-optimizely-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-optimizely-build-query:

Build query
==================================================

.. sendto-optimizely-build-query-start

You will need to build a query that can send results to |destination-name| as a CSV file. This may be done for one of the following typically done for one of the following types:

* :ref:`Customer profiles <sendto-optimizely-build-query-customer-profiles>`
* :ref:`List attributes <sendto-optimizely-build-query-list-attributes>`

.. warning:: :ref:`Queries and database exports from Amperity sent to |destination-name| should not include PII data <sendto-optimizely-build-query-pii>`.

.. sendto-optimizely-build-query-end


.. _sendto-optimizely-build-query-pii:

Optimizely and PII data
--------------------------------------------------

.. sendto-optimizely-build-query-pii-start

Optimizely terms of service prohibit PII data -- names, social security numbers, email addresses, and similar data -- from being collected by or sent to |destination-name| services for use with customer profiles or any other feature. It is important to ensure that queries and database exports from Amperity comply with requirements for using |destination-name| services.

Because the data sent to |destination-name| contains the Amperity ID, should you need to associate data with PII, you can use other systems that allow PII data along with the Amperity ID to make these associations.

If email addresses or other types of fields that contain PII must be provided, use :ref:`one-way SHA-256 hashing <sendto-optimizely-build-query-sha-256>` or :ref:`cast the value to a random unique identifier (UUID) <sendto-optimizely-build-query-cast-as-uuid>`.

.. sendto-optimizely-build-query-pii-end


.. _sendto-optimizely-build-query-sha-256:

One-way SHA-256 hash
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-style-guide-one-way-sha256-hashes-start
   :end-before: .. sql-presto-style-guide-one-way-sha256-hashes-end

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-style-guide-one-way-sha256-hash-syntax-start
   :end-before: .. sql-presto-style-guide-one-way-sha256-hash-syntax-end

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-to-hex-example-one-way-hash-start
   :end-before: .. sql-presto-function-to-hex-example-one-way-hash-end


.. _sendto-optimizely-build-query-cast-as-uuid:

CAST as UUID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-cast-start
   :end-before: .. sql-presto-function-cast-end

.. include:: ../../amperity_reference/source/sql_presto.rst
   :start-after: .. sql-presto-function-cast-example-cast-as-uuid-start
   :end-before: .. sql-presto-function-cast-example-cast-as-uuid-end


.. _sendto-optimizely-build-query-customer-profiles:

Customer profiles
--------------------------------------------------

.. sendto-optimizely-build-query-customer-profiles-start

`customer profiles <https://docs.developers.optimizely.com/web/docs/customer-profiles>`__ |ext_link| are a collection of customer attributes, such as demographic data, behavioral characteristics, or any other information particular to your industry and customers. Customer profiles provide a consolidated, dynamic view of your customers, enabling you to refine this view as you obtain more information and to take action based on this view.

You can export any combination of attributes from Amperity for use with customer profiles. This requires exporting an ID that is mapped to the |destination-name| **customerId** field, after which you can join the Amperity ID, and any collection of customer profile attributes to that output result, before sending to |destination-name|.

.. sendto-optimizely-build-query-customer-profiles-end


.. _sendto-optimizely-build-query-customer-profile-requirements:

Customer profile requirements
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sendto-optimizely-build-query-customer-profile-requirements-start

Data that is output from Amperity and sent to |destination-name| must be shaped to the following requirements:

#. The header row of the CSV file must include a column named **customerId**. This name is not case-sensitive. All rows in the CSV file must contain a valid value for this column. The value of this column should be unchanged from the original value. For example. if the customer ID field is a UUID in Amperity, then it should be sent to |destination-name| as the same UUID.

#. Each column in the header row must be a registered attribute name in |destination-name|. A CSV *may contain a subset* of the registered attributes, it *does not need to contain all* of the registered attributes. There is no requirement for a minimum number of registered attributes.

#. Each column header for a registered attribute in the CSV file must correspond to the correct data type in |destination-name| and attribute name.

   .. note:: If a column header doesn't correspond to a registered attribute name, the upload will fail. If an attribute value doesn't respect the attribute's data type and format, the upload will fail.

.. sendto-optimizely-build-query-customer-profile-requirements-end


.. _sendto-optimizely-build-query-customer-profile-map-id:

Map ID to Optimizely
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sendto-optimizely-build-query-customer-profile-map-id-start

|destination-name| requires data to contain a **customerID** field. This field should not be associated with the Amperity ID, but instead be associated with a field that |destination-name| is already aware of by way of other data sources.

#. Choose an ID that is available in the Amperity customer 360 database that **IS NOT** the Amperity ID.
#. Build a query that outputs that ID as the **customerId** field for |destination-name|.
#. Add any other attributes you want to that data. Each of these attributes should be mapped in the query to a known field in |destination-name|.
#. Any number of fields in Amperity, from any number of individual tables, can be mapped to fields in |destination-name|.
#. Output the results of this query to |destination-name| as a CSV file using |plugin-name| and the customer's |destination-name| credentials.

The customerID must be at least 8 characters. Use a **CASE** statement to ensure that the ID that is associated to the **customerId** in |destination-name| is at least 8 characters. For example:

.. code-block:: sql
   :linenos:

   CASE
     WHEN LENGTH(id_from_amperity_table) < 8
     THEN lpad(id_from_amperity_table, 8, '0')
     ELSE id_from_amperity_table
   END AS "customerId"

and then join attributes to this ID, including the Amperity ID (as an attribute in the output).

.. sendto-optimizely-build-query-customer-profile-map-id-end


.. _sendto-optimizely-build-query-customer-profile-define-query:

Define a query
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sendto-optimizely-build-query-customer-profile-define-query-start

The following **SELECT** statement collects all the distinct IDs from Table O to associate with the |destination-name| **customerId**, ensures they are at least 8 characters, collects attributes from the customer 360 profile (represented by C) and Table A (represented by A), and then joins the attributes, along with the Amperity ID to a table that uses the **customerId** as the unique ID.

.. important:: For each row in the example, the field names that are represented by **AS "Optimizely_abc"** and **AS "Optimizely_123"** represent the field names to which the query maps data as they are defined in |destination-name|. These must match.

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     CASE
       WHEN LENGTH(id_to_associate_to_customerId) < 8
       THEN lpad(id_to_associate_to_customerId, 8, '0')
       ELSE id_to_associate_to_customerId
     END AS "customerId"

     ,C.amperity_id AS "Optimizely_ampID"
     ,C.given_name AS "Optimizely_FirstName"
     ,C.gender AS "Optimizely_Gender"
     ,C.city AS "Optimizely_City"
     ,C.state AS "Optimizely_State"
     ,C.postal AS "Optimizely_Postal"
     ,C.country AS "Optimizely_Country"
     ,C.profile_attribute_a AS "Optimizely_A"
     ,C.profile_attribute_b AS "Optimizely_B"
     ,C.profile_attribute_c AS "Optimizely_C"

     ,A.pk AS "Optimizely_pk"
     ,A.guid AS "Optimizely_guid"
     ,A.country AS "Optimizely_country"
     ,A.table_attribute_1 AS "Optimizely_1"
     ,A.table_attribute_2 AS "Optimizely_2"
     ,A.table_attribute_3 AS "Optimizely_3"

   FROM Customer360 C
   JOIN TableO O ON O.amperity_id = C.amperity_id
   LEFT JOIN TableA A ON A.amperity_id = C.amperity_id
   WHERE O.id_to_associate_to_customerId IS NOT NULL

.. note:: There are many ways to build a **SELECT** or **SELECT DISTINCT** statement that maps data in the Amperity customer 360 database to fields in |destination-name|. The only absolute requirement is to map an ID that is not the Amperity ID to the **customerID** field in Optimizely. Attributes from tables in Amperity that you want to send to |destination-name| must be mapped to the field names as they are defined in |destination-name|, but there is no requirement to map to any particular attribute.

.. sendto-optimizely-build-query-customer-profile-define-query-end


.. _sendto-optimizely-build-query-list-attributes:

List attributes
--------------------------------------------------

.. sendto-optimizely-build-query-list-attributes-start

A `list attributes <https://docs.developers.optimizely.com/web/docs/list-attributes>`__ |ext_link| targets users who are already part of a defined audience that exists in a downstream system that is not in |destination-name|. All the list attribute requires is a CSV file that contains unique IDs in a single column. This may be the Amperity ID or it may be some other unique ID. The ID that is set to the |destination-name| list attribute must be the ID that is required by the external downstream system.

.. sendto-optimizely-build-query-list-attributes-end


.. _sendto-optimizely-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-optimizely-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
