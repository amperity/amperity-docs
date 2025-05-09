.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Microsoft Dynamics
.. |plugin-name| replace:: "Microsoft Dynamics"
.. |credential-type| replace:: "dynamics"
.. |required-credentials| replace:: "client ID" and "client secret"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "micro"


.. meta::
    :description lang=en:
        Configure Amperity to send email lists to Microsoft Dynamics.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send email lists to Microsoft Dynamics.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destination for Microsoft Dynamics

==================================================
Configure destination for Microsoft Dynamics
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_microsoft_dynamics.html>`__ |ext_link|.

.. destination-microsoft-dynamics-about-start

|destination-name| is a customer relationship management (CRM) software application that is focused on the supporting sales, marketing, and services. It is part of the Microsoft Dynamics family of business applications.

.. destination-microsoft-dynamics-about-end

.. destination-microsoft-dynamics-api-note-start

.. note:: This destination uses the `Microsoft Dynamics Web API <https://learn.microsoft.com/en-us/previous-versions/dynamicscrm-2016/developers-guide/mt607689(v=crm.8)>`__ |ext_link|.

.. destination-microsoft-dynamics-api-note-end


.. _destination-microsoft-dynamics-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-microsoft-dynamics-get-details-table-start

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

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dynamics-client-id-and-secret-start
             :end-before: .. credential-microsoft-dynamics-client-id-and-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dynamics-client-id-and-secret-expiration-start
             :end-before: .. credential-microsoft-dynamics-client-id-and-secret-expiration-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Azure active directory ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dynamics-azure-ad-id-start
             :end-before: .. setting-microsoft-dynamics-azure-ad-id-end

       **Dynamics URL**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dynamics-url-start
             :end-before: .. setting-microsoft-dynamics-url-end

       **Dynamics entity** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dynamics-entity-start
             :end-before: .. setting-microsoft-dynamics-entity-end

       **Operation** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dynamics-operation-start
             :end-before: .. setting-microsoft-dynamics-operation-end

       **ID field** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dynamics-id-field-start
             :end-before: .. setting-microsoft-dynamics-id-field-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Microsoft Dynamics configuration**

       An application user that is assigned to a role with an access level that allows that user to modify and update records. (Some use cases require a user to delete records.) Admin credentials for portal.azure.com (if the customer wants Amperity to configure |destination-name| on their behalf).

       .. note:: A single tenant account type should be all that is required for Amperity to send data to |destination-name|.

.. destination-microsoft-dynamics-get-details-end


.. _destination-microsoft-dynamics-configure-azure:

Build Azure application
--------------------------------------------------

.. destination-microsoft-dynamics-configure-azure-start

An application for |destination-name| must be created in Microsoft Azure. This is the location to which query data is sent by Amperity.

.. destination-microsoft-dynamics-configure-azure-end

**To build the Azure application**

.. destination-microsoft-dynamics-configure-azure-steps-start

#. Go to portal.azure.com, and then log in with Admin credentials.
#. Open **Azure Active Directory**, and then click **App registrations**.
#. Click **New Registration**. The **Register an application** page opens.
#. Enter a name, such as "Amperity integration with |destination-name|", specify the account type (single tenant should be fine), and then click **Register**. (You should leave the redirect URI setting blank.)
#. The application page opens. The client ID and Azure Active Directory ID are shown on the page.

   .. important:: The Azure Active Directory ID is often referred to as the tenant ID.

#. On the application page, click **Certificates & secrets**, and then click **New client secret**.
#. Add a description for the secret, specify if the secret "expires in 1 year", "expires in 2 years", or "never expires", and then click **Add**.
#. Copy the secret that is generated.

.. destination-microsoft-dynamics-configure-azure-steps-end


.. _destination-microsoft-dynamics-configure-user:

Add application user
--------------------------------------------------

.. destination-microsoft-dynamics-configure-user-start

An application user with permission to modify and update records is required.

.. warning:: Only one application user may be created for each |destination-name| client ID.

.. destination-microsoft-dynamics-configure-user-end

**To add the application user**

.. destination-microsoft-dynamics-configure-user-steps-start

#. Go to the customer's instance of |destination-name|, and then log in with Admin credentials. The URL for |destination-name| is similar to "<tenant-name>.crm.dynamics.com".
#. Click **Settings**, then **System**, and then **Security**.
#. On the **Security** page, click **Users**, and then click **Application Users**.
#. Click **New**.
#. In the **New User** dialog box enter the user name, the application ID (which is the same as the |destination-name| client ID), full name, and primary email address. 

   .. note:: The URI for the application ID and the Azure Active Directory Object ID are both completed automatically.

#. Assign the user a role. Click **Manage Roles**, and then select a role with an access level that allows that user to modify and update records. (Some use cases require a user to delete records.)

.. destination-microsoft-dynamics-configure-user-steps-end


.. _destination-microsoft-dynamics-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Microsoft Dynamics**

.. destination-microsoft-dynamics-credentials-steps-start

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

          A client ID and client secret that has permission to access your instance of |destination-name|.

.. destination-microsoft-dynamics-credentials-steps-end


.. _destination-microsoft-dynamics-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Microsoft Dynamics**

.. destination-microsoft-dynamics-add-steps-start

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

       **Azure active directory ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dynamics-azure-ad-id-start
             :end-before: .. setting-microsoft-dynamics-azure-ad-id-end

       **Dynamics URL**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dynamics-url-start
             :end-before: .. setting-microsoft-dynamics-url-end

       **Dynamics entity**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dynamics-entity-start
             :end-before: .. setting-microsoft-dynamics-entity-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end

.. destination-microsoft-dynamics-add-steps-end


.. _destination-microsoft-dynamics-web-api:

Common Data Service Web API
==================================================

.. destination-microsoft-dynamics-web-api-start

.. note:: |destination-name| is a complex system. Even though Amperity has a built-in connector that supports sending data to entities within |destination-name|, there are more than 400 possible entities to which you can send data, such as sending segments to :doc:`Dynamics 365 Marketing <destination_dynamics_365_marketing>`, with each of these entities having its own schema that requires a unique mapping of data in a data template.

The `Common Data Service Web API <https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/about?view=dynamics-ce-odata-9>`__ |ext_link| (version 8.2 and higher or version 9.0) is the API to which Amperity can send data.

* |destination-name| is not strict about required fields, in that you may choose to not send fields to |destination-name| even when they are marked as required.
* |destination-name| is strict about extra fields, in that you should not send fields to |destination-name| that do not already exist in the entity's schema. Use the **include** section in the data template mapping to drop fields that should not be sent to |destination-name|.

Review the entities in the Common Data Service Web API prior to configuring a data template. Some of the entities that are more focused toward marketing and user activity include `Contact <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/contact>`__ |ext_link|, `List <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/list>`__ |ext_link|, `Campaign <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/campaign>`__ |ext_link|, `CampaignActivity <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/campaignactivity>`__ |ext_link|, `CampaignResponse <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/campaignresponse>`__ |ext_link|, or `CustomerAddress <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/customeraddress>`__ |ext_link|. Any of the entities found in the `Web API EntityType Reference <https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/entitytypes?view=dynamics-ce-odata-9>`__ |ext_link| may be configured as a destination, depending on your use case.

.. destination-microsoft-dynamics-web-api-end


.. TODO: Add workflow resolutions from existing topics HERE.
