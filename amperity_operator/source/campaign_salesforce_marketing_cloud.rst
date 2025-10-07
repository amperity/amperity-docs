.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Salesforce Marketing Cloud
.. |plugin-name| replace:: "Salesforce Marketing Cloud"
.. |credential-type| replace:: "sfmc-sftp"
.. |required-credentials| replace:: "username", "hostname", and "passphrase"
.. |what-send| replace:: CSV files
.. |where-send| replace:: |destination-name|
.. |sftp-hostname| replace:: "[hostname].ftp.marketingcloudops.com"
.. |remote-folder| replace:: "/folder"
.. |sftp-port| replace:: "22"
.. |filter-the-list| replace:: "sales"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Salesforce Marketing Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Salesforce Marketing Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Salesforce Marketing Cloud

====================================================
Configure campaigns for Salesforce Marketing Cloud
====================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-marketing-cloud-start
   :end-before: .. term-salesforce-marketing-cloud-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-configure-start
   :end-before: .. setting-common-file-configure-end


.. TODO: Keep the How it works + Subscriber key + SFTP password expiration sections.

How this destination works
==================================================

.. campaign-salesforce-marketing-cloud-howitworks-start

Amperity can send |what-send| with contact data to business units in |destination-name|. The |what-send| are uploaded to |destination-name| using SFTP, after which the Marketing Cloud REST API is used to manage data extensions and to move contacts data from the |what-send| into the data extensions.

.. campaign-salesforce-marketing-cloud-howitworks-end

.. UNCOMMENT

.. .. image:: ../../images/destination-salesforce-marketing-cloud.png
..    :width: 600 px
..    :alt: Send contact data from Amperity to Salesforce Marketing Cloud.
..    :align: left
..    :class: no-scaled-link

.. campaign-salesforce-marketing-cloud-howitworks-callouts-start

A |destination-name| destination works like this:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Optional. Configure a data extension in |destination-name|.

       .. admonition:: What is a data extension?

          A `data extension <https://help.salesforce.com/s/articleView?id=sf.mc_cab_data_extensions.htm&type=5>`__ |ext_link| is a table that stores data about your contacts. The fields that are available from your data extension match the columns and attributes that are sent from Amperity.

          Within |destination-name|, use the data in the data extension as a data source. Run queries, pull a subset of contacts from the data extension, and then send offers to that subset of contacts.

       This step is optional because Amperity manages the data extension as part of its workflow. If the data extension does not exist, Amperity adds it. If the data extension does exist, Amperity updates the contact data in that data extension.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Configure permissions for the installed package to allow business units to read from and write to the data extension.

       .. note:: You may configure Amperity to send |what-send| to |destination-name| using only SFTP. This places the |what-send| in the configured SFTP location, but requires configuring the data extension and import definition, along with any process that moves that data from the SFTP location to the data extension.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Use a query or segment to build a list of contacts.

       The fields that are sent from Amperity must match the fields that are defined in the schema for the data extension in |destination-name|.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Configure the :ref:`Salesforce Marketing Cloud destination <destination-salesforce-marketing-cloud-add>` in Amperity.

       .. admonition:: Why does Amperity use SFTP?

          Amperity uses SFTP to transfer data to |destination-name|.

          |destination-name| has strict rate limits when using their APIs to manage contact data. These rate limits exceed the number of contacts that are in the lists that you send to |destination-name|.

          Amperity uses SFTP to ensure that your contact lists can be successfully updated in |destination-name|, after which Amperity uses the Marketing Cloud REST API to make that list of contacts available to the configured data extension.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Send a test from Amperity.

       .. important:: Be sure to send all fields from Amperity that is required by the data extension in |destination-name|.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - From within |destination-name| verify the data that has been loaded to the data extension is correct and that you can run a query against it.

.. campaign-salesforce-marketing-cloud-howitworks-callouts-end


