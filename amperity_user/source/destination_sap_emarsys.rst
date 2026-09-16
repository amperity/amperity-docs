.. https://docs.amperity.com/user/


.. |destination-name| replace:: SAP Emarsys
.. |destination-api| replace:: SAP Emarsys REST API
.. |plugin-name| replace:: emarsys
.. |attributes-sent| replace:: **email** or **phone**, along with optional profile and custom attributes.


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to SAP Emarsys.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to SAP Emarsys.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to SAP Emarsys

==================================================
Send query results to SAP Emarsys
==================================================

.. include:: ../../amperity_operator/source/destination_sap_emarsys.rst
   :start-after: .. destination-sap-emarsys-about-start
   :end-before: .. destination-sap-emarsys-about-end

.. include:: ../../amperity_operator/source/destination_sap_emarsys.rst
   :start-after: .. destination-sap-emarsys-configure-start
   :end-before: .. destination-sap-emarsys-configure-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-sap-emarsys-build-query:

Build query
==================================================

.. sendto-sap-emarsys-build-query-start

Build a query that returns an email address or a phone number, along with up to 400 additional profile attributes.

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-sap-emarsys-attributes-and-fields-start
   :end-before: .. setting-sap-emarsys-attributes-and-fields-end

.. sendto-sap-emarsys-build-query-end

**Example**

.. sendto-sap-emarsys-build-query-example-start

The following query returns an audience with profile attributes mapped to system fields in |destination-name| and a custom field named **external_id** for the Amperity ID. The **WHERE** clause ensures that only records with an email address are part of the audience.

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS 'external_id'
     ,given_name AS 'first_name'
     ,surname AS 'last_name'
     ,email AS 'email'
     ,phone AS 'phone'
     ,address AS 'address'
     ,city AS 'city'
     ,state AS 'state'
     ,postal AS 'zip_code'
     ,country AS 'country'
     ,birthdate AS 'birth_date'
   FROM Merged_Customers mc
   WHERE (
     LOWER(mc.email) IS NOT NULL
   )

.. sendto-sap-emarsys-build-query-example-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-sap-emarsys-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-sap-emarsys-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
