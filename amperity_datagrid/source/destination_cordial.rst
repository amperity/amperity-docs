.. https://docs.amperity.com/datagrid/


.. |destination-name| replace:: Cordial
.. |destination-api| replace:: Cordial API
.. |plugin-name| replace:: Cordial
.. |what-send| replace:: audience lists
.. |email-plus-send| replace:: additional attributes
.. |filter-the-list| replace:: "cor"
.. |credential-type| replace:: **cordial**
.. |credential-details| replace:: the Cordial API key
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |sendto-link| replace:: |sendto_cordial|
.. |channel-link| replace:: |campaign_cordial|


.. meta::
    :description lang=en:
        Configure Amperity to send data to Cordial.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Cordial.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Cordial

==================================================
Send data to Cordial
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-cordial-start
   :end-before: .. term-cordial-end

.. destination-cordial-start

Use Amperity to manage contacts--attributes and list membership--in |destination-name| using the following REST APIs:

* |ext_cordial_api_account_contact_attributes| to create contact attributes. Attributes that do not exist in |destination-name| are added as custom contact attributes.
* |ext_cordial_api_account_lists| to fetch, create, and clear account lists, to which contacts are associated. An account list is overwritten each time results are sent from Amperity. An email address is added when it is not already a contact, after which it is assigned the **subscribed** status. An email address that is already a contact will retain its assigned subscription status.
* |ext_cordial_api_contact_imports| to import contacts to |destination-name|, and then associate contacts to the account list.
* |ext_cordial_api_jobs| to monitor the import job for completion.

Build a query or segment that contains the **email** field, along with any other fields that you want created or updated in |destination-name| and represented as contact attributes.

.. destination-cordial-end

.. destination-cordial-get-details-alternate-note-start

.. note:: Amperity recommends using the |destination-api| to send |what-send| from Amperity to |destination-name|.

   However, if you prefer to send a CSV or JSON file (one-time or recurring) instead of using the |destination-api| you may configure |ext_cordial_data_automations|, and then enable that workflow using any of these destinations: :doc:`SFTP <destination_sftp>`, :doc:`Amazon S3 <destination_amazon_s3>`, or :doc:`Google Cloud Storage <destination_google_cloud_storage>`.

.. destination-cordial-get-details-alternate-note-end

.. destination-cordial-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-cordial-get-details>`
#. :ref:`Add destination <destination-cordial-add-destination>`
#. :ref:`Add data template <destination-cordial-add-data-template>`

.. destination-cordial-steps-to-send-end


.. _destination-cordial-get-details:

Get details
==================================================

.. destination-cordial-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - A |destination-api| key and the URL for the |destination-name| API.

       .. important:: Use the |ext_amperity_allowlist_ip_address| for Amperity to configure the allowlist for the |destination-api|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The name of the contacts list.

       .. important:: The list name is configured as part of the data template.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The following REST API methods must be enabled:

       ::

           GET /accountcontractattributes
           POST /accountcontractattributes

           GET /accountlists
           POST /accountlists
           PUT /accountlists/{key}/clear

           POST /contactimports

           GET /jobs/{id}

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - A query or segment that returns the **email** field, along with any other fields that you want created or updated in |destination-name| and represented as contact attributes in |destination-name|.

.. destination-cordial-get-details-end


.. _destination-cordial-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-cordial-add-destination-steps-start

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

       * The |destination-api| key.
       * The URL for the |destination-name| API.

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
          :alt: Settings for Cordial.
          :align: left
          :class: no-scaled-link


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

.. destination-cordial-add-destination-steps-end


.. _destination-cordial-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-cordial-add-data-template-steps-start

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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-allow-campaigns-start
          :end-before: .. destinations-data-template-business-users-allow-campaigns-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end


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

.. destination-cordial-add-data-template-steps-end


.. _destination-cordial-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-cordial-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

       .. image:: ../../images/mockup-destinations-tab-workflow-error-sources.png
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
          :align: left
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
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-a-start
          :end-before: .. workflow-actions-common-table-section-three-a-end

       .. image:: ../../images/workflow-actions-cordial-unique-list-name.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-cordial-workflow-actions-invalid-credentials`
       * :ref:`destination-cordial-workflow-actions-required-attributes-missing`
       * :ref:`destination-cordial-workflow-actions-unique-list-name-required`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-cordial-unique-list-name-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-cordial-workflow-actions-end


.. _destination-cordial-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-cordial-workflow-actions-required-attributes-missing:

Required attributes are missing
--------------------------------------------------

.. destination-cordial-workflow-actions-required-attributes-missing-start

|destination-name| will reject audiences when required attributes are missing.

.. destination-cordial-workflow-actions-required-attributes-missing-end

**For campaigns**

.. destination-cordial-workflow-actions-required-attributes-missing-campaigns-steps-start

To resolve this error, verify the attributes that are required by |destination-name|, and then verify that the list of attributes is correct for each treatment group in this campaign that is sending data to |destination-name|.

#. Open the |destination-name| management console, and then |ext_cordial_jobs|.
#. Find the job with the ID that matches the ID in the error message associated with this workflow action, and then view job details.

#. Download the rejected errors using the link in the job details. If the errors mention "missing required attribute(s)" do one of the following:

   Update the attribute(s) in |destination-name| to no longer be required.

   *or*

   Add the missing attributes for each treatment group that is associated with this campaign.
#. Open the **Campaigns** page, and then for each treatment group that is configured to send audiences to |destination-name|, edit the list of attributes to include all required attributes.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-cordial-workflow-actions-required-attributes-missing-campaigns-steps-start

**For orchestrations**

.. destination-cordial-workflow-actions-required-attributes-missing-orchestrations-steps-start

To resolve this error, verify the attributes that are required by |destination-name|, and then verify that the query used with this orchestration is returning all required attributes.

#. Open the |destination-name| management console, and then |ext_cordial_jobs|.
#. Find the job with the ID that matches the ID in the error message associated with this workflow action, and then view job details.

#. Download the rejected errors using the link in the job details. If the errors mention "missing required attribute(s)" do one of the following:

   Update the attribute(s) in |destination-name| to no longer be required.

   *or*

   Add the missing attributes to the results that are returned by the query that is associated with this orchestration.
#. Open the **Queries** page, and then open the query used with this workflow. Update the query to return the list of attributes that are required by |destination-name|.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-cordial-workflow-actions-required-attributes-missing-orchestrations-steps-start


.. _destination-cordial-workflow-actions-unique-list-name-required:

Unique list name required
--------------------------------------------------

.. destination-cordial-workflow-actions-unique-list-name-required-start

|destination-name| |ext_cordial_lists| must be unique.

To resolve this error, verify that the name of the list is unique.

#. Open the **Destinations** page, and then review the data template for the destination associated with this workflow error.
#. Verify that the value of the **List Name** setting is a unique value within |destination-name|.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-cordial-workflow-actions-unique-list-name-required-end
