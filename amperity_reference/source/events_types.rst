:orphan:

.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        Reference documentation for the Event types page in Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Reference documentation for the Event types page in Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Event types


==================================================
Event types
==================================================

.. events-types-about-start

The **Event types** page shows all event types configured across every event stream in the tenant. Event types define the structure of events a stream accepts: what field names to extract from the incoming JSON, how to type those fields, and which fields act as keychain linking keys. Each event type is scoped to a single event stream. To add a new event type, open the stream's detail page and click **Add event type** on the **Overview** tab.

.. events-types-about-end


.. _events-types-stats:

Stats cards
==================================================

.. events-types-stats-start

The stats bar at the top of the page shows 30-day event counts rolled up across all event streams and all event types. The same five cards appear on the :ref:`individual stream detail page <events-streams-stats>`, where counts are scoped to that stream.

.. events-types-stats-end


.. _events-types-stats-total:

Total
--------------------------------------------------

.. events-types-stats-total-start

The total number of events received across all streams in the past 30 days. This is the gross inbound count before any routing or validation is applied.

.. events-types-stats-total-end


.. _events-types-stats-unrecognized:

Unrecognized
--------------------------------------------------

.. events-types-stats-unrecognized-start

Events that arrived at a stream but did not match the routing expression of any configured event type. Unrecognized events are not written to any event type table and do not reach the profile pipeline.

A high unrecognized count typically means the stream is receiving events with an event name or type field value that does not match any routing expression--or that event types have not yet been configured for the stream.

.. events-types-stats-unrecognized-end


.. _events-types-stats-ignored:

Ignored
--------------------------------------------------

.. events-types-stats-ignored-start

Events that were received and matched an event type but were discarded without being processed. Ignored events are accepted by the stream (the endpoint returns **202**) and counted, but are not written to the profile pipeline.

.. events-types-stats-ignored-end


.. _events-types-stats-invalid:

Invalid
--------------------------------------------------

.. events-types-stats-invalid-start

Events that matched an event type but failed field validation. Common causes:

* A required field was absent from the event payload.
* A field value could not be coerced to the declared data type--for example, a string that cannot be parsed as a decimal.
* The event body exceeded the 64 KB per-event size limit.

Invalid events are not written to the profile pipeline. Inspect sample events using the **Samples** tab on the event type detail page to diagnose validation failures.

.. events-types-stats-invalid-end


.. _events-types-stats-valid:

Valid
--------------------------------------------------

.. events-types-stats-valid-start

Events that matched an event type, passed all field validation, and were written to the profile pipeline. Valid events are the billable ingest count and the source of data for profile attributes and segments.

.. events-types-stats-valid-end


.. _events-types-grid:

Event types grid
==================================================

.. events-types-grid-start

The grid lists every event type across all streams. Each row shows the event type name and per-type event counts for the past 30 days.

**Search and filters**

* A search box filters the grid by event type name.
* Click **Show filters** to reveal the stream picklist. Select one or more streams to limit the grid to event types belonging to those streams. The filter control shows the number of active filters when the filter panel is hidden.
* The grid paginates at 100 rows per page.

Click an event type name to open the event type detail page.

.. events-types-grid-end


.. _events-types-detail:

Event type detail
==================================================

.. events-types-detail-start

The event type detail page shows the configuration and activity for a single event type.

.. events-types-detail-end


.. _events-types-detail-panel:

Details
--------------------------------------------------

.. events-types-detail-panel-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Field
     - Description

   * - **Stream**
     - The event stream this type belongs to. Click the link to open the stream detail page.

   * - **Symbolic name**
     - The lowercase system name for this event type (``[a-z_][a-z_0-9]*``). This name is used in generated table names.

.. events-types-detail-panel-end


.. _events-types-detail-tabs:

Tabs
--------------------------------------------------

.. events-types-detail-tabs-start

