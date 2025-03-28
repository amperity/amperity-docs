.. https://docs.amperity.com/internal/



.. |destination-name| replace:: Criteo
.. |plugin-name| replace:: "Criteo"
.. |credential-type| replace:: "criteo"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "crit"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Criteo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Criteo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Criteo

==================================================
Send audiences to Criteo
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_criteo.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-criteo-start
   :end-before: .. term-criteo-end

.. destination-criteo-api-note-start

.. note:: This destination uses the |ext_criteo_api|.

.. destination-criteo-api-note-end

.. destination-criteo-custom-audiences-and-offline-events-start

Your brand can send custom audiences and offline events to |destination-name|:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Custom audiences
          :align: left
          :class: no-scaled-link
     - **Custom audiences**

       Use :ref:`Custom audiences <destination-criteo-add>` to help find who can be activated using |destination-name|.

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Custom audiences
          :align: left
          :class: no-scaled-link
     - **Transactions data**

       Use :ref:`transactions data <destination-criteo-send-transactions>` to help your brand track offline conversions from your marketing campaigns.

.. destination-criteo-custom-audiences-and-offline-events-end


.. _destination-criteo-send-transactions:

Send transactions data
--------------------------------------------------

.. TODO: Sync this with ampiq/events_criteo and also internal/events_criteo and datagrid/events_criteo

.. events-criteo-overview-start

You can send transactions data (offline events) to |destination-name| as a CSV or TSV file using SFTP.

Review the |ext_criteo_sftp|, and then configure Amperity to connect to |destination-name| using the |destination_sftp| destination.

.. events-criteo-overview-end

.. events-criteo-build-query-start

After the SFTP destination is configured, use a query to map a customer's email address and transactions data to the fields that can be sent to |destination-name|. For example:

.. code-block:: sql

   SELECT
     uit.amperity_id AS user_crmid
     ,mc.email AS user_email
     ,uit.order_id AS event_id
     ,uit.item_quantity AS event_item_quantity
     ,uit.product_id AS event_item_id
     ,uit.currency AS event_currency
     ,uit.item_revenue AS event_item_price
     ,uit.order_datetime AS event_timestamp
     ,uit.store_id AS store_id
     --,uit.purchase_brand AS event_item_brand --optional
     --,uit.product_category AS event_item_category --optional
   FROM Merged_Customers mc
   INNER JOIN Unified_Itemized_Transactions uit
   ON mc.amperity_id = uit.amperity_id
   WHERE mc.email IS NOT NULL
   AND uit.is_return = false
   AND uit.is_cancellation = false

Use an orchestration to send transactions to |destination-name| using the |destination_sftp| destination.

.. events-criteo-build-query-end


.. _destination-criteo-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-criteo-get-details-table-start

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

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

       .. important:: When configuring OAuth for |destination-name| you must |ext_criteo_portfolio| to which access will be granted.

          |destination-name| will only create the credential if the account you are using has not already granted Amperity access. If you need to create a new credential, |ext_criteo_oauth_consent|, and then reconfigure OAuth using the newly-generated link.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Advertiser ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-advertiser-id-start
             :end-before: .. setting-criteo-advertiser-id-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-audience-name-start
             :end-before: .. setting-criteo-audience-name-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

.. destination-criteo-get-details-end


.. _destination-criteo-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

.. destination-criteo-configure-oauth-must-select-portfolios-start

.. important:: When configuring OAuth for |destination-name| you must |ext_criteo_portfolio| to which access will be granted.

   |destination-name| will only create the credential if the account you are using has not already granted Amperity access. If you need to create a new credential, |ext_criteo_oauth_consent|, and then reconfigure OAuth using the newly-generated link.

.. destination-criteo-configure-oauth-must-select-portfolios-end

**To configure credentials for Criteo**

.. destination-criteo-credentials-steps-start

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

.. destination-criteo-credentials-steps-end


.. _destination-criteo-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-criteo-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Criteo**

.. destination-criteo-add-steps-start

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

       **Advertiser ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-advertiser-id-start
             :end-before: .. setting-criteo-advertiser-id-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-audience-name-start
             :end-before: .. setting-criteo-audience-name-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-criteo-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
