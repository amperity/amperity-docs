.. https://docs.amperity.com/user/

:orphan:


.. meta::
    :description lang=en:
        Use Presto SQL to build queries using the SQL or visual Query Editor.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use Presto SQL to build queries using the SQL or visual Query Editor.

.. meta::
    :content class=swiftype name=title data-type=string:
        Build queries

==================================================
Build queries
==================================================

.. queries-static-intro-start

Sending data from Amperity is a combination of three things: building a query, linking the results of that query to an orchestration that sends the results to a destination, and then monitoring the workflow to ensure that your data safely makes it downstream.

This is part one of a series of topics that describes how this works.

* Build queries using Presto SQL. A SELECT statement, along with standard clauses, operators, and functions, is all you need to return data that support any use case.
* An :doc:`orchestration <orchestrations>` connects the results of your query to a workflow that sends those results to its destination.
* A :doc:`workflow <workflows>` manages the process of sending that data to the selected destination.

  .. note:: Each workflow is monitored by Amperity. You may see notifications about the state of the workflow within the **Queries** and **Destinations** pages. Depending on the type of notification, you may be directed to a workflow actions page that will actively help you troubleshoot issues within that workflow.

.. queries-static-intro-end

.. queries-howitworks-start

The visual **Query Editor** is a user interface within the **Queries** page that helps you build queries without having to write SQL. The SQL **Query Editor** is a SQL interface in which you can support any use case by writing SELECT statements using Presto SQL.

.. queries-howitworks-end

.. queries-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link

     - The SQL **Query Editor** is available on the **Queries** page. Click the **Create** button in the top right corner, and then choose **SQL Query**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link

     - You may use any table in any database to build a query.

       Your customer 360 database should already be selected for you by default, though it is possible to have more than one 360 database available to the SQL **Query Editor**. Expand each of the table rows to see the attributes that are available from that table. Open the **Data Explorer** to view detailed information about every table and every attribute, including examples of the values they contain.

       .. image:: ../../images/mockup-segments-tab-database-and-tables.png
          :width: 340 px
          :alt: Use your customer 360 database to build queries.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link

     - Start building your query by writing a SELECT statement using Presto SQL that accesses the tables in your customer 360 database.

       The query that you build will depend on your goals and your use case.

       .. include:: ../../amperity_user/source/queries_reference.rst
          :start-after: .. queries-example-revenue-by-month-intro-start
          :end-before: .. queries-example-revenue-by-month-intro-end

       .. include:: ../../amperity_user/source/queries_reference.rst
          :start-after: .. queries-example-revenue-by-month-statement-start
          :end-before: .. queries-example-revenue-by-month-statement-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Click **Run Query** to run the query. The syntax for the attributes you added to the query are validated, after which the results are shown in the lower part of the SQL **Query Editor**.

       The results shows you a list of columns, one for each attribute that was returned by the query.

       In this example, four columns are returned: **order_month**, **top_20_revenue**, **total_month_revenue**, and **top_20_percent_revenue**. The results are similar to:

       ::

          ------- ------------- --------------- ----------
           month   revenue       total_revenue   percent
          ------- ------------- --------------- ----------
           1       52201487.51   144137695.60    0.362164
           2       50893203.32   142132298.13    0.358069
           3       41257843.42   121747802.99    0.338879
           4       43616719.20   126389526.45    0.345097
           5       75123545.83   188169441.30    0.399233
           6       37406903.31   112992544.71    0.331056
           7       40533591.78   120249271.98    0.337079
           8       41941599.44   123349972.21    0.340021
           9       44461258.48   128513319.04    0.345966
           10      48251130.38   136503680.65    0.353478
           11      96664540.49   225473807.02    0.428717
           12      301944067.23  498955371.34    0.605152
          ------- ------------- --------------- ----------


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Give your query a name a clear and understandable name. The name field is located in the upper left corner of the SQL **Query Editor**.

       .. tip:: Use good naming patterns to ensure that you can always find your queries when you need them. Add details like "historical", "daily", or "test" as appropriate. Be sure to include the brand name and the region name if you have multiple brands or have multiple regions.

          Some examples:

          * "Yearly_Revenue_by_Month"
          * "Analytics_Yearly_Revenue_by_Month"
          * "Domo_Yearly_Revenue_by_Month"

          Prefix a query that is located in a folder with that folder name as often as possible. For example, if you have a folders named "Tableau" use query names like "Tableau_Yearly_Revenue_by_Month" for all queries that exist within that folder.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Save your query.
          :align: center
          :class: no-scaled-link
     - When you are done building your query, click the **Activate** button in the top right corner of the SQL **Query Editor**.

.. queries-howitworks-callouts-end
