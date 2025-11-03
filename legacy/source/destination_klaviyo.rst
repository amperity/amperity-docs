.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Klaviyo
.. |destination-api| replace:: Klaviyo API
.. |plugin-name| replace:: Klaviyo
.. |what-send| replace:: audience lists
.. |filter-the-list| replace:: "kla"
.. |credential-type| replace:: **klaviyo**
.. |credential-details| replace:: the Klaviyo API key. Be sure to add the full Klaviyo API key
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: audience list settings were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_klaviyo|
.. |channel-link| replace:: |campaign_klaviyo|


==================================================
Configure campaigns for Klaviyo
==================================================

.. vale off

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_klaviyo.html>`__ |ext_link|.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-klaviyo-start
   :end-before: .. term-klaviyo-end

.. destination-klaviyo-start

Use Amperity to manage audience lists in Klaviyo. Build a query using the **email** field, with optional additional customer profile fields, and then send the results of that query to Klaviyo. The audience list is updated to match the query.

.. destination-klaviyo-end

.. destination-klaviyo-api-note-start

.. note:: This destination uses the `Klaviyo REST API <https://apidocs.klaviyo.com/reference/api-overview>`__ |ext_link|.

   Amperity uses the `Update Profile <https://developers.klaviyo.com/en/reference/update_profile>`__ |ext_link| endpoint in the Klaviyo API to send customer profile attributes to |destination-name|.

   Review the `rate limits <https://developers.klaviyo.com/en/docs/rate_limits_and_error_handling#rate-limits>`__ |ext_link| that are applied to endpoints in the |destination-name| REST API to manage customer profiles.

   Before sending a set of customer profiles to |destination-name|, and to help set expectations, you should review the rate limits and estimate the amount of time required to complete the process of adding your set of customer profiles to |destination-name|.

.. destination-klaviyo-api-note-end

.. destination-klaviyo-csv-note-start

   If you do not want to wait to load customer profiles, you may instead use the `SFTP import tool <https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool>`__ |ext_link| process. This approach is efficient and quick. It uses the :doc:`built-in SFTP connector in Amperity <destination_sftp>` and is capable of importing large sets of customer profiles.

   The CSV file that is imported to |destination-name| has specific requirements on formatting and must include one or more of the following fields: "Email", "PhoneNumber", or "ExternalID". When these fields are present in the CSV file they must have those exact names.

.. destination-klaviyo-csv-note-end

.. destination-klaviyo-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-klaviyo-get-details>`
#. :ref:`Add destination <destination-klaviyo-add-destination>`
#. :ref:`Add data template <destination-klaviyo-add-data-template>`

.. destination-klaviyo-steps-to-send-end


.. _destination-klaviyo-get-details:

Get details
==================================================

.. destination-klaviyo-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: center
          :class: no-scaled-link
     - A private API key.

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-klaviyo-api-key-scopes-start
          :end-before: .. credential-klaviyo-api-key-scopes-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: center
          :class: no-scaled-link
     - The list name to which the Klaviyo connector writes. This can be the name of an existing list or a new list.

       .. note:: |destination-name| supports up to 1000 lists or segments in your account at any given time.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: center
          :class: no-scaled-link
     - A query that outputs the fields that must be mapped to the Klaviyo audience.

.. destination-klaviyo-get-details-end

.. destination-klaviyo-get-details-account-info-start

.. admonition:: How to find Klaviyo account, private API key, and audience information?

   You can find all of this information after you log into Klaviyo.

   #. A private API key is associated with your account username. Click your username, then **Account**, then **Settings**, and then **API Keys**. Create a new private API Key for use with Amperity, and then copy it.
   #. There can be many lists in Klaviyo. For each list to which you want to send query results, click **Lists & Segments**. Copy the name of the list into which you want to load query data or provide a new name to create a new list.

.. destination-klaviyo-get-details-account-info-end


.. _destination-klaviyo-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-klaviyo-add-destination-steps-start

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

       Enter |credential-details|.

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
          :alt: Settings for Klaviyo.
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

.. destination-klaviyo-add-destination-steps-end


.. _destination-klaviyo-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-klaviyo-add-data-template-steps-start

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
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Configure how Amperity sends data to |destination-name|.

       **For campaigns**

       Under **Template Settings**, configure the following settings:

       **List Name** This is the name of the audience list in |destination-name|. If the audience list does not exist, this is the name of the audience list that will be created by Amperity.

       .. note:: By default, Amperity manages audience lists using only **email**.

       **For orchestrations**

       When you configure Amperity to send query results to |destination-name| you have two choices:

       #. Configure the data template to allow only email addresses
       #. Configure the data template to allow email addresses *and* customer profiles

       Under **Template Settings**, configure the following settings:

       **List Name** This is the name of the audience list in |destination-name|. If the audience list does not exist, this is the name of the audience list that will be created by Amperity.

       **Use full profile to update list** This option allows queries to send additional customer profile fields as part of the audience list, after which they is visible in |destination-name| from the **Customer Properties** section within individual profiles for members of that audience list.

       .. note:: By default, Amperity manages audience lists using only **email**.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
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

.. destination-klaviyo-add-data-template-steps-end


.. _destination-klaviyo-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-klaviyo-workflow-actions-start

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

       * :ref:`destination-klaviyo-workflow-actions-invalid-credentials`
       * :ref:`destination-klaviyo-workflow-actions-maximum-lists`


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

.. destination-klaviyo-workflow-actions-end


.. _destination-klaviyo-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-klaviyo-workflow-actions-maximum-lists:

Maximum number of lists exceeded
--------------------------------------------------

.. destination-klaviyo-workflow-actions-maximum-lists-start

|destination-name| supports up to 1000 lists or segments in your account at any given time.

.. destination-klaviyo-workflow-actions-maximum-lists-end

.. destination-klaviyo-workflow-actions-maximum-lists-steps-start

To resolve this error, verify the number of lists or segments associated with your |destination-name| account.

#. Log into |destination-name| and verify the number of lists or segments that are associated with your |destination-name| account.
#. Remove unused lists or segments.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-klaviyo-workflow-actions-maximum-lists-steps-start


.. _destination-klaviyo-customer-profile-parameters:

Customer profile parameters
==================================================

.. destination-klaviyo-customer-profile-parameters-start

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

.. destination-klaviyo-customer-profile-parameters-end
