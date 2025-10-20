.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Oracle Eloqua
.. |plugin-name| replace:: "Oracle Eloqua"
.. |credential-type| replace:: "eloqua"
.. |required-credentials| replace:: "username", "password", and "company name"
.. |audience-primary-key| replace:: "C_EmailAddress"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "oracle"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Oracle Eloqua.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Oracle Eloqua.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Oracle Eloqua

==================================================
Configure campaigns for Oracle Eloqua
==================================================

.. campaign-oracle-eloqua-about-start

|destination-name| is an automation platform for email and SMS marketing. Use the Oracle Eloqua REST API to manage audiences in |destination-name|.

.. campaign-oracle-eloqua-about-end

.. campaign-oracle-eloqua-context-start

Send audiences from Amperity to manage `shared lists <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/SharedLists/SharedContactLists.htm>`__ |ext_link|. Shared lists are static lists of contacts that can be used across |destination-name|. Each shared list should contain a list of contacts with a defined relationship to the campaign or program that is managed from |destination-name|.

Amperity adds and remove audience members from a shared list, and then update any contact attributes that are associated with members of that shared list. The first audience that is sent from Amperity to |destination-name| should be to a new or empty shared list.

.. campaign-oracle-eloqua-context-end

.. campaign-oracle-eloqua-api-note-start

.. note:: The first audience that is sent from Amperity to |destination-name| should be to a new or empty shared list.

.. campaign-oracle-eloqua-api-note-end

.. campaign-oracle-eloqua-api-note-start

.. important:: This destination uses the `Bulk Loader API <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/Developers/BulkAPI/Reference/bulk-limits.htm>`__ |ext_link| to send shared lists to |destination-name|.

   Review the `Bulk API best practices <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/Developers/BulkAPI/BestPractices/best-practices.htm?Highlight=off-peak>`__ |ext_link| to help ensure that Amperity will be successful when importing your shared lists to |destination-name|.

.. campaign-oracle-eloqua-api-note-end


.. _campaign-oracle-eloqua-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-oracle-eloqua-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Username**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-username-start
             :end-before: .. credential-sftp-username-end

       **Password**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-eloqua-password-start
             :end-before: .. credential-oracle-eloqua-password-end

       **Company name**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-eloqua-company-name-start
             :end-before: .. credential-oracle-eloqua-company-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Shared list configuration**

       Provide the name of the `shared lists <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/SharedLists/SharedContactLists.htm>`__ |ext_link| to be managed by Amperity.

       Use **C_EmailAddress** as the primary key for the shared list.

       An email address that is mapped to the primary key is the only requirement for sending audiences to |destination-name| for use as a shared list. Additional attributes may be sent. Some must be mapped to the `default attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/ContactFieldsDefinitions.htm>`__ |ext_link|. `Custom attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/Tasks/CreatingContactFields.htm>`__ |ext_link| may be defined.

       Use filename templates to configure Amperity to support managing more than one shared list. For example a timestamp at the end

       ::

          Early_Purchasers_{{format:'MM-dd-yyyy'}}.csv

       creates a new shared list each time an audience is sent from Amperity. The shared list will always be titled "Early Purchasers", but have a unique datestamp.

       A campaign that is configured only for campaign name and group name

       ::

          {{ campaign_name }} - {{ group_name }}

       updates the same shared list each time the audience is sent from Amperity.

       .. caution:: You may add custom attributes to the shared list as long as each custom attribute is mapped to the database name that was assigned to the custom contact field by |destination-name|.

          This approach requires adding an empty shared list to |destination-name|, and then adding any custom contact fields to that shared list. This will generate the database name, which is typically, but not always, prefixed with **C_**.

          Use a query to build the results your brand wants to send to |destination-name|. Be sure to map each field in the query results to the database name in |destination-name|.

          A campaign must use the **Edit Attributes** dialog box to configure the attributes to be sent, along with ensuring the correct database type mapping from |destination-name| is applied to each field.

.. campaign-oracle-eloqua-get-details-end


.. _campaign-oracle-eloqua-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Oracle Eloqua**

.. campaign-oracle-eloqua-credentials-steps-start

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

       **Username**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sftp-username-start
             :end-before: .. credential-sftp-username-end

       **Password**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-eloqua-password-start
             :end-before: .. credential-oracle-eloqua-password-end

       **Company name**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-eloqua-company-name-start
             :end-before: .. credential-oracle-eloqua-company-name-end

.. campaign-oracle-eloqua-credentials-steps-end


.. _campaign-oracle-eloqua-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Oracle Eloqua**

.. campaign-oracle-eloqua-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
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
          :alt: Step three.
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
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Shared list name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-oracle-eloqua-shared-list-name-start
             :end-before: .. setting-oracle-eloqua-shared-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-oracle-eloqua-shared-list-name-caution-start
             :end-before: .. setting-oracle-eloqua-shared-list-name-caution-end

       **Audience primary key**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end


       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

.. campaign-oracle-eloqua-add-steps-end
