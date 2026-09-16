.. https://docs.amperity.com/contributing/


==================================================
Verbs
==================================================

.. verbs-intro-start

The right verb immediately communicates the type of action a user will take. A verb implies a single action and should never require qualifiers to distinguish it from others. Use the same verb consistently for the same actions across documentation and user interfaces.

.. admonition:: Do not use a gerund in titles, navigation, or user interface labels

   Gerunds end in *-ing* and imply the user is performing the action while reading. Most users are not. We often write this way within paragrpah and user interface strings, but do not use the gerund in titles, section headers, left-side navigations, right-side navigations, and user interface labels. For example: **Open a window**, not **Opening a window**.

   Gerunds are fine in prose. For example: "Using the **Bulk delete** action removes all selected items."

Users rely on documentation as a reference. A scannable list of action-verb titles is more useful than a list of present-participial phrases that imply the user is performing the action while reading, which is often not true.

The same verbs consistently applied in user interfaces helps reinforce those actions.

Verbs fall into natural groupings. Within a grouping, use only the verbs listed here.

.. important:: Do not introduce synonyms. For example:

   #. Use *close* not *shut*
   #. Use *delete* not *remove* when the item is permanently destroyed

.. verbs-intro-end


.. _verbs-groupings:

Groupings
==================================================

.. verbs-groupings-start

Apply the following groupings to documentation and user interfaces.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Verbs
     - Description

   * - **Add**, **Delete**, **Edit**, **View**
     - The four core operations for list-managed objects. An item exists in a list and you **Add**, **Delete**, **Edit**, or **View** it.

       These verbs together cover the full lifecycle of most objects in the application.

       Prefer **Add** over **Create** when the object appears in a list and its configuration is not complex.

   * - **Create**
     - Use **Create** instead of **Add** when the object involves a multi-step configuration process or a series of steps that are not all on one page. Creating a segment, building a query, or generating a campaign each implies setup work beyond filling in a single form.

   * - **Open**, **Close**
     - Use for user interface surfaces that appear and disappear, such as dialogs, panels, drawers, and pages within a multi-step flow. An object is

       * Opened and made visible
       * Closed and dismissed or hidden

   * - **Show**, **Hide**
     - Use for revealing or concealing content within a page without opening or closing a surface.

       A column is shown or hidden. A section of detail is shown or hidden.

       Prefer **Show** and **Hide** for in-place content visibility and **Open** and **Close** for interactive surfaces like dialogs and drawers.

   * - **Expand**, **Collapse**
     - Use for tree views, accordions, and nested sections.

       **Expand** reveals child items or additional detail.

       **Collapse** hides them.

       Similar to **Show** and **Hide** but specifically for hierarchical or sectioned content.

   * - **Enable**, **Disable**
     - Use for features, settings, and integrations that can be turned on or off without deleting them.

       **Enable** activates something that was inactive.

       **Disable** deactivates it.

   * - **Activate**, **Deactivate**
     - Use for objects such as destinations, workflows, and users that must be switched between active and inactive states.

       Similar to **Enable** and **Disable** but applied to entities rather than features or settings.

   * - **Connect**, **Disconnect**
     - Use when a service, integration, or credential is linked to or unlinked from another system.

   * - **Switch**
     - Use when moving between two defined modes, views, or states.

       **Switch** implies a toggle between named options rather than enabling or disabling a feature.

   * - **Run**, **Start**, **Stop**
     - Use for processes, jobs, and workflows that execute over time.

       **Run** is the default verb for a single execution.

       **Start** implies initiating an ongoing process.

       **Stop** ends a process that is in progress.

       .. warning:: Do not use **Abort** instead of **Stop**.

   * - **Restart**, **Rerun**, **Skip**
     - Use for workflow recovery actions.

       **Restart** resets a process from the beginning.

       **Rerun** executes a previously completed process again.

       **Skip** bypasses a specific step or task in a workflow.

   * - **Upload**, **Download**
     - Use for file transfer between a user and the application.

       **Upload** moves a file from the user to Amperity.

       **Download** moves a file from Amperity to the user.

   * - **Import**, **Export**
     - Use for structured data exchange between systems.

       **Import** brings data into Amperity.

       **Export** sends data out.

       Prefer **Upload** or **Download** for individual file operations and **Import** or **Export** for data pipeline operations.

   * - **Send**
     - Use when data is transmitted to a destination, audience, or channel on demand or as part of a campaign.

   * - **Load**, **Pull**, **Push**, **Sync**
     - Use for data pipeline operations.

       **Load** brings data into a feed or table.

       **Pull** retrieves data from a source system.

       **Push** sends data to a destination.

       **Sync** keeps two systems in alignment over time.

   * - **Browse**, **Search**, **Filter**, **Sort**
     - Use for navigation and data discovery.

       **Browse** explores available options without a specific target.

       **Search** finds a specific item by query. **Filter** narrows a list by one or more criteria.

       **Sort** reorders a list.

   * - **Select**, **Deselect**, **Click**
     - Use **Select** when a user chooses one or more items from a set: a dropdown, a list, a checkbox group.

       Use **Deselect** to remove an item from an active selection.

       Use **Click** for discrete user interface actions on a button, link, or control.

   * - **Copy**
     - Use when duplicating text, a value, or an object.

       **Copy** a URL, **Copy** a query, **Copy** a segment to another sandbox.

   * - **Convert**, **Format**, **Map**
     - Use for data transformation.

       **Convert** changes a value from one type or structure to another.

       **Format** applies a display pattern to a value.

       **Map** assigns a source field to a destination field.

   * - **Comment**, **Uncomment**
     - Use in the context of SQL or code.

       **Comment** adds a comment marker to a line or block.

       **Uncomment** removes it.

   * - **Preview**, **Compare**, **Validate**
     - Use **Preview** when showing a user what a result will look like before it is committed or run.

       Use **Compare** when displaying two versions of an object or result side by side.

       Use **Validate** when checking that something meets requirements before proceeding: validate a schema, validate credentials, validate a configuration. **Validate** implies a pass or fail check.

       **Preview** implies visual inspection.

   * - **Configure**, **Set**, **Unset**, **Apply**
     - Use for settings and properties.

       **Configure** implies a multi-property setup.

       **Set** assigns a value to a property or flag.

       **Unset** clears a property back to its default or empty state.

       **Apply** activates or submits a configuration change.

   * - **Save**, **Cancel**
     - Use at the end of a configuration or editing flow.

       **Save** commits the user's changes.

       **Cancel** abandons the in-progress action and returns the user to the previous state without saving.

       These are user interface interaction verbs and appear most often in procedural steps: "Click **Save**." and "Click **Cancel** to return without saving."

   * - **Build**, **Generate**
     - Use for output produced by a process.

       **Build** creates something from a defined set of inputs: a model, an index, a segment.

       **Generate** produces output algorithmically: a report, a query, a token.

   * - **Refresh**
     - Use when an existing view or dataset is updated from its source without a full reload. The data already exists and is being brought up to date.

   * - **Rename**, **Update**, **Replace**
     - Use for modification operations.

       **Rename** changes only the name of an object.

       **Update** changes one or more properties and is often the right verb for API operations.

       **Replace** substitutes one object or value for another entirely.

   * - **Review**
     - Use when a user is expected to examine something before taking action.

       **Review** implies deliberate inspection rather than passive viewing. **Review** a workflow, **Review** a match category result, **Review** a list of changes before committing.

   * - **Resolve**
     - Use for clearing error states, workflow holds, or data conflicts.

       A workflow task is resolved.

       A data conflict is resolved.

       **Resolve** implies that a problem existed and has been addressed.

   * - **Rotate**
     - Use for credential and key management. **Rotate** generates a new key or secret and invalidates the previous one. This is the standard term in security contexts.

   * - **Archive**
     - Use when an item is moved out of the active list but preserved and recoverable.

       **Archive** is softer than **Delete** because the item still exists.

       **Archive** is more final than **Remove** when it is no longer active.

       Use **Archive** when the application distinguishes between active and archived states.

   * - **Remove**
     - Use when an item is disassociated from a group or context but not permanently deleted. Prefer **Delete** when the item is permanently destroyed.

   * - **Organize**, **Manage**
     - Use as parent-level navigation labels or topic titles that group many sub-actions.

       **Organize** applies to arranging or structuring items.

       **Manage** applies to a broader set of lifecycle operations for a feature area.

   * - **Allow**, **Grant**, **Assign**, **Revoke**
     - Use for access control.

       **Allow** permits an action for a role or policy.

       **Grant** gives a user or role access to a resource.

       **Assign** attaches a policy or role to a user or object.

       **Revoke** removes access that was previously granted.

   * - **Use**
     - Use as a title verb when the topic explains how to apply a feature, function, or tool to accomplish a specific outcome.

       **Use** is the most common verb in reference documentation and works well for function and feature reference topics.

