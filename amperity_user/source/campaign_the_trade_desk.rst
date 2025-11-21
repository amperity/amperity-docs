.. https://docs.amperity.com/user/


.. |destination-name| replace:: The Trade Desk
.. |what-send| replace:: email address lists
.. |what-enable| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires only email addresses. There are no optional fields.
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to The Trade Desk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to The Trade Desk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to The Trade Desk

==================================================
Send audiences to The Trade Desk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. destination-the-trade-desk-start

Amperity can manage audiences for |destination-name| demand-side platform, from which your brand can reach audiences throughout their entire digital journey and across every channel and device, including:

* Display advertising on ABC, ESPN, the Wall Street Journal, live sporting events (Major League Baseball), in-store advertising at WalMart, and more.
* Video advertising on over-the-top (OTT) and connected TV (CTV) apps and platforms, such as Disney+, Major League Baseball, Hulu, Fox, Vevo, Paramount+, and more.
* Audio advertising in-between songs and during podcasts across Spotify, Pandora, SoundCloud, iHeart, and more.

.. destination-the-trade-desk-start

.. include:: ../../amperity_operator/source/destination_the_trade_desk.rst
   :start-after: .. destination-the-trade-desk-whatis-20-start
   :end-before: .. destination-the-trade-desk-whatis-20-end

.. include:: ../../amperity_operator/source/destination_the_trade_desk.rst
   :start-after: .. destination-the-trade-desk-api-note-start
   :end-before: .. destination-the-trade-desk-api-note-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-the-trade-desk-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end


.. _channel-the-trade-desk-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add The Trade Desk to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-tdd.png
          :width: 500 px
          :alt: Add a destination for The Trade Desk.
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

       .. image:: ../../images/mockup-campaigns-attributes-tdd.png
          :width: 500 px
          :alt: Edit the attributes for The Trade Desk.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end




.. _channel-the-trade-desk-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-the-trade-desk-configure-default-attributes-start

|destination-name| has the following requirements:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email

   * - uid2

       You may use **uid2** as a source attribute when Amperity is configured as a `UID2 Operator <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| for your brand.

     - uid2

   * - euid

       You may use **euid** as a source attribute when your brand is a participant in `European Unified ID (EUID) <https://docs.amperity.com/reference/euid.html>`__ |ext_link|.

     - euid

.. channel-the-trade-desk-configure-default-attributes-end
