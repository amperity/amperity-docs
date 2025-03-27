.. https://docs.amperity.com/internal/



.. |destination-name| replace:: Klaviyo
.. |destination-api| replace:: Klaviyo API
.. |plugin-name| replace:: "Klaviyo"
.. |credential-type| replace:: "klaviyo"
.. |required-credentials| replace:: "API key"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audience lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "klav"


.. meta::
    :description lang=en:
        Configure Amperity to send audience lists to Klaviyo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audience lists to Klaviyo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audience lists to Klaviyo

==================================================
Send audience lists to Klaviyo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-klaviyo-start
   :end-before: .. term-klaviyo-end

.. destination-klaviyo-start

Use Amperity to manage audience lists in |destination-name|. Build a query using the **email** field, with optional additional customer profile fields, and then send the results of that query to |destination-name|. The audience list will be updated to match the query.

.. destination-klaviyo-end

.. destination-klaviyo-api-note-start

.. note:: This destination uses the `Klaviyo REST API <https://apidocs.klaviyo.com/reference/api-overview>`__ |ext_link|.

   Amperity uses the `Update Profile <https://developers.klaviyo.com/en/reference/update_profile>`__ |ext_link| endpoint in the |destination-name| REST API to send customer profile attributes to |destination-name|.

   Review the `rate limits <https://developers.klaviyo.com/en/docs/rate_limits_and_error_handling#rate-limits>`__ |ext_link| that are applied to endpoints in the |destination-name| REST API to manage customer profiles.

   Before sending a set of customer profiles to |destination-name|, and to help set expectations, you should review the rate limits and estimate the amount of time required to complete the process of adding your set of customer profiles to |destination-name|.

.. destination-klaviyo-api-note-end

.. destination-klaviyo-csv-note-start

   If you don't want to wait to load customer profiles, you may instead use the `SFTP import tool <https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool>`__ |ext_link| process. This approach is efficient and quick. It uses the :doc:`built-in SFTP connector in Amperity <destination_sftp>` and is capable of importing large sets of customer profiles.

   The CSV file that is imported to |destination-name| has specific requirements on formatting and must include one (or more) of the following fields: "Email", "PhoneNumber", and/or "ExternalID". When these fields are present in the CSV file they must have those exact names.

.. destination-klaviyo-csv-note-end


.. _destination-klaviyo-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-klaviyo-get-details-table-start

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
             :start-after: .. credential-klaviyo-api-key-start
             :end-before: .. credential-klaviyo-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-klaviyo-api-key-scopes-start
             :end-before: .. credential-klaviyo-api-key-scopes-end

.. destination-klaviyo-get-details-end


.. _destination-klaviyo-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Klaviyo**

.. destination-klaviyo-credentials-steps-start

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
             :start-after: .. credential-klaviyo-api-key-start
             :end-before: .. credential-klaviyo-api-key-end

.. destination-klaviyo-credentials-steps-end


.. _destination-klaviyo-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Klaviyo**

.. destination-klaviyo-add-steps-start

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

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-klaviyo-list-name-start
             :end-before: .. setting-klaviyo-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-klaviyo-list-name-note-start
             :end-before: .. setting-klaviyo-list-name-note-end

       **Update contacts**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-list-name-start
             :end-before: .. setting-cordial-list-name-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-klaviyo-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
