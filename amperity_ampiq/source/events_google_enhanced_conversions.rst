.. https://docs.amperity.com/ampiq/


.. |destination-name| replace:: Google Enhanced Conversions
.. |what-send| replace:: first-party customer data that is associated with transactions
.. |what-enablex| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires first-party data that is associated with transactions.
.. |where-send| replace:: |destination-name|
.. |required-credentials| replace:: "Customer ID"
.. |credential-type| replace:: "google-ads"
.. |filter-the-list| replace:: "google"
.. |plugin-name| replace:: "Google Enhanced Conversions"


.. meta::
    :description lang=en:
        Configure Amperity to send offline events to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send offline events to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send offline events to Google Enhanced Conversions

==================================================
Send offline events to Google Enhanced Conversions
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-enhanced-conversions-start
   :end-before: .. term-google-enhanced-conversions-end

.. include:: ../../amperity_operator/source/events_google_enhanced_conversions.rst
   :start-after: .. destination-google-enhanced-conversions-about-start
   :end-before: .. destination-google-enhanced-conversions-about-end


.. _destination-google-enhanced-conversions-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-google-enhanced-conversions-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Configure Google Ads**

       Enable enhanced conversions for leads in Google Ads:

       #. `Enable conversion tracking in Google Ads <https://developers.google.com/google-ads/api/docs/conversions/enhanced-conversions/leads-setup>`__ |ext_link|.
       #. Accept customer data terms and opt-in to enhanced conversions for leads.
       #. Set up tagging through Google Tag Manager.
       #. Create at least one ConversionAction.

          The conversion_action_type must be set to **UPLOAD_CLICKS**.

       #. `Configure Google tag settings <https://support.google.com/google-ads/answer/11021502#configure>`__ |ext_link| to enable enhanced conversions for leads.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for "Google Enhanced Conversions" *must* be completed within Google prior to configuring Amperity to send ads to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Customer ID**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-customer-id-end

.. destination-google-enhanced-conversions-get-details-table-end


.. _destination-google-enhanced-conversions-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure OAuth**

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

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-google-enhanced-conversions-credentials-steps-end


.. _destination-google-enhanced-conversions-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Enhanced Conversions**

.. destination-google-enhanced-conversions-add-steps-start

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

       **Conversion action name** (Required at orchestration)
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-action-name-start
             :end-before: .. setting-google-enhanced-conversions-action-name-end

       **Customer ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-customer-id-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end

.. destination-google-enhanced-conversions-add-steps-end


.. _events-google-enhanced-conversions-build-query:

Build a query
==================================================

.. events-google-enhanced-conversions-build-query-start

After the destination is configured, use a query to collect first-party data that is associated with transactions. Use SHA-256 hashing for all customer profile fields that are returned by the query.

For example:

.. code-block:: sql

   SELECT
     SHA256(c.email) AS Email,
     SHA256(c.phone) AS Phone,
     SHA256(c.given_name) AS FirstName,
     SHA256(c.surname) AS LastName
   FROM Customer_360 c
   JOIN Unified_Transactions t ON c.amperity_id = t.amperity_id
   WHERE t.order_datetime >= DATE_ADD('day', -30, CURRENT_DATE)

.. events-google-enhanced-conversions-build-query-end
