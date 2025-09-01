.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Klaviyo
.. |destination-api| replace:: Klaviyo API
.. |plugin-name| replace:: "Klaviyo"
.. |credential-type| replace:: "klaviyo"
.. |required-credentials| replace:: "API key"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audience lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "klav"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Klaviyo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Klaviyo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Klaviyo

==================================================
Configure campaigns for Klaviyo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-klaviyo-start
   :end-before: .. term-klaviyo-end

.. campaign-klaviyo-start

Use Amperity to manage audience lists in |destination-name|. Build a query using the **email** field, with optional additional customer profile fields, and then send the results of that query to |destination-name|. The audience list will be updated to match the query.

.. campaign-klaviyo-end

.. campaign-klaviyo-api-note-start

.. note:: This destination uses the `Klaviyo REST API <https://apidocs.klaviyo.com/reference/api-overview>`__ |ext_link|.

   Amperity uses the `Update Profile <https://developers.klaviyo.com/en/reference/update_profile>`__ |ext_link| endpoint in the |destination-name| REST API to send customer profile attributes to |destination-name|.

   Review the `rate limits <https://developers.klaviyo.com/en/docs/rate_limits_and_error_handling#rate-limits>`__ |ext_link| that are applied to endpoints in the |destination-name| REST API to manage customer profiles.

   Before sending a set of customer profiles to |destination-name|, and to help set expectations, you should review the rate limits and estimate the amount of time required to complete the process of adding your set of customer profiles to |destination-name|.

.. campaign-klaviyo-api-note-end

.. campaign-klaviyo-csv-note-start

   If you don't want to wait to load customer profiles, you may instead use the `SFTP import tool <https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool>`__ |ext_link| process. This approach is efficient and quick. It uses the :doc:`built-in SFTP connector in Amperity <destination_sftp>` and is capable of importing large sets of customer profiles.

   The CSV file that is imported to |destination-name| has specific requirements on formatting and must include one or more of the following fields: "Email", "PhoneNumber", and/or "ExternalID". When these fields are present in the CSV file they must have those exact names.

.. campaign-klaviyo-csv-note-end


.. _campaign-klaviyo-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-klaviyo-get-details-table-start

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
             :start-after: .. credential-klaviyo-api-key-start
             :end-before: .. credential-klaviyo-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-klaviyo-api-key-scopes-start
             :end-before: .. credential-klaviyo-api-key-scopes-end

.. campaign-klaviyo-get-details-end


.. _campaign-klaviyo-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Klaviyo**

.. campaign-klaviyo-credentials-steps-start

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
             :start-after: .. credential-klaviyo-api-key-start
             :end-before: .. credential-klaviyo-api-key-end

.. campaign-klaviyo-credentials-steps-end


.. _campaign-klaviyo-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Klaviyo**

.. campaign-klaviyo-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
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
          :alt: Step 2.
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
          :alt: Step 3.
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
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-klaviyo-list-name-start
             :end-before: .. setting-klaviyo-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-klaviyo-list-name-note-start
             :end-before: .. setting-klaviyo-list-name-note-end

       **Update contacts**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-cordial-list-name-start
             :end-before: .. setting-cordial-list-name-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Campaign file settings**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

.. campaign-klaviyo-add-steps-end


.. _campaign-klaviyo-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. campaign-klaviyo-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-klaviyo-maximum-lists.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`campaign-klaviyo-workflow-actions-invalid-credentials`
       * :ref:`campaign-klaviyo-workflow-actions-maximum-lists`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-klaviyo-maximum-lists-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. campaign-klaviyo-workflow-actions-end


.. _campaign-klaviyo-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _campaign-klaviyo-workflow-actions-maximum-lists:

Maximum number of lists exceeded
--------------------------------------------------

.. campaign-klaviyo-workflow-actions-maximum-lists-start

|destination-name| supports up to 1000 lists and/or segments in your account at any given time.

.. campaign-klaviyo-workflow-actions-maximum-lists-end

