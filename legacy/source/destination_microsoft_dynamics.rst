.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Microsoft Dynamics
.. |plugin-name| replace:: Microsoft Dynamics
.. |what-send| replace:: data
.. |filter-the-list| replace:: "micro"
.. |credential-type| replace:: "azure-application"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by |destination-name| were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


==================================================
Send data to Microsoft Dynamics
==================================================

.. vale off

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_microsoft_dynamics.html>`__ |ext_link|.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-dynamics-start
   :end-before: .. term-microsoft-dynamics-end

.. destination-microsoft-dynamics-api-note-start

.. note:: This destination uses the `Microsoft Dynamics Web API <https://docs.microsoft.com/en-us/previous-versions/dynamicscrm-2016/developers-guide/mt607689%28v%3dcrm.8%29>`__ |ext_link|.

.. destination-microsoft-dynamics-api-note-end

.. destination-microsoft-dynamics-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-microsoft-dynamics-get-details>`
#. :ref:`Configure Microsoft Dynamics <destination-microsoft-dynamics-configure>`
#. :ref:`Build a query <destination-microsoft-dynamics-build-query>`
#. :ref:`Add destination <destination-microsoft-dynamics-add-destination>`
#. :ref:`Add data template <destination-microsoft-dynamics-add-data-template>`

.. destination-microsoft-dynamics-steps-to-send-end


.. _destination-microsoft-dynamics-get-details:

Get details
==================================================

.. destination-microsoft-dynamics-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - The client ID and client secret.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - The Azure Active Directory ID.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - The login URL of |destination-name|, similar to "<tenant-name>.crm.dynamics.com".

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: left
          :class: no-scaled-link
     - Admin credentials for portal.azure.com (if the customer wants Amperity to configure |destination-name| on their behalf).

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 5.
          :align: left
          :class: no-scaled-link
     - An application user that is assigned to a role with an access level that allows that user to modify and update records. (Some use cases require a user to delete records.)

       .. note:: A single tenant account type should be all that is required for Amperity to send data to |destination-name|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 6.
          :align: left
          :class: no-scaled-link
     - The expiration date for the client secret: one of "expires in 1 year", "expires in 2 years", or "never expires".

.. destination-microsoft-dynamics-get-details-end

.. destination-microsoft-dynamics-get-details-account-info-start

.. admonition:: How to find |destination-name| account information?

   You can find all of this information from your |destination-name| instance in Microsoft Azure.

   #. The registered application in Microsoft Azure have the |destination-name| client ID, client secret, and Azure Active Directory ID.
   #. The login URL is similar to "https://<tenant-name>.crm.dynamics.com".
   #. The application user is added to the customer's instance of |destination-name|.

.. destination-microsoft-dynamics-get-details-account-info-end


.. _destination-microsoft-dynamics-configure:

Configure Microsoft Dynamics
==================================================

.. destination-facebook-ads-configure-account-access-start

|destination-name| requires :ref:`an application to be created in Microsoft Azure <destination-microsoft-dynamics-configure-azure>`, and then :ref:`add an application user to Microsoft Dynamics <destination-microsoft-dynamics-configure-user>`

.. destination-facebook-ads-configure-account-access-end


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

#. Go to the customer's instance of |destination-name|, and then log in with Admin credentials. The URL of |destination-name| is similar to "<tenant-name>.crm.dynamics.com".
#. Click **Settings**, then **System**, and then **Security**.
#. On the **Security** page, click **Users**, and then click **Application Users**.
#. Click **New**.
#. In the **New User** dialog box enter the user name, the application ID (which is the same as the |destination-name| client ID), full name, and primary email address. 

   .. note:: The URI for the application ID and the Azure Active Directory Object ID are both completed automatically.

#. Assign the user a role. Click **Manage Roles**, and then select a role with an access level that allows that user to modify and update records. (Some use cases require a user to delete records.)

.. destination-microsoft-dynamics-configure-user-steps-end


.. _destination-microsoft-dynamics-build-query:

Build query
==================================================

.. destination-microsoft-dynamics-build-query-start

You need to build a query that outputs fields that can be mapped to |destination-name|.

.. destination-microsoft-dynamics-build-query-end


.. _destination-microsoft-dynamics-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-microsoft-dynamics-add-destination-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-name-and-description-start
          :end-before: .. destinations-add-name-and-description-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-01-select.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       |destination-name| has the following settings:

       * Client ID and secret

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings.png
          :width: 500 px
          :alt: Settings for Microsoft Dynamics.
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Active Directory ID**
            - The Active Directory tenant ID that is associated with your Microsoft Azure subscription.

          * - **Dynamics URL**
            - The URL of your instance of |destination-name|.  The URL must be the full URL, including ``https://``. For example:

              ::

                 https://<tenant-name>.crm.dynamics.com


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-microsoft-dynamics-add-destination-steps-end


.. _destination-microsoft-dynamics-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-microsoft-dynamics-add-data-template-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-start
          :end-before: .. destinations-data-template-open-template-end

       .. image:: ../../images/mockup-data-template-tab-add-01-details.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-name-start
          :end-before: .. destinations-data-template-open-template-name-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       .. image:: ../../images/mockup-data-template-tab-add-03-settings.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-note-start
          :end-before: .. destinations-data-template-verify-config-settings-note-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-start
          :end-before: .. destinations-data-template-save-end

       .. image:: ../../images/mockup-destinations-tab-add-05-save.png
          :width: 500 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

.. destination-microsoft-dynamics-add-data-template-steps-end


.. _destination-microsoft-dynamics-web-api:

Common Data Service Web API
==================================================

.. destination-microsoft-dynamics-web-api-start

.. note:: |destination-name| is a complex system. Even though Amperity has a built-in connector that supports sending data to entities within |destination-name|, there are more than 400 possible entities to which you can send data, such as sending segments to :doc:`Dynamics 365 Marketing <destination_dynamics_365_marketing>`, with each of these entities having its own schema that requires a unique mapping of data in a data template.

The `common data services Web API <https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/about?view=dynamics-ce-odata-9>`__ |ext_link| (version 8.2 and higher or version 9.0) is the API to which Amperity can send data.

* |destination-name| is not strict about required fields, in that you may choose to not send fields to |destination-name| even when they are marked as required.
* |destination-name| is strict about extra fields, in that you should not send fields to |destination-name| that do not already exist in the entity's schema. Use the **include** section in the data template mapping to drop fields that should not be sent to |destination-name|.

Review the entities in the Common Data Service Web API prior to configuring a data template. Some of the entities that are more focused toward marketing and user activity include `Contact <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/contact>`__ |ext_link|, `List <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/list>`__ |ext_link|, `Campaign <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/campaign>`__ |ext_link|, `CampaignActivity <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/campaignactivity>`__ |ext_link|, `CampaignResponse <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/campaignresponse>`__ |ext_link|, or `CustomerAddress <https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/customeraddress>`__ |ext_link|. Any of the entities found in the `Web API EntityType Reference <https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/entitytypes?view=dynamics-ce-odata-9>`__ |ext_link| may be configured as a destination, depending on your use case.

.. destination-microsoft-dynamics-web-api-end
