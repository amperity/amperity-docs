.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Viant DSP
.. |destination-api| replace:: VDP Connect API
.. |plugin-name| replace:: "Viant DSP"
.. |credential-type| replace:: "viant-dsp"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "identifier"
.. |what-send| replace:: audience segments
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "via"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Viant DSP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Viant DSP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Viant DSP

==================================================
Configure campaigns for Viant DSP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-viant-dsp-start
   :end-before: .. term-viant-dsp-end

.. campaign-viant-dsp-start

Use Amperity to build audience segments and send them to |destination-name| for use in programmatic advertising campaigns. Amperity syncs hashed identifier data, such as emails, phone numbers, IP addresses, mobile device IDs, or cookie IDs, to first-party audience segments in |destination-name|, where they become targetable in DSP campaigns.

.. campaign-viant-dsp-end

.. campaign-viant-dsp-api-note-start

.. note:: This destination uses the `VDP Connect API <https://docs.api.viantinc.com/reference/how-to-get-started>`__ |ext_link|.

.. campaign-viant-dsp-api-note-end


.. _campaign-viant-dsp-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-viant-dsp-get-details-table-start

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
             :start-after: .. credential-viant-dsp-refresh-token-start
             :end-before: .. credential-viant-dsp-refresh-token-end

          .. tip:: Contact your Viant account representative to initiate the OAuth2 authorization flow and obtain a refresh token.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required destination settings**

       **Account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-account-id-start
             :end-before: .. setting-viant-dsp-account-id-end

       **Advertiser ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-advertiser-id-start
             :end-before: .. setting-viant-dsp-advertiser-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required campaign settings**

       **Audience name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-audience-name-start
             :end-before: .. setting-viant-dsp-audience-name-end

       **Identifier type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-identifier-type-start
             :end-before: .. setting-viant-dsp-identifier-type-end

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
     - A segment that returns an **identifier** column containing the identifier values to send to |destination-name|. The identifier type must match the **Identifier type** setting. See `Preparing your user data <https://docs.api.viantinc.com/reference/prepaing-your-user-data>`__ |ext_link| for formatting requirements by identifier type.

.. campaign-viant-dsp-get-details-end


.. _campaign-viant-dsp-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Viant DSP**

.. campaign-viant-dsp-credentials-steps-start

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
             :start-after: .. credential-viant-dsp-refresh-token-start
             :end-before: .. credential-viant-dsp-refresh-token-end

.. campaign-viant-dsp-credentials-steps-end


.. _campaign-viant-dsp-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Viant DSP**

.. campaign-viant-dsp-add-steps-start

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

       **Account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-account-id-start
             :end-before: .. setting-viant-dsp-account-id-end

       **Advertiser ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-advertiser-id-start
             :end-before: .. setting-viant-dsp-advertiser-id-end

       **Audience name** (Required at campaign)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-audience-name-start
             :end-before: .. setting-viant-dsp-audience-name-end

       **Identifier type** (Required at campaign)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-identifier-type-start
             :end-before: .. setting-viant-dsp-identifier-type-end

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

.. campaign-viant-dsp-add-steps-end


.. TODO: Add workflow resolutions from existing topics HERE.
