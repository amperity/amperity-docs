.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building an audience of customers who have purchased only one time.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of customers who have purchased only one time.

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

The following sections describe using the **Segment Editor** to build a segment that returns a list of customers who have purchased only one time.

.. usecase-one-and-done-howitworks-end

**FIND ONE AND DONE CUSTOMERS**

.. usecase-one-and-done-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link

     - Open the **Segment Editor**, look in the lower-right of the page and make sure your customer 360 database is selected.

       .. image:: ../../images/mockup-segments-tab-database-and-tables-small.png
          :width: 340 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find customers who have purchased only one time.
          :align: center
          :class: no-scaled-link

     - To identify which customers who have purchased only one time, choose the **One and Done** attribute from the **Transaction Attributes Extended** table, and then select the "is true" operator:

       .. image:: ../../images/attribute-one-and-done-example.png
          :width: 540 px
          :alt: Find customers who have purchased only one time.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them could belong to a future campaign.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done. Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "One and Done".

       .. image:: ../../images/usecases-dialog-save-one-and-done.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. important:: Amperity uses the range of data that is provided to it to identify one-time buyers. For example, if Amperity is provided data for the years 2015-2022, purchases made in 2014 are not used to identify one-time buyers.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-one-and-done-callouts-end
