.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Pinterest
.. |destination-api| replace:: Pinterest API
.. |plugin-name| replace:: Pinterest
.. |what-send| replace:: email address lists
.. |filter-the-list| replace:: "pin"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |credential-type| replace:: pinterest
.. |credential-details| replace:: the Pinterest API key and API secret
.. |sendto-link| replace:: |sendto_pinterest|
.. |channel-link| replace:: |campaign_pinterest|
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


==================================================
Configure campaigns for Pinterest Ads
==================================================

.. vale off

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_pinterest_ads.html>`__ |ext_link|.

.. vale on

.. include:: ../../shared/terms.rst
   :start-after: .. term-pinterest-start
   :end-before: .. term-pinterest-end

.. destination-pinterest-start

You can configure Amperity to maintain a list of SHA-256 hashed email addresses as a customer list in |destination-name| using the |destination-api|. (Amperity automatically applies SHA-256 hashing to all email addresses prior to sending them to |destination-name|.)

.. destination-pinterest-end

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

.. destination-pinterest-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-pinterest-get-details>`
#. :ref:`Configure OAuth <destination-pinterest-configure-oauth>`
#. :ref:`Add destination <destination-pinterest-add-destination>`
#. :ref:`Add data template <destination-pinterest-add-data-template>`

.. destination-pinterest-steps-to-send-end


.. _destination-pinterest-get-details:

Get details
==================================================

.. destination-pinterest-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Your |destination-name| advertising account ID.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - The customer list name to which the |destination-name| connector sends a list of SHA-256 hashed email addresses.

       If the customer list does not exist, Amperity creates the list using the :ref:`list name defined in the data template <destination-pinterest-add-data-template>`, and then add the list of email addresses that are sent from Amperity.

       If the customer list already exists, Amperity updates the list to match the list of email addresses that are sent from Amperity.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - :ref:`Authorize Amperity to send data to the customer's Pinterest account <destination-pinterest-configure-oauth>`.

       All |destination-api| endpoints may only be accessed by an `authenticated Pinterest user <https://developers.pinterest.com/docs/getting-started/authentication/>`__ |ext_link|. |destination-name| identifies this user based on the access token that is passed with each request.

.. destination-pinterest-get-details-end


.. _destination-pinterest-configure-oauth:

Configure OAuth
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oauth-start
   :end-before: .. term-oauth-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-intro-start
   :end-before: .. destinations-oauth-intro-end

**To configure OAuth**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-1-start
          :end-before: .. destinations-oauth-configure-step-1-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-2-start
          :end-before: .. destinations-oauth-configure-step-2-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-3-start
          :end-before: .. destinations-oauth-configure-step-3-end


.. _destination-pinterest-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-pinterest-add-destination-steps-start

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

       .. image:: ../../images/mockup-destinations-tab-add-01-select-pinterest.png
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

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-pinterest.png
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
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-oauth-start
          :end-before: .. destinations-intro-for-additional-settings-oauth-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-pinterest.png
          :width: 500 px
          :alt: Settings for Pinterest.
          :align: left
          :class: no-scaled-link

       The **Advertiser account ID** is a 12-character string similar to "567890123456". It is available from the Pinterest management console by any user that is authorized to access the settings for your |destination-name| account.

       The value for **Audience primary key** must be set to "email".


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

.. destination-pinterest-add-destination-steps-end


.. _destination-pinterest-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add a data template**

.. destination-pinterest-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details-pinterest.png
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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-allow-campaigns-start
          :end-before: .. destinations-data-template-business-users-allow-campaigns-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       .. image:: ../../images/mockup-destinations-tab-data-template-settings-pinterest.png
          :width: 500 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

       Add the name of the customer list to the **List name** field. This may be the name of an existing customer list in |destination-name|. If the customer list does not exist, Amperity creates it.


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

.. destination-pinterest-add-data-template-steps-end
