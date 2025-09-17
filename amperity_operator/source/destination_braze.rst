.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Braze
.. |plugin-name| replace:: "Braze"
.. |credential-type| replace:: "braze"
.. |required-credentials| replace:: "API key"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "braz"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Braze.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Braze.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Braze

==================================================
Configure destinations for Braze
==================================================

.. destination-braze-intro-start

|destination-name| is a marketing automation platform that uses customer profile attributes and segments to build custom experiences, and then map those experiences to campaigns. Use the Braze API to send customer profile attributes from Amperity to |destination-name|.

.. destination-braze-intro-end

.. destination-braze-context-start

Amperity can send :ref:`customer profile and custom attributes <destination-braze-about-custom-attributes>` to |destination-name|, attaching the data that is sent from Amperity to customer profiles that already exist in |destination-name|.

.. destination-braze-context-end


.. _destination-braze-about-custom-attributes:

About custom attributes
==================================================

.. destination-braze-ampiq-and-amp360-shared-intro-start

Attributes in |destination-name| describe your customers.

* :ref:`Profile attributes <destination-braze-profile-attributes>` describe who your customers are. For example: names, birthdates, email addresses, and phone numbers.
* :ref:`Custom attributes <destination-braze-custom-attributes>` describe how your customers have interacted with your brand. For example: purchase histories, loyalty status, and value tiers.

.. destination-braze-ampiq-and-amp360-shared-intro-end

.. include:: ../../shared/braze.rst
   :start-after: .. braze-attributes-about-start
   :end-before: .. braze-attributes-about-end


.. _destination-braze-profile-attributes:

Customer profiles
--------------------------------------------------

.. include:: ../../shared/braze.rst
   :start-after: .. braze-customer-profiles-about-start
   :end-before: .. braze-customer-profiles-about-end

.. include:: ../../shared/braze.rst
   :start-after: .. braze-customer-profiles-admonition-start
   :end-before: .. braze-customer-profiles-admonition-end

.. include:: ../../amperity_operator/source/campaign_braze.rst
   :start-after: .. campaign-braze-profile-attributes-start
   :end-before: .. campaign-braze-profile-attributes-end

.. include:: ../../shared/braze.rst
   :start-after: .. braze-customer-profiles-common-attributes-start
   :end-before: .. braze-customer-profiles-common-attributes-end

.. include:: ../../shared/braze.rst
   :start-after: .. braze-customer-profiles-common-attributes-note-start
   :end-before: .. braze-customer-profiles-common-attributes-note-end


.. _destination-braze-custom-attributes:

Custom attributes
--------------------------------------------------

.. include:: ../../shared/braze.rst
   :start-after: .. braze-custom-attributes-start
   :end-before: .. braze-custom-attributes-end


.. _destination-braze-data-points:

About data points
--------------------------------------------------

.. include:: ../../shared/braze.rst
   :start-after: .. braze-data-points-start
   :end-before: .. braze-data-points-end

.. include:: ../../amperity_operator/source/campaign_braze.rst
   :start-after: .. profile-api-usecase-braze-connected-content-does-not-use-data-points-start
   :end-before: .. profile-api-usecase-braze-connected-content-does-not-use-data-points-end


.. _destination-braze-attribute-updates:

Audience profile updates
--------------------------------------------------

.. include:: ../../shared/braze.rst
   :start-after: .. braze-attribute-updates-start
   :end-before: .. braze-attribute-updates-end

.. include:: ../../shared/braze.rst
   :start-after: .. braze-attribute-updates-admonition-start
   :end-before: .. braze-attribute-updates-admonition-end


.. _destination-braze-table:

Customer attributes table
--------------------------------------------------

.. destination-braze-table-start

