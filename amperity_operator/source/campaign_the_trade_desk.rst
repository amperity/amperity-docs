.. https://docs.amperity.com/operator/


.. |destination-name| replace:: The Trade Desk
.. |destination-api| replace:: The Trade Desk API
.. |plugin-name| replace:: "The Trade Desk"
.. |credential-type| replace:: "tradedesk"
.. |required-credentials| replace:: "advertiser ID" and "advertiser secret"
.. |what-send| replace:: email addresses, EUID, or UID2 tokens
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "180"
.. |filter-the-list| replace:: "trade"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours

.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to The Trade Desk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to The Trade Desk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for The Trade Desk

==================================================
Configure campaigns for The Trade Desk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. campaign-the-trade-desk-about-start

Amperity can manage audiences within |destination-name| demand-side platform, from which your brand can reach those audiences throughout their entire digital journey and across every channel and device, including:

* Display advertising on ABC, ESPN, the Wall Street Journal, live sporting events like Major League Baseball, in-store advertising at WalMart, and more.
* Video advertising on over-the-top (OTT) and connected TV (CTV) apps and platforms, such as Disney+, Major League Baseball, Hulu, Fox, Vevo, Paramount+, and more.
* Audio advertising in-between songs and during podcasts across Spotify, Pandora, SoundCloud, iHeart, and more.

.. campaign-the-trade-desk-about-end

.. TODO: Single-source these following two sections across all The Trade Desk destinations.

.. campaign-the-trade-desk-whatis-20-start

.. admonition:: What is UID 2.0?

   .. include:: ../../shared/terms.rst
      :start-after: .. term-unified-id-20-start
      :end-before: .. term-unified-id-20-end

   |destination-name| supports using `UID 2.0 <https://unifiedid.com/docs/intro>`__ |ext_link| to help establish your customers' identifies without using third-party data. UID 2.0 enables publisher websites, mobile apps, and Connected TV (CTV) apps to monetize through programmatic workflows, while offering user transparency and privacy controls that meet local market requirements.

.. campaign-the-trade-desk-whatis-20-end

.. campaign-the-trade-desk-api-note-start

.. note:: This destination uses the `The Trade Desk API <https://api.thetradedesk.com/v3/portal/data/doc/UnifiedIDs>`__ |ext_link| to manage audiences and send events.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. campaign-the-trade-desk-api-note-end


.. _campaign-the-trade-desk-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-the-trade-desk-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - A `UID 2.0 agreement <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| and / or a `European Unified ID (EUID) agreement <https://docs.amperity.com/reference/euid.html>`__ |ext_link|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Advertiser ID**

          |checkmark-required| **Required**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-advertiser-id-start
          :end-before: .. credential-the-trade-desk-advertiser-id-end

       **Advertiser secret**

          |checkmark-required| **Required**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-advertiser-secret-start
          :end-before: .. credential-the-trade-desk-advertiser-secret-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-find-id-and-secret-start
          :end-before: .. credential-the-trade-desk-find-id-and-secret-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Segment name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-segment-name-start
             :end-before: .. setting-the-trade-desk-segment-name-end

.. campaign-the-trade-desk-get-details-end


.. _campaign-the-trade-desk-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for The Trade Desk**

.. campaign-the-trade-desk-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Advertiser ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-advertiser-id-start
             :end-before: .. credential-the-trade-desk-advertiser-id-end

       **Advertiser secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-advertiser-secret-start
             :end-before: .. credential-the-trade-desk-advertiser-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-find-id-and-secret-start
             :end-before: .. credential-the-trade-desk-find-id-and-secret-end

.. campaign-the-trade-desk-credentials-steps-end


.. _campaign-the-trade-desk-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for The Trade Desk**

.. campaign-the-trade-desk-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-select-credential-start
          :end-before: .. campaigns-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-test-connection-start
             :end-before: .. campaigns-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Segment name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-segment-name-start
             :end-before: .. setting-the-trade-desk-segment-name-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-start
             :end-before: .. setting-common-membership-duration-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-membership-duration-minmax-start
             :end-before: .. setting-the-trade-desk-membership-duration-minmax-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-membership-duration-example-start
             :end-before: .. setting-the-trade-desk-membership-duration-example-end


       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

.. campaign-the-trade-desk-add-steps-end
