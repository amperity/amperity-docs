.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Meta Ads Manager
.. |plugin-name| replace:: "Facebook"
.. |credential-type| replace:: "facebook"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: custom audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "meta"
.. |allow-for-what| replace:: custom audiences
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Meta Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Meta Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Meta Ads Manager

==================================================
Configure campaigns for Meta Ads Manager
==================================================

.. campaign-meta-ads-manager-start

Send custom audiences to |destination-name| to help find people who already know about or have engaged with your brand. Use custom audiences for re-marketing, finding potential repeat customers, and finding lookalike audiences that can be activated from Facebook, Facebook Messenger, Instagram, and WhatsApp.

The `Facebook Marketing API <https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences>`__ |ext_link|, specifically the `Replace Users endpoint <https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences#replace-api>`__ |ext_link|, is used to send custom audiences.

This endpoint removes existing customers from an audience **without resetting your ad set's learning phase when an audience is part of active ad sets**, and then replaces those users with the list of customers that was sent to |destination-name| from Amperity.

.. campaign-meta-ads-manager-end

.. note::

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end


.. _campaign-meta-ads-manager-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-meta-ads-manager-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Access token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Meta Ads Manager settings**

       **Account ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-meta-ads-manager-account-id-start
             :end-before: .. setting-meta-ads-manager-account-id-end

       **Custom audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-meta-ads-manager-custom-audience-name-start
             :end-before: .. setting-meta-ads-manager-custom-audience-name-end

       **Customer file source**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-meta-ads-manager-customer-file-source-start
             :end-before: .. setting-meta-ads-manager-customer-file-source-end


.. campaign-meta-ads-manager-get-details-end


.. _campaign-meta-ads-manager-meta-ads-manager:

About Meta Ads Manager
--------------------------------------------------

.. campaign-meta-ads-manager-meta-ads-manager-start

Audiences sent to Meta Ads Manager have access to Facebook, Messenger, Instagram and the Meta Audience Network.


.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-facebook-ads.svg
          :width: 140 px
          :alt: Facebook Ads
          :align: center
          :class: no-scaled-link
     - Use Meta Ads Manager to configure `a variety of ad placements across Facebook <https://www.facebook.com/business/help/407108559393196?id=369787570424415>`__ |ext_link|.

   * - .. image:: ../../amperity_base/source/_static/connector-instagram.svg
          :width: 140 px
          :alt: Instagram
          :align: center
          :class: no-scaled-link
     - Use Meta Ads Manager to configure objectives that `place ads on Instagram <https://www.facebook.com/business/help/1634705703469129?helpref=search&sr=2&query=create%20ads%20in%20instagram>`__ |ext_link|.

   * - .. image:: ../../amperity_base/source/_static/connector-facebook-messenger.svg
          :width: 140 px
          :alt: Facebook Messenger
          :align: center
          :class: no-scaled-link
     - Use Meta Ads Manager to configure objectives that `place ads on Messenger <https://www.facebook.com/business/help/1420905584664062?id=274377816589261>`__ |ext_link|.

   * - .. image:: ../../amperity_base/source/_static/connector-whatsapp.svg
          :width: 140 px
          :alt: WhatsApp
          :align: center
          :class: no-scaled-link
     - Use `Audience Manager <https://www.facebook.com/business/help/1409448922609084?id=571563249872422&ref=fbb_an>`__ |ext_link| to reach users who are not on Facebook or Instagram, but are on mobile apps that are within the audience network. For example, creating ads that `open conversation threads in WhatsApp <https://www.facebook.com/business/help/447934475640650?id=371525583593535>`__ |ext_link|.

.. campaign-meta-ads-manager-meta-ads-manager-end


.. _campaign-meta-ads-manager-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Meta Ads Manager**

.. campaign-meta-ads-manager-credentials-steps-start

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

       **Access token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. campaign-meta-ads-manager-credentials-steps-end


.. _campaign-meta-ads-manager-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _campaign-meta-ads-manager-terms-of-service:

Terms of service
--------------------------------------------------

.. TODO: Sync this with the updated events topics.

.. campaign-meta-ads-manager-terms-of-service-start

