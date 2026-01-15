.. https://docs.amperity.com/user/


.. |destination-name| replace:: Listrak SMS
.. |what-send| replace:: SMS profiles
.. |what-enable| replace:: **phone**
.. |attributes-sent| replace:: |destination-name| requires phone numbers. You may include system and custom profile attributes.


.. meta::
    :description lang=en:
        Use orchestrations to manage lists in Listrak SMS.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to manage lists in Listrak SMS.

.. meta::
    :content class=swiftype name=title data-type=string:
        Manage lists in Listrak SMS

==================================================
Manage lists in Listrak SMS
==================================================

.. include:: ../../amperity_operator/source/destination_listrak_sms.rst
   :start-after: .. destination-listrak-sms-about-start
   :end-before: .. destination-listrak-sms-about-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-sms-optin-start
   :end-before: .. setting-listrak-sms-optin-end

.. include:: ../../amperity_operator/source/destination_listrak_sms.rst
   :start-after: .. destination-listrak-sms-context-start
   :end-before: .. destination-listrak-sms-context-end

.. sendto-listrak-sms-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-listrak-sms-build-query>`
#. :ref:`Add orchestration <sendto-listrak-sms-add-orchestration>`
#. :ref:`Run orchestration <sendto-listrak-sms-run-orchestration>`

.. sendto-listrak-sms-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-listrak-sms-build-query:

Build query
==================================================

.. include:: ../../amperity_operator/source/destination_listrak_sms.rst
   :start-after: .. destination-listrak-sms-attributes-start
   :end-before: .. destination-listrak-sms-attributes-end

.. sendto-listrak-sms-build-query-fields-start

An SMS profile in |destination-name| requires only a phone number, but may include all system profile attributes, including email address, first name, last name, postal code, and birthdate. Custom attributes may be included in the query results.

.. important:: Use the **SMS Opt Status** table to filter the results to include only customers who have opted in to receiveing SMS messaaging.

.. sendto-listrak-sms-build-query-fields-end

.. include:: ../../amperity_operator/source/destination_listrak_sms.rst
   :start-after: .. destination-listrak-sms-howitworks-optin-start
   :end-before: .. destination-listrak-sms-howitworks-optin-end

.. sendto-listrak-sms-build-query-start

**Example query**

.. code-block:: sql
   :linenos:

   WITH sms_opt_status AS (
     SELECT
       so.amperity_id
       ,so.phone
       ,so.is_sms_opted_in
     FROM SMS_Opt_Status so
   )

   SELECT
     co.amperity_id
     ,co.Phone AS "Phone"
     ,co.Email AS "Email Address"
     ,co.FirstName AS "First Name"
     ,co.LastName AS "Last Name"
     ,co.PostalCode AS "Postal Code"
     ,co.Birthdate AS "Birthday"
     ,co.LoyaltyTier AS "Loyalty"
   FROM Customer360 co
   LEFT JOIN SMS_Opt_Status so ON co.amperity_id = so.amperity_id
   WHERE is_sms_opted_in = true

.. sendto-listrak-sms-build-query-end

.. include:: ../../amperity_user/source/campaign_listrak_sms.rst
   :start-after: .. channel-listrak-sms-configure-attributes-start
   :end-before: .. channel-listrak-sms-configure-attributes-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-listrak-sms-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-listrak-sms-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
