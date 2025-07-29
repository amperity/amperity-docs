.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Dotdigital
.. |plugin-name| replace:: "Dotdigital"
.. |credential-type| replace:: "dotdigital"
.. |required-credentials| replace:: "API username" and "API password"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "dotd"


.. meta::
    :description lang=en:
        Configure Amperity to send customer profiles to Dotdigital.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profiles to Dotdigital.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Dotdigital

==================================================
Configure destinations for Dotdigital
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dotdigital-start
   :end-before: .. term-dotdigital-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-configure-start
   :end-before: .. setting-common-file-configure-end


.. _destination-dotdigital-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-dotdigital-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API username**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-dotdigital-api-username-start
             :end-before: .. credential-dotdigital-api-username-end

       **API password**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-dotdigital-api-password-start
             :end-before: .. credential-dotdigital-api-password-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **List name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-list-name-start
             :end-before: .. setting-common-list-name-end

       **Contact identifier type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dotdigital-contact-identifier-type-start
             :end-before: .. setting-dotdigital-contact-identifier-type-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required permissions**

       The `Dotdigital API user <https://developer.dotdigital.com/docs/setting-up-an-api-user>`__ |ext_link| must have permission to access account information, create and update contacts, manage address books, and manage data fields.


.. destination-dotdigital-get-details-table-end


.. _destination-dotdigital-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Dotdigital**

.. destination-dotdigital-credentials-steps-start

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

       **API username**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-dotdigital-api-username-start
             :end-before: .. credential-dotdigital-api-username-end

       **API password**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-dotdigital-api-password-start
             :end-before: .. credential-dotdigital-api-password-end

.. destination-dotdigital-credentials-steps-end


.. _destination-dotdigital-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Dotdigital**

.. destination-dotdigital-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-sftp.png
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
          :align: center
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
          :align: center
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
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **List name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-list-name-start
             :end-before: .. setting-common-list-name-end

       **Contact identifier type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dotdigital-contact-identifier-type-start
             :end-before: .. setting-dotdigital-contact-identifier-type-end

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
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


.. destination-dotdigital-add-steps-end
