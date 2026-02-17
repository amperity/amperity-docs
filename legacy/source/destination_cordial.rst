.. https://docs.amperity.com/legacy/


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


==================================================
Send data to Cordial
==================================================

.. vale off

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_cordial.html>`__ |ext_link|.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-cordial-start
   :end-before: .. term-cordial-end

.. destination-cordial-start

Use Amperity to manage contacts--attributes and list membership--in |destination-name| using the following REST APIs:

* `Account Contract Attributes <https://support.cordial.com/hc/en-us/articles/204570347-Account-Contact-Attributes>`__ |ext_link| to create contact attributes. Attributes that do not exist in |destination-name| are added as custom contact attributes.
* `Account Lists <https://support.cordial.com/hc/en-us/articles/204570497-Account-Lists>`__ |ext_link| to fetch, create, and clear account lists, to which contacts are associated. An account list is overwritten each time results are sent from Amperity. An email address is added when it is not already a contact, after which it is assigned the **subscribed** status. An email address that is already a contact retains its assigned subscription status.
* `Contact Imports <https://support.cordial.com/hc/en-us/articles/203886058-Contact-Imports>`__ |ext_link| to import contacts to |destination-name|, and then associate contacts to the account list.
* `Jobs <https://support.cordial.com/hc/en-us/articles/204570807-Jobs>`__ |ext_link| to monitor the import job for completion.

Build a query or segment that contains the **email** field, along with any other fields that you want created or updated in |destination-name| and represented as contact attributes.

.. destination-cordial-end

.. destination-cordial-get-details-alternate-note-start

.. note:: Amperity recommends using the |destination-api| to send |what-send| from Amperity to |destination-name|.

   However, if you prefer to send a CSV or JSON file instead of using the |destination-api| you may configure `Cordial Data Automations <https://support.cordial.com/hc/en-us/articles/360029407471>`__ |ext_link|, and then enable that workflow using any of these destinations: :doc:`SFTP <destination_sftp>`, :doc:`Amazon S3 <destination_amazon_s3>`, or :doc:`Google Cloud Storage <destination_google_cloud_storage>`.

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
          :align: center
          :class: no-scaled-link
     - A |destination-api| key and the URL of the |destination-name| API.

       .. important:: Use the `IP address for allowlists <https://docs.amperity.com/operator/send_data.html#ip-allowlists>`__ |ext_link| for Amperity to configure the allowlist for the |destination-api|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: center
          :class: no-scaled-link
     - The name of the contacts list.

       .. important:: The list name is configured as part of the data template.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: center
          :class: no-scaled-link
     - The following REST API methods must be enabled:

       ::

           GET /accountcontactattributes
           POST /accountcontactattributes

           GET /accountlists
           POST /accountlists
           PUT /accountlists/{key}/clear

           POST /contactimports

           GET /jobs/{id}

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail four.
          :align: center
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
          :alt: Step one.
          :align: center
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
          :alt: Step two.
          :align: center
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
       * The URL of the |destination-name| API.

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
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
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
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
          :alt: Step one.
          :align: center
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
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2
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
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
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
          :align: center
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
          :align: center
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

#. Open the |destination-name| management console, and then `open Jobs <https://support.cordial.com/hc/en-us/articles/115008871127-Jobs-widget>`__ |ext_link|.
#. Find the job with the ID that matches the ID in the error message associated with this workflow action, and then view job details.

#. Download the rejected errors using the link in the job details. If the errors mention "missing required attributes" do one of the following:

   Update the attributes in |destination-name| to no longer be required.

   *or*

   Add the missing attributes for each treatment group that is associated with this campaign.
#. Open the **Campaigns** page, and then for each treatment group that is configured to send audiences to |destination-name|, edit the list of attributes to include all required attributes.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-cordial-workflow-actions-required-attributes-missing-campaigns-steps-start

**For orchestrations**

.. destination-cordial-workflow-actions-required-attributes-missing-orchestrations-steps-start

To resolve this error, verify the attributes that are required by |destination-name|, and then verify that the query used with this orchestration is returning all required attributes.

#. Open the |destination-name| management console, and then `open Jobs <https://support.cordial.com/hc/en-us/articles/115008871127-Jobs-widget>`__ |ext_link|.
#. Find the job with the ID that matches the ID in the error message associated with this workflow action, and then view job details.

#. Download the rejected errors using the link in the job details. If the errors mention "missing required attributes" do one of the following:

   Update the attributes in |destination-name| to no longer be required.

   *or*

   Add the missing attributes to the results that are returned by the query that is associated with this orchestration.
#. Open the **Queries** page, and then open the query used with this workflow. Update the query to return the list of attributes that are required by |destination-name|.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-cordial-workflow-actions-required-attributes-missing-orchestrations-steps-start


.. _destination-cordial-workflow-actions-unique-list-name-required:

Unique list name required
--------------------------------------------------

.. destination-cordial-workflow-actions-unique-list-name-required-start

|destination-name| `list names <https://support.cordial.com/hc/en-us/articles/115005528428-Lists>`__ |ext_link| must be unique.

To resolve this error, verify that the name of the list is unique.

#. Open the **Destinations** page, and then review the data template for the destination associated with this workflow error.
#. Verify that the value of the **List Name** setting is a unique value within |destination-name|.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-cordial-workflow-actions-unique-list-name-required-end
