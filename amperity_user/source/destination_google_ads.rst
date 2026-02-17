.. https://docs.amperity.com/user/


.. |destination-name| replace:: Google Ads
.. |what-send| replace:: customer data
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Google Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Google Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Google Ads

==================================================
Send query results to Google Ads
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-ads-start
   :end-before: .. term-google-ads-end

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-note-start
   :end-before: .. destination-google-ads-api-note-end

.. sendto-google-ads-user-consent-start

.. important:: :ref:`Review the user consent policy <sendto-google-ads-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.

.. sendto-google-ads-user-consent-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

.. sendto-google-ads-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-google-ads-build-query>`
#. :ref:`Add orchestration <sendto-google-ads-add-orchestration>`
#. :ref:`Run orchestration <sendto-google-ads-run-orchestration>`

.. sendto-google-ads-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-google-ads-build-query:

Build query
==================================================

.. sendto-google-ads-build-query-start

You need to build a query that outputs fields that can be mapped to :ref:`Google Ads API matching keys <sendto-google-ads-api-matching>`, one of:

#. :ref:`Contact information, including personally identifiable information (PII) matching <sendto-google-ads-api-matching-contact>`
#. :ref:`Mobile device matching <sendto-google-ads-api-matching-mobile>`
#. :ref:`Advertiser-generated and assigned user ID matching <sendto-google-ads-api-matching-user>`.

.. sendto-google-ads-build-query-end

.. sendto-google-ads-build-query-note-start

.. note:: The Google Ads API has specific requirements. Define a query, and then export it as a CSV file to profile the data.

   * Add and normalize the country code when states are US and Canada, but the country is **NULL**.
   * Phone numbers are required to have a +11231234567 format.
   * First name, last name, ZIP code, and country are all required for the "Contact Info" upload key. If any are missing, none are passed.

.. sendto-google-ads-build-query-note-end

**Example**

.. sendto-google-ads-build-query-example-start

.. code-block:: sql
   :linenos:

   SELECT 
     email AS Email
     ,CONCAT('+',REGEXP_REPLACE(phone, '(\s*)([^a-zA-Z0-9])', '')) AS Phone
     ,surname AS LastName
     ,given_name AS FirstName
     ,postal AS Zip 
     ,country AS Country
   FROM Merged_Customers
   WHERE email IS NOT NULL
   OR phone IS NOT NULL
   OR (given_name IS NOT NULL
       AND surname IS NOT NULL
       AND postal IS NOT NULL
       AND country IS NOT NULL
   )

.. sendto-google-ads-build-query-example-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-google-ads-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-google-ads-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _sendto-google-ads-api-matching:

Google Ads API Matching
==================================================

.. sendto-google-ads-api-matching-start

Google Ads API matching can be done through the following list ID types:

* :ref:`Contact information, including personally identifiable information (PII) matching <sendto-google-ads-api-matching-contact>`
* :ref:`European Union user consent <sendto-google-ads-api-matching-eu-consent>`
* :ref:`Mobile device matching <sendto-google-ads-api-matching-mobile>`
* :ref:`Advertiser-generated and assigned user ID matching <sendto-google-ads-api-matching-user>`

.. sendto-google-ads-api-matching-end


.. _sendto-google-ads-api-matching-contact:

Contact Info Matching
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-contact-list-start
   :end-before: .. destination-google-ads-api-matching-contact-list-end


.. _sendto-google-ads-api-matching-eu-consent:

European Union user consent
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-eu-consent-start
   :end-before: .. destination-google-ads-api-matching-eu-consent-end


.. _sendto-google-ads-api-matching-mobile:

Mobile Device ID Matching
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-mobile-list-start
   :end-before: .. destination-google-ads-api-matching-mobile-list-end


.. _sendto-google-ads-api-matching-user:

User ID Matching
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-user-start
   :end-before: .. destination-google-ads-api-matching-user-end
