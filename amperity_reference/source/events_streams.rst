:orphan:

.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        Reference documentation for the Event streams page in Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Reference documentation for the Event streams page in Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Event streams


==================================================
Event streams
==================================================

.. events-streams-about-start

The **Event streams** page is the primary surface for managing inbound event streams. The **Events streams** page lists all event streams in the tenant. Click a stream name to open its detail page, where you can inspect its configuration, copy the endpoint URL, view event volume, and manage event types.

.. events-streams-about-end


.. _events-streams-howitworks:

How events streams work
==================================================

.. TODO: From amperity_realtime/identity_resolution

.. identity-recognition-what-is-start

Identity recognition is the process of matching customer profile information that arrives through event streams with known customer profiles. Identity recognition relies on linking keys that correlate important identifiers in source data with customer identifiers in events. Identity recognition is the only way to associate anonymous customer activity with known profiles.

.. identity-recognition-what-is-end


.. _events-streams-howitworks-known:

Known profiles
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-known-profile-start
   :end-before: .. term-known-profile-end

.. _events-streams-howitworks-passthrough:

Passthrough profiles
++++++++++++++++++++++++++++++++++++++++++++++++++

.. identity-recognition-linking-keys-start

A linking key is an event type field that with unique customer identifiers. For example:

* Email addresses
* Phone numbers
* Loyalty IDs
* Customer IDs

All events with linking keys are compared to known profiles. When a linking key matches a value in a known profile the event associates with the known profile.

Linking keys are defined in priority order. When two or more linking keys match, the highest priority matching linking key determines the profile to which the event associates.

An event with no linking keys is still processed, but is not associated with a known profile.

.. identity-recognition-linking-keys-end


.. _events-streams-howitworks-merged:

Merged profiles
++++++++++++++++++++++++++++++++++++++++++++++++++

.. identity-recognition-outcome-passthrough-start

A linking key value matches one or more existing known profiles. The event associates with the highest-priority known profile. An anonymous profile is not created. A **Merge** outcome does not occur. **Passthrough** is the most common outcome for returning customers.

.. identity-recognition-outcome-passthrough-end

.. identity-recognition-outcome-passthrough-example-start

.. admonition:: Example of passthrough outcomes

   Record A arrives through the event stream and matches a linking key in a known profile. The event is immediately added to the esisting known profile.

   .. image:: ../../images/identity-recognition-passthrough.png
      :width: 500 px
      :alt: A passthrough outcome for identity recognition of events in an event stream
      :align: left
      :class: no-scaled-link

.. identity-recognition-outcome-passthrough-example-end

.. identity-recognition-outcome-merge-note-start

.. note:: Anonymous profiles are absorbed by known profiles after a **Merge** outcome. Any events attributed to the anonymous profile are re-attributed to the known profile.

.. identity-recognition-outcome-merge-note-end

.. identity-recognition-outcome-merge-example-start

.. admonition:: Example of merge outcomes

  Record F arrives through the event stream and matches a linking key in a known profile. Record F matches records D and E in an anonymous profile. Records D and E were previously in an :ref:`unlinked anonymous profile <events-streams-howitworks-unlinked>` A merge outcome merges all matching records, including the reconrds in the previously anonymous profile into a known profile.

   .. image:: ../../images/identity-recognition-merge.png
      :width: 500 px
      :alt: A merge outcome for identity recognition of events in an event stream
      :align: left
      :class: no-scaled-link

.. identity-recognition-outcome-merge-example-end


.. _events-streams-anonymous-records:

Anonymous profiles
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-anonymous-profile-start
   :end-before: .. term-anonymous-profile-end

.. identity-recognition-anonymous-profiles-start

An anonymous profile is created automatically when an event arrives with a linking key that does not match any known profile.

An anonymous profile is treated like a customer profile. It accumulates attribute updates and belongs to segments just like known profiles. The only difference is that anonymous profiles have no association with a known profile created by batched identity resolution. Anonymous profiles exists only within the context of events data.

Anonymous profiles are useful when they can be associated with known profiles.

.. identity-recognition-anonymous-profiles-end


.. _events-streams-howitworks-unclaimed:

Unclaimed profiles
++++++++++++++++++++++++++++++++++++++++++++++++++

.. identity-recognition-outcome-unclaimed-start

A linking key value matches a known profile, but the specific key-value pair has not been recorded for the matching profile.

A new linking key is added to the known profile and associated with the event. For example, a profile previously linked by email, but now links also with loyalty ID when loyalty events arrive.

.. identity-recognition-outcome-unclaimed-end

.. identity-recognition-outcome-unclaimed-example-start

