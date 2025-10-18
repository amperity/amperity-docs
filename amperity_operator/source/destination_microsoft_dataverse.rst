.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Microsoft Dataverse
.. |plugin-name| replace:: "Microsoft Dataverse"
.. |credential-type| replace:: "microsoft-dataverse"
.. |required-credentials| replace:: "Azure tenant ID", "Azure client ID", and "Azure client secret"
.. |what-send| replace:: table rows that match a table schema
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "micro"


.. meta::
    :description lang=en:
        Configure Amperity to send data tables to Microsoft Dataverse.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data tables to Microsoft Dataverse.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Microsoft Dataverse

==================================================
Configure destinations for Microsoft Dataverse
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-dataverse-start
   :end-before: .. term-microsoft-dataverse-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-microsoft-dataverse-requirements-start
   :end-before: .. credential-microsoft-dataverse-requirements-end


.. UNCOMMENT

.. 
.. .. _destination-microsoft-dataverse-howitworks:
.. 
.. How this destination works
.. ==================================================
.. 
.. .. destination-microsoft-dataverse-howitworks-start
.. 
.. Use |destination-name| to send rows of data from Amperity, and then add them to tables in |destination-name|. The connector will validate each row of data that is sent from Amperity against the table schema in |destination-name|. Only rows that validate against the table schema will be added to the table.
.. 
.. .. destination-microsoft-dataverse-howitworks-end
.. 
.. .. image:: ../../images/destination-microsoft-dataverse.png
..    :width: 600 px
..    :alt: Send rows of data from Amperity to Microsoft Dataverse.
..    :align: left
..    :class: no-scaled-link
.. 
.. .. destination-microsoft-dataverse-howitworks-callouts-start
.. 
.. A |destination-name| destination works like this:
.. 
.. #. Use a query to build a table with rows of data that match the schema of a table in |destination-name|. The column names, data types, and column order must match the schema that is defined in |destination-name|.
.. #. Configure the :ref:`Microsoft Dataverse destination <destination-microsoft-dataverse-add>` in Amperity.
.. #. Validated table rows are sent to |destination-name|.
.. 
.. .. destination-microsoft-dataverse-howitworks-callouts-end
.. 


.. _destination-microsoft-dataverse-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-microsoft-dataverse-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Azure tenant ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dataverse-azure-tenant-id-start
             :end-before: .. credential-microsoft-dataverse-azure-tenant-id-end

       **Azure client ID and client secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dataverse-azure-client-id-and-secret-start
             :end-before: .. credential-microsoft-dataverse-azure-client-id-and-secret-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Power Apps environment region**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dataverse-powerapps-region-start
             :end-before: .. setting-microsoft-dataverse-powerapps-region-end

       **Power Apps environment name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dataverse-powerapps-name-start
             :end-before: .. setting-microsoft-dataverse-powerapps-name-end

       **Dataverse table logical name**

          |checkmark-required| **Required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dataverse-table-logical-name-start
             :end-before: .. setting-microsoft-dataverse-table-logical-name-end


.. destination-microsoft-dataverse-get-details-end


.. _destination-microsoft-dataverse-application:

Configure your Microsoft application
==================================================

.. destination-microsoft-dataverse-application-start

To send data to |destination-name|, you need to configure an application in Microsoft Azure to create the application and directory IDs and a client secret, after which you must add your application to the Microsoft Power Platform.

.. destination-microsoft-dataverse-application-start

**To configure your application in Microsoft Azure**

.. destination-microsoft-dataverse-application-azure-steps-start

#. Log in to your Microsoft Azure account.
#. Open **Azure Active Directory**, and then **App Registrations**.
#. Click **New Registration**, and then enter the name for your application. Leave all other settings as the default, and then click **Register**.
#. The application overview page contains the following IDs:

   **Application (client) ID**

   **Directory (tenant) ID**

#. From the left-side navigation, click **Authentication**, then **Add a platform**, and then **Web**.
#. On the next page, in the **Redirect URI** field, enter: ``https://app.amperity.com``.
#. Under **Implicit grant and hybrid flows**, enable the **Access tokens (used for implicit flows)** option, and then click **Configure**.
#. From the left-side navigation, click **Certificates & Secrets**, select the **Client secrets** tab, and then click **New client secret**.

#. From the left-side navigation, click **API Permissions**, select **Add a permission**, select **Dynamics CRM**, select **user_impersonation**, and then click **Add permissions**.

.. destination-microsoft-dataverse-application-azure-steps-end

**To add your application to the Microsoft Power Platform**

.. destination-microsoft-dataverse-application-power-steps-start

#. Open the `Microsoft Power Platform console <https://admin.powerplatform.microsoft.com/>`__ |ext_link|, click **Environments**, and then click on your environment.
#. Click **Settings**, then **Users and permissions**, and then **Application users**.
#. Click **New app user**, and then select the application you just created, your business unit, and then under **Security roles** click the **Edit** button.
#. Select the following settings:

   **Service Reader**

   **Service Writer**

   and then click **Save**.
#. Click **Create**.

.. destination-microsoft-dataverse-application-power-steps-end


.. _destination-microsoft-dataverse-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Microsoft Dataverse**

.. destination-microsoft-dataverse-credentials-steps-start

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

       **Azure tenant ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dataverse-azure-tenant-id-start
             :end-before: .. credential-microsoft-dataverse-azure-tenant-id-end

       **Azure client ID and client secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dataverse-azure-client-id-and-secret-start
             :end-before: .. credential-microsoft-dataverse-azure-client-id-and-secret-end

.. destination-microsoft-dataverse-credentials-steps-end


.. _destination-microsoft-dataverse-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Microsoft Dataverse**

.. destination-microsoft-dataverse-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
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
          :alt: Step two.
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
          :alt: Step three.
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
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Power Apps environment region**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dataverse-powerapps-region-start
             :end-before: .. setting-microsoft-dataverse-powerapps-region-end

       **Power Apps environment name**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dataverse-powerapps-name-start
             :end-before: .. setting-microsoft-dataverse-powerapps-name-end

       **Dataverse table logical name**
          |checkmark-required| **Required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dataverse-table-logical-name-start
             :end-before: .. setting-microsoft-dataverse-table-logical-name-end

       **Truncate table?**
          |checkmark-required| **Required at orchestration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-dataverse-truncate-table-start
             :end-before: .. setting-microsoft-dataverse-truncate-table-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end

.. destination-microsoft-dataverse-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
