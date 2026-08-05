.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Amazon Ads
.. |plugin-name| replace:: "Amazon CAPI"
.. |credential-type| replace:: "amazon-capi"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: conversion events
.. |where-send| replace:: |destination-name|
.. |hashed-fields| replace:: **email** and **phone**

.. meta::
    :description lang=en:
        Configure Amperity to send conversion events to Amazon Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send conversion events to Amazon Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for Amazon Ads

==================================================
Configure events for Amazon Ads
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-capi-start
   :end-before: .. term-amazon-capi-end

.. events-amazon-capi-overview-start

Send conversion events to |destination-name| using the Amazon Ads Conversion API (CAPI) to measure return on ad spend (ROAS), attribute offline conversions to Amazon DSP campaigns, and enrich audiences with first-party data. Each row returned by your query is sent as a single conversion event carrying a conversion type, an event source, an event timestamp, a country code, and one or more customer identifiers.

Amperity hashes **email** and **phone** identifiers with SHA-256 before sending them; raw email and phone values never leave Amperity. A mobile advertising ID (**maid**) and an Amperity match ID (**match_id**) are sent as-is. See the `Amazon Ads Events API documentation <https://advertising.amazon.com/API/docs/en-us/guides/events/events>`__ |ext_link| for more information.

.. events-amazon-capi-overview-end

.. events-amazon-capi-beta-start

.. admonition:: Beta

   The Amazon CAPI connector is currently in beta. Contact your Amperity representative to learn more.

.. events-amazon-capi-beta-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sha-256-hashed-fields-start
   :end-before: .. setting-common-sha-256-hashed-fields-end


.. _events-amazon-capi-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-amazon-capi-get-details-table-start

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
             :start-after: .. credential-amazon-capi-refresh-token-start
             :end-before: .. credential-amazon-capi-refresh-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-capi-refresh-token-find-start
             :end-before: .. credential-amazon-capi-refresh-token-find-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Amazon Ads settings**

       **DSP Advertiser ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-capi-dsp-advertiser-id-start
             :end-before: .. setting-amazon-capi-dsp-advertiser-id-end

          .. important:: The DSP Advertiser ID must be linked to a manager account in each Amazon Ads region you send events to. Events for a region where the advertiser is not linked are not sent.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Request properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-capi-query-must-return-start
             :end-before: .. setting-amazon-capi-query-must-return-end

          See :ref:`events-amazon-capi-parameters` for the full list, and :ref:`events-amazon-capi-event-types` for the allowed **conversion_type** and **event_source** values.

.. events-amazon-capi-get-details-table-end


.. _events-amazon-capi-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Amazon CAPI**

.. events-amazon-capi-credentials-steps-start

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

       From the **Plugin** dropdown, select **Amazon CAPI**.

       .. note:: Amperity provides two Amazon connectors. Select **Amazon CAPI** to send conversion events to the Amazon Ads Conversion API. **Amazon Ads** is a separate connector that sends first-party audiences to Amazon DSP.

       Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-capi-refresh-token-start
             :end-before: .. credential-amazon-capi-refresh-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amazon-capi-refresh-token-find-start
             :end-before: .. credential-amazon-capi-refresh-token-find-end

.. events-amazon-capi-credentials-steps-end


.. _events-amazon-capi-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-amazon-capi-add-destination-start

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

       Enter the name of the destination and a description. For example: "|destination-name| events" and "Send conversion events to |destination-name|.".

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

       **DSP Advertiser ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-capi-dsp-advertiser-id-start
             :end-before: .. setting-amazon-capi-dsp-advertiser-id-end

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

.. events-amazon-capi-add-destination-end


.. _events-amazon-capi-build-query:

Build a query
==================================================

.. events-amazon-capi-build-query-start

Use a query to build a combination of data — typically from the **Unified Transactions** and **Customer 360** tables — that returns one row per conversion event to send to |destination-name|. Each row must include a conversion type, an event source, an event timestamp, a country code, and at least one customer identifier (email, phone, mobile advertising ID, or match ID). Adding more identifiers can improve the match rate, and you can include event attributes such as conversion value, currency, and units sold, which Amperity sends with each event.

.. events-amazon-capi-build-query-end

.. events-amazon-capi-build-query-required-start

Review the :ref:`events-amazon-capi-parameters` section for the columns your query must and may return, and the :ref:`events-amazon-capi-event-types` section for the allowed **conversion_type** and **event_source** values.

.. events-amazon-capi-build-query-required-end

