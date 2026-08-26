.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Microsoft Advertising
.. |plugin-name| replace:: "Microsoft Ads Conversions API"
.. |credential-type| replace:: "Microsoft Ads Conversions API"
.. |required-credentials| replace:: "API token"
.. |what-send| replace:: conversion events
.. |where-send| replace:: |destination-name|
.. |hashed-fields| replace:: **email** and **phone**

.. meta::
    :description lang=en:
        Configure Amperity to send conversion events to the Microsoft Advertising Conversions API.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send conversion events to the Microsoft Advertising Conversions API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure the Microsoft Ads Conversions API

==================================================
Configure the Microsoft Ads Conversions API
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-ads-conversions-start
   :end-before: .. term-microsoft-ads-conversions-end

.. events-microsoft-ads-conversions-overview-start

Send conversion events to |destination-name| using the Conversions API (CAPI) to attribute conversions that happen away from the browser — in-store purchases, CRM events, phone orders, and other server-side transactions — back to your |destination-name| campaigns, and to build audiences for remarketing. Each row returned by your query is sent as a single custom conversion event, carrying an event name, an event time, and at least one customer identifier.

Amperity hashes **email** and **phone** identifiers with SHA-256 before sending them; raw email and phone values never leave Amperity. Other identifiers — an anonymous ID, external ID, Microsoft click ID (**msclkid**), or mobile advertising ID — are sent as provided. See the `Conversions API (CAPI) guide <https://learn.microsoft.com/en-us/advertising/guides/uet-conversion-api-integration?view=bingads-13>`__ |ext_link| for more information.

.. events-microsoft-ads-conversions-overview-end

.. events-microsoft-ads-conversions-beta-start

.. admonition:: Beta

   The Microsoft Ads Conversions API connector is currently in beta. Contact your Amperity representative to learn more.

.. events-microsoft-ads-conversions-beta-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sha-256-hashed-fields-start
   :end-before: .. setting-common-sha-256-hashed-fields-end


.. _events-microsoft-ads-conversions-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-microsoft-ads-conversions-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-ads-conversions-api-token-start
             :end-before: .. credential-microsoft-ads-conversions-api-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-ads-conversions-api-token-find-start
             :end-before: .. credential-microsoft-ads-conversions-api-token-find-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Microsoft Advertising settings**

       **UET Tag ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-conversions-tag-id-start
             :end-before: .. setting-microsoft-ads-conversions-tag-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Request properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-conversions-query-must-return-start
             :end-before: .. setting-microsoft-ads-conversions-query-must-return-end

          See :ref:`events-microsoft-ads-conversions-parameters` for the full list of columns your query may return.

.. events-microsoft-ads-conversions-get-details-table-end


.. _events-microsoft-ads-conversions-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for the Microsoft Ads Conversions API**

.. events-microsoft-ads-conversions-credentials-steps-start

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
     - In the **Credentials settings** dialog box, do the following:

       From the **Plugin** dropdown, select **Microsoft Ads Conversions API**.

       .. note:: Amperity provides three Microsoft Advertising connectors. Select **Microsoft Ads Conversions API** to send conversion events through Microsoft Advertising's Conversions API. **Microsoft Ads Offline Events** sends offline conversions through the older offline-conversions API, and **Microsoft Ads** sends customer profiles for audience targeting.

       Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-ads-conversions-api-token-start
             :end-before: .. credential-microsoft-ads-conversions-api-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-ads-conversions-api-token-find-start
             :end-before: .. credential-microsoft-ads-conversions-api-token-find-end

.. events-microsoft-ads-conversions-credentials-steps-end


.. _events-microsoft-ads-conversions-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-microsoft-ads-conversions-add-destination-start

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

       Enter the name of the destination and a description. For example: "|destination-name| conversion events" and "Send conversion events to |destination-name|.".

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

       **UET Tag ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-conversions-tag-id-start
             :end-before: .. setting-microsoft-ads-conversions-tag-id-end

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

