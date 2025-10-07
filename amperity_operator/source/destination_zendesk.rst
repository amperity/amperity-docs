.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Zendesk
.. |destination-api| replace:: Zendesk Users API
.. |plugin-name| replace:: "Zendesk"
.. |credential-type| replace:: "zendesk"
.. |required-credentials| replace:: "email address" and "API token"
.. |audience-primary-key| replace:: "email"
.. |credential-details| replace:: the Zendesk User API token and the email address of the administrator who created the token
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "zen"


.. meta::
    :description lang=en:
        Configure Amperity to send customer profiles to Zendesk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profiles to Zendesk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Zendesk

==================================================
Configure destinations for Zendesk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-zendesk-start
   :end-before: .. term-zendesk-end

.. destination-zendesk-start

Amperity may be configured to create or update user records in |destination-name| by using the |destination-api| to `create or update users <https://developer.zendesk.com/api-reference/ticketing/users/users/#create-or-update-many-users>`__ |ext_link|. Use this connector to deliver a better customer support experience by pre-populating |destination-name| user records with customer records from Amperity, including:

* Order history
* Loyalty status
* Satisfaction survey results
* Shopping preferences
* and more

Use this data to show customer support representatives information related to product recommendations, next best actions, and likelihood of churn.

.. destination-zendesk-end

.. destination-zendesk-note-start

.. note:: Creating or updating records are `rate limited <https://developer.zendesk.com/rest_api/docs/support/introduction#endpoint-specific-rate-limits>`__ |ext_link| to a maximum of 100 users per second.

.. destination-zendesk-note-end


.. _destination-zendesk-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-zendesk-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-zendesk-api-token-start
             :end-before: .. credential-zendesk-api-token-end

       **Email address**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-zendesk-email-address-start
             :end-before: .. credential-zendesk-email-address-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Subdomain**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-zendesk-subdomain-start
             :end-before: .. setting-zendesk-subdomain-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required fields for Zendesk**

       Be sure to send all fields from Amperity that is required by |destination-name|.

       .. important:: Fields must exist in |destination-name| and should follow a "user_fields.[field_name]" naming pattern, where "field_name" is the name of the field that is sent to |destination-name| from Amperity.

       The **name**, **email** or **external_id** fields must be included.

       Values for states should be 2 uppercase letters only.

       Phone numbers should start with "+1" and contain only digits.

       Floating point numbers must be in **DECIMAL(10,2)** format.

       From within |destination-name| verify that audience data has been loaded and is usable by all of the use cases you want to use within |destination-name| to build better customer experiences.



.. destination-zendesk-get-details-end


.. _destination-zendesk-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Zendesk**

.. destination-zendesk-credentials-steps-start

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

       **API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-zendesk-api-token-start
             :end-before: .. credential-zendesk-api-token-end

       **Email address**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-zendesk-email-address-start
             :end-before: .. credential-zendesk-email-address-end

.. destination-zendesk-credentials-steps-end


.. _destination-zendesk-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Zendesk**

.. destination-zendesk-add-steps-start

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

       **Subdomain**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-zendesk-subdomain-start
             :end-before: .. setting-zendesk-subdomain-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-zendesk-add-steps-end


.. _destination-zendesk-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-zendesk-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-zendesk-403.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-zendesk-workflow-actions-authorization-error`
       * :ref:`destination-zendesk-workflow-actions-invalid-credentials`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-zendesk-403-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-zendesk-workflow-actions-end


.. _destination-zendesk-workflow-actions-authorization-error:

Authorization error
--------------------------------------------------

.. destination-zendesk-workflow-actions-authorization-error-start

A 403 response means that Amperity is not able to access the Zendesk Users API. When a 403 response is received from Zendesk, a workflow action named "Authorization Error" is generated.

Amperity uses two configuration settings -- |credential-details| -- to build a credentials string that is added to the request authorization header. The format for the credentials string is:

::

   {email_address}/token:{api_token}

A 403 response from Zendesk indicates that the credentials string does not have the correct information. This could be for a number of reasons, including:

* The wrong values for email address or API token are configured in Amperity.
* The API token was deleted in Zendesk.
* The email address for the user who generated the API token is no longer a valid email address within Zendesk or is not associated with a user who has permission to access the Zendesk Users API.

.. destination-zendesk-workflow-actions-authorization-error-end

.. destination-zendesk-workflow-actions-authorization-error-steps-start

To resolve this error, you must provide a combination of email address and Zendesk API token that allows Amperity access to Zendesk.

#. Open the Amperity **Credentials** page in a new tab.
#. Verify that the individual who authorized access to Zendesk has the correct permissions to allow Amperity to access Zendesk.
#. Update the values that build the credentials string as necessary.

   .. tip:: You may need to generate a new API token in Zendesk, and then reconfigure Amperity with the updated API token string *and* the email address for the user that generated the newly generated API token.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-zendesk-workflow-actions-authorization-error-steps-start


.. _destination-zendesk-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end
