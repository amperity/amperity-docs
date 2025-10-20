.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Attentive
.. |destination-api| replace:: Custom Attributes API
.. |plugin-name| replace:: "attentive-api"
.. |credential-type| replace:: "Custom Attributes API"
.. |required-credentials| replace:: "API key"
.. |audience-primary-key| replace:: "email" or "phone"
.. |what-send| replace:: custom attributes
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "att"
.. |allow-for-what| replace:: custom attributes
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Configure Amperity to use campaigns to send customer attributes to Attentive.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to use campaigns to send customer attributes to Attentive.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Attentive (attributes)

==================================================
Configure campaigns for Attentive (attributes)
==================================================

.. campaign-attentive-mobile-api-attributes-start

|destination-name| is your source of truth for your customers' subscription status, while Amperity is your source of truth for profile attributes that describe those customers.

Amperity uses the `Subscriptions <https://docs.attentive.com/openapi/reference/tag/Subscribers/>`__ |ext_link| and `Custom Attributes <https://docs.attentivemobile.com/openapi/reference/tag/Custom-Attributes/>`__ |ext_link| endpoints to send custom profile attributes to |destination-name|. Use these attributes to apply customizable data or characteristics to each of your subscribers, and then use that information to build segments for use with campaigns and journeys.

.. campaign-attentive-mobile-api-attributes-end

.. include:: ../../amperity_operator/source/destination_attentive_mobile_api.rst
   :start-after: .. destination-attentive-mobile-api-attributes-caution-start
   :end-before: .. destination-attentive-mobile-api-attributes-caution-end

.. include:: ../../amperity_operator/source/destination_attentive_mobile_api.rst
   :start-after: .. destination-attentive-mobile-api-attributes-important-start
   :end-before: .. destination-attentive-mobile-api-attributes-important-end

.. campaign-attentive-sftp-and-api-start

.. admonition:: Why are there two ways to send data to Attentive?

   Amperity uses the `subscriber segment upload <https://docs.attentivemobile.com/pages/developer-guides/sftp-solution/subscriber-segment-upload/#subscriber-segment-upload>`__ |ext_link| process to manage segments. This process does not use an endpoint and is not subject to `Attentive API rate limits <https://docs.attentive.com/pages/api-rate-limits/>`__ |ext_link|. Updates appear on the **Segments** page within your audience in |destination-name|.

.. campaign-attentive-sftp-and-api-end


.. _campaign-attentive-api-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-attentive-api-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-attentive-api-key-start
             :end-before: .. credential-attentive-api-key-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Primary identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-attentive-primary-identifier-start
             :end-before: .. setting-attentive-primary-identifier-end

          .. important:: 

             .. include:: ../../shared/destination_settings.rst
                :start-after: .. setting-attentive-primary-identifier-context-start
                :end-before: .. setting-attentive-primary-identifier-context-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Sign-up units**

       The ID for the `sign-up unit <https://help.attentivemobile.com/hc/en-us/articles/360051443552-What-are-sign-up-units->`__ |ext_link|. Sign-up units are managed from the **Sign-up Units** page in |destination-name|. You must provide an ID for an active sign-up unit.

.. campaign-attentive-api-get-details-end


.. _campaign-attentive-api-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Attentive API**

.. campaign-attentive-api-credentials-steps-start

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

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-attentive-api-key-start
             :end-before: .. credential-attentive-api-key-end

.. campaign-attentive-api-credentials-steps-end


.. _campaign-attentive-api-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Attentive API**

.. campaign-attentive-api-add-steps-start

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

       **Primary identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-verbose-logging-start
             :end-before: .. setting-active-campaign-verbose-logging-end

          .. important:: 

             .. include:: ../../shared/destination_settings.rst
                :start-after: .. setting-attentive-primary-identifier-context-start
                :end-before: .. setting-attentive-primary-identifier-context-end

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

.. campaign-attentive-api-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
