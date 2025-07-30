.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Braze
.. |plugin-name| replace:: Braze
.. |credential-type| replace:: **braze**
.. |what-send| replace:: custom attributes
.. |filter-the-list| replace:: "br"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by |destination-name| were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_braze|
.. |channel-link| replace:: |campaign_braze|


==================================================
Configure campaigns for Braze
==================================================

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_braze.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-braze-start
   :end-before: .. term-braze-end

.. destination-braze-context-start

Amperity can send :ref:`customer profile and custom attributes <destination-braze-about-custom-attributes>` to |destination-name|, attaching the data that is sent from Amperity to customer profiles that already exist in |destination-name|.

.. destination-braze-context-end

.. destination-braze-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`About custom attributes <destination-braze-about-custom-attributes>`
#. :ref:`Get details <destination-braze-get-details>`
#. :ref:`Add destination <destination-braze-add-destination>`
#. :ref:`Add data template <destination-braze-add-data-template>`

.. destination-braze-steps-to-send-end


.. _destination-braze-about-custom-attributes:

About custom attributes
==================================================

.. include:: ../../amperity_user/source/destination_braze.rst
   :start-after: .. destination-braze-ampiq-and-amp360-shared-intro-start
   :end-before: .. destination-braze-ampiq-and-amp360-shared-intro-end


.. _destination-braze-profile-attributes:

Customer profiles
--------------------------------------------------

.. include:: ../../amperity_user/source/destination_braze.rst
   :start-after: .. destination-braze-ampiq-and-amp360-shared-intro-start
   :end-before: .. destination-braze-ampiq-and-amp360-shared-intro-end

.. include:: ../../amperity_user/source/destination_braze.rst
   :start-after: .. destination-braze-profile-attributes-admonition-consent-status-start
   :end-before: .. destination-braze-profile-attributes-admonition-consent-status-end

.. include:: ../../amperity_user/source/destination_braze.rst
   :start-after: .. destination-braze-profile-attributes-table-start
   :end-before: .. destination-braze-profile-attributes-table-end

.. include:: ../../amperity_user/source/destination_braze.rst
   :start-after: .. destination-braze-profile-attributes-note-start
   :end-before: .. destination-braze-profile-attributes-note-end


.. _destination-braze-custom-attributes:

Custom attributes
--------------------------------------------------

.. include:: ../../amperity_user/source/destination_braze.rst
   :start-after: .. destination-braze-custom-attributes-start
   :end-before: .. destination-braze-custom-attributes-end


.. _destination-braze-data-points:

About data points
--------------------------------------------------

.. include:: ../../amperity_user/source/destination_braze.rst
   :start-after: .. destination-braze-data-points-start
   :end-before: .. destination-braze-data-points-end

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-start

.. important:: `Connected Content <https://docs.amperity.com/operator/api_profile.html#braze-connected-content>`__ does not write data to user profiles, which means you can use Connected Content to dynamically populate values into messages without consuming data points.

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-end


.. _destination-braze-attribute-updates:

Audience profile updates
--------------------------------------------------

.. destination-braze-attribute-updates-overview-start

Profile attributes, such as **email**, **birthdate**, **address**, and **phone**, contain stable values. Most customers remain at the same address and have the same phone number for years. An individual customer's birthdate never changes. When customer profile attributes do change your brand will always want to update any downstream audience profiles.

Behavioral attributes, both historical and predicted, are more likely to contain values that change frequently. Behavioral attributes should be carefully evaluated before including them within audience profiles. This will help ensure that updates related to behavioral attributes are adding value to your brand's downstream business use case(s).

.. destination-braze-attribute-updates-overview-end

.. destination-braze-attribute-updates-admonition-start

.. admonition:: What types of attributes have values that change frequently?

   The following types of attributes contain values that change frequently:

   .. list-table::
      :widths: 35 65
      :header-rows: 0

      * - **Relative date values**
        - Attributes with relative date values typically contain a rolling value that is updated daily.

          For example, the **Transaction Attributes Extended** table contains an attribute named **Days Since Latest Order**. This is a useful attribute that counts the number of days that have elapsed since an individual customer last placed an order with your brand. Today that value might be "10" and tomorrow, if that customer has not purchased, will be "11".

          Using **Days Since Latest Order** as an attribute within customer profiles ensures that every customer profile associated with a customer who did not purchase during the previous X days will get an updated profile.

          For relative date values, consider building a custom attribute that converts the ranges into a list of values. For example, you can assign a single value to represent a range of values. Less than 30 days is "green", less than 90 days is "yellow", and less than 365 days is "red". Include the custom attribute to capture the range of days as an indicator instead of the specific relative value.

      * - **High-precision values**
        - High-precision values are found in attributes that contain floating points, decimals, and percentages.

          These types of values---1.09413481, 345.47 or .34---often change slightly, but in a way that offers little value to the downstream business use case.

          For example, predictive attributes are refreshed daily. Predicted CLV during the next 365 days might be $345.37 on one day and $348.75 a few days later.

          Instead of using predicted CLV in an audience profile, consider using predicted lifecycle status (active, at risk, etc.) or predicted value tier (gold, bronze, etc.), both of which are less likely to change because they represent a range of predicted behaviors instead of a specific predicted value.

      * - **Calculated attribute values**
        - Many attributes are calculated by Amperity, including all time period rollups.

          For example, the **Transaction Attributes Extended** table contains an attribute named **L6M Order Revenue**. This attribute returns the order revenue for each customer over a rolling 6-month timeframe. This attribute is refreshed on a daily basis and the value is updated each time a customer makes a purchase.

          Instead of using the time period rollup attributes directly you can build a custom attribute to define thresholds or to return a yes or no. For example, instead of using the specific revenue amount for **L6M Order Revenue** you could build a custom attribute that returns true when the value for **L6M Order Revenue** is greater than $500.

