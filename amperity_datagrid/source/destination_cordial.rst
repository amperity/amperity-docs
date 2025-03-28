.. https://docs.amperity.com/internal/



.. |destination-name| replace:: Cordial
.. |destination-api| replace:: Cordial API
.. |plugin-name| replace:: "Cordial"
.. |credential-type| replace:: "cordial"
.. |required-credentials| replace:: "API key" and "API URL"
.. |audience-primary-key| replace:: "audience"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "cord"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Cordial.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Cordial.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Cordial

==================================================
Send audiences to Cordial
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_cordial.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-cordial-start
   :end-before: .. term-cordial-end

.. destination-cordial-start

Use Amperity to manage contacts--attributes and list membership--in |destination-name| using the following REST APIs:

* `Account Contact Attributes <https://support.cordial.com/hc/en-us/articles/204570347-Account-Contact-Attributes>`__ |ext_link| to create contact attributes. Attributes that do not exist in |destination-name| are added as custom contact attributes.
* `Account Lists <https://support.cordial.com/hc/en-us/articles/204570497-Account-Lists>`__ |ext_link| to fetch, create, and clear account lists, to which contacts are associated. An account list is overwritten each time results are sent from Amperity. An email address is added when it is not already a contact, after which it is assigned the **subscribed** status. An email address that is already a contact will retain its assigned subscription status.
* `Contact Imports <https://support.cordial.com/hc/en-us/articles/203886058-Contact-Imports>`__ |ext_link| to import contacts to |destination-name|, and then associate contacts to the account list.
* `Jobs <https://support.cordial.com/hc/en-us/articles/204570807-Jobs>`__ |ext_link| to monitor the import job for completion.

Build a query or segment that contains the **email** field, along with any other fields that you want created or updated in |destination-name| and represented as contact attributes.

.. destination-cordial-end

.. destination-cordial-get-details-alternate-note-start

.. note:: Amperity recommends using the |destination-api| to send |what-send| from Amperity to |destination-name|.

   However, if you prefer to send a CSV or JSON file (one-time or recurring) instead of using the |destination-api| you may configure `Cordial Data Automations <https://support.cordial.com/hc/en-us/articles/360029407471>`__ |ext_link|, and then enable that workflow using any of these destinations: :doc:`SFTP <destination_sftp>`, :doc:`Amazon S3 <destination_amazon_s3>`, or :doc:`Google Cloud Storage <destination_google_cloud_storage>`.

.. destination-cordial-get-details-alternate-note-end


.. _destination-cordial-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-cordial-get-details-table-start

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

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-cordial-api-key-start
             :end-before: .. credential-cordial-api-key-end

       **API URL**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-cordial-api-url-start
             :end-before: .. credential-cordial-api-url-end

       .. tip:: Use the `IP address for allowlists <https://docs.amperity.com/datagrid/send_data.html#ip-allowlists>`__ for Amperity to configure the allowlist for the |destination-api|.

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

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-list-name-start
             :end-before: .. setting-cordial-list-name-end

       **Subscription status**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-subscription-status-start
             :end-before: .. setting-cordial-subscription-status-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - **Cordial Rest API configuration**

       The following Cordial REST API methods must be enabled:

       ::

           GET /accountcontractattributes
           POST /accountcontractattributes

           GET /accountlists
           POST /accountlists
           PUT /accountlists/{key}/clear

           POST /contactimports

           GET /jobs/{id}

.. destination-cordial-get-details-end


.. _destination-cordial-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Cordial**

.. destination-cordial-credentials-steps-start

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

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-cordial-api-key-start
             :end-before: .. credential-cordial-api-key-end

       **API URL**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-cordial-api-url-start
             :end-before: .. credential-cordial-api-url-end

.. destination-cordial-credentials-steps-end


.. _destination-cordial-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Cordial**

.. destination-cordial-add-steps-start

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
             :start-after: .. setting-cordial-list-name-start
             :end-before: .. setting-cordial-list-name-end

       **Subscription status**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-subscription-status-start
             :end-before: .. setting-cordial-subscription-status-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-cordial-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
