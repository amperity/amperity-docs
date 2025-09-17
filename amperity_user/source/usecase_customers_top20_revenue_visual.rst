.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Return your top-20 customers for revenue in the previous year.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return your top-20 customers for revenue in the previous year.

.. meta::
    :content class=swiftype name=title data-type=string:
        Top 20% revenue during previous year

==================================================
Top 20% revenue during previous year
==================================================

.. include:: ../../amperity_user/source/usecase_customers_top20_revenue.rst
   :start-after: .. usecase-customers-top-20-revenue-start
   :end-before: .. usecase-customers-top-20-revenue-end

.. usecase-customers-top-20-revenue-howitworks-start

The following sections describe using the visual **Query Editor** to build a query that returns a list of your top 20-percent customers for revenue in the previous year.

.. usecase-customers-top-20-revenue-howitworks-end

.. usecase-customers-top-20-revenue-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Visual Query Editor.
          :align: center
          :class: no-scaled-link

     - Open the visual **Query Editor**, look in the lower-right of the page and make sure your customer 360 database is selected.

       .. image:: ../../images/mockup-segments-tab-database-and-tables-small.png
          :width: 340 px
          :alt: Use your customer 360 database to build queries.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Who are your top 20% customers for revenue in the previous year?
          :align: center
          :class: no-scaled-link

     - To identify customers who are in your top 20-percent for revenue during the previous year, choose the **Amperity ID** and **L12M Monetary** attributes from the **Transaction Attributes Extended** table. Set the condition for **Amperity ID** to "is not NULL" and the condition for **L12M Monetary** to "is in list", and then select "9" and "10":

       .. image:: ../../images/attribute-rfm-monetary-top-20-visual-query.png
          :width: 540 px
          :alt: Who are your top 20-percent customers for revenue in the previous year?
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Run the query.
          :align: center
          :class: no-scaled-link

     - Run the query to validate the syntax, and then review the results.

       .. note:: RFM scores are split into ten percentile groups. The lowest percentile is 0 and the highest percentile is 10. Each percentile represents 10% of the customers who belong to that segment. When you select "9" and "10" together the results is the top 20 percent of your customers for revenue.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: left
          :class: no-scaled-link
     - You're done! Give your query a name that clearly describes the purpose. For example: "Top 20 Percent Customers During Previous Year".

       Click the **Activate** button in the top right corner of the visual **Query Editor**. 

       .. tip:: Use good naming patterns to ensure that you can always find your queries when you need them. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions and want to build queries that are brand- and/or region-specific.

.. usecase-customers-top-20-revenue-callouts-end
