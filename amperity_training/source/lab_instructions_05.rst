.. https://docs.amperity.com/reference/


==================================================
Lab 05: Querying data
==================================================

A query in Amperity is a SQL statement that is run from the Queries page against database tables in the Customer 360 page. A query returns a refined and filtered subset of useful customer data.

.. admonition:: Reference Materials

   * `About queries <../references/queries.html>`__ |ext_link|
   * `About the AI Assistant <../references/assistant.html>`__ |ext_link|


Objective
==================================================

To gain practical experience with running queries in Amperity. You will learn how the query editor and the AI assistant are used.


Create a Query Using SQL
==================================================

#. Navigate to the Queries tab and then click Create and Select SQL Query.

   .. image:: /_images/ex05_create_sql_query.png
      :width: 500 px
      :alt: Create SQL Query
      :align: left
      :class: no-scaled-link

#. If you are handy with SQL try writing a query to find the most popular product of all time.

   .. hint:: Viewing the Unified_Itemized_Transactions table and docs will be helpful when writing the query.

#. Or give the AI a try.

#. Expand the AI Assistant tab on the left-hand side of the query editor.

   .. image:: /_images/ex05_use_ai_assistant.png
      :width: 500 px
      :alt: AI Assistant tab
      :align: left
      :class: no-scaled-link

#. Ask the AI to help generate a query by pasting the following question in the AI Assistant message box and clicking the send button. What is the most popular product of all time

   This is an example of a good query use case - not directly tied to a list of customers. How can you tell the AI generated a good result?

   .. image:: /_images/ex05_assistant_query.png
      :width: 500 px
      :alt: AI Assistant query
      :align: left
      :class: no-scaled-link

#. After the SQL Query is returned click Copy SQL and paste it into the query pane. Then click Run query and view the results.

#. Click Untitled Query in the top left-hand corner to edit the name and name the query Most popular product and click Activate.

   .. image:: /_images/ex05_activate_query.png
      :width: 400 px
      :alt: Name and activate query
      :align: left
      :class: no-scaled-link

#. Select Activate only and click on Activate.

   .. image:: /_images/ex05_activate_only.png
      :width: 380 px
      :alt: Activate only
      :align: left
      :class: no-scaled-link


.. tip:: The AI Assistant can answer all sorts of questions. For a bit of fun, click Create and Select SQL Query again. Expand the AI Assistant tab on the left-hand side of the query editor and ask the question: "What is the airspeed velocity of an unladen swallow?"

   After you have read the result click Discard.
