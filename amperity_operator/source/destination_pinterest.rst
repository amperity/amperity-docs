.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Pinterest
.. |destination-api| replace:: Pinterest API
.. |plugin-name| replace:: "Pinterest"
.. |credential-type| replace:: "pinterest"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "pin"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send email lists to Pinterest.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send email lists to Pinterest.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Pinterest

==================================================
Configure destinations for Pinterest
==================================================

.. destination-pinterest-about-start

|destination-name| is a visual discovery engine on which your brand can engage with your customers. Send a list of products that are in your product catalog to |destination-name| to enable pins, and then send a list of customers with whom your brand wants to engage.

.. destination-pinterest-about-end

.. destination-pinterest-configure-start

You can configure Amperity to maintain a list of SHA-256 hashed email addresses as a customer list in |destination-name| using the |destination-api|. (Amperity automatically applies SHA-256 hashing to all email addresses prior to sending them to |destination-name|.)

.. destination-pinterest-configure-end

.. destination-pinterest-shared-start

A customer list is associated with an audience in |destination-name|, after which your brand may use that audience to advertise on |destination-name|.

Amperity creates the customer list (if it does not already exist), and then add email addresses to that customer list **OR** Amperity updates the customer list (if it already exists) so that it matches the list of email addresses that were sent from Amperity.

.. note:: An existing customer list should be empty the first time Amperity sends a list of email addresses.

When a customer list is not associated with an audience in |destination-name|, Amperity creates an audience using the same name as the list name that was used in Amperity, and then attach the customer list that is managed by Amperity to that audience list.

.. note:: A customer list must contain at least 100 email addresses that are associated with a |destination-name| account before it can be associated with an audience.

.. destination-pinterest-shared-end

.. destination-pinterest-api-note-start

.. admonition:: About Pinterest API endpoints

   Amperity uses a combination of endpoints in the |destination-api|:

   * The `create audience <https://developers.pinterest.com/docs/api/v5/#operation/audiences/create>`__ |ext_link| endpoint to create an audience that can be used to reach specific groups of users in |destination-name|. This converts a customer list into the **CUSTOMER_LIST** audience type.

   * The `create customer list <https://developers.pinterest.com/docs/api/v5/#operation/customer_lists/create>`__ |ext_link| endpoint to create a customer list from a list of SHA-256 hashed email addresses sent to |destination-name| from Amperity.

   * The `update customer list <https://developers.pinterest.com/docs/api/v5/#operation/customer_lists/update>`__ |ext_link| endpoint to manage the list of email addresses in a customer list.

   |destination-name| applies `standard access rate limits <https://developers.pinterest.com/docs/reference/ratelimits/>`__ |ext_link|. Amperity can read from existing customer lists at up to 1000 calls per minute and can write to customer lists at up to 400 calls per minute.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-pinterest-api-note-end


.. _destination-pinterest-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-pinterest-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Ad account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-ad-account-id-start
             :end-before: .. setting-pinterest-ad-account-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Customer list name**

       The customer list name to which the |destination-name| connector sends a list of SHA-256 hashed email addresses.

       If the customer list does not exist, Amperity creates the list using the configured list name, and then add the list of email addresses that are sent from Amperity.

       If the customer list already exists, Amperity updates the list to match the list of email addresses that are sent from Amperity.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - :ref:`Authorize Amperity to send data to the customer's Pinterest account <destination-pinterest-credentials>`.

       All |destination-api| endpoints may only be accessed by an `authenticated Pinterest user <https://developers.pinterest.com/docs/getting-started/authentication/>`__ |ext_link|. |destination-name| identifies this user based on the access token that is passed with each request.

.. destination-pinterest-get-details-end


.. _destination-pinterest-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Pinterest**

.. destination-pinterest-credentials-steps-start

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

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-pinterest-credentials-steps-end


.. _destination-pinterest-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-pinterest-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Pinterest**

.. destination-pinterest-add-steps-start

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

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Ad account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-ad-account-id-start
             :end-before: .. setting-pinterest-ad-account-id-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-pinterest-list-name-start
             :end-before: .. setting-pinterest-list-name-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-pinterest-add-steps-end
