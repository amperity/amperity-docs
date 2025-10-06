.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Return a list of customers who have purchased only one time.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of customers who have purchased only one time.

.. meta::
    :content class=swiftype name=title data-type=string:
        One and done

==================================================
One and done
==================================================

.. include:: ../../amperity_user/source/onetime_buyers.rst
   :start-after: .. onetime-buyers-about-start
   :end-before: .. onetime-buyers-about-end

.. include:: ../../amperity_reference/source/attribute_one_and_done.rst
   :start-after: .. attribute-one-and-done-start
   :end-before: .. attribute-one-and-done-end

.. usecase-one-and-done-howitworks-start

The following sections describe using the visual **Query Editor** to build a query that returns a list of customers who have purchased only one time.

.. usecase-one-and-done-howitworks-end

.. usecase-one-and-done-howitworks-callouts-start

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
          :alt: Find customers who have purchased only one time.
          :align: center
          :class: no-scaled-link

     - To identify which customers who have purchased only one time, choose the **Amperity ID** and **One and Done** attributes from the **Transaction Attributes Extended** table. Set the condition for **Amperity ID** to "is not NULL" and the condition for **One and Done** to "is true":

       .. image:: ../../images/attribute-one-and-done-example-visual-query.png
          :width: 540 px
          :alt: Find customers who have purchased only one time.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Run the query.
          :align: center
          :class: no-scaled-link

     - Run the query to validate the syntax, and then review the results.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done. Give your query a name that clearly describes the purpose. For example: "One and Done".

       Click the **Activate** button in the top right corner of the visual **Query Editor**. 

       .. important:: Amperity uses the range of data that is provided to it to identify one-time buyers. For example, if Amperity is provided data for the years 2015-2022, purchases made in 2014 are not used to identify one-time buyers.

.. usecase-one-and-done-callouts-end
