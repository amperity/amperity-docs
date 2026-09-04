.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Attentive
.. |plugin-name| replace:: "Attentive eCommerce & Conversion Events"
.. |credential-type| replace:: "attentive-ecommerce-offline-events"
.. |required-credentials| replace:: "API key"
.. |what-send| replace:: ecommerce and conversion events
.. |where-send| replace:: |destination-name|

.. meta::
    :description lang=en:
        Configure Amperity to send ecommerce and conversion events to Attentive.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send ecommerce and conversion events to Attentive.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for Attentive

==================================================
Configure events for Attentive
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-attentive-ecommerce-start
   :end-before: .. term-attentive-ecommerce-end

.. events-attentive-ecommerce-overview-start

Send |what-send| to |destination-name| to power SMS and email journey triggers, audience segmentation, and revenue attribution. Amperity sends the rows returned by your query to Attentive as events, each identified by a customer email, phone number, or both.

A destination sends a single event type, which you choose from ``PRODUCT_VIEW``, ``ADD_TO_CART``, ``PURCHASE``, ``CUSTOM_EVENT``, or ``CUSTOM_ATTRIBUTES``. To send more than one event type, configure a separate destination for each. See the `Attentive API reference <https://docs.attentivemobile.com/openapi/reference/overview/>`__ |ext_link| for more information.

.. events-attentive-ecommerce-overview-end

.. events-attentive-ecommerce-beta-start

.. admonition:: Beta

   The Attentive eCommerce & Conversion Events connector is currently in beta. Contact your Amperity representative to learn more.

.. events-attentive-ecommerce-beta-end


.. _events-attentive-ecommerce-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-attentive-ecommerce-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-attentive-api-key-start
             :end-before: .. credential-attentive-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-attentive-api-key-find-start
             :end-before: .. credential-attentive-api-key-find-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Attentive settings**

       **Event Type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-attentive-event-type-start
             :end-before: .. setting-attentive-event-type-end

       **Custom Event Type Name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-attentive-custom-event-type-name-start
             :end-before: .. setting-attentive-custom-event-type-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Request properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-attentive-query-must-return-start
             :end-before: .. setting-attentive-query-must-return-end

          See :ref:`events-attentive-ecommerce-event-types` for the event type each destination sends, and :ref:`events-attentive-ecommerce-source-columns` for the columns each event type accepts.

.. events-attentive-ecommerce-get-details-table-end


.. _events-attentive-ecommerce-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Attentive**

.. events-attentive-ecommerce-credentials-steps-start

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

       From the **Plugin** dropdown, select **Attentive eCommerce & Conversion Events**.

       Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-attentive-api-key-start
             :end-before: .. credential-attentive-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-attentive-api-key-find-start
             :end-before: .. credential-attentive-api-key-find-end

.. events-attentive-ecommerce-credentials-steps-end


.. _events-attentive-ecommerce-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-attentive-ecommerce-add-destination-start

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

       Enter the name of the destination and a description. For example: "|destination-name| purchase events" and "Send purchase events to |destination-name|.".

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

       **Event Type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-attentive-event-type-start
             :end-before: .. setting-attentive-event-type-end

       **Custom Event Type Name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-attentive-custom-event-type-name-start
             :end-before: .. setting-attentive-custom-event-type-name-end

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

.. events-attentive-ecommerce-add-destination-end


.. _events-attentive-ecommerce-build-query:

Build a query
==================================================

.. events-attentive-ecommerce-build-query-start

Use a query to build a combination of data that returns one row per event to send to |destination-name|. Every event type requires at least one customer identifier — an **email**, a **phone** number, or both. The remaining columns your query returns depend on the event type the destination sends; review :ref:`events-attentive-ecommerce-source-columns` for the columns each event type accepts.

.. events-attentive-ecommerce-build-query-end

.. events-attentive-ecommerce-build-query-required-start

Bound the query to recent activity so each orchestration sends new events instead of re-sending the full history; choose a window that matches how often the orchestration runs.

.. events-attentive-ecommerce-build-query-required-end

A purchase query typically draws one row per line item from the **Unified Itemized Transactions** table, joined to **Customer 360** for identifiers. Rows that share an **order_id** (with the same identifiers) are grouped into a single purchase event, so return every line item for an order. A query that returns recent purchase line items for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     c360.email AS email
     ,c360.phone AS phone
     ,txn.order_id AS order_id
     ,txn.order_datetime AS occurred_at
     ,txn.product_id AS product_id
     ,txn.product_id AS product_variant_id
     ,txn.product_description AS name
     ,txn.unit_revenue AS price
     ,txn.item_quantity AS quantity
     ,'USD' AS currency
     ,'WEB' AS sales_channel
   FROM Unified_Itemized_Transactions txn
   LEFT JOIN Customer_360 c360 ON txn.amperity_id = c360.amperity_id
   WHERE txn.order_datetime > (CURRENT_DATE - interval '30' day)
     AND (txn.is_return = FALSE OR txn.is_return IS NULL)
     AND (txn.is_cancellation = FALSE OR txn.is_cancellation IS NULL)
     AND (c360.email IS NOT NULL OR c360.phone IS NOT NULL)

