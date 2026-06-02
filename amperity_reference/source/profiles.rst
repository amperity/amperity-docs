:orphan:

.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        Reference documentation for the Profiles page in Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Reference documentation for the Profiles page in Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Profiles


==================================================
Profiles
==================================================

.. profiles-about-start

The **Profiles** page is the primary surface for managing real-time profile collections and real-time segments.

The page has two sections: profile collections, displayed as cards, and real-time segments, displayed as a grid. Click **View details** on a collection card to open the collection detail page, where you can manage attributes, configure event assignment, and query the Profile API.

.. profiles-about-end


.. _profiles-collections:

About profile collections
==================================================

.. profiles-collections-about-start

Profile collections are the core objects on the **Profiles** page. Each collection draws identity data from a database, accepts events from one or more event streams, and exposes a set of attributes through the Profile API.

.. profiles-collections-about-end


.. _profiles-collections-list:

List of profile collections
--------------------------------------------------

.. profiles-collections-list-start

Profile collections are displayed as cards. Each card shows:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Field
     - Description

   * - **Title**
     - The display name of the collection.

   * - **Based on**
     - The database the collection draws identity data from.

   * - **Attributes**
     - The count of attributes defined for the collection.

   * - **Description**
     - An optional description. Shown in italic when empty.

   * - **View details**
     - Opens the collection detail page.

.. profiles-collections-list-end


.. _profiles-collection-detail:

Collection details
--------------------------------------------------

.. profiles-collection-detail-start

The collection detail page shows the configuration and activity for a single profile collection. The page header shows the collection title, description, and a live profile count.

.. profiles-collection-detail-end

.. profiles-collection-detail-tabs-start

The collection detail page has three tabs.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Tab
     - Description

   * - **Attributes**
     - Lists all attributes defined for the collection, grouped by category. Provides controls for adding, searching, filtering, and managing attributes.

   * - **Configuration**
     - Shows the collection's name, symbolic name, database, description, and event assignment. Both sections are editable from this tab.

   * - **Profile API viewer**
     - Provides an interactive lookup tool for querying the Profile API directly from the browser. Requires the **pii:read** permission.

.. profiles-collection-detail-tabs-end


.. _profiles-attributes:

Attributes tab
--------------------------------------------------

.. profiles-attributes-about-start

The **Attributes** tab is the primary surface for managing profile attributes within a collection. The left sidebar organizes attributes by category. The main area shows the attributes grid.

.. profiles-attributes-about-end


.. _profiles-attributes-categories:

Attribute categories
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-attributes-categories-start

The category sidebar lists all categories defined for the collection. Attributes without a category appear under **Uncategorized**, which is always shown first. User-defined categories are sorted alphabetically below it.

Each category row shows the category name and the count of attributes assigned to it. Hovering a category row reveals an actions menu with options to edit or delete the category.

The **Add category** button at the bottom of the sidebar opens the category dialog, where you provide a name and choose an icon from a set of 24 options.

When a category is deleted, its attributes move to **Uncategorized**.

.. profiles-attributes-categories-end


.. _profiles-attributes-grid:

List of attributes
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-attributes-grid-start

The attributes grid lists all attributes in the active category. Clicking a different category in the sidebar filters the grid to that category.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Column
     - Description

   * - **Attribute**
     - The display name of the attribute. Click to open the attribute detail view.

   * - **Attribute type**
     - The computation method: **Database**, **Event**, or **Computed**.

   * - **Created**
     - The date the attribute was created.

   * - **Last updated**
     - The date the attribute was last modified.

   * - **Updated by**
     - The user who last modified the attribute.

   * - **Description**
     - An optional description of the attribute.

**Search and filters**

* The search box filters the grid by attribute display name as you type.
* Click **Show filters** to reveal the filter panel. The filter panel provides a type filter that limits the grid to attributes of a selected type (**Database**, **Event**, or **Computed**). The link label changes to **Hide filters** when the panel is open.
* Click **Reset** to clear all active filters and return the grid to its unfiltered state.

**Row actions**

Each attribute row has an actions menu with the following options:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Action
     - Description

   * - **View**
     - Opens the attribute details modal, showing the name, symbolic name, description, category, and definition.

   * - **Edit**
     - Opens the attribute editor to modify the definition, including function, event type, field, condition, and timeframe.

   * - **Rename**
     - Opens a rename dialog to change the display name without affecting the symbolic name or definition.

   * - **Copy name**
     - Copies the attribute's symbolic name to the clipboard.

   * - **Delete**
     - Removes the attribute from the collection. Any segments or use cases referencing the attribute must be updated.

