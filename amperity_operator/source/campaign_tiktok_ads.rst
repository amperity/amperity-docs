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
        Configure Amperity to send campaigns to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to TikTok Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for TikTok Ads

==================================================
Configure campaigns for TikTok Ads
==================================================

.. campaign-tiktok-ads-custom-audiences-start

Custom audiences help find people who already know about or have engaged with your brand. Use custom audiences for re-marketing, finding potential repeat customers, and finding lookalike audiences.

.. campaign-tiktok-ads-custom-audiences-end

.. campaign-tiktok-ads-custom-audiences-size-start

.. important:: A custom audience must have at least 1000 members in |destination-name| before it can be used in an ad group.

.. campaign-tiktok-ads-custom-audiences-size-end

.. TODO: Sync following with ampiq/destination_tiktok_ads

.. campaign-tiktok-ads-important-one-time-delivery-start

.. caution:: To refresh audiences from Amperity, new one-time segment deliveries need to be created and uploaded to the client's |destination-name| account.

.. campaign-tiktok-ads-important-one-time-delivery-end

.. campaign-tiktok-ads-api-note-start

.. note:: Amperity uses a combination of endpoints in the |destination-name| Segment API to `verify existing segments <https://ads.tiktok.com/marketing_api/docs?id=1708578418908161>`__ |ext_link|, `add or update <https://ads.tiktok.com/marketing_api/docs?id=1735136750113793>`__ |ext_link| the list of customers to match the list of customers sent from Amperity, and then `map multiple advertising account IDs to the same business account <https://ads.tiktok.com/marketing_api/docs?id=1735141667215361>`__ |ext_link|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. campaign-tiktok-ads-api-note-end


.. _campaign-tiktok-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-tiktok-ads-get-details-table-start

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

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-tiktok-ads-manager-oauth-requirements-start
             :end-before: .. credential-tiktok-ads-manager-oauth-requirements-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
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

.. campaign-tiktok-ads-get-details-end


.. _campaign-tiktok-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. campaign-tiktok-ads-configure-oauth-important-start

.. important:: TikTok Advertiser Accounts are required to use OAuth. Confirm that the account that is used to authorize to |destination-name| has the **TikTok Ad Account Operator** or **TikTok Ad Account Admin** permission level. OAuth will not work if your account has **TikTok Ad Account Analyst** permission.

.. campaign-tiktok-ads-configure-oauth-important-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for TikTok Ads Manager**

.. campaign-tiktok-ads-credentials-steps-start

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

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-tiktok-ads-manager-oauth-requirements-start
             :end-before: .. credential-tiktok-ads-manager-oauth-requirements-end

.. campaign-tiktok-ads-credentials-steps-end


.. _campaign-tiktok-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _campaign-tiktok-ads-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for TikTok Ads Manager**

.. campaign-tiktok-ads-add-steps-start

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

.. campaign-tiktok-ads-add-steps-end


.. _campaign-tiktok-ads-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. campaign-tiktok-ads-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

       .. image:: ../../images/mockup-destinations-tab-workflow-error.png
          :width: 500 px
          :alt: Review a notifications error.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-b-start
          :end-before: .. workflow-actions-common-table-section-one-b-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-two-start
          :end-before: .. workflow-actions-common-table-section-two-end

       .. image:: ../../images/mockups-workflow-failed.png
          :width: 500 px
          :alt: The workflow tab, showing a workflow with errors.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-a-start
          :end-before: .. workflow-actions-common-table-section-three-a-end

       .. image:: ../../images/workflow-actions-tiktok-ads-advertiser-not-found.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-tiktok-ads-workflow-actions-advertiser-not-found`
       * :ref:`destination-tiktok-ads-workflow-actions-invalid-credentials`
       * :ref:`destination-tiktok-ads-workflow-actions-missing-advertiser-permissions`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-tiktok-ads-advertiser-not-found-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. campaign-tiktok-ads-workflow-actions-end


.. _campaign-tiktok-ads-workflow-actions-advertiser-not-found:

Advertiser not found
--------------------------------------------------

.. campaign-tiktok-ads-workflow-actions-advertiser-not-found-start

Amperity may only send data to an advertiser account ID that already exists within |destination-name|. When Amperity cannot find the advertiser account ID within |destination-name|, this may be due to any of the following:

#. An Amperity configuration issue related to the destination *or* the data template that is associated with that destination.
#. An advertiser account ID that is not associated with an approved advertising account in |destination-name|.

.. campaign-tiktok-ads-workflow-actions-advertiser-not-found-end

.. campaign-tiktok-ads-workflow-actions-advertiser-not-found-steps-start

To resolve this error, determine the cause of the configuration issue.

#. Open the Amperity **Destinations** page in a new browser tab.

   Review the configuration for the destination and data template that is associated with this workflow.
#. Open `TikTok Business Center <https://business.tiktok.com/>`__ |ext_link| and verify that the advertising account exists, is approved, and has a valid advertiser account ID.
#. Update the configuration for Amperity to match the correct advertiser account ID.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-tiktok-ads-workflow-actions-advertiser-not-found-steps-start


.. _campaign-tiktok-ads-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _campaign-tiktok-ads-workflow-actions-missing-advertiser-permissions:

Missing advertiser permissions
--------------------------------------------------

.. campaign-tiktok-ads-workflow-actions-missing-advertiser-permissions-start

The business user that is associated with your |destination-name| account is the same business user that provides credentials for Amperity to manage audiences in |destination-name|.

This business user *must* have permission to manage audiences, which requires that business user to be assigned to one of the following roles:

* Admin
* Operator (recommended)

.. campaign-tiktok-ads-workflow-actions-missing-advertiser-permissions-end

.. campaign-tiktok-ads-workflow-actions-missing-advertiser-permissions-steps-start

To resolve this error, verify that the business user is assigned to the **Operator** role.

#. Open `TikTok Business Center <https://business.tiktok.com/>`__ |ext_link|.

   Verify the role to which the business user that provides credentials for Amperity is assigned. The business user must be assigned to the **Operator** role.
#. Open the Amperity **Credentials** page in a new tab, and regenerate the authorization link for the business user who is assigned to the **Operator** role.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-tiktok-ads-workflow-actions-missing-advertiser-permissions-steps-start
