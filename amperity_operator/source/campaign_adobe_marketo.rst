.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Adobe Marketo
.. |plugin-name| replace:: "Marketo"
.. |credential-type| replace:: "marketo"
.. |required-credentials| replace:: "client ID", "client secret", and "subdomain"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: static audience lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "adobe"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Adobe Marketo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Adobe Marketo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Adobe Marketo

==================================================
Configure campaigns for Adobe Marketo
==================================================

|destination-name| is marketing automation software that streamlines, automates, and measures marketing tasks and workflows. An email address must be sent to |destination-name|. You may also send first names, last names, company names, and phone numbers.

.. note::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-adobe-marketo-list-name-membership-start
      :end-before: .. setting-adobe-marketo-list-name-membership-end


.. _campaign-adobe-marketo-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-adobe-marketo-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Client ID and client secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-marketo-client-id-start
             :end-before: .. credential-adobe-marketo-client-id-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-marketo-access-token-start
             :end-before: .. credential-adobe-marketo-access-token-end

       **Subdomain**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-marketo-subdomain-start
             :end-before: .. credential-adobe-marketo-subdomain-end


.. campaign-adobe-marketo-get-details-end


.. _campaign-adobe-marketo-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Adobe Marketo**

.. campaign-adobe-marketo-credentials-steps-start

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

       **Client ID and client secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-marketo-client-id-start
             :end-before: .. credential-adobe-marketo-client-id-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-marketo-access-token-start
             :end-before: .. credential-adobe-marketo-access-token-end

       **Subdomain**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-marketo-subdomain-start
             :end-before: .. credential-adobe-marketo-subdomain-end

.. campaign-adobe-marketo-credentials-steps-end


.. _campaign-adobe-marketo-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

.. note::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-adobe-marketo-list-name-limitations-start
      :end-before: .. setting-adobe-marketo-list-name-limitations-end

**To add a destination for Adobe Marketo**

.. campaign-adobe-marketo-add-steps-start

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

       **Folder name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-adobe-marketo-folder-name-start
             :end-before: .. setting-adobe-marketo-folder-name-end

       **Program name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-adobe-marketo-program-name-start
             :end-before: .. setting-adobe-marketo-program-name-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-adobe-marketo-list-name-start
             :end-before: .. setting-adobe-marketo-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-adobe-marketo-list-name-first-audience-start
             :end-before: .. setting-adobe-marketo-list-name-first-audience-end

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


.. campaign-adobe-marketo-add-steps-end