.. profiles-attributes-grid-end


.. _profiles-configuration:

Configuration tab
--------------------------------------------------

.. profiles-configuration-about-start

The **Configuration** tab shows two cards: **Details** and **Event assignment**. Each card has an edit button that opens a dialog.

.. profiles-configuration-about-end


.. _profiles-configuration-details:

Configuration details
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-configuration-details-start

The **Details** card shows the collection's name, symbolic name, database, and description. The database cannot be changed after the collection is created.

.. profiles-configuration-details-end


.. _profiles-configuration-event-assignment:

Events assignment
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-configuration-event-assignment-start

The **Event assignment** card shows how incoming events are linked to profiles and which event streams are enabled for the collection.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Field
     - Description

   * - **Assignment to profiles**
     - The ordered list of keychain linking keys used to match events to profiles. The first position is always ``amperity_id`` and cannot be removed. Additional keys are matched in priority order.

   * - **Event streams**
     - The event streams whose events are processed for this collection. Only events from selected streams are included.

.. profiles-configuration-event-assignment-end


.. _profiles-api-viewer:

Profile API viewer
--------------------------------------------------

.. profiles-api-viewer-about-start

The **Profile API viewer** tab lets you query the Profile API directly from the browser without writing code. It requires the **pii:read** permission.

Two lookup methods are available.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Method
     - Description

   * - **Direct lookup**
     - Retrieves a specific profile by its Amperity ID.

   * - **Keychain lookup**
     - Retrieves a profile using a keychain key and value, such as an email address or loyalty ID.

The **Retrieve enriched attributes** toggle includes computed and aggregated attribute values in the response. The **Sample cURL** block shows the equivalent command with the token redacted. The **Response** panel displays the raw JSON returned by the API.

.. profiles-api-viewer-about-end


.. _profiles-segments:

About real-time segments
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-realtime-segment-start
   :end-before: .. term-realtime-segment-end

.. profiles-segments-about-start

The **Real-time segments** section lists all real-time segments defined across all collections.

.. profiles-segments-about-end


.. _profiles-segments-list:

List of real-time segments
--------------------------------------------------

.. profiles-segments-list-start

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Column
     - Description

   * - **Name**
     - The display name of the segment. Click to open the segment in view-only mode.

   * - **Profile collection**
     - The collection this segment filters against. Click to open the collection detail page.

   * - **Profile count**
     - The number of profiles currently matching the segment.

   * - **Status**
     - The backfill status: **Queued**, **Ready**, or an in-progress indicator.

Each segment row has an actions menu with options to view, edit, copy the segment ID, or delete the segment.

.. profiles-segments-list-end


.. _profiles-segments-conditions:

Real-time conditions
--------------------------------------------------

.. profiles-segments-conditions-start

Segments are defined using a condition builder that supports both visual and expression modes. In visual mode, each condition row specifies a field, a comparison operator, and a value. Multiple conditions are joined with **and** or **or**.

Available comparison operators:

* **equals**
* **more than**
* **less than**
* **is empty**
* **is null**
* **is true**
* **is false**

The **value** input is omitted for operators that do not require a value (is empty, is null, is true, is false).

In code mode, the condition is written directly as an expression. A field reference panel on the right lists all available field names; click a name to insert it into the editor.

.. profiles-segments-conditions-end


.. _profiles-howtos:

How-tos
==================================================

.. profiles-howtos-start

Tasks related to profiles:

* :ref:`profiles-howto-add-attribute`
* :ref:`profiles-howto-add-category`
* :ref:`profiles-howto-copy-attribute-name`
* :ref:`profiles-howto-create-profile`
* :ref:`profiles-howto-delete-attribute`
* :ref:`profiles-howto-delete-category`
* :ref:`profiles-howto-edit-attribute`
* :ref:`profiles-howto-edit-category`
* :ref:`profiles-howto-edit-details`
* :ref:`profiles-howto-edit-event-assignment`
* :ref:`profiles-howto-filter-attributes`
* :ref:`profiles-howto-lookup-amperity-id`
* :ref:`profiles-howto-lookup-keychain`
* :ref:`profiles-howto-manage-realtime-segments`
* :ref:`profiles-howto-refresh-profiles`
* :ref:`profiles-howto-rename-attribute`
* :ref:`profiles-howto-search-attributes`
* :ref:`profiles-howto-view-attribute`
* :ref:`profiles-howto-view-profile`

