.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Roku
.. |plugin-name| replace:: "Roku CAPI"
.. |credential-type| replace:: "roku-capi"
.. |required-credentials| replace:: "CAPI token"
.. |what-send| replace:: conversion events
.. |where-send| replace:: |destination-name|
.. |hashed-fields| replace:: **email**, **phone**, **given_name**, **surname**, **gender**, and **birthdate**

.. meta::
    :description lang=en:
        Configure Amperity to send conversion events to Roku.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send conversion events to Roku.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for Roku

==================================================
Configure events for Roku
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-roku-capi-start
   :end-before: .. term-roku-capi-end

.. events-roku-capi-overview-start

Send conversion events to |destination-name| using the Roku Conversions API (CAPI) to power campaign optimization, event-based custom audiences, and conversion attribution (ROAS). Each row returned by your query is sent as a single conversion event carrying a Roku event type, an event timestamp, and one or more hashed customer identifiers.

Amperity hashes customer identifiers with SHA-256 before sending them; raw identifier values never leave Amperity. See the `Roku Conversions API reference <https://help.ads.roku.com/en/articles/8880744-conversions-api>`__ |ext_link| for more information.

.. events-roku-capi-overview-end

.. events-roku-capi-beta-start

.. admonition:: Beta

   The Roku CAPI connector is currently in beta. Contact your Amperity representative to learn more.

.. events-roku-capi-beta-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sha-256-hashed-fields-start
   :end-before: .. setting-common-sha-256-hashed-fields-end


.. _events-roku-capi-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-roku-capi-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **CAPI token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-roku-capi-capi-token-start
             :end-before: .. credential-roku-capi-capi-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-roku-capi-capi-token-find-start
             :end-before: .. credential-roku-capi-capi-token-find-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Roku settings**

       **Event group ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-capi-event-group-id-start
             :end-before: .. setting-roku-capi-event-group-id-end

          .. important:: The CAPI token must belong to the same Roku Ads account as the event group. A token from a different account authenticates but is not authorized for the event group.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Request properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-capi-query-must-return-start
             :end-before: .. setting-roku-capi-query-must-return-end

          See :ref:`events-roku-capi-parameters` for the full list, and :ref:`events-roku-capi-event-types` for the allowed **event_name** and **event_source** values.

.. events-roku-capi-get-details-table-end


.. _events-roku-capi-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Roku CAPI**

.. events-roku-capi-credentials-steps-start

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

       From the **Plugin** dropdown, select **Roku CAPI**.

       .. note:: Amperity provides two Roku connectors. Select **Roku CAPI** to send conversion events to the Roku Conversions API. **Roku Audience** is a separate connector that sends first-party audiences for household targeting.

       Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **CAPI token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-roku-capi-capi-token-start
             :end-before: .. credential-roku-capi-capi-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-roku-capi-capi-token-find-start
             :end-before: .. credential-roku-capi-capi-token-find-end

.. events-roku-capi-credentials-steps-end


.. _events-roku-capi-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-roku-capi-add-destination-start

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

       **Event group ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-capi-event-group-id-start
             :end-before: .. setting-roku-capi-event-group-id-end

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

.. events-roku-capi-add-destination-end


.. _events-roku-capi-build-query:

Build a query
==================================================

.. events-roku-capi-build-query-start

Use a query to build a combination of data — typically from the **Unified Transactions** and **Customer 360** tables — that returns one row per conversion event to send to |destination-name|. Each row must include an event type, an event source, an event timestamp, and a customer email. Adding a phone number can improve the match rate; you can also include additional identifiers — name, gender, and birthdate — and event attributes such as conversion value, currency, and order ID, which Amperity sends with each event.

.. events-roku-capi-build-query-end

.. events-roku-capi-build-query-required-start

Review the :ref:`events-roku-capi-parameters` section for the columns your query must and may return, and the :ref:`events-roku-capi-event-types` section for the allowed **event_name** and **event_source** values.

.. events-roku-capi-build-query-required-end

