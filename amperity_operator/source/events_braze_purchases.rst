.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Braze
.. |plugin-name| replace:: "Braze Purchases"
.. |credential-type| replace:: "braze-purchases"
.. |required-credentials| replace:: "REST API key"
.. |what-send| replace:: purchase events
.. |where-send| replace:: |destination-name|

.. meta::
    :description lang=en:
        Configure Amperity to send purchase events to Braze.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send purchase events to Braze.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure purchase events for Braze

==================================================
Configure purchase events for Braze
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-braze-start
   :end-before: .. term-braze-end

.. events-braze-purchases-overview-start

Send purchase events to |destination-name| using the Braze REST API. Each row returned by your query is sent as a single Braze purchase object to the `/users/track <https://www.braze.com/docs/api/endpoints/user_data/post_user_track/>`__ |ext_link| endpoint and is matched to a Braze user profile by the identifier you choose. See the `purchase object <https://www.braze.com/docs/api/objects_filters/purchase_object/>`__ |ext_link| reference for more information.

.. events-braze-purchases-overview-end

.. events-braze-purchases-billing-start

.. caution:: Braze records and bills for every purchase you send as a data point. Amperity sends each row in the query result on every run and does not de-duplicate purchases against previous runs. Bound your query to recent purchases and avoid re-sending rows you have already sent, or Braze counts the revenue more than once. A row with a **quantity** greater than 100 is sent as more than one purchase object — for example, 250 becomes 100, 100, and 50 — and Braze bills each object as a separate data point.

.. events-braze-purchases-billing-end

.. events-braze-purchases-beta-start

.. admonition:: Beta

   The Braze Purchases connector is currently in beta. Contact your Amperity representative to learn more.

.. events-braze-purchases-beta-end


.. _events-braze-purchases-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-braze-purchases-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **REST API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-braze-purchases-api-key-start
             :end-before: .. credential-braze-purchases-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-braze-purchases-api-find-key-start
             :end-before: .. credential-braze-purchases-api-find-key-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Braze settings**

       **Instance**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-purchases-instance-start
             :end-before: .. setting-braze-purchases-instance-end

       **User identifier**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-user-identifier-start
             :end-before: .. setting-braze-user-identifier-end

          See :ref:`events-braze-purchases-user-identifiers` for the columns each option requires.

       **Update existing profiles only?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-purchases-update-existing-only-start
             :end-before: .. setting-braze-purchases-update-existing-only-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Request properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-purchases-query-must-return-start
             :end-before: .. setting-braze-purchases-query-must-return-end

          See :ref:`events-braze-purchases-fields` for the full list of columns.

.. events-braze-purchases-get-details-table-end


.. _events-braze-purchases-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Braze Purchases**

.. events-braze-purchases-credentials-steps-start

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

       From the **Plugin** dropdown, select **Braze Purchases**.

       .. note:: Amperity provides more than one Braze connector. Select **Braze Purchases** to send purchase events to the Braze REST API. **Braze** (profile attribute sync) and **Braze Cohorts** (audience membership) are separate connectors.

       Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **REST API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-braze-purchases-api-key-start
             :end-before: .. credential-braze-purchases-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-braze-purchases-api-find-key-start
             :end-before: .. credential-braze-purchases-api-find-key-end

.. events-braze-purchases-credentials-steps-end


.. _events-braze-purchases-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-braze-purchases-add-destination-start

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

       Enter the name of the destination and a description. For example: "|destination-name| purchases" and "Send purchase events to |destination-name|.".

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

       **Instance**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-purchases-instance-start
             :end-before: .. setting-braze-purchases-instance-end

       **User identifier**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-user-identifier-start
             :end-before: .. setting-braze-user-identifier-end

       **Update existing profiles only?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-braze-purchases-update-existing-only-start
             :end-before: .. setting-braze-purchases-update-existing-only-end

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

.. events-braze-purchases-add-destination-end


.. _events-braze-purchases-build-query:

Build a query
==================================================

.. events-braze-purchases-build-query-start

Use a query to build a combination of data — typically from the **Unified Itemized Transactions** and **Customer 360** tables — that returns one row per purchase to send to |destination-name|. Each row must include a column for the selected **User identifier** and columns for the purchase's **product_id**, **price**, **currency**, and **purchase_time**. A **quantity** column is optional.

.. events-braze-purchases-build-query-end

.. events-braze-purchases-build-query-required-start

Review the :ref:`events-braze-purchases-fields` section for the columns your query must and may return, and the :ref:`events-braze-purchases-user-identifiers` section for the columns each identifier option requires.

.. events-braze-purchases-build-query-required-end

Bound the query to recent purchases so each orchestration sends new purchases instead of re-sending purchases you have already sent. A query that returns recent purchases keyed by **external_id** is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     c360.customer_id AS external_id
     ,uit.product_id AS product_id
     ,uit.unit_revenue AS price
     ,uit.item_quantity AS quantity
     ,uit.currency AS currency
     ,uit.order_datetime AS purchase_time
   FROM Unified_Itemized_Transactions uit
   JOIN Customer_360 c360 ON uit.amperity_id = c360.amperity_id
   WHERE uit.order_datetime > (CURRENT_DATE - interval '7' day)
     AND COALESCE(uit.is_return, false) = false
     AND COALESCE(uit.is_cancellation, false) = false

.. note:: This example sends the per-unit **unit_revenue** column as **price**, because Braze computes revenue as **price** multiplied by **quantity** — map a per-unit price rather than a line total. When your data has only a line total, divide it by the quantity and guard against a zero or missing divisor, for example ``line_total / NULLIF(quantity, 0) AS price``, or send **quantity** as 1 with the line total as **price**.