Amazon accepts conversion events only from the **past 21 days**, so bound the query to a recent window that matches how often the orchestration runs; this also avoids re-sending the full transaction history. A query that returns a collection of recent purchase events for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     'Purchase' AS event_name
     ,'OFF_AMAZON_PURCHASES' AS conversion_type
     ,'OFFLINE' AS event_source
     ,ut.order_datetime AS event_time
     ,c360.country AS country_code
     ,c360.email AS email
     ,c360.phone AS phone
     ,ut.order_revenue AS value
     ,ut.currency AS currency_code
     ,ut.order_id AS event_id
   FROM Unified_Transactions ut
   LEFT JOIN Customer_360 c360 ON ut.amperity_id = c360.amperity_id
   WHERE ut.order_datetime > (CURRENT_DATE - interval '21' day)
   AND c360.email IS NOT NULL


.. _events-amazon-capi-event-types:

Supported conversion types and event sources
==================================================

.. events-amazon-capi-event-types-start

**conversion_type** and **event_source** are required and must exactly match one of the values below. The values are **case-sensitive** and uppercase, so ``purchase`` or ``Offline`` are rejected. Rows with a missing or unrecognized **conversion_type** or **event_source** are not sent and are reported as failed.

**Supported conversion_type values (12)**

ADD_TO_SHOPPING_CART, APPLICATION, CHECKOUT, CONTACT, LEAD, MOBILE_APP_FIRST_START, OFF_AMAZON_PURCHASES, PAGE_VIEW, SEARCH, SIGN_UP, SUBSCRIBE, OTHER

**Supported event_source values (6)**

ANDROID, FIRE_TV, IOS, OFFLINE, WEBSITE, MEASUREMENT_PARTNER

.. events-amazon-capi-event-types-end


.. _events-amazon-capi-regions:

Regional routing and consent
==================================================

.. events-amazon-capi-regions-start

Amazon Ads serves the Conversion API from three regional hosts. Amperity routes each event to the correct host based on its **country_code**, so a single query can include events for customers in different regions.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Region
     - Country codes

   * - North America
     - BR, CA, MX, US

   * - Europe
     - AE, BE, DE, EG, ES, FR, GB, IN, IT, NL, PL, SA, SE, TR, ZA

   * - Far East
     - AU, JP, SG

Provide **country_code** as an |ext_iso_31661alpha2| code (for example, ``US`` or ``GB`` — use ``GB`` for Great Britain, because ``UK`` is not a valid code). Amperity trims and uppercases the value before matching. An unrecognized or missing **country_code** defaults to North America.

**DSP advertiser must be linked per region.** A DSP Advertiser ID is valid only in the Amazon Ads region(s) it is provisioned in. Before sending a region's events, Amperity confirms the configured **DSP Advertiser ID** is linked to a manager account in that region. If it is not, that region's events are not sent — they are reported as failed with an explanatory message — while events for the other regions are still delivered. Confirm in Amazon Ads that the DSP Advertiser ID is linked to a manager account in every region you send events to.

**European consent default.** Amazon requires consent information on every event routed to the Europe host. When a Europe-routed event does not include **amzn_ad_storage** or **amzn_user_data**, Amperity sets both to **DENIED** so the event is accepted. Events routed to North America and Far East receive no default — consent is sent only when your query provides **consent_tcf**, **amzn_ad_storage**, or **amzn_user_data**.

.. note:: The European consent default applies to every country in Amazon's Europe routing group above, not only to countries in the European Union. To send an explicit consent signal, populate **amzn_ad_storage** and **amzn_user_data** (each ``GRANTED`` or ``DENIED``), or **consent_tcf** with an IAB TCF string.

.. events-amazon-capi-regions-end


.. _events-amazon-capi-data-validation:

Data validation
==================================================

.. events-amazon-capi-data-validation-start

Amperity validates each row before sending and drops rows that Amazon Ads would reject, so that one invalid row does not cause an entire batch of events to be rejected. Dropped rows are reported as failed with the reason. A row is dropped when:

* **event_name**, **conversion_type**, **event_source**, **event_time**, or **country_code** is missing.
* **conversion_type** or **event_source** is not one of the supported values (see :ref:`events-amazon-capi-event-types`).
* **event_time** cannot be parsed as an |ext_iso_8601| instant (for example, ``2026-03-15T14:30:00Z``).
* the row has no identifier — **email**, **phone**, **maid**, and **match_id** are all empty.

An optional value that cannot be used is dropped from that row individually, and the rest of the event is still sent. For example, an **email** that is not a valid email address is dropped (and reported) and the event is sent using its other identifiers; a non-numeric **value** is omitted.

.. events-amazon-capi-data-validation-end


.. _events-amazon-capi-parameters:

Conversion API parameters
==================================================

.. events-amazon-capi-parameters-start

The following table describes each column Amperity sends to |destination-name|. A query must return columns with the same name as listed in the "Amperity name" column; Amperity maps them to the Amazon Conversion API field names automatically.

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-amazon-capi-query-must-return-start
      :end-before: .. setting-amazon-capi-query-must-return-end

