.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        AmpAI Assistants help author SQL queries and create customer segments from natural language commands.

.. meta::
    :content class=swiftype name=body data-type=text:
        AmpAI Assistants help author SQL queries and create customer segments from natural language commands.

.. meta::
    :content class=swiftype name=title data-type=string:
        AmpAI Assistants


==================================================
About AmpAI Assistants
==================================================

.. assistant-overview-start

There are two **AmpAI Assistants**:

* **Queries AI Assistant** helps users author SQL queries and resolve errors
* **Segments AI Assistant** helps users build segments

These assistants are generative AI features within Amperity that lets users input commands in natural language. 

.. assistant-overview-end

.. image:: ../../images/ampai-assist.png
   :width: 500 px
   :alt: Assist
   :align: left
   :class: no-scaled-link

.. assistant-usecases-start

Use the **Queries AI Assistant** in the SQL **Query Editor** to:

* Create SQL queries starting from natural language, such as "Who are my top 100 customers by lifetime spend?" or "Show me everyone who shopped in-store over the last 30 days."
* Ask for help while resolving a SQL error
* Get advice on how to improve a query
* Ask questions about SQL syntax, such as "What is the syntax for a window function?" 

Use the **Segments AI Assistant** in the **Segment Editor** to:

* Generate customer segments
* Refine customer segments 
* Get advice on building better customer segments to meet campaign goals


.. assistant-usecases-end

.. assistant-overview-important-start

.. important:: As with all generative AI capabilities, the outputs of **AmpAI Assistants** are probabilistic. Users should double check outputs for accuracy.

   Review the |support_ai_assistant_privacy_faq| to learn more about how the **AmpAI Assistant** interacts with LLMs and the Microsoft Azure OpenAI Service.

.. assistant-overview-important-end

.. assistant-learning-lab-start

.. admonition:: Amperity Learning Lab

   The **AmpAI Assistants** are generative AI features that can help you build better SQL queries and generate customer segments based on the data in your Amperity tenant.

   Open **Learning Lab** to learn more about how the `AmpAI Assistant <https://learn.amperity.com/the-amperity-ai-assistant>`__ |ext_link| can help you build better queries and segments. Registration is required.

.. assistant-learning-lab-end


.. _assistant-enable-disable:

Enable or disable AmpAI Assistants
==================================================

.. assistant-enable-disable-start

AmpAI features, including **AmpAI Assistants**, may be enabled (or disabled) by a user who is assigned the **DataGrid Operator** or **DataGrid Administrator** policy.

.. assistant-enable-disable-end

**To disable AmpAI Assistants**

.. include:: ../../amperity_reference/source/ampai_settings.rst
   :start-after: .. settings-user-ampai-steps-start
   :end-before: .. settings-user-ampai-steps-end


.. _assistant-howitworks:

How AmpAI Assistants work
==================================================

.. assistant-howitworks-start

**AmpAI Assistants** are powered by LLMs on a private instance of Azure OpenAI Service.

Amperity passes information on the schema information, query and segment examples, results, errors, table usage, and performs a series of research tool calls to improve the quality of results.

.. note:: More detail about how **AmpAI Assistants** work, including data sharing policies, how the model stores data, and what types of data is sent (or not sent), is available from the |ext_amperity_assistant_privacy_faq|.

.. assistant-howitworks-end


.. _assistant-query-examples:

Query Examples
==================================================

.. assistant-query-examples-start

The following examples show some of the ways you can use the **Queries AI Assistant** while working in the SQL **Query Editor**.

* :ref:`assistant-query-example-natural-language`
* :ref:`assistant-query-example-errors`
* :ref:`assistant-query-example-syntax`

.. note:: The answers to these questions within your tenant will depend on the query, schema, results, and error information that was provided to the model and may be different than the examples shown.

.. assistant-query-examples-end


.. _assistant-query-example-natural-language:

Build natural language queries
--------------------------------------------------

.. assistant-query-example-natural-language-start

You can use natural language--the same types of sentences you use when talking to co-workers and friends--to ask the **AmpAI Assistant** to help you build queries against any database in the **Customer 360** page.

.. assistant-query-example-natural-language-end


.. _assistant-query-example-natural-language-lifetime-spend:

Customers by lifetime spend
++++++++++++++++++++++++++++++++++++++++++++++++++

.. assistant-example-natural-language-lifetime-spend-start

**Question**
   "Who are my top 100 customers by lifetime spend?"

**Answer**
   The **Queries AI Assistant** will respond similar to:

   .. image:: ../../images/assistant-example-syntax-natural-language.png
      :width: 400 px
      :alt: Build natural language queries
      :align: left
      :class: no-scaled-link

   .. tip:: When "Tables and fields are valid" is shown for the SQL returned by the **AmpAI Assistant** you can try running the query in the SQL **Query Editor**.

      Click the **Copy SQL** link in the response from the **AmpAI Assistant**, paste the SQL into the SQL **Query Editor**, click the **Run query** button, and then (after the query is finished running) you can view the results.

.. assistant-query-example-natural-language-lifetime-spend-end


.. _assistant-query-example-natural-language-in-store-shoppers:

In-store shoppers
++++++++++++++++++++++++++++++++++++++++++++++++++

.. assistant-example-natural-language-in-store-shoppers-start

**Question**
   "Show me everyone who shopped in-store over the last 30 days."

**Answer**
   The **Queries AI Assistant** will respond similar to:

   .. image:: ../../images/assistant-example-syntax-thirty-days.png
      :width: 400 px
      :alt: Build natural language queries
      :align: left
      :class: no-scaled-link

