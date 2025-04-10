.. https://docs.amperity.com/operator/



.. |destination-name| replace:: TikTok Ads
.. |plugin-name| replace:: "TikTok Ads"
.. |credential-type| replace:: "tiktok"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "tik"
.. |allow-for-what| replace:: audience mapping
.. |allow-for-duration| replace:: up to 10 hours


.. meta::
    :description lang=en:
        Configure Amperity to send email lists to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send email lists to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send email lists to TikTok Ads

==================================================
Send email lists to TikTok Ads
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_tiktok_ads.html>`__ |ext_link|.

.. destination-tiktok-ads-custom-audiences-start

Custom audiences help find people who already know about or have engaged with your brand. Use custom audiences for re-marketing, finding potential repeat customers, and finding lookalike audiences.

.. destination-tiktok-ads-custom-audiences-end

.. destination-tiktok-ads-custom-audiences-size-start

.. important:: A custom audience must have at least 1000 members in |destination-name| before it can be used in an ad group.

.. destination-tiktok-ads-custom-audiences-size-end

.. TODO: Sync following with ampiq/destination_tiktok_ads

.. destination-tiktok-ads-important-one-time-delivery-start

.. caution:: To refresh audiences from Amperity, new one-time segment deliveries need to be created and uploaded to the client's |destination-name| account.

.. destination-tiktok-ads-important-one-time-delivery-end

.. destination-tiktok-ads-api-note-start

.. note:: Amperity uses a combination of endpoints in the |destination-name| Segment API to `verify existing segments <https://ads.tiktok.com/marketing_api/docs?id=1708578418908161>`__ |ext_link|, `add or update <https://ads.tiktok.com/marketing_api/docs?id=1735136750113793>`__ |ext_link| the list of customers to match the list of customers sent from Amperity, and then `map multiple advertising account IDs to the same business account <https://ads.tiktok.com/marketing_api/docs?id=1735141667215361>`__ |ext_link|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-tiktok-ads-api-note-end


.. _destination-tiktok-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-tiktok-ads-get-details-table-start

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
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-tiktok-ads-manager-oauth-requirements-start
             :end-before: .. credential-tiktok-ads-manager-oauth-requirements-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Advertiser ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-advertiser-id-start
             :end-before: .. setting-tiktok-ads-manager-advertiser-id-end

       **Audience name**
          |checkmark-required| **Required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-custom-audience-name-start
             :end-before: .. setting-tiktok-ads-manager-custom-audience-name-end

       **User ID type**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-user-id-type-start
             :end-before: .. setting-tiktok-ads-manager-user-id-type-end

.. destination-tiktok-ads-get-details-end


.. _destination-tiktok-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. destination-tiktok-ads-configure-oauth-important-start

.. important:: TikTok Advertiser Accounts are required to use OAuth. Confirm that the account that will be used to authorize to |destination-name| has the **TikTok Ad Account Operator** or **TikTok Ad Account Admin** permission level. OAuth will not work if your account has **TikTok Ad Account Analyst** permission.

.. destination-tiktok-ads-configure-oauth-important-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for TikTok Ads Manager**

.. destination-tiktok-ads-credentials-steps-start

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
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-tiktok-ads-manager-oauth-requirements-start
             :end-before: .. credential-tiktok-ads-manager-oauth-requirements-end

.. destination-tiktok-ads-credentials-steps-end


.. _destination-tiktok-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-tiktok-ads-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for TikTok Ads Manager**

.. destination-tiktok-ads-add-steps-start

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

       **Advertiser ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-advertiser-id-start
             :end-before: .. setting-tiktok-ads-manager-advertiser-id-end

       **Audience name**
          |checkmark-required| **Required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-custom-audience-name-start
             :end-before: .. setting-tiktok-ads-manager-custom-audience-name-end

       **User ID type**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-tiktok-ads-manager-user-id-type-start
             :end-before: .. setting-tiktok-ads-manager-user-id-type-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-tiktok-ads-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
