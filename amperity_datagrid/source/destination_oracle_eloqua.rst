.. https://docs.amperity.com/datagrid/


.. |destination-name| replace:: Oracle Eloqua
.. |plugin-name| replace:: Oracle Eloqua
.. |what-send| replace:: audiences
.. |filter-the-list| replace:: "ora"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: shared list name and primary key
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_oracle_eloqua|
.. |channel-link| replace:: |channel_oracle_eloqua|


.. meta::
    :description lang=en:
        Configure Amperity to send data to Oracle Eloqua.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Oracle Eloqua.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Oracle Eloqua

==================================================
Send audiences to Oracle Eloqua
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oracle-eloqua-start
   :end-before: .. term-oracle-eloqua-end

.. destination-oracle-eloqua-context-start

Send audiences from Amperity to manage `shared lists <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/SharedLists/SharedContactLists.htm>`__ |ext_link|. Shared lists are static lists of contacts that can be used across |destination-name|. Each shared list should contain a list of contacts with a clearly defined relationship to the campaign or program that is managed from |destination-name|.

Amperity will add and remove audience members from a shared list, and then update any contact attributes that are associated with members of that shared list.

.. destination-oracle-eloqua-context-end

.. destination-oracle-eloqua-api-note-start

.. note:: The first audience that is sent from Amperity to |destination-name| should be to a new or empty shared list.

.. destination-oracle-eloqua-api-note-end

.. destination-oracle-eloqua-api-note-start

.. important:: This destination uses the `Bulk Loader API <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/Developers/BulkAPI/Reference/bulk-limits.htm>`__ |ext_link| to send shared lists to |destination-name|.

   Review the `Bulk API best practices <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/Developers/BulkAPI/BestPractices/best-practices.htm?Highlight=off-peak>`__ |ext_link| to help ensure that Amperity will be successful when importing your shared lists to |destination-name|.

.. destination-oracle-eloqua-api-note-end

.. destination-oracle-eloqua-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-oracle-eloqua-get-details>`
#. :ref:`Add destination <destination-oracle-eloqua-add-destination>`
#. :ref:`Add data template <destination-oracle-eloqua-add-data-template>`

.. destination-oracle-eloqua-steps-to-send-end


.. _destination-oracle-eloqua-get-details:

Get details
==================================================

.. destination-oracle-eloqua-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Login information for |destination-name|. This includes:

       * **Username** The username for your |destination-name| account.
       * **Password** The password associated with your username.
       * **Company name** The name of your company, as used with your |destination-name| account.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The name of the shared list to be managed by Amperity.

       Use filename templates and/or data templates to configure Amperity to support managing more than one shared list. For example:

       * A timestamp at the end of a filename template --- **Early_Purchasers_{{format:'MM-dd-yyyy'}}.csv** --- will create a new shared list each time an audience is sent from Amperity. The shared list will always be titled "Early Purchasers", but will have a unique datestamp.
       * A campaign that is configured only for campaign name and group name --- **{{ campaign_name }} - {{ group_name }}** --- will update the same shared list each time the audience is sent from Amperity.

       .. caution:: You may add custom attributes to the shared list as long as each custom attribute is mapped to the database name that was assigned to the custom contact field by |destination-name|.

          This approach requires adding an empty shared list to |destination-name|, and then adding any custom contact fields to that shared list. This will generate the database name, which is typically (but not always) prefixed with **C_**.

          Use a query to build the results your brand wants to send to |destination-name|. Be sure to map each field in the query results to the database name in |destination-name|.

          A campaign must use the **Edit Attributes** dialog box to configure the attributes to be sent, along with ensuring the correct database type mapping from |destination-name| is applied to each field.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The primary key for the shared list: **C_EmailAddress**.

       An email address (mapped to the database type **C_EmailAddress**) is the only requirement for sending audiences to |destination-name| for use as a shared list. Additional attributes may be sent. Some must be mapped to the `default attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/ContactFieldsDefinitions.htm>`__ |ext_link|; `custom attributes <https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/ContactFields/Tasks/CreatingContactFields.htm>`__ |ext_link| may be defined.

.. destination-oracle-eloqua-get-details-end


.. _destination-oracle-eloqua-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-oracle-eloqua-add-destination-steps-start

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

       * **Username** The username for your |destination-name| account.
       * **Password** The password associated with your username.
       * **Company name** The name of your company, as used with your |destination-name| account.

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
          :alt: Settings for Dynamics 365 Marketing.
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Shared List Name**
            - The name of the shared list in |destination-name|. If the shared list does not exist, Amperity will create it.

              .. important:: Amperity does not create custom attributes for a shared list. A shared list that contains custom attributes must be created in |destination-name| along with any custom attributes before Amperity can send data.

          * - **Audience Primary Key**
            - This value must be set to **C_EmailAddress**.


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

.. destination-oracle-eloqua-add-destination-steps-end


.. _destination-oracle-eloqua-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-oracle-eloqua-add-data-template-steps-start

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
          :start-after: .. destinations-data-template-save-after-start
          :end-before: .. destinations-data-template-save-after-end

.. destination-oracle-eloqua-add-data-template-steps-end