Build a table that contains all of the attributes in |destination-name| that your brand wants to manage from Amperity. The columns in this table must be correctly mapped to requirements for `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link| and should contain the list of `custom attributes <https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/>`__ |ext_link| that will be maintained.

**To add a Braze customer attributes table**

.. destination-braze-add-destination-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - Open your customer 360 database and add a table named "Braze Customer Attributes".

       Use SQL to define the default user profile fields that are required by |destination-name|:

       .. code-block:: sql

          SELECT
            mc.amperity_id
            ,mc.amperity_id AS external_id
            ,mc.given_name AS first_name
            ,mc.surname AS last_name
            ,mc.email
            ,mc.phone
            ,mc.city AS home_city
            ,mc.country
            ,mc.birthdate AS dob
            ,mc.gender
          FROM Merged_Customers mc

       You may include custom attributes that map to other fields in your customer 360. For example, to use transaction attributes as custom attributes in |destination-name| you can extend the table to include fields from the **Transaction Attributes Extended** table:

       .. code-block:: sql

          SELECT
            mc.amperity_id
            ,mc.amperity_id AS external_id
            ,mc.given_name AS first_name
            ,mc.surname AS last_name
            ,mc.email
            ,mc.phone
            ,mc.city AS home_city
            ,mc.country
            ,mc.birthdate AS dob
            ,mc.gender
            ,ta.L30D_purchase_channels
            ,ta.L30D_order_revenue
            ,ta.L30D_order_frequency
            ,ta.L3M_purchase_channels
            ,ta.L3M_order_revenue
            ,ta.L3M_order_frequency
            ,ta.L12M_rfm_score
            ,ta.L12M_recency
            ,ta.L12M_frequency
            ,ta.L12M_monetary
            ,ta.lifetime_order_revenue
            ,ta.one_and_done
            ,ta.multi_purchase_channel
            ,ta.first_to_second_order_days
            ,ta.days_since_latest_order
            ,ta.latest_order_datetime
            ,ta.early_repeat_purchaser
          FROM Merged_Customers mc
          LEFT JOIN Transaction_Attributes_Extended ta
          ON mc.amperity_id = ta.amperity_id
          LEFT JOIN Customer_Attributes ca
          ON mc.amperity_id = ca.amperity_id


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - Validate the table, and then click **Next**.

       Name the table "Braze Customer Attributes", and then save the table. Verify that the table is accessible to the **Segment Editor** and to the **Edit Attributes** editor within campaigns.

.. destination-braze-table-end


.. _destination-braze-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-braze-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-braze-api-key-start
          :end-before: .. credential-braze-api-key-end

       .. admonition:: Create the Braze API key

          Open the `Developer Console <https://www.braze.com/docs/api/basics#creating-and-managing-rest-api-keys>`__ |ext_link|. Under **REST API Key**, click **+ Create New API Key**, and then set the following permissions under **User Data**: "users.track", "users.export.segment", and "segments.list".

          Save the API key.

          If you view the REST API key after you have saved it you should see a configuration similar to:

          .. image:: ../../images/destination-braze-rest-api-endpoints.png
             :width: 500 px
             :alt: The endpoints that are required for an Amperity-to-Braze workflow.
             :align: left
             :class: no-scaled-link

          The API key that you use to configure Amperity credentials is available from the **Identifier** column on the **Rest API Key** page and is similar to: "a1bc2345-678d-9012-e3fg-hi34jk5l6789".

          .. image:: ../../images/destination-braze-rest-api-identifier.png
             :width: 500 px
             :alt: Add the identifier that is required by this workflow.
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Instance**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-instance-start
             :end-before: .. setting-braze-instance-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-instance-example-start
             :end-before: .. setting-braze-instance-example-end

       **User identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-user-identifier-start
             :end-before: .. setting-braze-user-identifier-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-user-identifier-about-start
             :end-before: .. setting-braze-user-identifier-about-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A list of `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link| or `custom attributes <https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/>`__ |ext_link| that may be sent to |destination-name| from Amperity.


.. destination-braze-get-details-end


.. _destination-braze-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Braze**

.. destination-braze-credentials-steps-start

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

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-braze-api-key-start
             :end-before: .. credential-braze-api-key-end

.. destination-braze-credentials-steps-end


.. _destination-braze-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Braze**

.. destination-braze-add-steps-start

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

       **Instance**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-instance-start
             :end-before: .. setting-braze-instance-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-instance-example-start
             :end-before: .. setting-braze-instance-example-end

       **User identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-user-identifier-start
             :end-before: .. setting-braze-user-identifier-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-user-identifier-about-start
             :end-before: .. setting-braze-user-identifier-about-end

       **Update existing profiles?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-update-existing-profiles-start
             :end-before: .. setting-braze-update-existing-profiles-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-braze-add-steps-end


.. _destination-braze-workflow-actions:

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

       .. image:: ../../images/workflow-actions-braze-missing-field.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-braze-workflow-actions-invalid-credentials`
       * :ref:`destination-braze-workflow-actions-missing-required-field`
       * :ref:`destination-braze-workflow-actions-status-401`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-braze-missing-field-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-braze-workflow-actions-end


.. _destination-braze-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-braze-workflow-actions-missing-required-field:

Missing required field
--------------------------------------------------

.. destination-braze-workflow-actions-missing-required-field-start

A unique identifier must be provided to |destination-name|. There are two options:

#. Recommended. The `external_id <https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import/#importing-with-external-id>`__ |ext_link|, which is a unique identifier for your customers. This may be the Amperity ID or it may be some other unique identifier.
#. The `braze_id <https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import/#importing-with-braze-id>`__ |ext_link|, which is a unique identifier for existing |destination-name| customers and may be available when |destination-name| is also a data source for your tenant.

.. destination-braze-workflow-actions-missing-required-field-end

**For campaigns**

.. destination-braze-workflow-actions-missing-required-field-campaigns-steps-start

To resolve this error, verify that "external_id" or "braze_id" are included in the list of attributes that are being sent to |destination-name|.

#. Open the **Campaigns** page, and then open the segment used with this workflow.
#. Verify that "external_id" or "braze_id" is included in the list of attributes for each treatment group that sends audiences to |destination-name|. Update the list of attributes for each treatment group if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-braze-workflow-actions-missing-required-field-campaigns-steps-start

**For orchestrations**

.. destination-braze-workflow-actions-missing-required-field-orchestrations-steps-start

To resolve this error, verify that "external_id" or "braze_id" are included in the query results.

#. Open the **Queries** page, and then open the query used with this workflow.
#. Verify that "external_id" or "braze_id" is included in the query results. Update the query if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-braze-workflow-actions-missing-required-field-orchestrations-steps-start


.. _destination-braze-workflow-actions-status-401:

Status 401 error
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-status-401-start
   :end-before: .. workflow-actions-generic-status-401-end
