.. https://docs.amperity.com/amp360/


.. meta::
    :description lang=en:
        Return a list of customers who are early repeat purchasers.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of customers who are early repeat purchasers.

.. meta::
    :content class=swiftype name=title data-type=string:
        Early repeat purchasers

==================================================
Early repeat purchasers
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-early-repeat-purchasers-start
   :end-before: .. term-early-repeat-purchasers-end

.. include:: ../../amperity_reference/source/attribute_early_repeat_purchaser.rst
   :start-after: .. attribute-early-repeat-purchaser-start
   :end-before: .. attribute-early-repeat-purchaser-end

.. usecase-early-repeat-purchasers-howitworks-start

The following sections describe using the the visual **Query Editor** to build a query that returns a list of customers who are early repeat purchasers.

.. usecase-early-repeat-purchasers-howitworks-end

.. usecase-early-repeat-purchasers-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Visual Query Editor.
          :align: left
          :class: no-scaled-link

     - Open the visual **Query Editor**, look in the lower-right of the page and make sure your customer 360 database is selected.

       .. image:: ../../images/mockup-segments-tab-database-and-tables-small.png
          :width: 340 px
          :alt: Use your customer 360 database to build queries.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find early repeat purchasers.
          :align: left
          :class: no-scaled-link

     - To identify customers who have made an early repeat purchase, choose the **Amperity ID** and **Early Repeat Purchaser** attributes from the **Transaction Attributes Extended** table. Set the condition for **Amperity ID** to "is not NULL" and the condition for **Early Repeat Purchaser** to "is true":

       .. image:: ../../images/attribute-early-repeat-purchaser-example-visual-query.png
          :width: 540 px
          :alt: Find early repeat purchasers.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Run the query.
          :align: left
          :class: no-scaled-link

     - Run the query to validate the syntax, and then review the results.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: left
          :class: no-scaled-link
     - You're done! Give your query a name that clearly describes the purpose. For example: "Early Repeat Purchasers".

       Click the **Activate** button in the top right corner of the visual **Query Editor**. 

       .. tip:: Use the **Early Repeat Purchaser** attribute as a leading indicator for overall conversion rate of one-time buyers to repeat customers, even when it does not capture the total number of one-time buyers who have returned to purchase again.

.. usecase-early-repeat-purchasers-callouts-end
