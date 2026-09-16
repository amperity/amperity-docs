.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Microsoft Advertising
.. |plugin-name| replace:: "Microsoft Ads Offline Events"
.. |credential-type| replace:: "microsoft-ads-offline-conversions"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: offline conversions
.. |where-send| replace:: |destination-name|
.. |hashed-fields| replace:: **email** and **phone**

.. meta::
    :description lang=en:
        Configure Amperity to send offline conversions to Microsoft Advertising.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send offline conversions to Microsoft Advertising.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for Microsoft Advertising

==================================================
Configure events for Microsoft Advertising
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-microsoft-ads-offline-conversions-start
   :end-before: .. term-microsoft-ads-offline-conversions-end

.. events-microsoft-ads-overview-start

Send offline conversions to |destination-name| to measure campaign performance, build audiences, and optimize bidding toward outcomes that happen away from your website — such as in-store purchases, phone orders, or qualified leads. Each row returned by your query is sent as a single offline conversion, matched to a Microsoft click ID or a hashed customer identifier.

Amperity hashes email and phone identifiers with SHA-256 before sending them; raw identifier values never leave Amperity. See the `ApplyOfflineConversions reference <https://learn.microsoft.com/en-us/advertising/campaign-management-service/applyofflineconversions>`__ |ext_link| for more information.

.. events-microsoft-ads-overview-end

.. events-microsoft-ads-beta-start

.. admonition:: Beta

   The |destination-name| offline conversions connector is currently in beta. Contact your Amperity representative to learn more.

.. events-microsoft-ads-beta-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sha-256-hashed-fields-start
   :end-before: .. setting-common-sha-256-hashed-fields-end


.. _events-microsoft-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-microsoft-ads-get-details-table-start

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
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Microsoft Advertising settings**

       **Operation mode**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-offline-conversions-operation-mode-start
             :end-before: .. setting-microsoft-ads-offline-conversions-operation-mode-end

       **Customer Account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-offline-conversions-customer-account-id-start
             :end-before: .. setting-microsoft-ads-offline-conversions-customer-account-id-end

       **Customer ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-offline-conversions-customer-id-start
             :end-before: .. setting-microsoft-ads-offline-conversions-customer-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Request properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-offline-conversions-query-must-return-start
             :end-before: .. setting-microsoft-ads-offline-conversions-query-must-return-end

          See :ref:`events-microsoft-ads-parameters` for the full list of columns your query may return.

.. events-microsoft-ads-get-details-table-end


.. _events-microsoft-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Microsoft Ads Offline Events**

.. events-microsoft-ads-credentials-steps-start

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

       From the **Plugin** dropdown, select **Microsoft Ads Offline Events**.

       .. note:: Amperity provides two Microsoft Advertising connectors. Select **Microsoft Ads Offline Events** to send offline conversions. **Microsoft Ads** is a separate connector that sends customer profiles for audience targeting.

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
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. events-microsoft-ads-credentials-steps-end


.. _events-microsoft-ads-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-microsoft-ads-add-destination-start

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

       Enter the name of the destination and a description. For example: "|destination-name| offline conversions" and "Send offline conversions to |destination-name|.".

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

       **Operation mode**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-offline-conversions-operation-mode-start
             :end-before: .. setting-microsoft-ads-offline-conversions-operation-mode-end

       **Customer Account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-offline-conversions-customer-account-id-start
             :end-before: .. setting-microsoft-ads-offline-conversions-customer-account-id-end

       **Customer ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-microsoft-ads-offline-conversions-customer-id-start
             :end-before: .. setting-microsoft-ads-offline-conversions-customer-id-end

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

.. events-microsoft-ads-add-destination-end


.. _events-microsoft-ads-build-query:

Build a query
==================================================

.. events-microsoft-ads-build-query-start

Use a query to build a combination of data — typically from the **Unified Transactions** and **Customer 360** tables — that returns one row per offline conversion to send to |destination-name|. Each row must include a conversion goal name, a conversion timestamp, and at least one identifier: a Microsoft click ID, an email address, or a phone number. You can also include an order ID, a conversion value, and a currency code, which Amperity sends with each conversion.

.. events-microsoft-ads-build-query-end

.. events-microsoft-ads-build-query-required-start

Review the :ref:`events-microsoft-ads-parameters` section for the columns your query must and may return, and the :ref:`events-microsoft-ads-operation-modes` section for how ``send-conversions`` and ``adjust-conversions`` queries differ.

.. note:: |destination-name| does not deduplicate offline conversions. Bound your query to new conversions — or use a unique-count conversion goal — so the same conversion is not sent, and counted, more than once.

.. events-microsoft-ads-build-query-required-end

Bound the query to recent conversions — |destination-name| accepts conversions up to 90 days old — so each orchestration sends new conversions instead of re-sending history. A query that returns a collection of recent purchase conversions for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     'In-store purchase' AS conversion_name
     ,ut.order_datetime AS conversion_time
     ,c360.email AS email
     ,c360.phone AS phone
     ,ut.order_id AS order_id
     ,ut.order_revenue AS conversion_value
     ,ut.currency AS currency_code
   FROM Unified_Transactions ut
   LEFT JOIN Customer_360 c360 ON ut.amperity_id = c360.amperity_id
   WHERE ut.order_datetime > (CURRENT_DATE - interval '7' day)
   AND (c360.email IS NOT NULL OR c360.phone IS NOT NULL)


.. _events-microsoft-ads-operation-modes:

Operation modes
==================================================

.. events-microsoft-ads-operation-modes-start

A destination sends data in one of two operation modes, set by the **Operation mode** setting:

* **send-conversions** uploads new offline conversions to |destination-name|.
* **adjust-conversions** restates or retracts conversions that were uploaded previously. A ``Restate`` adjustment updates a conversion's value; a ``Retract`` adjustment voids it.

