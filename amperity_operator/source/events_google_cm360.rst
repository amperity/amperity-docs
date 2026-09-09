.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Campaign Manager 360
.. |plugin-name| replace:: "Google CM360"
.. |credential-type| replace:: "google-cm360"
.. |required-credentials| replace:: "Refresh token"
.. |what-send| replace:: offline conversions
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "google"


.. meta::
    :description lang=en:
        Configure Amperity to send offline conversions to Google Campaign Manager 360.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send offline conversions to Google Campaign Manager 360.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure events for Google Campaign Manager 360

=======================================================
Configure events for Google Campaign Manager 360
=======================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-cm360-start
   :end-before: .. term-google-cm360-end

.. events-google-cm360-overview-start

Send |what-send| to |destination-name| (CM360) so that Search Ads 360 can optimize bidding on the real, delivered value of a conversion. Each row returned by your query is sent as a single conversion, tied to the Google Click ID (**gclid**) of the ad click that led to it. A common use is sending a predicted lifetime value as the conversion value, rather than the order total alone.

Amperity sends conversions to CM360 through the Google Data Manager API. There is no audience or list involved — every orchestration submits a new batch of conversions.

.. caution:: Amperity records consent as granted at the request level for every conversion in a batch. The connector does not send per-customer consent signals, so exclude any customer who has opted out of ad tracking from the query that returns results for |destination-name|.

.. events-google-cm360-overview-end

.. events-google-cm360-beta-start

.. admonition:: Beta

   The Google CM360 connector is currently in beta. Contact your Amperity representative to learn more.

.. events-google-cm360-beta-end


.. _events-google-cm360-howitworks:

How this destination works
==================================================

.. events-google-cm360-howitworks-start

When a customer clicks a Google ad, a Google Click ID (**gclid**) is captured. If that customer later converts away from your website — for example, an in-store purchase — CM360 has no record of that conversion. Amperity sends the conversion with the original **gclid** attached, and CM360 matches it back to the click so that Search Ads 360 can attribute and bid on the conversion.

CM360 matches conversions in the background, and the process can take a long time — from minutes to days. Because an orchestration cannot wait that long, Amperity reports a conversion as delivered once CM360 accepts the batch.

.. important:: A successful orchestration means CM360 accepted the conversions, not that it has matched and credited them. Confirm final, per-conversion outcomes in the Campaign Manager 360 interface.

.. events-google-cm360-howitworks-end


.. _events-google-cm360-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-google-cm360-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Configure Google Campaign Manager 360**

       #. In Campaign Manager 360, get the numeric **Floodlight configuration ID** and the numeric **Floodlight activity ID** for the conversions you want to send. Use the numeric activity ID, not the activity tag string.
       #. Make sure the Google account you connect to Amperity can reach that Floodlight configuration and has been granted access to the Campaign Manager account.
       #. During sign-in, approve Amperity's request to access Google's Data Manager service. A Google account connected for another Amperity Google connector does not automatically carry this access.


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

       **Floodlight configuration ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-cm360-floodlight-config-id-start
             :end-before: .. setting-google-cm360-floodlight-config-id-end

       **Floodlight activity ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-cm360-floodlight-activity-id-start
             :end-before: .. setting-google-cm360-floodlight-activity-id-end

.. events-google-cm360-get-details-table-end


.. _events-google-cm360-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure OAuth**

.. events-google-cm360-credentials-steps-start

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

       .. note:: Amperity provides several Google connectors. Select |plugin-name| to send offline conversions to |destination-name|.

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

.. events-google-cm360-credentials-steps-end


.. _events-google-cm360-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Campaign Manager 360**

.. events-google-cm360-add-destination-start

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

       **Floodlight configuration ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-cm360-floodlight-config-id-start
             :end-before: .. setting-google-cm360-floodlight-config-id-end

       **Floodlight activity ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-cm360-floodlight-activity-id-start
             :end-before: .. setting-google-cm360-floodlight-activity-id-end

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

.. events-google-cm360-add-destination-end


.. _events-google-cm360-build-query:

Build a query
==================================================

.. events-google-cm360-build-query-start

Use a query to return one row per offline conversion to send to |destination-name|. Each row must include a Google Click ID (**gclid**), a conversion timestamp, a conversion value, and a currency code. You can also include an order ID, which CM360 uses to deduplicate conversions that are re-sent across repeated runs.

The **gclid** comes from your online events or ad-click data, not from a standard Amperity table. Join that data to your transaction data to build each conversion.

.. events-google-cm360-build-query-end

.. events-google-cm360-build-query-required-start

Review the :ref:`events-google-cm360-parameters` section for the columns your query must and may return.

.. events-google-cm360-build-query-required-end

Bound the query to recent conversions so each orchestration sends new conversions instead of re-sending history; choose a window that matches how often the orchestration runs. A query that returns a collection of recent conversions for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     oe.gclid AS gclid
     ,ut.order_datetime AS conversion_timestamp
     ,ut.order_revenue AS conversion_value
     ,'USD' AS currency_code
     ,ut.order_id AS order_id
   FROM Unified_Transactions ut
   JOIN Online_Events oe ON ut.amperity_id = oe.amperity_id
   WHERE oe.gclid IS NOT NULL
     AND ut.order_datetime > (CURRENT_DATE - interval '7' day)