The event type detail page has three tabs.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Tab
     - Description

   * - **Overview**
     - Contains two sections. **Event volume** shows a bar chart of daily event counts for the past 7, 14, or 30 days, broken down by Invalid, Valid, and Ignored states. Clicking a bar opens the **Samples** tab filtered to that event state. **Associated attributes** lists profile attributes sourced from this event type; each row has an actions menu with options to view, edit, rename, copy the name, or delete the attribute.

   * - **Samples**
     - Shows a sample of recently received raw event payloads that matched this event type. Requires the **pii:read** permission. Use the **Status** dropdown to filter by Any status, Valid, Invalid, Ignored, or Unknown. Use samples to inspect actual field names and JSON nesting before writing or updating field expressions.

   * - **Properties**
     - Shows the field schema defined for this event type: the property name, JSON path expression, data type, and keychain linking key assignment for each field.

.. events-types-detail-tabs-end


.. _events-types-howtos:

How-tos
==================================================

.. events-types-howtos-start

Tasks related to event types:

* :ref:`events-types-howto-add`
* :ref:`events-types-howto-delete`
* :ref:`events-types-howto-delete-attribute`
* :ref:`events-types-howto-edit`
* :ref:`events-types-howto-edit-attribute`
* :ref:`events-types-howto-filter-by-stream`
* :ref:`events-types-howto-filter-samples-status`
* :ref:`events-types-howto-rename-attribute`
* :ref:`events-types-howto-search`
* :ref:`events-types-howto-view`
* :ref:`events-types-howto-view-attribute`
* :ref:`events-types-howto-view-properties`
* :ref:`events-types-howto-view-samples`

.. events-types-howtos-end


.. _events-types-howto-add:

Add event type
--------------------------------------------------

.. events-types-howto-add-start

Event types are scoped to a stream. To add an event type, open the stream's detail page first.

.. events-types-howto-add-end

**To add an event type**

.. events-types-howto-add-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page on the **Overview** tab, click **Add event type**.
#. Provide a **Name** (``[a-z_][a-z_0-9]*``) and an optional **Idempotency key**.
#. Define the fields for this event type.
#. Click **Save**.

.. events-types-howto-add-steps-end


.. _events-types-howto-view:

View an event type
--------------------------------------------------

.. events-types-howto-view-start

The event type detail page shows the event type's field schema, event volume, and associated profile attributes.

.. events-types-howto-view-end

**To view an event type**

.. events-types-howto-view-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name to open its detail page.

.. events-types-howto-view-steps-end


.. _events-types-howto-edit:

Edit event type
--------------------------------------------------

.. events-types-howto-edit-start

Editing an event type lets you update the name, idempotency key, and field definitions.

.. events-types-howto-edit-end

**To edit an event type**

.. events-types-howto-edit-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name to open its detail page.
#. Click **Edit event type**.
#. Update the name, idempotency key, or field definitions as needed.
#. Click **Save**.

.. events-types-howto-edit-steps-end


.. _events-types-howto-delete:

Delete event type
--------------------------------------------------

.. events-types-howto-delete-start

Deleting an event type removes its field definitions and stops routing incoming events to it. Events that previously matched this type will become unrecognized.

.. events-types-howto-delete-end

**To delete an event type**

.. events-types-howto-delete-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name.
#. Open the |fa-kebab| actions menu and click **Delete event type**.
#. Confirm the deletion.

.. events-types-howto-delete-steps-end


.. _events-types-howto-search:

Search event types
--------------------------------------------------

.. events-types-howto-search-start

The search box filters the grid by event type name as you type.

.. events-types-howto-search-end

**To search for an event type**

.. events-types-howto-search-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, type in the search box above the grid.

The grid filters to event types whose names match the search text as you type.

.. events-types-howto-search-steps-end


.. _events-types-howto-filter-by-stream:

Filter event types by stream
--------------------------------------------------

.. events-types-howto-filter-start

The stream filter limits the grid to event types belonging to one or more selected streams.

.. events-types-howto-filter-end

**To filter event types by stream**

.. events-types-howto-filter-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click **Show filters**.
#. In the **Stream** picklist, select one or more streams.

The grid updates immediately. To clear the filter, click **Reset** in the filters panel or deselect all streams in the picklist.

.. events-types-howto-filter-steps-end


.. _events-types-howto-view-properties:

View event type properties
--------------------------------------------------

