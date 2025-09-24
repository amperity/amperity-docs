.. https://docs.amperity.com/operator/


.. |destination-name| replace:: LinkedIn DMP
.. |destination-api| replace:: LinkedIn Marketing API
.. |plugin-name| replace:: "LinkedIn DMP"
.. |credential-type| replace:: "LinkedIn-DMP"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: customer profiles
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "link"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours

.. meta::
    :description lang=en:
        Configure Amperity to send customer profiles to LinkedIn DMP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profiles to LinkedIn DMP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for LinkedIn DMP

==================================================
Configure destinations for LinkedIn DMP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-linkedin-dmp-start
   :end-before: .. term-linkedin-dmp-end

.. destination-linkedin-dmp-start

Use the |destination-name| connector to build audiences in Amperity, and then activate those audiences in |destination-name| to members of LinkedIn.

.. destination-linkedin-dmp-end

.. destination-linkedin-dmp-about-start

This connector automates uploading data into the |destination-name| as a CSV file of contacts to match with LinkedIn members, letting you create new audience segments to target specific accounts for LinkedIn advertising campaigns.

The CSV file may contain the following contact information fields:

* **email**
* **title**
* **employeecountry**
* **company**

The CSV file must have between 300 and 300,000 contacts.

.. destination-linkedin-dmp-about-end

.. destination-linkedin-dmp-api-note-start

.. note:: This destination uses the `LinkedIn Marketing API <https://learn.microsoft.com/en-us/linkedin/marketing/matched-audiences/create-and-manage-list-uploads?view=li-lms-2025-01&tabs=http>`__ |ext_link|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-linkedin-dmp-api-note-end


.. _destination-linkedin-dmp-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-linkedin-dmp-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

       **Permissions**
          |checkmark-required| **Required**

          The LinkedIn account of the user configuring this connector must have access to the Advertising API, which will give them the necessary **rw_ads** and **r_ads** OAuth scopes.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Account ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-linkedin-dmp-account-id-start
             :end-before: .. setting-linkedin-dmp-account-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Identifier type**

          .. include:: ../../shared/destination_settings.rst
            :start-after: .. setting-linkedin-dmp-identifier-type-start
            :end-before: .. setting-linkedin-dmp-identifier-type-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - **Dataset size requirements**

       LinkedIn requires the uploaded dataset to be `between 300 and 300,000 rows. <https://learn.microsoft.com/en-us/linkedin/marketing/matched-audiences/create-and-manage-list-uploads?view=li-lms-2025-01&tabs=curl#content-requirements-1>`__ |ext_link|

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 5.
          :align: center
          :class: no-scaled-link
     - **List attach limit**

       A given segment `can only have one list attached to it. <https://learn.microsoft.com/en-us/linkedin/marketing/matched-audiences/create-and-manage-list-uploads?view=li-lms-2025-01&tabs=http#attach-list-to-dmp-segment>`__ |ext_link| Updating a segment deletes the current list and attaches the new list.


.. _destination-linkedin-dmp-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for LinkedIn DMP**

.. destination-linkedin-dmp-credentials-steps-start

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

       **Refresh token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

       **Permissions**
          |checkmark-required| **Required**

          The LinkedIn account of the user configuring this connector must have access to the Advertising API, which will give them the necessary **rw_ads** and **r_ads** OAuth scopes.

.. destination-linkedin-dmp-credentials-steps-end


.. _destination-linkedin-dmp-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-linkedin-dmp-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for LinkedIn DMP**

.. destination-linkedin-dmp-add-steps-start

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

       .. image:: ../../images/mockup-destinations-add-01-select-destination-linkedin-dmp.png
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

       **Account ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-linkedin-dmp-account-id-start
             :end-before: .. setting-linkedin-dmp-account-id-end

       **Identifier type** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-linkedin-dmp-identifier-type-start
             :end-before: .. setting-linkedin-dmp-identifier-type-end

       **Segment name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-linkedin-dmp-segment-name-start
             :end-before: .. setting-linkedin-dmp-segment-name-end

       **Segment description** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-linkedin-dmp-segment-description-start
             :end-before: .. setting-linkedin-dmp-segment-description-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-linkedin-dmp-add-steps-end


