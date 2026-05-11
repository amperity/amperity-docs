.. https://docs.amperity.com/user/


.. |destination-name| replace:: Listrak SMS
.. |what-send| replace:: SMS profile updates
.. |what-enable| replace:: **phone**
.. |attributes-sent| replace:: |destination-name| requires phone numbers. You may include system and custom profile attributes.


.. meta::
    :description lang=en:
        Use orchestrations to update profiles in Listrak SMS.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to update profiles in Listrak SMS.

.. meta::
    :content class=swiftype name=title data-type=string:
        Update profiles in Listrak SMS

==================================================
Update profiles in Listrak SMS
==================================================

.. include:: ../../amperity_operator/source/destination_listrak_sms_profile.rst
   :start-after: .. destination-listrak-sms-profile-about-start
   :end-before: .. destination-listrak-sms-profile-about-end

.. include:: ../../amperity_operator/source/destination_listrak_sms_profile.rst
   :start-after: .. destination-listrak-sms-profile-updates-only-start
   :end-before: .. destination-listrak-sms-profile-updates-only-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-sms-optin-start
   :end-before: .. setting-listrak-sms-optin-end

.. include:: ../../amperity_operator/source/destination_listrak_sms_profile.rst
   :start-after: .. destination-listrak-sms-profile-context-start
   :end-before: .. destination-listrak-sms-profile-context-end

.. sendto-listrak-sms-profile-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-listrak-sms-profile-build-query>`
#. :ref:`Add orchestration <sendto-listrak-sms-profile-add-orchestration>`
#. :ref:`Run orchestration <sendto-listrak-sms-profile-run-orchestration>`

.. sendto-listrak-sms-profile-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-listrak-sms-profile-build-query:

Build query
==================================================

.. include:: ../../amperity_operator/source/destination_listrak_sms_profile.rst
   :start-after: .. destination-listrak-sms-profile-attributes-start
   :end-before: .. destination-listrak-sms-profile-attributes-end

.. sendto-listrak-sms-profile-build-query-fields-start

An SMS profile in |destination-name| requires only a phone number, but may include all system profile attributes, including email address, first name, last name, postal code, and birthdate. Custom attributes may be included in the query results.

.. important:: Only phone numbers that already exist in |destination-name| will be updated. Phone numbers that do not exist are silently dropped. Use the **SMS Opt Status** table to filter the results to include only customers who have opted in to receiving SMS messaging.

.. sendto-listrak-sms-profile-build-query-fields-end

.. sendto-listrak-sms-profile-build-query-fields-replace-underscores-start

Replace spaces in `custom SMS profile field names <https://help.listrak.com/en/articles/1852936-sms-profile-fields-and-personalization-guide>`__ |ext_link| with underscores in the Amperity SQL query. For example, a custom SMS profile field is named "Loyalty Tier" in |destination-name|. Alias the field name in the query using underscores:

.. code-block:: sql

   current_tier AS Loyalty_Tier

.. sendto-listrak-sms-profile-build-query-fields-replace-underscores-end

.. include:: ../../amperity_operator/source/destination_listrak_sms_profile.rst
   :start-after: .. destination-listrak-sms-profile-howitworks-optin-start
   :end-before: .. destination-listrak-sms-profile-howitworks-optin-end

.. sendto-listrak-sms-profile-build-query-start

**Example query**

.. code-block:: sql
   :linenos:

   WITH sms_opt_status AS (
     SELECT
       so.amperity_id
       ,so.is_sms_opted_in
     FROM SMS_Opt_Status so
   )

   SELECT
     co.phone
     ,co.email AS "Email Address"
     ,co.given_name AS "First Name"
     ,co.surname AS "Last Name"
     ,co.postal AS "Postal Code"
     ,co.birthdate AS "Birthday"
     ,co.current_tier AS Loyalty_Tier
   FROM Customer_360 co
   JOIN sms_opt_status so ON co.amperity_id = so.amperity_id
   WHERE so.is_sms_opted_in = true

.. sendto-listrak-sms-profile-build-query-end

.. include:: ../../amperity_user/source/campaign_listrak_sms_profile.rst
   :start-after: .. channel-listrak-sms-profile-configure-attributes-start
   :end-before: .. channel-listrak-sms-profile-configure-attributes-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-listrak-sms-profile-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-listrak-sms-profile-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
