.. https://docs.amperity.com/ampiq/


.. |destination-name| replace:: DV360
.. |what-send| replace:: customer profiles
.. |what-enable| replace:: **email**, **phone**, **firstname**, **lastname**, **zip**, and **country**
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours
.. |attributes-sent| replace:: |destination-name| accepts any combination of email address, phone number, first name, last name, zip code, and country attributes.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to DV360.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to DV360.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to DV360

==================================================
Send audiences to DV360
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dv360-start
   :end-before: .. term-dv360-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../amperity_operator/source/destination_dv360.rst
   :start-after: .. destination-dv360-api-note-start
   :end-before: .. destination-dv360-api-note-end

.. important:: :ref:`Review the user consent policy <channel-dv360-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end


.. _channel-dv360-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. _attributes:

.. admonition:: Which attributes should you use?

   .. include:: ../../shared/channels.rst
      :start-after: .. channels-build-segment-context-start
      :end-before: .. channels-build-segment-context-end


.. _channel-dv360-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add DV360 to a campaign**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-open-page-start
          :end-before: .. channels-build-campaign-steps-open-page-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-start
          :end-before: .. channels-build-campaign-steps-destinations-end

       .. image:: ../../images/mockup-campaigns-destination-dv360.png
          :width: 500 px
          :alt: Add a destination for DV360.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-note-start
          :end-before: .. channels-build-campaign-steps-destinations-note-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-end

       .. image:: ../../images/mockup-campaigns-attributes-google-customer-match.png
          :width: 500 px
          :alt: Edit the attributes for DV360.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end





.. _channel-dv360-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-dv360-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - EMAIL

   * - phone
     - PHONE

   * - given_name
     - firstname

   * - surname
     - lastname

   * - postal
     - zip

   * - country
     - country

.. channel-dv360-configure-default-attributes-end


.. _channel-dv360-api-matching:

Google Audience Partner API Matching
==================================================

.. channel-dv360-api-matching-start

|destination-name| matching can be done through the following list ID types:

* :ref:`Contact information, including personally identifiable information (PII) matching <channel-dv360-api-matching-contact>`
* :ref:`European Union user consent <channel-dv360-api-matching-eu-consent>`
* :ref:`Mobile device matching <channel-dv360-api-matching-mobile>`

.. channel-dv360-api-matching-end


.. _channel-dv360-api-matching-contact:

Contact Info Matching
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-contact-list-start
   :end-before: .. destination-google-ads-api-matching-contact-list-end


.. _channel-dv360-api-matching-eu-consent:

European Union user consent
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-eu-consent-start
   :end-before: .. destination-google-ads-api-matching-eu-consent-end


.. _channel-dv360-api-matching-mobile:

Mobile Device ID Matching
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-mobile-list-start
   :end-before: .. destination-google-ads-api-matching-mobile-list-end
