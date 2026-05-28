.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        AmpAI is the engine that drives the conversational AI tools within Amperity, from the Customer Data Assistant to the AI Assistants.

.. meta::
    :content class=swiftype name=body data-type=text:
        AmpAI is the engine that drives the conversational AI tools within Amperity, from the Customer Data Assistant to the AI Assistants.

.. meta::
    :content class=swiftype name=title data-type=string:
        About AmpAI

==================================================
About AmpAI
==================================================

.. ampai-overview-start

**AmpAI** is the engine that drives the conversational AI tools within Amperity, including the **Customer Data Assistant** and the **AI Assistants**. **AmpAI** lets you ask and answer complex questions about your customers, with support for visualizations, and operates over the data in the database.

**AmpAI** supports customization through :ref:`custom prompts <ampai-custom-prompt>` and :ref:`company context <ampai-company-context>`. Custom prompts encode specific business logic and definitions that apply to every prompt you write, while company context provides a library of reference documents for AmpAI to better understand your business. Together, these help you tailor **AmpAI** to align with your business requirements and keep results consistent.

**AmpAI** offers enterprise-grade privacy and security and is built on the Azure OpenAI Service.

To enhance response accuracy, **AmpAI** leverages tenant-specific information, such as schema metadata, database field descriptions, and usage patterns to refine its understanding and to improve the relevance and precision of results.

**AmpAI** enforces user-level permissions, allowing granular control over access.

.. ampai-overview-end

.. ampai-privacy-note-start

.. note:: AmpAI is powered by models that reside on Azure OpenAI Service. Review the :doc:`AmpAI Privacy FAQ <ampai_privacy>` for information about how Amperity interacts with Azure OpenAI service.

.. ampai-privacy-note-end

.. ampai-learning-lab-start

.. admonition:: Amperity Learning Lab

   **AmpAI** is the engine that drives conversational AI tools within Amperity, including the Customer Data Assistant and other AI Assistants.

   Open **Learning Lab** to learn more about `the Amperity AI Assistant <https://amperity.com/learning-lab/the-amperity-ai-assistant>`__ |ext_link|, `exploring data with AmpAI <https://amperity.com/learning-lab/exploring-data-with-ampai>`__ |ext_link|, and `creating custom prompts with AmpAI <https://amperity.com/learning-lab/creating-custom-prompts-with-ampai>`__ |ext_link|. Registration is required.

.. ampai-learning-lab-end


.. _ampai-tools:

AmpAI tools
==================================================

.. ampai-tools-start

**AmpAI** encompasses multiple tools, each designed for a different stage of your workflow. The **Customer Data Assistant** is a conversational starting point --- describe what you want to accomplish and it generates segments or journeys from scratch. The **AI Assistants** are embedded in individual editors for segments, journeys, and queries, where they help with detailed refinements, while the **Consumption AI Assistant** helps you understand how you are using Amps.

A typical workflow might start with the **Customer Data Assistant** to quickly create a segment and journey, then use the **Manual edit** option to open the specialized editors where the **AI Assistants** can help with detailed adjustments.

.. note:: Custom prompts and company context set in **AmpAI** apply to all AmpAI tools, including the Customer Data Assistant and all other AI Assistants.

.. ampai-tools-overview-table-start

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Tool
     - Best for
     - Access point
   * - Customer Data Assistant
     - Starting from intent, creating segments and journeys from scratch, multi-step workflows
     - AmpAI button in sidebar
   * - Segments AI Assistant
     - Fine-tuning existing segments, making precise adjustments within the segment editor
     - Within the **Segments** page
   * - Journeys AI Assistant
     - Refining journey logic, adjusting channel configurations within the journey editor
     - Within the **Journeys** page
   * - Queries AI Assistant
     - Writing and debugging SQL queries, data exploration
     - Within the **Queries** page
   * - Consumption AI Assistant
     - Monitoring Amps consumption
     - Within the **Amps** page

.. ampai-tools-overview-table-end

.. ampai-tools-links-start

Learn more about :doc:`Customer Data Assistant <customer_data_assistant>` and :doc:`AI Assistants <assistant>`.

.. ampai-tools-links-end

.. _ampai-getting-good-results:

Getting good results with AmpAI
==================================================

.. ampai-getting-good-results-start

To achieve optimal results when using **AmpAI**, follow these best practices for structuring your prompts:

* **Understand the question’s scope**

  Define the scope of your question to avoid ambiguous results. For example, specify the timeframe, customer segments, or metrics you are analyzing.