.. admonition:: Example of unclaimed outcomes

   Event B arrives through the event stream. Event B matches record 1 on email address, but Event B *also* arrives with a loyalty ID. A loyalty ID is a strong identifier for identity recognition. An unclaimed outcome adds the loyalty ID to the linking keys for the known profile.

   .. image:: ../../images/identity-recognition-unclaimed1.png
      :width: 500 px
      :alt: An unclaimed outcome for identity recognition of events in an event stream.
      :align: left
      :class: no-scaled-link

   Event C arrives through the event stream and matches on the linking key for loyalty ID. A passthrough outcome adds event C to the known profile.

   .. image:: ../../images/identity-recognition-unclaimed2.png
      :width: 500 px
      :alt: An unclaimed outcome for identity recognition of events in an event stream.
      :align: left
      :class: no-scaled-link

.. identity-recognition-outcome-unclaimed-example-end


.. _events-streams-howitworks-unlinked:

Unlinked records
++++++++++++++++++++++++++++++++++++++++++++++++++

.. identity-recognition-outcome-unlinked-start

A linking key value does not match any existing profile. A new anonymous profile is linked to the identifier and to the associated event. Future events with this identifier will match to the anonymous profile until a **Merge** outcome associates it with a known profile.

.. identity-recognition-outcome-unlinked-end

.. identity-recognition-outcome-unlinked-example-start

.. admonition:: Example of unlinked outcomes

   Record D arrives through the event stream and does not match any known profiles. An unlinked outcome creates an anonymous profile with only record D.

   .. image:: ../../images/identity-recognition-unlinked1.png
      :width: 500 px
      :alt: An unlinked outcome for identity recognition of events in an event stream.
      :align: left
      :class: no-scaled-link

   Record E arrives through the event stream and does not match any known profiles. Record E matches record D on an anonymous identifier. An unlinked outcome adds record E to the anonymous profile with record D.

   .. image:: ../../images/identity-recognition-unlinked2.png
      :width: 500 px
      :alt: An unlinked outcome for identity recognition of events in an event stream.
      :align: left
      :class: no-scaled-link

   Record F arrives through the event stream and matches a linking key in a known profile. A :ref:`merge outcome <events-streams-howitworks-merged>` merges the anonymous records to a known profile.

.. identity-recognition-outcome-unlinked-example-end


.. _events-streams-list:

Event streams list
==================================================

.. events-streams-list-start

The event streams list shows all event streams in the tenant.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Column
     - Description

   * - **Title**
     - The display name of the stream. Click to open the stream detail page.

   * - **Mode**
     - The current operating mode of the stream: **Active**, **Drop**, or **Reject**. See :ref:`events-streams-mode`.

.. events-streams-list-end


.. _events-streams-detail:

Event stream detail
==================================================

.. events-streams-detail-start

The event stream detail page shows the configuration and current activity for a single stream.

.. events-streams-detail-end


.. _events-streams-detail-panel:

Details panel
--------------------------------------------------

.. events-streams-detail-panel-start

The details panel appears at the top of the stream detail page and shows the following fields.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Field
     - Description

   * - **Endpoint ID**
     - The stream ID, in ``esm-`` format. This is the unique identifier used in API calls and environment variable configuration.

   * - **Mode**
     - The current stream mode. See :ref:`events-streams-mode`.

   * - **HTTP URL**
     - The full endpoint URL for sending events to this stream. Use this URL as the ``POST`` target in relay functions and upstream webhook configuration. Click the copy icon to copy it to the clipboard.

   * - **Symbolic name**
     - The lowercase system name assigned to the stream (``[a-z_][a-z_0-9]*``). This name is used in generated table names and internal references.

.. events-streams-detail-panel-end


.. _events-streams-stats:

Stats cards
--------------------------------------------------

.. events-streams-stats-start

The stats bar shows rolled-up event counts for the stream over the past 30 days.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Card
     - Description

   * - **Total**
     - All events received by the stream.

   * - **Unrecognized**
     - Events that did not match any configured event type routing expression.

   * - **Ignored**
     - Events that were received and matched an event type but were discarded without processing.

   * - **Invalid**
     - Events that matched an event type but failed field validation--for example, a required field was missing or a value could not be coerced to the declared type.

   * - **Valid**
     - Events that matched an event type and passed all field validation. These events were written to the profile pipeline.

.. events-streams-stats-end


.. _events-streams-overview:

Overview
--------------------------------------------------

.. events-streams-overview-start

The **Overviews** tab shows an event volume chart for the stream and the list of event types configured for it. The **Add event type** button is available here for users with write access.

.. events-streams-overview-end


.. _events-streams-samples:

Samples
--------------------------------------------------

.. events-streams-samples-start

The **Samples** tab shows a sample of recently received raw event payloads. Requires the **pii:read** permission. Use the **Event type** dropdown to filter by a specific event type and the **Status** dropdown to filter by Any status, Valid, Invalid, Ignored, or Unknown. Use sample events to inspect field names and JSON structure before writing field expressions.