.. profiles-howtos-end


.. _profiles-howto-add-attribute:

Add attribute
--------------------------------------------------

.. profiles-howto-add-attribute-start

Attributes define the computed values exposed through the Profile API for a given collection. Each attribute specifies a function, source event type, field, optional condition, and timeframe.

.. profiles-howto-add-attribute-end

**To add an attribute**

.. profiles-howto-add-attribute-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, click **Add attribute**.
#. Provide a name, select a category, and define the attribute using the function, event type, field, condition, and timeframe fields.
#. Click **Save**.

.. profiles-howto-add-attribute-steps-end


.. _profiles-howto-add-category:

Add category
--------------------------------------------------

.. profiles-howto-add-category-start

Categories organize attributes in the sidebar. New categories are available immediately and can be assigned to attributes when creating or editing them.

.. profiles-howto-add-category-end

**To add a category**

.. profiles-howto-add-category-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, click **Add category** at the bottom of the category sidebar.
#. Enter a name and select an icon.
#. Click **Create**.

.. profiles-howto-add-category-steps-end


.. _profiles-howto-copy-attribute-name:

Copy attribute name
--------------------------------------------------

.. profiles-howto-copy-attribute-start

Copying an attribute's symbolic name places it on the clipboard for use in expressions, API calls, or segment conditions.

.. profiles-howto-copy-attribute-end

**To copy an attribute name**

.. profiles-howto-copy-attribute-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, find the attribute.
#. Open the |fa-kebab| actions menu and click **Copy name**.

.. profiles-howto-copy-attribute-steps-end


.. _profiles-howto-create-profile:

Create profile
--------------------------------------------------

.. profiles-howto-create-profile-start

Creating a profile collection is a three-step wizard. The first step collects the collection name, title, description, and source database. The second step selects which database attributes to include. The third step configures event stream assignment and the keychain linking key priority order. The database cannot be changed after creation.

.. profiles-howto-create-profile-end

**To create a profile collection**

.. profiles-howto-create-profile-steps-start

#. On the **Profiles** page, click **Create profile**.
#. In the **Details** step, provide a **Name**, **Title**, optional **Description**, and select a **Database**. Click **Next**.
#. In the **Database attributes** step, select the attributes to include from the source table. Click **Next**.
#. In the **Events** step, select the event streams to associate with the collection and configure the keychain linking key priority order. Click **Save**.

.. profiles-howto-create-profile-steps-end


.. _profiles-howto-delete-attribute:

Delete attribute
--------------------------------------------------

.. profiles-howto-delete-attribute-start

Deleting an attribute removes it from the collection and the Profile API response. Any segments or use cases referencing the attribute must be updated.

.. profiles-howto-delete-attribute-end

**To delete an attribute**

.. profiles-howto-delete-attribute-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, find the attribute.
#. Open the |fa-kebab| actions menu and click **Delete**.
#. Confirm the deletion.

.. profiles-howto-delete-attribute-steps-end


.. _profiles-howto-delete-category:

Delete category
--------------------------------------------------

.. profiles-howto-delete-category-start

Deleting a category moves all attributes in that category to **Uncategorized**. The attributes themselves are not affected.

.. profiles-howto-delete-category-end

**To delete a category**

.. profiles-howto-delete-category-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, hover the category in the sidebar.
#. Open the |fa-kebab| actions menu and click **Delete**.
#. Confirm the deletion.

.. profiles-howto-delete-category-steps-end


.. _profiles-howto-edit-attribute:

Edit attribute
--------------------------------------------------

.. profiles-howto-edit-attribute-start

Editing an attribute lets you update its definition, including the function, source event type, field, condition, and timeframe.

.. profiles-howto-edit-attribute-end

**To edit an attribute**

.. profiles-howto-edit-attribute-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, find the attribute.
#. Open the |fa-kebab| actions menu and click **Edit**.
#. Update the definition and click **Save**.

.. profiles-howto-edit-attribute-steps-end


.. _profiles-howto-edit-category:

Edit category
--------------------------------------------------

.. profiles-howto-edit-category-start

Editing a category lets you change its display name and icon. Attributes already assigned to the category are not affected.

.. profiles-howto-edit-category-end

**To edit a category**

.. profiles-howto-edit-category-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, hover the category in the sidebar.
#. Open the |fa-kebab| actions menu and click **Edit**.
#. Update the name or icon and click **Save**.

