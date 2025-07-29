.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        AmpAI provides marketers, analysts, and data engineers with an AI-powered toolkit for smarter decision-making.

.. meta::
    :content class=swiftype name=body data-type=text:
        AmpAI provides marketers, analysts, and data engineers with an AI-powered toolkit for smarter decision-making.

.. meta::
    :content class=swiftype name=title data-type=string:
        About AmpAI

==================================================
About AmpAI
==================================================

.. ampai-overview-start

**AmpAI** enables brands to ask and answer complex questions about their customers, with support for visualizations. **AmpAI** operates over the data in the database and takes natural language questions and converts them into SQL.

**AmpAI** supports customization through custom prompting capabilities. This enables organizations to encode specific business logic and defintions, tailoring **AmpAI** to align with their business requirements and ensuring consistency in results.

**AmpAI** offers enterprise-grade privacy and security and is built on the Azure OpenAI Service.

To enhance response accuracy, **AmpAI** leverages tenant-specific information, such as schema metadata, database field descriptions, and usage patterns to refine its understanding and to improve the relevance and precision of results.

**AmpAI** enforces user-level permissions, allowing granular control over access.

.. ampai-overview-end


.. _ampai-good-results:

Getting good results with AmpAI
==================================================

.. ampai-good-results-start

To achieve optimal results when using **AmpAI**, follow these best practices for structing your prompts:

* **Understand the question's scope**

  Clearly define the scope of your question to avoid ambiguous results. For example, specify the timeframe, customer segments, or metrics you are analyzing.

* **Avoid overloading**

  Focus on one primary question or task per prompt to ensure clarity and to avoid confusing results.

  For example, instead of asking how the demographics of omnichannel customers compare to single-channel customers, ask a question first about omnichannel customer demographics, and then ask a second question about single-channel customer demographics.

* **Use consistent terminology**

  Stick to terminology used in your schema and business logic to align with how **AmpAI** understands your data.

* **Update the custom prompt often**

  The custom prompt is a powerful tool. Update the custom prompt whenever you get a result that doesn't align with the way your business views the world.

.. ampai-good-results-end


.. _ampai-custom-prompt:

About the custom prompt
==================================================

.. ampai-custom-prompt-start

The custom prompt in **AmpAI** enables your brand to tailor responses to align with specific business logic. Custom prompts apply to all user queries within AmpAI and can be updated to include:

* Customer definitions, such as defining how your brand interprets retention metrics
* Priority tables and fields, such as specifying priority for default tables and fields that are used with loyalty-related queries
* Exclusions, such as automatically excluding employees or outliers from analysis
* Default customer identifiers
* Fiscal calendar information

While **AmpAI** works effectively out of the box, updating the custom prompt is often necessary to keep AmpAI aligned with how your brand understands your customers. The custom prompt should be updated when an AmpAI response does not meet expectations.

.. ampai-custom-prompt-end


.. _ampai-configure:

Configure AmpAI
==================================================

.. ampai-configure-start

When your brand starts using AmpAI you should start with a list of 3-5 key customer questions that AmpAI should answer correctly. Test these questions, and then refine the custom prompt to ensure accurate and meaningful responses. This will help establish an effective first iteration of the custom prompt.

.. ampai-configure-end


.. _ampai-configure-custom-prompt:

Custom prompt iteration
--------------------------------------------------

.. ampai-configure-custom-prompt-start

AmpAI supports two types of prompts for customization and iteration:

#. **Production prompt**

   The production prompt applies universally to all users and queries within AmpAI. Any changes to this prompt should be deliberate and well-tested using the draft prompt.

#. **Draft prompt**

   The draft prompt is a testing environment where changes can be made and evaluated without affecting all users. Changes to the draft prompt only apply to your specific instance of AmpAI and not to any other users.

   Use the draft prompt to test modifications until the changes are ready for deployment.

   Click "Revert prompt" to revert the draft prompt to the current version of the production prompt.

   Click "Activate draft" to update the production prompt to match the current version of the draft prompt. This will make the updates available to all users. 

To maximize the effectiveness of custom prompts:

* **Be specific**

  Reference exact field names, values, and table names whenever possible to ensure precise results.

* **Use SQL**

  For complex logic, including SQL statements within the custom prompt can clarify definitions. For example, a SQL query that defines retained customers if specific logic applies.

* **Test iteratively**

  Make small incremental changes to the custom prompt and test after each modification to help identify what works and what needs additional refinement.

.. ampai-configure-custom-prompt-end


.. _ampai-permissions-and-policies:

Permissions and policies
==================================================

.. ampai-permissions-and-policies-start

AmpAI permissions are controlled at the user level, allowing **User Administrators** the ability to grant access to AmpAI for individual users.

There are three user-level policy options associated with AmpAI:

#. **Restrict AmpAI access**

   Prevents users from accessing the **AmpAI** page.

#. **Restrict AmpAI Assistant access**

   Prevents users from accessing the **AmpAI Assistant** from within the **Queries** page.

#. **Enable prompt administration**

   Allows users to update the custom prompt. By default, this policy option is enabled for users assigned the **Datagrid Operator** and **Datagrid Administrator** policies.

.. ampai-permissions-and-policies-end


.. _ampai-disable:

Disable AmpAI features
==================================================

.. ampai-disable-start

**AmpAI** and the **AmpAI Assistant** can be disabled for all users. Open the **Settings** page, select the **AmpAI** tab, and then click **Disable AmpAI features**.

.. ampai-disable-end


.. _ampai-audit:

Audit conversations
==================================================

.. ampai-audit-start

**AmpAI** and **AmpAI Assistant** conversations can be audited by users assigned the **Datagrid Operator** and **Datagrid Administrator** policies from the **Settings** page.

The **AmpAI** tab on the **Settings** page logs the questions that are asked to **AmpAI** and the **AmpAI Assistant** under **AI Conversations**.

The **Activity log** tab on the **Settings** page logs when **AmpAI Assistant** questions are asked using the "amperity.query.exec/sampled" action.

.. ampai-audit-end