.. events-microsoft-ads-conversions-add-destination-end


.. _events-microsoft-ads-conversions-build-query:

Build a query
==================================================

.. events-microsoft-ads-conversions-build-query-start

Use a query to build a combination of data — typically from the **Unified Transactions** and **Customer 360** tables — that returns one row per conversion event to send to |destination-name|. Each row must include an event name and an event time, plus at least one customer identifier — an email address, phone number, Microsoft click ID, anonymous ID, external ID, or mobile advertising ID. Adding more identifiers can improve the match rate. You can also include a conversion value and currency, and a transaction ID, which Amperity sends with each event.

.. events-microsoft-ads-conversions-build-query-end

.. events-microsoft-ads-conversions-build-query-required-start

Review the :ref:`events-microsoft-ads-conversions-parameters` section for the columns your query must and may return.

.. note:: |destination-name| deduplicates events by **event_id**. If your query does not return **event_id**, Amperity generates a stable one from the event's name, time, transaction ID, and first identifier, so that retries of the same event do not create duplicate conversions.

.. note:: For an event to be attributed to a conversion goal, its **event_name** must match the event action of a custom conversion goal configured in |destination-name|. Events are still accepted — and can contribute to audiences and measurement — when no matching goal exists, so confirm your goal setup in |destination-name| if accepted events are not appearing as conversions.

.. events-microsoft-ads-conversions-build-query-required-end

Bound the query to recent conversions — |destination-name| accepts events with an **event_time** within the last **7 days** — so each orchestration sends new events instead of re-sending history. A query that returns a collection of recent purchase events for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     'purchase' AS event_name
     ,ut.order_datetime AS event_time
     ,ut.order_id AS transaction_id
     ,c360.email AS email
     ,c360.phone AS phone
     ,ut.order_revenue AS value
     ,ut.currency AS currency
   FROM Unified_Transactions ut
   LEFT JOIN Customer_360 c360 ON ut.amperity_id = c360.amperity_id
   WHERE ut.order_datetime > (CURRENT_DATE - interval '7' day)
   AND (c360.email IS NOT NULL OR c360.phone IS NOT NULL)


.. _events-microsoft-ads-conversions-data-validation:

Data validation
==================================================

.. events-microsoft-ads-conversions-data-validation-start

Amperity validates each row before sending and drops rows that |destination-name| would reject, so that one invalid row does not cause an entire batch of events to be rejected. Dropped rows are reported as failed with the reason. A row is dropped when:

* **event_name** or **event_time** is missing.
* **event_time** cannot be parsed as UNIX epoch seconds or an |ext_iso_8601| instant, is more than 7 days in the past, or is in the future.
* the row has no identifier — **anonymous_id**, **external_id**, **email**, **phone**, **msclkid**, **idfa**, and **gaid** are all empty.
* every identifier the row provides is unusable — for example, the only identifier is an email address that cannot be validated — leaving no identifier after normalization.

An individual identifier that cannot be used — an **email** without an ``@``, or a **phone** number that cannot be normalized — is dropped from that row; the rest of the event is still sent when another identifier remains. A non-numeric **value** (and its **currency**) is omitted the same way, and an **ad_storage_consent** value other than ``G`` or ``D`` is omitted.

.. events-microsoft-ads-conversions-data-validation-end


.. _events-microsoft-ads-conversions-parameters:

Conversion event fields
==================================================

.. events-microsoft-ads-conversions-parameters-start

The following table describes each column Amperity sends to |destination-name|. A query must return columns with the same name as listed in the "Amperity name" column; Amperity maps them to the |destination-name| Conversions API field names automatically.

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-microsoft-ads-conversions-query-must-return-start
      :end-before: .. setting-microsoft-ads-conversions-query-must-return-end

