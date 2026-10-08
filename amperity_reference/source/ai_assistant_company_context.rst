.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Company context is a library of reference documents that the AI Assistant searches when a question involves business-specific knowledge, so responses are grounded in your actual business.

.. meta::
    :content class=swiftype name=body data-type=text:
        Company context is a library of reference documents that the AI Assistant searches when a question involves business-specific knowledge, so responses are grounded in your actual business.

.. meta::
    :content class=swiftype name=title data-type=string:
        Company context

==================================================
Company context
==================================================

.. _ampai-company-context:

.. include:: ../../amperity_reference/source/ai_assistant_custom_prompts.rst
   :start-after: .. ai-assistant-prompts-page-start
   :end-before: .. ai-assistant-prompts-page-end

.. include:: ../../amperity_reference/source/ai_assistant_custom_prompts.rst
   :start-after: .. ai-assistant-prompts-workflow-start
   :end-before: .. ai-assistant-prompts-workflow-end

.. ai-assistant-company-context-definition-start

* **Company context** is a library of reference documents that the assistant searches only when a question involves business-specific knowledge. Use context files to provide richer background material such as brand guidelines, product catalogs, and business term definitions. Context files are used by all **AmpAI** tools including the Customer Data Agent and other AI Assistants in the platform. They can also be read via MCP connection.

.. ai-assistant-company-context-definition-end


.. ampai-company-context-start

Company context lets tenant administrators upload company-specific knowledge like business definitions, brand guidelines, product catalogs, and strategy documents, so that **AmpAI** produces outputs grounded in your actual business rather than generic defaults. Context files are a searchable reference library that AI assistants consult on demand. Unlike custom prompts, which are injected into every conversation, context files are searched only when a question involves business-specific knowledge.

Context files are used by **AmpAI** and via **MCP** connection. Think of a context file as an overview that helps AI get to know the nuances of the business, including additional information about a brand or business and its goals.

Context files are available across the following AmpAI tools: **Customer Data Assistant**, **Segments AI Assistant**, and **Journeys AI Assistant**.

.. ampai-company-context-end


.. _ampai-company-context-manage:

Manage context files
==================================================

.. ampai-company-context-manage-start

Context files are managed in the **Context files** section on the **Prompts** page, below the prompt text area. The **Context files** section appears on both the **Draft** side and the **Production** side.

To add context files:

#. Open the **Prompts** page: On the **AmpAI** page, click **Production prompts** and then **Edit prompts**.
#. Click **Upload file** or drag and drop files into the **Context files** section on the **Draft** side.
#. Use the checkbox next to each file to enable or disable it. Only enabled files are searched by the assistant.
#. Click **Activate draft** to push context file changes to production.

Uploaded files are listed with the file name, the user who uploaded the file, file size, and upload timestamp.

**Supported formats and limits**

* File types: .txt, .md, and .csv
* Maximum file size: 100 MB per file

.. ampai-company-context-manage-end


.. _ampai-company-context-how-it-works:

How the assistant uses context
==================================================

.. ampai-company-context-how-it-works-start

When a user asks a question that involves business-specific knowledge, the assistant automatically searches enabled context files behind the scenes. The assistant searches the context library and returns the most relevant excerpts, along with the source document title. The assistant then uses those excerpts to inform its response, including segment thresholds, journey channels, terminology, and other business-specific details.

No specific action is required when prompting. Context lookup is automatic when the assistant determines that a question involves business-specific knowledge.

Some examples of situations where the assistant will check company context:

* Answering questions about promotions, campaigns, products, policies, or company assets
* Creating segments or building journeys
* Checking for company-specific definitions of terms like "high value," "churn," "VIP," etc.

You can also manually trigger the context lookup by adding a sentence like "Please use company context to answer this next question." 

.. note:: AmpAI only uses your context files for reference when answering your questions or responding to your prompts. Company context is not used to train any models or applied in any other capacity.

.. ampai-company-context-how-it-works-end


.. _ampai-company-context-best-practices:

Best practices for context files
==================================================

.. ampai-company-context-best-practices-start

Upload files that contain knowledge the assistant needs to answer business-specific questions accurately. Good candidates for context files include:

* **Business term definitions** such as "high-value customer," "active subscriber," or "churn"
* **Brand voice and messaging guidelines** that describe tone, terminology, and communication standards
* **Product line descriptions and catalog information** that describe products, categories, and pricing tiers
* **Channel preferences and routing rules** that specify how customers should be reached
* **Campaign naming conventions** that define how campaigns and programs are named and organized
* **Unique fiscal calendars** that reflect the rhythm of the business


Write context files in plain language. The assistant searches them semantically, so clear, well-organized documents produce better results than raw data dumps. Use descriptive headings and group related information together within each file.

.. ampai-company-context-best-practices-end


.. _ampai-company-context-test:

Test context files
==================================================

.. ampai-company-context-test-start

Use the same draft and production workflow on the **Prompts** page to test context files. After uploading files to the **Draft** side, click **Test draft** and then ask questions that should require business-specific knowledge.

For each response, verify:

* Did the assistant retrieve relevant context from the uploaded files?
* Did the response use correct business-specific terminology and definitions?
* Did the response reflect your brand's actual thresholds, tiers, or rules rather than generic defaults?

Test with questions at different levels of specificity:

.. code-block:: none

   "How do we define a high-value customer?"
   -> Verify: uses your uploaded definition, not a generic threshold

   "Create a segment of customers at risk of churning"
   -> Verify: the segment uses your churn definition from the context files

   "What channels should we use for a win-back campaign?"
   -> Verify: reflects your channel preferences, not generic best practices

If the assistant does not retrieve context for a question that should use it, try rephrasing the question to include more specific business terminology. If results are inconsistent, review the context file for clarity and organization.

.. ampai-company-context-test-end


.. _ampai-company-context-limitations:

Context file limitations
==================================================

.. ampai-company-context-limitations-start

Company context has the following limitations:

* Only text-based file formats are supported: .txt, .md, and .csv. PDF, Word, and image files are not supported.

.. note:: While .csv files are supported, tabular data is not as effective for extracting excerpts. If using .csv, small lookup tables with descriptive headers would be more useful than wide or long .csv tables. 

* Maximum file size is 100 MB per file. 
* The assistant must recognize that a question involves business-specific knowledge to trigger a context search. Very generic questions may not trigger context lookup.
* Context search adds a small amount of latency to responses that use it.

.. ampai-company-context-limitations-end
