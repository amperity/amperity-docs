.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Administer the AI Assistant: regional availability, user-level permissions and policies, enabling or disabling AI Assistant features, and auditing conversations.

.. meta::
    :content class=swiftype name=body data-type=text:
        Administer the AI Assistant: regional availability, user-level permissions and policies, enabling or disabling AI Assistant features, and auditing conversations.

.. meta::
    :content class=swiftype name=title data-type=string:
        Administer the AI Assistant

==================================================
Administer the AI Assistant
==================================================

.. _ai-assistant-administer:

.. ai-assistant-administer-intro-start

Administering the **AI Assistant** covers where it is available, who can use it, how it is turned on or off for a tenant, and how conversations are audited.

.. ai-assistant-administer-intro-end


.. _ai-assistant-regional-availability:

Regional availability
==================================================

.. ai-assistant-regional-availability-intro-start

Availability varies by region and by tool. Tenant settings and user permissions may also affect access.

.. ai-assistant-regional-availability-intro-end


.. _customer-data-agent-regional-availability:

AI Assistant
--------------------------------------------------


.. customer-data-agent-regional-availability-start

The capabilities available from the **AI Assistant** button and the model used depend on the region and hosting platform for your Amperity tenant.

.. list-table::
   :widths: 35 35 30
   :header-rows: 1

   * - Region
     - Hosting platform
     - Current model
   * - United States
     - Amazon AWS
     - GPT-5.4
   * - United States
     - Microsoft Azure
     - GPT-5.4
   * - European Union
     - Microsoft Azure
     - GPT-5.4
   * - Canada
     - Amazon AWS
     - GPT-4.1 mini
   * - Australia
     - Amazon AWS
     - GPT-4.1 mini

The **AI Assistant** requests GPT-5.4. If GPT-5.4 is not deployed in a region, Amperity routes the request to the first available model in its fallback sequence. Canada and Australia currently deploy GPT-4.1 mini only. Enabling the **AI Assistant** in either region without an additional model deployment would therefore continue to use GPT-4.1 mini.

The supported workflows also differ by region. For example, consider the request: "Find high-value customers who have lapsed for 90 days, create a segment for them, and build a re-engagement journey."

* In the United States and the European Union, the **AI Assistant** can analyze the data, create and track a plan, produce a reviewable segment draft, save the segment after approval, and then draft the journey.
* In Canada and Australia, the **AI Assistant** can analyze the data, generate and run SQL, retry SQL errors, and return a table or visualization. It cannot create, edit, search, or save segments; create journeys; or provide the plan, artifact, and approval workflow.

.. customer-data-agent-regional-availability-end


.. _assistant-regional-availability:

Tool-specific AI Assistants
--------------------------------------------------


.. assistant-regional-availability-start

The availability of each tool-specific **AI Assistant** depends on the hosting region for your tenant. Tenant settings and user permissions may also affect access.

For tenants hosted in Canada:

.. list-table::
   :widths: 35 30 35
   :header-rows: 1

   * - Assistant
     - Availability
     - Additional requirements
   * - Amp Insights
     - Available
     - **AI Assistant** enabled for the tenant and access to the **Amps** dashboard
   * - Journeys AI Assistant
     - Not available
     - Not applicable
   * - Queries AI Assistant
     - Available
     - **AI Assistant** enabled for the tenant and access to the **Queries** page
   * - Segments AI Assistant
     - Not available
     - Not applicable

Canada currently deploys GPT-4.1 mini. When an available assistant requests a model that is not deployed in Canada, Amperity routes the request to GPT-4.1 mini.

.. assistant-regional-availability-end


.. _ampai-permissions-and-policies:

Permissions and policies
==================================================

.. ampai-permissions-and-policies-start

**AI Assistant** permissions are controlled at the user level, allowing **User Administrators** the ability to grant access for individual users.

The **AI Assistant** has the following user-level policy options:

#. **Restrict AI Assistant access**

   Prevents users from accessing the **AI Assistant** page.

#. **Restrict Queries AI Assistant access**

   Prevents users from accessing the **Queries AI Assistant** from within the **Queries** page.

#. **Restrict Segments AI Assistant access**

   Prevents users from accessing the **Segments AI Assistant** from within the **Segments** page.

#. **Allow prompt administration**

   Allows users to update the custom prompt and company context. **Datagrid Operators** and **Datagrid Administrators** always have the ability to modify prompts.

.. ampai-permissions-and-policies-end


.. _ampai-disable:

.. _assistant-enable-disable:

Enable or disable AI Assistant features
==================================================

.. ai-assistant-enable-disable-start

AI Assistant features, including the **AI Assistant** and all tool-specific **AI Assistants**, may be enabled (or disabled) for all users in a tenant by a user who is assigned the **DataGrid Operator** or **DataGrid Administrator** policy.

.. ai-assistant-enable-disable-end

**To disable AI Assistant features**

.. include:: ../../amperity_reference/source/ampai_settings.rst
   :start-after: .. settings-user-ampai-steps-start
   :end-before: .. settings-user-ampai-steps-end


.. _ampai-audit:

Audit conversations
==================================================

.. ampai-audit-start

**AI Assistant** and tool-specific **AI Assistant** conversations can be audited by users assigned the **Datagrid Operator** and **Datagrid Administrator** policies from the **Settings** page.
The **AI Assistant** tab on the **Settings** page logs the questions that are asked to the **AI Assistant** and the tool-specific **AI Assistants** under **AI Assistant conversations**.

The **Activity log** tab on the **Settings** page logs when tool-specific **AI Assistant** questions are asked using the "amperity.query.exec/sampled" action.

.. ampai-audit-end
