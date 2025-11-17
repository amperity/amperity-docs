.. 
.. xxxxx
..


.. vale off

**COMMON CONTENT FOR BRAZE CAMPAIGNS AND DESTINATIONS**

.. vale on


**About Braze attributes**

First paragraph is not shared.

.. braze-attributes-about-start

When `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link| and `custom attributes <https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/>`__ |ext_link| are available in |destination-name| they can be used to build out audience `segments <https://www.braze.com/docs/user_guide/engagement_tools/segments/creating_a_segment/>`__ |ext_link| and to apply `personalization <https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid>`__ |ext_link| to your campaigns.

.. braze-attributes-about-end


**Customer profiles**

.. braze-customer-profiles-about-start

Customer profiles in |destination-name| are represented by a set of `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link|. To update these fields in |destination-name| you must follow a strict naming convention when sending data from Amperity. These fields are case sensitive and must be lowercase.

.. braze-customer-profiles-about-end

.. braze-customer-profiles-admonition-start

.. admonition:: What about email and phone subscription status?

   |destination-name| uses two fields to track email and phone subscription status: **email_subscribe** and **push_subscribe**. Braze should be your source of truth for customer consent and for tracking email and phone subscription status.

.. braze-customer-profiles-admonition-end

.. vale off

.. braze-customer-profiles-common-attributes-start

The following table describes the default `user profile fields <https://www.braze.com/docs/api/objects_filters/user_attributes_object#braze-user-profile-fields>`__ |ext_link| that are most commonly updated from Amperity:

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Braze default field
     - Amperity field name
     - Description
   * - **external_id**
     - varies
     - Required. The **external_id** is a unique identifier for user profiles in |destination-name|. The **external_id** is a unique identifier that exists in another system, such as the Amperity ID, a loyalty ID, or some other unique customer identifier.

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
     - Optional. Accepted values: "M", "F", "O" (other), "N" (not applicable), "P" (prefer not to say), or **NULL**.

.. braze-customer-profiles-common-attributes-end

.. vale on

.. braze-customer-profiles-common-attributes-note-start

.. note:: Default user profile fields also exist for **alias_name**, **alias_label**, **current_location**, **date_of_first_session**, **date_of_last_session**, **email_open_tracking_disabled**, **email_click_tracking_disabled**, **email_subscribe**, **facebook**, **language**, **marked_email_as_spam_at**, **push_subscribe**, **push_tokens**, **subscription_groups**, **time_zone**, and **twitter**.

   These fields are not commonly sent to |destination-name| from Amperity, but if your brand chooses to update these user profile fields from Amperity, be sure to use the exact name of the default field name, send the correct value or values, and to use lowercase.

.. braze-customer-profiles-common-attributes-note-end



**Custom attributes**

.. braze-custom-attributes-start

Custom attributes in |destination-name| are represented by a set of custom-named fields. The names of these fields are determined by your brand. They may already exist in |destination-name|, in which case shape the output that is sent from Amperity to align to the names you already have.

The names of custom attributes that can be managed by Amperity are defined by your brand. The names are strings, may contain hyphens, spaces, or underscores, may include numbers, and may contain a mix of lowercase and uppercase letters. For example, custom attribute can have names that:

* Already exist within your organization.
* Are exactly the same as Amperity standard output, such as "One and Done" or "L12M Monetary" (the "monetary" component of an RFM score), or "Early Repeat Purchaser".
* Align to marketing goals or terminology that exists within your brand's segmentation strategy.

Verify the names of custom attributes that is sent to |destination-name| from Amperity. Amperity adds a custom attribute whenever there is not a matching name.

.. tip:: Avoid sending custom attributes as duplicates of default user profile fields. For example, birthdates should be sent to |destination-name| as a user profile field named "dob". If they are sent as "birthday", "Birthdate", or any other string, a custom attribute will be created and the values in the "dob" field is not updated.

.. important:: Your brand's list of custom attributes *should* be a list that is static, remains stable over time, and is focused on your most valuable customers.

   Only update custom attributes for customers to which your brand is engaged. Define an audience in Amperity that is some combination of historical or predicted "high value", "active", and are "contactable" because they have an opt-in status of true for phone numbers or email addresses.

   This will help ensure that you are only updating custom attributes for your most valuable customers. Custom attributes is updated only for those customers have a matching "external_id" or "braze_id" within |destination-name|.

.. braze-custom-attributes-end



**Data points**

.. braze-data-points-start

|destination-name| uses `data points <https://www.braze.com/docs/user_guide/data_and_analytics/data_points/>`__ |ext_link| to determine when to update segment membership, to identify which types of messages should be sent, and how to apply message personalization.

You can send custom attributes to |destination-name| from Amperity by attaching attributes from your customer profiles in Amperity, such as first and last names, email addresses, phone numbers, physical locations, SMS and email consent status, and purchase histories.

Amperity tracks changes as they are sent to Braze and only sends list membership and attribute that have changed since the previous update.

.. note:: Data points are part of the billing and pricing structure in your |destination-name| contract. Some data points are non-billable.

   Review the `lists of non-billable and billable data points <https://www.braze.com/docs/user_guide/data_and_analytics/data_points/#data-points-1>`__ |ext_link|, and then review those lists against the attributes you sends to Braze from Amperity to understand which of those attributes are considered billable or non-billable data points.

.. braze-data-points-end



**Audience profile updates**

.. braze-attribute-updates-start

Profile attributes, such as **email**, **birthdate**, **address**, and **phone**, contain stable values. Most customers remain at the same address and have the same phone number for years. An individual customer's birthdate never changes. When customer profile attributes do change your brand will always want to update any downstream audience profiles.

Behavioral attributes, both historical and predicted, are more likely to contain values that change frequently. Behavioral attributes should be evaluated before including them within audience profiles. This will help ensure that updates related to behavioral attributes are adding value to your brand's downstream business use cases.

.. braze-attribute-updates-end

.. braze-attribute-updates-admonition-start

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

          These types of values--1.09413481, 345.47 or .34--often change slightly, but in a way that offers little value to the downstream business use case.

          For example, predictive attributes are refreshed daily. Predicted CLV during the next 365 days might be $345.37 on one day and $348.75 a few days later.

          Instead of using predicted CLV in an audience profile, consider using predicted lifecycle status or predicted value tier, both of which are less likely to change because they represent a range of predicted behaviors instead of a specific predicted value.

      * - **Calculated attribute values**
        - Many attributes are calculated by Amperity, including all time period rollups.

          For example, the **Transaction Attributes Extended** table contains an attribute named **L6M Order Revenue**. This attribute returns the order revenue for each customer over a rolling 6-month timeframe. This attribute is refreshed on a daily basis and the value is updated each time a customer makes a purchase.

          Instead of using the time period rollup attributes directly you can build a custom attribute to define thresholds or to return a yes or no. For example, instead of using the specific revenue amount for **L6M Order Revenue** you could build a custom attribute that returns true when the value for **L6M Order Revenue** is greater than $500.

.. braze-attribute-updates-admonition-end