A destination uses a single mode. To both upload and adjust conversions, configure a separate destination for each mode. In ``adjust-conversions`` mode, each row must also identify the original conversion with **conversion_name**, **conversion_time**, and one of **msclkid**, **email**, or **phone**.

.. events-microsoft-ads-operation-modes-end


.. _events-microsoft-ads-conversion-goals:

Set up a conversion goal
==================================================

.. events-microsoft-ads-conversion-goals-start

Before you send offline conversions, create an offline conversion goal in |destination-name| and note its name. The **conversion_name** column returned by your query must match the goal name exactly, including capitalization.

A new conversion goal can take up to two hours to become available. Until it does, |destination-name| rejects conversions sent to that goal.

.. events-microsoft-ads-conversion-goals-end


.. _events-microsoft-ads-data-validation:

Data validation
==================================================

.. events-microsoft-ads-data-validation-start

Amperity validates each row before sending and drops rows that |destination-name| would reject, so that one invalid row does not cause an entire batch of conversions to be rejected. Dropped rows are reported as failed with the reason. A row is dropped when:

* **conversion_name** or **conversion_time** is missing.
* None of **msclkid**, **email**, or **phone** is present.
* **conversion_time** cannot be parsed as an |ext_iso_8601| instant with a UTC offset (for example, ``2026-07-10T12:00:00Z``), or is more than 90 days in the past.
* In ``adjust-conversions`` mode: **adjustment_type** is not ``Restate`` or ``Retract``, **adjustment_time** is missing or is not later than **conversion_time**, or a ``Restate`` is missing **adjustment_value** or **adjustment_currency_code**.

An individual identifier that cannot be used — an **email** without an ``@``, or a **phone** number that cannot be normalized — is dropped from that row; the rest of the conversion is still sent when another identifier remains. A non-numeric **conversion_value** (and its **currency_code**) is dropped the same way.

.. events-microsoft-ads-data-validation-end


.. _events-microsoft-ads-parameters:

Offline conversion fields
==================================================

.. events-microsoft-ads-parameters-start

The following table describes each column Amperity sends to |destination-name|. A query must return columns with the same name as listed in the "Amperity name" column; Amperity maps them to the |destination-name| field names automatically.

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-microsoft-ads-offline-conversions-query-must-return-start
      :end-before: .. setting-microsoft-ads-offline-conversions-query-must-return-end

.. list-table::
   :widths: 24 24 52
   :header-rows: 1

   * - Amperity name
     - Microsoft Advertising field
     - Description

   * - **conversion_name**
     - **ConversionName**
     - **Required**

       The name of the offline conversion goal. Case-sensitive — must match the goal in |destination-name| exactly. See :ref:`events-microsoft-ads-conversion-goals`.

   * - **conversion_time**
     - **ConversionTime**
     - **Required**

       When the conversion occurred, as an |ext_iso_8601| instant with a UTC offset (for example, ``2026-07-10T12:00:00Z``). Values that cannot be parsed, or that are more than 90 days old, are dropped.

   * - **msclkid**
     - **MicrosoftClickId**
     - **Optional**

       The Microsoft click ID captured from the ad click. One of **msclkid**, **email**, or **phone** is required.

   * - **email**
     - **HashedEmailAddress**
     - **Optional**

       An email address. Amperity applies SHA-256 hashing before sending. One of **msclkid**, **email**, or **phone** is required.

   * - **phone**
     - **HashedPhoneNumber**
     - **Optional**

       A phone number. Amperity normalizes the number to E.164 format using the US region and applies SHA-256 hashing before sending. One of **msclkid**, **email**, or **phone** is required.

   * - **order_id**
     - **ClientId**
     - **Optional**

       Your identifier for the conversion. Include it so the conversion can be restated or retracted later in ``adjust-conversions`` mode.

   * - **conversion_value**
     - **ConversionValue**
     - **Optional**

       A numeric value for the conversion.

   * - **currency_code**
     - **ConversionCurrencyCode**
     - **Optional**

       A three-character |ext_iso_4217| currency code for **conversion_value**. Sent only when **conversion_value** is present.

.. events-microsoft-ads-parameters-end

.. events-microsoft-ads-adjustment-fields-start

In ``adjust-conversions`` mode, a query returns the same identifying columns, plus the following:

.. list-table::
   :widths: 24 24 52
   :header-rows: 1

   * - Amperity name
     - Microsoft Advertising field
     - Description

   * - **adjustment_type**
     - **AdjustmentType**
     - **Required**

       ``Restate`` to update a conversion's value, or ``Retract`` to void it.

   * - **adjustment_time**
     - **AdjustmentTime**
     - **Required**

       When the adjustment occurred, as an |ext_iso_8601| instant. Must be later than **conversion_time**.

   * - **adjustment_value**
     - **AdjustmentValue**
     - **Required for Restate**

       The new conversion value.

   * - **adjustment_currency_code**
     - **AdjustmentCurrencyCode**
     - **Required for Restate**

       A three-character |ext_iso_4217| currency code for **adjustment_value**.

.. events-microsoft-ads-adjustment-fields-end


.. _events-microsoft-ads-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-microsoft-ads-workflow-actions-start

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

       * :ref:`events-microsoft-ads-workflow-actions-invalid-credentials`

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

.. events-microsoft-ads-workflow-actions-end

.. note:: If |destination-name| rejects a batch of conversions, the workflow reports the error with Microsoft's field-level detail. A common cause is a **conversion_name** that does not match a conversion goal exactly, or a goal that has not finished propagating — see :ref:`events-microsoft-ads-conversion-goals`. If sends are rate limited, Amperity retries automatically.


.. _events-microsoft-ads-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end
