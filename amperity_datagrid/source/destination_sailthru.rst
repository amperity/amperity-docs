.. https://docs.amperity.com/internal/



.. |destination-name| replace:: Sailthru by Marigold
.. |destination-api| replace:: Sailthru API
.. |plugin-name| replace:: "Sailthru"
.. |credential-type| replace:: "sailthru"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "sai"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send data to Sailthru by Marigold.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Sailthru by Marigold.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Sailthru by Marigold

==================================================
Send audience lists to Sailthru by Marigold
==================================================

.. note:: This topic contains information for configuring a destination for sending query results to |destination-name| using orchestrations. To configure a destination for sending audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_sailthru.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-sailthru-start
   :end-before: .. term-sailthru-end

.. destination-sailthru-start

Use Amperity to manage audience lists in |destination-name|. Build a query using the **email** field, and then send the results of that query to |destination-name| or build a segment that matches specific criteria, and then send the email addresses for customers who belong to that audience. You may extend the audience using custom attributes.

.. destination-sailthru-end

.. destination-sailthru-api-note-start

.. note:: This destination uses the `Sailthru API <https://getstarted.sailthru.com/developers/api-basics/introduction/>`__ |ext_link|.

.. destination-sailthru-api-note-end


.. _destination-sailthru-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-sailthru-get-details-table-start

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
             :start-after: .. credential-sailthru-api-key-start
             :end-before: .. credential-sailthru-api-key-end

       **API secret**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sailthru-secret-start
             :end-before: .. credential-sailthru-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sailthru-api-find-key-and-secret-start
             :end-before: .. credential-sailthru-api-find-key-and-secret-end

       .. tip:: You can find the API key and secret after you log in to |destination-name|. The `API key and API secret <https://getstarted.sailthru.com/account/management/settings/>`__ |ext_link| are available after you authenticate to the |destination-name| API. (See the first item under "Setup – API & Postbacks" on that page.)

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Audience primary key**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **List name**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sailthru-list-name-start
             :end-before: .. setting-sailthru-list-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - A query that outputs the fields that must be mapped to the |destination-name| audience.

.. destination-sailthru-get-details-end


.. _destination-sailthru-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Pinterest**

.. destination-sailthru-credentials-steps-start

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
             :start-after: .. credential-sailthru-api-key-start
             :end-before: .. credential-sailthru-api-key-end

       **API secret**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sailthru-secret-start
             :end-before: .. credential-sailthru-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sailthru-api-find-key-and-secret-start
             :end-before: .. credential-sailthru-api-find-key-and-secret-end

.. destination-sailthru-credentials-steps-end


.. _destination-sailthru-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Pinterest**

.. destination-sailthru-add-steps-start

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

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sailthru-list-name-start
             :end-before: .. setting-sailthru-list-name-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-sailthru-add-steps-end


.. _destination-sailthru-extended-profile-attributes:

Extended profile attributes
==================================================

.. destination-sailthru-extended-profile-attributes-start

You can extend audiences that are sent to |destination-name| by including extended profile attributes.

The following SQL query shows how to return results that map to |destination-name| field naming requirements:

.. code-block::

   SELECT
     address AS postal_address
     ,address2 AS postal_address2
     ,birthdate AS birth_date
     ,city AS postal_city
     ,country
     ,full_name AS name
     ,gender
     ,given_name AS first_name
     ,phone
     ,postal AS postal_code
     ,surname AS last_name
     ,state AS postal_state
   FROM Customer360

.. note:: |destination-name| field names are case sensitive and cannot start with a number. Review the list of `extended profile attributes <https://getstarted.sailthru.com/audience/managing-users/set-variables-on-users/>`__ |ext_link| that are supported by |destination-name|.

.. destination-sailthru-extended-profile-attributes-end


.. TODO: Add workflow resolutions from existing topics HERE.
