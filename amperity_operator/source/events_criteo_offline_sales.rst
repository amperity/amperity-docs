.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Criteo
.. |plugin-name| replace:: "Criteo Offline Sales"
.. |credential-type| replace:: "criteo-offline-sales"
.. |required-credentials| replace:: "API key"
.. |what-send| replace:: offline sales
.. |where-send| replace:: |destination-name|
.. |hashed-fields| replace:: **email**

.. meta::
    :description lang=en:
        Configure Amperity to send offline sales to Criteo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send offline sales to Criteo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for Criteo Offline Sales

==================================================
Configure events for Criteo Offline Sales
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-criteo-offline-sales-start
   :end-before: .. term-criteo-offline-sales-end

.. events-criteo-offline-sales-overview-start

Send offline sales to |destination-name| to attribute in-store purchases back to the ads that |destination-name| served, and to inform ad targeting. Amperity sends transaction data at the line-item level: each row returned by your query is one product within a purchase, grouped by transaction and then by shopper, and sent to |destination-name|'s offline sales ingestion service.

Amperity hashes email addresses before sending them; raw email addresses never leave Amperity. A shopper can also be identified by a customer ID or a retailer visitor ID. At least one identifier is required on every row.

.. events-criteo-offline-sales-overview-end

.. events-criteo-offline-sales-beta-start

.. admonition:: Beta

   The |destination-name| Offline Sales connector is currently in beta. Contact your Amperity representative to learn more.

.. events-criteo-offline-sales-beta-end

.. events-criteo-offline-sales-verify-start

.. important::

   Amperity cannot confirm that |destination-name| received or attributed your transactions. |destination-name| accepts any request it can read and reports acceptance the same way whether or not the configured account is correct. A successful connection test and a run that reports no failed rows both mean only that |destination-name| accepted the request — not that the sales were attributed. Confirm that events landed with your Criteo Account Strategist using |destination-name|'s own reporting after your first send.

.. events-criteo-offline-sales-verify-end


.. _events-criteo-offline-sales-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-criteo-offline-sales-get-details-table-start

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
             :start-after: .. credential-criteo-offline-sales-api-key-start
             :end-before: .. credential-criteo-offline-sales-api-key-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Criteo settings**

       **Account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-offline-sales-account-id-start
             :end-before: .. setting-criteo-offline-sales-account-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Query results**

          A query returns one row per transaction line item, with the columns described in :ref:`events-criteo-offline-sales-parameters`. Each row must include a transaction ID, a timestamp, a product ID, a price, a quantity, and at least one shopper identifier.

.. events-criteo-offline-sales-get-details-table-end


.. _events-criteo-offline-sales-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Criteo Offline Sales**

.. events-criteo-offline-sales-credentials-steps-start

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

       From the **Plugin** dropdown, select **Criteo Offline Sales**.

       .. note:: Amperity provides more than one |destination-name| connector. Select **Criteo Offline Sales** to send in-store transactions for retail media attribution. **Criteo** and **Criteo Retail Media** are separate connectors that send audience segments.

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
             :start-after: .. credential-criteo-offline-sales-api-key-start
             :end-before: .. credential-criteo-offline-sales-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-criteo-offline-sales-find-credentials-start
             :end-before: .. credential-criteo-offline-sales-find-credentials-end

.. events-criteo-offline-sales-credentials-steps-end


.. _events-criteo-offline-sales-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-criteo-offline-sales-add-destination-start

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

       Enter the name of the destination and a description. For example: "|destination-name| offline sales" and "Send in-store transactions to |destination-name|.".

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

       **Account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-offline-sales-account-id-start
             :end-before: .. setting-criteo-offline-sales-account-id-end

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

.. events-criteo-offline-sales-add-destination-end


.. _events-criteo-offline-sales-build-query:

Build a query
==================================================

.. events-criteo-offline-sales-build-query-start

Use a query to build a combination of data — typically from the **Unified Itemized Transactions** and **Customer 360** tables — that returns one row per transaction line item to send to |destination-name|. Each row must include a transaction ID, a timestamp, a product ID, a price, a quantity, and at least one shopper identifier: a hashed email address, a customer ID, or a retailer visitor ID. You can also include a currency code and a store ID.

.. events-criteo-offline-sales-build-query-end

.. events-criteo-offline-sales-build-query-required-start

Review the :ref:`events-criteo-offline-sales-parameters` section for the columns your query must and may return, and the :ref:`events-criteo-offline-sales-matching` section for how line items are grouped into transactions and shoppers.

.. note:: |destination-name| attributes offline sales only within **two days** of the transaction. Amperity enforces this window and skips rows outside it — reported as failed with the reason — so late-arriving in-store data cannot be backfilled through this connector. Any delay between an in-store sale and it reaching Amperity reduces this window.

.. note:: |destination-name| deduplicates transactions on their transaction ID, so re-sending a transaction does not count it twice. Bound your query to recent transactions so each orchestration sends new sales rather than re-sending history.

.. events-criteo-offline-sales-build-query-required-end