.. campaign-klaviyo-workflow-actions-maximum-lists-steps-start

To resolve this error, verify the number of lists and/or segments associated with your |destination-name| account.

#. Log into |destination-name| and verify the number of lists and/or segments that are associated with your |destination-name| account.
#. Remove unused lists and/or segments.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-klaviyo-workflow-actions-maximum-lists-steps-start


.. _campaign-klaviyo-customer-profile-parameters:

Customer profile parameters
==================================================

.. campaign-klaviyo-customer-profile-parameters-start

The following table describes the parameters that may be sent to |destination-name|. Use the **properties** field to define a series of custom properties as key-value pairs to represent offline events.

Amperity uses the `Update Profile <https://developers.klaviyo.com/en/reference/update_profile>`__ |ext_link| endpoint in the Klaviyo API to send customer profile attributes to |destination-name|.

The list of customer profile parameters supported by |destination-name| are described in the following table. Parameters are listed alphabetically, but may be returned in any order.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field name
     - Description

   * - **address1**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-address-start
          :end-before: .. term-address-end


   * - **address2**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-address2-start
          :end-before: .. term-address2-end


   * - **city**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-city-start
          :end-before: .. term-city-end


   * - **country**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-country-start
          :end-before: .. term-country-end


   * - **email**
     - **Required**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-email-start
          :end-before: .. term-email-end

       .. important:: An email address is used by |destination-name| to generate a unique customer identifier for each customer profile that exists within |destination-name|.

          This email address is most often found in the **email** field in the **Merged Customers** table, but may be located elsewhere depending on how your brand has configured your customer 360 database and depending on the downstream use cases your brand wants to enable within |destination-name|.


   * - **external_id**
     - **Optional**

       A unique identifier that associates |destination-name| profiles with customer profiles that exist within an external system.

       For example, a unique ID for a point-of-sale system or the Amperity ID.


   * - **first_name**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-given-name-start
          :end-before: .. term-given-name-end


   * - **image**
     - **Optional**

       A URL that points to the location of a profile image for this customer profile.


   * - **ip**
     - **Optional**

       An IP address that is associated with this customer profile.


   * - **last_event_date**
     - **Optional**

       A timestamp for an event that is associated with this customer profile.

       For example, the date and time of the most recent transaction from your brand's website or store.


   * - **last_name**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-surname-start
          :end-before: .. term-surname-end


   * - **latitude**
     - **Optional**

       A latitude coordinate that may be used to define `location-based segments <https://help.klaviyo.com/hc/en-us/articles/115005065887#create-a-location-based-segment1>`__ |ext_link| in |destination-name|.

       .. note:: This value should have a precision of four decimal places.


   * - **longitude**
     - **Optional**

       A longitude coordinate that may be used to define `location-based segments <https://help.klaviyo.com/hc/en-us/articles/115005065887#create-a-location-based-segment1>`__ |ext_link| in |destination-name|.

       .. note:: This value should have a precision of four decimal places.


   * - **organization**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-company-start
          :end-before: .. term-company-end


   * - **phone_number**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-phone-start
          :end-before: .. term-phone-end

       .. note:: A phone number must be in |ext_e164_format|, which represents a phone number as a number up to fifteen digits in length (without spaces) that starts with a + symbol. For example: +12061234567.


   * - **properties**
     - **Optional**

       A series of custom properties represented as key-value pairs for additional data that your brand wants to associate with this customer profile.

       For example, a store ID or the name (or SKU) of the most recent product purchase associated with this customer profile.


   * - **region**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end


   * - **timezone**
     - **Optional**

       The name of a timezome. |destination-name| recommends using the name of a timezone in the `IANA Time Zone Database <https://www.iana.org/time-zones>`__ |ext_link|.


   * - **title**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-title-start
          :end-before: .. term-title-end


   * - **zip**
     - **Optional**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-postal-start
          :end-before: .. term-postal-end

.. campaign-klaviyo-customer-profile-parameters-end