Returns and cancellations are excluded so that only completed purchases are sent. If your products have distinct variants, map the variant identifier to **product_variant_id** instead of reusing **product_id**.


.. _events-attentive-ecommerce-event-types:

Event types
==================================================

.. events-attentive-ecommerce-event-types-start

The **Event Type** setting determines which Attentive endpoint a destination sends to. Each destination sends exactly one event type; to send more than one, configure a separate destination for each. The API key's scopes must cover the event types you send.

.. list-table::
   :widths: 24 40 36
   :header-rows: 1

   * - Event Type
     - Description
     - Required Attentive scope

   * - ``PRODUCT_VIEW``
     - A subscriber viewed a product. Sends one event per row.
     - ``ecommerce:write``

   * - ``ADD_TO_CART``
     - A subscriber added a product to their cart. Sends one event per row.
     - ``ecommerce:write``

   * - ``PURCHASE``
     - A subscriber completed a purchase. Line items that share an order are sent together as one event.
     - ``ecommerce:write``

   * - ``CUSTOM_EVENT``
     - Any behavioral event — for example, "Order Shipped" — that triggers a pre-configured Attentive journey. Sends one event per row.
     - ``events:write``

   * - ``CUSTOM_ATTRIBUTES``
     - Subscriber profile attributes — for example, loyalty tier or preferred category. Sends one update per row.
     - ``attributes:write``

.. note:: A ``CUSTOM_EVENT`` type must already exist in the Attentive UI before you send it. Rows sent for an event type that does not exist are rejected and skipped. With ``CUSTOM_ATTRIBUTES``, each attribute is locked to the data type Amperity first sends — for example, a value first sent as text cannot later be sent as a number — so plan attribute types before you enable a destination.

.. events-attentive-ecommerce-event-types-end


.. _events-attentive-ecommerce-source-columns:

Source columns by event type
==================================================

.. events-attentive-ecommerce-source-columns-start

The columns your query must return depend on the destination's **Event Type**. Column names are case-insensitive. Every event type requires at least one of **email** or **phone**; Amperity lowercases and trims **email** and normalizes **phone** to E.164 format.

**PRODUCT_VIEW and ADD_TO_CART**

.. list-table::
   :widths: 24 16 60
   :header-rows: 1

   * - Amperity column
     - Attentive field
     - Description

   * - **email**
     - **user.email**
     - **Required** (one of email or phone). A subscriber email address.

   * - **phone**
     - **user.phone**
     - **Required** (one of email or phone). A subscriber phone number. Amperity normalizes it to E.164; a number that cannot be normalized falls back to email only.

   * - **product_id**
     - **productId**
     - **Required.** The vendor product identifier. A row missing this value is skipped.

   * - **product_variant_id**
     - **productVariantId**
     - **Required.** The vendor product variant identifier. A row missing this value is skipped.

   * - **name**
     - **name**
     - **Optional.** The product display name.

   * - **price**
     - **price.value**
     - **Optional.** A unit price, as a number or a string (for example, ``19.99`` or ``$19.99``). Non-numeric or negative values are dropped from the row.

   * - **currency**
     - **price.currency**
     - **Optional.** The |ext_iso_4217| currency code for **price**. Defaults to ``USD`` when absent.

   * - **quantity**
     - **quantity**
     - **Optional.** The number of units, as a number or a string. Zero, negative, or non-numeric values are dropped from the row.

   * - **product_image**
     - **productImage**
     - **Optional.** A product image URL.

   * - **product_url**
     - **productUrl**
     - **Optional.** A product page URL.

   * - **occurred_at**
     - **occurredAt**
     - **Optional.** When the event occurred, as an |ext_iso_8601| timestamp. Omit to use the time the event is sent. See :ref:`events-attentive-ecommerce-data-validation` for how timestamps in the past are handled.

**PURCHASE**

Purchase accepts every product view column above, plus the following. Return one row per line item; rows that share the same **order_id** and identifiers are grouped into a single purchase event.

.. list-table::
   :widths: 24 16 60
   :header-rows: 1

   * - Amperity column
     - Attentive field
     - Description

   * - **order_id**
     - **orderId**
     - **Optional.** The order identifier. Used both to group line items into one purchase event and by Attentive to deduplicate.

   * - **sales_channel**
     - **salesChannel.channelType**
     - **Optional.** The channel the purchase occurred on (for example, ``WEB`` or ``IN_STORE``). Amperity converts the value to uppercase.

