.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Reddit Ads
.. |destination-api| replace:: Reddit Ads API
.. |plugin-name| replace:: "Reddit"
.. |credential-type| replace:: "reddit"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audience segments
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "red"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Reddit Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Reddit Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Reddit Ads

==================================================
Configure campaigns for Reddit Ads
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-reddit-ads-start
   :end-before: .. term-reddit-ads-end

.. campaign-reddit-ads-start

Use Amperity to build audience segments and send them to |destination-name| as custom audiences for ad targeting. Amperity normalizes and SHA-256 hashes email addresses before sending them to |destination-name|, where they are matched to Reddit accounts and made available for campaign targeting.

.. campaign-reddit-ads-end

.. campaign-reddit-ads-api-note-start

.. note:: This destination uses the `Reddit Ads API v3 <https://ads-api.reddit.com/docs/v3/>`__ |ext_link|.

.. campaign-reddit-ads-api-note-end


.. _campaign-reddit-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-reddit-ads-get-details-table-start

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
             :start-after: .. credential-reddit-ads-refresh-token-start
             :end-before: .. credential-reddit-ads-refresh-token-end

          .. tip:: Contact your Reddit Ads representative to initiate the OAuth2 authorization flow and obtain a refresh token.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required destination settings**

       **Ad account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-reddit-ads-ad-account-id-start
             :end-before: .. setting-reddit-ads-ad-account-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Optional campaign settings**

       **List name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-reddit-ads-list-name-start
             :end-before: .. setting-reddit-ads-list-name-end

       **Audience primary key**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - A segment that returns an **email** column. Amperity normalizes and hashes email addresses before sending them to |destination-name|.

.. campaign-reddit-ads-get-details-end


.. _campaign-reddit-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Reddit Ads**

.. campaign-reddit-ads-credentials-steps-start

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

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-reddit-ads-refresh-token-start
             :end-before: .. credential-reddit-ads-refresh-token-end

.. campaign-reddit-ads-credentials-steps-end


.. _campaign-reddit-ads-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Reddit Ads**

.. campaign-reddit-ads-add-steps-start

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
          :alt: Add a destination.
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

       **Ad account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-reddit-ads-ad-account-id-start
             :end-before: .. setting-reddit-ads-ad-account-id-end

       **List name** (Optional)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-reddit-ads-list-name-start
             :end-before: .. setting-reddit-ads-list-name-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

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

.. campaign-reddit-ads-add-steps-end


.. TODO: Add workflow resolutions from existing topics HERE.
