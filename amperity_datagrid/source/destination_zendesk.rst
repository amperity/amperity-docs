.. https://docs.amperity.com/internal/



.. |destination-name| replace:: Zendesk
.. |destination-api| replace:: Zendesk Users API
.. |plugin-name| replace:: "Zendesk"
.. |credential-type| replace:: "zendesk"
.. |required-credentials| replace:: "email address" and "API token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "zen"


.. meta::
    :description lang=en:
        Configure Amperity to send customer profiles to Zendesk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profiles to Zendesk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send customer profiles to Zendesk

==================================================
Send customer profiles to Zendesk
==================================================

.. note:: This topic contains information for configuring a destination for sending query results to |destination-name| using orchestrations. To configure a destination for sending audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_zendesk.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-zendesk-start
   :end-before: .. term-zendesk-end

.. destination-zendesk-start

Amperity may be configured to create or update user records in |destination-name| by using the |destination-api| to `create or update users <https://developer.zendesk.com/api-reference/ticketing/users/users/#create-or-update-many-users>`__ |ext_link|. Use this connector to deliver a better customer support experience by pre-populating |destination-name| user records with customer records from Amperity, including:

* Order history
* Loyalty status
* Satisfaction survey results
* Shopping preferences
* and more

Use this data to show customer support representatives information related to product recommendations, next best actions, and likelihood of churn.

.. destination-zendesk-end

.. destination-zendesk-note-start

.. note:: Creating or updating records are `rate limited <https://developer.zendesk.com/rest_api/docs/support/introduction#endpoint-specific-rate-limits>`__ |ext_link| to a maximum of 100 users per second.

.. destination-zendesk-note-end


.. _destination-zendesk-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-zendesk-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **API token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-zendesk-api-token-start
             :end-before: .. credential-zendesk-api-token-end

       **Email address**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-zendesk-email-address-start
             :end-before: .. credential-zendesk-email-address-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Subdomain**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-zendesk-subdomain-start
             :end-before: .. setting-zendesk-subdomain-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - **Required fields for Zendesk**

       Be sure to send all fields from Amperity that will be required by |destination-name|. The **name**, **email** or **external_id** fields must be included.

       From within |destination-name| verify that audience data has been loaded and is usable by all of the use cases you want to use within |destination-name| to build better customer experiences.

.. destination-zendesk-get-details-end


.. _destination-zendesk-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Zendesk**

.. destination-zendesk-credentials-steps-start

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

       **API token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-zendesk-api-token-start
             :end-before: .. credential-zendesk-api-token-end

       **Email address**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-zendesk-email-address-start
             :end-before: .. credential-zendesk-email-address-end

.. destination-zendesk-credentials-steps-end


.. _destination-zendesk-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Zendesk**

.. destination-zendesk-add-steps-start

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

       **Subdomain**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-zendesk-subdomain-start
             :end-before: .. setting-zendesk-subdomain-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-zendesk-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
