.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        The AI Assistant provides real-time insights while authoring SQL queries.

.. meta::
    :content class=swiftype name=body data-type=text:
        The AI Assistant provides real-time insights while authoring SQL queries.

.. meta::
    :content class=swiftype name=title data-type=string:
        AI Assistant

==================================================
AI Assistant
==================================================

.. assistant-overview-start

The AI Assistant is a generative AI feature within the SQL **Query Editor** that provides real-time insights while you author SQL queries against any database in the **Customer 360** page.

.. assistant-overview-end

.. image:: ../../images/ampai-assist.png
   :width: 500 px
   :alt: Assist
   :align: left
   :class: no-scaled-link

.. assistant-usecases-start

Use the AI Assistant to:

* Ask for help while resolving a SQL error
* Get advice on how to improve a query
* Ask questions about SQL syntax, such as "What is the syntax for a window function?"
* Create SQL queries starting from natural language, such as "Who are my top 100 customers by lifetime spend?" or "Show me everyone who shopped in-store over the last 30 days." 

.. assistant-usecases-end

.. assistant-overview-important-start

.. important:: As with all generative AI capabilities, the outputs of AI Assistant are probabilistic. Users should double check outputs for accuracy.

   Review the |support_ai_assistant_privacy_faq| to learn more about how the AI Assistant interacts with GPT-4 and the Microsoft Azure OpenAI Service.

.. assistant-overview-important-end

.. assistant-learning-lab-start

.. admonition:: Amperity Learning Lab

   .. list-table::
      :widths: 150 450
      :header-rows: 0

      * - .. image:: ../../images/learning-lab-ai-assistant.png
             :width: 140 px
             :alt: Amperity Learning Lab
             :align: left
             :class: no-scaled-link
        - The AI Assistant is a generative AI-based feature that can help you build better SQL queries against the data in your Amperity tenant.

          Open **Learning Lab** to learn more about how the |ext_learning_lab_ai_assistant| can help you build better queries. Registration is required.

.. assistant-learning-lab-end


.. _assistant-enable-disable:

Enable (or disable) the AI Assistant
==================================================

.. include:: ../../amperity_reference/source/queries.rst
   :start-after: .. queries-disable-ai-assistant-start
   :end-before: .. queries-disable-ai-assistant-end

**To disable the AI Assistant**

.. include:: ../../amperity_reference/source/queries.rst
   :start-after: .. queries-disable-ai-assistant-steps-start
   :end-before: .. queries-disable-ai-assistant-steps-end


.. _assistant-howitworks:

How the AI Assistant works
==================================================

.. assistant-howitworks-start

The AI Assistant is powered by a private instance of OpenAI GPT-4.

Amperity uses the largest context window that is currently available, and then provides query, schema, results, and error information to the model to help ensure the best chance of generating highly relevant results.

.. note:: More detail about how the AI Assistant works, including data sharing policies, how the model stores data, and what types of data is sent (or not sent), is available from the |ext_amperity_assistant_privacy_faq|.

.. assistant-howitworks-end


.. _assistant-examples:

Examples
==================================================

.. assistant-examples-start

The following examples show some of the ways you can use the AI Assistant while working in the SQL **Query Editor**.

* :ref:`assistant-example-syntax`
* :ref:`assistant-example-errors`
* :ref:`assistant-example-natural-language`

.. note:: The answers to these questions within your tenant will depend on the query, schema, results, and error information that was provided to the model and may be different than the examples shown in this topic.

.. assistant-examples-end


.. _assistant-example-syntax:

Ask questions about syntax
--------------------------------------------------

.. assistant-example-syntax-start

You can ask the AI Assistant to help you understand how specific types of syntax work in a SQL query.

**Question**
   "What is the syntax for a CASE statement?"

**Answer**
   The AI Assistant will respond similar to:

   .. image:: ../../images/assistant-example-syntax.png
      :width: 400 px
      :alt: Ask questions about syntax
      :align: left
      :class: no-scaled-link

.. note:: Amperity uses :doc:`Presto SQL syntax <sql_presto>` within the SQL **Query Editor**.

.. assistant-example-syntax-end


.. _assistant-example-errors:

Ask for help resolving errors
--------------------------------------------------

.. assistant-example-errors-start

When you have an error in your query syntax you can ask the AI Assistant for help resolving the error.

**Question**
   "Can you help me resolve this error?"

**Answer**
   The AI Assistant will respond similar to:

   .. image:: ../../images/assistant-example-errors.png
      :width: 400 px
      :alt: Ask for help resolving errors
      :align: left
      :class: no-scaled-link

.. assistant-example-errors-end


.. _assistant-example-natural-language:

Build natural language queries
--------------------------------------------------

.. assistant-example-natural-language-start

You can use natural language---the same types of sentences you use when talking to co-workers and friends---to ask the AI Assistant to help you build queries against any database in the **Customer 360** page.

.. assistant-example-natural-language-end


.. _assistant-example-natural-language-lifetime-spend:

Customers by lifetime spend
++++++++++++++++++++++++++++++++++++++++++++++++++

.. assistant-example-natural-language-lifetime-spend-start

**Question**
   "Who are my top 100 customers by lifetime spend?"

**Answer**
   The AI Assistant will respond similar to:

   .. image:: ../../images/assistant-example-syntax-natural-language.png
      :width: 400 px
      :alt: Build natural language queries
      :align: left
      :class: no-scaled-link

   .. tip:: When "Tables and fields are valid" is shown for the SQL returned by the AI Assistant you can try running the query in the SQL **Query Editor**.

      Click the **Copy SQL** link in the response from the AI Assistant, paste the SQL into the SQL **Query Editor**, click the **Run query** button, and then (after the query is finished running) you can view the results.

.. assistant-example-natural-language-lifetime-spend-end


.. _assistant-example-natural-language-in-store-shoppers:

In-store shoppers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. assistant-example-natural-language-in-store-shoppers-start

**Question**
   "Show me everyone who shopped in-store over the last 30 days."

**Answer**
   The AI Assistant will respond similar to:

   .. image:: ../../images/assistant-example-syntax-thirty-days.png
      :width: 400 px
      :alt: Build natural language queries
      :align: left
      :class: no-scaled-link

.. assistant-example-natural-language-in-store-shoppers-end
