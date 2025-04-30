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
        Configure Amperity to send static audience lists to Adobe Marketo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send static audience lists to Adobe Marketo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send static audience lists to Adobe Marketo

==================================================
Send static audience lists to Adobe Marketo
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_adobe_marketo.html>`__ |ext_link|.

|destination-name| is marketing automation software that streamlines, automates, and measures marketing tasks and workflows. An email address must be sent to |destination-name|. You may also send first names, last names, company names, and phone numbers.

.. note::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-adobe-marketo-list-name-membership-start
      :end-before: .. setting-adobe-marketo-list-name-membership-end


.. _destination-adobe-marketo-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-adobe-marketo-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
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


.. destination-adobe-marketo-get-details-end


.. _destination-adobe-marketo-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Adobe Marketo**

.. destination-adobe-marketo-credentials-steps-start

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

.. destination-adobe-marketo-credentials-steps-end


.. _destination-adobe-marketo-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Adobe Marketo**

.. destination-adobe-marketo-add-steps-start

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


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-adobe-marketo-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
