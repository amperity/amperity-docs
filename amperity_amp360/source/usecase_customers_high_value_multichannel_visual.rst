.. https://docs.amperity.com/amp360/


.. meta::
    :description lang=en:
        Return a list of customers with a high lifetime value who have purchased across multiple channels.

.. meta::
    :content class=swiftype name=body data-type=text:
        Return a list of customers with a high lifetime value who have purchased across multiple channels.

.. meta::
    :content class=swiftype name=title data-type=string:
        High-value multichannel customers

==================================================
High-value multichannel customers
==================================================

.. include:: ../../amperity_ampiq/source/usecase_customers_high_value_multichannel.rst
   :start-after: .. usecase-customers-high-value-multi-channel-start
   :end-before: .. usecase-customers-high-value-multi-channel-end

.. usecase-customers-high-value-multi-channel-howitworks-start

The following sections describe using the the visual **Query Editor** to build a query that returns a list of customers with a high lifetime value who have purchased across multiple channels.

.. usecase-customers-high-value-multi-channel-howitworks-end

.. usecase-customers-high-value-multi-channel-howitworks-callouts-start

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
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find customers with a lifetime order revenue greater than $500.
          :align: left
          :class: no-scaled-link

     - To identify which customers have spent at least $500, choose the **Amperity ID** and **Lifetime Order Revenue** attributes from the **Transaction Attributes Extended** table. Set the condition for **Amperity ID** to "is not NULL" and the condition for **Lifetime Order Revenue** to "is greater than", and then configure a relative date range of "500":

       .. image:: ../../images/attribute-lifetime-order-revenue-greater-than-500-visual-query.png
          :width: 540 px
          :alt: Find customers with a lifetime order revenue greater than $500.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Find customers who have purchased across multiple channels.
          :align: left
          :class: no-scaled-link

     - Add a second attribute to your segment.

       To identify customers who have purchased from multiple channels, choose the **Multi Purchase Channel** attribute from the **Transaction Attributes Extended** table, and then select the "is true" operator:

       .. image:: ../../images/usecase-high-value-multi-channel-combo-visual-query.png
          :width: 540 px
          :alt: Find customers who have purchased across multiple channels.
          :align: left
          :class: no-scaled-link

       Keep the and/or slider set to **AND**.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Run the query.
          :align: left
          :class: no-scaled-link

     - Run the query to validate the syntax, and then review the list of customers who have spent at least $500 *and* have purchased from more than one channel.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Save your segment.
          :align: left
          :class: no-scaled-link
     - You're done! Give your query a name that clearly describes the purpose. For example: "High Value Multichannel Purchases".

       Click the **Activate** button in the top right corner of the visual **Query Editor**. 

       .. tip:: Use good naming patterns to ensure that you can always find your queries when you need them. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions and want to build queries that are brand- and/or region-specific.

.. usecase-customers-high-value-multi-channel-callouts-end