.. events-streams-samples-end


.. _events-streams-mode:

Stream modes
==================================================

.. events-streams-mode-start

Each event stream has an operating mode that determines how incoming events are handled.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Mode
     - Description

   * - **Active**
     - Events are accepted and forwarded to the profile pipeline for processing. This is the default mode for newly created streams.

   * - **Drop**
     - Events are accepted (the stream returns **202**) but discarded without processing. Use this mode to pause ingest while keeping the upstream source configured and sending.

   * - **Reject**
     - The stream returns **409 Conflict** and does not accept events. Use this mode to block ingest entirely.

.. events-streams-mode-end


.. _events-streams-settings-dialog:

Settings dialog
==================================================

.. events-streams-settings-dialog-start

The settings dialog opens automatically after stream creation and is also accessible from the **Edit event stream** button on the detail page. It has two sections.

**Endpoint configuration**

Shows the values needed to configure an upstream relay or webhook source.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Field
     - Description

   * - **HTTP ENDPOINT**
     - The full endpoint URL for the stream. Read-only. Click the copy icon to copy it to the clipboard.

   * - **API KEY**
     - A dropdown listing API keys with the **Real-time API data access** policy. Select a key, then click **Get token** to generate a bearer token. Selecting **My user token** uses the current user's session token, which is suitable for testing but not for production relays.

**Stream configuration**

Editable stream settings including name, description, mode, event type recognition method, default timestamp field, and linked profile collections.

.. events-streams-settings-dialog-end


.. _events-streams-howtos:

How-tos
==================================================

.. events-streams-howtos-start

Tasks related to event streams:

* :ref:`events-streams-howto-add-event-type`
* :ref:`events-streams-howto-change-mode`
* :ref:`events-streams-howto-create`
* :ref:`events-streams-howto-delete`
* :ref:`events-streams-howto-edit`
* :ref:`events-streams-howto-get-endpoint-url`
* :ref:`events-streams-howto-get-token`
* :ref:`events-streams-howto-revoke-credentials`
* :ref:`events-streams-howto-test-event`
* :ref:`events-streams-howto-view`
* :ref:`events-streams-howto-view-samples`

.. events-streams-howtos-end


.. _events-streams-howto-create:

Create event stream
--------------------------------------------------

.. events-streams-howto-create-start

Creating an event stream is a two-step flow. The setup dialog collects the stream name, description, and API key. After the stream is created, the settings dialog opens automatically and provides the endpoint URL and token generation controls.

.. events-streams-howto-create-end

**To create an event stream**

.. events-streams-howto-create-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page. On the **Events streams** page click **Create event stream**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - In the setup dialog, provide a **Name** (``[a-z_][a-z_0-9]*``), an optional **Description**, and select or create an **API key** with the **Real-time API data access** policy. Click **Save**.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - The settings dialog opens automatically. Copy the **HTTP ENDPOINT** URL and click **Get token** to generate a bearer token. Store the token in a secure secrets manager before closing the dialog.

.. events-streams-howto-create-steps-end


.. _events-streams-howto-view:

View a stream
--------------------------------------------------

.. events-streams-howto-view-start

The stream detail page shows the stream's configuration, endpoint URL, event volume, and event types.

.. events-streams-howto-view-end

**To view an event stream**

.. events-streams-howto-view-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. Click the stream name to open the stream detail page.

.. events-streams-howto-view-steps-end


.. _events-streams-howto-edit:

Edit event stream
--------------------------------------------------

.. events-streams-howto-edit-start

The settings dialog lets you update the stream name, description, mode, recognition method, default timestamp field, and linked profile collections.

.. events-streams-howto-edit-end

**To edit an event stream**

.. events-streams-howto-edit-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. Click **Edit event stream**.
#. Update the stream name, description, mode, recognition method, timestamp field, or linked profile collections as needed.
#. Click **Save** when the settings are unchanged to close, or **Save** after making changes to apply them.

.. events-streams-howto-edit-steps-end


.. _events-streams-howto-delete:

Delete event stream
--------------------------------------------------

.. events-streams-howto-delete-start

Deleting an event stream removes its configuration and associated event types. Events sent to the stream endpoint after deletion are not accepted.

.. events-streams-howto-delete-end

**To delete an event stream**

.. events-streams-howto-delete-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. On the **Event streams** page, find the stream to delete.
#. Open the |fa-kebab| actions menu and click **Delete**.
#. Confirm the deletion.

.. events-streams-howto-delete-steps-end


.. _events-streams-howto-get-endpoint-url:

Get endpoint URL
--------------------------------------------------

.. events-streams-howto-get-endpoint-url-start

The endpoint URL is the POST target for upstream webhook sources and relay functions. It is assigned when the stream is created and does not change.