.. _campaign-salesforce-marketing-cloud-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-salesforce-marketing-cloud-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-get-details-passphrase-start
          :end-before: .. credential-get-details-passphrase-end

       **API client ID and client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-marketing-cloud-api-client-secret-start
             :end-before: .. credential-salesforce-marketing-cloud-api-client-secret-end

       **API authentication subdomain**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-marketing-cloud-api-subdomain-start
             :end-before: .. credential-salesforce-marketing-cloud-api-subdomain-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-marketing-cloud-api-subdomain-base-uri-start
             :end-before: .. credential-salesforce-marketing-cloud-api-subdomain-base-uri-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Data extension configuration**

       Within |destination-name|, configure the installed package to allow business units:

       #. Apply **Read** and **Write** permissions to the data extension.
       #. Apply **Read**, **Write**, and **Execute** permissions for Automations.

       .. important:: Each installed package is configured to have access to one business unit *or* multiple business units, depending on the desired workflow.

          Configure a data template for each busines unit to which you want to send data. When a single installed package has permissions to multiple business units, you must configure a data template for each business unit.

          Amperity cannot send data to a shared business unit in |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Business unit configuration**

       For each business unit to which data is sent: the account ID for the business unit, the import location, and selecting the field to use as the primary key.

       .. note:: The account ID is also referred to as the member ID within |destination-name|.

       .. important:: Review the `Marketing Cloud File Location Guide <https://help.salesforce.com/articleView?id=sf.mc_overview_create_file_transfer_location.htm&type=5>`__ |ext_link| to configure a File Transfer Location with Location Type "Marketing Cloud Enhanced FTP Site Import Directory".


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - The :ref:`subscriber key <destination-salesforce-marketing-cloud-subscriber-key>` for |destination-name|. (The use of the subscriber key is recommended.)

       .. important:: A subscriber key is configured as the "primary key" for the destination. There are two options: using the |destination-name| subscriber key or using **email**. One of these options must be specified before the destination can send data to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 5.
          :align: center
          :class: no-scaled-link
     - Review the `Marketing Cloud SFTP Guide <https://help.salesforce.com/articleView?id=mc_es_enhanced_ftp_guide.htm>`__ |ext_link| to answer questions about configuring and managing |destination-name|.

       .. tip:: Configuration details for |destination-name| are available from within Salesforce.

          #. For the installed package, click **Setup** > **Platform tools** > **Aps** > **Installed packages**.
          #. For SFTP, click **Setup** > **Administration** > **Data management** > **FTP accounts**.

.. campaign-salesforce-marketing-cloud-get-details-table-end


.. _campaign-salesforce-marketing-cloud-subscriber-key:

Subscriber key
--------------------------------------------------

.. campaign-salesforce-marketing-cloud-subscriber-key-start

The subscriber key is an identifier in |destination-name|. All data that is sent to |destination-name| must be associated to a subscriber key. Use the **primary key** field while configuring |destination-name| to specify the subscriber key to use for this destination.

The use of the subscriber key within Amperity varies, depending on if the subscriber key is made available to Amperity as field provided by a |destination-name| data source:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: center
          :class: no-scaled-link
     - When a subscriber key is available, ensure that it is made available to the **Customer 360**, **Queries**, and **Segments** pages and that it may be included in queries and segments that is sent to |destination-name|.

       Use a customer key semantic tag, such as "fk-salesforce-subscriber key", to identify the subscriber key in your data sources.

       .. tip:: Use an email address as the subscriber key if the subscriber key identifier is unavailable.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: center
          :class: no-scaled-link
     - The **primary key** field **must** be set to **subscriber_key** or **email** as part of the configuration of the data template that is used for this destination.

       .. caution:: A mismatch between the primary key in Amperity and the subscriber key in |destination-name| will cause duplicate records to be created.

.. campaign-salesforce-marketing-cloud-subscriber-key-end


.. _campaign-salesforce-marketing-cloud-sftp-password:

SFTP password expiration
--------------------------------------------------

.. campaign-salesforce-marketing-cloud-sftp-password-start

The SFTP password for |destination-name| may be set to periodically expire. The default for SFTP passwords is 3 months. The SFTP password is configured in |destination-name| at **Setup** > **Settings** > **Security** > **Security Settings** > **Password Policies** > **Exclude FTP Users From Password Expiration**.

.. campaign-salesforce-marketing-cloud-sftp-password-end


.. _campaign-salesforce-marketing-cloud-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Salesforce Marketing Cloud**

.. campaign-salesforce-marketing-cloud-credentials-steps-start

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

       **API client ID and client secret**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-marketing-cloud-api-client-secret-start
             :end-before: .. credential-salesforce-marketing-cloud-api-client-secret-end

       **API authentication subdomain**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-salesforce-marketing-cloud-api-subdomain-start
             :end-before: .. credential-salesforce-marketing-cloud-api-subdomain-end

       **Hostname**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-hostname-start
             :end-before: .. credential-sftp-hostname-end

       **Passphrase**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-passphrase-start
             :end-before: .. credential-sftp-passphrase-end

       **Username**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-username-start
             :end-before: .. credential-sftp-username-end


.. campaign-salesforce-marketing-cloud-credentials-steps-end


.. _campaign-salesforce-marketing-cloud-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Salesforce Marketing Cloud**

