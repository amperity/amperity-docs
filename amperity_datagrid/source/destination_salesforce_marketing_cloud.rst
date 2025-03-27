.. https://docs.amperity.com/internal/



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
        Configure Amperity to send customer profiles to Salesforce Marketing Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profiles to Salesforce Marketing Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send customer profiles to Salesforce Marketing Cloud

====================================================
Send customer profiles to Salesforce Marketing Cloud
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

.. destination-salesforce-marketing-cloud-howitworks-start

Amperity can send |what-send| with contact data to business units in |destination-name|. The |what-send| are uploaded to |destination-name| using SFTP, after which the Marketing Cloud SOAP API is used to manage data extensions and to move contacts data from the |what-send| into the data extensions.

.. destination-salesforce-marketing-cloud-howitworks-end

.. UNCOMMENT

.. .. image:: ../../images/destination-salesforce-marketing-cloud.png
..    :width: 600 px
..    :alt: Send contact data from Amperity to Salesforce Marketing Cloud.
..    :align: left
..    :class: no-scaled-link

.. destination-salesforce-marketing-cloud-howitworks-callouts-start

A |destination-name| destination works like this:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: left
          :class: no-scaled-link
     - Optional. Configure a data extension in |destination-name|.

       .. admonition:: What is a data extension?

          A `data extension <https://help.salesforce.com/s/articleView?id=sf.mc_cab_data_extensions.htm&type=5>`__ |ext_link| is a table that stores data about your contacts. The fields that are available from your data extension match the columns and/or attributes that are sent from Amperity.

          Within |destination-name|, use the data in the data extension as a data source. Run queries, pull a subset of contacts from the data extension, and then send offers to that subset of contacts.

       This step is optional because Amperity will manage the data extension as part of its workflow. If the data extension does not exist, Amperity will add it. If the data extension does exist, Amperity will update the contact data in that data extension.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: left
          :class: no-scaled-link
     - Configure permissions for the installed package to allow business units to read from and write to the data extension.

       .. admonition:: When does Amperity use an API?

          Amperity uses the `Marketing Cloud SOAP API <https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/soap_tech_articles_de.html>`__ |ext_link| to manage the installed package and manage the `import definition <https://help.salesforce.com/s/articleView?id=sf.mc_cab_imports.htm&type=5>`__ |ext_link| process, which gets the contact data from the |what-send| that were sent from Amperity and then either adds a data extension or updates an existing data extension.

       .. note:: You may configure Amperity to send |what-send| to |destination-name| using only SFTP. This will place the |what-send| in the configured SFTP location, but will require configuring the data extension and import definition, along with any process that moves that data from the SFTP location to the data extension.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: left
          :class: no-scaled-link
     - Use a query or segment to build a list of contacts.

       The fields that are sent from Amperity must match the fields that are defined in the schema for the data extension in |destination-name|.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - Configure the :ref:`Salesforce Marketing Cloud destination <destination-salesforce-marketing-cloud-add>` in Amperity.

       .. admonition:: Why does Amperity use SFTP?

          Amperity uses SFTP to transfer data to |destination-name|.

          |destination-name| has strict rate limits when using their APIs to manage contact data. These rate limits generally exceed the number of contacts that are in the lists that you will want to send to |destination-name|.

          Amperity uses SFTP to ensure that your contact lists can be successfully updated in |destination-name|, after which Amperity uses the Marketing Cloud SOAP API to make that list of contacts available to the configured data extension.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: left
          :class: no-scaled-link
     - Send a test from Amperity.

       .. important:: Be sure to send all fields from Amperity that will be required by the data extension in |destination-name|.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: left
          :class: no-scaled-link
     - From within |destination-name| verify the data that has been loaded to the data extension is correct and that you can run a query against it.

.. destination-salesforce-marketing-cloud-howitworks-callouts-end


