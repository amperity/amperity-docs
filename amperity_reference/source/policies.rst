

.. meta::
    :description lang=en:
        Policies define how your users can interact with features and data within Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Policies define how your users can interact with features and data within Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        About policies

==================================================
About policies
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-policy-start
   :end-before: .. term-policy-end

.. policies-start

Policies may be assigned to users, along with assigning the actions that each policy represents. You may assign more than one policy to a user.

.. policies-end

.. policies-important-start

.. important:: If you see the message "Access Denied" when trying to access a page in Amperity, you may not have sufficient policies assigned to your user. See the :ref:`list of actions by policy <policies-allowed-actions>` for detailed information about the specific areas within Amperity that each policy represents.

.. policies-important-end


.. _policies-howitworks:

How policies work
==================================================

.. policies-howitworks-start

Actions within Amperity are controlled by policies, which act as containers for a set of actions. All tenants share a set of global policies with groups for standard policies and administrator policies. Each tenant assigns one or more policies to every user in their tenant, after which each user may also be assigned any of the policy options.

Each user has a set of assigned actions that are determined by their assigned policy (or policies). Policy assignment may be managed using SSO (recommended) or may be :doc:`managed from the Amperity user interface <resource_groups>` by users who are assigned the **Allow user administration** policy option.

The access model in Amperity defines actions as short strings that contain a resource type and an associated verb. A policy is a series of statements that allow or deny actions. For example: ``pii:download`` is an action. ``pii`` is the resource type and ``download`` is the associated verb. A user that is authorized to perform this action may run a query or segment, and then click the **Download** button to download the results.

When a user logs on to Amperity the policy (or policies) that are assigned to that user are identified, and are then used to determine the set of statements that allow or deny actions to that user.

.. policies-howitworks-end


.. _policies-standard:

Standard policies
==================================================

.. policies-standard-start

Standard policies are the primary policy types that are assigned to users. The following standard policies are available:

* :ref:`Amp360 User <policies-amp360-user>`
* :ref:`AmpIQ User <policies-ampiq-user>`
* :ref:`DataGrid Operator <policies-datagrid-operator>`
* :ref:`DataGrid Administrator <policies-datagrid-administrator>`

.. policies-standard-end


.. _policies-amp360-user:

Amp360 User
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-amp360-user-policy-start
   :end-before: .. term-amp360-user-policy-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-amp360-user-policy-assign-start
   :end-before: .. term-amp360-user-policy-assign-end


.. _policies-ampiq-user:

AmpIQ User
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ampiq-user-policy-start
   :end-before: .. term-ampiq-user-policy-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-ampiq-user-policy-assign-start
   :end-before: .. term-ampiq-user-policy-assign-end


.. _policies-datagrid-administrator:

DataGrid Administrator
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-datagrid-administrator-policy-start
   :end-before: .. term-datagrid-administrator-policy-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-datagrid-administrator-policy-assign-start
   :end-before: .. term-datagrid-administrator-policy-assign-end


.. _policies-datagrid-operator:

DataGrid Operator
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-datagrid-operator-policy-start
   :end-before: .. term-datagrid-operator-policy-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-datagrid-operator-policy-assign-start
   :end-before: .. term-datagrid-operator-policy-assign-end

.. policices-datagrid-operator-manual-assign-start

If users are assigned to a sandbox manually they must be assigned the **DataGrid Administrator** policy within the sandbox to allow that user full access to all features within the sandbox.

.. policices-datagrid-operator-manual-assign-end


.. _policies-policy-options:

Policy options
==================================================

.. policies-policy-options-start

Policy options are not standalone policies. They must be attached to :ref:`standard policies <policies-standard>` to allow users to perform additional actions within your tenant.

The following policy options are available:

* :ref:`Allow API key administration <policies-api-key-administrator>`
* :ref:`Allow Profile API administration <policies-profile-api-administrator>`
* :ref:`Allow sandbox administration <policies-sandbox-administrator>`
* :ref:`Allow inbound bridge credential rotation <policies-allow-inbound-bridge-credential-rotation>`
* :ref:`Allow source data deletion <policies-allow-source-data-deletion>`
* :ref:`Allow user administration <policies-allow-user-administration>`
* :ref:`Audience monetization access <policies-audience-monetization-access>`
* :ref:`Restrict AmpAI access <policies-option-restrict-ampai>`
* :ref:`Restrict data exports <policies-option-restrict-data-exports>`
* :ref:`Restrict download access <policies-option-restrict-downloads>`
* :ref:`Restrict PII access <policies-option-restrict-pii>`
* :ref:`Restrict upload access <policies-option-restrict-upload-access>`