.. campaign-salesforce-marketing-cloud-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-sftp.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
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
          :alt: Step 3.
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
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Account ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-account-id-start
             :end-before: .. setting-salesforce-marketing-cloud-account-id-end

       **Folder name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-folder-name-start
             :end-before: .. setting-salesforce-marketing-cloud-folder-name-end

       **Primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-primary-key-start
             :end-before: .. setting-salesforce-marketing-cloud-primary-key-end

       **Subscriber field**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-subscriber-field-start
             :end-before: .. setting-salesforce-marketing-cloud-subscriber-field-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-subscriber-field-important-start
             :end-before: .. setting-salesforce-marketing-cloud-subscriber-field-important-end

       **Append data**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-append-data-start
             :end-before: .. setting-salesforce-marketing-cloud-append-data-end

       **Data extension name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-data-extension-name-start
             :end-before: .. setting-salesforce-marketing-cloud-data-extension-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-data-extension-name-context-campaigns-start
             :end-before: .. setting-salesforce-marketing-cloud-data-extension-name-context-campaigns-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-data-extension-name-context-orchestrations-start
             :end-before: .. setting-salesforce-marketing-cloud-data-extension-name-context-orchestrations-end

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
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end


.. campaign-salesforce-marketing-cloud-add-steps-end


.. _campaign-salesforce-marketing-cloud-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. campaign-salesforce-marketing-cloud-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

       .. image:: ../../images/mockup-destinations-tab-workflow-error.png
          :width: 500 px
          :alt: Review a notifications error.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-b-start
          :end-before: .. workflow-actions-common-table-section-one-b-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-two-start
          :end-before: .. workflow-actions-common-table-section-two-end

       .. image:: ../../images/mockups-workflow-failed.png
          :width: 500 px
          :alt: The workflow tab, showing a workflow with errors.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-a-start
          :end-before: .. workflow-actions-common-table-section-three-a-end

       .. image:: ../../images/workflow-actions-sfmc-nopk.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-salesforce-marketing-cloud-workflow-actions-import-wrong-type`
       * :ref:`destination-salesforce-marketing-cloud-workflow-actions-import-wrong-location`
       * :ref:`destination-salesforce-marketing-cloud-workflow-actions-incorrect-extension-name`
       * :ref:`destination-salesforce-marketing-cloud-workflow-actions-incorrect-folder`
       * :ref:`destination-salesforce-marketing-cloud-workflow-actions-invalid-credentials`
       * :ref:`destination-salesforce-marketing-cloud-workflow-actions-missing-primary-key`
       * :ref:`destination-salesforce-marketing-cloud-workflow-actions-sftp-unavailable`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-sfmc-nopk-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. campaign-salesforce-marketing-cloud-workflow-actions-end


.. _campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-type:

Import location has wrong type
--------------------------------------------------

.. campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-type-start

The import location within the |destination-name| SFTP site must be set to "Enhanced FTP Site Import Directory", which is the standard location type for file imports within |destination-name|. If this location is not set to the standard location type for file imports, Amperity will be unable to send data.

.. campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-type-end

.. campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-type-steps-start

To resolve this error, you must verify that the import directory within |destination-name| is set to "Enhanced FTP Site Import Directory".

#. Open the `Salesforce Marketing Cloud management console <https://mc.exacttarget.com/cloud/>`__ |ext_link|, find the `file location <https://help.salesforce.com/s/articleView?id=sf.mc_overview_create_file_transfer_location.htm&type=5>`__ |ext_link|, and then verify that it is configured for the "Enhanced FTP Site Import Directory" location type.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-type-steps-end


.. _campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-location:

Import location not found
--------------------------------------------------

.. campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-location-start

The name of the directory into which Amperity adds data must be discoverable to Amperity. If Amperity cannot find that directory, CSV files is not uploaded to the |destination-name| SFTP site.

.. campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-location-end

.. campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-location-steps-start

To resolve this error, you must ensure that the import location within the |destination-name| SFTP site matches the import location that is configured in Amperity.

#. Verify import location within |destination-name|.
#. Verify import location as it is configured for the destination within Amperity. Make any necessary changes.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-salesforce-marketing-cloud-workflow-actions-import-wrong-location-steps-end


.. _campaign-salesforce-marketing-cloud-workflow-actions-incorrect-extension-name:

Incorrect data extension name
--------------------------------------------------

.. campaign-salesforce-marketing-cloud-workflow-actions-incorrect-extension-name-start

The name of a data extension must be unique within |destination-name|, should use underscores ( _ ) instead of spaces, and may not contain *any* of the following characters:

::

   ! @ # $ % ^ * ( ) = { } [ ] \ . < > / " : ? | , &

The name of a data extension in |destination-name| must be globally unique across folders in |destination-name| *and also* must match the primary key of that data extension, as it is configured in Amperity.

.. important:: You cannot change the primary key that is associated with a data extension from within |destination-name|.

.. campaign-salesforce-marketing-cloud-workflow-actions-incorrect-extension-name-end

.. campaign-salesforce-marketing-cloud-workflow-actions-incorrect-extension-name-steps-start

To resolve this error, you must delete or rename the data extension in |destination-name|, and then re-apply the primary key by resending the workflow from Amperity.

