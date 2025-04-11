.. https://docs.amperity.com/operator/



.. |destination-name| replace:: Snapchat
.. |plugin-name| replace:: "Snapchat"
.. |credential-type| replace:: "snapchat"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email addresses, mobile advertiser IDs, or phone numbers
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "snap"


.. meta::
    :description lang=en:
        Configure Amperity to send audience lists to Snapchat.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audience lists to Snapchat.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audience lists to Snapchat

==================================================
Send audience lists to Snapchat
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_snapchat.html>`__ |ext_link|.

.. destination-snapchat-about-start

Send email addresses, mobile advertiser IDs, or phone numbers to |destination-name|, and then manage ads and advertising campaign.

.. destination-snapchat-about-end

.. destination-snapchat-api-note-start

.. note:: This destination uses the `Snap Audience Match <https://marketingapi.snapchat.com/docs/?lang=en-US#snap-audience-match>`__ |ext_link| component within the `Snapchat Marketing API <https://marketingapi.snapchat.com/docs/>`__ |ext_link| to `add users <https://marketingapi.snapchat.com/docs/?lang=en-US#adding-users>`__ |ext_link| as a list of email addresses, mobile advertiser IDs, or phone numbers.

.. destination-snapchat-api-note-end

.. _destination-snapchat-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-snapchat-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
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
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Ad account ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snapchat-ad-account-id-start
             :end-before: .. setting-snapchat-ad-account-id-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - The name of the custom audience to which Amperity will send data. Amperity will create the custom audience name if it does not already exist.

       .. tip:: The custom audience name is visible from the **Snapchat Audiences** page. This name should be clear and understandable to users of Snapchat. An audience with this will be created if it does not exist.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: left
          :class: no-scaled-link
     - :ref:`Authorize Amperity to send data to the customer's Snapchat account <destination-snapchat-credentials>`. This requires activation in the Amperity |destination-name| account and approval in the customer's |destination-name| account.

.. destination-snapchat-get-details-end


.. _destination-snapchat-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Snapchat**

.. destination-snapchat-credentials-steps-start

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

       **Refresh token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-snapchat-credentials-steps-end


.. _destination-snapchat-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-snapchat-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Snapchat**

.. destination-snapchat-add-steps-start

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

       **Ad account ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snapchat-ad-account-id-start
             :end-before: .. setting-snapchat-ad-account-id-end

       **Segment name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-snapchat-segment-name-start
             :end-before: .. setting-snapchat-segment-name-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-snapchat-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