.. policies-policy-options-end

.. policies-policy-options-note-start

.. note:: Restricted actions are indicated in the :ref:`policy table <policies-allowed-actions>` using the |no-download-policy| icon. Any user may be assigned the **Allow user administration** policy option (indicated by |manage-users-icon|).

.. policies-policy-options-note-end


.. _policies-api-key-administrator:

Allow API key administration
--------------------------------------------------

.. policies-api-key-administrator-start

The **Allow API key administration** policy option allows full access to managing the API keys and access tokens that are used with the Profile and Streaming Ingest APIs. This policy option enables the **API keys** list on the **Security** tab on the **Settings** page.

.. policies-api-key-administrator-end


.. _policies-profile-api-administrator:

Allow Profile API administration
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-profile-api-administrator-policy-start
   :end-before: .. term-profile-api-administrator-policy-end


.. _policies-sandbox-administrator:

Allow sandbox administration
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-sandbox-administrator-policy-start
   :end-before: .. term-sandbox-administrator-policy-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-sandbox-administrator-policy-assign-start
   :end-before: .. term-sandbox-administrator-policy-assign-end


.. _policies-allow-source-data-deletion:

Allow source data deletion
--------------------------------------------------

.. policies-sandbox-administrator-start

The **Allow source data deletion** policy option may be assigned to a **DataGrid Operator** to allow users assigned that policy the ability to delete domain table data from the **Sources** page.

.. policies-sandbox-administrator-end


.. _policies-allow-inbound-bridge-credential-rotation:

Allow inbound bridge credential rotation
--------------------------------------------------

.. policies-allow-inbound-bridge-credential-rotation-start

The **Allow inbound bridge credential rotation** policy option may be assigned to a **DataGrid Operator** to allow that user to upload a new credential file for an inbound bridge share from the **Sources** page.

.. policies-allow-inbound-bridge-credential-rotation-end


.. _policies-allow-user-administration:

Allow user administration
--------------------------------------------------

.. policies-allow-user-administration-start

The **Allow user administration** policy option may be assigned to users to enable access to the :ref:`Users settings tab <policies-allowed-actions-settings-users>`, the :ref:`Security settings tab (for resource groups) <policies-allowed-actions-settings-security>`, and the :ref:`Activity log settings tab <policies-allowed-actions-settings-activity-log>`.

.. policies-allow-user-administration-end


.. _policies-audience-monetization-access:

Audience monetization access
--------------------------------------------------

.. policies-audience-monetization-access-start

The **Audience monetization access** policy option may be assigned to users assigned the **Datagrid Operator** policy to enable access to the `Audience monetization <../operator/monetize_the_trade_desk_marketplace.html>`__ page.

.. policies-audience-monetization-access-end


.. _policies-option-restrict-ampai:

Restrict AmpAI access
--------------------------------------------------

.. policies-option-restrict-ampai-start

The **Restrict AmpAI access** policy option prevents users from interacting with **AmpAI** features.

.. policies-option-restrict-ampai-end


.. _policies-option-restrict-data-exports:

Restrict data exports
--------------------------------------------------

.. policies-option-restrict-data-exports-start

The **Restrict data exports** policy option prevents users from using orchestrations or campaigns.

.. policies-option-restrict-data-exports-end


.. _policies-option-restrict-downloads:

Restrict download access
--------------------------------------------------

.. policies-option-restrict-downloads-start

The **Restrict download access** policy option prevents users from downloading query and segment results.

.. policies-option-restrict-downloads-end


.. _policies-option-restrict-pii:

Restrict PII access
--------------------------------------------------

.. policies-option-restrict-pii-start

The **Restrict PII access** policy option prevents users from viewing data that is marked as PII.

This option may only be assigned to the **AmpIQ User** and **Amp360 User** policies.

.. policies-option-restrict-pii-end

.. policies-option-restrict-pii-context-start

Users of Amperity who are assigned the **AmpIQ User** and **Amp360 User** policies *along with* the :ref:`Restrict PII access <policies-option-restrict-pii>` policy option are prevented from viewing PII when that data was marked as PII in the database table.

When the **PII** checkbox is selected, the following locations will not show PII values to users who do not have permission to view PII data:

* The **Examples** page in the **Data Explorer**.
* Data that is returned by a query in the **Queries** page.
* Data that is returned by a segment in the **Segments** page.

When PII data is hidden, users are shown the following message:

::

   Some personally identifiable information has been redacted from these results.

.. policies-option-restrict-pii-context-end


.. _policies-option-restrict-upload-access:

Restrict upload access
--------------------------------------------------