* **Avoid overloading**

  Focus on one primary question or task per prompt to ensure clarity and to avoid confusing results.

  For example, instead of asking how the demographics of omnichannel customers compare to single-channel customers, ask a question first about omnichannel customer demographics, and then ask a second question about single-channel customer demographics.

* **Use consistent terminology**

  Stick to terminology used in your schema and business logic to align with how **AmpAI** understands your data.

* **Update the custom prompt often**

  The custom prompt is a powerful tool. Update the custom prompt whenever you get a result that does not align with the way your business views the world.

.. ampai-getting-good-results-end


.. _ampai-customize:

Customize AmpAI
==================================================

.. ampai-customize-start

Both custom prompts and context files are managed on the **Prompts** page. To open the **Prompts** page:

#. On the **AmpAI** page, click **Production prompts** to view the production prompt. 
#. Click **Edit prompts** in the **Production prompt** window.

* **Custom prompts** are short, always-on instructions that are injected into every AmpAI conversation. Use custom prompts to encode business logic, define terminology, and set default behaviors.
* **Company context** is a library of reference documents that the assistant searches only when a question involves business-specific knowledge. Use context files to provide richer background material such as brand guidelines, product catalogs, and business term definitions.

The **Prompts** page uses a draft and production workflow:

#. Make changes on the **Draft prompt** side.
#. Click **Test draft** to validate changes in your own AmpAI session without affecting other users.
#. Click **Activate draft** to push draft changes to production for all users.
#. Click **Revert draft** to discard draft changes and return to the current production version.

Learn more about :ref:`custom prompts <ampai-custom-prompt>` and :ref:`company context <ampai-company-context>`.

.. ampai-customize-end


.. _ampai-custom-prompt:

Custom prompts
==================================================

.. ampai-custom-prompt-start

Custom prompts are short, always-on instructions that are injected into every **AmpAI** conversation. Use custom prompts to encode business logic, define terminology, and set default behaviors. Custom prompts apply to all AmpAI tools, including the Customer Data Assistant and AI Assistants, and can be updated to include:

* Customer definitions, such as defining how your brand interprets retention metrics
* Priority tables and fields, such as specifying priority for default tables and fields that are used with loyalty-related queries
* Exclusions, such as automatically excluding employees or outliers from analysis
* Default customer identifiers
* Fiscal calendar information

Set a custom prompt on the **Prompts** page: On the **AmpAI** page, click **Production prompts** and then **Edit prompts**.

While **AmpAI** works out of the box, updating the custom prompt is often necessary to keep AmpAI aligned with how your brand understands your customers. The custom prompt should be updated when an AmpAI response does not meet expectations.

When your brand starts using AmpAI you should start with a list of 3-5 key customer questions that AmpAI should answer correctly. Test these questions, and then refine the custom prompt to ensure accurate and meaningful responses. This will help establish an effective first iteration of the custom prompt.

.. ampai-custom-prompt-end


.. _ampai-write-custom-prompt:

Write an effective custom prompt
--------------------------------------------------

.. ampai-write-custom-prompt-start

Follow these guidelines to create custom prompts that help **AmpAI** understand your brand's specific terminology, business logic, and data structure.

.. ampai-write-custom-prompt-end


.. _ampai-write-custom-prompt-database-headers:

Use database section headers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-write-custom-prompt-database-headers-start

The custom prompt is set per tenant, but a tenant may have multiple databases. To define different behavior per database, use the database name as a section header. When **AmpAI** runs a session, it operates against a single active database. The system prompt instructs **AmpAI** to use the section matching the active database name for additional context.

If a tenant has rules for multiple databases, structure the prompt like this:

.. code-block:: none

   C360
   Use Customer360 for all customer profile data.
   "High-value customer" means lifetime revenue > $1,500.
   Always exclude employees using Employee_Flag = 'N'.

   Marketing_DB
   Use Campaign_Customers for profile data.
   "Engaged customer" means opened an email in the last 90 days.

If the tenant only has one database, the header is still recommended for clarity but is less critical.

.. ampai-write-custom-prompt-database-headers-end


.. _ampai-write-custom-prompt-be-specific:

Be specific with exact names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-write-custom-prompt-be-specific-start

Reference exact field names, values, and table names whenever possible to ensure precise results.

**Avoid vague references:**

Bad: "Use the main customer table for profiles"
Good: "Use Customer360 for all customer profile data (names, contact info, attributes)"

