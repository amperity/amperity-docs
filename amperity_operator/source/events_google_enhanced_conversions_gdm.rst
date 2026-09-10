.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Enhanced Conversions (GDM)
.. |plugin-name| replace:: "Google Enhanced Conversions (GDM)"
.. |credential-type| replace:: "google-enhanced-conversions-gdm"
.. |required-credentials| replace:: "Refresh token"
.. |what-send| replace:: offline conversions
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "google"
.. |hashed-fields| replace:: **email** and **phone**


.. meta::
    :description lang=en:
        Configure Amperity to send offline conversions to Google Enhanced Conversions (GDM).

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send offline conversions to Google Enhanced Conversions (GDM).

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for Google Enhanced Conversions (GDM)

======================================================================
Configure events for Google Enhanced Conversions (GDM)
======================================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-enhanced-conversions-gdm-start
   :end-before: .. term-google-enhanced-conversions-gdm-end

.. events-google-enhanced-conversions-gdm-overview-start

Send |what-send| to a Google Ads conversion action so that Google Ads can measure and optimize on conversions that happen away from your website. Each row returned by your query is sent as a single conversion, matched to a Google user on a hashed **email** address or **phone** number. Because it matches on personal information rather than an ad-click identifier, it suits in-store purchases, call-center bookings, in-app purchases, and other offline activity where no click ID exists.

Amperity sends conversions to Google Ads through the Google Data Manager API. There is no audience or list involved — every orchestration submits a new batch of conversions.

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sha-256-hashed-fields-start
   :end-before: .. setting-common-sha-256-hashed-fields-end

.. note:: For **gmail.com** and **googlemail.com** addresses, Amperity removes dots from the username and drops any plus-sign tag before hashing, matching Google's own normalization.

.. events-google-enhanced-conversions-gdm-overview-end

.. events-google-enhanced-conversions-gdm-beta-start

.. admonition:: Beta

   The Google Enhanced Conversions (GDM) connector is currently in beta. Contact your Amperity representative to learn more.

.. events-google-enhanced-conversions-gdm-beta-end

.. events-google-enhanced-conversions-gdm-which-start

.. important:: Amperity provides two Google Enhanced Conversions connectors, and both appear in the destination picker. Use **Google Enhanced Conversions (GDM)** — this connector — for new setups: it sends conversions over Google's Data Manager platform, which Google requires for advertisers who began uploading enhanced conversions after 15 June 2026. The separate **Google Enhanced Conversions** connector uses the older Google Ads API upload path. Connect and configure each one separately.

.. events-google-enhanced-conversions-gdm-which-end


.. _events-google-enhanced-conversions-gdm-howitworks:

How this destination works
==================================================

.. events-google-enhanced-conversions-gdm-howitworks-start

Amperity normalizes and hashes each row's **email** and **phone**, then submits the conversion to the configured Google Ads conversion action. Google Ads matches the hashed identifiers to a signed-in Google user and attributes the conversion.

Google matches conversions in the background, and the process can take a long time — from minutes to days. Because an orchestration cannot wait that long, Amperity reports a conversion as delivered once Google accepts the batch.

.. important:: A successful orchestration means Google accepted the conversions, not that it has matched and credited them. Because matching depends on whether the hashed identifiers correspond to real Google users, confirm results in the Google Ads interface.

.. events-google-enhanced-conversions-gdm-howitworks-end


.. _events-google-enhanced-conversions-gdm-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-google-enhanced-conversions-gdm-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Configure Google Ads**

       #. In the Google Ads interface, get the numeric **Conversion action ID** for the conversion action these events are attributed to. This connector uses the numeric ID; it cannot look a conversion action up by name.
       #. Make sure the Google account you connect to Amperity can reach that Google Ads account and can upload conversions to that conversion action.
       #. During sign-in, approve Amperity's request to access Google's Data Manager service. A Google account connected for one of the older Google Ads connectors does not carry this access, because that authorization covers a different Google service.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for |destination-name| *must* be completed within Google, using the **Connect with Google** sign-in flow, before Amperity can send |what-send| to |where-send|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Google Ads customer ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-gdm-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-gdm-customer-id-end

       **Conversion action ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-gdm-conversion-action-id-start
             :end-before: .. setting-google-enhanced-conversions-gdm-conversion-action-id-end

       **Event source**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-gdm-event-source-start
             :end-before: .. setting-google-enhanced-conversions-gdm-event-source-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - **Optional configuration settings**

       **Manager (MCC) customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-gdm-login-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-gdm-login-customer-id-end