The `custom audience terms of service <https://developers.facebook.com/docs/marketing-api/audiences/reference/custom-audience-terms-of-service/>`__ |ext_link| must be signed by *each business user* that is associated with your |destination-name| account. If the terms of service are not signed, a permissions error prevents Amperity from sending data to |destination-name|.

.. campaign-meta-ads-manager-terms-of-service-end

.. campaign-meta-ads-manager-terms-of-service-error-start

The permissions error is similar to:

::

   Permissions error: To create or edit an audience with an uploaded
   customer list, please agree to the Custom Audience terms at
   https://business.facebook.com/ads/manage/customaudiences/tos/?act=123.

To resolve this error the terms of service must be signed by a business user who has a role in your |destination-name| account.

.. campaign-meta-ads-manager-terms-of-service-error-end


.. _campaign-meta-ads-manager-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Meta Ads Manager**

.. campaign-meta-ads-manager-add-steps-start

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

       **Account ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-meta-ads-manager-account-id-start
             :end-before: .. setting-meta-ads-manager-account-id-end

       **Custom audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-meta-ads-manager-custom-audience-name-start
             :end-before: .. setting-meta-ads-manager-custom-audience-name-end

       **Customer file source**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-meta-ads-manager-customer-file-source-start
             :end-before: .. setting-meta-ads-manager-customer-file-source-end


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


.. campaign-meta-ads-manager-add-steps-end


.. _campaign-meta-ads-manager-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. campaign-meta-ads-manager-workflow-actions-start

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

       .. image:: ../../images/workflow-actions-meta-ads-manager-missing-extern-id.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-meta-ads-manager-workflow-actions-authorization-error`
       * :ref:`destination-meta-ads-manager-workflow-actions-cannot-create-ads`
       * :ref:`destination-meta-ads-manager-workflow-actions-extern-id-missing`
       * :ref:`destination-meta-ads-manager-workflow-actions-invalid-credentials`
       * :ref:`destination-meta-ads-manager-workflow-actions-maximum-audiences`
       * :ref:`destination-meta-ads-manager-workflow-actions-facebook-terms`
       * :ref:`destination-meta-ads-manager-workflow-actions-business-account`
       * :ref:`destination-meta-ads-manager-workflow-actions-security-challenge`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-meta-ads-manager-missing-extern-id-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. campaign-meta-ads-manager-workflow-actions-end


.. _campaign-meta-ads-manager-workflow-actions-authorization-error:

Authorization error
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-oauth-start
   :end-before: .. term-oauth-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _campaign-meta-ads-manager-workflow-actions-cannot-create-ads:

Cannot create ads
--------------------------------------------------

.. campaign-meta-ads-manager-workflow-actions-cannot-create-ads-start

The advertising account that is used by this workflow must have permission to create ads.

.. campaign-meta-ads-manager-workflow-actions-cannot-create-ads-end

.. campaign-meta-ads-manager-workflow-actions-cannot-create-ads-steps-start

To resolve this error, update the user permissions in |destination-name| to ensure that the advertising account can create ads.

#. Log into |destination-name| and verify the user permissions for the account.
#. Update the user permissions to ensure that the **Create and edit ads** permission is assigned to the advertising account used by this workflow.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-meta-ads-manager-workflow-actions-cannot-create-ads-steps-start


.. _campaign-meta-ads-manager-workflow-actions-extern-id-missing:

EXTERN_ID is missing
--------------------------------------------------

.. campaign-meta-ads-manager-workflow-actions-extern-id-missing-start

An **EXTERN_ID** is a unique ID used within |destination-name|, such as a loyalty ID, a customer ID, an external ID, or the Amperity ID.

Amperity will be unable to send orchestrations or campaigns when **EXTERN_ID** is not included within an audience that is sent to |destination-name|.

.. campaign-meta-ads-manager-workflow-actions-extern-id-missing-end

**For campaigns**

.. campaign-meta-ads-manager-workflow-actions-extern-id-missing-campaigns-steps-start

To resolve this error, verify that **EXTERN_ID** is included in the list of attributes that are being sent to |destination-name|.

#. Open the **Campaigns** page, and then open the segment used with this workflow.
#. Verify that **EXTERN_ID** is included in the list of attributes for each treatment group that sends audiences to |destination-name|. Update the list of attributes for each treatment group if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-meta-ads-manager-workflow-actions-extern-id-missing-campaigns-steps-start

**For orchestrations**

.. campaign-meta-ads-manager-workflow-actions-extern-id-missing-orchestrations-steps-start

To resolve this error, verify that **EXTERN_ID** is included in the query results.

#. Open the **Queries** page, and then open the query used with this workflow.
#. Verify that **EXTERN_ID** is included in the query results. Update the query if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-meta-ads-manager-workflow-actions-extern-id-missing-orchestrations-steps-start


.. _campaign-meta-ads-manager-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _campaign-meta-ads-manager-workflow-actions-maximum-audiences:

Maximum custom audiences exceeded
--------------------------------------------------

.. campaign-meta-ads-manager-workflow-actions-maximum-audiences-start

|destination-name| supports having up to 500 custom audiences in your account at any given time. Amperity will be unable to create custom audiences when this limit is exceeded.

.. campaign-meta-ads-manager-workflow-actions-maximum-audiences-end

.. campaign-meta-ads-manager-workflow-actions-maximum-audiences-steps-start

To resolve this error, verify the number of custom-audiences associated with your |destination-name| account.

#. Log into |destination-name| and verify the number of custom audiences that are associated with your |destination-name| account.
#. Remove custom audiences that are not in active use.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-meta-ads-manager-workflow-actions-maximum-audiences-steps-start


.. _campaign-meta-ads-manager-workflow-actions-facebook-terms:

Must agree to Facebook terms
--------------------------------------------------

.. campaign-meta-ads-manager-workflow-actions-facebook-terms-start

The `custom audience terms of service <https://developers.facebook.com/docs/marketing-api/audiences/reference/custom-audience-terms-of-service/>`__ |ext_link| must be signed by *each business user* that is associated with your Facebook Ads account. If the terms of service are not signed, a permissions error prevents Amperity from sending data to Facebook Ads.

