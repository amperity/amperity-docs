.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Configuration settings allow AmpAI to be turned on or off.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configuration settings allow AmpAI to be turned on or off.

.. meta::
    :content class=swiftype name=title data-type=string:
        AmpAI settings

==================================================
About AmpAI settings
==================================================

.. settings-user-ampai-start

AmpAI provides marketers, analysts, and data engineers with an AI-powered toolkit for smarter decision-making. AmpAI features, including the AmpAI Assistant, may be enabled or disabled by a user who is assigned the **DataGrid Operator** policy.

.. settings-user-ampai-end

**To disable AmpAI features**

.. settings-user-ampai-steps-start

#. From the **Settings** page, open the **AmpAI** tab.
#. Under **Advanced settings**, select the **Disable AmpAI features** option to disable AmpAI features, including the AmpAI Assistant.
#. Click **Confirm**.

.. settings-user-ampai-steps-end


.. _settings-user-ampai-prompts:

AmpAI prompts
==================================================

.. settings-user-ampai-prompts-start

.. note:: Ask your Amperity representative about configuring AmpAI prompts for your tenant.

A prompt is a question asked to AmpAI by a user of Amperity, such as asking AmpAI to build a query or segment that meets a set of criteria.

Prompts can also be used to provide context to AmpAI to help ensure answers from AmpAI align to brand criteria and goals. For example:

* Defining key terms
* Excluding certain types of customers from analysis
* Specifying which tables should be referenced for specific business questions

Use the prompt testing environment to validate that prompts achieve the desired results, and then promote effective prompts to your production environment.

**Example prompts**

* Use the [table_name] table instead of the **Customer 360** table.
* When referencing gender use the "gender" field in the [table_name] table.
* When a prompt references [product], where [product detail] is [A], [B], or [C], use [product-filter].
* When a prompt references a purchase channel with [context A] or [context B] use [channel A] and not [channel B].
* When a prompt references "full price" use [product-field] to identify US price or CA price.
* When a prompt references [qualifier A, qualifier B, or qualifier C] use [field] in [table].

  For example, qualifiers could be "ecom", "ecommerce", or "online" and field is the "webstore" field in the **Unified_Itemized_Transactions** table.

.. settings-user-ampai-prompts-end
