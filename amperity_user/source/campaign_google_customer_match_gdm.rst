.. https://docs.amperity.com/user/


.. |destination-name| replace:: Google Customer Match (GDM)
.. |what-send| replace:: audiences
.. |attributes-sent| replace:: an email address, a phone number, or a mobile advertising ID


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Google Customer Match (GDM).

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Google Customer Match (GDM).

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Google Customer Match (GDM)

==================================================
Send audiences to Google Customer Match (GDM)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-customer-match-gdm-start
   :end-before: .. term-google-customer-match-gdm-end

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-api-note-start
   :end-before: .. destination-google-customer-match-gdm-api-note-end

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-behavior-start
   :end-before: .. destination-google-customer-match-gdm-behavior-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end

.. _channel-google-customer-match-gdm-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. admonition:: About segments that use the sub-audience editor

   .. include:: ../../shared/channels.rst
      :start-after: .. channels-build-segment-context-start
      :end-before: .. channels-build-segment-context-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _channel-google-customer-match-gdm-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. channel-google-customer-match-gdm-build-campaign-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-open-page-start
          :end-before: .. channels-build-campaign-steps-open-page-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-start
          :end-before: .. channels-build-campaign-steps-destinations-end

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-note-start
          :end-before: .. channels-build-campaign-steps-destinations-note-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-end

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end

.. channel-google-customer-match-gdm-build-campaign-steps-end


.. _channel-google-customer-match-gdm-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-google-customer-match-gdm-configure-default-attributes-start

|destination-name| matches members on a single identifier — the **Match identifier** configured on the destination. Map the source attribute that matches that identifier. Return only that attribute; Amperity rejects a dataset that contains attributes it does not recognize.

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Source attribute
     - Required?
     - Destination attribute
   * - **email**
     - Depends
     - An email address. Map this attribute when the destination's **Match identifier** is **email**. Amperity applies SHA-256 hashing before sending.
   * - **phone**
     - Depends
     - A phone number. Map this attribute when the destination's **Match identifier** is **phone**. Amperity converts the number to E.164 format and applies SHA-256 hashing before sending.
   * - **mobile-id**
     - Depends
     - A mobile advertising ID. Map this attribute when the destination's **Match identifier** is **mobile-id**. Sent as-is, because Google does not accept mobile advertising IDs hashed.

.. channel-google-customer-match-gdm-configure-default-attributes-end
