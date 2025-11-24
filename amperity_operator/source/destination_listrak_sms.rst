.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Listrak SMS
.. |plugin-name| replace:: "Listrak SMS"
.. |credential-type| replace:: "listrak-sms"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "phone"
.. |what-send| replace:: phone numbers and SMS profile attributes
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "list"


.. meta::
    :description lang=en:
        Configure Amperity to send SMS profiles to Listrak.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send SMS profiles to Listrak.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Listrak SMS

==================================================
Configure destinations for Listrak SMS
==================================================

.. destination-listrak-sms-about-start

|destination-name| is an automation platform for audience activation through mobile messaging campaigns and personalized SMS marketing.

.. destination-listrak-sms-about-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-sms-optin-start
   :end-before: .. setting-listrak-sms-optin-end

.. destination-listrak-sms-context-start

Use the `Listrak SMS REST API <https://api.listrak.com/sms>`__ |ext_link| to manage SMS profiles in |destination-name|.

.. destination-listrak-sms-context-end


.. _destination-listrak-sms-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-listrak-sms-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       You must configure this destination for SMS profiles:

       **SMS client ID and client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-sms-client-id-secret-start
             :end-before: .. credential-listrak-sms-client-id-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-client-id-secret-location-start
             :end-before: .. credential-listrak-client-id-secret-location-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **SMS lists and Listrak**

       An active SMS list must exist in |destination-name| before Amperity can send SMS profiles to that list.

       #. Log in to `your Listrak account <https://admin.listrak.com/Account/Login.aspx>`__ |ext_link|.
       #. Open the **Contacts** menu, and then choose **SMS Lists**.
       #. On the **SMS Lists** page, review the list of **Active** lists or click **New list** to add a list.

          The **List Name** in |destination-name| is the value for the **Phone list ID** configuration setting in Amperity.

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-listrak-sms-optin-start
          :end-before: .. setting-listrak-sms-optin-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Define custom SMS profile attributes**

       `Custom SMS profile attributes <https://help.listrak.com/en/articles/1852936-sms-profile-fields-and-personalization-guide>`__ |ext_link| must be created in |destination-name| before Amperity can send custom attributes.

       * Up to fifty custom attributes may be defined in |destination-name|.

         .. include:: ../../shared/destination_settings.rst
            :start-after: .. setting-listrak-sms-enable-segmentation-caveat-start
            :end-before: .. setting-listrak-sms-enable-segmentation-caveat-end

       * Custom attributes are defined in the |destination-name| user interface. Open the **Contacts** menu, and then choose **Profile Fields**. Click **New Profile Field** to add custom attributes.
       * System fields--**Birthday**, **Email Address**, **First Name**, **Last Name**, and **Postal Code**--are pre-defined by |destination-name| and cannot be modified.
       * **Phone Number** is the primary identifier for each SMS profile and is required.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **SMS list ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-sms-phone-list-id-start
             :end-before: .. setting-listrak-sms-phone-list-id-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-default-list-name-start
             :end-before: .. setting-listrak-default-list-name-end

       **Sender code ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-sms-sender-code-id-start
             :end-before: .. setting-listrak-sms-sender-code-id-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 5.
          :align: center
          :class: no-scaled-link
     - **Audience configuration**

       Use a query or a segment to build an audience to send to |destination-name|. The **phone** field must be part of the audience. You may append additional profile attributes to the query or segment.

.. destination-listrak-sms-get-details-end


.. _destination-listrak-sms-attributes:

About Listrak SMS profile attributes
==================================================

.. destination-listrak-sms-attributes-start

|destination-name| uses phone numbers as the primary identifier for each SMS profile.

|destination-name| has the following SMS pre-defined attributes to collect additional information about SMS profiles.

**System fields**

* **Birthday** Use for date-based segmentation.
* **Email Address** A contact attribute.
* **First Name** and **Last Name** Use for personalization.
* **Postal Code** Use for location targeting.

Use system attributes to personalize messages, such as adding a first name to an SMS message, and to filter messages to only those who match certain criteria.

**Custom attributes**

Enable the **Include attributes that match custom profile fields** field to sychronize all profile attributes in Amperity that match custom profile fields defined in |destination-name|.

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-sms-enable-segmentation-caveat-start
   :end-before: .. setting-listrak-sms-enable-segmentation-caveat-end

|destination-name| supports up to fifty custom SMS profile attributes. Use these to define additional SMS profile attributes to support your brand's use cases.

.. important:: Each custom attribute must be defined in |destination-name| before Amperity can send them with SMS profiles.

Custom attributes must be one of the following data types: `Checkbox, Date, Number, or Text <https://help.listrak.com/en/articles/1852936-sms-profile-fields-and-personalization-guide#custom-profile-fields>`__ |ext_link|. Any custom attributes sent from Amperity must match one of these data types.

.. destination-listrak-sms-attributes-end


.. _destination-listrak-sms-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Listrak SMS**

.. destination-listrak-sms-credentials-steps-start

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

       You must configure this destination for SMS profiles:

       **SMS client ID and client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-sms-client-id-secret-start
             :end-before: .. credential-listrak-sms-client-id-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-client-id-secret-location-start
             :end-before: .. credential-listrak-client-id-secret-location-end

.. destination-listrak-sms-credentials-steps-end


.. _destination-listrak-sms-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Listrak SMS**

.. destination-listrak-sms-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
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
          :alt: Step two.
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

       **SMS list ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-sms-phone-list-id-start
             :end-before: .. setting-listrak-sms-phone-list-id-end

          .. note::  Lists are available from the **Contacts** menu within the |destination-name| user interface. Open the **Contacts** menu, and then choose **SMS Lists**.

             .. include:: ../../shared/destination_settings.rst
                :start-after: .. setting-listrak-default-list-name-start
                :end-before: .. setting-listrak-default-list-name-end

       **Sender code ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-sms-sender-code-id-start
             :end-before: .. setting-listrak-sms-sender-code-id-end


       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Include attributes that match custom profile fields**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-sms-enable-segmentation-start
             :end-before: .. setting-listrak-sms-enable-segmentation-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-sms-enable-segmentation-caveat-start
             :end-before: .. setting-listrak-sms-enable-segmentation-caveat-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-listrak-sms-add-steps-end


.. _destination-listrak-sms-sftp:

Customers, products, and orders
==================================================

.. include:: ../../amperity_operator/source/destination_listrak.rst
   :start-after: .. destination-listrak-sftp-start
   :end-before: .. destination-listrak-sftp-end
