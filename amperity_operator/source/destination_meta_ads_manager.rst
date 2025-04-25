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
        Configure Amperity to send custom audiences to Meta Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send custom audiences to Meta Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send custom audiences to Meta Ads Manager

==================================================
Send custom audiences to Meta Ads Manager
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_meta_ads_manager.html>`__ |ext_link|.

.. destination-meta-ads-manager-start

Send custom audiences to |destination-name| to help find people who already know about or have engaged with your brand. Use custom audiences for re-marketing, finding potential repeat customers, and finding lookalike audiences that can be activated from Facebook, Facebook Messenger, Instagram, and WhatsApp.

The |ext_facebook_marketing_api|, specifically the |ext_facebook_marketing_api_replace_users|, is used to send custom audiences.

This endpoint removes existing customers from an audience **without resetting your ad set's learning phase when an audience is part of active ad sets**, and then replaces those users with the list of customers that was sent to |destination-name| from Amperity.

.. destination-meta-ads-manager-end

.. note::

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end


.. _destination-meta-ads-manager-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-meta-ads-manager-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
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
          :align: left
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


.. destination-meta-ads-manager-get-details-end


.. _destination-meta-ads-manager-meta-ads-manager:

About Meta Ads Manager
--------------------------------------------------

.. destination-meta-ads-manager-meta-ads-manager-start

Audiences sent to Meta Ads Manager have access to Facebook, Messenger, Instagram and the Meta Audience Network.


.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - .. image:: ../../amperity_base/source/_static/connector-facebook-ads.svg
          :width: 140 px
          :alt: Facebook Ads
          :align: left
          :class: no-scaled-link
     - Use Meta Ads Manager to configure `a variety of ad placements across Facebook <https://www.facebook.com/business/help/407108559393196?id=369787570424415>`__ |ext_link|.

   * - .. image:: ../../amperity_base/source/_static/connector-instagram.svg
          :width: 140 px
          :alt: Instagram
          :align: left
          :class: no-scaled-link
     - Use Meta Ads Manager to configure objectives that `place ads on Instagram <https://www.facebook.com/business/help/1634705703469129?helpref=search&sr=2&query=create%20ads%20in%20instagram>`__ |ext_link|.

   * - .. image:: ../../amperity_base/source/_static/connector-facebook-messenger.svg
          :width: 140 px
          :alt: Facebook Messenger
          :align: left
          :class: no-scaled-link
     - Use Meta Ads Manager to configure objectives that `place ads on Messenger <https://www.facebook.com/business/help/1420905584664062?id=274377816589261>`__ |ext_link|.

   * - .. image:: ../../amperity_base/source/_static/connector-whatsapp.svg
          :width: 140 px
          :alt: WhatsApp
          :align: left
          :class: no-scaled-link
     - Use `Audience Manager <https://www.facebook.com/business/help/1409448922609084?id=571563249872422&ref=fbb_an>`__ |ext_link| to reach users who are not on Facebook or Instagram, but are on mobile apps that are within the audience network. For example, creating ads that `open conversation threads in WhatsApp <https://www.facebook.com/business/help/447934475640650?id=371525583593535>`__ |ext_link|.

.. destination-meta-ads-manager-meta-ads-manager-end


.. _destination-meta-ads-manager-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Meta Ads Manager**

.. destination-meta-ads-manager-credentials-steps-start

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

       **Access token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-meta-ads-manager-credentials-steps-end


.. _destination-meta-ads-manager-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-meta-ads-manager-terms-of-service:

Terms of service
--------------------------------------------------

.. TODO: Sync this with the updated events topics.

.. destination-meta-ads-manager-terms-of-service-start

The |ext_facebook_tos| must be signed by *each business user* that is associated with your |destination-name| account. If the terms of service are not signed, a permissions error will prevent Amperity from sending data to |destination-name|.

.. destination-meta-ads-manager-terms-of-service-end

.. destination-meta-ads-manager-terms-of-service-error-start

The permissions error is similar to:

::

   Permissions error: To create or edit an audience with an uploaded
   customer list, please agree to the Custom Audience terms at
   https://business.facebook.com/ads/manage/customaudiences/tos/?act=123.

To resolve this error the terms of service must be signed by a business user who has a role in your |destination-name| account.

.. destination-meta-ads-manager-terms-of-service-error-end


.. _destination-meta-ads-manager-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Meta Ads Manager**

.. destination-meta-ads-manager-add-steps-start

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


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


.. destination-meta-ads-manager-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.


.. _destination-meta-ads-manager-api-keys:

Facebook Marketing API keys
==================================================

.. destination-meta-ads-manager-api-keys-start

The following Amperity columns should be mapped to the corresponding |ext_facebook_marketing_api| keys when they are present in query data:

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
     - .. warning:: Do not pass this column. For this key, the connector will use birthdate to split out the value for DOBY with a format of **YYYY** and a range from 1900 to the current year.

   * - **Birth Month**
     - **DOBM**
     - .. warning:: Do not pass this column. For this key, the connector will use birthdate to split out the value for DOBM with a format of **01** to **12**.

   * - **Birth Day**
     - **DOBD**
     - .. warning:: Do not pass this column. For this key, the connector will use birthdate to split out the value for DOBD with a format of **01** to **31**.

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
     - .. warning:: Do not pass this column. The connector will use the first character of the normalized first name.
   * - **US States**
     - **ST**
     - A two-character |ext_ansi_abbreviation_code| for US states.

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
     - Use only the first five digits for the United States. Use Use `postcodes (area, district, sector) format <https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom>`__ |ext_link| for United Kingdom.

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

.. destination-meta-ads-manager-api-keys-end