where:

* **gclid** is the Google Click ID from your online events or ad-click data. The ``WHERE`` clause keeps only rows that have one, because a conversion without a **gclid** cannot be sent.
* **conversion_timestamp** must be an |ext_iso_8601| instant with a UTC offset, such as ``2026-07-10T12:00:00Z``. Amperity sends it as returned by your query.
* **conversion_value** is the value CM360 bids on. To bid on delivered value, such as a predicted lifetime value, send that value here in place of the order total.
* **currency_code** is a valid |ext_iso_4217| currency code — for example, ``USD`` — that matches the currency of **conversion_value**.
* **order_id** is the deduplication key. Send a stable value so that repeated sends of the same conversion are not double-counted.


.. _events-google-cm360-data-validation:

Data validation
==================================================

.. events-google-cm360-data-validation-start

Amperity validates each row before sending and drops rows that CM360 would reject, so that one invalid row does not stop the rest of the batch. Dropped rows are reported as failed with the reason. A row is dropped when:

* **gclid**, **conversion_timestamp**, **conversion_value**, or **currency_code** is missing.
* **conversion_value** is not a number.

Column names are matched without regard to capitalization.

.. events-google-cm360-data-validation-end


.. _events-google-cm360-parameters:

Conversion fields
==================================================

.. events-google-cm360-parameters-start

The following table describes each column Amperity sends to |destination-name|. A query must return columns with the same name as listed in the "Amperity name" column; Amperity maps them to the Data Manager field names automatically.

.. list-table::
   :widths: 24 22 54
   :header-rows: 1

   * - Amperity name
     - Data Manager field
     - Description

   * - **gclid**
     - **adIdentifiers.gclid**
     - **Required**

       The Google Click ID that identifies the ad click the conversion is attributed to. Every conversion must include a **gclid**; a conversion that cannot be tied to a click cannot be sent.

   * - **conversion_timestamp**
     - **eventTimestamp**
     - **Required**

       When the conversion happened. CM360 requires an |ext_iso_8601| instant with a UTC offset — for example, ``2026-07-10T12:00:00Z``. Amperity sends the value as returned by your query, so make sure the query returns it in this form.

   * - **conversion_value**
     - **conversionValue**
     - **Required**

       The value of the conversion, as a number. Rows whose value cannot be read as a number are dropped. Send a predicted lifetime value here to have Search Ads 360 bid on delivered value.

   * - **currency_code**
     - **currency**
     - **Required**

       The currency that **conversion_value** is expressed in, as a three-character |ext_iso_4217| code.

   * - **order_id**
     - **transactionId**
     - **Optional**

       A deduplication key. When the same conversion is re-sent across repeated runs, CM360 collapses rows with the same order ID into one so the conversion is not counted twice.

.. events-google-cm360-parameters-end


.. _events-google-cm360-delivery:

Delivery and results
==================================================

.. events-google-cm360-delivery-start

CM360 accepts a batch of conversions almost immediately and then matches them in the background over a window that can range from minutes to days. Amperity treats a conversion as delivered once CM360 accepts the batch.

* A successful orchestration means CM360 accepted the conversions, not that it matched and credited them. Confirm final, per-conversion outcomes in the Campaign Manager 360 interface.
* Per-conversion failures are reported on a best-effort basis. Amperity reports the failures that CM360 returns quickly — such as an invalid or duplicate click ID — as failed rows in the orchestration's error log. Failures that CM360 surfaces only later do not appear in the orchestration.
* Amperity automatically splits large sends into batches of 2,000 conversions. This is not something you configure.
* Conversions cannot be deleted or retracted once submitted. CM360 offers no way to take back a conversion, so test with care.

.. events-google-cm360-delivery-end


.. _events-google-cm360-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-google-cm360-workflow-actions-start

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

.. events-google-cm360-workflow-actions-end

.. note:: Connection problems are caught when the destination is saved: Amperity submits a single test conversion to CM360 in a validate-only mode that writes nothing. If the check fails, the connected Google account may not be authorized, or the **Floodlight configuration ID** or **Floodlight activity ID** may be wrong or belong to an account the connected account cannot reach. During an orchestration, CM360 reports per-conversion failures by reason — an invalid or duplicate click ID, a malformed timestamp, or an unrecognized currency — and Amperity records them as failed rows with CM360's own explanation in the error log.


.. _events-google-cm360-api-reference:

Google Data Manager API reference
==================================================

.. vale off

.. events-google-cm360-api-reference-start

Amperity sends conversions to |destination-name| using the `Google Data Manager API <https://developers.google.com/data-manager/api/reference/rest/v1/events/ingest>`__ |ext_link|. Conversions are submitted through the ``events:ingest`` method.

.. events-google-cm360-api-reference-end

.. vale on
