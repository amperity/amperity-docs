.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Zendesk
.. |what-send| replace:: customer data

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Zendesk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Zendesk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Zendesk

==================================================
Send query results to Zendesk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-zendesk-start
   :end-before: .. term-zendesk-end

.. sendto-zendesk-start

Amperity may be configured to create or update user records in Zendesk by using the Zendesk Users API to |ext_zendesk_rest_api_create_or_update_users|. Use this connector to deliver a better customer support experience by pre-populating Zendesk user records with customer records from Amperity, including:

* Order history
* Loyalty status
* Satisfaction survey results
* Shopping preferences
* and more

Use this data to show customer support representatives information related to product recommendations, next best actions, and likelihood of churn.

.. sendto-zendesk-end

.. sendto-zendesk-note-start

.. note:: Creating or updating records are |ext_zendesk_rest_api_rate_limits| to a maximum of 100 users per second.

.. sendto-zendesk-note-end

.. sendto-zendesk-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-zendesk-build-query>`
#. :ref:`Add orchestration <sendto-zendesk-add-orchestration>`
#. :ref:`Run orchestration <sendto-zendesk-run-orchestration>`

.. sendto-zendesk-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-zendesk-build-query:

Build query
==================================================

.. sendto-zendesk-map-results-start

Results that are sent to Zendesk must be correctly mapped to the following attributes, as required by the |ext_zendesk_rest_api_user|:

.. list-table::
   :widths: 140 140 320
   :header-rows: 1

   * - Zendesk Fields
     - Type
     - Description

   * - **email**
     - String
     - Optional; may be used instead of **external_id**. The primary email address for the customer record. Zendesk uses the **email** field to identify users within Zendesk by default. You may use the **external_id** field to provide the Amperity ID to Zendesk, after which you may use the Amperity ID within Zendesk to identify a user.

       When the **email** field is present and **external_id** is not present, multiple records orchestrated with the same email address are treated as updates to the same user.

       .. tip:: Use this field in conjunction with the **verified** field to define when email address updates are made to a customer's primary or secondary email address.
   * - **external_id**
     - String
     - Optional; should be used instead of **email**. This field should be associated with the Amperity ID.

       When **external_id** field is provided, it will take precedence over **email** and becomes the field Zendesk will use to identify users. After the creation of a user with a given **external_id**, subsequent requests with the same **external_id** are treated as updates and, in the presence of the same **external_id** and different **email** values, additional email addresses are added to the same user as secondary email addresses.

       .. tip:: Zendesk requires one of **email** or **external_id**, but is designed to *prefer* the **external_id** when it is available.

   * - **name**
     - String
     - Required. The full name of the customer.

       .. warning:: A record without a **name** and one of **email** or **external_id** is filtered out, marked with an error, and is not submitted to Zendesk.

   * - **phone**
     - String
     - Optional. The primary phone number associated with the customer record.

       .. note:: The Zendesk User API requires phone numbers to be compliant with the |ext_e164_format|.
   * - **user_fields.[field]**
     - String
     - Optional. The Zendesk User API contains 37 fields, most of which are not required. The Zendesk User API supports custom fields as long as they are prefixed with **user_fields.** in the field name. For example: **user_fields.city**.

       .. note:: Fields submitted to Zendesk that are not built into the Zendesk User API or are not formatted as valid custom fields (including misspellings) will be ignored.

.. sendto-zendesk-map-results-end


.. _sendto-zendesk-map-results-with-attributes-table:

Use an attributes table
--------------------------------------------------

.. term-attributes-table-start

An attributes table consolidates a set of fields for use with a specific downstream workflow, and then assigns column names to each field that correctly maps to the naming patterns that are required by that workflow.

.. term-attributes-table-end

.. sendto-zendesk-map-results-with-attributes-table-start

An attributes table can be configured to allow users of the **Visual Segment Editor** to build segments that send results to Zendesk.

.. sendto-zendesk-map-results-with-attributes-table-end

.. term-attributes-table-note-start

.. note:: Fields in an attributes table are available to SQL editors in the **Queries** and **Segments** pages. An attributes table must be configured to be made available to the visual editors.

.. term-attributes-table-note-end

.. sendto-zendesk-map-results-with-attributes-table-context-start

For example, to send results from Amperity to Zendesk you must associate a user's **full_name** to **name**, you may associate the Amperity ID to **external_id**, and you may provide custom fields as long as they begin with **user_fields.**. When this table has been **Made available to the Visual Segment Editor** users of AmpIQ will be able to build visual segments that use fields in the attributes table.

.. sendto-zendesk-map-results-with-attributes-table-context-end

.. sendto-zendesk-map-results-with-attributes-table-example-start

The following query will build an attributes table that maps the Amperity ID to the Zendesk external ID, and then map email addresses, full names, and phone numbers to the corresponding Zendesk attributes:

.. code-block:: sql

   SELECT
     amperity_id
     ,amperity_id AS external_id
     ,email AS email
     ,LOWER(full_name) AS name
     ,phone AS phone
   FROM Customer_360

.. important:: Only tables that contain the Amperity ID can be made available to the **Visual Segment Editor**. The first line in a **SELECT** statement that builds an attributes table must be **amperity_id**.

A user can build a visual query or visual segment by selecting fields from this attributes table, and then send the results to Zendesk with the correct mapping already applied.

.. caution:: You cannot build an attributes table that contains custom fields. A column name may only contain alphanumeric characters (a-Z), underscores (_), and must start with an alphanumeric character. Use a query for results that send custom fields to Zendesk.

.. sendto-zendesk-map-results-with-attributes-table-example-end


.. _sendto-zendesk-map-results-with-query:

Use a query
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-query-start
   :end-before: .. term-query-end

.. sendto-zendesk-build-query-example-minimum-start

The following example is a query that contains only the fields that are required by Zendesk: a name, an email address, and the Amperity ID, which will be used to identify the users in Zendesk:

.. code-block:: sql

   SELECT
     amperity_id AS external_id
     ,LOWER(full_name) AS name
     ,email AS email
   FROM Customer_360

.. sendto-zendesk-build-query-example-minimum-end

.. sendto-zendesk-build-query-example-custom-fields-start

The following example is a query that sends additional contact information for customers that uses some of the fields that are built into the Zendesk User API along with a small set of custom fields for each customer's location:

.. code-block:: sql

   SELECT
     amperity_id AS external_id
     ,LOWER(full_name) AS name
     ,email AS email
     ,phone AS phone
     ,address AS "user_fields.address"
     ,address2 AS "user_fields.address2"
     ,city AS "user_fields.city"
     ,state AS "user_fields.state"
     ,postal AS "user_fields.postal"
   FROM Customer_360

.. sendto-zendesk-build-query-example-custom-fields-end


.. sendto-zendesk-build-query-example-custom-fields-start

Build a query named "Zendesk - Users" to collect name and phone data from the customer 360 database, along with the Amperity ID and a custom field:

.. code-block:: sql

   SELECT
     amperity_id AS external_id,
     lower(full_name) AS name,
     phone AS phone,
     city AS "user_fields.city"
   FROM Customer_360

.. sendto-zendesk-build-query-example-custom-fields-end


.. _sendto-zendesk-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-zendesk-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
