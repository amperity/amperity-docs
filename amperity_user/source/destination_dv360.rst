.. https://docs.amperity.com/user/


.. |destination-name| replace:: DV360
.. |what-send| replace:: customer data
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to DV360.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to DV360.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to DV360

==================================================
Send query results to DV360
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dv360-start
   :end-before: .. term-dv360-end

.. include:: ../../amperity_operator/source/destination_dv360.rst
   :start-after: .. destination-dv360-api-note-start
   :end-before: .. destination-dv360-api-note-end

.. important:: :ref:`Review the user consent policy <sendto-dv360-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.

.. destination-dv360-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <destination-dv360-build-query>`
#. :ref:`Add orchestration <destination-dv360-add-orchestration>`
#. :ref:`Run orchestration <destination-dv360-run-orchestration>`

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _destination-dv360-build-query:

Build query
==================================================

.. destination-dv360-build-query-start

You will need to build a query that outputs fields that can be mapped to :ref:`Google Audience Partner API matching keys <sendto-dv360-api-matching>`, one of:

#. :ref:`Contact information, including personally identifiable information (PII) matching <sendto-dv360-api-matching-contact>`
#. :ref:`Mobile device matching <sendto-dv360-api-matching-mobile>`

.. destination-dv360-build-query-end

.. destination-dv360-build-query-note-start

.. note:: |destination-name| has specific requirements. Define a query, and then export it as a CSV file to profile the data.

   * Add and normalize the country code when states are US and Canada, but the country is NULL.
   * Phone numbers are required to have a +11231234567 format.
   * First name, last name, zip code, and country are all required for the "Contact Info" upload key. If any are missing, none are passed.

.. destination-dv360-build-query-note-end

**Example**

.. destination-dv360-build-query-example-start

.. code-block:: sql
   :linenos:

   SELECT 
     Email AS email, 
     concat('+',regexp_replace(Phone, '(\s*)([^a-zA-Z0-9])', '')) AS phone, 
     LastName AS lastname, 
     FirstName AS firstname, 
     PostalCode AS zip, 
     'US' AS country
   FROM Customer360

   WHERE 
     email IS NOT NULL AND
     Phone IS NOT NULL AND
     FirstName IS NOT NULL AND
     LastName IS NOT NULL AND
     PostalCode IS NOT NULL

   LIMIT 1000

.. destination-dv360-build-query-example-end


.. _destination-dv360-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _destination-dv360-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _sendto-dv360-api-matching:

Google Audience Partner API Matching
==================================================

.. destination-dv360-api-matching-start

|destination-name| matching can be done through the following list ID types:

* :ref:`Contact information, including personally identifiable information (PII) matching <sendto-dv360-api-matching-contact>`
* :ref:`European Union user consent <sendto-dv360-api-matching-eu-consent>`
* :ref:`Mobile device matching <sendto-dv360-api-matching-mobile>`

.. destination-dv360-api-matching-end


.. _sendto-dv360-api-matching-contact:

Contact Info Matching
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-contact-list-start
   :end-before: .. destination-google-ads-api-matching-contact-list-end


.. _sendto-dv360-api-matching-eu-consent:

European Union user consent
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-eu-consent-start
   :end-before: .. destination-google-ads-api-matching-eu-consent-end


.. _sendto-dv360-api-matching-mobile:

Mobile Device ID Matching
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-mobile-list-start
   :end-before: .. destination-google-ads-api-matching-mobile-list-end