When the business user has not agreed to Facebook terms, an error similar to the following is shown:

::

   Permissions error: To create or edit an audience with an uploaded customer list,
   please agree to the Custom Audience terms at
   https://business.facebook.com/ads/manage/customaudiences/tos/?act=1234567890123456.

.. campaign-meta-ads-manager-workflow-actions-facebook-terms-end

.. campaign-meta-ads-manager-workflow-actions-facebook-terms-steps-start

To resolve this error, log into |destination-name| as the business user associated with this workflow and agree to the terms of service.

#. Follow the instructions in the error message, and then open the provided link in a new tab.
#. Log in as the business user associated with this workflow, and then agree to the Facebook terms of service.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-meta-ads-manager-workflow-actions-facebook-terms-steps-start


.. _campaign-meta-ads-manager-workflow-actions-business-account:

Must belong to business account
--------------------------------------------------

.. campaign-meta-ads-manager-workflow-actions-business-account-start

The advertising account used to enable workflows to be sent to |destination-name| from Amperity requires the advertising account to *also* belong to a business account. When an advertising account does not also belong to a business account, Amperity workflows will be unable to create or edit a custom audience.

.. campaign-meta-ads-manager-workflow-actions-business-account-end

.. campaign-meta-ads-manager-workflow-actions-business-account-steps-start

To resolve this error, verify that the advertising account also belongs to a business account.

#. Log into |destination-name| and verify the configuration for the advertising account to ensure that it also belongs to a business account.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-meta-ads-manager-workflow-actions-business-account-steps-start


.. _campaign-meta-ads-manager-workflow-actions-security-challenge:

Security challenge
--------------------------------------------------

.. campaign-meta-ads-manager-workflow-actions-security-challenge-start

Sometimes |destination-name| issues a security challenge to the advertising account or business account associated with this workflow.

.. campaign-meta-ads-manager-workflow-actions-security-challenge-end

.. campaign-meta-ads-manager-workflow-actions-security-challenge-steps-start

To resolve this error, complete the steps that are required to resolve the security challenge.