.. policies-option-restrict-upload-access-start

The **Restrict upload access** policy option prevents users from uploading files to the **Customer 360**, **Queries**, or **Segments** pages.

This option may only be assigned to the **AmpIQ User** and **Amp360 User** policies.

.. policies-option-restrict-upload-access-end


.. _policies-read-only:

Read-only policies
==================================================

.. policies-read-only-start

Read-only policies are available in addition to the standard policies described in the previous section. Amperity has the following read-only policies:

* :ref:`Amp360 User - Read Only <policies-read-only-amp360-user>`
* :ref:`AmpIQ User - Read Only <policies-read-only-ampiq-user>`
* :ref:`DataGrid Operator Read Only <policies-read-only-datagrid-operator>`

.. policies-read-only-end


.. _policies-read-only-amp360-user:

Amp360 User - Read Only
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-amp360-read-only-user-policy-start
   :end-before: .. term-amp360-read-only-user-policy-end


.. _policies-read-only-ampiq-user:

AmpIQ User - Read Only
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-ampiq-read-only-user-policy-start
   :end-before: .. term-ampiq-read-only-user-policy-end


.. _policies-read-only-datagrid-operator:

DataGrid Operator Read Only
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-datagrid-operator-read-only-policy-start
   :end-before: .. term-datagrid-operator-read-only-policy-end

The **DataGrid Operator Read Only** policy allows read-only access to the **Sources**, **Stitch**, **Customer 360**, **Queries**, **Segments**, **Activations**, and **Destinations** page.


.. _policies-allowed-actions:

Actions by policy
==================================================

.. policies-allowed-actions-start

The following sections describe the set of actions that may be assigned to users of Amperity. These actions are grouped by page (:ref:`AmpAI <policies-allowed-actions-amp-ai>`, :ref:`Sources <policies-allowed-actions-sources>`, :ref:`Stitch <policies-allowed-actions-stitch>`, :ref:`Customer 360 <policies-allowed-actions-databases>`, :ref:`Queries <policies-allowed-actions-queries>`, :ref:`Segments <policies-allowed-actions-segments>`, :ref:`Campaigns <policies-allowed-actions-campaigns>`, :ref:`Journeys <policies-allowed-actions-journeys>`, :ref:`Audience Monetization <policies-allowed-actions-audience-monetization>`, :ref:`Orchestrations <policies-allowed-actions-orchestrations>`, :ref:`Destinations <policies-allowed-actions-destinations>`, :ref:`Settings <policies-allowed-actions-settings>`, :ref:`Workflows <policies-allowed-actions-workflows>`, and :ref:`Credentials <policies-allowed-actions-settings-credentials>`) with additional sections for the :ref:`Data Explorer <policies-allowed-actions-data-explorer>` and :ref:`Sandboxes <policies-allowed-actions-sandboxes>`.

.. policies-allowed-actions-end

.. policies-allowed-actions-icons-start

.. admonition:: Allowed, optional, and required actions

   The following sections use icons to indicate when actions are available.

   .. list-table::
      :widths: 8 20 72
      :header-rows: 0

      * - |policy|
        - Allowed.
        - A user assigned to this policy can perform this action.

      * - |allowed-read-only-actions-icon|
        - Read-only.
        - A user assigned to this policy has read-only access.

      * - |no-download-policy|
        - Optional.
        - This action may be restricted using the **Restrict download access** add-on policy.

      * - |no-upload-policy|
        - Optional.
        - This action may be restricted using the **Restrict upload access** add-on policy.

      * - |polino|
        - Optional.
        - This action is allowed, but visibility of data may be restricted using the **Restrict PII access** add-on policy.

      * - |polius|
        - Optional.
        - This action is allowed when a user is assigned the **User Administration** add-on policy.

      * - |poliky|
        - Optional.
        - This action is allowed when a user is assigned the **API key administration** add-on policy or the **Profile API administration** add-on policy.

      * - |policy-sandbox-allow-admin|
        - Optional.
        - This action is allowed when a **DataGrid Operator** or **DataGrid Administrator** is assigned the **Allow sandbox administration** add-on policy.

      * - |fa-rotate-right|
        - Optional.
        - This action is allowed when a **DataGrid Operator** is assigned the **Allow inbound bridge credential rotation** add-on policy.

      * - |policy-sandbox-validation-required|
        - Validation required.
        - This action is allowed *after* changes in a sandbox have passed validation and are ready to be promoted to your production tenant.

          .. important:: Only users who are assigned the **Allow sandbox administration** policy option may promote changes from a sandbox to production.

.. policies-allowed-actions-icons-end