.. events-streams-howto-get-endpoint-url-end

**To get the endpoint URL**

.. events-streams-howto-get-endpoint-url-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. On the **Event streams** page, click the stream name.
#. Click **Edit event stream** to open the settings dialog.
#. Copy the **HTTP ENDPOINT** URL.

.. events-streams-howto-get-endpoint-url-steps-end


.. _events-streams-howto-get-token:

Get access token
--------------------------------------------------

.. events-streams-howto-get-token-start

The access token is a bearer token used in the ``Authorization`` header when sending events to the stream. Tokens are generated from an API key with the **Real-time API data access** policy. Tokens do not expire on a schedule but can be revoked or regenerated at any time.

.. events-streams-howto-get-token-end

**To get an access token**

.. events-streams-howto-get-token-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. On the **Event streams** page, click the stream name.
#. Click **Edit event stream** to open the settings dialog.
#. Select an API key from the **API KEY** dropdown.
#. Click **Get token** to generate a bearer token.
#. Copy the token and store it in a secure secrets manager.

.. events-streams-howto-get-token-steps-end


.. _events-streams-howto-revoke-credentials:

Revoke credentials
--------------------------------------------------

.. events-streams-howto-revoke-credentials-start

Revoking credentials immediately invalidates bearer tokens and OAuth credentials for an API key. Two options are available: revoke only the credentials issued before the last rotation, leaving the current active credentials valid; or revoke all credentials immediately, which will cause any relay function using the key to stop sending events until it is updated with a new token.

Credentials are managed from the **Security** tab under **Settings**, not from the event stream page.

.. events-streams-howto-revoke-credentials-end

**To revoke credentials**

.. events-streams-howto-revoke-credentials-steps-start

#. Open **Settings** and click the **Security** tab.
#. Find the API key and open the |fa-kebab| actions menu.
#. Click **Revoke credentials**.
#. Select an option:

   * **Revoke old credentials** -- invalidates credentials issued before the last rotation. Active credentials remain valid.
   * **Revoke all credentials** -- immediately invalidates all credentials, including active ones.

#. Confirm the revocation.

.. events-streams-howto-revoke-credentials-steps-end


.. _events-streams-howto-change-mode:

Change stream mode
--------------------------------------------------

.. events-streams-howto-change-mode-start

The stream mode controls whether incoming events are processed, silently dropped, or rejected. See :ref:`events-streams-mode` for a description of each mode.

.. events-streams-howto-change-mode-end

**To change the stream mode**

.. events-streams-howto-change-mode-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. On the **Event streams** page, click the stream name.
#. Click **Edit event stream**.
#. Under **Stream configuration**, select a new **Mode**: **Active**, **Drop**, or **Reject**.
#. Click **Save**.

.. events-streams-howto-change-mode-steps-end


.. _events-streams-howto-add-event-type:

Add event type
--------------------------------------------------

.. events-streams-howto-add-event-type-start

Event types are configured per stream. Adding an event type opens the event type editor on the stream's **Overview** tab.

.. events-streams-howto-add-event-type-end

**To add an event type to a stream**

.. events-streams-howto-add-event-type-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. On the **Event streams** page, click the stream name.
#. On the **Overview** tab, click **Add event type**.
#. Provide a name and configure the event type fields.
#. Click **Save**.

See :ref:`events-types-howto-add` for the full event type creation steps.

.. events-streams-howto-add-event-type-steps-end


.. _events-streams-howto-view-samples:

View sample events
--------------------------------------------------

.. events-streams-howto-view-samples-start

The **Samples** tab shows a sample of recently received raw event payloads. Viewing samples requires the **pii:read** permission.

.. events-streams-howto-view-samples-end

**To view sample events for a stream**

.. events-streams-howto-view-samples-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. On the **Event streams** page, click the stream name.
#. Click the **Samples** tab.

Use the event type and state dropdowns to filter the sample list. Click any event to expand its raw JSON payload.

.. events-streams-howto-view-samples-steps-end


.. _events-streams-howto-test-event:

Send a test event
--------------------------------------------------

.. events-streams-howto-test-event-start

The **Quick start** expander on the stream detail page lets you send a test event directly from the browser and copy the equivalent cURL command. Use this to verify stream credentials and confirm that events are arriving before connecting an upstream source.

.. events-streams-howto-test-event-end

**To send a test event**

.. events-streams-howto-test-event-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event streams** page.
#. On the **Event streams** page, click the stream name.
#. Expand the **Quick start** section.
#. Edit the JSON payload to match a representative event from your upstream source.
#. Click **Post event** to send the payload to the stream.
#. To get the equivalent cURL command, click the copy icon next to the cURL snippet.

.. events-streams-howto-test-event-steps-end
