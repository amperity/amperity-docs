.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |destination-name| replace:: Salesforce Marketing Cloud Personalization
.. |plugin-name| replace:: SFTP
.. |what-send| replace:: CSV files
.. |email-plus-send| replace:: additional attributes
.. |filter-the-list| replace:: "sftp"
.. |sftp-type| replace:: **sftp**
.. |sftp-hostname| replace:: the hostname for your SFTP server, such as **sftp.evergage.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by the SFTP site were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_oracle_responsys|
.. |channel-link| replace:: Salesforce Marketing Cloud Personalization


.. meta::
    :description lang=en:
        Configure Amperity to send data to Salesforce Marketing Cloud Personalization.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Salesforce Marketing Cloud Personalization.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Marketing Cloud Personalization

==================================================
Send data to Marketing Cloud Personalization
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-marketing-cloud-personalization-start
   :end-before: .. term-salesforce-marketing-cloud-personalization-end

.. destination-salesforce-marketing-cloud-personalization-intro-start

Use |ext_salesforce_sfmc_personalization_etl_data_feeds| to send |what-send| to |destination-name| using the built-in |plugin-name| destination in Amperity.

.. important:: Review the |ext_salesforce_sfmc_personalization_formatting_requirements| before configuring Amperity.

.. destination-salesforce-marketing-cloud-personalization-intro-end

.. destination-salesforce-marketing-cloud-personalization-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-salesforce-marketing-cloud-personalization-get-details>`
#. :ref:`Add destination <destination-salesforce-marketing-cloud-personalization-add-destination>`
#. :ref:`Add data template <destination-salesforce-marketing-cloud-personalization-add-data-template>`

.. destination-salesforce-marketing-cloud-personalization-steps-to-send-end


.. _destination-salesforce-marketing-cloud-personalization-get-details:

Get details
==================================================

.. destination-salesforce-marketing-cloud-personalization-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The hostname, port number, username, and host public key.

       For passphrase credentials, the passphrase; for private key credentials, the private key.

       .. tip:: This information is available from a user credetials CSV file that is downloaded from |destination-name| *after* creating the SFTP site.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The remote folder to which Amperity will send data.

       .. important:: A "/" (forward slash) must be used as the first character for this value. For example: "/folder/name".

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Optional. The public key to use for PGP encryption.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Review the |ext_salesforce_sfmc_personalization_formatting_requirements| in |destination-name|, including:

       * A user profile object must be configured and enabled on the **Catalog and Profile Objects** page in |destination-name|.
       * The file that is sent from Amperity does not exceed |ext_salesforce_sfmc_personalization_limits|.
       * Meets all |ext_salesforce_sfmc_personalization_etl_file_requirements|.

       Review the schema requirements. The following fields must be present in the CSV file:

       * **userId**. A unique identifer for a customer. For example, an email address, a customer ID, or a unique identifier that already exists within |destination-name|.
       * **objectId**. A unique identifier for the user profile object.
       * **attribute:<attribute name>**. Custom attributes for the user profile object.
       * **relatedCatalogObject:<catalog object name>**. Catalog objects that are related to the user profile object.
       * **remove**. When "true" will remove the user profile object for "delta" updates.


.. destination-salesforce-marketing-cloud-personalization-get-details-end


.. _destination-salesforce-marketing-cloud-personalization-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-salesforce-marketing-cloud-personalization-add-destination-steps-start

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
          :start-after: .. destinations-add-credentials-sftp-start
          :end-before: .. destinations-add-credentials-sftp-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-sftp-start
          :end-before: .. destinations-intro-for-additional-settings-sftp-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-sftp.png
          :width: 500 px
          :alt: Update the settings for the SFTP destination.
          :align: left
          :class: no-scaled-link

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

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-sftp.png
          :width: 500 px
          :alt: Settings for SFTP destinations.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-sftp-start
          :end-before: .. destinations-destination-settings-sftp-end


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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-enable-start
          :end-before: .. destinations-business-users-enable-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-allow-start
          :end-before: .. destinations-business-users-allow-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-salesforce-marketing-cloud-personalization-add-destination-steps-end


.. _destination-salesforce-marketing-cloud-personalization-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. destination-salesforce-marketing-cloud-personalization-add-data-template-important-start

.. important:: The filename template **must** be defined using the following pattern:

   ::

      user-profile-objects-<objectTypeId>-<delta/replace>-<file number>.csv

   The "<delta/replace>" component refers to the type of update.

   #. Delta updates the user profile objects in the file. If a user profile object isn't included in the file, it remains unchanged. If the value of the "remove" column is "true", the user profile object is removed.

   #. Replace replaces all user profile objects for the object type for that user. If the user profile object isn't included in the file, that user profile object is deleted.

   Review the |ext_salesforce_sfmc_personalization_formatting_requirements| in |destination-name| for more information.

.. destination-salesforce-marketing-cloud-personalization-add-data-template-important-end

**To add a data template**

.. destination-salesforce-marketing-cloud-personalization-add-data-template-steps-start

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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-after-queries-only-start
          :end-before: .. destinations-data-template-save-after-queries-only-end

.. destination-salesforce-marketing-cloud-personalization-add-data-template-steps-end