.. assistant-query-example-natural-language-in-store-shoppers-end

.. _assistant-query-example-errors:

Ask for help resolving errors
--------------------------------------------------

.. assistant-query-example-errors-start

When you have an error in your query syntax you can ask the **AmpAI Assistant** for help resolving the error.

**Question**
   "Can you help me resolve this error?"

**Answer**
   The **Queries AI Assistant** will respond similar to:

   .. image:: ../../images/assistant-example-errors.png
      :width: 400 px
      :alt: Ask for help resolving errors
      :align: left
      :class: no-scaled-link

.. assistant-query-example-errors-end

.. _assistant-query-example-syntax:

Ask questions about syntax
--------------------------------------------------

.. assistant-query-example-syntax-start

You can ask the **AmpAI Assistant** to help you understand how specific types of syntax work in a SQL query.

**Question**
   "What is the syntax for a CASE statement?"

**Answer**
   The **Queries AI Assistant** will respond similar to:

   .. image:: ../../images/assistant-example-syntax.png
      :width: 400 px
      :alt: Ask questions about syntax
      :align: left
      :class: no-scaled-link

.. note:: Amperity uses :doc:`Presto SQL syntax <sql_presto>` within the SQL **Query Editor**.

.. assistant-query-example-syntax-end


.. _assistant-segment-examples:

Segment Examples
==================================================

The following examples show some of the ways you can use the **Segments AI Assistant** while working in the **Segment Editor**.

* :ref:`ampai-segments-example-create-segment`
* :ref:`ampai-segments-example-refine-segment`
* :ref:`ampai-segments-example-get-advice-on-segment`

.. note:: The answers to these questions within your tenant will depend on the query, schema, results, and error information that was provided to the model and may be different than the examples shown.


.. _ampai-segments-example-create-segment:

Create a segment
--------------------------------------------------

.. assistant-segments-example-create-segment-start

You can ask the **Segments AI Assistant** to build a segment based on the criteria you lay out.

**Question**
   "Build a segment of my highest value customers based on customer lifetime value."

**Answer**
  The **Segments AI Assistant** will respond similar to:
  
  .. image:: ../../images/assistant-segments-example-create-segment.png
     :width: 600 px
     :alt: Build natural language queries
     :align: left
     :class: no-scaled-link

.. tip:: Be sure to check that the segment created matches what you were looking for, and if not you can guide the **AmpAI Assistant** on how to try again.

   For example, if you ask for a segment of your highest value customers without specifying customer lifetime value as the criteria, you may get a segment based on highest spend over the past year. 

   In cases like this, prompt the **AmpAI Assistant** again and specify how you want to measure value. 

.. ampai-segments-example-create-segment-end


.. _ampai-segments-example-refine-segment:

Refine a segment
--------------------------------------------------

.. ampai-segments-example-refine-segment-start

You can ask the **Segments AI Assistant** to add additional conditions to your segment. 

**Question**
   "Narrow it down to high value customers who have a product preference for jeans and have not purchased in the last month."

**Answer**
  The **Segments AI Assistant** will respond similar to:

  .. image:: ../../images/assistant-segments-example-refine-segment.png
     :width: 600 px
     :alt: Build natural language queries
     :align: left
     :class: no-scaled-link

.. ampai-segments-example-refine-segment-end


.. _ampai-segments-example-get-advice-on-segment:

Get advice on your segment
--------------------------------------------------

.. ampai-segments-example-get-advice-on-segment-start

You can ask the **Segments AI Assistant** for guidance on how else you might design your segment to meet the goals of your campaign.

**Question**
   "What other criteria should I consider adding to the segment in order to attract high-value customers who have not recently purchased to buy new offerings in our jeans category?"

**Answer**
  The **Segments AI Assistant** will respond similar to:
  
..  .. image:: ../../images/assistant-segments-example-get-segment-advice.png
..     :width: 600 px
..     :alt: Build natural language queries
..     :align: left
..     :class: no-scaled-link

.. code-block:: none

   "To make your segment even more effective for targeting high-value customers
   who have not recently purchased (especially with the goal of promoting new 
   jeans offerings), you might consider adding additional criteria."

Answers will include suggestsions similar to:

#. Predicted Affinity for Related Categories:

   Include customers who also have a demonstrated or predicted interest in complementary categories, such as "Tops and T-shirts" or "Accessories," which pair well with jeans.

#. Preferred Channel or Brand:

   Focus on customers who prefer a specific purchase channel or brand, if your new jeans offerings are exclusive or more prominent in certain channels or under specific brands.

#. Contactability:

   Ensure that customers are opted into email or SMS marketing, so your campaigns can actually reach them.

#. Geographic Proximity:

   Filter for customers living in regions where jeans sales or promotions are planned or more likely and in areas with upcoming in-store events.

#. Previous Buyers of Premium Jeans:

   Target customers who have purchased higher-value or premium jeans in the past, as they are more likely to be interested in new, similar offerings.

#. Lapsed but Historically Loyal Customers:

   Identify customers who have bought jeans repeatedly in the past but have not purchased any recently—they may respond well to a "welcome back" campaign for new jeans.

#. Customer Lifecycle Status:

   Pay attention to customers with a "likely to return" or "at-risk" predicted lifecycle, as they could be nudged toward purchase with targeted messaging.

.. ampai-segments-example-get-advice-on-segment-end