Bad: "Filter out internal users"
Good: "Exclude records where email ends with @acmeretail.com, @acmeinternal.com, or @testvendor.com"

.. ampai-write-custom-prompt-be-specific-end


.. _ampai-write-custom-prompt-map-terms:

Map business terms to Amperity terms
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-write-custom-prompt-map-terms-start

Customers often use business terminology that differs from your schema column names and values. Define these mappings explicitly in the custom prompt.

For example, customers say "SKU" but the column is ``product_id``. Customers say "online" but the field value is ``ecommerce``.

.. code-block:: none

   When users say "SKU," "product code," or "item number," use the product_id
   column from Unified_Itemized_Transactions.

   When users say "online," "ecom," or "ecommerce," filter on
   channel = 'ecommerce' in the TRANSACTIONS table.

   When users say "store" or "in-store," filter on channel = 'retail'
   in the TRANSACTIONS table.

.. ampai-write-custom-prompt-map-terms-end


.. _ampai-write-custom-prompt-sql-patterns:

Provide SQL patterns for complex logic
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-write-custom-prompt-sql-patterns-start

For reusable filters and complex business logic, give **AmpAI** a complete CTE it can copy and adapt.

.. code-block:: sql

   WITH real_customers AS (
     SELECT AMPID
     FROM Customer360 c
     JOIN (
       SELECT AMPID, COUNT(txn_nbr) AS txn_count
       FROM TRANSACTIONS
       GROUP BY AMPID
       HAVING COUNT(txn_nbr) BETWEEN 1 AND 60
     ) t ON c.AMPID = t.AMPID
     WHERE c.Employee_Flag = 'N'
       AND c.email NOT LIKE '%@acmeretail.com'
       AND c.email NOT LIKE '%@acmeinternal.com'
       AND c.email NOT LIKE '%@testvendor.com'
   )

.. ampai-write-custom-prompt-sql-patterns-end


.. _ampai-write-custom-prompt-define-concepts:

Define business concepts
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-write-custom-prompt-define-concepts-start

If your brand has specific definitions for retention, churn, high-value, or loyalty tiers, spell them out explicitly.

.. code-block:: none

   "High-value customer" means a customer with lifetime revenue > $1,500
   (top 25% of active customers).

   "Churning customer" means a customer with < 50% probability of returning
   in the next 12 months AND has made at least one purchase in the past 2 years.

   "Active customer" means at least 1 purchase in the last 365 days.

   Loyalty tiers:
   - Bronze: lifetime revenue $0-$250
   - Silver: lifetime revenue $251-$1,000
   - Gold: lifetime revenue $1,001-$2,500
   - Platinum: lifetime revenue > $2,500

.. ampai-write-custom-prompt-define-concepts-end


.. _ampai-write-custom-prompt-default-exclusions:

Specify default exclusions
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-write-custom-prompt-default-exclusions-start

If every query should filter out test accounts, employees, or bots, state it once in the custom prompt.

.. code-block:: none

   Always apply the following filters unless the user explicitly asks
   for unfiltered results:
   - Employee_Flag = 'N'
   - Total transaction count between 1 and 60
   - Exclude email domains: @acmeretail.com, @acmeinternal.com, @testvendor.com

.. ampai-write-custom-prompt-default-exclusions-end


.. _ampai-test-custom-prompt:

Test custom prompts
--------------------------------------------------

.. ampai-test-custom-prompt-start

Testing is not "ask a question and see if it looks right." Use a structured approach to validate that your custom prompt produces the expected results.

#. **Define test categories.**

   Before writing test cases, identify what your prompt is supposed to do.

   .. list-table::
      :widths: 20 35 45
      :header-rows: 1

      * - Category
        - What to test
        - Example
      * - Term mapping
        - Brand terminology resolves to correct columns/values
        - "Show me online orders" uses ``channel = 'ecommerce'``
      * - Default filters
        - Exclusions are applied automatically
        - Any customer count query excludes employees
      * - Table routing
        - AmpAI uses the right table
        - Profile questions go to Customer360, not Unified_Coalesced
      * - Business definitions
        - Concepts match brand meaning
        - "High-value customers" uses lifetime revenue > $1,500
      * - Edge cases
        - Opt-out works, ambiguity is handled
        - "Show me ALL customers including employees" skips exclusion filter

#. **Write test questions.**

   For each category, write 1-2 natural-language questions a real user would ask. Use the customer's actual vocabulary, not Amperity terminology.