.. list-table::
   :widths: 22 20 58
   :header-rows: 1

   * - Amperity name
     - Amazon field
     - Description

   * - **event_name**
     - **name**
     - **Required**

       A name for the conversion event.

   * - **conversion_type**
     - **conversionType**
     - **Required**

       The type of conversion. Must be one of the 12 supported values (see :ref:`events-amazon-capi-event-types`).

   * - **event_source**
     - **eventSource**
     - **Required**

       Where the event originated. Must be one of the 6 supported values (see :ref:`events-amazon-capi-event-types`).

   * - **event_time**
     - **eventTime**
     - **Required**

       When the event occurred, as a full |ext_iso_8601| instant with a UTC offset (for example, ``2026-03-15T14:30:00Z``). Date-only or space-separated values are rejected. Amazon accepts only events from the past 21 days.

   * - **country_code**
     - **countryCode**
     - **Required**

       The customer's |ext_iso_31661alpha2| country code. Determines which Amazon Ads region receives the event (see :ref:`events-amazon-capi-regions`). Amperity trims and uppercases the value; an unrecognized or missing value routes to North America.

   * - **email**
     - **matchKeys** (EMAIL)
     - **Optional**

       An email address. Amperity applies SHA-256 hashing before sending. At least one of **email**, **phone**, **maid**, or **match_id** is required per row.

   * - **phone**
     - **matchKeys** (PHONE)
     - **Optional**

       A phone number. Amperity normalizes the number and applies SHA-256 hashing before sending.

   * - **maid**
     - **matchKeys** (MAID)
     - **Optional**

       A mobile advertising ID, sent as-is (not hashed).

   * - **match_id**
     - **matchKeys** (MATCH_ID)
     - **Optional**

       An Amperity-generated match identifier, sent as-is (not hashed).

   * - **value**
     - **value**
     - **Optional**

       A numeric conversion value for the event, rounded to two decimal places.

   * - **currency_code**
     - **currencyCode**
     - **Optional**

       The currency for **value**. Sent only when **value** is also provided.

   * - **units_sold**
     - **unitsSold**
     - **Optional**

       The number of units sold, as an integer from 1 to 9,999,999,999,999. Sent only when **conversion_type** is ``OFF_AMAZON_PURCHASES``.

   * - **event_id**
     - **eventId**
     - **Optional**

       A unique identifier for the event, passed through as-is. Amazon uses it to deduplicate events across ingestion sources (for example, the Amazon Ads Tag and CAPI). Provide a stable value, such as an order ID, so that events sent through more than one source are not double-counted.

   * - **dataset_name**
     - **dataSetName**
     - **Optional**

       The name of the Amazon dataset the event belongs to.

   * - **consent_tcf**
     - **consent.tcf**
     - **Optional**

       An IAB Transparency and Consent Framework (TCF) consent string.

   * - **amzn_ad_storage**
     - **consent.amazonConsent.amznAdStorage**
     - **Optional**

       A consent signal for advertising storage. Must be ``GRANTED`` or ``DENIED``; other values are treated as absent. See :ref:`events-amazon-capi-regions` for the European default.

   * - **amzn_user_data**
     - **consent.amazonConsent.amznUserData**
     - **Optional**

       A consent signal for user-data processing. Must be ``GRANTED`` or ``DENIED``; other values are treated as absent. See :ref:`events-amazon-capi-regions` for the European default.

   * - **limited_data_use**
     - **dataProcessingOptions**
     - **Optional**

       Set to ``true`` to apply Amazon's ``LIMITED_DATA_USE`` data-processing option to the event.

.. events-amazon-capi-parameters-end


.. _events-amazon-capi-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-amazon-capi-workflow-actions-start

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

       * :ref:`events-amazon-capi-workflow-actions-invalid-credentials`

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

.. events-amazon-capi-workflow-actions-end

.. note:: If Amazon Ads rejects an entire batch of events, the workflow reports Amazon's per-event error messages (up to 10 per batch) — review the field values returned by your query. Events older than 21 days are rejected by Amazon; filter your query to recent events. If the configured **DSP Advertiser ID** is not linked to a manager account in a region, that region's events are reported as failed and skipped while the other regions are still delivered. If sends are rate limited, Amperity retries automatically; reduce the volume of events sent per orchestration if the limit persists.


.. _events-amazon-capi-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end

.. note:: A 401 or 403 response from Amazon Ads means the refresh token is expired, was revoked, or does not have permission to submit conversion events. Re-complete the Amazon Ads authorization flow to obtain a new refresh token, and then update the credential in Amperity. Refresh tokens issued after June 30, 2026 expire 365 days after the advertiser grants consent.
