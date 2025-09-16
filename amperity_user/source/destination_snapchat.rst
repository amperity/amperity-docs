.. https://docs.amperity.com/user/


.. |destination-name| replace:: Snapchat
.. |what-send| replace:: email addresses, phone numbers, and mobile advertiser IDs


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Snapchat.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Snapchat.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Snapchat

==================================================
Send query results to Snapchat
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-snapchat-start
   :end-before: .. term-snapchat-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-snapchat-build-query>`
#. :ref:`Add orchestration <sendto-snapchat-add-orchestration>`
#. :ref:`Run orchestration <sendto-snapchat-run-orchestration>`

.. sendto-snapchat-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-snapchat-build-query:

Build query
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-email-only-start
   :end-before: .. sendtos-build-query-email-only-end

.. sendto-snapchat-build-query-note-start

.. admonition:: Notes about sending data to Snapchat

   #. |destination-name| allows the following fields: **email**, **mobile_id**, and **phone**.
   #. You may send only one of only one **email**, **mobile_id**, or **phone**. 
   #. Amperity ensure that fields are mapped correctly to the schema types required by Snapchat.
   #. Amperity applies SHA-256 hashing automatically.
   #. Audience targeting in |destination-name| requires at least 1000 unique customers. Be sure your audience includes at least 1000 unique customers.

.. sendto-snapchat-build-query-note-end


.. _sendto-snapchat-build-query-email:

Use email addresses
--------------------------------------------------

.. sendto-snapchat-build-query-email-start

The following example shows how to send results using an email address:

.. code-block:: sql
   :linenos:

   SELECT
     email AS email
   FROM Merged_Customers
   WHERE email IS NOT NULL

.. sendto-snapchat-build-query-email-end


.. _sendto-snapchat-build-query-madid:

Use mobile advertiser IDs
--------------------------------------------------

.. sendto-snapchat-build-query-madid-start

The following example shows how to send results using a mobile advertising ID:

.. code-block:: sql
   :linenos:

   SELECT
     mobile_id_field AS mobile_id
   FROM MobileID_Table
   WHERE mobile_id_field IS NOT NULL

.. note:: **mobile_id_field** represents a field in Amperity that contains the mobile advertising ID and **MobileID_Table** represents the table in which that field is located.

.. sendto-snapchat-build-query-madid-end


.. _sendto-snapchat-build-query-phone:

Use phone numbers
--------------------------------------------------

.. sendto-snapchat-build-query-phone-start

The following example shows how to send results using a phone number:

.. code-block:: sql
   :linenos:

   SELECT
     phone AS phone
   FROM Merged_Customers
   WHERE phone IS NOT NULL

.. sendto-snapchat-build-query-phone-end


.. _sendto-snapchat-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-snapchat-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _destination-snapchat-schema-types:

Snapchat schema types
==================================================

.. sendto-snapchat-schema-types-start

The following Amperity columns may be mapped to the corresponding schema type to `add users <https://marketingapi.snapchat.com/docs/?lang=en-US#adding-users>`__ |ext_link| using `Snap Audience Match <https://marketingapi.snapchat.com/docs/?lang=en-US#snap-audience-match>`__ |ext_link|.

.. note:: A row that contains a **NULL** value is automatically filtered out and is shown in the error logs.

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity Column
     - Snapchat Schema Type
     - Description

   * - **email**
     - **EMAIL_SHA256**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Hashes data as SHA-256

   * - **mobile_id**
     - **MOBILE_AD_ID_SHA256**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Keeps hyphens
       * Hashes data as SHA-256

   * - **phone**
     - **PHONE_SHA256**
     - Converts each phone number to |ext_e164_format| which represents a phone number as a number up to fifteen digits in length (without spaces) that starts with a + symbol. For example: +12061234567.

       For this key, the connector:

       * Trims leading and trailing whitespace
       * Removes symbols, letters, and any leading zeros
       * Hashes data as SHA-256

.. sendto-snapchat-schema-types-end
