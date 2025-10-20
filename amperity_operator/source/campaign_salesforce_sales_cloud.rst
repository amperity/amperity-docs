.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Salesforce Sales Cloud
.. |plugin-name| replace:: "Salesforce Sales Cloud"
.. |credential-type| replace:: "salesforce"
.. |required-credentials| replace:: "username", "password", and "security token"
.. |what-send| replace:: customer profiles
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "sales"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Salesforce Sales Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Salesforce Sales Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Salesforce Sales Cloud

==================================================
Configure campaigns for Salesforce Sales Cloud
==================================================

.. campaign-salesforce-sales-cloud-start

|destination-name| brings customer information together into an integrated platform, and then provides access to thousands of applications through the AppExchange.

.. .. campaign-salesforce-sales-cloud-end

.. campaign-salesforce-sales-cloud-api-note-start

.. note:: This destination uses the `Salesforce Sales Cloud SOAP API <https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_intro.htm>`__ |ext_link|.

.. campaign-salesforce-sales-cloud-api-note-end


.. _campaign-salesforce-sales-cloud-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-salesforce-sales-cloud-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Username and password**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-sales-cloud-username-and-password-start
             :end-before: .. credential-salesforce-sales-cloud-username-and-password-end

       **Security token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-sales-cloud-security-token-start
             :end-before: .. credential-salesforce-sales-cloud-security-token-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Salesforce object**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-salesforce-object-start
             :end-before: .. setting-salesforce-sales-cloud-salesforce-object-end


.. campaign-salesforce-sales-cloud-get-details-end


.. _campaign-salesforce-sales-cloud-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Salesforce Sales Cloud**

.. campaign-salesforce-sales-cloud-credentials-steps-start

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

       **Username and password**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-sales-cloud-username-and-password-start
             :end-before: .. credential-salesforce-sales-cloud-username-and-password-end

       **Security token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-sales-cloud-security-token-start
             :end-before: .. credential-salesforce-sales-cloud-security-token-end

.. campaign-salesforce-sales-cloud-credentials-steps-end


.. _campaign-salesforce-sales-cloud-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Salesforce Sales Cloud**

.. campaign-salesforce-sales-cloud-add-steps-start

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

       **Connect to sandbox instance?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-connect-to-sandbox-start
             :end-before: .. setting-salesforce-sales-cloud-connect-to-sandbox-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-connect-to-sandbox-ignored-start
             :end-before: .. setting-salesforce-sales-cloud-connect-to-sandbox-ignored-end

       **Custom Salesforce login URL**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-custom-login-url-start
             :end-before: .. setting-salesforce-sales-cloud-custom-login-url-end

       **Salesforce object**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-salesforce-object-start
             :end-before: .. setting-salesforce-sales-cloud-salesforce-object-end

       **Operation**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-operation-start
             :end-before: .. setting-salesforce-sales-cloud-operation-end

       **External ID field**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-external-id-field-start
             :end-before: .. setting-salesforce-sales-cloud-external-id-field-end

       **Load data in parallel?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-load-data-in-parallel-start
             :end-before: .. setting-salesforce-sales-cloud-load-data-in-parallel-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-load-data-in-parallel-caution-start
             :end-before: .. setting-salesforce-sales-cloud-load-data-in-parallel-caution-end

       **Use NULL for empty fields?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-sales-cloud-use-null-for-empty-fields-start
             :end-before: .. setting-salesforce-sales-cloud-use-null-for-empty-fields-end

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
          :start-after: .. campaigns-steps-business-users-orchestration-only-start
          :end-before: .. campaigns-steps-business-users-orchestration-only-end

.. campaign-salesforce-sales-cloud-add-steps-end
