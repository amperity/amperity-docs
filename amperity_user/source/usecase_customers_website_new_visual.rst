.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Return a list of customers who placed their first website order within the previous 30 days.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of customers who placed their first website order within the previous 30 days.

.. meta::
    :content class=swiftype name=title data-type=string:
        New website customers

==================================================
New website customers
==================================================

.. include:: ../../amperity_user/source/usecase_customers_website_new.rst
   :start-after: .. usecase-customers-new-website-customers-start
   :end-before: .. usecase-customers-new-website-customers-end

.. usecase-customers-new-website-customers-howitworks-start

The following sections describe using the visual **Query Editor** to build a query that returns a list of customers who placed their first website order within the previous 30 days.

.. usecase-customers-new-website-customers-howitworks-end

.. usecase-customers-new-website-customers-howitworks-callouts-start

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
          :alt: Find customers whose first purchase was within the last 30 days.
          :align: center
          :class: no-scaled-link

     - To identify which customers have made their first purchase within the previous 30 days, choose the **Amperity ID** and **First Order Datetime** attributes from the **Transaction Attributes Extended** table. Set the condition for **Amperity ID** to "is not NULL" and the condition for **First Order Datetime** to "is after", and then configure a relative date range of "now - 30 days":

       .. image:: ../../images/attribute-first-order-datetime-last-30-days-visual-query.png
          :width: 540 px
          :alt: Find customers whose first purchase was within the last 30 days.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Find customers who have purchased from your website.
          :align: center
          :class: no-scaled-link

     - Add a second attribute to your query.

       To identify customers who have purchased from your website, choose the **First Order Purchase Channel** attribute from the **Transaction Attributes Extended** table, select the "is" operator, and then select "web":

       .. image:: ../../images/usecase-new-website-customers-combo-visual-query.png
          :width: 540 px
          :alt: Find customers who have purchased from your website.
          :align: left
          :class: no-scaled-link

       Keep the slider set to **AND**.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Run the query.
          :align: center
          :class: no-scaled-link

     - Run the query to validate the syntax, and then review the results.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done. Give your query a name that clearly describes the purpose. For example: "New Customers L30D Website".

       Click the **Activate** button in the top right corner of the visual **Query Editor**. 

       .. tip:: Use good naming patterns to ensure that you can always find your queries when you need them. Be sure to include the brand name and the region name if you have multiple brands or have multiple regions and want to build queries that are brand- or region-specific.

.. usecase-customers-new-website-customers-callouts-end
