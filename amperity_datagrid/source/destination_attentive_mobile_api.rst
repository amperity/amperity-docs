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
        Configure Amperity to send custom attributes to Attentive.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send custom attributes to Attentive.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send custom attributes to Attentive

==================================================
Send custom attributes to Attentive
==================================================

.. destination-attentive-mobile-api-attributes-start

|destination-name| is your source of truth for your customers' subscription status, while Amperity is your source of truth for profile attributes that describe those customers.

Amperity uses the `Subscriptions <https://docs.attentive.com/openapi/reference/tag/Subscribers/>`__ |ext_link| and `Custom Attributes <https://docs.attentivemobile.com/openapi/reference/tag/Custom-Attributes/>`__ |ext_link| endpoints to send custom profile attributes to |destination-name|. Use these attributes to apply customizable data or characteristics to each of your subscribers, and then use that information to build segments for use with campaigns and journeys.

.. caution:: The |destination-name| |destination-api| allows you to build segments based on a match with customer profile attributes. Custom attributes `cannot contain any sensitive or special categories of information <https://docs.attentivemobile.com/pages/legal-docs/pi-disclaimer/>`__ |ext_link|.

.. destination-attentive-mobile-api-attributes-end

.. destination-attentive-sftp-and-api-start

.. admonition:: Why are there two ways to send data to Attentive?

   Amperity uses the `subscriber segment upload <https://docs.attentivemobile.com/pages/developer-guides/sftp-solution/subscriber-segment-upload/#subscriber-segment-upload>`__ |ext_link| process to manage segments. This process does not use an endpoint and is not subject to `Attentive API rate limits <https://docs.attentive.com/pages/api-rate-limits/>`__ |ext_link|. Updates appear on the **Segments** page within your audience in |destination-name|.

.. destination-attentive-sftp-and-api-end


.. _destination-attentive-api-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-attentive-api-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
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
          :align: left
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

.. TODO: What is this? "The ID for the |ext_attentive_mobile_signup_units|. Sign-up units are managed from the **Sign-up Units** page in |destination-name|. You must provide an ID for an active sign-up unit."

.. destination-attentive-api-get-details-end


.. _destination-attentive-api-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Attentive API**

.. destination-attentive-api-credentials-steps-start

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

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-attentive-api-key-start
             :end-before: .. credential-attentive-api-key-end

.. destination-attentive-api-credentials-steps-end


.. _destination-attentive-api-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Attentive API**

.. destination-attentive-api-add-steps-start

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

       **Primary identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-verbose-logging-start
             :end-before: .. setting-active-campaign-verbose-logging-end

          .. important:: 

             .. include:: ../../shared/destination_settings.rst
                :start-after: .. setting-attentive-primary-identifier-context-start
                :end-before: .. setting-attentive-primary-identifier-context-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-attentive-api-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
