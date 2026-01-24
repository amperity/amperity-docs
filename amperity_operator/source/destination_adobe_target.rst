.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Adobe Target
.. |plugin-name| replace:: "Adobe Target"
.. |credential-type| replace:: "adobe-target"
.. |required-credentials| replace:: "client code" and "bearer token"
.. |what-send| replace:: profile parameters
.. |where-send| replace:: |destination-name|
.. |allow-for-what| replace:: profile parameter updates
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Configure Amperity to send profile parameters to Adobe Target.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send profile parameters to Adobe Target.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure profile parameters for Adobe Target

==================================================
Configure profile parameters for Adobe Target
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-adobe-target-start
   :end-before: .. term-adobe-target-end

.. destination-adobe-target-overview-start

Send profile parameters from Amperity to |destination-name| and manage the collection of profile parameters your brand uses for personalization and optimization from your Amperity customer 360 database.

.. destination-adobe-target-overview-end

.. destination-adobe-target-api-note-start

.. note:: Amperity uses the `Bulk Profile Update API <https://experienceleague.adobe.com/en/docs/target-dev/developer/api/profile-apis/profile-bulk-api>`__ |ext_link| to send |what-send| to |where-send|.

   Profiles are unique by **thirdPartyId**. Each profile property value

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-adobe-target-api-note-end


.. _destination-adobe-target-profile-parameters:

What are profile parameters?
==================================================

.. destination-adobe-target-profile-parameters-start

`Profile parameters <https://experienceleague.adobe.com/en/docs/target/using/audiences/visitor-profiles/profile-parameters>`__ |ext_link| in Adobe Target are attributes specific to the customer identified by a **thirdPartyId**. Profile parameters are stored in the |destination-name| profile store and can be accessed by the |destination-name| cookie to collect information that supports personalization and optimization use cases.

Each customer's profile collection contains demographic and behavioral information, such as age, gender, purchase history, product preferences, and geographic location.

Profile parameters are an object referenced from a profile script using the **profile.get('<profile_parameter>')** function call. Each profile parameter sent to |destination-name| from Amperity is accessble using individual function calls. For example, if profile properties exist for **gender**, **favoriteProduct**, **lastPurchaseDate**, and **loyaltyTier** in Adobe Target, each profile parameter is accessable from a profile script using a function call for each profile parameter. For example: **profile.get('<favoriteProduct>')**.

.. destination-adobe-target-profile-parameters-end

.. destination-adobe-target-profile-parameters-pii-caution-start

.. caution:: Profile parameters that contain `personally identifiable information (PII) should be hashed before uploading <https://experienceleague.adobe.com/en/docs/core-services/interface/services/customer-attributes/privacy-mac>`__ |ext_link| to |destination-name|. Hashed information is useful for analysis and for marketing activity in |destination-name|. Sensitive information, such as medical records, financial account information, or information about minors, should never be sent to |destination-name|.

   `Profile parameter values sent using the Bulk Profile Update API are stored for up to 14 days <https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-14022>`__ |ext_link|, after which inactive profile parameters are deleted and inactive profiles expire.

.. destination-adobe-target-profile-parameters-pii-caution-end


.. _destination-adobe-target-activities:

Personalization and optimization activities
--------------------------------------------------

.. destination-adobe-target-activities-start

Use |destination-name| to test variations of websites and mobile apps to optimize shopping experiences and to personalize offers on websites, mobile apps, and social media platforms.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - |destination-name| activity types
     - Description
   * - **Auto allocation**
     - Use `auto allocation <https://experienceleague.adobe.com/en/docs/target/using/activities/auto-allocate/automated-traffic-allocation>`__ |ext_link| to identify a winner among two or more experiences, and then redirect traffic to the experience with the best conversion rate.

   * - **Auto targeting**
     - Use `auto targeting <https://experienceleague.adobe.com/en/docs/target/using/activities/auto-target/auto-target-to-optimize>`__ |ext_link| to personalize conversions based on individual customer profiles and historical behavior.

   * - **Automated personalization**
     - Use `automated personalization <https://experienceleague.adobe.com/en/docs/target/using/activities/automated-personalization/automated-personalization>`__ |ext_link| to combine specific offers and messages that match different offer variations based on individual customer profiles.

   * - **Experience targeting**
     - Use `experience targeting <https://experienceleague.adobe.com/en/docs/target/using/activities/experience-targeting/experience-target>`__ |ext_link| to deliver content to audiences based on a set of defined rules and criteria.

   * - **Manual A/B testing**
     - Use `manual A/B testing <https://experienceleague.adobe.com/en/docs/target/using/activities/abtest/test-ab>`__ |ext_link| to compare experiences to identify which experience improves conversion rates.

   * - **Multivariate testing**
     - Use `multivariate testing (MVT) <https://experienceleague.adobe.com/en/docs/target/using/activities/multivariate-test/multivariate-testing>`__ |ext_link| to compare combinations of offers to determine which combination offer is best for a specific audience.

   * - **Recommendations**
     - Use `recommendations <https://experienceleague.adobe.com/en/docs/target/using/recommendations/recommendations>`__ |ext_link| to automatically display products, services, or content that might interest visitors based on their previous activity, preferences, or other criteria.