.. events-google-enhanced-conversions-gdm-get-details-end


.. _events-google-enhanced-conversions-gdm-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure OAuth**

.. events-google-enhanced-conversions-gdm-credentials-steps-start

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
     - In the **Credentials settings** dialog box, from the **Plugin** dropdown, select |plugin-name|.

       .. note:: Amperity provides two Google Enhanced Conversions connectors. Select |plugin-name| to send conversions over Google's Data Manager platform. **Google Enhanced Conversions** is the separate connector that uses the older Google Ads API upload path.

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

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. events-google-enhanced-conversions-gdm-credentials-steps-end


.. _events-google-enhanced-conversions-gdm-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Enhanced Conversions (GDM)**

.. events-google-enhanced-conversions-gdm-add-destination-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
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

       **Google Ads customer ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-gdm-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-gdm-customer-id-end

       **Conversion action ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-gdm-conversion-action-id-start
             :end-before: .. setting-google-enhanced-conversions-gdm-conversion-action-id-end

       **Event source**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-gdm-event-source-start
             :end-before: .. setting-google-enhanced-conversions-gdm-event-source-end

       **Manager (MCC) customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-gdm-login-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-gdm-login-customer-id-end

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

.. events-google-enhanced-conversions-gdm-add-destination-end


.. _events-google-enhanced-conversions-gdm-build-query:

Build a query
==================================================

.. events-google-enhanced-conversions-gdm-build-query-start

Use a query to return one row per offline conversion to send to |destination-name|. Each row must include a conversion timestamp and at least one identifier — an **email** address, a **phone** number, or both. Sending both improves the match rate. You can also include a conversion value with its currency, and an order ID that Google uses to deduplicate conversions re-sent across repeated runs.

.. events-google-enhanced-conversions-gdm-build-query-end

.. events-google-enhanced-conversions-gdm-build-query-required-start

Review the :ref:`events-google-enhanced-conversions-gdm-parameters` section for the columns your query must and may return.

.. events-google-enhanced-conversions-gdm-build-query-required-end

Bound the query to recent conversions so each orchestration sends new conversions instead of re-sending history; choose a window that matches how often the orchestration runs. A query that returns a collection of recent conversions for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     c360.email AS email
     ,c360.phone AS phone
     ,ut.order_datetime AS conversion_timestamp
     ,ut.order_revenue AS conversion_value
     ,'USD' AS currency_code
     ,ut.order_id AS order_id
   FROM Unified_Transactions ut
   JOIN Customer_360 c360 ON ut.amperity_id = c360.amperity_id
   WHERE ut.order_datetime > (CURRENT_DATE - interval '7' day)
     AND (c360.email IS NOT NULL OR c360.phone IS NOT NULL)

where:

* **email** and **phone** are the match identifiers. The ``WHERE`` clause keeps only rows that have at least one, because a conversion with neither cannot be matched. Do not hash them in the query — Amperity hashes them automatically.
* **conversion_timestamp** must be an |ext_iso_8601| instant with a UTC offset, such as ``2026-07-10T12:00:00Z``. Amperity sends it as returned by your query.
* **conversion_value** is the value Google Ads bids on, and is sent only when **currency_code** is also present.
* **currency_code** is a valid |ext_iso_4217| currency code — for example, ``USD``.
* **order_id** is the deduplication key. Send a stable value so that repeated sends of the same conversion are not double-counted.


.. _events-google-enhanced-conversions-gdm-data-validation:

Data validation
==================================================

.. events-google-enhanced-conversions-gdm-data-validation-start

Amperity validates the dataset and each row before sending. A dataset that maps neither **email** nor **phone** is rejected before the orchestration runs, because Google cannot match a conversion without an identifier.

During a send, a row is dropped and reported as failed when:

* It has no usable **email** or **phone** value.

