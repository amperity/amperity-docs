.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Customer Match
.. |plugin-name| replace:: "Google Customer Match"
.. |credential-type| replace:: "google-customer-match"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "540"
.. |filter-the-list| replace:: "google"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Google Customer Match.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Google Customer Match.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destination for Google Customer Match

==================================================
Configure destination for Google Customer Match
==================================================

.. destination-google-customer-match-start

Use Google Customer Match to create and publish search, display, and video ads across the Google-owned paid media ecosystem.

.. destination-google-customer-match-end


.. _destination-google-customer-match-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-google-customer-match-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for "Google Customer Match" *must* be completed within Google prior to configuring Amperity to send |what-send| to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Customer product**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-customer-product-start
             :end-before: .. setting-google-customer-match-customer-product-end

       **Customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-customer-id-start
             :end-before: .. setting-google-ads-customer-id-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-audience-name-start
             :end-before: .. setting-google-ads-audience-name-end

       **Upload key type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-upload-key-type-start
             :end-before: .. setting-google-ads-upload-key-type-end

.. destination-google-customer-match-get-details-end


.. _destination-google-customer-match-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Google Customer Match**

.. destination-google-customer-match-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-google-customer-match-credentials-steps-end


.. _destination-google-customer-match-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-google-customer-match-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Customer Match**

.. destination-google-customer-match-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
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
          :alt: Step 2.
          :align: left
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
          :alt: Step 3.
          :align: left
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
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Customer product**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-customer-product-start
             :end-before: .. setting-google-customer-match-customer-product-end

       **Customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-customer-id-start
             :end-before: .. setting-google-ads-customer-id-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-audience-name-start
             :end-before: .. setting-google-ads-audience-name-end

       **Audience description** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-audience-description-start
             :end-before: .. setting-google-ads-audience-description-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-start
             :end-before: .. setting-common-membership-duration-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-frequency-start
             :end-before: .. setting-common-membership-duration-frequency-end

       **Upload key type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-upload-key-type-start
             :end-before: .. setting-google-ads-upload-key-type-end

       **Mobile app ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-ads-mobile-app-id-start
             :end-before: .. setting-google-ads-mobile-app-id-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-google-customer-match-add-steps-end
