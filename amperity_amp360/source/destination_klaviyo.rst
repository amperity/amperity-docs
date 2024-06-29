.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Klaviyo
.. |what-send| replace:: CSV files

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Klaviyo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Klaviyo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Klaviyo

==================================================
Send query results to Klaviyo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-klaviyo-start
   :end-before: .. term-klaviyo-end

.. include:: ../../amperity_datagrid/source/destination_klaviyo.rst
   :start-after: .. destination-klaviyo-api-note-start
   :end-before: .. destination-klaviyo-api-note-end

.. include:: ../../amperity_datagrid/source/destination_klaviyo.rst
   :start-after: .. destination-klaviyo-csv-note-start
   :end-before: .. destination-klaviyo-csv-note-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-klaviyo-build-query>`
#. :ref:`Add orchestration <sendto-klaviyo-add-orchestration>`
#. :ref:`Run orchestration <sendto-klaviyo-run-orchestration>`

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-klaviyo-build-query:

Build query
==================================================

.. sendto-klaviyo-build-query-start

To send query results to |destination-name| you must know which type of audience list will be updated by Amperity. There are two types:

* :ref:`Email address only <sendto-klaviyo-build-query-email-only>`
* :ref:`Email address + customer profiles <sendto-klaviyo-build-query-email-plus-profile>`

.. sendto-klaviyo-build-query-end


.. _sendto-klaviyo-build-query-email-only:

Email address only
--------------------------------------------------

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-email-only-start
   :end-before: .. sendtos-build-query-email-only-end


.. _sendto-klaviyo-build-query-email-plus-profile:

Email address + customer profiles
--------------------------------------------------

.. sendto-klaviyo-build-query-email-plus-profile-start

You can send results to |destination-name| that include customer profiles along with their email address, such as first and last names, phone numbers, and zip codes. :ref:`Review the list of customer profile parameters <destination-klaviyo-customer-profile-parameters>` your brand can send to |destination-name|.

For example:

.. code-block:: sql

   SELECT
     amperity_id AS "external_id"
     ,given_name AS "first_name"
     ,surname AS "last_name"
     ,address AS "address1"
     ,address2 AS "address2"
     ,city
     ,state AS "region"
     ,postal AS "zip"
     ,country
     ,email AS "email"
     ,phone AS "phone_number"
     ,company AS "organization"
   FROM Merged_Customers mc

You can use a **LEFT JOIN** to add parameters from the **Unified Transactions** table, such as the most recently purchased product and the date and time of that purchase, similar to:

.. code-block:: sql

     ,order_datetime AS "last_event_date"
     ,product AS "product"
     ...
   FROM Merged_Customers mc
   LEFT JOIN Unified_Transactions ut ON mc.amperity_id = ut.amperity_id

where **last_event_date** is a built-in parameter and **product** is an example of sending a custom parameter to |destination-name|.

.. important:: This option requires the **Use full profile to update list** setting to be enabled in the data template used to send query results to |destination-name|.

.. sendto-klaviyo-build-query-email-plus-profile-end


.. _sendto-klaviyo-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-klaviyo-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _destination-klaviyo-customer-profile-parameters:

Customer profile parameters
==================================================

.. include:: ../../amperity_datagrid/source/destination_klaviyo.rst
   :start-after: .. destination-klaviyo-customer-profile-parameters-start
   :end-before: .. destination-klaviyo-customer-profile-parameters-end
