.. https://docs.amperity.com/user/


.. |destination-name| replace:: Google Ads
.. |what-send| replace:: customer profiles
.. |what-enable| replace:: **email**, **phone**, **firstname**, **lastname**, **zip**, and **country**
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours
.. |attributes-sent| replace:: |destination-name| accepts any combination of email address, phone number, first name, last name, zip code, and country attributes.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Google Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Google Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Google Ads

==================================================
Send audiences to Google Ads
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-ads-start
   :end-before: .. term-google-ads-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-note-start
   :end-before: .. destination-google-ads-api-note-end

.. important:: :ref:`Review the user consent policy <channel-google-ads-api-matching-eu-consent>` for the European Union (EU) and European Economic Area (EEA), and then add the required columns to your orchestration or campaign.

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-google-ads-build-segment:

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


.. _channel-google-ads-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add Google Ads to a campaign**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-open-page-start
          :end-before: .. channels-build-campaign-steps-open-page-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-start
          :end-before: .. channels-build-campaign-steps-destinations-end

       .. image:: ../../images/mockup-campaigns-destination-google-ads.png
          :width: 500 px
          :alt: Add a destination for Google Ads.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-note-start
          :end-before: .. channels-build-campaign-steps-destinations-note-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-end

       .. image:: ../../images/mockup-campaigns-attributes-google-ads.png
          :width: 500 px
          :alt: Edit the attributes for Google Ads.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end





.. _channel-google-ads-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-google-ads-configure-default-attributes-start

|destination-name| has the following requirements:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email

   * - phone
     - phone

   * - given_name
     - firstname

   * - surname
     - lastname

   * - postal
     - zip

   * - country
     - country

.. channel-google-ads-configure-default-attributes-end


.. _channel-google-ads-api-matching:

Google Ads API Matching
==================================================

.. channel-google-ads-api-matching-start

Google Ads API matching can be done through the following list ID types:

* :ref:`Contact information, including personally identifiable information (PII) matching <channel-google-ads-api-matching-contact>`
* :ref:`European Union user consent <channel-google-ads-api-matching-eu-consent>`
* :ref:`Mobile device matching <channel-google-ads-api-matching-mobile>`
* :ref:`Advertiser-generated and assigned user ID matching <channel-google-ads-api-matching-user>`

.. channel-google-ads-api-matching-end


.. _channel-google-ads-api-matching-contact:

Contact Info Matching
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-contact-list-start
   :end-before: .. destination-google-ads-api-matching-contact-list-end


.. _channel-google-ads-api-matching-eu-consent:

European Union user consent
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-eu-consent-start
   :end-before: .. destination-google-ads-api-matching-eu-consent-end


.. _channel-google-ads-api-matching-mobile:

Mobile Device ID Matching
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-mobile-list-start
   :end-before: .. destination-google-ads-api-matching-mobile-list-end


.. _channel-google-ads-api-matching-user:

User ID Matching
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_google_ads.rst
   :start-after: .. destination-google-ads-api-matching-user-start
   :end-before: .. destination-google-ads-api-matching-user-end