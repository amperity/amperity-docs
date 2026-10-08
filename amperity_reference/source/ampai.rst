.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        The AI Assistant is the conversational interface to your customer data in Amperity. Ask questions, build segments and journeys, and tailor responses with custom prompts and company context.

.. meta::
    :content class=swiftype name=body data-type=text:
        The AI Assistant is the conversational interface to your customer data in Amperity. Ask questions, build segments and journeys, and tailor responses with custom prompts and company context.

.. meta::
    :content class=swiftype name=title data-type=string:
        AI Assistant

==================================================
AI Assistant
==================================================

.. ai-assistant-about-start

The **AI Assistant** is the conversational interface to your customer data in Amperity. Describe what you want to accomplish in plain language, and then use the **AI Assistant** to ask and answer complex questions about your customers, with support for visualizations, over the data in the database. The **AI Assistant** can also create segments and journeys from scratch.

Tool-specific **AI Assistants** bring the same conversation into individual editors---segments, journeys, queries, and Amps consumption---where they help with detailed refinements in the place you are already working.

The **AI Assistant** supports customization through :ref:`custom prompts <ampai-custom-prompt>` and :ref:`company context <ampai-company-context>`. Custom prompts encode specific business logic and definitions that apply to every prompt you write, while company context provides a library of reference documents that help the **AI Assistant** better understand your business. Together, these help you align results with your business requirements and keep them consistent. Custom prompts and company context apply to the **AI Assistant** and to all tool-specific **AI Assistants**.

To enhance response accuracy, the **AI Assistant** leverages tenant-specific information, such as schema metadata, database field descriptions, and usage patterns to refine its understanding and to improve the relevance and precision of results.

The **AI Assistant** offers enterprise-grade privacy and security, is built on the Azure OpenAI Service, and enforces user-level permissions, allowing granular control over access.

.. ai-assistant-about-end

.. ai-assistant-privacy-note-start

.. note:: The **AI Assistant** is powered by models that reside on Azure OpenAI Service. Review the :doc:`AI Assistant Privacy FAQ <ampai_privacy>` for information about how Amperity interacts with Azure OpenAI service.

.. ai-assistant-privacy-note-end

.. ai-assistant-learning-lab-start

.. admonition:: Amperity Learning Lab

   The **AI Assistant** is the conversational interface to your customer data in Amperity, and tool-specific **AI Assistants** bring that same conversation into individual editors.

   Open **Learning Lab** to learn more about `the Amperity AI Assistant <https://amperity.com/learning-lab/the-amperity-ai-assistant>`__ |ext_link|, `exploring data with AmpAI <https://amperity.com/learning-lab/exploring-data-with-ampai>`__ |ext_link|, and `creating custom prompts with AmpAI <https://amperity.com/learning-lab/creating-custom-prompts-with-ampai>`__ |ext_link|. Registration is required.

.. ai-assistant-learning-lab-end


.. _ai-assistant-grid:

.. ai-assistant-grid-start

.. grid:: 1 1 2 2
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: |fa-sparkles| Working with the AI Assistant
      :link-type: doc
      :link: customer_data_assistant

      Access the **AI Assistant**, work on the canvas, review proposed changes, and get good results from your prompts.

   .. grid-item-card:: |fa-layer-group| Tool-specific AI Assistants
      :link-type: doc
      :link: assistant

      Conversational help embedded in the segment, journey, query, and Amps consumption editors.

   .. grid-item-card:: |fa-square-sliders| Custom prompts
      :link-type: doc
      :link: ai_assistant_custom_prompts

      Always-on instructions that encode business logic, define terminology, and set default behaviors.

   .. grid-item-card:: |fa-book-open| Company context
      :link-type: doc
      :link: ai_assistant_company_context

      A searchable library of reference documents that ground responses in your actual business.

   .. grid-item-card:: |fa-gears| Administer the AI Assistant
      :link-type: doc
      :link: ai_assistant_administer

      Regional availability, user-level permissions and policies, enablement, and conversation auditing.

   .. grid-item-card:: |fa-shield-check| AI Assistant Privacy FAQ
      :link-type: doc
      :link: ampai_privacy

      How Amperity interacts with the Azure OpenAI Service, and how your data is handled.

.. ai-assistant-grid-end


.. toctree::
   :caption: AI Assistant
   :maxdepth: 2
   :hidden:

   Working with the AI Assistant <customer_data_assistant>
   Tool-specific AI Assistants <assistant>
   Custom prompts <ai_assistant_custom_prompts>
   Company context <ai_assistant_company_context>
   Administer the AI Assistant <ai_assistant_administer>
   AI Assistant Privacy FAQ <ampai_privacy>