.. destination-adobe-target-activities-end


.. _destination-adobe-target-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-adobe-target-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Client code**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-target-client-code-start
             :end-before: .. credential-adobe-target-client-code-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Authentication token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-target-authentication-token-start
             :end-before: .. credential-adobe-target-authentication-token-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Identifier type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-adobe-target-identifier-start
             :end-before: .. setting-adobe-target-identifier-end

       * **thirdPartyId** (Recommended)

         .. include:: ../../shared/destination_settings.rst
            :start-after: .. setting-adobe-target-identifier-thirdpartyid-start
            :end-before: .. setting-adobe-target-identifier-thirdpartyid-end

       * **pcId**

         .. include:: ../../shared/destination_settings.rst
            :start-after: .. setting-adobe-target-identifier-pcid-start
            :end-before: .. setting-adobe-target-identifier-pcid-end

         .. admonition:: When should the identity type be set to pcId in Amperity?

            Answer: Not often.

           The **pcId** is not the best identity type to send from Amperity because **pcId** interacts with the |destination-name| profile store directly from the cookie.

            When a visitor accesses a page on which |destination-name| is enabled, that visitor is assigned a **pcId**. If the visitor then logs in, and the implementation passes the **mbox3rdPartyId** to |destination-name|, |destination-name| connects that visitor’s **mbox3rdPartyId** with the **pcId**.

          `Updates are synced with the profile store every 5-10 minutes <https://experienceleague.adobe.com/en/docs/target/using/audiences/visitor-profiles/3rd-party-id>`__ |ext_link|. When the visitor’s session ends, the merged data replaces the previous data associated with the **mbox3rdPartyId**, creating a complete record of that visitor’s actions.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - A list of profile parameters to send to |destination-name|.

       * Parameter names are case-sensitive. **firstName**, **firstname**, **first_name**, and **Firstname** are different parameter names.

       * `Parameter names cannot be the same as a system parameter name <https://experienceleague.adobe.com/en/docs/target/using/audiences/visitor-profiles/variables-profiles-parameters-methods>`__ |ext_link|, inculding **averageDaysBetweenVisits**, **browserTime**, **geolocation**, **mobile**, **parameter**, **sessionCount** or **user**.

       * Parameter values are case-sensitive.

       * Parameters should not contain unhashed personally identifiable information (PII).

       * Parameters must not contain sensitive data, such as medical records, financial records, or information about minors.

       * **thirdPartyId** or **pcId** must be the name of the first column in the dataset sent to |destination-name|.

       * There is no restriction on the number of attributes you can upload to the |destination-name| profile store. However, the total size of external profile data, which includes Adobe Customer Attributes, profile parameters in the |destination-name| profile store, |destination-name| Mbox profile parameters, and profile script output, must not exceed 64 KB.

.. destination-adobe-target-get-details-table-end


.. _destination-adobe-target-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Adobe Target**

.. destination-adobe-target-credentials-steps-start

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

       **Client code**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-target-client-code-start
             :end-before: .. credential-adobe-target-client-code-end

       **Authentication token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-adobe-target-authentication-token-start
             :end-before: .. credential-adobe-target-authentication-token-end

.. destination-adobe-target-credentials-steps-end


.. _destination-adobe-target-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. destination-adobe-target-add-destination-start

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

       Enter the name of the destination and a description. For example: "|destination-name| events" and "Send events to |destination-name|.".


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end


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

       **Identifier type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-adobe-target-identifier-start
             :end-before: .. setting-adobe-target-identifier-end

          **thirdPartyId**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-adobe-target-identifier-thirdpartyid-start
             :end-before: .. setting-adobe-target-identifier-thirdpartyid-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. destination-adobe-target-add-destination-end


.. _destination-adobe-target-build-dataset:

Build a dataaset for Adobe Target
==================================================

.. destination-adobe-target-build-dataset-start

Create a dataset dedicated to |destination-name| profile parameters by adding a database table to your customer 360 database or by using a query and mapping fields in your customer 360 database to profile properties your brand wants to us in |destination-name|. Use an orchestration to send the profile parameters to |destination-name| on a batched schedule.

.. destination-adobe-target-build-dataset-end


.. _destination-adobe-target-build-dataset-table:

Adobe Target table
--------------------------------------------------

.. destination-adobe-target-build-dataset-table-start

Add a database table to your customer 360 database with all profile parameters your brand wants to send to |destination-name|. The |destination-name| table should use attributes in the customer 360 database mapped to the names of profile properties your brand keeps in the |destination-name| profile store.

An |destination-name| table consolidates data from multiple tables and uses an **INNER JOIN** on the Amperity ID.

