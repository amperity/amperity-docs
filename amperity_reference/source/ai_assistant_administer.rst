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

The experience available from the **AmpAI** button and the model used depend on the region and hosting platform for your Amperity tenant.

.. list-table::
   :widths: 20 20 35 25
   :header-rows: 1

   * - Region
     - Hosting platform
     - AmpAI experience
     - Current model
   * - United States
     - Amazon AWS
     - Customer Data Assistant
     - GPT-5.4
   * - United States
     - Microsoft Azure
     - Customer Data Assistant
     - GPT-5.4
   * - European Union
     - Microsoft Azure
     - Customer Data Assistant
     - GPT-5.4
   * - Canada
     - Amazon AWS
     - AmpGPT
     - GPT-4.1 mini
   * - Australia
     - Amazon AWS
     - AmpGPT
     - GPT-4.1 mini

The **Customer Data Assistant** requests GPT-5.4. If GPT-5.4 is not deployed in a region, Amperity routes the request to the first available model in its fallback sequence. Canada and Australia currently deploy GPT-4.1 mini only. Enabling the **Customer Data Assistant** in either region without an additional model deployment would therefore continue to use GPT-4.1 mini.

The experiences also support different workflows. For example, consider the request: "Find high-value customers who have lapsed for 90 days, create a segment for them, and build a re-engagement journey."

* The **Customer Data Assistant** can analyze the data, create and track a plan, produce a reviewable segment draft, save the segment after approval, and then draft the journey.
* **AmpGPT** can analyze the data, generate and run SQL, retry SQL errors, and return a table or visualization. It cannot create, edit, search, or save segments; create journeys; or provide the plan, artifact, and approval workflow.

.. customer-data-agent-regional-availability-end


.. _assistant-regional-availability:

Tool-specific AI Assistants
--------------------------------------------------


.. assistant-regional-availability-start

The availability of each **AmpAI** assistant depends on the hosting region for your tenant. Tenant settings and user permissions may also affect access.

For tenants hosted in Canada:

.. list-table::
   :widths: 35 30 35
   :header-rows: 1

   * - Assistant
     - Availability
     - Additional requirements
   * - Amp Insights
     - Available
     - **AmpAI** enabled for the tenant and access to the **Amps** dashboard
   * - Journeys AI Assistant
     - Not available
     - Not applicable
   * - Queries AI Assistant
     - Available
     - **AmpAI** enabled for the tenant and access to the **Queries** page
   * - Segments AI Assistant
     - Not available
     - Not applicable

Canada currently deploys GPT-4.1 mini. When an available assistant requests a model that is not deployed in Canada, Amperity routes the request to GPT-4.1 mini.

.. assistant-regional-availability-end


.. _ampai-permissions-and-policies:

Permissions and policies
==================================================

.. ampai-permissions-and-policies-start

AmpAI permissions are controlled at the user level, allowing **User Administrators** the ability to grant access to AmpAI for individual users.

AmpAI has the following user-level policy options:

#. **Restrict AmpAI access**

   Prevents users from accessing the **AmpAI** page.

#. **Restrict Queries AI Assistant access**

   Prevents users from accessing the **AmpAI Assistant** from within the **Queries** page.

#. **Restrict Segments AI Assistant access**

   Prevents users from accessing the **AmpAI Assistant** from within the **Segments** page.

#. **Allow prompt administration**

   Allows users to update the custom prompt and company context. **Datagrid Operators** and **Datagrid Administrators** always have the ability to modify prompts.

.. ampai-permissions-and-policies-end


.. _ampai-disable:

Disable AmpAI features
==================================================

.. ampai-disable-start

The **Customer Data Assistant** and the **AmpAI Assistants** can be disabled for all users. Open the **Settings** page, select the **AmpAI** tab, and then click **Disable AmpAI features**.

.. ampai-disable-end


.. _ampai-audit:

Audit conversations
==================================================

.. ampai-audit-start

**Customer Data Assistant** and **AmpAI Assistant** conversations can be audited by users assigned the **Datagrid Operator** and **Datagrid Administrator** policies from the **Settings** page.
The **AmpAI** tab on the **Settings** page logs the questions that are asked to the **Customer Data Assistant** and the **AmpAI Assistants** under **AI Conversations**.

The **Activity log** tab on the **Settings** page logs when **AmpAI Assistant** questions are asked using the "amperity.query.exec/sampled" action.

.. ampai-audit-end


.. _assistant-enable-disable:

Enable or disable AmpAI assistants
==================================================

.. assistant-enable-disable-start

AmpAI features, including **AmpAI** assistants, may be enabled (or disabled) by a user who is assigned the **DataGrid Operator** or **DataGrid Administrator** policy.

.. assistant-enable-disable-end

**To disable AmpAI assistants**

.. include:: ../../amperity_reference/source/ampai_settings.rst
   :start-after: .. settings-user-ampai-steps-start
   :end-before: .. settings-user-ampai-steps-end