#. Log into |destination-name| using the link provided in the workflow action, and then follow the instructions to resolve the security challenge.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-meta-ads-manager-workflow-actions-security-challenge-steps-start


.. _campaign-meta-ads-manager-api-keys:

Facebook Marketing API keys
==================================================

.. campaign-meta-ads-manager-api-keys-start

The following Amperity columns should be mapped to the corresponding `Facebook Marketing API <https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences>`__ |ext_link| keys when they are present in query data:

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity Column
     - Facebook API Key
     - Description

   * - **Amperity ID**
     - **EXTERN_ID**
     - This value is a unique ID used by the advertiser, such as a loyalty ID, a customer ID, an external cookie ID, or the Amperity ID.

       For this key, the connector trims leading and trailing whitespace.

       .. tip:: A query can alias the Amperity ID directly in a query: **SELECT amperity_id AS EXTERN_ID from custom_table**. This approach can be helpful for queries that are dedicated to returning data to be sent only to Facebook Ads.

   * - **Email Addresses**
     - **EMAIL**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Hashes data as SHA-256

   * - **Phone Numbers**
     - **PHONE**
     - Converts each phone number to |ext_e164_format| which represents a phone number as a number up to fifteen digits in length (without spaces) that starts with a + symbol. For example: +12061234567.

       For this key, the connector:

       * Trims leading and trailing whitespace
       * Removes symbols, letters, and any leading zeros
       * Hashes data as SHA-256

   * - **Gender**
     - **GEN**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Converts to m and f
       * Hashes data as SHA-256

   * - **Birth Date**
     - **BIRTH**
     - The birth date in Amperity date format.

       For this key, the connector splits this value into three fields: birth year (DOBY), birth month (DOBM), and birth day (DOBD).

   * - **Birth Year**
     - **DOBY**
     - .. warning:: Do not pass this column. For this key, the connector uses birthdate to split out the value for DOBY with a format of **YYYY** and a range from 1900 to the current year.

   * - **Birth Month**
     - **DOBM**
     - .. warning:: Do not pass this column. For this key, the connector uses birthdate to split out the value for DOBM with a format of **01** to **12**.

   * - **Birth Day**
     - **DOBD**
     - .. warning:: Do not pass this column. For this key, the connector uses birthdate to split out the value for DOBD with a format of **01** to **31**.

   * - **Last Name**
     - **LN**
     - This key supports special characters and non-Roman alphabet characters. For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Removes punctuation
       * Updates special characters to `UTF-8 format <https://en.wikipedia.org/wiki/UTF-8>`__ |ext_link|
       * Hashes data as SHA-256
   * - **First Name**
     - **FN**
     - This key supports special characters and non-Roman alphabet characters. For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Removes punctuation
       * Updates special characters to `UTF-8 format <https://en.wikipedia.org/wiki/UTF-8>`__ |ext_link|
       * Hashes data as SHA-256
   * - **First Initial**
     - **FI**
     - .. warning:: Do not pass this column. The connector uses the first character of the normalized first name.
   * - **US States**
     - **ST**
     - A two-character `ANSI abbreviation code <https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations>`__ |ext_link| for US states.

       For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Normalizes states located outside of the United States
       * Removes punctuation, special characters, and whitespace
       * Hashes data as SHA-256
   * - **City**
     - **CT**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Removes punctuation, special characters, and whitespace
       * Hashes data as SHA-256
   * - **Zip Code**
     - **ZIP**
     - Use only the first five digits for the United States. Use `postcodes (area, district, sector) format <https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom>`__ |ext_link| for United Kingdom.

       For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Removes whitespace from lower-case for United Kingdom
       * Trims to five digits for United States
       * Hashes data as SHA-256
   * - **Country Code**
     - **COUNTRY**
     - A two-letter country code in |ext_iso_31661alpha2| format.

       For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Hashes data as SHA-256
   * - **Mobile Advertiser ID**
     - **MADID**
     - For this key, the connector:

       * Trims leading and trailing whitespace
       * Converts to lower-case
       * Keeps hyphens
       * Hashes data as SHA-256

.. campaign-meta-ads-manager-api-keys-end