**CUSTOM_EVENT**

.. list-table::
   :widths: 24 16 60
   :header-rows: 1

   * - Amperity column
     - Attentive field
     - Description

   * - **email**
     - **user.email**
     - **Required** (one of email or phone). A subscriber email address.

   * - **phone**
     - **user.phone**
     - **Required** (one of email or phone). A subscriber phone number.

   * - **event_type_name**
     - **type**
     - **Optional.** The Attentive custom event type name for this row. Overrides the **Custom Event Type Name** setting. The value must exactly match an event type already created in the Attentive UI (case-sensitive).

   * - **external_event_id**
     - **externalEventId**
     - **Optional.** A unique identifier for the event that Attentive uses to deduplicate.

   * - **occurred_at**
     - **occurredAt**
     - **Optional.** When the event occurred, as an |ext_iso_8601| timestamp. Omit to use the time the event is sent.

   * - *any other column*
     - **properties**
     - **Optional.** Every other column becomes an event property. Restricted characters (``"'(){}[]\|,``) are stripped from column names.

**CUSTOM_ATTRIBUTES**

.. list-table::
   :widths: 24 16 60
   :header-rows: 1

   * - Amperity column
     - Attentive field
     - Description

   * - **email**
     - **user.email**
     - **Required** (one of email or phone). A subscriber email address.

   * - **phone**
     - **user.phone**
     - **Required** (one of email or phone). A subscriber phone number.

   * - *any other column*
     - **properties**
     - **Required.** Every other column becomes a subscriber attribute; at least one is required. Restricted characters (``"'(){}[]\|,``) are stripped from attribute names.

.. events-attentive-ecommerce-source-columns-end


.. _events-attentive-ecommerce-data-validation:

Data validation
==================================================

.. events-attentive-ecommerce-data-validation-start

Amperity validates each row before sending, so that one invalid row does not stop the rest of the events. A row is skipped, and reported, when:

* It has neither a valid **email** nor a phone number that can be normalized to E.164 — Attentive requires at least one identifier to match a subscriber.
* For ``PRODUCT_VIEW``, ``ADD_TO_CART``, or ``PURCHASE``, it is missing **product_id** or **product_variant_id**.
* For ``CUSTOM_EVENT``, no event type is resolved from either the **event_type_name** column or the **Custom Event Type Name** setting.
* For ``CUSTOM_ATTRIBUTES``, it contains no attribute columns beyond the identifiers.

Optional values that cannot be used — a non-numeric or negative **price**, a zero or non-numeric **quantity**, or an unparseable **occurred_at** — are dropped from that row individually; the rest of the event is still sent.

.. note:: An event whose **occurred_at** is more than 12 hours in the past is still sent and recorded in Attentive's behavioral history, but it does not trigger journey automations. This is expected when backfilling historical events. Amperity logs the number of such events after each run.

.. events-attentive-ecommerce-data-validation-end


.. _events-attentive-ecommerce-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-attentive-ecommerce-workflow-actions-start

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

       * :ref:`events-attentive-ecommerce-workflow-actions-invalid-credentials`

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

.. events-attentive-ecommerce-workflow-actions-end

.. note:: If Attentive rejects a request, Amperity reports the error with Attentive's response detail — review the field values returned by your query. Rows that Attentive rejects individually (for example, an unknown subscriber, or a custom event type that does not yet exist) are skipped and reported without stopping the rest of the run. If sends are rate limited, Amperity retries automatically.


.. _events-attentive-ecommerce-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. events-attentive-ecommerce-workflow-actions-invalid-credentials-start

|destination-name| was unable to accept the API key configured for this workflow. The key may be incorrect or revoked, or it may be missing a scope required by the destination's event type — ``PRODUCT_VIEW``, ``ADD_TO_CART``, and ``PURCHASE`` require ``ecommerce:write``; ``CUSTOM_EVENT`` requires ``events:write``; ``CUSTOM_ATTRIBUTES`` requires ``attributes:write``.

.. events-attentive-ecommerce-workflow-actions-invalid-credentials-end

.. events-attentive-ecommerce-workflow-actions-invalid-credentials-steps-start

To resolve this error, verify the API key configured for this workflow in Amperity.

#. In the Attentive UI, confirm the API key is active and has the scopes required by the event type this destination sends. Regenerate the key if necessary.
#. Open the **Destinations** page and update the credential associated with this workflow with a valid API key.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. events-attentive-ecommerce-workflow-actions-invalid-credentials-steps-end
