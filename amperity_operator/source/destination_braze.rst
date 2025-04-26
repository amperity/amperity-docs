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
        Send audiences to Braze

==================================================
Send audiences to Braze
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_braze.html>`__ |ext_link|.

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

When `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link| and `custom attributes <https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/>`__ |ext_link| are available in |destination-name| they can be used to build out audience `segments <https://www.braze.com/docs/user_guide/engagement_tools/segments/creating_a_segment/>`__ |ext_link| and to apply `personalization <https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid>`__ |ext_link| to your campaigns.

.. destination-braze-ampiq-and-amp360-shared-intro-end

.. TODO: Uncomment these inclusions and remove the previous section/s:

.. 
.. .. include:: ../../amperity_amp360/source/destination_braze.rst
..    :start-after: .. destination-braze-ampiq-and-amp360-shared-intro-start
..    :end-before: .. destination-braze-ampiq-and-amp360-shared-intro-end
.. 


.. _destination-braze-profile-attributes:

Customer profiles
--------------------------------------------------

.. destination-braze-profile-attributes-start

Customer profiles in |destination-name| are represented by a set of `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link|. To update these fields in |destination-name| you must follow a strict naming convention when sending data from Amperity. These fields are also case sensitive (and are in lowercase).

.. destination-braze-profile-attributes-end

.. destination-braze-profile-attributes-admonition-consent-status-start

.. admonition:: What about email and phone subscription status?

   |destination-name| uses two fields to track email and phone subscription status: **email_subscribe** and **push_subscribe**. The values for these fields are not modified by Amperity *even when the fields are sent from Amperity with the correct values*. Braze is your source of truth for customer consent and for tracking email and phone subscription status.

.. destination-braze-profile-attributes-admonition-consent-status-end

.. destination-braze-profile-attributes-start

An orchestration can send customer profile updates to |destination-name| as the results of a query. For example:

.. code-block:: sql

   SELECT
     amperity_id AS external_id
     ,given_name AS first_name
     ,surname AS last_name
     ,email
     ,phone
     ,city AS home_city
     ,country
     ,birthdate AS dob
     ,gender
   FROM Customer_360

.. destination-braze-profile-attributes-end

.. destination-braze-profile-attributes-table-start

The following table describes the default `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link| that are most commonly updated from Amperity:

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Braze default field
     - Amperity field name
     - Description
   * - **external_id**
     - varies
     - Required. The **external_id** is a unique identifer for user profiles in |destination-name|. The **external_id** is a unique identifier that exists in another system, such as the Amperity ID, a loyalty ID, or some other unique customer identifier.

   * - **first_name**
     - **given_name**
     - Optional.

   * - **last_name**
     - **surname**
     - Optional.

   * - **email**
     - **email**
     - Optional.

   * - **phone**
     - **phone**
     - Optional.

   * - **home_city**
     - **city**
     - Optional.

   * - **country**
     - **country**
     - Optional. Must be in |ext_iso_31661alpha2| format.

   * - **dob**
     - **birthdate**
     - Optional. Must be in "YYYY-MM-DD" format.

   * - **gender**
     - **gender**
     - Optional. Accepted values: "M", "F", "O" (other), "N" (not applicable), "P" (prefer not to say), or NULL.

.. destination-braze-profile-attributes-table-end

.. destination-braze-profile-attributes-note-start

.. note:: Default user profile fields also exist for **alias_name**, **alias_label**, **current_location**, **date_of_first_session**, **date_of_last_session**, **email_open_tracking_disabled**, **email_click_tracking_disabled**, **facebook**, **language**, **marked_email_as_spam_at**, **push_tokens**, **subscription_groups**, **time_zone**, and **twitter**.

   These fields are not commonly sent to |destination-name| from Amperity, but if your brand chooses to update these user profile fields from Amperity, be sure to use the exact name of the default field name, send the correct value (or values), and to use lowercase.

.. destination-braze-profile-attributes-note-end

.. TODO: Uncomment these inclusions and remove the previous section/s:

.. 
.. .. include:: ../../amperity_amp360/source/destination_braze.rst
..    :start-after: .. destination-braze-ampiq-and-amp360-shared-intro-start
..    :end-before: .. destination-braze-ampiq-and-amp360-shared-intro-end
.. 
.. .. include:: ../../amperity_amp360/source/destination_braze.rst
..    :start-after: .. destination-braze-profile-attributes-admonition-consent-status-start
..    :end-before: .. destination-braze-profile-attributes-admonition-consent-status-end
.. 
.. .. include:: ../../amperity_amp360/source/destination_braze.rst
..    :start-after: .. destination-braze-profile-attributes-table-start
..    :end-before: .. destination-braze-profile-attributes-table-end
.. 
.. .. include:: ../../amperity_amp360/source/destination_braze.rst
..    :start-after: .. destination-braze-profile-attributes-note-start
..    :end-before: .. destination-braze-profile-attributes-note-end
.. 

.. _destination-braze-custom-attributes:

Custom attributes
--------------------------------------------------

.. destination-braze-custom-attributes-start