* Give the table a name that ensures all users in your tenant will know what the table is for. For example: **Adobe_Target_Profile_Parameters**.
* The first column in the table must be named **thirdPartyId**. The value of **thirdPartyId** must be a persistent identifier that uniquely identifies visitors to a website, mobile app, social media platform, and other cross-channel locations to which your customers log in. For example, a loyalty ID, a membership number, or a web account ID.
* Parameter names are case-sensitive: **firstName**, **firstname**, **first_name**, and **Firstname** are different parameter names.
* `Parameter names cannot be the same as a system parameter name <https://experienceleague.adobe.com/en/docs/target/using/audiences/visitor-profiles/variables-profiles-parameters-methods>`__ |ext_link|, inculding **averageDaysBetweenVisits**, **browserTime**, **geolocation**, **mobile**, **parameter**, **sessionCount** or **user**.
* Parameters should not contain unhashed personally identifiable information (PII). Apply SHA-256 hashing to any profile parameter that contains PII.
* Parameters must not contain sensitive data, such as medical records, financial records, or information about minors.
* A database table with rows unique by Amperity ID may be made available to the **Segments Editor**.

.. note:: The SQL that your brand requires may be different, depending on which tables are the sources for profile parameters sent to |destination-name|.

.. destination-adobe-target-build-dataset-table-end

**Example SQL for the Adobe_Target_Profile_Parameters table**

.. destination-adobe-target-build-dataset-table-example-start

The following example combines data from three source tables:

#. The **Customer_360** table for a hashed email address.
#. A **Web_Accounts** table for the **Web_Account_Id**. This is a persistent identifier that uniquely identifies visitors and is returned as the value for **thirdPartyId**.
#. A **Unified_Apps** table that has some consolidated interactions data for website and mobile app activity. Most recent login, most recent transaction, primary account time, and the date the customer's account was created.

.. code-block:: sql

   SELECT
     wa.Web_Account_Id AS thirdPartyId
     ,SHA2(LOWER(TRIM(c360.email)),256) AS email
     ,ua.lastLogin AS lastLogin
     ,ua.lastTransaction AS lastTransaction
     ,ua.primaryAccountType AS primaryAccountType
     ,ua.openDate AS openDate
   FROM Web_Accounts AS wa
   INNER JOIN Customer_360 AS c360 ON wa.amperity_id = c360.amperity_id
   INNER JOIN Unified_Apps AS ub ON wa.amperity_id = ua.amperity_id
   GROUP BY
     wa.Web_Account_Id
     ,c360.email
     ,ua.lastLogin
     ,ua.lastTransaction
     ,ua.primaryAccountType
     ,ua.openDate

.. destination-adobe-target-build-dataset-table-example-end


.. _destination-adobe-target-build-dataset-query:

Adobe Target query
--------------------------------------------------

.. destination-adobe-target-build-dataset-query-start

A query that returns profile parameters to send to |destination-name| maps attributes in the customer 360 database to the names of profile properties in the |destination-name| profile store.

.. destination-adobe-target-build-dataset-query-end

.. destination-adobe-target-build-dataset-query-tips-start

An query can consolidate data from multiple tables.

* Give the query a name that ensures all users in your tenant will know what the query is for. For example: **Adobe_Target_Profile_Parameters**.
* The first column returned by the query must be named **thirdPartyId**. The value of **thirdPartyId** must be a persistent identifier that uniquely identifies visitors to a website, mobile app, social media platform, and other cross-channel locations to which your customers log in. For example, a loyalty ID, a membership number, or a web account ID.
* Parameter names are case-sensitive: **firstName**, **firstname**, **first_name**, and **Firstname** are different parameter names.
* `Parameter names cannot be the same as a system parameter name <https://experienceleague.adobe.com/en/docs/target/using/audiences/visitor-profiles/variables-profiles-parameters-methods>`__ |ext_link|, inculding **averageDaysBetweenVisits**, **browserTime**, **geolocation**, **mobile**, **parameter**, **sessionCount** or **user**.
* Parameters should not contain unhashed personally identifiable information (PII). Apply SHA-256 hashing to any profile parameter that contains PII.
* Parameters must not contain sensitive data, such as medical records, financial records, or information about minors.
* A query that returns rows unique by Amperity ID may be made available to the **Segments Editor**.

.. note:: The SQL that your brand requires may be different, depending on which tables are the sources for profile parameters sent to |destination-name|.

.. destination-adobe-target-build-dataset-query-tips-end

**Example SQL for the Adobe_Target_Profile_Parameters query**

.. destination-adobe-target-build-dataset-query-example-start

.. code-block:: sql

   SELECT
     wa.Web_Account_Id AS thirdPartyId
     ,SHA256(TO_UTF8(LOWER(TRIM(c360.email)))) AS email
     ,ua.lastLogin AS lastLogin
     ,ua.lastTransaction AS lastTransaction
     ,ua.primaryAccountType AS primaryAccountType
     ,ua.openDate AS openDate
   FROM Web_Accounts AS wa
   INNER JOIN Customer_360 AS c360 ON wa.amperity_id = c360.amperity_id
   INNER JOIN Unified_Apps AS ua ON wa.amperity_id = ua.amperity_id
   GROUP BY
     wa.Web_Account_Id
     ,c360.email
     ,ua.lastLogin
     ,ua.lastTransaction
     ,ua.primaryAccountType
     ,ua.openDate

.. destination-adobe-target-build-dataset-query-example-end