.. destination-braze-attribute-updates-admonition-end


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
          :align: left
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
            ,tae.L30D_purchase_channels
            ,tae.L30D_order_revenue
            ,tae.L30D_order_frequency
            ,tae.L3M_purchase_channels
            ,tae.L3M_order_revenue
            ,tae.L3M_order_frequency
            ,tae.L12M_rfm_score
            ,tae.L12M_recency
            ,tae.L12M_frequency
            ,tae.L12M_monetary
            ,tae.lifetime_order_revenue
            ,tae.one_and_done
            ,tae.multi_purchase_channel
            ,tae.first_to_second_order_days
            ,tae.days_since_latest_order
            ,tae.latest_order_datetime
            ,tae.early_repeat_purchaser
          FROM Merged_Customers mc
          LEFT JOIN Transaction_Attributes_Extended tae
          ON mc.amperity_id = tae.amperity_id
          LEFT JOIN Customer_Attributes ca
          ON mc.amperity_id = ca.amperity_id


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Validate the table, and then click **Next**.

       Name the table "Braze Customer Attributes", and then save the table. Verify that the table is accessible to the **Segment Editor** and to the **Edit Attributes** editor within campaigns.

.. destination-braze-table-end


.. _destination-braze-get-details:

Get details
==================================================

.. destination-braze-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Configuration details for |destination-name|.

       * The API key for your instance of |destination-name|.

         Open the `Developer Console <https://www.braze.com/docs/api/basics#creating-and-managing-rest-api-keys>`__ |ext_link|. Under **REST API Key**, click **+ Create New API Key**, and then set the following permissions under **User Data**: "users.track", "users.export.segment", and "segments.list".

         Save the API key.

         .. note:: If you view the REST API key after you have saved it you should see a configuration similar to:

            .. image:: ../../images/destination-braze-rest-api-endpoints.png
               :width: 500 px
               :alt: The endpoints that are required for an Amperity-to-Braze workflow.
               :align: left
               :class: no-scaled-link

         The API key that you will use to configure Amperity credentials is available from the **Identifier** column on the **Rest API Key** page and is similar to: "a1bc2345-678d-9012-e3fg-hi34jk5l6789".

         .. image:: ../../images/destination-braze-rest-api-identifier.png
            :width: 500 px
            :alt: Add the identifier that is required by this workflow.
            :align: left
            :class: no-scaled-link

       * The `REST API endpoint <https://www.braze.com/docs/api/basics#endpoints>`__ |ext_link| from which your instance of |destination-name| is available.

         For example, if your URL for |destination-name| is ``https://dashboard-03.braze.com``, the REST API endpoint is ``https://rest.iad-03.braze.com``, and the instance is "US-03".

       * A list of `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link| and/or `custom attributes <https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/>`__ |ext_link| that may be sent to |destination-name| from Amperity.

.. destination-braze-get-details-end


.. _destination-braze-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-braze-add-destination-start

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

       .. image:: ../../images/mockup-destinations-tab-add-01-select-braze.png
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

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-braze.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-01-select-braze.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       Add the API key for your instance of |destination-name|.

       .. image:: ../../images/mockup-destinations-tab-credentials-02-select-braze.png
          :width: 500 px
          :alt: Set the following credentials for Braze.
          :align: left
          :class: no-scaled-link

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

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-braze.png
          :width: 500 px
          :alt: Settings for Braze.
          :align: left
          :class: no-scaled-link

       Select the `Braze instance <https://www.braze.com/docs/user_guide/administrative/access_braze/braze_instances>`__ |ext_link|.

       Select the user identifier. The `external_id <https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import/#importing-with-external-id>`__ |ext_link| is a unique identifier for your customers, such as the Amperity ID. The `braze_id <https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_import/#importing-with-braze-id>`__ |ext_link| is a unique identifier for existing |destination-name| customers.

       To update audience profiles only when one (or more) values change, enable the **Only send updated audience profiles** option.

       .. note:: Use the **Only send updated audience profiles** option to configure Amperity to :ref:`update audience profiles <destination-braze-attribute-updates>` only when one (or more) values within a profile have changed. An update to an individual value in an audience profile requires updating the entire audience profile.

          For use cases that require sending attributes that have values that are expected to change frequently, consider using additional queries to orchestrate specific sets of attributes at defined intervals so that your brand can maintain these values independently of your customer profiles.

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


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-braze-add-destination-end


.. _destination-braze-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-braze-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details-braze.png
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

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-braze.png
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

.. destination-braze-add-data-template-steps-end


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
          :align: left
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
          :align: left
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
