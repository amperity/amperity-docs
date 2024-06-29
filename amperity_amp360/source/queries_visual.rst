.. 
.. https://docs.amperity.com/amp360/
.. 


.. meta::
    :description lang=en:
        Build queries using the visual Query Editor.

.. meta::
    :content class=swiftype name=body data-type=text:
        Build queries using the visual Query Editor.

.. meta::
    :content class=swiftype name=title data-type=string:
        About the visual Query Editor

==================================================
About the visual Query Editor
==================================================

.. queries-visual-start

The visual **Query Editor** is a user interface within the **Queries** page that helps you build queries without having to write SQL. The visual **Query Editor** is combination of filters for tables (and the attributes within those tables) that are organized as a series of configurable drop-down menus and pick-lists that build SQL queries that run against the tables in your customer 360 database.

.. queries-visual-start

.. queries-visual-steps-start

The following sections describe how you can use the visual **Query Editor** to build queries.

.. queries-visual-steps-end

.. queries-visual-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Visual Query Editor.
          :align: left
          :class: no-scaled-link

     - The visual **Query Editor** is available on the **Queries** page. Click the **Create** button in the top right corner, and then choose visual **Query**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Use the customer 360 database.
          :align: left
          :class: no-scaled-link

     - You may use any table in any database to build a query.

       Your customer 360 database should already be selected for you (by default), though it is possible to have more than one 360 database available to the visual **Query Editor**. Expand each of the table rows to see the attributes that are available from that table. Open the **Data Explorer** to view detailed information about every table and every attribute, including examples of the values they contain.

       .. image:: ../../images/mockup-segments-tab-database-and-tables.png
          :width: 340 px
          :alt: Use your customer 360 database to build queries.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Build your query.
          :align: left
          :class: no-scaled-link

     - Start building your query by choosing an attribute from the selected table. The attributes that you choose to add to your query will depend on your goals and your use case.

       The example in this topic builds a list of customers who have opted out of receiving emails. Start building your query with the **Amperity ID** and **Email** attributes that are available in the **Merged Customers** table. Set the conditions for both of these columns to "is not NULL".

       .. image:: ../../images/mockup-queries-tab-visual-email-and-amperity-id.png
          :width: 600 px
          :alt: Start building your query.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Add attributes.
          :align: left
          :class: no-scaled-link
     - The next attribute you'll need is in a different table. Click **+ Add section** to add another group of attributes, choose the **Email Opt Status** table, add the **Amperity ID** and **Is Email Opted In** attributes, and then set the condition for **Amperity ID** to "is not NULL" and the condition for **Is Email Opted In** to "is false".

       .. image:: ../../images/mockup-queries-tab-visual-email-optin.png
          :width: 600 px
          :alt: Add more attributes to your query.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Run the query.
          :align: left
          :class: no-scaled-link
     - Click **Run Query** to run the query. The syntax for the attributes you added to the query are validated, after which the results are shown in the lower part of the visual **Query Editor**.

       The results will show you the matching records from the **Customer 360** table (by default). You can change the table from which matching records are shown. The **Show matching records from** option is located at the end of the visual query. In the same row you can click **Filter columns**, and then choose which attributes you want to see in the results.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Name your query.
          :align: left
          :class: no-scaled-link
     - Give your query a name a clear and understandable name. The name field is located in the upper left corner of the visual **Query Editor**.

       .. tip:: Use good naming patterns to ensure that you can always find your queries when you need them. Add details like "historical", "daily", or "test" as appropriate. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions.

          Some examples:

          * "Rolling_90_Days_Transactions"
          * "Top_10_Revenue"
          * "Socktown_Do_Not_Email"

          Prefix a query that is located in a folder with that folder name as often as possible. For example, if you have a folders named "Tableau" use query names like "Tableau_Rolling_90_Day_Transactions" for all queries that exist within that folder.

   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Save your query.
          :align: left
          :class: no-scaled-link
     - When you are done building your query, click the **Activate** button in the top right corner of the visual **Query Editor**.

.. queries-visual-callouts-end


.. _queries-visual-howitworks-and-vs-or:

AND vs. OR
==================================================

.. include:: ../../amperity_reference/source/segments.rst
   :start-after: .. segments-howitworks-and-vs-or-start
   :end-before: .. segments-howitworks-and-vs-or-end


.. _segments-howitworks-and-vs-or-context:

How AND vs. OR works
--------------------------------------------------

.. include:: ../../amperity_reference/source/segments.rst
   :start-after: .. segments-howitworks-and-vs-or-context-start
   :end-before: .. segments-howitworks-and-vs-or-context-end