Custom attributes in |destination-name| are represented by a set of custom-named fields. The names of these fields are determined by your brand. They may already exist in |destination-name|, in which case you will want to shape the output that is sent from Amperity to align to the names you already have.

The names of custom attributes that can be managed by Amperity are defined by your brand. The names are strings, may contain hyphens, spaces, or underscores, may include numbers, and may contain a mix of lowercase and uppercase letters. For example, custom attribute can have names that:

* Already exist within your organization.
* Are exactly the same as Amperity standard output, such as "One and Done" or "L12M Monetary" (the "monetary" component of an RFM score), or "Early Repeat Purchaser".
* Align to marketing goals and/or terminology that exists within your brand's segmentation strategy.

Verify the names of custom attributes that will be sent to |destination-name| from Amperity. Amperity will add a custom attribute whenever there isn't a matching name.

.. tip:: Avoid sending custom attributes as duplicates of default user profile fields. For example, birthdates should be sent to |destination-name| as a user profile field named "dob". If they are sent as "birthday", "Birthdate", or any other string, a custom attribute will be created and the values in the "dob" field will not be updated.

.. important:: Your brand's list of custom attributes *should* be a list that is mostly static, remains stable over time, and is focused on your most valuable customers.

   Only update custom attributes for customers to which your brand is currently engaged. Define an audience in Amperity that is some combination of "high value" (historical or predicted), "active" (has purchased recently), and are "contactable" (with an opt-in status of true for phone numbers and/or email addresses).

   This will help ensure that you are only updating custom attributes for your most valuable customers. Custom attributes will be updated only for those customers have a matching "external_id" or "braze_id" within |destination-name|.

.. destination-braze-custom-attributes-end

.. TODO: Uncomment these inclusions and remove the previous section/s:

.. 
.. .. include:: ../../amperity_amp360/source/destination_braze.rst
..    :start-after: .. destination-braze-custom-attributes-start
..    :end-before: .. destination-braze-custom-attributes-end
.. 

.. _destination-braze-data-points:

About data points
--------------------------------------------------

.. destination-braze-data-points-start

|destination-name| uses `data points <https://www.braze.com/docs/user_guide/data_and_analytics/data_points/>`__ |ext_link| to determine when to update segment membership, to identify which types of messages should be sent, and how to apply message personalization.

You can send custom attributes to |destination-name| from Amperity by attaching attributes from your customer profiles in Amperity, such as first and last names, email addresses, phone numbers, physical locations, SMS and email consent status, purchase histories, and so on.

Amperity tracks changes as they are sent to Braze and only sends list membership and attribute that have changed since the previous update.

.. note:: Data points are part of the billing and pricing structure in your |destination-name| contract. Some data points are non-billable; many data points are billable.

   Review the `lists of non-billable and billable data points <https://www.braze.com/docs/user_guide/data_and_analytics/data_points/#data-points-1>`__ |ext_link|, and then review those lists against the attributes you will send to Braze from Amperity to understand which of those attributes are considered billable or non-billable data points.

.. destination-braze-data-points-end

.. TODO: Uncomment these inclusions:

.. 
.. .. include:: ../../amperity_amp360/source/destination_braze.rst
..    :start-after: .. destination-braze-data-points-start
..    :end-before: .. destination-braze-data-points-end
.. 


.. profile-api-usecase-braze-connected-content-does-not-use-data-points-start

.. important:: Connected Content does not write data to user profiles, which means you can use Connected Content to dynamically populate values into messages without consuming data points.

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-end


.. TODO: Replace the previous paragraph with the following after this topic has been moved back into the operators guide.

.. 
.. .. profile-api-usecase-braze-connected-content-does-not-use-data-points-start
.. 
.. .. important:: :ref:`Connected Content <profile-api-usecase-braze>` does not write data to user profiles, which means you can use Connected Content to dynamically populate values into messages without consuming data points.
.. 
.. .. profile-api-usecase-braze-connected-content-does-not-use-data-points-end
.. 

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
          :align: left
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
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **API key**

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

             The API key that you will use to configure Amperity credentials is available from the **Identifier** column on the **Rest API Key** page and is similar to: "a1bc2345-678d-9012-e3fg-hi34jk5l6789".

             .. image:: ../../images/destination-braze-rest-api-identifier.png
                :width: 500 px
                :alt: Add the identifier that is required by this workflow.
                :align: left
                :class: no-scaled-link


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
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

       **Profile updates?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-profile-updates-start
             :end-before: .. setting-braze-profile-updates-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-profile-updates-usewhen-start
             :end-before: .. setting-braze-profile-updates-usewhen-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - A list of `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link| and/or `custom attributes <https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/>`__ |ext_link| that may be sent to |destination-name| from Amperity.


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
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
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
          :align: left
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
          :align: left
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
          :align: left
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
          :align: left
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

       **Profile updates?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-profile-updates-start
             :end-before: .. setting-braze-profile-updates-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-profile-updates-usewhen-start
             :end-before: .. setting-braze-profile-updates-usewhen-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
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