.. list-table::
   :widths: 22 24 54
   :header-rows: 1

   * - Amperity name
     - Microsoft Advertising field
     - Description

   * - **event_name**
     - **eventName**
     - **Required**

       A name for the conversion event. To deduplicate an event that is also sent by Universal Event Tracking (UET), use the same event name in both systems.

   * - **event_time**
     - **eventTime**
     - **Required**

       When the event occurred, as UNIX epoch seconds (for example, ``1710438591``) or a full |ext_iso_8601| instant (for example, ``2026-07-10T12:00:00Z``). Must be within the last 7 days; values older than 7 days or in the future are dropped.

   * - **event_id**
     - **eventId**
     - **Optional**

       A unique identifier for the event, used to deduplicate an event sent by both UET and the Conversions API. If omitted, Amperity generates a stable value so retries do not create duplicate conversions.

   * - **anonymous_id**
     - **userData.anonymousId**
     - **Optional**

       A guest (non-authenticated) visitor ID, sent as provided. At least one identifier — **anonymous_id**, **external_id**, **email**, **phone**, **msclkid**, **idfa**, or **gaid** — is required per row.

   * - **external_id**
     - **userData.externalId**
     - **Optional**

       An authenticated user ID, sent as provided.

   * - **email**
     - **userData.em**
     - **Optional**

       An email address. Amperity normalizes and SHA-256 hashes the value following Microsoft's hashing rules before sending.

   * - **phone**
     - **userData.ph**
     - **Optional**

       A phone number. Amperity normalizes the number to E.164 format using the US region and applies SHA-256 hashing before sending.

   * - **msclkid**
     - **userData.msclkid**
     - **Optional**

       The Microsoft click ID captured from the ad click.

   * - **idfa**
     - **userData.idfa**
     - **Optional**

       An Apple mobile advertising ID (Identifier for Advertisers), sent as provided.

   * - **gaid**
     - **userData.gaid**
     - **Optional**

       A Google (Android) advertising ID, sent as provided.

   * - **client_user_agent**
     - **userData.clientUserAgent**
     - **Optional**

       The user agent of the customer's browser, sent as provided.

   * - **client_ip_address**
     - **userData.clientIpAddress**
     - **Optional**

       The IP address of the customer, sent as provided.

   * - **ad_storage_consent**
     - **adStorageConsent**
     - **Optional**

       The customer's advertising-storage consent. Must be ``G`` (granted) or ``D`` (denied); any other value is omitted. An event with no value defaults to granted.

   * - **transaction_id**
     - **customData.transactionId**
     - **Optional**

       Your identifier for the transaction, sent as provided.

   * - **value**
     - **customData.value**
     - **Optional**

       A numeric conversion value for the event.

   * - **currency**
     - **customData.currency**
     - **Optional**

       The currency for **value**. Sent only when **value** is also present.

.. events-microsoft-ads-conversions-parameters-end

.. events-microsoft-ads-conversions-consent-note-start

.. note:: **ad_storage_consent** controls how |destination-name| may use an event. Send ``G`` (granted) or ``D`` (denied) per row; an event with no value is processed as granted. If you send |destination-name| conversion data for customers in the EEA, the UK, or Switzerland, populate **ad_storage_consent** from your own consent records for those rows rather than relying on the default.

.. events-microsoft-ads-conversions-consent-note-end


.. _events-microsoft-ads-conversions-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-microsoft-ads-conversions-workflow-actions-start

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

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`events-microsoft-ads-conversions-workflow-actions-invalid-credentials`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. events-microsoft-ads-conversions-workflow-actions-end

.. note:: If |destination-name| rejects an event, the workflow reports Microsoft's field-level validation message (up to 10 per batch) — review the values returned by your query. A batch is rejected in full only when every event in it is invalid; otherwise the valid events are still sent. If sends are rate limited, Amperity retries automatically.


.. _events-microsoft-ads-conversions-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end

.. note:: A 401 response from |destination-name| means the API token is missing, expired, or not authorized for the configured **UET Tag ID**. Obtain a new token from the Microsoft Advertising UI for the correct tag, and then update the credential in Amperity.