#. Open the `Salesforce Marketing Cloud management console <https://mc.exacttarget.com/cloud/>`__ |ext_link|, and then `delete or rename the data extension <https://help.salesforce.com/s/articleView?id=sf.mc_cab_data_extensions.htm&type=5>`__ |ext_link|.
#. Open the data template that is associated with this workflow.
#. Edit the data extension name in the data template so that its name is globally unique within |destination-name|, and then save the data template.

   .. tip:: The name of the data extension may require updating in |destination-name|.

      **To update the data extension in Salesforce Marketing Cloud**

      #. Open the `Salesforce Marketing Cloud management console <https://mc.exacttarget.com/cloud/>`__ |ext_link|.
      #. Select **Audience Builder**, and then choose **Contact Builder**.
      #. Open **Data Extensions**.
      #. Search for the data extension for which this error is associated, and then rename the data extension or delete the data extension.

#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-salesforce-marketing-cloud-workflow-actions-incorrect-extension-name-steps-end


.. _campaign-salesforce-marketing-cloud-workflow-actions-incorrect-folder:

Incorrect folder
--------------------------------------------------

.. campaign-salesforce-marketing-cloud-workflow-actions-incorrect-folder-start

The name of the directory within the |destination-name| SFTP site must match the folder name that is configured in Amperity. When the folder name does not match, the Marketing Cloud REST API is unable to get CSV files from that directory and the data extension is not updated.

.. campaign-salesforce-marketing-cloud-workflow-actions-incorrect-folder-end

.. campaign-salesforce-marketing-cloud-workflow-actions-incorrect-folder-steps-start

To resolve this error, you must ensure that the name of the folder name within the |destination-name| SFTP site matches the folder name that is configured in Amperity.

#. Verify the folder name within |destination-name|.
#. Verify the folder name as it is configured for the destination within Amperity. Make any necessary changes.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-salesforce-marketing-cloud-workflow-actions-incorrect-folder-steps-end


.. _campaign-salesforce-marketing-cloud-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end

.. campaign-salesforce-marketing-cloud-workflow-actions-invalid-credentials-note-start

.. note:: In some situations the user account that is associated with the Amperity workflow requires a new password and security token. When a new password and security token are created in |destination-name|, be sure to update the credentials for this workflow in Amperity.

.. campaign-salesforce-marketing-cloud-workflow-actions-invalid-credentials-note-end


.. _campaign-salesforce-marketing-cloud-workflow-actions-missing-primary-key:

Missing primary key
--------------------------------------------------

.. campaign-salesforce-marketing-cloud-workflow-actions-missing-primary-key-start

The **primary_key** field is typically used to specify the :ref:`subscriber key <destination-salesforce-marketing-cloud-subscriber-key>` that is used with this destination.

There are two options: using the |destination-name| subscriber key or using email addresses. One of these options must be specified before Amperity can send data to |destination-name|.

.. campaign-salesforce-marketing-cloud-workflow-actions-missing-primary-key-end

.. campaign-salesforce-marketing-cloud-workflow-actions-missing-primary-key-steps-start

To resolve this error, you must configure the primary key.

#. Open the Amperity **Credentials** page in a new tab.
#. For a query, open the **Queries** page, and then update the query to return the field -- **subscriber_key** or **email** -- that matches the **Primary Key** setting in the data template. Validate, and then activate the query.

   For a campaign, open the **Campaigns** page, and then update the campaign and ensure the primary key is in the list of attributes that are sent to |destination-name|. Activate the campaign.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-salesforce-marketing-cloud-workflow-actions-missing-primary-key-steps-end


.. _campaign-salesforce-marketing-cloud-workflow-actions-sftp-unavailable:

SFTP unavailable
--------------------------------------------------

.. campaign-salesforce-marketing-cloud-workflow-actions-sftp-unavailable-start

Amperity must be able to connect to the SFTP site that is used with |destination-name|.

.. note:: An SFTP site may be unavailable even when Amperity is configured correctly. For example, the SFTP site is down or there is not enough free space available within the SFTP site. Amperity cannot send data to an SFTP site that is unavailable.

.. campaign-salesforce-marketing-cloud-workflow-actions-sftp-unavailable-end

.. campaign-salesforce-marketing-cloud-workflow-actions-sftp-unavailable-steps-start

To resolve this error, you must verify the configuration settings for SFTP.

#. Open the Amperity **Credentials** page in a new tab.
#. Find the credentials for the SFTP site that is associated with |destination-name|, and then verify the configuration for the hostname, username, and passphrase. Make any necessary changes.

   .. note:: If the SFTP site is unavailable due to external reasons, such as not enough free space or the SFTP site is down, you must resolve those issues before Amperity is able to send data to that SFTP site.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-salesforce-marketing-cloud-workflow-actions-sftp-unavailable-steps-end
