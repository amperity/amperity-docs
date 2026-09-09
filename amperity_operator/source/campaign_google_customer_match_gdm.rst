.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Customer Match (GDM)
.. |destination-api| replace:: Google Data Manager API
.. |plugin-name| replace:: "Google Customer Match (GDM)"
.. |credential-type| replace:: "google-customer-match-gdm"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "google"
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "540"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Google Customer Match (GDM).

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Google Customer Match (GDM).

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Google Customer Match (GDM)

======================================================================
Configure campaigns for Google Customer Match (GDM)
======================================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-customer-match-gdm-start
   :end-before: .. term-google-customer-match-gdm-end

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-beta-start
   :end-before: .. destination-google-customer-match-gdm-beta-end

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-start
   :end-before: .. destination-google-customer-match-gdm-end

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-api-note-start
   :end-before: .. destination-google-customer-match-gdm-api-note-end

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-behavior-start
   :end-before: .. destination-google-customer-match-gdm-behavior-end


.. _campaign-google-customer-match-gdm-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-google-customer-match-gdm-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for |destination-name| *must* be completed within Google, using the **Connect with Google** sign-in flow, before configuring Amperity to send |what-send| to |where-send|. During sign-in, approve access to Google's Data Manager service.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Customer product**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-customer-product-start
             :end-before: .. setting-google-customer-match-gdm-customer-product-end

       **Customer ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-customer-id-start
             :end-before: .. setting-google-customer-match-gdm-customer-id-end

       **Match identifier**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-match-identifier-start
             :end-before: .. setting-google-customer-match-gdm-match-identifier-end

       **Audience name** (Required at campaign)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-audience-name-start
             :end-before: .. setting-google-customer-match-gdm-audience-name-end

.. campaign-google-customer-match-gdm-get-details-end


.. _campaign-google-customer-match-gdm-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Google Customer Match (GDM)**

.. campaign-google-customer-match-gdm-credentials-steps-start

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

       .. note:: Amperity provides two Google Customer Match connectors. Select |plugin-name| to sync audiences over Google's Data Manager platform. **Google Customer Match** is the separate connector that uses the older Audience Partner API.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. campaign-google-customer-match-gdm-credentials-steps-end


.. _campaign-google-customer-match-gdm-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Customer Match (GDM)**

.. campaign-google-customer-match-gdm-add-steps-start

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

       **Customer product**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-customer-product-start
             :end-before: .. setting-google-customer-match-gdm-customer-product-end

       **Customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-customer-id-start
             :end-before: .. setting-google-customer-match-gdm-customer-id-end

       **Match identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-match-identifier-start
             :end-before: .. setting-google-customer-match-gdm-match-identifier-end

       **Audience name** (Required at campaign)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-audience-name-start
             :end-before: .. setting-google-customer-match-gdm-audience-name-end

       **Audience description**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-audience-description-start
             :end-before: .. setting-google-customer-match-gdm-audience-description-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-start
             :end-before: .. setting-common-membership-duration-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-frequency-start
             :end-before: .. setting-common-membership-duration-frequency-end

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

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. campaign-google-customer-match-gdm-add-steps-end