#. **Run tests in draft mode.**

   Set your custom prompt as the draft prompt, open **AmpAI** in a new conversation, and ask each test question one at a time. For each response, check:

   * Did it use the correct table?
   * Did it use the correct column names?
   * Did it apply the expected filters?
   * Did the SQL match your expected pattern?
   * If it ran a query, do the results make sense?

#. **Record results.**

   Track your test results systematically to identify patterns and failures.

   .. list-table::
      :widths: 5 15 18 22 18 7 15
      :header-rows: 1

      * - #
        - Category
        - Question
        - Expected
        - Actual
        - Pass?
        - Notes
      * - 1
        - Term mapping
        - "online orders"
        - channel = 'ecommerce'
        - channel = 'ecommerce'
        - Yes
        -
      * - 2
        - Default filter
        - "how many customers"
        - Employee exclusion applied
        - No filter
        - No
        - Make exclusion rule stronger

#. **Iterate.**

   For each failure, identify why **AmpAI** didn't follow the instruction. Common reasons:

   * Instruction was ambiguous ("use the customer table"—which one?)
   * Instruction was buried in too much text (move critical rules to the top)
   * Column/table name was wrong (check the actual schema)
   * Conflicting instructions in the prompt

   Make one change at a time to the draft prompt. Re-run the failing test case. Re-run passing test cases to check for regressions.

#. **Promote to production.**

   Re-run the full test set one final time on the draft. Activate the draft to production. Have a second person run 2-3 test questions to sanity check.

.. ampai-test-custom-prompt-end


.. _ampai-sample-test-prompts:

Sample test prompts
--------------------------------------------------

.. ampai-sample-test-prompts-start

Copy these into **AmpAI** with the draft prompt active. Adapt the expected results to your brand's custom prompt.

.. ampai-sample-test-prompts-end


.. _ampai-sample-test-prompts-term-mapping:

Term mapping
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-sample-test-prompts-term-mapping-start

.. code-block:: none

   "How many customers bought online last month?"
   -> Verify: uses the correct channel column and value, not LIKE '%online%'

   "What are the top 10 SKUs by revenue?"
   -> Verify: uses product_id, not a literal column called "SKU"

   "Show me in-store revenue by month for the last year"
   -> Verify: uses channel = 'retail' (or whatever mapping you defined)

.. ampai-sample-test-prompts-term-mapping-end


.. _ampai-sample-test-prompts-default-filters:

Default exclusion filters
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-sample-test-prompts-default-filters-start

.. code-block:: none

   "How many active customers do we have?"
   -> Verify: employee exclusion, email domain exclusion, and transaction
      count filters are all applied

   "What is our average customer lifetime value?"
   -> Verify: same exclusions applied even though the question doesn't
      mention filtering

   "Show me ALL records in the Customer360 table with no filters"
   -> Verify: exclusions are NOT applied (user explicitly asked for everything)

   "How many total rows are in Customer360?"
   -> Verify: no exclusions — this is a raw count question, not a "customer" question

.. ampai-sample-test-prompts-default-filters-end


.. _ampai-sample-test-prompts-table-routing:

Table routing
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-sample-test-prompts-table-routing-start

.. code-block:: none

   "What is the average age of our customers?"
   -> Verify: queries Customer360, not Unified_Transactions or Unified_Coalesced

   "What was total revenue last quarter?"
   -> Verify: queries TRANSACTIONS or Unified_Transactions, not Customer360

   "Show me customer names alongside their last purchase date"
   -> Verify: joins Customer360 (names) to the transaction table (purchase date)
      on the correct ID

.. ampai-sample-test-prompts-table-routing-end


.. _ampai-sample-test-prompts-business-definitions:

Business definitions
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-sample-test-prompts-business-definitions-start

.. code-block:: none

   "How many high-value customers do we have?"
   -> Verify: uses your exact definition (e.g., lifetime revenue > $1,500),
      not an invented threshold

   "Break down customers by loyalty tier"
   -> Verify: uses your tier ranges (Bronze/Silver/Gold/Platinum),
      not made-up buckets

   "How many customers are at risk of churning?"
   -> Verify: uses your churn definition, not a generic "hasn't purchased in 90 days"

.. ampai-sample-test-prompts-business-definitions-end


.. _ampai-sample-test-prompts-stress-tests:

Stress tests
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-sample-test-prompts-stress-tests-start

