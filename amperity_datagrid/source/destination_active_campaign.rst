.. https://docs.amperity.com/internal/



.. |destination-name| replace:: ActiveCampaign
.. |plugin-name| replace:: "ActiveCampaign"
.. |credential-type| replace:: "active-campaign"
.. |required-credentials| replace:: "API key" and "URL"
.. |what-send| replace:: audience lists
.. |where-send| replace:: |destination-name|
.. |audience-primary-key| replace:: "email"
.. |filter-the-list| replace:: "acti"
.. |allow-for-what| replace:: audience lists
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Configure Amperity to send audience lists to ActiveCampaign.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audience lists to ActiveCampaign.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audience lists to ActiveCampaign

==================================================
Send audience lists to ActiveCampaign
==================================================

.. note:: This topic contains information for configuring a destination for sending query results to |destination-name| using orchestrations. To configure a destination for sending audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_active_campaign.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-active-campaign-start
   :end-before: .. term-active-campaign-end

.. destination-active-campaign-api-note-start

.. note:: This destination uses the `Active Campaign REST API <https://developers.activecampaign.com/reference/url>`__ |ext_link|.

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. allow-for-start
      :end-before: .. allow-for-end

   |destination-name| API is rate limited to 5 requests per second.

.. destination-active-campaign-api-note-end


.. _destination-active-campaign-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-active-campaign-get-details-table-start

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
             :start-after: .. credential-active-campaign-api-key-start
             :end-before: .. credential-active-campaign-api-key-end

       **Base URL**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-active-campaign-url-start
             :end-before: .. credential-active-campaign-url-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Audience primary key**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Group name**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-group-name-start
             :end-before: .. setting-active-campaign-group-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-group-name-access-start
             :end-before: .. setting-active-campaign-group-name-access-end

       **List name** (Required at orchestration)
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-list-name-start
             :end-before: .. setting-active-campaign-list-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-active-campaign-email-required-start
          :end-before: .. setting-active-campaign-email-required-end

.. destination-active-campaign-get-details-table-end


.. _destination-active-campaign-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for ActiveCampaign**

.. destination-active-campaign-credentials-steps-start

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
             :start-after: .. credential-active-campaign-api-key-start
             :end-before: .. credential-active-campaign-api-key-end

       **URL**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-active-campaign-url-start
             :end-before: .. credential-active-campaign-url-end

.. destination-active-campaign-credentials-steps-end


.. _destination-active-campaign-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for ActiveCampaign**

.. destination-active-campaign-add-steps-start

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

       .. image:: ../../images/mockup-destinations-add-01-select-destination-active-campaign.png
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

       **Audience primary key**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Group name**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-group-name-start
             :end-before: .. setting-active-campaign-group-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-group-name-access-start
             :end-before: .. setting-active-campaign-group-name-access-end

       **List name** (Required at orchestration)
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-list-name-start
             :end-before: .. setting-active-campaign-list-name-end

       **Verbose logging?**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-verbose-logging-start
             :end-before: .. setting-active-campaign-verbose-logging-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-active-campaign-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