.. profiles-howto-edit-category-steps-end


.. _profiles-howto-edit-details:

Edit collection details
--------------------------------------------------

.. profiles-howto-edit-details-start

Collection details include the display name, symbolic name, and description. The source database cannot be changed after creation.

.. profiles-howto-edit-details-end

**To edit collection details**

.. profiles-howto-edit-details-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. Click the **Configuration** tab.
#. In the **Details** card, click **Edit**.
#. Update the name or description and click **Save**.

.. profiles-howto-edit-details-steps-end


.. _profiles-howto-edit-event-assignment:

Edit event assignment
--------------------------------------------------

.. profiles-howto-edit-event-assignment-start

Event assignment controls which event streams feed the collection and how events are linked to profiles. Changes take effect on the next profile refresh.

.. profiles-howto-edit-event-assignment-end

**To edit event assignment**

.. profiles-howto-edit-event-assignment-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. Click the **Configuration** tab.
#. In the **Event assignment** card, click **Edit**.
#. Update the event stream selection or keychain linking key priority order.
#. Click **Save**.

.. profiles-howto-edit-event-assignment-steps-end


.. _profiles-howto-filter-attributes:

Filter attributes
--------------------------------------------------

.. profiles-howto-filter-attributes-start

The filter panel narrows the attributes grid by attribute type. Click **Reset** to clear all active filters.

.. profiles-howto-filter-attributes-end

**To filter attributes by type**

.. profiles-howto-filter-attributes-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, click **Show filters**.
#. Select one or more attribute types: **Database**, **Event**, or **Computed**.

The grid updates immediately. Click **Reset** to clear the filter or **Hide filters** to close the panel.

.. profiles-howto-filter-attributes-steps-end


.. _profiles-howto-lookup-amperity-id:

Look up a profile by Amperity ID
--------------------------------------------------

.. profiles-howto-lookup-amperity-id-start

The **Profile API viewer** tab lets you retrieve a specific profile by its Amperity ID without writing code. Requires the **pii:read** permission.

.. profiles-howto-lookup-amperity-id-end

**To look up a profile by Amperity ID**

.. profiles-howto-lookup-amperity-id-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. Click the **Profile API viewer** tab.
#. Select **Direct lookup**.
#. Enter the Amperity ID and click **Get profile**.

The raw JSON response appears in the **Response** panel. Enable **Retrieve enriched attributes** to include computed and aggregated attribute values.

.. profiles-howto-lookup-amperity-id-steps-end


.. _profiles-howto-lookup-keychain:

Look up a profile by keychain
--------------------------------------------------

.. profiles-howto-lookup-keychain-start

A keychain lookup retrieves a profile using a linking key name and value, such as an email address or loyalty ID. Requires the **pii:read** permission.

.. profiles-howto-lookup-keychain-end

**To look up a profile by keychain**

.. profiles-howto-lookup-keychain-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. Click the **Profile API viewer** tab.
#. Select **Keychain lookup**.
#. Enter the **Key name** and **Key value** and click **Get profile**.

The raw JSON response appears in the **Response** panel.

.. profiles-howto-lookup-keychain-steps-end


.. _profiles-howto-manage-realtime-segments:

Manage real-time segments
--------------------------------------------------

.. profiles-howto-manage-realtime-segments-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-realtime-segment-start
   :end-before: .. term-realtime-segment-end

* :ref:`profiles-howto-copy-segment-id`
* :ref:`profiles-howto-create-segment`
* :ref:`profiles-howto-delete-segment`
* :ref:`profiles-howto-edit-segment`
* :ref:`profiles-howto-view-segment`

.. profiles-howto-manage-realtime-segments-end


.. _profiles-howto-copy-segment-id:

Copy segment ID
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-howto-copy-segment-id-start

The segment ID is the unique identifier used when referencing a real-time segment in API calls.

.. profiles-howto-copy-segment-id-end

**To copy a segment ID**

.. profiles-howto-copy-segment-id-steps-start

#. On the **Profiles** page, find the segment in the **Real-time segments** list.
#. Open the |fa-kebab| actions menu and click **Copy ID**.

.. profiles-howto-copy-segment-id-steps-end


.. _profiles-howto-create-segment:

Create real-time segment
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-howto-create-segment-start

A real-time segment defines a filter condition against a profile collection. After creation, the segment is backfilled and its profile count is updated. Segments can be queried through the Profile API.