.. events-types-howto-view-properties-start

The **Properties** tab shows the complete field schema for the event type: property names, JSON path expressions, data types, and keychain linking key assignments.

.. events-types-howto-view-properties-end

**To view the field schema for an event type**

.. events-types-howto-view-properties-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name.
#. Click the **Properties** tab.

The table shows each defined field with its JSON path expression, data type, and keychain linking key assignment.

.. events-types-howto-view-properties-steps-end


.. _events-types-howto-view-samples:

View sample events
--------------------------------------------------

.. events-types-howto-view-samples-start

Sample events show the raw JSON payloads of recently received events that matched this event type. Samples require the **pii:read** permission.

.. events-types-howto-view-samples-end

**To view sample events for an event type**

.. events-types-howto-view-samples-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name.
#. Click the **Samples** tab.

Use the sample payloads to verify that field expressions reference the correct paths and that field values are arriving in the expected format.

.. events-types-howto-view-samples-steps-end


.. _events-types-howto-filter-samples-status:

Filter samples by status
--------------------------------------------------

.. events-types-howto-filter-samples-start

The **Status** dropdown on the **Samples** tab filters the sample list to events in a specific state. Available options are Any status, Valid, Invalid, Ignored, and Unknown.

.. events-types-howto-filter-samples-end

**To filter sample events by status**

.. events-types-howto-filter-samples-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name.
#. Click the **Samples** tab.
#. Use the **Status** dropdown to select a state: **Valid**, **Invalid**, **Ignored**, or **Unknown**.

To return to the unfiltered list, select **Any status**.

.. events-types-howto-filter-samples-steps-end


.. _events-types-howto-view-attribute:

View attribute details
--------------------------------------------------

.. events-types-howto-view-attribute-start

The **Associated attributes** section on the **Overview** tab lists profile attributes sourced from this event type. Opening an attribute shows its name, symbolic name, description, category, and definition.

.. events-types-howto-view-attribute-end

**To view attribute details**

.. events-types-howto-view-attribute-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name.
#. On the **Overview** tab, find the attribute in the **Associated attributes** list.
#. Open the |fa-kebab| actions menu and click **View**.

.. events-types-howto-view-attribute-steps-end


.. _events-types-howto-edit-attribute:

Edit an attribute
--------------------------------------------------

.. events-types-howto-edit-attribute-start

Editing an attribute lets you update its definition, including the function, event type, field, condition, and timeframe used to compute it.

.. events-types-howto-edit-attribute-end

**To edit an attribute**

.. events-types-howto-edit-attribute-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name.
#. On the **Overview** tab, find the attribute in the **Associated attributes** list.
#. Open the |fa-kebab| actions menu and click **Edit**.
#. Update the definition as needed and click **Save**.

.. events-types-howto-edit-attribute-steps-end


.. _events-types-howto-rename-attribute:

Rename an attribute
--------------------------------------------------

.. events-types-howto-rename-attribute-start

Renaming an attribute changes its display name without affecting its symbolic name or definition.

.. events-types-howto-rename-attribute-end

**To rename an attribute**

.. events-types-howto-rename-attribute-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name.
#. On the **Overview** tab, find the attribute in the **Associated attributes** list.
#. Open the |fa-kebab| actions menu and click **Rename**.
#. Enter the new name and click **Save**.

.. events-types-howto-rename-attribute-steps-end


.. _events-types-howto-delete-attribute:

Delete an attribute
--------------------------------------------------

.. events-types-howto-delete-attribute-start

Deleting an attribute removes it from the profile pipeline. Any segments or campaigns that reference the attribute will need to be updated.

.. events-types-howto-delete-attribute-end

**To delete an attribute**

.. events-types-howto-delete-attribute-steps-start

#. Expand the **Events** menu in the left-side navigation, and then open the **Event types** page.
#. On the **Event types** page, click the event type name.
#. On the **Overview** tab, find the attribute in the **Associated attributes** list.
#. Open the |fa-kebab| actions menu and click **Delete**.
#. Confirm the deletion.

.. events-types-howto-delete-attribute-steps-end