.. _destination-salesforce-marketing-cloud-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-salesforce-marketing-cloud-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
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
          :align: left
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
          :align: left
          :class: no-scaled-link
     - **Business unit configuration**

       For each business unit to which data will be sent: the account ID for the business unit, the import location, and selecting the field to use as the primary key.

       .. note:: The account ID is also referred to as the member ID within |destination-name|.

       .. important:: Review the `Marketing Cloud File Location Guide <https://help.salesforce.com/articleView?id=sf.mc_overview_create_file_transfer_location.htm&type=5>`__ |ext_link| to configure a File Transfer Location with Location Type "Marketing Cloud Enhanced FTP Site Import Directory".


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: left
          :class: no-scaled-link
     - The :ref:`subscriber key <destination-salesforce-marketing-cloud-subscriber-key>` for |destination-name|. (The use of the subscriber key is recommended.)

       .. important:: A subscriber key is configured as the "primary key" for the destination. There are two options: using the |destination-name| subscriber key or using **email**. One of these options must be specified before the destination can send data to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 5.
          :align: left
          :class: no-scaled-link
     - Review the `Marketing Cloud SFTP Guide <https://help.salesforce.com/articleView?id=mc_es_enhanced_ftp_guide.htm>`__ |ext_link| to answer questions about configuring and managing |destination-name|.

       .. tip:: Configuration details for |destination-name| are available from within Salesforce.

          #. For the installed package, click **Setup** > **Platform tools** > **Aps** > **Installed packages**.
          #. For SFTP, click **Setup** > **Administration** > **Data management** > **FTP accounts**.

.. destination-salesforce-marketing-cloud-get-details-table-end


.. _destination-salesforce-marketing-cloud-subscriber-key:

Subscriber key
--------------------------------------------------

.. destination-salesforce-marketing-cloud-subscriber-key-start

The subscriber key is an identifier in |destination-name|. All data that is sent to |destination-name| must be associated to a subscriber key. Use the **primary key** field while configuring |destination-name| to specify the subscriber key to use for this destination.

The use of the subscriber key within Amperity will vary, depending on if the subscriber key is made available to Amperity as field provided by a |destination-name| data source:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - When a subscriber key is available, ensure that it is made available to the **Customer 360**, **Queries**, and **Segments** pages and that it may be included in queries and segments that will be sent to |destination-name|.

       Use a customer key semantic tag (e.g. "fk-salesforce-subscriber key") to identify the subscriber key in your data sources.

       .. tip:: Use an email address as the subscriber key if the subscriber key identifier is unavailable.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - The **primary key** field **must** be set to **subscriber_key** or **email** as part of the configuration of the data template that is used for this destination.

       .. caution:: A mismatch between the primary key in Amperity and the subscriber key in |destination-name| will cause duplicate records to be created.

.. destination-salesforce-marketing-cloud-subscriber-key-end


.. _destination-salesforce-marketing-cloud-sftp-password:

SFTP password expiration
--------------------------------------------------

.. destination-salesforce-marketing-cloud-sftp-password-start

The SFTP password for |destination-name| may be set to periodically expire. The default for SFTP passwords is 3 months. The SFTP password is configured in |destination-name| at **Setup** > **Settings** > **Security** > **Security Settings** > **Password Policies** > **Exclude FTP Users From Password Expiration**.

.. destination-salesforce-marketing-cloud-sftp-password-end


.. _destination-salesforce-marketing-cloud-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Salesforce Marketing Cloud**

.. destination-salesforce-marketing-cloud-credentials-steps-start

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


.. destination-salesforce-marketing-cloud-credentials-steps-end


.. _destination-salesforce-marketing-cloud-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Salesforce Marketing Cloud**

.. destination-salesforce-marketing-cloud-add-steps-start

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

       **Account ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-account-id-start
             :end-before: .. setting-salesforce-marketing-cloud-account-id-end

       **Import location**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-salesforce-marketing-cloud-import-location-start
             :end-before: .. setting-salesforce-marketing-cloud-import-location-end

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

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


.. destination-salesforce-marketing-cloud-add-steps-end


.. TODO: Add workflow resolutions from existing topics HERE.
