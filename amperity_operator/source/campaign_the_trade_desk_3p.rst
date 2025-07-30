.. https://docs.amperity.com/operator/


.. |destination-name| replace:: The Trade Desk 3rd-party Marketplace
.. |plugin-name| replace:: "The Trade Desk 3rd-party Marketplace"
.. |credential-type| replace:: "tradedesk-3rd-party"
.. |required-credentials| replace:: "advertiser ID", "advertiser secret", "provider ID", and "platform API token"
.. |what-send| replace:: email addresses, EUID, or UID2 tokens
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "180"
.. |filter-the-list| replace:: "trade"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours

.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to The Trade Desk 3rd-party Marketplace.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to The Trade Desk 3rd-party Marketplace.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for The Trade Desk 3rd-party Marketplace

==============================================================
Configure campaigns for The Trade Desk 3rd-party Marketplace
==============================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. campaign-the-trade-desk-3p-about-start

Use this destination to monetize your brand's UID 2.0-based audiences by making them available to advertisers for more granular targeting.

.. campaign-the-trade-desk-3p-about-end


.. _campaign-the-trade-desk-3p-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-the-trade-desk-3p-get-details-table-start

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

       **Provider ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-provider-id-start
             :end-before: .. credential-the-trade-desk-provider-id-end

       **Platform API token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-platform-api-token-start
             :end-before: .. credential-the-trade-desk-platform-api-token-end

.. campaign-the-trade-desk-3p-get-details-end


.. _campaign-the-trade-desk-3p-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for The Trade Desk 3rd-party**

.. campaign-the-trade-desk-3p-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
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

       **Provider ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-provider-id-start
             :end-before: .. credential-the-trade-desk-provider-id-end

       **Platform API token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-platform-api-token-start
             :end-before: .. credential-the-trade-desk-platform-api-token-end

.. campaign-the-trade-desk-3p-credentials-steps-end


.. _campaign-the-trade-desk-3p-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for The Trade Desk 3rd-party**

.. campaign-the-trade-desk-3p-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
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
          :alt: Step 2.
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
          :alt: Step 3.
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
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

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

       **Segment taxonomy ID** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-3p-segment-taxonomy-id-start
             :end-before: .. setting-the-trade-desk-3p-segment-taxonomy-id-end


       **Campaign file settings**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

.. campaign-the-trade-desk-3p-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