.. profiles-howto-create-segment-end

**To create a real-time segment**

.. profiles-howto-create-segment-steps-start

#. On the **Profiles** page, click **Create real-time segment**.
#. Provide a **Name** and select a **Profile** collection.
#. Build the segment condition using the visual builder or switch to **Code** mode to write an expression directly.
#. Click **Create**.

.. profiles-howto-create-segment-steps-end


.. _profiles-howto-delete-segment:

Delete real-time segment
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-howto-delete-segment-start

Deleting a real-time segment removes its definition and profile count. Any API calls that reference the segment ID will stop returning results.

.. profiles-howto-delete-segment-end

**To delete a real-time segment**

.. profiles-howto-delete-segment-steps-start

#. On the **Profiles** page, find the segment in the **Real-time segments** list.
#. Open the |fa-kebab| actions menu and click **Delete**.
#. Confirm the deletion.

.. profiles-howto-delete-segment-steps-end


.. _profiles-howto-edit-segment:

Edit real-time segment
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-howto-edit-segment-start

Editing a real-time segment lets you update the name, profile collection, and filter conditions. The segment is re-backfilled after saving.

.. profiles-howto-edit-segment-end

**To edit a real-time segment**

.. profiles-howto-edit-segment-steps-start

#. On the **Profiles** page, find the segment in the **Real-time segments** list.
#. Open the |fa-kebab| actions menu and click **Edit**.
#. Update the name, profile, or conditions.
#. Click **Save**.

.. profiles-howto-edit-segment-steps-end


.. _profiles-howto-view-segment:

View real-time segments
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profiles-howto-view-segment-start

Viewing a segment opens it in read-only mode, showing its name, profile collection, and filter conditions.

.. profiles-howto-view-segment-end

**To view a real-time segment**

.. profiles-howto-view-segment-steps-start

#. On the **Profiles** page, find the segment in the **Real-time segments** list.
#. Click the segment name, or open the |fa-kebab| actions menu and click **View**.

.. profiles-howto-view-segment-steps-end


.. _profiles-howto-refresh-profiles:

Refresh profiles
--------------------------------------------------

.. profiles-howto-refresh-profiles-start

Refreshing a collection triggers a workflow to reload profile data from the source database. Use this after making configuration changes or to force a manual update outside the automatic refresh schedule.

.. profiles-howto-refresh-profiles-end

**To refresh profiles**

.. profiles-howto-refresh-profiles-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. Click **Refresh profiles**.
#. Confirm the refresh.

.. profiles-howto-refresh-profiles-steps-end


.. _profiles-howto-rename-attribute:

Rename attribute
--------------------------------------------------

.. profiles-howto-rename-attribute-start

Renaming an attribute changes its display name without affecting its symbolic name or definition.

.. profiles-howto-rename-attribute-end

**To rename an attribute**

.. profiles-howto-rename-attribute-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, find the attribute.
#. Open the |fa-kebab| actions menu and click **Rename**.
#. Enter the new name and click **Save**.

.. profiles-howto-rename-attribute-steps-end


.. _profiles-howto-search-attributes:

Search attributes
--------------------------------------------------

.. profiles-howto-search-attributes-start

The search box filters the attributes grid by display name as you type.

.. profiles-howto-search-attributes-end

**To search for an attribute**

.. profiles-howto-search-attributes-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, type in the **Search by name** box.

The grid filters as you type. Clear the search box to return to the full list.

.. profiles-howto-search-attributes-steps-end


.. _profiles-howto-view-attribute:

View attribute details
--------------------------------------------------

.. profiles-howto-view-attribute-start

The attribute details modal shows the name, symbolic name, description, category, and full definition of an attribute.

.. profiles-howto-view-attribute-end

**To view attribute details**

.. profiles-howto-view-attribute-steps-start

#. On the **Profiles** page, click **View details** on the collection.
#. On the **Attributes** tab, find the attribute.
#. Open the |fa-kebab| actions menu and click **View**.

.. profiles-howto-view-attribute-steps-end


.. _profiles-howto-view-profile:

View a profile collection
--------------------------------------------------

.. profiles-howto-view-profile-start

The collection detail page shows the attributes, configuration, and Profile API viewer for a single profile collection.

.. profiles-howto-view-profile-end

**To view a profile collection**

.. profiles-howto-view-profile-steps-start

#. On the **Profiles** page, find the collection card.
#. Click **View details**.

.. profiles-howto-view-profile-steps-end