.. note:: The example filters out returns and cancellations so they are not sent as purchases and counted as revenue. A return can also carry a negative **unit_revenue**, which Amperity sends as a negative **price** (validation accepts it), so decide deliberately what to send.

.. note:: Map **currency** to a three-character |ext_iso_4217| alphabetic code, such as ``USD``. Amperity checks each value against the ISO 4217 code list and drops rows whose currency is not on it, so a source column that stores a value like "dollar" or "US Dollar" fails every row.


.. _events-braze-purchases-user-identifiers:

User identifiers
==================================================

.. events-braze-purchases-user-identifiers-start

The **User identifier** setting selects how Amperity matches each purchase to a Braze user profile. Choose the identifier your Braze profiles are keyed on — typically the same one the **Braze** connector uses to sync profile attributes — so that purchases land on the right profiles.

* **braze_id** — the Braze-assigned user ID. The query must return a **braze_id** column.
* **external_id** — your own customer identifier. The query must return an **external_id** column.
* **user_alias** — a Braze user alias, which is a name and label pair. The query must return both an **alias_name** and an **alias_label** column.

A row whose identifier value is empty is reported as failed. If the query does not return the column or columns for the selected identifier at all, the orchestration fails validation before sending anything.

.. events-braze-purchases-user-identifiers-end


.. _events-braze-purchases-data-validation:

Data validation
==================================================

.. events-braze-purchases-data-validation-start

Amperity validates each row before sending and drops rows that Braze would reject, so that one invalid row does not cause the rest of a request to be rejected. Dropped rows are reported as failed with the reason. A row is dropped when:

* the value for the selected **User identifier** is empty (for **user_alias**, either **alias_name** or **alias_label** is empty).
* **product_id** is missing or is longer than 255 characters.
* **currency** is not a valid |ext_iso_4217| alphabetic currency code.
* **price** is not a number.
* **purchase_time** is missing or cannot be parsed as a date or timestamp.
* **quantity** is present but is not a whole number, is less than 1 (including 0), or is larger than 7,500 (the most units Amperity can split one row into).

.. events-braze-purchases-data-validation-end


.. _events-braze-purchases-fields:

Purchase object fields
==================================================

.. events-braze-purchases-fields-start

The following table describes each column Amperity sends to |destination-name| as part of a `purchase object <https://www.braze.com/docs/api/objects_filters/purchase_object/>`__ |ext_link|. A query must return columns with the same name as listed in the "Amperity name" column; Amperity maps them to the Braze purchase object automatically.

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-braze-purchases-query-must-return-start
      :end-before: .. setting-braze-purchases-query-must-return-end

.. list-table::
   :widths: 22 20 58
   :header-rows: 1

   * - Amperity name
     - Braze field
     - Description

   * - Identifier column(s)
     - **external_id**, **braze_id**, or **user_alias**
     - **Required**

       The column or columns for the selected **User identifier**: an **external_id** column, a **braze_id** column, or an **alias_name** and **alias_label** pair. See :ref:`events-braze-purchases-user-identifiers`.

   * - **product_id**
     - **product_id**
     - **Required**

       An identifier for the purchase, such as a product name or product category. Maximum 255 characters. Braze shows up to 5,000 distinct values, so a product name or category is more useful than a SKU.

   * - **price**
     - **price**
     - **Required**

       The price for a single unit, as a number. Braze computes revenue as **price** multiplied by **quantity**.

   * - **currency**
     - **currency**
     - **Required**

       A three-character |ext_iso_4217| alphabetic currency code. For example: "USD".

   * - **purchase_time**
     - **time**
     - **Required**

       When the purchase occurred. Accepts a date- or time-typed column, a full |ext_iso_8601| timestamp string, a date-only string, or an epoch-seconds value. A string timestamp must include a UTC offset, such as "2026-07-20T10:00:00Z" — a warehouse form without one, such as "2026-07-20 10:00:00", is not accepted and the row is dropped. A date-only string, such as "2026-07-20", is treated as midnight UTC. The column is named **purchase_time** because **time** is a reserved word in many warehouses.

   * - **quantity**
     - **quantity**
     - **Optional**

       A whole number of units. Braze defaults an absent quantity to 1. A quantity greater than 100 is split across multiple purchase objects (for example, 250 becomes 100, 100, and 50), which preserves the row's total revenue; a single row can carry up to 7,500 units.

.. events-braze-purchases-fields-end


.. _events-braze-purchases-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-braze-purchases-workflow-actions-start

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

       * :ref:`events-braze-purchases-workflow-actions-invalid-credentials`

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

.. events-braze-purchases-workflow-actions-end

.. note:: Braze can accept a request and still reject individual purchases within it. Those rows are reported as failed with the message Braze returned for each, while the workflow itself succeeds — the state behind "the orchestration succeeded but some rows failed." Amperity lists up to 10 such errors per request, followed by a summary line naming how many more were dropped. If Braze rejects an entire request, the workflow reports the error with Braze's message for the whole request — review the purchase field values returned by your query. If sends are rate limited, Amperity retries automatically; reduce the volume of purchases sent per orchestration if the limit persists.


.. _events-braze-purchases-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. events-braze-purchases-workflow-actions-invalid-credentials-start

|destination-name| rejected the REST API key. Braze returns the same error for a REST API key that is not valid and for a key used against the wrong instance, so verify that the key is still active, has the **users.track** permission, and belongs to the same **Instance** the destination is configured for.

.. events-braze-purchases-workflow-actions-invalid-credentials-end

To resolve this error, verify the credentials and instance configured for this workflow in Amperity.

#. Open the **Credentials** page and review the REST API key used with this workflow. Verify that it is still active and has the **users.track** permission.
#. Open the **Destinations** page and verify that the **Instance** setting for the |destination-name| destination matches the instance the REST API key belongs to.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.