Bound the query to recent transactions — within |destination-name|'s two-day attribution window — and exclude returns and cancellations so that only completed sales are sent. A query that returns a collection of recent purchase line items for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     uit.order_id AS transaction_id
     ,uit.order_datetime AS timestamp
     ,uit.product_id AS product_id
     ,uit.unit_revenue AS price
     ,uit.item_quantity AS quantity
     ,uit.currency AS currency
     ,c360.email AS email
   FROM Unified_Itemized_Transactions uit
   LEFT JOIN Customer_360 c360 ON uit.amperity_id = c360.amperity_id
   WHERE uit.order_datetime > (CURRENT_DATE - interval '2' day)
   AND COALESCE(uit.is_return, false) = false
   AND COALESCE(uit.is_cancellation, false) = false


.. _events-criteo-offline-sales-matching:

How shoppers and transactions are matched
==================================================

.. events-criteo-offline-sales-matching-start

|destination-name|'s ingestion format carries one shopper per request, with that shopper's transactions nested beneath, and each transaction's line items nested under that. Amperity reassembles the flat rows your query returns into that shape: line items are grouped into transactions, and transactions are grouped by shopper, so one request is sent per shopper. Throughput is therefore measured in shoppers, not rows — a send covering many purchases by a few thousand shoppers is a few thousand requests.

Each shopper is grouped by their strongest available identifier, in this order:

* **email** — the only identifier that keys into |destination-name|'s identity graph. Amperity normalizes and hashes the address before sending.
* **customer_id** — the identifier of a signed-in shopper, stable across their logged-in sessions but meaningful only within your business.
* **retailer_visitor_id** — an identifier for an unrecognized shopper, persistent only on the same device, so the weakest of the three.

Amperity sends every identifier a shopper's rows agree on, not only the strongest one, because |destination-name| matches on whichever it recognizes. Where a shopper's rows carry two genuinely different values for the same identifier, that identifier is omitted rather than a value being chosen at random. Where line items within one transaction disagree on timestamp, currency, or store ID, one value is used rather than the transaction being rejected.

.. events-criteo-offline-sales-matching-end


.. _events-criteo-offline-sales-data-validation:

Data validation
==================================================

.. events-criteo-offline-sales-data-validation-start

Amperity validates each row before grouping it and drops rows that cannot be sent, so that one invalid line item does not sink a shopper's whole request. Dropped rows are reported as failed with the reason. A row is dropped when:

* Every shopper identifier — **email**, **customer_id**, and **retailer_visitor_id** — is empty.
* **transaction_id** is empty.
* **timestamp** is empty or cannot be read. A timestamp may be a full date and time, a date on its own (treated as midnight UTC), or an epoch second count.
* **timestamp** is more than two days in the past, outside |destination-name|'s attribution window. |destination-name| would accept the row and then discard it downstream without reporting it, so Amperity skips it instead.
* **price** is not a number.
* **quantity** is not a whole number.

.. events-criteo-offline-sales-data-validation-end


.. _events-criteo-offline-sales-parameters:

Offline sales fields
==================================================

.. events-criteo-offline-sales-parameters-start

The following table describes each column Amperity sends to |destination-name|. A query must return columns with the same name as listed in the "Amperity name" column; Amperity maps them to the |destination-name| fields automatically. Column names are matched without regard to capitalization.

.. list-table::
   :widths: 24 24 52
   :header-rows: 1

   * - Amperity name
     - Criteo field
     - Description

   * - **transaction_id**
     - **id**
     - **Required**

       The transaction identifier. |destination-name| deduplicates on this value.

   * - **timestamp**
     - **timestamp**
     - **Required**

       When the transaction occurred. Accepts a full date and time, a date on its own (treated as midnight UTC), or an epoch second count. Values that cannot be read, or that are more than two days old, are dropped.

   * - **product_id**
     - **item.id**
     - **Required**

       The product identifier for this line item, matching your product catalog.

   * - **price**
     - **item.price**
     - **Required**

       The unit price for this line item. A non-numeric value is dropped.

   * - **quantity**
     - **item.quantity**
     - **Required**

       The number of units purchased for this line item. A non-whole-number value is dropped.

   * - **email**
     - **id.email**
     - **Optional**

       An email address. Amperity normalizes and hashes the address before sending; the raw address is never sent. At least one of **email**, **customer_id**, or **retailer_visitor_id** is required.

   * - **customer_id**
     - **customer_id**
     - **Optional**

       The identifier of a signed-in shopper. At least one of **email**, **customer_id**, or **retailer_visitor_id** is required.

   * - **retailer_visitor_id**
     - **retailer_visitor_id**
     - **Optional**

       An identifier for an unrecognized shopper, persistent only on the same device. At least one of **email**, **customer_id**, or **retailer_visitor_id** is required.

   * - **currency**
     - **currency**
     - **Optional**

       A three-letter |ext_iso_4217| currency code for the transaction.

   * - **store_id**
     - **store_id**
     - **Optional**

       The store the sale happened in.

.. events-criteo-offline-sales-parameters-end


.. _events-criteo-offline-sales-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-criteo-offline-sales-workflow-actions-start

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

       * :ref:`events-criteo-offline-sales-workflow-actions-invalid-credentials`

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

.. events-criteo-offline-sales-workflow-actions-end

.. note:: A submission that |destination-name| rejects, or that cannot be delivered, is reported as failed rows with |destination-name|'s own message or the delivery error. Because |destination-name| does not authenticate the API key or validate the account, a wrong API key or Account ID produces no error in Amperity — such problems surface only in |destination-name|'s reporting. See :ref:`events-criteo-offline-sales-get-details`.


.. _events-criteo-offline-sales-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end