.. _destination-linkedin-dmp-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-braze-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-microsoft-ads-not-authorized.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-linkedin-dmp-workflow-actions-dataset-size-error`
       * :ref:`destination-linkedin-dmp-workflow-actions-invalid-account-id`
       * :ref:`destination-linkedin-dmp-workflow-actions-invalid-fields`
       * :ref:`destination-linkedin-dmp-workflow-actions-linkedin-is-processing-data`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-microsoft-ads-not-authorized-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-linkedin-dmp-workflow-actions-end


.. _destination-linkedin-dmp-workflow-actions-dataset-size-error:

Dataset size error
--------------------------------------------------

.. destination-linkedin-dmp-workflow-actions-dataset-size error-start

|destination-name| requires the uploaded audience to be between 300 and 300,000 rows.

.. destination-linkedin-dmp-workflow-actions-dataset-size error-end

.. destination-linkedin-dmp-workflow-actions-dataset-size error-steps-start

To resolve this error, verify that the number of rows in the audience list is at least 300 and no more than 300,000.

#. Open the **Activations** page, and then open the segment used with this workflow.
#. Adjust segment attributes, monitor the segment insights panel to see how many customers are in the segment, and click **Refresh** to update the count as you make changes. 
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-linkedin-dmp-workflow-actions-dataset-size error-steps-end

.. _destination-linkedin-dmp-workflow-actions-invalid-account-id:

Invalid account ID
--------------------------------------------------

.. destination-linkedin-dmp-workflow-actions-invalid-account-id-start

|destination-name| requires a valid Linkedin account ID to be associated with an advertiser. When an advertiser is not associated with a LinkedIn account ID--such as when an advertiser LinkedIn ID has been deleted--Amperity will be unable to manage audiences within LinkedIn and a workflow action is shown.

.. destination-linkedin-dmp-workflow-actions-invalid-account-id-end

.. destination-linkedin-dmp-workflow-actions-invalid-account-id-steps-start

To resolve this error, verify that the advertiser LinkedIn account ID exists in LinkedIn, and then update Amperity for the correct LinkedIn ID if necessary

#. Open the LinkedIn DMP management console and verify your LinkedIn account ID
#. Open the **Destinations** page, and then open the destination for LinkedIn DMP associated with this workflow.
#. Update the destination for the correct LinkedIn account ID.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-linkedin-dmp-workflow-actions-invalid-account-id-steps-end


.. _destination-linkedin-dmp-workflow-actions-invalid-fields:

Invalid fields
--------------------------------------------------

.. destination-linkedin-dmp-workflow-actions-invalid-fields-start

|destination-name| requires the name of the identifier type to be one of the following: 1) **email** 2) **firstname** and **lastname**. Including any other fields will return an error. Map the output of query results and segments before sending to |destination-name|.

.. destination-linkedin-dmp-workflow-actions-invalid-fields-end

.. destination-linkedin-dmp-workflow-actions-invalid-fields-start

To resolve this error, verify that the list you want to upload contains only allowed fields.

#. Open the **Activations** page and locate the segment used with this workflow.
#. Confirm that fields included are only 1) **email** or 2) **firstname** and **lastname**.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-linkedin-dmp-workflow-actions-invalid-fields-end

.. _destination-linkedin-dmp-workflow-actions-linkedin-is-processing-data:

LinkedIn is processing data
--------------------------------------------------

.. destination-linkedin-dmp-workflow-actions-linkedin-is-processing-data-start

|destination-name| may take up to 48 hours to process a segment. During this time, Amperity does not allow list updates on a given segment.

.. destination-linkedin-dmp-workflow-actions-linkedin-is-processing-data-end

.. destination-linkedin-dmp-workflow-actions-linkedin-is-processing-data-steps-start

To resolve this error, verify that the segment is ready. 

#. Open the **Workflows** page and locate the segment used with this workflow.
#. Confirm that the segment status is "ready."
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-linkedin-dmp-workflow-actions-linkedin-is-processing-data-steps-end