Bound the query to recent events so each orchestration sends new conversions instead of re-sending the full transaction history; choose a window that matches how often the orchestration runs. A query that returns a collection of recent purchase events for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     'PURCHASE' AS event_name
     ,'website' AS event_source
     ,ut.order_datetime AS event_time
     ,c360.email AS email
     ,c360.phone AS phone
     ,c360.country AS country
     ,c360.given_name AS given_name
     ,c360.surname AS surname
     ,ut.order_id AS event_id
     ,ut.order_revenue AS value
     ,ut.currency AS currency
     ,ut.order_id AS order_id
   FROM Unified_Transactions ut
   LEFT JOIN Customer_360 c360 ON ut.amperity_id = c360.amperity_id
   WHERE ut.order_datetime > (CURRENT_DATE - interval '7' day)
   AND c360.email IS NOT NULL


.. _events-roku-capi-event-types:

Supported event types and sources
==================================================

.. events-roku-capi-event-types-start

**event_name** and **event_source** are required and must exactly match one of the values below. The values are **case-sensitive**: **event_name** values are uppercase and **event_source** values are lowercase, so ``Purchase`` or ``Website`` are rejected. Rows with a missing or unrecognized **event_name** or **event_source** are not sent and are reported as failed.

**Supported event_name values (27)**

ACHIEVE_LEVEL, ADD_PAYMENT_INFO, ADD_TO_CART, ADD_TO_WISHLIST, APP_INSTALL, COMPLETE_REGISTRATION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, DOWNLOAD, FIND_LOCATION, FIRST_VIDEO_VIEW, INITIATE_CHECKOUT, LEAD, PAGE_VIEW, PURCHASE, QSS, SCHEDULE, SEARCH, SESSION_START, SIGN_UP, START_TRIAL, SUBSCRIBE, SUBSCRIPTION_CANCELLATION, SUBSCRIPTION_RENEWAL, UNLOCK_ACHIEVEMENT, VIEW_CONTENT

**Supported event_source values (10)**

chat, ctv_app, email, mobile_app, phone_call, physical_store, roku, system-generated, website, other

.. events-roku-capi-event-types-end


.. _events-roku-capi-data-validation:

Data validation
==================================================

.. events-roku-capi-data-validation-start

Amperity validates each row before sending and drops rows that Roku would reject, so that one invalid row does not cause an entire batch of events to be rejected. Dropped rows are reported as failed with the reason. A row is dropped when:

* **event_name**, **event_source**, or **event_time** is missing or unrecognized.
* **email** is missing or is not a valid email address (email is the required identifier).
* **event_time** is more than one hour in the future — usually a sign of a wrong column mapping or a milliseconds-versus-seconds mismatch.

Optional fields that cannot be used — for example, an unparseable birthdate, a non-US national-format phone number sent without a **country**, or a non-numeric **value** — are dropped from that row individually and reported; the rest of the event is still sent.

.. events-roku-capi-data-validation-end


.. _events-roku-capi-parameters:

Conversions API parameters
==================================================

.. events-roku-capi-parameters-start

The following table describes each column Amperity sends to |destination-name|. A query must return columns with the same name as listed in the "Amperity name" column; Amperity maps them to the Roku parameter names automatically.

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-roku-capi-query-must-return-start
      :end-before: .. setting-roku-capi-query-must-return-end

