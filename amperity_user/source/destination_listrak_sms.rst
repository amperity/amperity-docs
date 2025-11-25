.. https://docs.amperity.com/user/


.. |destination-name| replace:: Listrak SMS
.. |what-send| replace:: SMS profiles
.. |what-enable| replace:: **phone**
.. |attributes-sent| replace:: |destination-name| requires phone numbers. You may include system and custom profile attributes.


.. meta::
    :description lang=en:
        Use orchestrations to send SMS profiles to Listrak SMS.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send SMS profiles to Listrak SMS.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Listrak SMS

==================================================
Send query results to Listrak SMS
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

.. sendto-listrak-sms-build-query-start

An SMS profile in |destination-name| requires only a phone number, but should include all system profile fields, along with any custom profile fields your brand is using for segmentation in |destination-name|.

For example:

.. code-block:: sql
   :linenos:

   SELECT
     phone AS "Phone"
     ,email AS "Email Address"
     ,given_name AS "First Name"
     ,surname AS "Last Name"
     ,postal AS "Postal Code"
     ,birthdate AS "Birthday"
     ,custom_field_1 AS "Custom Profile Field 1"
     ,custom_field_2 AS "Custom Profile Field 2"
   FROM Customer360

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
