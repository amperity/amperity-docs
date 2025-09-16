.. https://docs.amperity.com/operator/


.. |destination-name| replace:: ActiveCampaign
.. |plugin-name| replace:: "ActiveCampaign"
.. |credential-type| replace:: "active-campaign"
.. |required-credentials| replace:: "API key" and "URL"
.. |what-send| replace:: audience lists
.. |where-send| replace:: |destination-name|
.. |audience-primary-key| replace:: "email"
.. |filter-the-list| replace:: "acti"
.. |allow-for-what| replace:: audience lists
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Configure Amperity to send audience lists to ActiveCampaign.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audience lists to ActiveCampaign.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for ActiveCampaign

==================================================
Configure destinations for ActiveCampaign
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-active-campaign-start
   :end-before: .. term-active-campaign-end

.. destination-active-campaign-api-note-start

.. note:: This destination uses the `Active Campaign REST API <https://developers.activecampaign.com/reference/url>`__ |ext_link|.

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. allow-for-start
      :end-before: .. allow-for-end

   |destination-name| API is rate limited to 5 requests per second.

.. destination-active-campaign-api-note-end


.. _destination-active-campaign-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-active-campaign-get-details-table-start

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
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-active-campaign-api-key-start
             :end-before: .. credential-active-campaign-api-key-end

       **Base URL**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-active-campaign-url-start
             :end-before: .. credential-active-campaign-url-end


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

       **Group name**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-group-name-start
             :end-before: .. setting-active-campaign-group-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-group-name-access-start
             :end-before: .. setting-active-campaign-group-name-access-end

       **List name** (Required at orchestration)
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-list-name-start
             :end-before: .. setting-active-campaign-list-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-active-campaign-email-required-start
          :end-before: .. setting-active-campaign-email-required-end

.. destination-active-campaign-get-details-table-end


.. _destination-active-campaign-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for ActiveCampaign**

.. destination-active-campaign-credentials-steps-start

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

       **API key**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-active-campaign-api-key-start
             :end-before: .. credential-active-campaign-api-key-end

       **URL**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-active-campaign-url-start
             :end-before: .. credential-active-campaign-url-end

.. destination-active-campaign-credentials-steps-end


.. _destination-active-campaign-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for ActiveCampaign**

.. destination-active-campaign-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-active-campaign.png
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
          :alt: Step 3.
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
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Audience primary key**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Group name**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-group-name-start
             :end-before: .. setting-active-campaign-group-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-group-name-access-start
             :end-before: .. setting-active-campaign-group-name-access-end

       **List name** (Required at orchestration)
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-list-name-start
             :end-before: .. setting-active-campaign-list-name-end

       **Verbose logging?**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-active-campaign-verbose-logging-start
             :end-before: .. setting-active-campaign-verbose-logging-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-active-campaign-add-steps-end


.. _destination-active-campaign-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-active-campaign-workflow-actions-start

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
          :alt: The Workflow page, showing a workflow with errors.
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

       .. image:: ../../images/workflow-actions-active-campaign-group-name.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-active-campaign-workflow-actions-invalid-credentials`
       * :ref:`destination-active-campaign-workflow-actions-invalid-group-name`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-active-campaign-group-name-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-active-campaign-workflow-actions-end


.. _destination-active-campaign-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-active-campaign-workflow-actions-invalid-group-name:

Invalid group name
--------------------------------------------------

.. destination-active-campaign-workflow-actions-invalid-group-name-start

A `user group <https://help.activecampaign.com/hc/en-us/articles/115000090164#setting-user-permissions-create-user-groups-0-0>`__ |ext_link| defines which set of users within |destination-name| have permission to interact with contacts in a contact list. For example: managing tags, defining list exclusions, or running campaigns.

When the name of the user group defined in Amperity does not match the name of a user group defined in |destination-name|, Amperity will be unable to update the list of contacts for a contact list and a workflow action is shown.

.. destination-active-campaign-workflow-actions-invalid-group-name-end

.. destination-active-campaign-workflow-actions-invalid-group-name-steps-start

To resolve this error, verify the name of the user group in |destination-name|, and then update the data template in Amperity for the correct name of the user group.

#. Log in to |destination-name| as a user assigned who is assigned to the **Admin** permission.
#. Verify the name of the user group and/or create a user group with the name that is required by this workflow.
#. Verify the name of the user group that is defined in the data template used by this workflow. Update this value if required.
#. Return to the workflow action, and then click **Resolve** to retry.

.. destination-active-campaign-workflow-actions-invalid-group-name-steps-start