.. vale off

   * - **GET**, **POST**, **PUT**, **PATCH**, **DELETE**
     - Use for API endpoint documentation. HTTP method verbs appear in uppercase.

       **GET** retrieves a resource.

       **POST** creates a new resource.

       **PUT** replaces a resource entirely.

       **PATCH** updates one or more properties of a resource.

       **DELETE** removes a resource.

.. vale on

.. verbs-groupings-end


.. _verbs-modifiers:

Modifiers
==================================================

.. verbs-modifiers-start

Some verbs take a modifier that describes the scope of the action.

**Bulk** is a modifier applied to an action verb when the same action is performed on many selected items at once. The verb that follows is the action. **Bulk** describes the scope.

* Bulk delete
* Bulk move
* Bulk assign

The noun following the verb should match what is being acted on in bulk. Use **Bulk** only when the multi-item scope is different from the single-item action and worth calling out in the user interface or documentation.

.. verbs-modifiers-end


.. _verbs-avoid:

Verbs to avoid
==================================================

.. verbs-avoid-start

Some verbs are close enough to approved verbs that they create inconsistency without adding meaning. Use the approved alternative instead.

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Avoid
     - Use instead
     - Why
   * - **Abort**
     - **Stop**
     - **Abort** is not used in documentation or user interfaces. Use **Stop** even when **Abort** is the correct programmatic term.

   * - **Change**
     - **Edit**, **Update**, **Rename**
     - **Change** is too generic.

       **Edit** is the right verb when a user modifies an object's properties in the user interface.

       **Update** is the right verb for API operations.

       **Rename** is the right verb when only the name is changing.

   * - **Choose**, **Pick**
     - **Select**
     - **Select** is shorter and already established. **Choose** and **Pick** mean the same thing and add nothing.

   * - **Duplicate**
     - **Copy**
     - **Copy** and **Duplicate** mean the same thing.

       **Copy** is shorter, already in the approved list, and consistent with how the action appears in many user interfaces. Use **Copy**.

   * - **Discard**
     - **Delete**, **Remove**, **Cancel**
     - **Discard** is ambiguous about whether the item is permanently gone.

       Use **Delete** when the item is permanently destroyed, **Remove** when it is only disassociated, or **Cancel** when the user is abandoning an in-progress action without saving.

.. verbs-avoid-end
