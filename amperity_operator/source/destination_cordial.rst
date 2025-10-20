.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Cordial
.. |destination-api| replace:: Cordial API
.. |plugin-name| replace:: "Cordial"
.. |credential-type| replace:: "cordial"
.. |required-credentials| replace:: "API key" and "API URL"
.. |audience-primary-key| replace:: "audience"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "cord"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Cordial.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Cordial.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Cordial

==================================================
Configure destinations for Cordial
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-cordial-start
   :end-before: .. term-cordial-end

.. destination-cordial-start

Use Amperity to manage contacts--attributes and list membership--in |destination-name| using the following REST APIs:

* `Account Contact Attributes <https://support.cordial.com/hc/en-us/articles/204570347-Account-Contact-Attributes>`__ |ext_link| to create contact attributes. Attributes that do not exist in |destination-name| are added as custom contact attributes.
* `Account Lists <https://support.cordial.com/hc/en-us/articles/204570497-Account-Lists>`__ |ext_link| to fetch, create, and clear account lists, to which contacts are associated. An account list is overwritten each time results are sent from Amperity. An email address is added when it is not already a contact, after which it is assigned the **subscribed** status. An email address that is already a contact retains its assigned subscription status.
* `Contact Imports <https://support.cordial.com/hc/en-us/articles/203886058-Contact-Imports>`__ |ext_link| to import contacts to |destination-name|, and then associate contacts to the account list.
* `Jobs <https://support.cordial.com/hc/en-us/articles/204570807-Jobs>`__ |ext_link| to monitor the import job for completion.

Build a query or segment that contains the **email** field, along with any other fields that you want created or updated in |destination-name| and represented as contact attributes.

.. destination-cordial-end

.. destination-cordial-get-details-alternate-note-start

.. note:: Amperity recommends using the |destination-api| to send |what-send| from Amperity to |destination-name|.

   However, if you prefer to send a CSV or JSON file instead of using the |destination-api| you may configure `Cordial Data Automations <https://support.cordial.com/hc/en-us/articles/14659667437453-Data-Jobs-and-Transformations-overview>`__ |ext_link|, and then enable that workflow using any of these destinations: :doc:`SFTP <destination_sftp>`, :doc:`Amazon S3 <destination_amazon_s3>`, or :doc:`Google Cloud Storage <destination_google_cloud_storage>`.

.. destination-cordial-get-details-alternate-note-end


.. _destination-cordial-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-cordial-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-cordial-api-key-start
             :end-before: .. credential-cordial-api-key-end

       **API URL**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-cordial-api-url-start
             :end-before: .. credential-cordial-api-url-end

       .. tip:: Use the `IP address for allowlists <https://docs.amperity.com/operator/send_data.html#ip-allowlists>`__ for Amperity to configure the allowlist for the |destination-api|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-list-name-start
             :end-before: .. setting-cordial-list-name-end

       **Subscription status**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-subscription-status-start
             :end-before: .. setting-cordial-subscription-status-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Cordial Rest API configuration**

       The following Cordial REST API methods must be enabled:

       ::

           GET /accountcontractattributes
           POST /accountcontractattributes

           GET /accountlists
           POST /accountlists
           PUT /accountlists/{key}/clear

           POST /contactimports

           GET /jobs/{id}

.. destination-cordial-get-details-end


.. _destination-cordial-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Cordial**

.. destination-cordial-credentials-steps-start

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

       **API key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-cordial-api-key-start
             :end-before: .. credential-cordial-api-key-end

       **API URL**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-cordial-api-url-start
             :end-before: .. credential-cordial-api-url-end

.. destination-cordial-credentials-steps-end


.. _destination-cordial-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Cordial**

.. destination-cordial-add-steps-start

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

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-list-name-start
             :end-before: .. setting-cordial-list-name-end

       **Subscription status**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-subscription-status-start
             :end-before: .. setting-cordial-subscription-status-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-cordial-add-steps-end


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
