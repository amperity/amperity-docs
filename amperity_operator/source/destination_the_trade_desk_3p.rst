.. https://docs.amperity.com/operator/

:orphan:

.. |destination-name| replace:: The Trade Desk 3P Marketplace
.. |plugin-name| replace:: "The Trade Desk 3P Marketplace"
.. |credential-type| replace:: "tradedesk-3rd-party"
.. |required-credentials| replace:: "brand ID", "platform API token", "provider ID", "provider secret", "UID2 key", and "UID2 secret"
.. |what-send| replace:: email addresses, phone numbers, EUID, or UID2 tokens
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "180"
.. |filter-the-list| replace:: "trade"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours

.. meta::
    :description lang=en:
        Configure Amperity to send audiences to The Trade Desk 3P Marketplace.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to The Trade Desk 3P Marketplace.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for The Trade Desk 3P Marketplace

=================================================================
Configure destinations for The Trade Desk 3P Marketplace
=================================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. destination-the-trade-desk-3p-about-start

Use this destination to monetize your brand's UID 2.0-based audiences by making them available to advertisers for more granular targeting.

.. destination-the-trade-desk-3p-about-end


.. _destination-the-trade-desk-3p-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-the-trade-desk-3p-get-details-table-start

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

       **Brand ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-brand-id-start
             :end-before: .. credential-the-trade-desk-marketplace-brand-id-end

       **Platform API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-platform-api-token-start
             :end-before: .. credential-the-trade-desk-marketplace-platform-api-token-end

       **Provider ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-provider-id-start
             :end-before: .. credential-the-trade-desk-marketplace-provider-id-end

       **Provider secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-provider-secret-start
             :end-before: .. credential-the-trade-desk-marketplace-provider-secret-end

       **UID2 Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-uid2-key-start
             :end-before: .. credential-the-trade-desk-marketplace-uid2-key-end

       **UID2 Secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-uid2-secret-start
             :end-before: .. credential-the-trade-desk-marketplace-uid2-secret-end

.. destination-the-trade-desk-3p-get-details-end


.. _destination-the-trade-desk-3p-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for The Trade Desk 3P**

.. destination-the-trade-desk-3p-credentials-steps-start

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

       **Brand ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-brand-id-start
             :end-before: .. credential-the-trade-desk-marketplace-brand-id-end

       **Platform API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-platform-api-token-start
             :end-before: .. credential-the-trade-desk-marketplace-platform-api-token-end

       **Provider ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-provider-id-start
             :end-before: .. credential-the-trade-desk-marketplace-provider-id-end

       **Provider secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-provider-secret-start
             :end-before: .. credential-the-trade-desk-marketplace-provider-secret-end

       **UID2 Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-uid2-key-start
             :end-before: .. credential-the-trade-desk-marketplace-uid2-key-end

       **UID2 Secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-uid2-secret-start
             :end-before: .. credential-the-trade-desk-marketplace-uid2-secret-end

.. destination-the-trade-desk-3p-credentials-steps-end


.. _destination-the-trade-desk-3p-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for The Trade Desk 3P**

.. destination-the-trade-desk-3p-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

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
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Segment type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-3p-segment-type-start
             :end-before: .. setting-the-trade-desk-3p-segment-type-end

       **Display name**

          |checkmark-required| **Required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-3p-display-name-start
             :end-before: .. setting-the-trade-desk-3p-display-name-end

       **Segment taxonomy ID**

          |checkmark-required| **Required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-3p-segment-taxonomy-id-start
             :end-before: .. setting-the-trade-desk-3p-segment-taxonomy-id-end

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

       **Buyable**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-3p-buyable-start
             :end-before: .. setting-the-trade-desk-3p-buyable-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. destination-the-trade-desk-3p-add-steps-end
