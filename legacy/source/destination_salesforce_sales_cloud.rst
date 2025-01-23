.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Salesforce Sales Cloud
.. |plugin-name| replace:: Salesforce Sales Cloud
.. |what-send| replace:: customer data
.. |filter-the-list| replace:: "sales"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by |destination-name| were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


==================================================
Send data to Salesforce Sales Cloud
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-sales-cloud-start
   :end-before: .. term-salesforce-sales-cloud-end

.. destination-salesforce-sales-cloud-api-note-start

.. note:: This destination uses the `Salesforce Sales Cloud SOAP API <https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_intro.htm>`__ |ext_link|.

.. destination-salesforce-sales-cloud-api-note-end

.. destination-salesforce-sales-cloud-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-salesforce-sales-cloud-get-details>`
#. :ref:`Add destination <destination-salesforce-sales-cloud-add-destination>`
#. :ref:`Add data template <destination-salesforce-sales-cloud-add-data-template>`

.. destination-salesforce-sales-cloud-steps-to-send-end


.. _destination-salesforce-sales-cloud-get-details:

Get details
==================================================

.. destination-salesforce-sales-cloud-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The username and password of a Salesforce account configured for API access.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The |destination-name| security token that belongs to username. (The security token is not required if IP range policies are configured from the Salesforce admin console.)

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The scheme and host for a custom |destination-name| URL, if used by customer.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - If Amperity will send data to a sandbox instance.

.. destination-salesforce-sales-cloud-get-details-end

.. destination-salesforce-sales-cloud-get-details-account-info-start

.. admonition:: How do I find |destination-name| account information?

   You can find all of this information by logging into your |destination-name| admin console and by viewing the URL for your instance of |destination-name|.

.. destination-salesforce-sales-cloud-get-details-account-info-end


.. _destination-salesforce-sales-cloud-build-query:

Build query
==================================================

.. destination-salesforce-sales-cloud-build-query-start

You will need to build a query that outputs fields that can be mapped to |destination-name|.

.. destination-salesforce-sales-cloud-build-query-end


.. _destination-salesforce-sales-cloud-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-salesforce-sales-cloud-add-destination-steps-start

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

       * Username and password
       * Security token associated with the username

         .. note:: The security token is not required if IP range policies are configured from the Salesforce admin console.

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
          :alt: Settings for Salesforce Sales Cloud.
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Sandbox?**
            - Optional. Select this option if the destination is a sandbox instance (and not a production instance).

              .. note:: A sandbox instance is ignored when a custom URL for |destination-name| logins is used.

          * - **Custom URL?**
            - Optional. The custom URL for |destination-name| logins requires only the scheme (``http://`` or ``https://``) and hostname parts of the URL. For example: ``https://<hostname>`` or ``http://<hostname>``. The rest of the path is added automatically by Amperity.

          * - **Salesforce object**
            - The name of the object in |destination-name| to which Amperity will send data.


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


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-salesforce-sales-cloud-add-destination-steps-end


.. _destination-salesforce-sales-cloud-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-salesforce-sales-cloud-add-data-template-steps-start

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
     - Under **Template Settings**, indicate if the destination is a sandbox instance, enter the custom URL for Salesforce logins (if used), the name of the object in Salesforce to which Amperity will send data, the type of operation to perform, the external ID field (which acts as the primary key in the Salesforce object and is used by Amperity to identify which objects require updates for "Upsert" operations), if data should be loaded in parallel, and if NULL values should be used when fields are empty.

       The custom URL for Salesforce logins requires only the scheme (http:// or https://) and hostname parts of the URL. For example: "https://<hostname>" or "http://<hostname>". The rest of the path is added automatically by Amperity.

       .. note:: A sandbox instance is ignored when a custom URL for Salesforce logins is used.

       The operation may be one of the following: "Insert", "Upsert" (recommended), "Update", or "Delete". Upsert operations will insert a new record *or* update an existing record, whereas insert and update operations insert or update (and not both).

       The external ID should be set to **Amperity_ID__c**. (The **__c** identifies the field as a custom field in the Salesforce object.)

       When enabled, NULL values in data sent from Amperity will be ignored during "Upsert" operations. If a field from Amperity is NULL and there is a value in the corresponding Salesforce object, the value in the Salesforce object will be preserved.

       .. caution:: Enabling parallelism may cause Salesforce to process batches in parallel. This *may* improve performance, but comes with the risk of introducing failures due to locking. It's possible for more than one batch to attempt to obtain a lock on the same row, causing one (or both) batches to fail.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
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

.. destination-salesforce-sales-cloud-add-data-template-steps-end