.. list-table::
   :widths: 22 20 58
   :header-rows: 1

   * - Amperity name
     - Roku parameter
     - Description

   * - **event_name**
     - **event_name**
     - **Required**

       The type of conversion event. Must be one of the 27 supported values (see :ref:`events-roku-capi-event-types`).

   * - **event_source**
     - **event_source**
     - **Required**

       Where the event originated. Must be one of the 10 supported values (see :ref:`events-roku-capi-event-types`).

   * - **event_time**
     - **event_time**
     - **Required**

       When the event occurred. Accepts a UNIX epoch-seconds value, a date- or time-typed column, or a string in full |ext_iso_8601| instant form with a UTC offset (for example, ``2026-07-10T12:00:00Z``). A date-only string such as ``2026-07-10``, or a space-separated timestamp such as ``2026-07-10 12:00:00``, is not accepted as a string — send those from a date- or time-typed column instead. Timestamps more than one hour in the future are rejected.

   * - **email**
     - **em**
     - **Required**

       An email address.

       .. note:: **em** is part of the **user_data** object. Amperity strips plus-addressing (john+promo@example.com is treated as john@example.com) and applies SHA-256 hashing before sending.

   * - **phone**
     - **ph**
     - **Optional**

       A phone number. Amperity normalizes the number to E.164 format (including the leading **+**) and applies SHA-256 hashing before sending.

       .. note:: For national-format numbers, include a **country** column so Amperity can parse them; without it, non-US national-format numbers are dropped. Numbers already in E.164 format parse without a country.

   * - **country**
     - Not sent
     - **Optional**

       A country used only to normalize national-format phone numbers. It is **not sent** to |destination-name|. Parsing defaults to US when **country** is absent.

   * - **given_name**
     - **fn**
     - **Optional**

       A first name. Amperity applies SHA-256 hashing before sending.

   * - **surname**
     - **ln**
     - **Optional**

       A last name. Amperity applies SHA-256 hashing before sending.

   * - **gender**
     - **ge**
     - **Optional**

       A gender identifier. Amperity maps values to **male**, **female**, or **unknown** (unrecognized values become **unknown**) and applies SHA-256 hashing before sending.

   * - **birthdate**
     - **db**
     - **Optional**

       A birthdate. Amperity normalizes it to **yyyy-mm-dd** and applies SHA-256 hashing before sending. Values that cannot be parsed as a date are dropped from the row.

   * - **event_id**
     - **event_id**
     - **Optional**

       A unique identifier for the event, passed through as-is. Roku uses it to deduplicate events. Provide a stable value (for example, an order ID) so that repeated sends of the same event are not double-counted.

   * - **value**
     - **value**
     - **Optional**

       A numeric conversion value for the event. Part of the **custom_data** object.

   * - **currency**
     - **currency**
     - **Optional**

       The currency for **value**, as a three-character |ext_iso_4217| code. Part of the **custom_data** object.

   * - **order_id**
     - **order_id**
     - **Optional**

       The order identifier associated with the event. Part of the **custom_data** object.

   * - **purchase_type**
     - **purchase_type**
     - **Optional**

       A purchase type for the event. Part of the **custom_data** object.

.. events-roku-capi-parameters-end


.. _events-roku-capi-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-roku-capi-workflow-actions-start

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

       * :ref:`events-roku-capi-workflow-actions-invalid-credentials`
       * :ref:`events-roku-capi-workflow-actions-invalid-settings`

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

.. events-roku-capi-workflow-actions-end

.. note:: If Roku rejects an entire batch of events, the workflow reports the error with Roku's field-level detail — review the event field values returned by your query. If sends are rate limited, Amperity retries automatically; reduce the volume of events sent per orchestration if the limit persists.


.. _events-roku-capi-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _events-roku-capi-workflow-actions-invalid-settings:

Invalid settings
--------------------------------------------------

.. events-roku-capi-workflow-actions-invalid-settings-start

The configuration for this workflow has a setting that |destination-name| was unable to accept. This most often means the CAPI token is not authorized for the configured event group — verify that the **Event group ID** is correct and that the CAPI token belongs to the same Roku Ads account as the event group.

.. events-roku-capi-workflow-actions-invalid-settings-end

.. events-roku-capi-workflow-actions-invalid-settings-steps-start

To resolve this error, verify the settings configured for this workflow in Amperity.

#. Open the **Destinations** page and review the settings for the |destination-name| destination associated with this workflow. Verify the **Event group ID**, and that the connected credential's CAPI token was generated in the same Roku Ads account.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. events-roku-capi-workflow-actions-invalid-settings-steps-end