A row that has a **conversion_value** but no **currency_code** is still sent, but the value is dropped and reported: the conversion is recorded as a count rather than carrying the value. Column names are matched without regard to capitalization. Rows that Google rejects — for example, an unparseable timestamp — are reported as failed rows with Google's reason in the orchestration's error log.

.. events-google-enhanced-conversions-gdm-data-validation-end


.. _events-google-enhanced-conversions-gdm-parameters:

Conversion fields
==================================================

.. events-google-enhanced-conversions-gdm-parameters-start

The following table describes each column Amperity sends to |destination-name|. A query must return columns with the same name as listed in the "Amperity name" column; Amperity maps them to the Data Manager field names automatically.

.. list-table::
   :widths: 24 24 52
   :header-rows: 1

   * - Amperity name
     - Data Manager field
     - Description

   * - **conversion_timestamp**
     - **eventTimestamp**
     - **Required**

       When the conversion happened, as an |ext_iso_8601| instant with a UTC offset — for example, ``2026-07-10T12:00:00Z``. Amperity sends the value as returned by your query.

   * - **email**
     - **userData.userIdentifiers.emailAddress**
     - **Optional**, but at least one of **email** or **phone** is required.

       An email address. Amperity normalizes it to Google's format and applies SHA-256 hashing before sending.

   * - **phone**
     - **userData.userIdentifiers.phoneNumber**
     - **Optional**, but at least one of **email** or **phone** is required.

       A phone number. Amperity converts it to E.164 format and applies SHA-256 hashing before sending.

   * - **conversion_value**
     - **conversionValue**
     - **Optional**

       The value of the conversion, as a number. Sent only when **currency_code** is also present.

   * - **currency_code**
     - **currency**
     - **Optional**

       The currency that **conversion_value** is expressed in, as a three-character |ext_iso_4217| code. Required in order to send **conversion_value**.

   * - **order_id**
     - **transactionId**
     - **Optional**

       A deduplication key. When the same conversion is re-sent across repeated runs, Google collapses rows with the same order ID into one so the conversion is not counted twice.

.. events-google-enhanced-conversions-gdm-parameters-end


.. _events-google-enhanced-conversions-gdm-delivery:

Delivery and results
==================================================

.. events-google-enhanced-conversions-gdm-delivery-start

Google accepts a batch of conversions almost immediately and then matches them in the background over a window that can range from minutes to days. Amperity treats a conversion as delivered once Google accepts the batch.

* A successful orchestration means Google accepted the conversions, not that it matched and credited them. Confirm final results in the Google Ads interface.
* Per-conversion failures are reported on a best-effort basis. Amperity reports the failures that Google returns quickly as failed rows in the orchestration's error log. Failures that Google surfaces only later do not appear in the orchestration.
* Amperity automatically splits large sends into batches of 2,000 conversions. This is not something you configure.
* Conversions cannot be deleted or retracted once submitted. Google offers no way to take back a conversion, so test with care.

.. events-google-enhanced-conversions-gdm-delivery-end


.. _events-google-enhanced-conversions-gdm-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-google-enhanced-conversions-gdm-workflow-actions-start

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

.. events-google-enhanced-conversions-gdm-workflow-actions-end

.. note:: Connection problems are caught when the destination is saved: Amperity submits a single test conversion to Google in a validate-only mode that writes nothing. If Google rejects the connected account, reconnect the destination to refresh the Google authorization. If Google accepts the sign-in but refuses the destination, check the **Google Ads customer ID** and **Conversion action ID**. During an orchestration, per-conversion failures are recorded as failed rows with Google's own explanation in the error log.


.. _events-google-enhanced-conversions-gdm-api-reference:

Google Data Manager API reference
==================================================

.. vale off

.. events-google-enhanced-conversions-gdm-api-reference-start

Amperity sends conversions to |destination-name| using the `Google Data Manager API <https://developers.google.com/data-manager/api/reference/rest/v1/events/ingest>`__ |ext_link|. Conversions are submitted through the ``events:ingest`` method. Amperity normalizes and hashes identifiers according to Google's `identifier formatting guide <https://developers.google.com/data-manager/api/devguides/concepts/formatting>`__ |ext_link|.

.. events-google-enhanced-conversions-gdm-api-reference-end

.. vale on
