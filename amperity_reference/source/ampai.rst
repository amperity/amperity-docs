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

**AmpAI** enables brands to ask and answer complex questions about their customers, with support for visualizations. **AmpAI** operates over the data in the database and makes it easy for users to ask questions and get answers about their customers.

**AmpAI** supports customization through custom prompting capabilities. This enables organizations to encode specific business logic and defintions, tailoring **AmpAI** to align with their business requirements and ensuring consistency in results.

**AmpAI** offers enterprise-grade privacy and security and is built on the Azure OpenAI Service.

To enhance response accuracy, **AmpAI** leverages tenant-specific information, such as schema metadata, database field descriptions, and usage patterns to refine its understanding and to improve the relevance and precision of results.

**AmpAI** enforces user-level permissions, allowing granular control over access.

.. ampai-overview-end

.. ampai-privacy-note-start

.. note:: AmpAI is powered by models that reside on Azure OpenAI Service. Review the :doc:`AmpAI Privacy FAQ <ampai_privacy>` for information about how Amperity interacts with Azure OpenAI service.

.. ampai-privacy-note-end

.. _ampai-good-results:

Getting good results with AmpAI
==================================================

.. ampai-getting-good-results-start

To achieve optimal results when using **AmpAI**, follow these best practices for structuring your prompts:

* **Understand the question's scope**

  Define the scope of your question to avoid ambiguous results. For example, specify the timeframe, customer segments, or metrics you are analyzing.

* **Avoid overloading**

  Focus on one primary question or task per prompt to ensure clarity and to avoid confusing results.

  For example, instead of asking how the demographics of omnichannel customers compare to single-channel customers, ask a question first about omnichannel customer demographics, and then ask a second question about single-channel customer demographics.

* **Use consistent terminology**

  Stick to terminology used in your schema and business logic to align with how **AmpAI** understands your data.

* **Update the custom prompt often**

  The custom prompt is a powerful tool. Update the custom prompt whenever you get a result that does not align with the way your business views the world.

.. ampai-getting-good-results-end


.. _ampai-custom-prompt:

About the custom prompt
==================================================

.. ampai-custom-prompt-start

The custom prompt in **AmpAI** enables your brand to tailor responses to align with specific business logic. Custom prompts apply to all user queries within AmpAI and the AI Assistant, and can be updated to include:

* Customer definitions, such as defining how your brand interprets retention metrics
* Priority tables and fields, such as specifying priority for default tables and fields that are used with loyalty-related queries
* Exclusions, such as automatically excluding employees or outliers from analysis
* Default customer identifiers
* Fiscal calendar information

While **AmpAI** works out of the box, updating the custom prompt is often necessary to keep AmpAI aligned with how your brand understands your customers. The custom prompt should be updated when an AmpAI response does not meet expectations.

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

.. ampai-configure-custom-prompt-end


.. _ampai-write-custom-prompt:

Write an effective custom prompt
==================================================

.. ampai-write-custom-prompt-start

Follow these guidelines to create custom prompts that help **AmpAI** understand your brand's specific terminology, business logic, and data structure.

.. ampai-write-custom-prompt-end


.. _ampai-write-custom-prompt-database-headers:

Use database section headers
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

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
==================================================

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
==================================================

.. ampai-sample-test-prompts-start

Copy these into **AmpAI** with the draft prompt active. Adapt the expected results to your brand's custom prompt.

.. ampai-sample-test-prompts-end


.. _ampai-sample-test-prompts-term-mapping:

Term mapping
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

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
--------------------------------------------------

.. ampai-sample-test-prompts-segments-journeys-start

.. code-block:: none

   "Create a segment of high-value customers at risk of churning"
   -> Verify: delegates to the Segment Agent and the resulting segment
      uses your definitions

   "Build me a segment of customers who bought online in the last 30 days"
   -> Verify: segment uses the correct channel mapping from your prompt

   "Create a win-back journey for churning platinum customers"
   -> Verify: creates a segment using your churn + tier definitions,
      then creates the journey

.. ampai-sample-test-prompts-segments-journeys-end


.. _ampai-prompt-patterns-by-industry:

Common prompt patterns by industry
==================================================

.. ampai-prompt-patterns-by-industry-start

Use these patterns as a starting point when writing custom prompts for your industry.

.. ampai-prompt-patterns-by-industry-end


.. _ampai-prompt-patterns-retail:

Retail and e-commerce
--------------------------------------------------

.. ampai-prompt-patterns-retail-start

* Map "online" / "ecom" / "web" to channel value
* Define loyalty tiers with spend thresholds
* Exclude employee purchases and internal accounts
* Map "SKU" / "item" / "product code" to ``product_id``

.. ampai-prompt-patterns-retail-end


.. _ampai-prompt-patterns-financial:

Financial services
--------------------------------------------------

.. ampai-prompt-patterns-financial-start

* Define "active account" vs "dormant account"
* Specify which transaction types count as revenue
* Exclude internal/test accounts by account type

.. ampai-prompt-patterns-financial-end


.. _ampai-prompt-patterns-hospitality:

Hospitality
--------------------------------------------------

.. ampai-prompt-patterns-hospitality-start

* Map "stays" / "visits" / "bookings" to transaction table
* Define "loyalty member" vs "guest"
* Specify how to calculate LTV (room revenue only vs total spend)

.. ampai-prompt-patterns-hospitality-end


.. _ampai-custom-prompt-limitations:

Custom prompt limitations
==================================================

.. ampai-custom-prompt-limitations-start

The custom prompt cannot:

* Change the AI's tools or capabilities
* Override core SQL syntax rules (Presto SQL)
* Make **AmpAI** access tables outside the active database
* Configure destinations, campaigns, or orchestrations
* For segment/journey creation, the custom prompt provides context but the Segment Agent and Journey Agent have their own specialized logic

.. ampai-custom-prompt-limitations-end


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

   Allows users to update the custom prompt. **Datagrid Operators** and **Datagrid Administrators** always have the ability to modify prompts.

.. ampai-permissions-and-policies-end


.. _ampai-disable:

Disable AmpAI features
==================================================

.. ampai-disable-start

**AmpAI** and the **AmpAI Assistants** can be disabled for all users. Open the **Settings** page, select the **AmpAI** tab, and then click **Disable AmpAI features**.

.. ampai-disable-end


.. _ampai-audit:

Audit conversations
==================================================

.. ampai-audit-start

**AmpAI** and **AmpAI Assistant** conversations can be audited by users assigned the **Datagrid Operator** and **Datagrid Administrator** policies from the **Settings** page.

The **AmpAI** tab on the **Settings** page logs the questions that are asked to **AmpAI** and the **AmpAI Assistants** under **AI Conversations**.

The **Activity log** tab on the **Settings** page logs when **AmpAI Assistant** questions are asked using the "amperity.query.exec/sampled" action.

.. ampai-audit-end
