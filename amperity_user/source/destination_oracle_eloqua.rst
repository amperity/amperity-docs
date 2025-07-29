.. https://docs.amperity.com/user/


.. |destination-name| replace:: Oracle Eloqua
.. |what-send| replace:: audiences


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Oracle Eloqua.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Oracle Eloqua.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Oracle Eloqua

==================================================
Send query results to Oracle Eloqua
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oracle-eloqua-start
   :end-before: .. term-oracle-eloqua-end

.. include:: ../../amperity_operator/source/destination_oracle_eloqua.rst
   :start-after: .. destination-oracle-eloqua-api-note-start
   :end-before: .. destination-oracle-eloqua-api-note-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-oracle-eloqua-build-query>`
#. :ref:`Add orchestration <sendto-oracle-eloqua-add-orchestration>`
#. :ref:`Run orchestration <sendto-oracle-eloqua-run-orchestration>`

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-oracle-eloqua-build-query:

Build query
==================================================

.. destination-oracle-eloqua-build-query-start

You will need to build a query that outputs fields that can be mapped to static lists in |destination-name|.

.. code-block:: sql
   :linenos:

   SELECT
     email AS C_EmailAddress
     ,given_name AS C_FirstName
     ,surname AS C_LastName
     ,full_name AS C_First_And_Last_Name
     ,address AS C_Address_1
     ,city AS C_City
     ,state AS C_State_Or_Province
     ,postal AS C_Zip_Or_Postal_Code
     ,TO_HEX(MD5(TO_UTF8(UPPER(TRIM(email))))) AS C_MD5_Hashed_Email_Address
     ,TO_HEX(SHA256(TO_UTF8(UPPER(TRIM(email))))) AS C_SHA256_Hashed_Email_Address
   FROM Customer_360

.. destination-oracle-eloqua-build-query-end

.. destination-oracle-eloqua-build-query-custom-attributes-start

.. tip:: You can define `custom attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/Tasks/CreatingContactFields.htm>`__ |ext_link| with |destination-name|. These attributes **must** exist in |destination-name| before Amperity can send updates and must be different than the `default attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/ContactFieldsDefinitions.htm>`__ |ext_link|.

   **To send custom attributes to Oracle Eloqua**

   #. Configure the custom attribute in |destination-name|.
   #. Find the database type name for that attribute. For example, a flag for customers who have made a repeat purchase within the previous 90 days: **C_Early_Repeat_Purchaser**.
   #. Build a query that returns a field in Amperity that is mapped to the database type name for that custom attribute. For example, if the **Early Repeat Purchaser** field from **Transaction Attributes Extended** has already been joined to your **Customer 360** table:

.. code-block:: sql
   :linenos:

   SELECT
     email AS C_EmailAddress
     ,given_name AS C_FirstName
     ,surname AS C_LastName
     ,full_name AS C_First_And_Last_Name
     ,address AS C_Address_1
     ,city AS C_City
     ,state AS C_State_Or_Province
     ,postal AS C_Zip_Or_Postal_Code
     ,TO_HEX(MD5(TO_UTF8(UPPER(TRIM(email))))) AS C_MD5_Hashed_Email_Address
     ,TO_HEX(SHA256(TO_UTF8(UPPER(TRIM(email))))) AS C_SHA256_Hashed_Email_Address
     ,early_repeat_purchaser AS C_Early_Repeat_Purchaser
   FROM Customer_360

.. destination-oracle-eloqua-build-query-custom-attributes-end


.. _sendto-oracle-eloqua-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-oracle-eloqua-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