.. code-block:: none

   "How many high-value online customers churned last quarter?"
   -> Verify: combines business definition + term mapping + time filter
      + default exclusions all correctly

   "Compare revenue from loyal vs churning customers"
   -> Verify: uses your definitions for both terms in the same query

   "Who are our top 100 customers?"
   -> Verify: uses your definition of "top" (by spend? by frequency?)
      and applies exclusions

.. ampai-sample-test-prompts-stress-tests-end


.. _ampai-sample-test-prompts-segments-journeys:

Segment and journey prompts
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-sample-test-prompts-segments-journeys-start

.. code-block:: none

   "Create a segment of high-value customers at risk of churning"
   -> Verify: delegates to the Segments AI Assistant and the resulting segment
      uses your definitions

   "Build me a segment of customers who bought online in the last 30 days"
   -> Verify: segment uses the correct channel mapping from your prompt

   "Create a win-back journey for churning platinum customers"
   -> Verify: creates a segment using your churn + tier definitions,
      then creates the journey

.. ampai-sample-test-prompts-segments-journeys-end


.. _ampai-prompt-patterns-by-industry:

Common prompt patterns by industry
--------------------------------------------------

.. ampai-prompt-patterns-by-industry-start

Use these patterns as a starting point when writing custom prompts for your industry.

.. ampai-prompt-patterns-by-industry-end


.. _ampai-prompt-patterns-retail:

Retail and e-commerce
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-prompt-patterns-retail-start

* Map "online" / "ecom" / "web" to channel value
* Define loyalty tiers with spend thresholds
* Exclude employee purchases and internal accounts
* Map "SKU" / "item" / "product code" to ``product_id``

.. ampai-prompt-patterns-retail-end


.. _ampai-prompt-patterns-financial:

Financial services
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-prompt-patterns-financial-start

* Define "active account" vs "dormant account"
* Specify which transaction types count as revenue
* Exclude internal/test accounts by account type

.. ampai-prompt-patterns-financial-end


.. _ampai-prompt-patterns-hospitality:

Hospitality
++++++++++++++++++++++++++++++++++++++++++++++++++

.. ampai-prompt-patterns-hospitality-start

* Map "stays" / "visits" / "bookings" to transaction table
* Define "loyalty member" vs "guest"
* Specify how to calculate LTV (room revenue only vs total spend)

.. ampai-prompt-patterns-hospitality-end


.. _ampai-custom-prompt-limitations:

Custom prompt limitations
--------------------------------------------------

.. ampai-custom-prompt-limitations-start

The custom prompt cannot:

* Change the AI's tools or capabilities
* Override core SQL syntax rules (Presto SQL)
* Make **AmpAI** access tables outside the active database
* Configure destinations, campaigns, or orchestrations
* For segment/journey creation, the custom prompt provides context but the Segment assistant and Journey assistant have their own specialized logic

.. ampai-custom-prompt-limitations-end


.. _ampai-company-context:

Company context
==================================================

.. ampai-company-context-start

Company context lets tenant administrators upload company-specific knowledge like business definitions, brand guidelines, product catalogs, and strategy documents, so that **AmpAI** produces outputs grounded in your actual business rather than generic defaults. Context files are a searchable reference library that AI assistants consult on demand. Unlike custom prompts, which are injected into every conversation, context files are searched only when a question involves business-specific knowledge.

Context files are available across the following AmpAI tools: **Customer Data Assistant**, **Segments AI Assistant**, and **Journeys AI Assistant**.

.. ampai-company-context-end


.. _ampai-company-context-manage:

Manage context files
--------------------------------------------------

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
--------------------------------------------------

.. ampai-company-context-how-it-works-start

When a user asks a question that involves business-specific knowledge, the assistant automatically searches enabled context files behind the scenes. The assistant  searches the context library and returns the most relevant excerpts --- typically a few short passages, at most five --- along with the source document title. The assistant then uses those excerpts to inform its response, including segment thresholds, journey channels, terminology, and other business-specific details.

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
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

.. ampai-company-context-limitations-start

Company context has the following limitations:

* Only text-based file formats are supported: .txt, .md, and .csv. PDF, Word, and image files are not supported.

.. note:: While .csv files are supported, tabular data is not as effective for extracting excerpts. If using .csv, small lookup tables with descriptive headers would be more useful than wide or long .csv tables. 

* Maximum file size is 100 MB per file. 
* The assistant must recognize that a question involves business-specific knowledge to trigger a context search. Very generic questions may not trigger context lookup.
* Context search adds a small amount of latency to responses that use it.

.. ampai-company-context-limitations-end


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
